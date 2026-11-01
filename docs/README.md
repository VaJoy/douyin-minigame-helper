# docs 说明

这里是从抖音开放平台抓下来的官方文档，供 `SKILL.md` 背后的 AI 检索原文用。

## 结构

三个大章节，共 12 个子章节，每个子章节一个目录：

| 大章节 | 子章节目录 | 官方页面清单 | 本地文档 |
|---|---|---|---|
| 快速入门 | `guide/` | 65 | 65 |
| 开发 | `develop/guide/` | 208 | 94 |
| | `develop/framework/` | 28 | 22 |
| | `develop/api/` | 695 | 483 |
| | `develop/dev-tools/` | 38 | 29 |
| | `develop/server/` | 62 | 45 |
| | `develop/basic-library/` | 2 | 2 |
| 运营 | `operation/user-ops/` | 31 | 31 |
| | `operation/about-data/` | 24 | 24 |
| | `operation/ability/` | 3 | 3 |
| | `operation/norms/` | 20 | 20 |
| | `operation/agreement-and-norms/` | 23 | 23 |

> 数字为 2026-11-01 快照，重算方法见文末。

## 三个东西的区别（最容易混淆）

| 名称 | 是什么 | 权威性 |
|---|---|---|
| `*/pages.json` | **官方导航树的全量快照**，含无正文的分组节点、也含已归档的 Unity/C# 页 | 反映官方结构，**不代表本地有什么** |
| `breadcrumb.md` | **本地实际存在的文档** ↔ 线上地址的映射 | 反映磁盘真实情况，查本地清单看它 |
| `archive/` | 刻意排除在 SKILL 之外的文档（Unity / C# / Godot，148 篇） | 不参与 SKILL，保留备查 |

所以 `docs/develop/api/pages.json` 写着 695 页，本地只有 483 篇，差值 212 = **80 篇已归档**（C# API）+ **132 个纯导航节点**（官方页面正文为空）。

全站对账：清单 **1199** = 本地 **841** + 纯导航节点 **210** + 已归档 **148**。

## 文档格式约定

每篇都是带 YAML 头的 Markdown：

```markdown
---
title: "接口调用凭证"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/...
update_time: 2025-10-29
---

## 正文标题（从 H2 起，H1 只属于文档标题）
```

- `title` / `source` 必有；`update_time` 官方没给就没有（只有 20 篇无正文的占位页缺）。
- 正文里所有站内链接都是绝对地址，可以直接点开。
- 代码围栏语言统一小写：`js` / `json` / `bash` / `csharp` / `text`。
- 官方页面里内嵌的富文本标签（`<p>` / `<span>` / `<h3>` 等）已清理成纯文字，正文不再有行内 HTML。
- 官方页面没有正文的导航节点，写的是占位文字（仅运营章节有此情况）。

## 怎么更新

```bash
python3 scripts/crawl_pages.py --preset all      # 1. 刷新官方页面清单
python3 scripts/download_docs.py --all --dry-run # 2. 先看会下多少（自动跳过归档）
python3 scripts/download_docs.py --all           # 3. 真正下载（已存在的跳过）
python3 scripts/normalize_docs.py --apply        # 4. 统一格式
python3 scripts/extract_api_index.py             # 5. 重建 API 索引
python3 scripts/check_refs.py                    # 6. 校验 SKILL 引用
```

## 重算上面的数字

```bash
# 本地文档数（不含 README / breadcrumb）
find docs -name '*.md' ! -name 'README.md' ! -name 'breadcrumb.md' | wc -l

# 归档数
find archive -name '*.md' | wc -l

# 各 pages.json 的清单条数合计
python3 -c "import json,glob;print(sum(json.load(open(f))['page_count'] for f in glob.glob('docs/**/pages.json',recursive=True)))"
```
