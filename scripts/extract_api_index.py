#!/usr/bin/env python3
"""从 API 文档抽取字段，生成 references/api-index.md。

抽什么：方法名、一句话说明、最低基础库、授权要求、支持平台。
抽不到就留「—」，不猜。

两个坑（都在代码里处理了）：
- 版本声明位置不固定：约 6 成写在 `## 语法` 小节，4 成在正文开头 → 必须全文搜索；
- 站点用伪列表（ul.list-bullet1~4）排版，说明文字取「版本句之后的第一段散文」。

用法
----
    python3 scripts/extract_api_index.py            # 重新生成
    python3 scripts/extract_api_index.py --check    # 只校验现有文件是否过期
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402

API_SUBDIR = "docs/develop/api/javascript-api"
OUT_FILE = "references/api-index.md"
PAGES_FILE = "docs/develop/api/pages.json"

VER = re.compile(r"基础库\s*([0-9]+(?:\.[0-9]+)*)\s*开始支持")
METHOD = re.compile(r"^(tt\.[A-Za-z0-9_]+|[A-Za-z][A-Za-z0-9_]*\.[A-Za-z0-9_]+)$")
GLOBALS = {"requestAnimationFrame", "cancelAnimationFrame"}
SKIP_START = ("```", "|", "!", "#", ">", "- ", "* ")


def section(body: str, name: str) -> str:
    """取某个小节的内容。

    标题级别不固定为 ##：格式归一后，原本写在富文本里的 ## 可能被降成 ###，
    所以从 2 级到 6 级都认，遇到同级或更浅的标题就结束。
    """
    m = re.search(rf"^#{{2,6}}\s+{name}\s*\n+(.+?)(?=\n#{{2,6}}\s|\Z)", body, re.S | re.M)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def norm_auth(text: str) -> str:
    if not text:
        return "—"
    if "无需用户授权" in text:
        return "无需"
    if "需要用户授权" in text:
        return "需用户"
    return text[:12]


def norm_platform(text: str) -> str:
    return text.replace("、", "/").replace(" ", "") or "—"


def clean_desc(text: str) -> str:
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*`#>]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    m = re.match(r"(.+?[。；;])", text)
    if m:
        text = m.group(1)
    text = text.rstrip("。；;").strip()
    if len(text) <= 46:
        return text
    cut = text[:45]
    if re.search(r"[A-Za-z0-9_.]$", cut) and " " in cut[-14:]:
        cut = cut[: cut.rfind(" ")]
    return cut.rstrip("，,、 ") + "…"


def parse(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    front, body = text[:end], text[end + 5:]
    mt = re.search(r'^title:\s*"?(.*?)"?\s*$', front, re.M)
    title = mt.group(1).strip() if mt else ""

    version = sync = desc = ""
    m = VER.search(body)
    if m:
        version = m.group(1)
        pos = m.end()
        line_end = body.find("\n", pos)
        rest = body[pos:line_end].strip("，,。 ")
        sync = "同步" if "同步" in rest else ("异步" if "异步" in rest else "")
        buf: list[str] = []
        for line in body[line_end + 1:].split("\n"):
            s = line.strip()
            if not s:
                if buf:
                    break
                continue
            if s.startswith(SKIP_START):
                break
            buf.append(s)
            if len("".join(buf)) > 90:
                break
        desc = re.sub(r"\s+", " ", "".join(buf)).strip()
        if "开始支持" in desc:
            desc = ""

    if not desc:
        for line in body.split("\n"):
            s = line.strip()
            if not s or s.startswith(SKIP_START) or "开始支持" in s:
                continue
            desc = s
            break

    return {
        "title": title,
        "version": version,
        "sync": sync,
        "desc": desc,
        "auth": norm_auth(section(body, "授权要求")),
        "platform": norm_platform(section(body, "支持平台")),
        "path": path,
    }


def load_categories() -> tuple[list[str], dict[str, str]]:
    import json
    pages = json.loads((common.REPO_ROOT / PAGES_FILE).read_text(encoding="utf-8"))["pages"]
    order: list[str] = []
    cat: dict[str, str] = {}
    for p in pages:
        if len(p["group"]) < 2:
            continue
        rel = p["path"].split("/zh-CN/mini-game/develop/api/javascript-api/", 1)[-1]
        cat[rel] = p["group"][1]
        if p["group"][1] not in order:
            order.append(p["group"][1])
    return order, cat


def latest_update(files) -> str:
    """取所有 API 文档里最新的 update_time。

    用它当「数据同步于」的日期，而不是生成当天 —— 否则跨天再跑 --check 必然报不一致。
    """
    best = ""
    for p in files:
        m = re.search(r"^update_time:\s*(\S+)", p.read_text(encoding="utf-8"), re.M)
        if m and m.group(1) > best:
            best = m.group(1)
    return best


def build() -> tuple[str, dict]:
    api_dir = common.REPO_ROOT / API_SUBDIR
    files = sorted(api_dir.rglob("*.md"))
    rows = [parse(p) for p in files]
    synced = latest_update(files)
    order, cat = load_categories()

    buckets: dict[str, list[dict]] = collections.OrderedDict((c, []) for c in order)
    skipped: list[str] = []
    seen: set[str] = set()

    for r in rows:
        rel = str(r["path"].relative_to(api_dir))
        key = rel[:-3]
        name = r["title"]
        keep = (bool(METHOD.match(name)) or name in GLOBALS) and name not in seen
        if not keep:
            skipped.append(name)
            continue
        seen.add(name)
        buckets.setdefault(cat.get(key, "其他"), []).append(r)

    total = sum(len(v) for v in buckets.values())
    out = [
        "# JavaScript API 速查\n",
        f"> **适用**：查 `tt.*`、实例方法与事件回调是否存在、最低基础库、授权要求、支持平台。"
        f"本表 **{total}** 项，数据截至 {synced or '未知'}；另有 {len(set(skipped))} 篇类说明与概念页未收录（见文末）。",
        f"> **源文档**：`docs/develop/api/javascript-api/`（{len(rows)} 篇官方 API 文档）。",
        "> **关联**：参数、返回值、错误码与完整示例回查 `docs/` 原文；可直接抄的代码见 `api-recipes.md`。\n",
        "低于表列版本的宿主上调用会失败，运行前用 `tt.canIUse('<方法名>')` 判断。"
        "表中每项只有一句话，定位到方法后请回原文看细节。\n",
    ]

    for c, items in buckets.items():
        if not items:
            continue
        items.sort(key=lambda x: x["title"])
        out.append(f"## {c}\n")
        out.append(f"_{len(items)} 项_\n")
        out.append("| 方法 | 说明 | 基础库 | 授权 | 平台 |")
        out.append("| --- | --- | --- | --- | --- |")
        for r in items:
            out.append(
                f'| `{r["title"]}` | {clean_desc(r["desc"]) or "—"} | '
                f'{r["version"] or "—"} | {r["auth"]} | {r["platform"]} |'
            )
        out.append("")

    if skipped:
        out.append("## 未收录的类与概念页\n")
        out.append("下列页面不是可调用方法，按需查原文：\n")
        out.append("、".join(f"`{s}`" for s in sorted(set(skipped))) + "\n")

    return "\n".join(out).rstrip() + "\n", {
        "total": total, "skipped": len(set(skipped)), "synced": synced}


def main() -> None:
    ap = argparse.ArgumentParser(description="生成 references/api-index.md")
    ap.add_argument("--check", action="store_true", help="只比对是否与现有文件一致")
    args = ap.parse_args()

    content, stat = build()
    out = common.REPO_ROOT / OUT_FILE

    if args.check:
        old = out.read_text(encoding="utf-8") if out.exists() else ""
        same = old == content
        print(f"当前索引 {stat['total']} 项，跳过 {stat['skipped']} 项，数据截至 {stat['synced']}；"
              f"与重新生成结果{'一致' if same else '不一致'}")
        sys.exit(0 if same else 1)

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    print(f"写入 {OUT_FILE}：{stat['total']} 项，跳过 {stat['skipped']} 项，数据截至 {stat['synced']}")


if __name__ == "__main__":
    main()
