---
title: "开放数据校验与解密"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/user-info/open-data-check
update_time: 2025-09-11
---

### **开发者后台校验与解密开放数据**

抖音会对这些开放数据做签名和加密处理。开发者后台拿到开放数据后可以对数据进行签名校验和解密，来保证数据不被篡改。

签名校验以及数据加解密涉及用户的会话密钥 `session_key`。 开发者应该通过 [tt.login](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/log-in/tt-login) 登录流程后由服务端获取会话密钥 `session_key` 并保存在服务器。为了数据不被篡改，开发者不应该把 `session_key` 传到小游戏客户端等服务器外的环境。

## **数据签名校验**

为了确保开放接口返回用户数据的安全性，抖音会对明文数据进行签名。开发者可以根据业务需要对数据包进行签名校验，确保数据的完整性。

通过调用接口（如 [tt.getUserInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-api/info/tt-get-user-info) ）获取数据时，接口会同时返回 `rawData`、`signature`，其中 `sha1(`${rawData}${session_key}`)`。

开发者将 `signature`、`rawData` 发送到开发者服务器进行校验。服务器利用用户对应的 `session_key` 使用相同的算法计算出签名 `signature2` ，比对 `signature` 与 `signature2` 即可校验数据的完整性。

## **tt.getUserInfo**
### **数据校验示例**

**接口返回的 ****rawData****：**

```json
{
  "nickName": "ByteDancer",
  "gender": 1,
  "language": "zh_CN",
  "city": "Beijing",
  "province": "Beijing",
  "country": "CN",
  "avatarUrl": "https://example.com/avatar.jpg"
}
```

**用户的 session_key：**
`HyVFkGl5F5OQWJZZaNzBBg==`

**用于签名的字符串为：**

```json
{
  "nickName": "ByteDancer",
  "gender": 1,
  "language": "zh_CN",
  "city": "Beijing",
  "province": "Beijing",
  "country": "CN",
  "avatarUrl": "https://example.com/avatar.jpg"
}
```

**使用 sha1 得到的结果为：**
`cc346c352e2281865ba85198e0d7c74692d2434d` (此为示例 hash，实际会不同)

#### **加密数据解密算法**

接口如果涉及敏感数据（如 [相应参数](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/log-in/code-2-session#%E5%93%8D%E5%BA%94%E5%8F%82%E6%95%B0) 当中的 `unionId`），请求时需要带有code参数才会返回

#### **用户登录态签名**

部分服务端接口需要使用 `session_key` 进行用户身份校验，为了保持 `session_key` 私密性，接口不明文传输 `session_key`，而是通过校验登录态签名 `signature` 完成。

登录态签名的生成方式详见[用户登录态签名](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/log-in/user-login-sign)

### **set_user_storage的签名校验示例 **

详见[setUserStorage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/data-caching/set-user-storage)

#### **会话密钥 session_key 有效性**

开发者如果遇到因为 `session_key` 不正确而校验签名失败或解密失败，请关注下面几个与 `session_key` 有关的注意事项。

1. `tt.login` 调用时，用户的 `session_key` 可能会被更新而致使旧 `session_key` 失效（刷新机制存在最短周期，如果同一个用户短时间内多次调用 `tt.login`，并非每次调用都导致 `session_key` 刷新）。开发者应该在明确需要重新登录时才调用 `tt.login`，并及时通过服务端 `jscode2session` 接口更新服务器存储的 `session_key`。
1. 抖音不会把 `session_key` 的有效期告知开发者。我们会根据用户使用小游戏的行为对 `session_key` 进行续期。用户越频繁使用小游戏，`session_key` 有效期越长。
1. 开发者在 `session_key` 失效时，可以通过重新执行登录流程获取有效的 `session_key`。使用接口 `tt.checkSession` 可以校验 `session_key` 是否有效，从而避免小游戏反复执行登录流程。
1. 当开发者在实现自定义登录态时，可以考虑以 `session_key` 有效期作为自身登录态有效期，也可以实现自定义的时效性策略。

// event
{
// weRunData 的值已被替换为开放数据
"weRunData": {
"cloudID": "xxx",
"data": {
"stepInfoList": [
{
"step": 5000,
"timestamp": 1554814312,
}
],
"watermark": {
"appid": "wx1111111111",
"timestampe": 1554815786
}
},
"obj": {
// 非顶层字段维持原样
"shareInfo": "yyy",
}

{
"nickName": "Band",
"gender": 1,
"language": "zh_CN",
"city": "Guangzhou",
"province": "Guangdong",
"country": "CN",
"avatarUrl": "http://wx.qlogo.cn/mmopen/vi_32/1vZvI39NWFQ9XM4LtQpFrQJ1xlgZxx3w7bQxKARol6503Iuswjjn6nIGBiaycAjAtpujxyzYsrztuuICqIM5ibXQ/0"
}

{"nickName":"Band","gender":1,"language":"zh_CN","city":"Guangzhou","province":"Guangdong","country":"CN","avatarUrl":"http://wx.qlogo.cn/mmopen/vi_32/1vZvI39NWFQ9XM4LtQpFrQJ1xlgZxx3w7bQxKARol6503Iuswjjn6nIGBiaycAjAtpujxyzYsrztuuICqIM5ibXQ/0"}HyVFkGl5F5OQWJZZaNzBBg==

{"kv_list":[{"key":"score","value":"100"},{"key":"gold","value":"3000"}]}

75e81ceda165f4ffa64f4068af58c64b8f54b88c

**

282c0d87a489e3cf6cb58d93c747716563ed67fb13ba38c2433327097adbe02c

9hAb/NEYUlkaMBEsmFgzig==

{
"kv_list":[
{"key":"score","value":"100"},
{"key":"gold","value":"3000"}
]
}

// event
{
"weRunData": {
"cloudID": "xxx",
"errCode": -601006,
"errMsg": "cloudID expired."
},
// ...
}

{
"openId": "OPENID",
"nickName": "NICKNAME",
"gender": GENDER,
"city": "CITY",
"province": "PROVINCE",
"country": "COUNTRY",
"avatarUrl": "AVATARURL",
"unionId": "UNIONID",
"watermark":
{
"appid":"APPID",
"timestamp":TIMESTAMP
}

wx.cloud.callFunction({
name: 'myFunction',
data: {
weRunData: wx.cloud.CloudID('xxx'), // 这个 CloudID 值到云函数端会被替换
obj: {
shareInfo: wx.cloud.CloudID('yyy'), // 非顶层字段的 CloudID 不会被替换，会原样字符串展示
}
})

HyVFkGl5F5OQWJZZaNzBBg==
