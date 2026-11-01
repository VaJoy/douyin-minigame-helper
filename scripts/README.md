# scripts/

把抖音开放平台文档变成这个 SKILL 的工具链。所有脚本都可重复执行、带本地缓存、支持断点续跑。

## 依赖

```bash
python3 -m pip install beautifulsoup4 markdownify
```

## 执行顺序

```
crawl_pages.py      爬导航树 → docs/**/pages.json
      ↓
download_docs.py    按 pages.json 下正文 → docs/**/*.md
      ↓
normalize_docs.py   统一格式（标题层级 / 围栏语言 / front matter 空行）
      ↓
extract_api_index.py 从 API 文档生成 references/api-index.md
      ↓
check_refs.py       防幻觉校验：SKILL 里的每个 tt.* 必须真实存在
```

## 各脚本

### crawl_pages.py — 爬导航树

```bash
python3 scripts/crawl_pages.py --preset guide
python3 scripts/crawl_pages.py --preset develop
python3 scripts/crawl_pages.py --preset operation
python3 scripts/crawl_pages.py --preset all --refresh
```

内置三章共 12 个子章节的预设（`PRESETS` 常量），也可以临时指定：

```bash
python3 scripts/crawl_pages.py \
  --entry /zh-CN/mini-game/develop/framework/basic-function/web-assembly \
  --prefix /zh-CN/mini-game/develop/framework/ \
  --title 框架 --out /tmp/framework_pages.json
```

**原理**：站点的左侧导航是 SSR 进 HTML 的，但只渲染「当前页祖先链」的展开部分。所以对每个带展开图标的节点再抓一次它自己的页面，就能拿到下一级，BFS 走完整棵树。

### download_docs.py — 下正文

```bash
python3 scripts/download_docs.py --all --dry-run        # 只统计，不联网不写盘
python3 scripts/download_docs.py --all                  # 扫描 docs/**/pages.json
python3 scripts/download_docs.py --root docs/develop/api
python3 scripts/download_docs.py --root docs/operation/norms --limit 2 --out-root /tmp/try
python3 scripts/download_docs.py --all --overwrite --refresh
```

- 默认跳过已存在文件，可断点续跑；`--overwrite` 覆盖。
- **已归档到 `archive/` 的页面默认跳过**（防止 Unity/C# 文档被重新下回 `docs/`），`--include-archived` 可强制下载。
- 空正文的导航节点默认跳过，`--stub` 会写占位文件保持 1:1。
- 输出带 YAML 头：`title` / `source` / `update_time`（从页面内嵌 `updateTime` 时间戳转日期）。
- `--dry-run` 会打印「待下载 / 已存在 / 已归档」三个数，用来确认不会误伤。

### normalize_docs.py — 统一格式

```bash
python3 scripts/normalize_docs.py            # 预览
python3 scripts/normalize_docs.py --apply    # 写入
```

四条规则，幂等：

1. 删掉与 front matter `title` 重复的首个标题行；
2. 文档内最浅标题是 H1 时整体下移一级，保证 H1 只属于标题；
3. 代码围栏语言归一（`C#`→`csharp`、`JavaScript`→`js`、`Plain Text`→`text`、`sh`/`Shell`→`bash`）；
4. front matter 与正文之间统一留一个空行。

### extract_api_index.py — 生成 API 速查

```bash
python3 scripts/extract_api_index.py           # 重新生成 references/api-index.md
python3 scripts/extract_api_index.py --check   # 只比对是否过期（CI 可用）
```

头部「数据截至」取的是所有 API 文档里最新的 `update_time`，而不是运行当天 —— 这样 `--check` 跨天也不会误报。

只收 `tt.*` / `Class.method` / 两个全局函数，类说明与概念页列在文末「未收录」。

### check_refs.py — 防幻觉闸门

```bash
python3 scripts/check_refs.py
```

扫描 `SKILL.md`、`references/*.md`、`examples/*.js`，检查：

- 每个 `tt.xxx` 是否能被 docs 原文或 API 索引印证；
- 每个 `references/...`、`examples/...` 路径是否存在；
- 代码块是否可用：`json` 块必须能被 `json.loads` 解析，`js` 块过 `node --check`（没装 node 就跳过）。

## 已知的站点坑（改脚本前先看）

| 坑 | 表现 | 处理 |
|---|---|---|
| 导航只渲染祖先链 | 直接抓一页只能看到 9 个节点 | 对分组节点逐个抓取做 BFS |
| 两套正文版式 | 短文档 `div.markdown-body`，长协议 `div.doc-renderer-container` | `extract_markdown` 两种都兼容 |
| 伪列表 | `<ul class="list-bullet1~4">` + `span.bullet-serial`，不是真 `<li>` | 按 `list-bulletN` 重建嵌套列表 |
| 双层 `div.doc-line` 包装 | 只判 `find('ul')` 会把整张表格当列表项吃掉 | 要求 `ul` 是直接子节点，并先 unwrap 包装层 |
| 代码块 token 化 | highlight.js 把代码拆成大量 span，按行取会一字一行 | `get_text("")` 无分隔拼接 |
| 懒加载占位图 | `src="data:image/svg+xml,..."` 紧挨真图 | 删掉 `data:` 开头的 `<img>` |
| 版本声明位置不定 | 6 成在 `## 语法` 里，4 成在正文开头 | 全文搜索，别只看 intro |
| 页面无更新时间 | HTML 里只有 `"updateTime":"<10位时间戳>"` | 转成 `YYYY-MM-DD` 写进 front matter |

## 新增 reference 的约定

1. 头部固定三行：`> **适用**：…` / `> **源文档**：…` / `> **关联**：…`，正文从 `##` 起；
2. **可运行代码只放 `api-recipes.md`**，其他文件需要示例时给关键片段 + 指回 api-recipes，避免同一段代码两处维护；
3. 出现「数据截至」「共 N 项」这类数字时注明来源日期，方便判断是否过期；
4. 写完跑一遍 `check_refs.py`：新引用的 `tt.*` 必须能在 docs 里找到。

## 缓存

默认缓存到 `~/.cache/douyin-docs-helper/`（可用环境变量 `DY_DOC_CACHE` 改），一个 URL 一个 `.html`。要强制重抓用 `--refresh`，或直接删缓存目录。

## 注意

- 这些脚本抓的是**公开文档页**，不要用来抓需要登录的接口。
- 站点改版会让选择器失效，届时优先看 `common.py` 里的 `parse_sidebar`、`extract_markdown` 两处。
