---
title: "支付签名生成算法"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/payment-signature-generation-algorithm
update_time: 2024-07-24
---

**以[获取游戏币余额](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/acquire-mini-game-coin-balance)的接口为例**
### 原始请求信息

1. 支付密钥 `key: da8d182e1cashjkulkof6ae22a4a918457`
2. HTTP 请求方式: `POST`
3. 请求的 URI: `/api/apps/game/wallet/get_balance`
4. 请求参数

```json
{
"openid": "fge35vh5h3f2",
"appid": "tthdch45hd2df",
"zone_id": "1",
"mp_sig": "d1f0a41272f9b85618361323e1b19cd8cb0213f2",
"access_token": "hds2rt6bhgh5wfg5nf4gdh6",
"ts": 1507530737, // 时间戳，单位：秒
"pf": "android"
}
```
### 签名算法

1. 参与签名请求参数，注意与请求参数保持一致（**不同接口参与签名的参数不同，具体以各接口中请求参数为准，所有请求参数除了mp_sig以外都要参与签名生成**）

```json
{
"openid": "fge35vh5h3f2",
"appid": "tthdch45hd2df",
"zone_id": "1",
"access_token": "hds2rt6bhgh5wfg5nf4gdh6",
"ts": 1507530737, // 时间戳，单位：秒
"pf": "android"
}
```

2. 对参与签名的参数按照`key=value`的格式，并按照参数名 ASCII 字典序升序排序如下：

```js
stringA =
"access_token=hds2rt6bhgh5wfg5nf4gdh6&appid=tthdch45hd2df&openid=fge35vh5h3f2&pf=android&ts=1507530737&zone_id=1";
```

3. 拼接`uri`、`method`：（**不同接口uri不同，请注意自行替换**）

```text
stringB=stringA+"&org_loc=/api/apps/game/wallet/get_balance&method=POST"
```

4. 把支付密钥作为 key，使用 HMAC-SHA256 得到签名`sig=hmac_sha256(key,stringB)`。

```text
sig=hmac_sha256(key,stringB)
="4317496a530d0593fa4365ca87714a12c9e6edd4df1fea5fe1f5e5d6a1781a78"
```
### Bug & Tip

- Tip: **支付密钥** 不可跨小游戏使用，请确认使用的是当前小游戏的密钥。
- Tip: **支付密钥** 不是小游戏的 **AppSecret**，**支付密钥** 指的是 开发者后台->功能管理->支付->支付设置->签名密钥。 ![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/image-4076444411127746.5.png)
