# 抖音小游戏开发助手

> 把抖音开放平台的 841 篇官方文档，整理成一个 AI 能直接用的技能包（Skill），面向 **Cocos + JavaScript** 开发。
>
> A skill package for Douyin mini-game development (Cocos + JavaScript), distilled from 841 official docs.

---

## 为什么做这个

抖音小游戏的官方文档有 1000+ 页，散在「快速入门 / 开发 / 运营」三大章节、12 个子章节里。直接让 AI 读原文，要么读不完，要么读到的是一堆用不上的 Unity 内容。

这个仓库做了两件事：

1. **可检索**：841 篇正文按官方结构落地，带 YAML 头和线上地址映射，AI 可以精确 `grep`。
2. **可执行**：17 份主题速查 + 415 个 API 索引 + 4 个能直接跑的文件，把「怎么接」和「踩什么坑」提前写好了。

## 特点

- **分层，不硬塞**：`SKILL.md` 只做路由，按问题类型加载 1–2 份 `references/`，不会一次吃掉几万 token
- **可回溯**：每条结论都能在 `docs/` 找到原文，`docs/breadcrumb.md` 记录本地文件 ↔ 线上地址
- **防幻觉**：`scripts/check_refs.py` 会校验 SKILL 里出现的每个 `tt.*` 是否真实存在
- **能更新**：官方文档一变，跑一遍脚本即可重爬、重整、重校验
- **有边界**：只覆盖 Cocos + JS，Unity / C# / Godot 的 148 篇已归档到 `archive/`，不进检索范围

## 快速开始

对于支持 Agent Skills（`SKILL.md` + 按需加载）的工具，把整个目录放进 skills 目录即可，例如：

- WorkBuddy：`~/.workbuddy/skills/douyin-minigame-helper/`
- Claude Code：`~/.claude/skills/douyin-minigame-helper/`


之后直接问「抖音小游戏怎么接激励视频广告」、「如何接入抖音小游戏的类型声明文件」，它会自己按 `SKILL.md` 的路由表去查询。


## 目录结构

```
.
├── SKILL.md              # 入口：能力边界、路由表、硬约束、关键事实
├── references/           # 17 份主题速查（AI 按需加载）
│   ├── api-index.md      # 415 个 JS API 速查表
│   ├── api-recipes.md    # 8 个高频场景的可抄代码
│   └── ...
├── examples/             # 4 个完整可运行文件
├── docs/                 # 841 篇官方文档正文 + 页面清单 + 地址映射
├── archive/              # 148 篇 Unity / C# 文档（不参与 SKILL）
└── scripts/              # 抓取、转换、校验工具链
```

## 内容覆盖

| 文件 | 讲什么 |
|---|---|
| `references/quickstart.md` | 从注册到打包上传的完整路径 |
| `references/cocos-publish.md` | Cocos 构建面板、分包配置、开放数据域、发抖音包 |
| `references/config.md` | `game.json` / `project.config.json` / 分包 / 版本兼容 |
| `references/runtime.md` | 无 DOM 环境、模块化、生命周期、Worker、文件系统 |
| `references/api-index.md` | 415 个 `tt.*` 方法的存在性、最低基础库、授权、支持平台 |
| `references/api-recipes.md` | 登录、激励视频、分享邀请、支付、存储、音频、系统信息、侧边栏 |
| `references/user-privacy.md` | openid / unionid / 匿名 id、登录态、昵称头像授权、隐私合规 |
| `references/ads.md` | 激励视频 / Banner / 插屏 / 游戏推荐组件，错误码与红线 |
| `references/social.md` | 分享、邀请、排行榜、关注、群聊、开放数据域 |
| `references/payment.md` | 虚拟支付、道具直购、掉单处理 |
| `references/live-platform.md` | 推荐流直玩、直播、小游戏站、PC、鸿蒙 |
| `references/capability-extra.md` | 礼包兑换码、手势识别、URL Link、添加到桌面 |
| `references/performance.md` | 包体标准、启动优化、机型分档、内存 |
| `references/security-release.md` | 必接能力、代码加固、资质备案、审核红线 |
| `references/server.md` | access_token、code2session、支付回调、内容安全 |
| `references/devtools.md` | 开发者工具、调试、Lite 模式、TS 类型 |
| `references/ops.md` | 后台数据看板、增长留存、结算激励 |

`examples/` 里有 4 个自成体系的文件：激励视频管理、分享邀请、登录支付、侧边栏复访。

## 数据来源

- 全部内容来自 [抖音开放平台文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/overview)
- 抓取时间：2026-10-31；收录的 API 文档最新更新至 2026-08-06
- 规模：官方页面清单 1199 条 = 本地 841 篇 + 空节点 210 条 + 归档 148 篇

## 更新文档

官方改版后按顺序跑：

```bash
python3 -m pip install beautifulsoup4 markdownify

python3 scripts/crawl_pages.py --preset all       # 1. 刷新页面清单
python3 scripts/download_docs.py --all --dry-run  # 2. 先看会下多少（自动跳过归档）
python3 scripts/download_docs.py --all            # 3. 下载正文
python3 scripts/normalize_docs.py --apply         # 4. 统一格式
python3 scripts/extract_api_index.py              # 5. 重建 API 索引
python3 scripts/check_refs.py                     # 6. 校验引用没断
```

细节和站点坑见 [`scripts/README.md`](scripts/README.md)。

## 已知限制

- **只覆盖 Cocos + JavaScript**。Unity、C#、Godot 的内容归档在 `archive/`，SKILL 不引用。
- **图片是外链**。正文里的 858 张图指向字节的 CDN，长期可能失效。
- **官方文档本身有错**。例如「用户隐私保护」页的示例代码里混进了微信的 `wx.requirePrivacyAuthorize`，抖音只有 `tt.onNeedPrivacyAuthorization`。这类地方在 references 里做了标注。
- **不是实时同步**。数据有截止日期，新能力请查官方原文。

## 许可与免责

- **代码与原创内容**（`SKILL.md`、`references/`、`examples/`、`scripts/`）采用 [MIT License](LICENSE)。
- **`docs/` 与 `archive/`** 是抖音开放平台官方文档的镜像，**版权归原平台所有**，此处仅作检索与学习用途，不构成对原文的授权。如需商用或再分发这些文档，请遵守官方条款。
- 本项目为个人整理，**与字节跳动 / 抖音官方无关**，不代表官方立场。相关商标归各自所有者。

## 贡献

- 发现内容过时或有误 → 开 Issue，附上官方链接和日期
- 想补充主题 → 改 `references/`，记得跑 `python3 scripts/check_refs.py`
- 新增 reference 的写作约定见 [`scripts/README.md`](scripts/README.md#新增-reference-的约定)
