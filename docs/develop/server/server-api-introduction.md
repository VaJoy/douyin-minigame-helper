---
title: "服务端API介绍"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/server-api-introduction
update_time: 2025-03-25
---

抖音小程序、小游戏给开发者提供了服务端使用的 HTTPS API 接口。
## access_token
access_token 是开发者调用服务端 API 的唯一凭证，开发者应该使用服务端 API 获取 access_token，并使用 access_token 调用其它服务端 API。
其中，access_token 最多**2 小时**即过期，重复获取 access_token 会导致上次 access_token 失效。为了平滑过渡，新老 access_token 在 **5 分钟**内都可使用。
## 请求参数格式说明
⁣⁣ 对于文档中提供的 GET 请求，无特殊要求。
⁣ 对于文档中提供的 POST 请求，body 中的参数应以 JSON 字符串形式写入。
⁣ 当以 JSON 传递数据时，需设置请求头`"content-type": "application/json"`。
## OpenAPI 列表

| 功能类型 | OpenAPI |
| --- | --- |
| 接口调用凭证 | [getAccessToken](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token) |
| 登录 | [code2Session](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/log-in/code-2-session) |
| 数据缓存 | [setUserStorage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/data-caching/set-user-storage) |
|  | [removeUserStorage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/data-caching/remove-user-storage) |
| 二维码 | [createQRCode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/qr-code/create-qr-code) |
| 其它 | [用户登录态签名](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/other/user-login-sign) |
| 订阅消息 | [发送订阅消息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/subscribe-notification/notify) |
