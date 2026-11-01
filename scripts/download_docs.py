#!/usr/bin/env python3
"""按 pages.json 批量下载文档正文，转成带 YAML 头的 Markdown。

输出约定（与现有 docs/ 一致）：
    ---
    title: "..."
    source: https://developer.open-douyin.com/docs/resource/...
    update_time: 2025-10-29
    ---

    正文（标题从 ## 起）

用法
----
    python3 scripts/download_docs.py --all                  # 扫描 docs/**/pages.json
    python3 scripts/download_docs.py --all --dry-run        # 只统计，不联网不写盘
    python3 scripts/download_docs.py --root docs/develop/api
    python3 scripts/download_docs.py --root docs/operation/norms --limit 2 --out-root /tmp/try
    python3 scripts/download_docs.py --all --overwrite --refresh

行为约定：
- 已存在的文件默认跳过（可断点续跑），--overwrite 才覆盖；
- **已归档到 archive/ 的页面默认跳过**，避免把 Unity/C# 文档重新下回 docs/，
  --include-archived 可强制下载；
- 空正文的导航节点默认不写文件，--stub 会写占位以保持与 pages.json 1:1。
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402

STUB_TEXT = "_（此节点为导航分组，官方页面没有正文内容。）_"
ARCHIVE_DIR = common.REPO_ROOT / "archive"


def url_prefix_of(pages: list[dict]) -> str:
    """从一批页面路径里推出公共 URL 前缀（以 / 结尾）。"""
    if not pages:
        return ""
    common_prefix = os.path.commonprefix([p["path"] for p in pages])
    cut = common_prefix.rfind("/")
    return common_prefix[: cut + 1] if cut > 0 else common_prefix


def local_path(root: Path, path: str, prefix: str, strip_dash: bool) -> Path:
    rel = path[len(prefix):] if path.startswith(prefix) else path.lstrip("/")
    parts = [seg[1:] if strip_dash and seg.startswith("-") else seg for seg in rel.split("/")]
    return root.joinpath(*parts).with_suffix(".md")


def archived_twin(out: Path) -> Path | None:
    """若该文件在 archive/ 下有对应副本，返回那个路径。

    archive/ 镜像了 docs/ 的目录结构，用来存放刻意不纳入 SKILL 的文档（Unity / C#）。
    """
    try:
        rel = out.relative_to(common.DOCS_DIR)
    except ValueError:
        return None
    twin = ARCHIVE_DIR / rel
    return twin if twin.exists() else None


def render(title: str, url: str, update_time: str, body: str) -> str:
    head = ["---", f'title: "{title}"', f"source: {url}"]
    if update_time:
        head.append(f"update_time: {update_time}")
    head.append("---")
    return "\n".join(head) + "\n\n" + body + "\n"


def process(root: Path, pages_file: Path, args) -> dict:
    data = json.loads(pages_file.read_text(encoding="utf-8"))
    pages = data["pages"]
    prefix = url_prefix_of(pages)
    if args.out_root:
        root = Path(args.out_root)
    if args.limit:
        pages = pages[: args.limit]

    todo, existing, archived = [], 0, 0
    for page in pages:
        out = local_path(root, page["path"], prefix, args.strip_dash)
        if out.exists() and not args.overwrite:
            existing += 1
            continue
        if not args.include_archived and not args.out_root and archived_twin(out):
            archived += 1
            continue
        todo.append((page, out))

    stats = {"written": 0, "stub": 0, "failed": 0,
             "existing": existing, "archived": archived, "todo": len(todo)}

    if args.dry_run:
        print(f"  待下载 {len(todo)}  已存在 {existing}  已归档 {archived}")
        return stats

    if not todo:
        print(f"  无事可做：已存在 {existing}，已归档 {archived}  ({common.display_path(pages_file)})")
        return stats

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        htmls = list(pool.map(lambda p: _safe_fetch(p["path"], args.refresh),
                              [p for p, _ in todo]))

    for (page, out), html in zip(todo, htmls):
        if not html:
            stats["failed"] += 1
            print(f"  ! 抓取失败: {page['path']}", file=sys.stderr)
            continue
        title, body = common.extract_markdown(html)
        title = title or page["title"]
        if not body:
            if not args.stub:
                continue
            body, stats["stub"] = STUB_TEXT, stats["stub"] + 1
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(title, page["url"], common.extract_update_time(html), body),
                       encoding="utf-8")
        stats["written"] += 1

    print(f"  写入 {stats['written']}（占位 {stats['stub']}）  "
          f"跳过：已存在 {existing} / 已归档 {archived}  {common.display_path(pages_file)}")
    return stats


def _safe_fetch(path: str, refresh: bool = False) -> str:
    try:
        return common.fetch(path, refresh=refresh)
    except Exception as exc:  # noqa: BLE001
        print(f"  ! {exc}", file=sys.stderr)
        return ""


def main() -> None:
    ap = argparse.ArgumentParser(description="批量下载抖音小游戏文档正文")
    ap.add_argument("--root", help="章节目录，如 docs/develop/api")
    ap.add_argument("--pages", help="直接指定 pages.json")
    ap.add_argument("--all", action="store_true", help="扫描 docs 下所有 pages.json")
    ap.add_argument("--overwrite", action="store_true", help="覆盖已存在文件")
    ap.add_argument("--include-archived", action="store_true",
                    help="连 archive/ 里已有的文档也重新下载")
    ap.add_argument("--stub", action="store_true", help="为空正文的导航节点写占位文件")
    ap.add_argument("--no-strip-dash", dest="strip_dash", action="store_false",
                    help="保留路径里的前导横线（默认去掉，如 -retention -> retention）")
    ap.add_argument("--limit", type=int, help="每个 pages.json 只处理前 N 页（试跑）")
    ap.add_argument("--out-root", help="输出到别的目录（试跑用，不污染 docs/）")
    ap.add_argument("--dry-run", action="store_true", help="只统计，不联网不写盘")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--refresh", action="store_true", help="忽略本地缓存重新抓取")
    args = ap.parse_args()

    targets: list[tuple[Path, Path]] = []
    if args.all:
        targets = [(fp.parent, fp) for fp in sorted(common.DOCS_DIR.rglob("pages.json"))]
    elif args.pages:
        pf = Path(args.pages)
        targets.append((Path(args.root or pf.parent), pf))
    elif args.root:
        root = Path(args.root)
        if not root.is_absolute():
            root = common.REPO_ROOT / root
        pf = root / "pages.json"
        if not pf.exists():
            ap.error(f"{pf} 不存在")
        targets.append((root, pf))
    else:
        ap.error("请指定 --all / --root / --pages")

    total = {"written": 0, "stub": 0, "failed": 0, "existing": 0, "archived": 0, "todo": 0}
    for root, pf in targets:
        print(f"[{common.display_path(root)}]")
        s = process(root, pf, args)
        for k in total:
            total[k] += s[k]

    print(f"\n合计：写入 {total['written']}（占位 {total['stub']}），失败 {total['failed']}，"
          f"跳过 已存在 {total['existing']} / 已归档 {total['archived']}")
    if args.dry_run:
        print(f"（dry-run：实际会请求 {total['todo']} 个页面）")


if __name__ == "__main__":
    main()
