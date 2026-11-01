---
name: douyin-minigame-helper
description: 抖音小游戏开发助手（Cocos + JavaScript）。当用户咨询抖音小游戏（minigame）的开发、接入、发布、变现、审核问题，或需要 tt.* API 用法、广告/支付/分享/排行榜接入、性能与包体优化、开发者工具使用时引用本技能。
agent_created: true
---

# 抖音小游戏开发助手

面向 **Cocos Creator + JavaScript** 的抖音小游戏知识库。所有结论来自抖音开放平台官方文档（同步于 2026-10-31，共 841 篇原文），已剔除 Unity / C# 内容。

## 何时用

- 要接抖音小游戏的某个能力（广告、支付、分享、排行榜、群聊、订阅消息、侧边栏复访）
- 查 `tt.*` API 的签名、参数、最低基础库、错误码
- 从 Cocos 导出的包跑不起来、白屏、方向不对、包体超限、掉帧
- 上线前的必接能力、资质备案、审核驳回
- 服务端对接（登录换 openid、支付回调、内容安全）

## 怎么用（重要）

**不要一次性读完所有文件。** 按下表定位 1-2 份，只读需要的：

| 用户问的是 | 读这个 |
|---|---|
| 从零跑通、导出、真机预览 | `references/quickstart.md` |
| `game.json` / `project.config.json` / 分包 / 版本兼容 | `references/config.md` |
| 没有 DOM、模块化、生命周期、Worker、文件系统 | `references/runtime.md` |
| 某个 `tt.xxx` 存不存在、什么版本、要不要授权 | `references/api-index.md`（**先 grep 再读**，见下） |
| 要能直接抄的代码（广告/登录/支付/分享/存储/音频） | `references/api-recipes.md` |
| 登录换 openid、UnionID、昵称头像、隐私授权 | `references/user-privacy.md` |
| 广告变现 | `references/ads.md` |
| 分享、邀请、排行榜、关注、群聊、开放数据域 | `references/social.md` |
| 内购、虚拟支付、掉单 | `references/payment.md` |
| 推荐流直玩、直播、小游戏站、PC、鸿蒙 | `references/live-platform.md` |
| 礼包/兑换码、手势识别、URL Link、添加到桌面 | `references/capability-extra.md` |
| 启动慢、包体大、掉帧、发热、内存 | `references/performance.md` |
| 代码加固、必接能力、资质备案、审核红线 | `references/security-release.md` |
| 服务端 API、access_token、code2session、支付回调 | `references/server.md` |
| 开发者工具、调试、彩蛋页、代码保护配置 | `references/devtools.md` |
| 后台数据看板、增长留存手段、结算激励 | `references/ops.md` |
| 要完整可运行的文件 | `examples/` |

路由不准时，先看下面「关键事实」找线索，再决定读哪份。

### 查 API 别整份读索引

`api-index.md` 有 500 多行，整份读约 1.2 万 token。绝大多数情况只需要一行：

```bash
grep "tt.createRewardedVideoAd" references/api-index.md
```

命中即可拿到「说明 / 最低基础库 / 授权要求 / 支持平台」；只有要按分类浏览（比如“媒体类都有哪些”）时才读整份。

## 硬约束

1. **不许编 API**。提到任何 `tt.*` 方法前，先确认它在 `references/api-index.md` 里；索引里没有的，去 `docs/develop/api/` 搜，搜不到就说文档未覆盖，不要猜签名。
2. **版本要说清**。API 有最低基础库要求（如 `tt.createInterstitialAd` 1.71.0、`tt.setGroupTag` 3.80.0）。给代码时提醒用 `tt.canIUse()` 判断，或比较 `tt.getSystemInfoSync().SDKVersion`。
3. **平台差异要点明**。iOS / Android / PC / 鸿蒙 行为不完全一致（广告的 onShow/onHide、PC 仅钻石支付、鸿蒙部分 API 缺失）。
4. **金额与结算只在服务端**。客户端不做任何结算、发币、签名逻辑；AppSecret 绝不进客户端。
5. **不引用第三方教程**。答案只基于本技能的 references 与 docs 原文。

## 关键事实速览

| 事实 | 值 |
|---|---|
| 运行环境 | 只有 JS，无 DOM/BOM，画布走 `tt.createCanvas()` |
| 三个必需文件 | `game.js` / `game.json` / `project.config.json` |
| 屏幕方向默认值 | **`landscape`**，竖屏游戏必须显式写 `portrait` |
| 首包大小限制 | 用分包 4MB / 不用分包 20MB |
| 广告形态 | 激励视频、Banner、插屏、游戏推荐组件 |
| 必接能力 | 侧边栏复访（全部）、客服（内购）、敏感词（有输入） |
| 登录 | `tt.login` 只给临时 code（3 分钟），openid 必须服务端换取 |
| access_token | 2 小时过期，重复获取会让旧 token 失效 |
| 支付场景 | 游戏币（`goodType` 0/1）、道具直购（`goodType` 2，需 3.47.0+） |
| 性能分档 | `deviceScore`：<7.3 低端 / 7.3–8.51 中端 / ≥8.51 高端，-1 视为中端 |

## 查原文

references 是浓缩版；需要精确参数、错误码全表、官方原文时查 `docs/`：

```bash
grep -rn "tt.createRewardedVideoAd" docs/develop/api/     # 找 API 原文
grep -rln "分包" docs/develop/guide/basic-function/       # 按关键词找文档
```

`docs/breadcrumb.md` 记录每个本地文件对应的官方线上地址，需要给用户链接时从这里取。

## 典型问答套路

**「我要接激励视频广告」** → 先读 `ads.md` 确认开通前提与形态差异 → 抄 `api-recipes.md` 第 2 节 → 提醒 `onClose` 里判断 `isEnded`、广告位要先在后台创建。

**「包体超了怎么办」** → 读 `performance.md` 的包体标准 → 看 `config.md` 的分包配置 → 给出「主包只留引擎与首场景」的具体拆法。

**「审核被打回」** → 读 `security-release.md` 的必接能力与驳回原因表 → 对照检查清单逐项确认 → 要原文时查 `docs/operation/norms/`。

**「这个 API 存在吗」** → 查 `api-index.md`；没有就 `grep docs/develop/api/`；仍没有就明确回答“官方文档未提供”。

**「两个小游戏怎么打通账号」** → 读 `user-privacy.md` 第一节：用 `unionid`，且只能在同一开发者的**小游戏之间**互通，跨抖音/极速版不行。
