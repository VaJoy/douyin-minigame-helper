---
title: "tt.requestGamePayment"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/tt-request-game-payment
update_time: 2026-03-19
---

> 基础库 1.0.0 开始支持本方法，这是一个异步方法。
发起支付

| 前提条件 | 使用前请参考[支付能力接入介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/payment/access-process)完成接入 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | •调用该方法时，需要保证用户已经[登录](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/log-in/tt-login/)。开发者需调用[tt.checkSession](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/log-in/tt-check-session)检测用户登录状态，以避免用户未登录时支付订单导致无法关联登录账户。 •异常情况下，充值有可能存在游戏币延迟到账问题，建议游戏在收到支付结果回调后，向服务端轮询最新游戏币余额，间隔 3 秒，持续约 1 分钟，可以根据返回值的 save_amt 的变化来确定是否充值成功。 同时也存在一些异常情况，导致充值成功后结果回调失败，因此建议游戏在启用游戏时主动[查询游戏币余额](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/acquire-mini-game-coin-balance)，并且提供给用户主动刷新余额的功能。（不要将查询余额作为进入游戏的必要条件，查询失败时，可在显示余额的界面显示异常，不要拒绝用户进入游戏，更不要直接显示 0） 强烈建议请求中填入 customId 和 extraInfo 字段（字段意义见下方表格），如果未填，支付结果回调将不包含游戏开发者的订单号，导致开发者无法确定回调是对应哪个订单，从而影响游戏道具发放。如果遇到此类问题，开发者可调用[queryPayState 接口](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/order-status-check)进行订单状态确认。 |
| 注意事项 | pc 端，仅支持钻石支付 |
| 相关教程 | 无 |

## 语法

```js
tt.requestGamePayment(options)
```

## 参数说明
options 为 object 类型，属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| mode | string |  | 是 | 支付的类型，枚举值 game - 表示购买游戏币，目前仅支持该类型 | 1.0.0 |
| env | number | 0 | 是 | 环境配置，枚举值 0 - 表示支付正式环境，目前仅支持该类型 | 1.0.0 |
| currencyType | string |  | 是 | 币种，枚举值 CNY - 表示人民币，目前仅支持该类型 注意：如果要感知用户实际的支付币种类型，请以[服务端支付结果回调](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/payment-server-callback)中回调结构体中的currency为准 | 1.0.0 |
| platform | string |  | 是 | 申请接入时的平台 android - 安卓 windows（可选）-pc 端 | 1.0.0 |
| buyQuantity | number |  | 否 | 金币购买数量，金币数量必须满足：**金币数量*金币单价 = 限定价格等级**（详见下方 **buyQuantity 说明**部分。开发者可以在字节小游戏平台的“支付”tab 设置游戏币单价） 注意：goodType为游戏币场景时必传，其他场景不传 | 1.0.0 |
| zoneId | string | 1 | 否 | 游戏服务区 id，开发者自定义。游戏不分大区则默认填写"1"。如果应用支持多角色，则角色 ID 接在分区 ID 后，用"_"连接 | 1.0.0 |
| customId | string |  | 是 | 游戏开发者自定义的唯一订单号，订单支付成功后通过[服务端支付结果回调](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/payment-server-callback)回传。必须具有唯一性，如果不传或重复传相同值，则会报错。 | 1.55.0 |
| extraInfo | string |  | 否 | 游戏开发者自定义的其他信息，订单支付成功后通过[服务端支付结果回调](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/payment-server-callback)回传。字符串长度最大不能超过 256。 | 1.55.0 |
| goodType | number | 0 | 否 | 支付场景，详见下方** goodType 说明** | 3.47.0 |
| orderAmount | number |  | 否 | goodType为道具直购场景时必传，代表道具现金价格，单位为【分】 如道具价格为0.1元，则回传10 | 3.47.0 |
| goodName | string |  | 否 | goodType为道具直购场景时，代表道具名称，长度限制小于等于10个字符，用于区分道具类型 | 3.47.0 |
| success | function |  | 否 | 接口调用成功的回调函数 | 1.0.0 |
| fail | function |  | 否 | 接口调用失败的回调函数 | 1.0.0 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） | 1.0.0 |

#### buyQuantity 说明
购买游戏币的数量，开发者可以在字节小游戏平台的“支付”tab 设置游戏币单价，换算为人民币时必须符合指定价格档位，计算公式为：buyQuantity *** ** 游戏币单价 = 限定价格等级。如：游戏币单价为 0.1 元，一次购买数量至少是 10 个，详见[小游戏接入流程说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/payment/access-process)。

| 限定价格等级（单位：元） | 1 3 6 8 12 18 25 30 40 45 50 60 68 73 78 88 98 108 118 128 148 168 188 198 328 648 998 1288 1998 2998 |
| --- | --- |

#### goodType 说明
由于 goodType 需要基础库版本 3.47.0 及以上支持，可使用 tt.canIUse('requestGamePayment.object.goodType')进行兼容判断，开发者需要确保与其他支付方式实现版本兼容。

| 值 | 说明 |
| --- | --- |
| 0 | 默认值，表示游戏币场景 |
| 1 | 游戏币场景 |
| 2 | 道具直购场景 |

## 回调成功
object 类型，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| errMsg | string | requestGamePayment:ok | 1.0.0 |

## 回调失败
object 类型，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| errMsg | string | "requestGamePayment:fail " + 错误详情 | 1.0.0 |
| errCode | number | 错误码，对应信息可参考**错误码说明** | 1.0.0 |

### 错误码说明

| errCode | errMsg | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| -1 | requestGamePayment:fail 支付失败 | 用户支付失败 | 1.0.0 |
| -1 | requestGamePayment:fail internal error | 小游戏框架内部错误，请通过[创建工单](https://developer.open-douyin.com/work-order-page?tab=workOrderRecord)进行咨询 | 1.0.0 |
| -2 | requestGamePayment:fail 支付取消 | 用户取消支付 | 1.0.0 |
| 3 | requestGamePayment:fail error_tip_start_cash_register_fail | 拉起收银台失败，如遇小游戏框架内部错误，请通过[创建工单](https://developer.open-douyin.com/work-order-page?tab=workOrderRecord)进行咨询 | 1.0.0 |
| 4 | requestGamePayment:fail 网络异常 | 用户网络异常 | 1.0.0 |
| -15002 | requestGamePayment:fail 请求参数不合法 | 请求参数不合法 | 1.0.0 |
| -15006 | requestGamePayment:fail app 没有支付权限 | 请确认是否设置游戏币汇率，如仍有问题请[创建工单](https://developer.open-douyin.com/work-order-page?tab=workOrderRecord)咨询 | 1.0.0 |
| -15098 | requestGamePayment:fail 当前用户未通过实名认证 | 当前用户未通过实名认证 | 1.0.0 |
| -15099 | requestGamePayment:fail 当前用户累计支付金额超过限制 | 当前用户累计支付金额超过限制 | 1.0.0 |
| -15101 | requestGamePayment:fail customId 为空或者不唯一 | customId 为空或者不唯一 | 1.0.0 |
| -16000 | requestGamePayment:fail 用户未登录 | 用户未登录 | 1.0.0 |
| -20002 | requestGamePayment:fail 交易存在风险 | 交易存在风险，被风控策略拦截 | 1.0.0 |
| 21113 | requestGamePayment:fail face authentication failed | 检测到疑似未成年下单，拉起人脸核验，人脸验证不通过 | 1.0.0 |

## 扫码体验
无
## 代码示例
道具直购场景

```js
if (tt.canIUse("requestGamePayment.object.goodType")) {
  // 道具直购场景
  tt.requestGamePayment({
    goodType: 2, // 道具直购
    orderAmount: 10, // 道具现金价值，单位分
    goodName: "道具名称", // 道具名称
    currencyType: "CNY",
    zoneId: "1",
    customId: "QWERTYUIDFxxxxx",
    mode: "game", // 支付类型
    env: 0, // 支付环境
    platform: "android",
    extraInfo: '{"userId":"12xxx6","version":"v0.0.0","price":"30"}', // extraInfo为字符串类型
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

游戏币场景

```js
tt.requestGamePayment({
  mode: "game", // 支付类型
  env: 0, // 支付环境
  platform: "android",
  currencyType: "CNY", // 币种：目前仅为 "CNY"
  buyQuantity: 600, // 购买数量，必须满足：金币数量*金币单价 = 限定价格等级（详见金币限定等级）
  zoneId: "1",
  customId: "QWERTYUIDFxxxxx", // 开发者自定义唯一订单号。如不填，支付结果回调将不包含此字段，将导致游戏开发者无法发放游戏道具, 基础库版本低于1.55.0没有此字段
  extraInfo: '{"userId":"12xxx6","version":"v0.0.0","price":"30"}', // extraInfo为字符串类型
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

## Bug & Tip
### 测试说明

| 在IDE中调用支付接口 | 在开发者工具中调用支付接口时，可验证接口传入参数有效性。 参数校验通过后模拟器将展示支付二维码，对应真机上表现为拉起收银台 |  | 此二维码只用作能力模拟，无法真实进行扫码支付 |
| --- | --- | --- | --- |
| 在IDE中使用Mock面板 | 在开发者工具中调用支付相关JSAPI时，可通过该能力Mock多个支付场景，帮助开发者快速调试接口。 |  | 抖音开发者工具4.4.1版本及以上支持该功能，只用作能力模拟，无法真实进行支付 |
| 扫码/真机调试**（推荐）** | 完整测试支付链路，使用开发者工具中的【预览/真机调试】功能，扫码后可在真机上拉起收银台 |  | 目前暂不支持测试**沙盒环境**，在真机测试的过程中将使用**真实金额**进行支付，建议选择小额支付进行测试，大额场景检查收银台支付金额是否正确即可 用户在不同APP端或系统支付时收银台样式存在差异，开发者无需关注 |
