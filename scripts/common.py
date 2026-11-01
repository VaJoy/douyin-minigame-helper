#!/usr/bin/env python3
"""抖音开放平台文档工具链的公共部分。

包含：路径常量、带缓存的 HTTP 抓取、Markdown 正文提取。
所有脚本都从本文件导入，保证抓取行为和缓存策略一致。
"""
from __future__ import annotations

import os
import re
import time
import urllib.request
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify

# ---------------------------------------------------------------- 路径

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
DEFAULT_CACHE = Path(os.environ.get("DY_DOC_CACHE", Path.home() / ".cache" / "douyin-docs-helper"))

BASE = "https://developer.open-douyin.com"
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)
FOOTER_HINTS = ("该文档是否有帮助", "上一篇：", "下一篇：")
ZERO_WIDTH = "\u200b\u200c\u200d\ufeff"

def display_path(path) -> str:
    """尽量显示相对仓库根的路径，仓库外的就显示绝对路径。"""
    from pathlib import Path
    path = Path(path)
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


# ---------------------------------------------------------------- 抓取


def fetch(path: str, cache_dir: Path | None = None, refresh: bool = False) -> str:
    """按文档路径抓 HTML，本地缓存到 cache_dir。

    path 形如 /zh-CN/mini-game/develop/guide/...，会自动补 /docs/resource 前缀。
    """
    cache_dir = Path(cache_dir or DEFAULT_CACHE)
    key = path.strip("/").replace("/", "_") + ".html"
    fp = cache_dir / key

    if not refresh and fp.exists() and fp.stat().st_size > 5000:
        return fp.read_text(encoding="utf-8", errors="ignore")

    url = BASE + "/docs/resource" + path
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "zh-CN,zh;q=0.9"})

    last_err: Exception | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                html = resp.read().decode("utf-8", "ignore")
            cache_dir.mkdir(parents=True, exist_ok=True)
            fp.write_text(html, encoding="utf-8")
            return html
        except Exception as exc:  # noqa: BLE001
            last_err = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"抓取失败 {path}: {last_err}")


# ---------------------------------------------------------------- 解析

LI_RE = re.compile(r'<li id="([^"]+)"[^>]*>(.*?)</li>', re.S)
TITLE_RE = re.compile(r"aside-tree-node-title[^>]*>([^<]*)<")
ICON_RE = re.compile(r"semi-icon-tree_([a-z_]+)")


def parse_sidebar(html: str, prefix: str) -> list[tuple[str, str, int, bool]]:
    """解析 SSR 出来的侧边栏树，返回 [(path, title, depth, has_children)]。

    站点把导航树直接渲染进 HTML，但只渲染「当前页祖先链」的展开部分，
    所以需要逐层抓取分组页才能拿到完整树。depth 由缩进节点数量推断。
    """
    start = html.find("tree-options-list")
    if start < 0:
        return []
    seg = html[start - 200: start + 400_000]

    out = []
    for path, body in LI_RE.findall(seg):
        if not path.startswith(prefix):
            continue
        m = TITLE_RE.search(body)
        title = m.group(1).strip() if m else ""
        out.append((path, title, body.count("indent-unit-"), bool(ICON_RE.search(body))))
    return out


# ---------------------------------------------------------------- 正文提取

_BULLET_RE = re.compile(r"list-bullet(\d+)")


def _bullet_level(el) -> int | None:
    """判断是否是伪列表项，返回层级。

    站点用 <ul class="list-bullet1~4"> 伪造列表，外层还套了两层 div.doc-line。
    必须要求 ul 是直接子节点，否则外层包装 div 会被误判，整块内容被替换掉。
    """
    ul = el.find("ul", recursive=False) if getattr(el, "name", None) else None
    if ul is None:
        return None
    for cls in ul.get("class") or []:
        m = _BULLET_RE.match(cls)
        if m:
            return int(m.group(1))
    return None


def extract_markdown(html: str) -> tuple[str, str] | tuple[str, None]:
    """把文档页 HTML 转成 (title, markdown)。

    站点有两种版式：
      A) div.markdown-body，子节点是 头部(doc-lib-container) + 正文 + 页脚
      B) div.doc-lib-container > div.doc-renderer-container
    """
    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    title = clean_title(h1.get_text(" ", strip=True)) if h1 else ""

    body = soup.select_one("div.markdown-body")
    if body is not None:
        holder = soup.new_tag("div")
        for ch in list(body.find_all(recursive=False)):
            cls = set(ch.get("class") or [])
            if "doc-lib-container" in cls:
                continue
            if any(h in ch.get_text(" ", strip=True) for h in FOOTER_HINTS):
                continue
            holder.append(ch.extract())
    else:
        holder = soup.select_one("div.doc-renderer-container")

    if holder is None:
        return title, None

    for sel in ("script", "style", "noscript", "svg", "button"):
        for tag in holder.select(sel):
            tag.decompose()
    for img in holder.find_all("img"):
        if (img.get("src") or "").startswith("data:"):  # 懒加载占位图
            img.decompose()

    _unwrap_docline(holder)
    _rebuild_lists(holder, soup)
    _drop_empty_rows(holder)
    _shift_headings(holder)

    # 代码块先抽成占位符，避免被 markdownify 拆行；顺便还原语言标记
    code_blocks = []
    for pre in holder.find_all("pre"):
        code = pre.find("code")
        lang = ""
        if code is not None:
            for cls in code.get("class") or []:
                m = re.match(r"language-(\w+)", cls)
                if m:
                    lang = m.group(1)
        # 代码被 highlight.js 拆成大量 span，必须无分隔拼接
        text = (code or pre).get_text("").strip("\n")
        token = f"\n\n@@CODEBLOCK{len(code_blocks)}@@\n\n"
        code_blocks.append((token.strip(), lang, text))
        pre.replace_with(soup.new_string(token))

    for a in holder.find_all("a", href=True):
        href = a["href"]
        if href.startswith("/"):
            a["href"] = BASE + href
    for img in holder.find_all("img", src=True):
        src = img["src"]
        if src.startswith("//"):
            img["src"] = "https:" + src
        elif src.startswith("/"):
            img["src"] = BASE + src

    text = markdownify(str(holder), heading_style="ATX", bullets="-")
    for token, lang, code in code_blocks:
        text = text.replace(token, f"```{lang}\n{code}\n```")
    for ch in ZERO_WIDTH:
        text = text.replace(ch, "")
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return title, clean_inline_html(text)


def _unwrap_docline(holder) -> None:
    """剥掉只包着一个 div.doc-line 的包装层，让列表项成为兄弟节点。"""
    changed = True
    while changed:
        changed = False
        for el in holder.find_all("div"):
            if "doc-line" not in (el.get("class") or []):
                continue
            kids = [c for c in el.find_all(recursive=False) if getattr(c, "name", None)]
            if len(kids) == 1 and "doc-line" in (kids[0].get("class") or []):
                el.unwrap()
                changed = True
                break


def _rebuild_lists(container, soup) -> None:
    """把伪列表重建为真正的嵌套 <ul><li>。"""
    kids = [c for c in container.find_all(recursive=False) if getattr(c, "name", None)]
    i = 0
    while i < len(kids):
        if _bullet_level(kids[i]) is None:
            if kids[i].find(True) is not None:
                _rebuild_lists(kids[i], soup)
            i += 1
            continue

        seq = []
        while i < len(kids) and _bullet_level(kids[i]) is not None:
            seq.append((_bullet_level(kids[i]), kids[i]))
            i += 1

        root = soup.new_tag("ul")
        cur, prev, last_li = root, 0, None
        for level, el in seq:
            li = soup.new_tag("li")
            content = el.select_one(".bullet-list-content")
            if content is not None:
                for c in list(content.contents):
                    li.append(c.extract())
            else:
                li.append(el.get_text(" ", strip=True))
            if level > prev and last_li is not None:
                sub = soup.new_tag("ul")
                last_li.append(sub)
                cur = sub
            elif level < prev:
                for _ in range(prev - level):
                    up = cur.parent.parent if cur.parent and cur.parent.parent else None
                    if up is None or up.name != "ul":
                        break
                    cur = up
            cur.append(li)
            last_li, prev = li, level

        seq[-1][1].insert_after(root)
        for _, el in seq:
            el.decompose()


def _drop_empty_rows(holder) -> None:
    """删掉全空的表格行，否则会被当成表头。"""
    for tr in holder.find_all("tr"):
        cells = tr.find_all(["td", "th"], recursive=False)
        if cells and all(not c.get_text(strip=True) and not c.find("img") for c in cells):
            tr.decompose()


def _shift_headings(holder) -> None:
    """正文标题整体下移一级，保证 H1 只属于文档标题。

    必须从深到浅改，正序会级联把 H1 一路降成 H6。
    """
    levels = [len(h.name) - 1 for h in holder.find_all(re.compile(r"^h[1-6]$"))]
    if not levels or min(levels) != 1:
        return
    for lvl in range(5, 0, -1):
        for h in holder.find_all(f"h{lvl}"):
            h.name = f"h{min(lvl + 1, 6)}"
    for h in holder.find_all(re.compile(r"^h[1-6]$")):
        for tag in h.find_all(["strong", "b", "em", "i"]):
            tag.unwrap()


def extract_update_time(html: str) -> str:
    """从页面内嵌数据里取更新时间，返回 YYYY-MM-DD；取不到返回空串。"""
    m = re.search(r'"updateTime"\s*:\s*"?(\d{10})', html)
    if not m:
        return ""
    from datetime import datetime, timezone, timedelta
    ts = datetime.fromtimestamp(int(m.group(1)), tz=timezone(timedelta(hours=8)))
    return ts.strftime("%Y-%m-%d")


# 标签名后必须紧跟 ">" 或空白，避免把代码里的比较运算（如 a<bB）当成标签
_TAG_P = re.compile(r"</?p(?:\s[^>]*)?>")
_TAG_SPAN = re.compile(r"</?span(?:\s[^>]*)?>")
_TAG_H = re.compile(r"<h([1-6])(?:\s[^>]*)?>(.*?)</h\1>", re.S)
# 行内强调这类单字母标签只在成对出现时才拆，进一步降低误伤代码的概率
_TAG_PAIR = re.compile(r"<(strong|b|em|i|font|u|s)(?:\s[^>]*)?>(.*?)</\1>", re.S)


def clean_inline_html(md: str) -> str:
    """清掉 markdown 里残留的行内 HTML（站点富文本块），只保留文字。

    这类标签来自官方文档内嵌的富文本（形如 <p>文字</p>、<h3 level="3"><span style=...>），
    markdownify 会原样透传。清理时必须跳过 ``` 围栏，否则会误伤代码里的尖括号。
    """
    parts = re.split(r"(```.*?```)", md, flags=re.S)
    out = []
    for seg in parts:
        if seg.startswith("```"):
            out.append(seg)
            continue
        seg = _TAG_SPAN.sub("", seg)
        seg = _TAG_PAIR.sub(lambda m: m.group(2), seg)
        seg = _TAG_H.sub(lambda m: "#" * len(m.group(1)) + " " + m.group(2).strip(), seg)
        seg = _TAG_P.sub("\n\n", seg)
        out.append(seg)
    text = "".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip("\n")


def clean_title(text: str) -> str:
    """去掉标题尾部混进来的「收藏 / 我的收藏」。"""
    text = (text or "").replace("我的收藏", "").replace("收藏", "")
    return re.sub(r"\s+", " ", text).strip()
