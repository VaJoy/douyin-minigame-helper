---
title: "能力接入介绍"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/payment/access-process
update_time: 2025-11-06
---

## 简介
该 Codelabs 将帮助开发者完成小游戏支付功能的接入，实现游戏内的商业化变现。
### 能力介绍
抖音小游戏支付能力是一套支持开发者在游戏内实现用户付费交易的完整解决方案，通过标准化接口与流程，帮助开发者构建安全、便捷的支付闭环。该能力支持 **道具直购** 与 **游戏币支付** 两种场景，用户可直接购买游戏道具或通过游戏币兑换道具，实现游戏内的商业化变现。
### **前提条件**
开始前请参考以下步骤完成支付功能开通。
1. 在[小游戏开发者后台](https://developer.open-douyin.com/)-【虚拟支付】查看能力，并申请开通（未满足开通条件时，请先按照说明补全资质认证）。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/291c369bb0d1439c9761193c8f544b93)

1. 请仔细阅读相关协议，并勾选同意协议。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1b74899203ea43e7bcbc6b053d960a42)

1. 开通收款商户，详细资料填写流程可参考[虚拟支付2.0接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/guaranteed-payment/guidelines)。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/64514493ddf94d7dbe513de27f51d1dc)

1. 确认结算账户信息并填写银行账号等相关信息。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/32d06c349ba945c7a833fdd198419843)

1. 设置游戏币兑换汇率（注意填写提交通过后将无法更改），设置服务端回调地址等，完成后提交申请，等待审核。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d754b9fc3f084a7a988cc64741972186)

1. 审核通过后即可使用支付 SDK 能力进行小游戏支付
### 学习内容
- 如何开通小游戏的支付能力
- 如何在道具直购场景和游戏币场景中接入支付能力
### 相关接口

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| [tt.requestGamePayment](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-request-game-payment) | JSAPI | Android发起支付JSAPI |
| [tt.openAwemeCustomerService](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-open-aweme-service) | JSAPI | iOS发起支付JSAPI |
| [服务端回调接口](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/payment-server-callback) | 回调 | 玩家支付完成后，字节服务端会将订单发送给小游戏服务端 |
| [主动查询订单状态](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/order-status-check) | OpenAPI | 未接收到回调时，开发者可以通过该接口主动回查订单状态 |
| [获取游戏币余额](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/acquire-mini-game-coin-balance) | OpenAPI | 开通小游戏支付后，如果需要查询某个用户的游戏币余额，此时可以通过调用获取游戏币余额接口获取用户余额。 |
| [游戏币扣除接口](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/mini-game-coin-deduction-interface) | OpenAPI | 可以调用该接口扣除某个用户的游戏币 |
| [游戏币赠送接口](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/mini-game-coin-gift-interface) | OpenAPI | 小游戏可设置一些场景任务给予玩家一定的游戏币奖励，如观看广告或者完成某些任务，此时可以通过调用游戏币赠送接口给玩家赠送游戏币。 |
| [支付签名算法](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/payment-signature-generation-algorithm) | 算法实现 | 为确保支付安全性，游戏币赠送接口，游戏币查询接口，扣除游戏币接口都需要传递支付签名字段 |

## 道具直购场景
> 道具直购功能需要抖音版本 >= 32.0.0。
### 流程介绍

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ac292c26859b4641ad83949e3ee988b9)

### 接入流程
1. 小游戏前端调用 [`tt.requestGamePayment`](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-request-game-payment)(Android) / [`tt.openAwemeCustomerService`](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-open-aweme-service)(iOS) 接口，生成订单调起小游戏收银台，发起支付流程。示例如下：

```js
// 使用 canIUse 判断是否支持使用道具直购功能
if (tt.canIUse('requestGamePayment.object.goodType')) {
   tt.requestGamePayment({
      goodType: 2, // 商品类型为道具直购
      orderAmount: 10， // 订单金额，单位人民币分
      goodName: "道具名称"
      currencyType: "CNY",
      zoneId: "1",
      customId: "QWERTYUIDFxxxxx", // 开发者自定义单号
      mode: "game", // 支付类型
      env: 0, // 支付环境
      platform: "android",
      extraInfo: "extraInfo",  // extraInfo为字符串格式，用户自定义额外信息,支付结果回调信息包含此字段，基础库版本低于1.55.0没有此字段
      success(res) {
        console.log("调用函数成功");
      },
      fail(res) {
        console.log("调用函数失败");
      },
      complete(res) {
        console.log("调用完成");
      },
    });
}
```

1. 获取支付结果，支付结果会发送给小游戏前端和字节服务端，**为减少掉单情况发生，建议开发者同时接入小游戏前端回调和服务端回调，同时把支付结果传递给小游戏服务端进行后续业务处理。**
  - 前端回调：小游戏可通过 `tt.requestGamePayment` / `tt.openAwemeCustomerService` 接口的 `success` 、`fail`、`complete` 参数设置不同支付结果的回调函数。
  - 服务端回调：需要提前设置服务端回调地址，参考[服务端回调接口](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/payment-server-callback)，设置成功后，字节服务端会将用户支付成功的订单发送给小游戏服务端，
  - 主动查询订单状态：**回调由于网络异常等原因无法 100%触达**，开发者可以使用[queryPayState](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/order-status-check)手动查询订单状态。
1. 当确认用户支付订单成功后，小游戏服务端发放游戏道具完成交易。如果支付时因为网络抖动等原因，未能确认订单支付状态，可以在重新查询订单状态或收到支付回调后补发道具。
## 游戏币支付场景
### 流程介绍

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/bd67876256c04acd8445570d6ccdc375)

### 接入流程
1. 小游戏前端调用 [`tt.requestGamePayment`](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-request-game-payment)(Android) / [`tt.openAwemeCustomerService`](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-open-aweme-service)(iOS) 接口，生成订单调起小收银台，发起支付流程。示例如下：

```js
tt.requestGamePayment({
  currencyType: "CNY",
  buyQuantity: 600, // 购买游戏币数量
  zoneId: "1",
  customId: "QWERTYUIDFxxxxx", //开发者自定义唯一订单号。如不填，支付结果回调将不包含此字段，将导致游戏开发者无法发放游戏道具, 基础库版本低于1.55.0没有此字段
  extraInfo: `{
    userId: "12xxx6",   //用户自定义额外信息,支付结果回调信息包含此字段， 基础库版本低于1.55.0没有此字段
    version: "v0.0.0",
    price: "30",
  }`,  //extraInfo要转成字符串
  success(res) {
    console.log("调用函数成功");
  },
  fail(res) {
    console.log("调用函数失败");
  },
  complete(res) {
    console.log("调用完成");
  },
});
```

1. 同道具直购步骤二。
1. 当确认用户支付订单成功后，小游戏服务端可使用[游戏币扣除接口](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/mini-game-coin-deduction-interface)进行游戏币扣除并发放游戏道具等，如果支付时因为网络抖动等原因，未能确认订单支付状态，可以在重新查询订单状态或收到支付回调后补发道具。
## 测试场景

| **方案** | **说明** | **图示** | **注意事项** |
| --- | --- | --- | --- |
| 在IDE中调用支付接口 | 在开发者工具中调用支付接口时，可验证接口传入参数有效性。 参数校验通过后模拟器将展示支付二维码，对应真机上表现为拉起收银台 |  | 此二维码只用作能力模拟，无法真实进行扫码支付 |
| 扫码/真机调试**（推荐）** | 完整测试支付链路，使用开发者工具中的【预览/真机调试】功能，扫码后可在真机上拉起收银台 |  | 目前暂不支持测试**沙盒环境**，在真机测试的过程中将使用**真实金额**进行支付，建议选择小额支付进行测试，大额场景检查收银台支付金额是否正确即可 测试版和预览版小游戏无需完成钻石支付签约，即可拉起钻石支付收银台；开发者可以完成测试后，再前往平台开通钻石支付签约。 用户在不同App端或系统支付时收银台样式存在差异，开发者无需关注 |

## 总结
恭喜，你已经完成了小游戏支付 Codelab，你在该接入文档中了解了：
- 如何开通小游戏的支付能力
- 如何在道具直购场景和游戏币场景接入支付能力
接下来，你可以将小游戏支付能力应用于实际场景。

#

// 使用 canIUse 判断是否支持使用道具直购功能
if (tt.canIUse('requestGamePayment.object.goodType')) {
tt.requestGamePayment({
goodType: 2, // 商品类型为道具直购
orderAmount: 10， // 订单金额，单位人民币分
goodName: "道具名称"
currencyType: "DIAMOND",
zoneId: "1",
customId: "QWERTYUIDFxxxxx", // 开发者自定义单号
mode: "game", // 支付类型
env: 0, // 支付环境
platform: "android",
extraInfo: "extraInfo",  // extraInfo为字符串格式，用户自定义额外信息,支付结果回调信息包含此字段，基础库版本低于1.55.0没有此字段
success(res) {
console.log("调用函数成功");
},
fail(res) {
console.log("调用函数失败");
},
complete(res) {
console.log("调用完成");
},
});
}

tt.requestGamePayment({
currencyType: "DIAMOND",
buyQuantity: 600, // 购买游戏币数量
zoneId: "1",
customId: "QWERTYUIDFxxxxx", //开发者自定义唯一订单号。如不填，支付结果回调将不包含此字段，将导致游戏开发者无法发放游戏道具, 基础库版本低于1.55.0没有此字段
extraInfo: `{
userId: "12xxx6",   //用户自定义额外信息,支付结果回调信息包含此字段， 基础库版本低于1.55.0没有此字段
version: "v0.0.0",
price: "30",
}`,  //extraInfo要转成字符串
success(res) {
console.log("调用函数成功");
},
fail(res) {
console.log("调用函数失败");
},
complete(res) {
console.log("调用完成");
},
});

道具直购功能需要抖音版本 >= 32.0.0。
