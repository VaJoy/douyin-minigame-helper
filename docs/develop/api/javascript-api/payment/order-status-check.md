---
title: "主动查询订单状态"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/order-status-check
update_time: 2026-03-09
---

> 服务端支付回调可能由于网络异常等原因导致无法 100%触达，开发者可以通过该接口主动回查订单状态，防止超发漏发。
根据 `access_token` 和自定义订单号 `orderno` 查询订单支付状态。
## 接口地址

```js
GET https://developer.toutiao.com/api/apps/game/payment/queryPayState
```

#### 输入

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| access_token | string | 是 | 小游戏 access_token，[获取方法](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token) |
| orderno | string | 是 | cp 自定义订单号，在下单的时候传入的，参考支付接口中的 customId |

#### 输出

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| status | string | 支付状态。success 表示支付成功且发币到账，unsuccess 表示支付失败或支付成功未发币到账 |
