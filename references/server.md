# 服务端 OpenAPI

> **适用**：登录换 openid、支付回调、内容安全、消息推送等需要服务端的场景。
> **源文档**：`docs/develop/server/`（45 篇）、`docs/develop/api/javascript-api/payment/payment-server-callback.md`。
> **关联**：前端下单见 `payment.md`；AppSecret 安全见 `security-release.md`。

## 通用约定

- 网关域名：`https://minigame.zijieapi.com/mgplatform/api/...`（旧域名 `developer.toutiao.com` 仍可用，但建议换新）。
- 鉴权：除换取 token 的接口外，全部要带 `access-token` 请求头。
- POST 请求 body 用 JSON 字符串，头里必须带 `content-type: application/json`。
- 返回统一结构：`{"err_no":0,"err_msg":"","log_id":"..."}`，`err_no != 0` 即失败，`log_id` 提工单时要用。

## access_token

**唯一凭证，必须由服务端获取和保存，绝不下发客户端。**

| 要点 | 说明 |
|---|---|
| 有效期 | 2 小时 |
| 互斥 | **重复获取会让上一次的 token 失效** |
| 平滑期 | 新老 token 有 5 分钟并存，便于灰度切换 |
| 缓存 | 服务端全局缓存，加分布式锁防并发刷新 |

两个接口：

| 接口 | 地址 | 说明 |
|---|---|---|
| 稳定版 | `POST /mgplatform/api/apps/stable_token` | 推荐，普通/稳定两种模式 |
| 普通版 | `POST /mgplatform/api/apps/v2/token` | 传统方式，会顶掉旧 token |

刷新策略：缓存里存 `token + 过期时间`，提前 5-10 分钟异步刷新；刷新失败继续用旧 token，别直接清空。

## 登录链路

```
客户端 tt.login() → code
        ↓
服务端 GET /mgplatform/api/apps/jscode2session?appid=&secret=&code=
        ↓
openid + session_key（+ anonymous_openid）
```

要点：
- `code` / `anonymous_code` **只能用一次**，且 3 分钟过期；非匿名要 `code`，匿名要 `anonymous_code`。
- `session_key` 是会话密钥，**只能留在服务端**，绝不能回传客户端。
- 需要用 `check_session_key` 校验服务端保存的登录态是否过期。
- AppSecret 泄露等于账号被接管，只在服务端环境变量里存。

## 支付回调

### 配置

后台「商业化 → 虚拟支付 → 支付设置」填**服务器地址**和**回调 Token**（自定义，平台会存）。平台会先发 **GET + echostr** 做可达性验证，通过后才会推 **POST** 订单。

### 验证来源（必做）

拼 `token + timestamp + nonce + msg`，按字符串自然序排序，SHA1 得到 `signature`，与请求里的 `signature` 比对，一致才处理；验证阶段要把 `echostr` 原样返回。

### 发货原则

1. **幂等**：按 `customId` 去重，同一订单只发一次；
2. **先校验后发货**：金额、商品、openid 都要与本地订单核对；
3. **失败重试**：返回非成功会触发平台重推，接口要能承受重复请求；
4. **兜底**：回调不保证 100% 触达，配合客户端 `queryPayState` 与余额轮询补单。

## 内容安全

| 接口 | 地址 | 用途 |
|---|---|---|
| 文本检测 | `POST https://developer.toutiao.com/api/v2/tags/text/antidirt` | 昵称、聊天、签名等 UGC 文本 |
| 图片检测 | `POST https://developer.toutiao.com/api/v2/tags/image` | 用户上传图片 |

- 必接：游戏内只要有用户自定义输入，就要过敏感词（后台必接能力要求）。
- 检测是**异步/有成本**的，客户端先做本地词库粗筛，服务端做二次校验。

## 消息推送

- 订阅消息：用户授权后，服务端可在指定场景推送（如体力恢复、活动开启）。
- 客服消息：内购游戏必接，走「抖音 IM 客服」或「抖音客服平台」。
- 推送要用户先授权，授权态过期需重新拉起。

## 其他能力速查

| 能力 | 目录 |
|---|---|
| 二维码 / Link / Schema 跳转 | `qr-code/`、`link/`、`schema/` |
| 游戏礼包、发奖 | `game-group-tag/`、`receive-reward.md` |
| 排行榜数据、赛事上报 | `social-interaction/`、`microgame-competition-*` |
| 广告变现数据 | `advertising-monetization-data/` |
| 动态分享、群标签 | `dynamic-sharing/`、`game-group-tag/` |
| OpenAPI SDK | `sdk-overview.md`（多语言 SDK 封装） |

## 常见错误

| err_no | 含义 | 处理 |
|---|---|---|
| 28001003 | access_token 无效 | 重新获取；检查是否被别处刷新顶掉 |
| 40001 | 参数错误 | 检查必填项与类型 |
| — | `log_id` 404 / 超时 | 带上 `log_id` 提工单 |
