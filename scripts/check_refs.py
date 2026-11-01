#!/usr/bin/env python3
"""校验 SKILL 产物：API 引用是否真实存在、文件引用是否断链。

这是防幻觉闸门：references / SKILL.md / examples 里出现的每个 `tt.xxx`，
都必须能在 docs/ 原文里找到（或出现在 API 索引中）。找不到就说明是编的。

用法
----
    python3 scripts/check_refs.py
    python3 scripts/check_refs.py --strict   # 把占位符 tt.xxx 也算失败
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402

TT_RE = re.compile(r"\btt\.[A-Za-z0-9_]+")
FILE_RE = re.compile(r"`((?:references|examples|docs)/[\w./\u4e00-\u9fa5-]+)`")
PLACEHOLDERS = {"tt.xxx"}


def collect_allowed() -> set[str]:
    """docs 里出现过的所有 tt.* + API 索引里的方法名。"""
    allowed: set[str] = set()
    for path in common.DOCS_DIR.rglob("*.md"):
        allowed.update(TT_RE.findall(path.read_text(encoding="utf-8", errors="ignore")))
    index = common.REPO_ROOT / "references" / "api-index.md"
    if index.exists():
        allowed.update(re.findall(r"^\| `([^`]+)` \|", index.read_text(encoding="utf-8"), re.M))
    return allowed


CODE_BLOCK = re.compile(r"```(js|javascript|json)\n(.*?)```", re.S)


def check_code_blocks(text: str, rel: str) -> list[str]:
    """校验代码块：json 必须能解析，js 必须过 node --check（装了 node 才查）。"""
    issues = []
    has_node = shutil.which("node") is not None
    for i, m in enumerate(CODE_BLOCK.finditer(text), 1):
        lang, code = m.group(1), m.group(2)
        if lang == "json":
            try:
                json.loads(code)
            except Exception as exc:  # noqa: BLE001
                issues.append(f"{rel} 第 {i} 个 json 块不是合法 JSON: {exc}")
        elif has_node:
            with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as fp:
                fp.write(code)
                path = fp.name
            r = subprocess.run(["node", "--check", path], capture_output=True)
            if r.returncode != 0:
                first = r.stderr.decode("utf-8", "ignore").splitlines()[:1]
                issues.append(f"{rel} 第 {i} 个 js 块语法错误: {' '.join(first)}")
    return issues


def main() -> None:
    ap = argparse.ArgumentParser(description="校验 SKILL 里的 API 与文件引用")
    ap.add_argument("--strict", action="store_true", help="连占位符也判为失败")
    args = ap.parse_args()

    allowed = collect_allowed()

    targets = [common.REPO_ROOT / "SKILL.md"]
    targets += sorted((common.REPO_ROOT / "references").glob("*.md"))
    targets += sorted((common.REPO_ROOT / "examples").glob("*.js"))
    targets = [p for p in targets if p.exists()]

    bad_api: dict[str, set[str]] = {}
    bad_file: dict[str, set[str]] = {}
    total_api = 0

    for path in targets:
        text = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(common.REPO_ROOT))
        for name in TT_RE.findall(text):
            total_api += 1
            if name in allowed:
                continue
            if name in PLACEHOLDERS and not args.strict:
                continue
            bad_api.setdefault(name, set()).add(rel)
        for ref in FILE_RE.findall(text):
            if not (common.REPO_ROOT / ref).exists():
                bad_file.setdefault(ref, set()).add(rel)

    print(f"扫描 {len(targets)} 个文件，tt.* 引用 {total_api} 处")
    print(f"文档中不存在的 API：{len(bad_api)}")
    for name, files in sorted(bad_api.items()):
        print(f"  {name}  <- {', '.join(sorted(files))}")
    print(f"断链文件引用：{len(bad_file)}")
    for ref, files in sorted(bad_file.items()):
        print(f"  {ref}  <- {', '.join(sorted(files))}")

    code_issues: list[str] = []
    for path in targets:
        code_issues += check_code_blocks(path.read_text(encoding="utf-8"),
                                         str(path.relative_to(common.REPO_ROOT)))

    print(f"代码块问题：{len(code_issues)}")
    for issue in code_issues:
        print(f"  {issue}")

    sys.exit(1 if (bad_api or bad_file or code_issues) else 0)


if __name__ == "__main__":
    main()
