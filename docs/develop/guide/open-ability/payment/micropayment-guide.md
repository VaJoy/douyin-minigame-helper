---
title: "小额支付接入指引"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/payment/micropayment-guide
update_time: 2025-07-09
---

## 简介
该 Codelabs 将帮助开发者完成小游戏小额支付功能的接入，帮助开发者降低支付门槛，撬动账户有钻石余额用户支付能力，提升付费破冰效率。

### 能力介绍
「小额支付」是一种付费点设计和定价策略，能够通过降低支付门槛，撬动账户有钻石余额用户支付能力，提升付费破冰效率，对扩大游戏付费用户规模，提升游戏全生命周期内购GMV具有重要作用。
在实际应用中，小额支付大多与游戏原有的激励广告点位共同展示，用户可自选观看广告获得奖励，也可通过使用小额钻石跳过广告获得奖励，同时平台也支持开发者将小额支付与激励广告解耦，单独设计小额支付点位。

### 目标
线上小额支付示例：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/5061ab4b403441969bd5df6a96da725a~tplv-9nona0m7ha-image.image)

### 相关接口

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| [tt.requestGamePayment](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-request-game-payment) | JSAPI | 安卓发起支付JSAPI |
| [tt.openAwemeCustomerService](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-open-aweme-service) | JSAPI | iOS发起支付JSAPI |

说明：
- 由于小额支付依托的道具直购能力需在基础库版本3.47.0及以上可用，需使用`canIUse`来判断是否支持，其中安卓为`tt.canIUse('requestGamePayment.object.goodType')` iOS为`tt.canIUse('openAwemeCustomerService.object.goodType')`，处理后线上表现为基础库版本大于3.47.0可见小额支付，小于3.47.0不可见小额支付。
- 若游戏为Unity引擎，需额外注意以下几点：
  - 接口使用：TT.RequestGamePayment（安卓）和TT.openAwemeCustomerService(iOS)
  - BGDT升级TTSDK至6.0.8版本，若接入还是StarkSDK 6.0.0以下版本，可以参考[旧版StarkSdk API迁移TTSDK API说明文档_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/starksdk-migration-guide)
  - 接入判断条件CanIUse为`CanIUse.RequestGamePaymentParams.GoodType`

### 前提条件
- ios端使用前请确认参考[钻石兑换功能](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/virtual-payment/diamonds)完成钻石支付能力接入

### 学习内容
- 小额支付及其核心优势
- 如何设计小额支付
- 如何接入小额支付

## 设计小额支付
参考文档[小额支付--快速入门](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/virtual-payment/small-payment-guide)

## 接入小额支付
### 流程介绍
小额支付使用了道具直购能力，支持在游戏内直接使用钻石/现金兑换明确的游戏道具/权益直购的场景，无需进行游戏币转换。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/0ec20d9c69034b49a53335dcec919ab6~tplv-9nona0m7ha-image.image)

### 接入流程
接入步骤如下：
1. 小游戏前端调用 [tt.requestGamePayment](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-request-game-payment)(Android) / [tt.openAwemeCustomerService](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-open-aweme-service)(ios) 接口，生成小额支付订单，发起支付流程。
参数设置：

| 属性名 | 类型 | 必填 | 差异化说明 | 最低支持基础库版本 |
| --- | --- | --- | --- | --- |
| goodType | number | 是 | 本参数传2，同时 buyQuantity 字段不传 | 3.47.0 |
| orderAmount | number | 是 | 使用小额支付功能时，代表道具现金价格，单位为【分】，如价格为1钻，则回传10 | 3.47.0 |
| goodName | string | 否 | 道具名称，长度限制小于等于10个字符，用于区分道具类型，非必填 | 3.47.0 |

普通小游戏代码示例如下：

```js
if (tt.canIUse('requestGamePayment.object.goodType')) {
   // 道具直购
   tt.requestGamePayment({
      goodType: 2,
      orderAmount: 10，
      goodName: "道具名称"
      currencyType: "CNY",
      zoneId: "1",
      customId: "QWERTYUIDFxxxxx", 
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
} else {
    // 游戏币
    tt.requestGamePayment({
      mode: "game", // 支付类型
      env: 0, // 支付环境
      platform: "android", 
      currencyType: "CNY", // 币种：目前仅为 "CNY"
      buyQuantity: 600, // 购买数量，必须满足：金币数量*金币单价 = 限定价格等级（详见金币限定等级）
      zoneId: "1",
      customId: "QWERTYUIDFxxxxx", // 开发者自定义唯一订单号。如不填，支付结果回调将不包含此字段，将导致游戏开发者无法发放游戏道具, 基础库版本低于1.55.0没有此字段
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

Unity小游戏代码示例如下：

```typescript
if (!CanIUse.RequestGamePayment)
{
    return;
}
if (CanIUse.RequestGamePaymentParams.GoodType) {
    var orderAmount = int.Parse(inputPrice.text);
    var orderInfoParams = new Dictionary<string, object>();
    orderInfoParams["mode"] = "game";
    orderInfoParams["env"] = "0";
    orderInfoParams["currencyType"] = "CNY"; // 固定值: CNY。币种
    orderInfoParams["platform"] = "android";
    orderInfoParams["customId"] = (TimeUtils.GetCurrentTimeMs() / 1000).ToString();
    orderInfoParams["goodType"] = 2;
    orderInfoParams["orderAmount"] = orderAmount;
    orderInfoParams["goodName"] = "测试商品";
    
    TT.RequestGamePayment(
        orderInfoParams,
        () =>
        {
            PrintText("Pay Success " + orderInfoParams["customId"]);
        },
        (errCode, errMsg) =>
        {
            PrintText("Pay failed - errCode: " + errCode + ", errMsg: " + errMsg, true);
        }
    );
} else {
    var quantity = int.Parse(inputPrice.text);
    Dictionary<string, object> orderInfoParams = new Dictionary<string, object>();
    orderInfoParams["mode"] = "game";
    orderInfoParams["env"] = "0";
    orderInfoParams["currencyType"] = "CNY"; // 固定值: CNY。币种
    orderInfoParams["platform"] = "android";
    orderInfoParams["buyQuantity"] = quantity;
    orderInfoParams["customId"] = (TimeUtils.GetCurrentTimeMs() / 1000).ToString();
    
    TT.RequestGamePayment(
        orderInfoParams,
        () =>
        {
            PrintText("Pay Success " + orderInfoParams["customId"]);
        },
        (errCode, errMsg) =>
        {
            PrintText("Pay failed - errCode: " + errCode + ", errMsg: " + errMsg, true);
        }
    );
}
```

1. 获取支付结果，支付结果会发送给小游戏前端和小游戏服务端，开发者可通过以下方式对后续业务进行处理。
   1. 前端回调：小游戏可通过 tt.requestGamePayment / tt.openAwemeCustomerService 接口的 success 、fail、complete 参数设置不同支付结果的回调函数
   1. 小游戏服务端收到支付成功的服务端回调后，可通过 cp_orderno 或 cp_extra 判断是否为小额支付的回调。

## 总结
恭喜，你已经完成了小额支付接入教程。
你在该教程中了解了：
- 小额支付及其核心优势
- 如何接入小额支付
接下来，你可以将小额支付，应用于游戏内实际场景。

if (!CanIUse.RequestGamePayment)
{
return;
}
if (CanIUse.RequestGamePaymentParams.GoodType) {
var orderAmount = int.Parse(inputPrice.text);
var orderInfoParams = new Dictionary<string, object>();
orderInfoParams["mode"] = "game";
orderInfoParams["env"] = "0";
orderInfoParams["currencyType"] = "CNY"; // 固定值: CNY。币种
orderInfoParams["platform"] = "android";
orderInfoParams["customId"] = (TimeUtils.GetCurrentTimeMs() / 1000).ToString();
orderInfoParams["goodType"] = 2;
orderInfoParams["orderAmount"] = orderAmount;
orderInfoParams["goodName"] = "测试商品";

TT.RequestGamePayment(
orderInfoParams,
() =>
{
PrintText("Pay Success " + orderInfoParams["customId"]);
},
(errCode, errMsg) =>
{
PrintText("Pay failed - errCode: " + errCode + ", errMsg: " + errMsg, true);
}
);
} else {
var quantity = int.Parse(inputPrice.text);
Dictionary<string, object> orderInfoParams = new Dictionary<string, object>();
orderInfoParams["mode"] = "game";
orderInfoParams["env"] = "0";
orderInfoParams["currencyType"] = "CNY"; // 固定值: CNY。币种
orderInfoParams["platform"] = "android";
orderInfoParams["buyQuantity"] = quantity;
orderInfoParams["customId"] = (TimeUtils.GetCurrentTimeMs() / 1000).ToString();

TT.RequestGamePayment(
orderInfoParams,
() =>
{
PrintText("Pay Success " + orderInfoParams["customId"]);
},
(errCode, errMsg) =>
{
PrintText("Pay failed - errCode: " + errCode + ", errMsg: " + errMsg, true);
}
);
}

if (tt.canIUse('requestGamePayment.object.goodType')) {
// 道具直购
tt.requestGamePayment({
goodType: 2,
orderAmount: 10，
goodName: "道具名称"
currencyType: "CNY",
zoneId: "1",
customId: "QWERTYUIDFxxxxx",
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
} else {
// 游戏币
tt.requestGamePayment({
mode: "game", // 支付类型
env: 0, // 支付环境
platform: "android",
currencyType: "CNY", // 币种：目前仅为 "CNY"
buyQuantity: 600, // 购买数量，必须满足：金币数量*金币单价 = 限定价格等级（详见金币限定等级）
zoneId: "1",
customId: "QWERTYUIDFxxxxx", // 开发者自定义唯一订单号。如不填，支付结果回调将不包含此字段，将导致游戏开发者无法发放游戏道具, 基础库版本低于1.55.0没有此字段
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
