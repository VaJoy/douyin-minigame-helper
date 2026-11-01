---
title: "用户登录态签名"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/log-in/user-login-sign
update_time: 2024-07-24
---

部分服务端 API 需要校验用户登录态签名。开发者在调用服务端 API 时，需提供以 session_key 为秘钥的签名，开发者需要先使用
[session_key 获取方法](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/server/log-in/code-2-session)接口获取用户登录态。
## 签名算法
签名算法 sig_method 指的是用户态签名的编码方法，目前仅支持 sig_method=hmac_sha256。
开发者生成签名的方法如下，其中 post_body 指的是 post 请求的 body 部分。
```js
crypto.createHmac("sha256", session_key).update(JSON.stringify(post_body)).digest("hex");
```
## 示例
假设开发者 post 请求的**body**部分为{"foo":"bar"}，**session_key**为"724edcafc423d167724edcbe"，则计算可得开发者签名为：
```
44b5092fa1c9adba03803239934d4958b8a1840adf0cee8d5e95c1cf5d495e0e
```
