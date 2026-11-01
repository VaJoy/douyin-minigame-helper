#!/usr/bin/env python3
"""统一 docs 下 Markdown 的格式（可重复执行，幂等）。

做三件事：
1. 删除正文里与 front matter `title` 完全重复的首个标题行；
2. 若文档内最浅标题是 H1，整体下移一级，保证 H1 只属于文档标题；
3. 代码围栏语言名归一为小写规范名（`C#`→`csharp`、`JavaScript`→`js`、`Plain Text`→`text`…）。

不改 front matter、不改链接、不改正文文字。

用法
----
    python3 scripts/normalize_docs.py            # 只看会改哪些
    python3 scripts/normalize_docs.py --apply    # 真正写入
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402

SKIP = {"README.md", "breadcrumb.md"}
HEADING = re.compile(r"^(#{1,6})(\s+)(.*)$")

LANG_MAP = {
    "js": "js", "javascript": "js",
    "c#": "csharp", "csharp": "csharp",
    "json": "json", "plain text": "text", "text": "text",
    "sh": "bash", "bash": "bash", "shell": "bash",
    "typescript": "typescript", "ts": "typescript",
    "sql": "sql", "python": "python", "py": "python",
    "java": "java", "css": "css", "go": "go",
    "xml": "xml", "http": "http", "ruby": "ruby", "php": "php",
    "nginx": "nginx", "kotlin": "kotlin", "c++": "cpp", "cpp": "cpp",
}


def norm(text: str) -> str:
    return text.replace("*", "").replace("`", "").strip()


def split_front(text: str) -> tuple[str | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    return text[: end + 5], text[end + 5:]


def process(path: Path, dry: bool = True) -> dict | None:
    src = path.read_text(encoding="utf-8")
    front, body = split_front(src)
    if front is None:
        return None

    m = re.search(r'^title:\s*"?(.*?)"?\s*$', front, re.M)
    title = norm(m.group(1)) if m else ""

    # 先清行内 HTML 再解析标题：<h1> 被清成 "# " 后必须参与层级统计，
    # 否则要跑第二遍才收敛。
    has_html = bool(re.search(r"</?(?:p|span|h[1-6]|strong|b|em|i|font|u|s)\b", body))
    original_body = body
    body = common.clean_inline_html(body)

    lines = body.split("\n")
    heads: list[tuple[int, int, str]] = []
    fence_ops: list[tuple[int, str]] = []
    in_fence = False

    for i, line in enumerate(lines):
        if line.startswith("```"):
            if not in_fence:
                in_fence = True
                info = line[3:].strip()
                canon = LANG_MAP.get(info.lower()) if info else None
                if canon and canon != info:
                    fence_ops.append((i, canon))
            else:
                in_fence = False
            continue
        if in_fence:
            continue
        hm = HEADING.match(line)
        if hm:
            heads.append((i, len(hm.group(1)), hm.group(3)))

    removed = None
    if heads and title and norm(heads[0][2]) == title:
        removed = heads.pop(0)[0]

    shift = 1 if heads and min(h[1] for h in heads) == 1 else 0
    needs_blank = bool(body.strip()) and original_body[:1] != "\n"
    if removed is None and shift == 0 and not fence_ops and not needs_blank and not has_html:
        return None

    out = list(lines)
    for i, lvl, txt in heads:
        if shift:
            out[i] = "#" * min(lvl + shift, 6) + " " + txt
    for i, canon in fence_ops:
        out[i] = "```" + canon
    if removed is not None:
        del out[removed]
        if removed < len(out) and out[removed].strip() == "":
            del out[removed]

    body_text = "\n".join(out)
    # front matter 与正文之间统一留一个空行（现有文档两种都有）
    if body_text.strip():
        body_text = "\n" + body_text.lstrip("\n")
    new = front + body_text
    if new == src:
        return None
    if not dry:
        path.write_text(new, encoding="utf-8")
    return {
        "dedup_title": removed is not None,
        "shift": shift,
        "fences": len(fence_ops),
        "front_blank": needs_blank,
        "html": has_html,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="统一 docs 下 Markdown 的格式")
    ap.add_argument("--apply", action="store_true", help="真正写入（默认只预览）")
    args = ap.parse_args()

    stat = collections.Counter()
    changed: list[tuple[Path, dict]] = []

    for path in sorted(common.DOCS_DIR.rglob("*.md")):
        if path.name in SKIP:
            continue
        r = process(path, dry=not args.apply)
        if not r:
            continue
        changed.append((path, r))
        stat["删除重复标题"] += r["dedup_title"]
        stat["标题下移一级"] += bool(r["shift"])
        stat["围栏语言变更"] += bool(r["fences"])
        stat["围栏行数"] += r["fences"]
        stat["front matter 空行"] += bool(r["front_blank"])
        stat["行内 HTML 清理"] += bool(r["html"])

    mode = "APPLIED" if args.apply else "DRY-RUN"
    print(f"{mode} 待改文件 {len(changed)}")
    for k, v in stat.items():
        print(f"  {k}: {v}")
    if not args.apply and changed:
        print("\n加 --apply 才会真正写入")


if __name__ == "__main__":
    main()
