#!/usr/bin/env python3
"""爬取章节导航树，生成 pages.json。

原理
----
文档站的左侧导航是服务端渲染进 HTML 的（`tree-options-list` 区域），但**只渲染当前页
所在祖先链的展开部分**。因此对每个「有子节点的分组节点」再抓一次它自己的页面，就能
拿到下一级子节点；对全树做 BFS 即可覆盖完整导航。

节点是否有子级：看 li 里有没有 `semi-icon-tree_triangle_*` 图标。
层级：数 `span.indent-unit-` 的个数。

用法
----
    python3 scripts/crawl_pages.py --preset guide
    python3 scripts/crawl_pages.py --preset develop
    python3 scripts/crawl_pages.py --preset operation

    # 临时爬一个子树
    python3 scripts/crawl_pages.py \
        --entry /zh-CN/mini-game/develop/framework/basic-function/web-assembly \
        --prefix /zh-CN/mini-game/develop/framework/ \
        --title 框架 --out /tmp/framework_pages.json
"""
from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402

BASE = common.BASE

PRESETS: dict[str, list[dict]] = {
    "guide": [
        dict(slug=None, title="快速入门",
             entry="/zh-CN/mini-game/guide/overview",
             prefix="/zh-CN/mini-game/guide/",
             out="docs/guide/pages.json"),
    ],
    "develop": [
        dict(slug="guide", title="指南",
             entry="/zh-CN/mini-game/develop/guide/dev-guide/bytedance-mini-game",
             prefix="/zh-CN/mini-game/develop/guide/",
             out="docs/develop/guide/pages.json"),
        dict(slug="framework", title="框架",
             entry="/zh-CN/mini-game/develop/framework/basic-function/web-assembly",
             prefix="/zh-CN/mini-game/develop/framework/",
             out="docs/develop/framework/pages.json"),
        dict(slug="api", title="API",
             entry="/zh-CN/mini-game/develop/api/javascript-api/overview",
             prefix="/zh-CN/mini-game/develop/api/",
             out="docs/develop/api/pages.json"),
        dict(slug="dev-tools", title="开发工具",
             entry="/zh-CN/mini-game/develop/dev-tools/mini-app-developer-instrument",
             prefix="/zh-CN/mini-game/develop/dev-tools/",
             out="docs/develop/dev-tools/pages.json"),
        dict(slug="server", title="服务端OpenAPI",
             entry="/zh-CN/mini-game/develop/server/server-api-introduction",
             prefix="/zh-CN/mini-game/develop/server/",
             out="docs/develop/server/pages.json"),
        dict(slug="basic-library", title="最近更新",
             entry="/zh-CN/mini-game/develop/basic-library/update-log",
             prefix="/zh-CN/mini-game/develop/basic-library/",
             out="docs/develop/basic-library/pages.json"),
    ],
    "operation": [
        dict(slug="user-ops", title="用户运营",
             entry="/zh-CN/mini-game/operation1/user-ops/game-management/workbench-function-introduction",
             prefix="/zh-CN/mini-game/operation1/user-ops/",
             out="docs/operation/user-ops/pages.json"),
        dict(slug="about-data", title="数据分析",
             entry="/zh-CN/mini-game/operation1/about-data/data-intro/intro",
             prefix="/zh-CN/mini-game/operation1/about-data/",
             out="docs/operation/about-data/pages.json"),
        dict(slug="ability", title="平台能力",
             entry="/zh-CN/mini-game/operation1/ability/incentive/guidelines",
             prefix="/zh-CN/mini-game/operation1/ability/",
             out="docs/operation/ability/pages.json"),
        dict(slug="norms", title="运营规范",
             entry="/zh-CN/mini-game/operation1/norms/introduction",
             prefix="/zh-CN/mini-game/operation1/norms/",
             out="docs/operation/norms/pages.json"),
        dict(slug="agreement-and-norms", title="服务协议",
             entry="/zh-CN/mini-game/operation1/agreement-and-norms/agreement",
             prefix="/zh-CN/mini-game/operation1/agreement-and-norms/",
             out="docs/operation/agreement-and-norms/pages.json"),
    ],
}


def crawl(entry: str, prefix: str, title: str, workers: int = 6,
          verbose: bool = True, refresh: bool = False) -> dict:
    """从入口页 BFS 出整棵子树，返回 pages.json 结构。"""
    nodes: dict[str, dict] = {}
    fetched: set[str] = set()
    queue = [entry]

    while queue:
        batch = [p for p in queue if p not in fetched]
        queue = []
        if not batch:
            break
        if verbose:
            print(f"  抓取 {len(batch)} 页", flush=True)

        with ThreadPoolExecutor(max_workers=workers) as pool:
            htmls = list(pool.map(partial(common.fetch, refresh=refresh), batch))

        for path, html in zip(batch, htmls):
            fetched.add(path)
            tree = common.parse_sidebar(html, prefix)
            if not tree:
                print(f"  ! 无导航树: {path}", file=sys.stderr)
                continue
            stack: list[tuple[int, str]] = []
            for p, t, depth, has_children in tree:
                while stack and stack[-1][0] >= depth:
                    stack.pop()
                parent = stack[-1][1] if stack else None
                stack.append((depth, p))
                nodes.setdefault(p, {"title": t, "parent": parent})
                if has_children and p not in fetched and p not in queue:
                    queue.append(p)
        # 保序去重
        seen: set[str] = set()
        queue = [p for p in queue if not (p in seen or seen.add(p))]

    children: dict[str | None, list[str]] = {}
    for p, info in nodes.items():
        children.setdefault(info["parent"], []).append(p)

    order: list[str] = []

    def dfs(parent: str | None) -> None:
        for p in children.get(parent, []):
            order.append(p)
            dfs(p)

    dfs(None)

    pages = []
    for p in order:
        chain, cur = [], p
        while cur is not None and cur in nodes:
            chain.append(nodes[cur]["title"])
            cur = nodes[cur]["parent"]
        chain.reverse()
        pages.append({
            "title": nodes[p]["title"],
            "path": p,
            "url": BASE + "/docs/resource" + p,
            "group": chain,
        })

    return {
        "chapter_url": BASE + "/docs/resource" + entry,
        "chapter_title": title,
        "page_count": len(pages),
        "pages": pages,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="爬取抖音开放平台文档导航树")
    ap.add_argument("--preset", choices=sorted(PRESETS) + ["all"], help="内置章节预设")
    ap.add_argument("--entry", help="入口页路径（与 --prefix/--title/--out 一起用）")
    ap.add_argument("--prefix", help="只保留该前缀下的节点")
    ap.add_argument("--title", help="章节标题")
    ap.add_argument("--out", help="输出文件")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--refresh", action="store_true", help="忽略本地缓存重新抓取")
    args = ap.parse_args()

    jobs: list[dict] = []
    if args.preset:
        if args.preset == "all":
            for cfg in PRESETS.values():
                jobs.extend(cfg)
        else:
            jobs = PRESETS[args.preset]
    elif args.entry:
        if not (args.prefix and args.title and args.out):
            ap.error("自定义爬取需要同时提供 --prefix --title --out")
        jobs = [dict(entry=args.entry, prefix=args.prefix, title=args.title, out=args.out)]
    else:
        ap.error("请指定 --preset 或 --entry")

    for job in jobs:
        print(f"[{job['title']}] {job['prefix']}")
        data = crawl(job["entry"], job["prefix"], job["title"],
                     workers=args.workers, refresh=args.refresh)
        out = Path(job["out"])
        if not out.is_absolute():
            out = common.REPO_ROOT / out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"  -> {data['page_count']} 页  {common.display_path(out)}")


if __name__ == "__main__":
    main()
