---
title: "接入指引"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/virtual-payment/wallet-apple-pay/ios-minigame-payment-guide
update_time: 2026-10-28
---

## 一、iOS 苹果支付介绍
为保障用户权益，提高交易安全，开发者在小游戏内提供的虚拟商品，购买和支付均需按照苹果 App Store 相关规则接入苹果虚拟支付能力，提供通过苹果应用内购买（IAP）完成支付的能力。
> 适用 iOS 系统
## 二、能力优势
对用户：用户直接使用现金支付，无需通过先充值钻石再购买商品，转化路径短操作熟悉度高，体验流畅。
对开发者：接入成本低，无需交易链路改造由，只需完成一次进件即可。

## 三、接入流程
### iOS苹果支付开通指引
入口路径：登录「[抖音开放平台](https://developer.open-douyin.com/) -> 控制台 -> 小游戏 -> 商业化 -> 虚拟支付 -> 支付产品管理 -> iOS苹果支付」页面，对符合准入要求的小游戏，会展示开通入口指引，点击「去开通」。

| **开通阶段** | **说明** | **示例** |
| --- | --- | --- |
| 首次开通能力 | 进件：首次开通能力均需要新增进件，进件填写内容详见「[商业能力指南/虚拟支付/虚拟支付2.0/接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/virtual-payment/guaranteed-payment/guidelines)」，进件成功后即能力开通成功，此链路仅支持进件一个商户号，不支持新增，商户主体请谨慎选择 如不满足准入要求，则无法开通能力，满足后可开通 如进件失败根据失败提示修改后重新提交 |  |
| 已开通能力 | 查看详情：查看商户号、进件信息详情 账户详情：苹果支付收入，也可在「小游戏管理工作台」-「收入结算」-「担保支付收入结算」查看对应信息 |  |
| 关闭能力 | 苹果能力关闭后不影响其他能力使用 账单和资金提现可正常操作 |  |
| 重新开通能力 | 能力关闭后重新开通无需再次进件，默认同意苹果支付协议即可 能力开通后苹果支付链路正常收单 |  |

### 相关代码改动
**核心改动点：已开通钻石兑换的游戏，在接入iOS苹果支付时**：需要将字段“currencyType”改为“CNY”（如果该字段传为“DIAMOND”，则会导致iOS苹果支付接入失败）
> 如果是道具直购场景：无需传递buyQuantity字段，传递goodType = 2，orderAmount传递道具对应的价格（单位分）

##### tt.openAwemeCustomerService
> 基础库 2.64.0 开始支持本方法。这是一个异步方法。
> 通过客服页面发起支付
仅支持抖音、抖极，建议限制在手机端/pad端的抖音ios版本大于等于22.5.0时(抖极2750及以上)用户可使用，并支持unity小游戏。
##### 语法与参数说明

```js
tt.openAwemeCustomerService([options]);
```

`options` 为 object 类型，属性如下：

| 属性 | 类型 | 默认值 | 是否必填 | 说明 | 最低基础库版本 |
| --- | --- | --- | --- | --- | --- |
| buyQuantity | number |  | 是 | 金币购买数量，金币数量必须满足：金币数量*金币单价 = 限定价格等级（详见下方 buyQuantity 限制说明。开发者可以在字节小游戏平台的“支付”tab 设置游戏币单价） | 2.64.0 |
| customId | string |  | 是 | 游戏开发者自定义的唯一订单号，订单支付成功后通过[服务端支付结果回调](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/payment-server-callback)回传 | 2.64.0 |
| currencyType | string | 'CNY' | 否 | 如需接入iOS苹果支付，币种请填入"CNY"（请勿传入“DIAMOND”） | 2.64.0 |
| zoneId | string | 1 | 否 | 游戏服务区 id，开发者自定义。游戏不分大区则默认填写"1"。如果应用支持多角色，则角色 ID 接在分区 ID 后，用"_"连接 | 2.64.0 |
| extraInfo | string |  | 否 | 游戏开发者自定义的其他信息，订单支付成功后通过[服务端支付结果回调](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/payment-server-callback)回传。字符串长度最大不能超过 256。（强烈建议传入） | 2.64.0 |

##### 代码示例

```js
tt.openAwemeCustomerService({
  currencyType: "CNY", // 币种填入"CNY"
  buyQuantity: 600, // 购买数量，必须满足：金币数量*金币单价 = 限定价格等级（详见金币限定等级）
  zoneId: "1",
  customId: "QWERTYUIDFxxxxx", //开发者自定义唯一订单号。如不填，支付结果回调将不包含此字段，将导致游戏开发者无法发放游戏道具, 基础库版本低于1.55.0没有此字段
  extraInfo: '{
    userId: "12xxx6",   //用户自定义额外信息,支付结果回调信息包含此字段， 基础库版本低于1.55.0没有此字段
    version: "v0.0.0",
    price: "30",  }',//extraInfo要转成字符串  success(res) {
    console.log("调用函数成功");  },  fail(res) {
    console.log("调用函数失败");  },  complete(res) {
    console.log("调用完成");  },});
```

## 四、交易链路
1. 正向付款：交易下单无需接口配置，能力开通后即可使用。如同时接入了钻石兑换能力，用户钻石余额充足则使用钻石兑换商品/服务；如用户钻石余额不足则使用iOS 苹果支付（现金）支付。
1. 逆向退款：退款无需接口配置。iOS 苹果支付订单如需退款，用户需前往苹果官方退款，详见[苹果退款说明](https://support.apple.com/zh-cn/118223)，开发者无法通过接口主动发起退款。

## 五、结算提现
1. 内购结算基数 = 订单支付总金额 - 支付渠道费
1. iOS支付渠道费（苹果佣金）说明详见[抖音小游戏/小程序苹果支付功能使用协议](https://sf1-cdn-tos.douyinstatic.com/obj/ies-hotsoon-draft/douyin/97db8ea9-c55d-45b4-bd57-f11553d8ec5a.html)
1. 提现即开发者将「可提现总资金」提到商户结算银行账户。结算完成后资金（在途资金账户）转为可提现资金，详见[小游戏结算使用指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/revenue/introduction/douyin-games-guide)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/69283509cda6419fb23c82d0204daa61~tplv-9nona0m7ha-image.image)

## FAQ
1. **苹果支付接入后，钻石兑换可以继续使用么？**
可以继续使用，如用户钻石余额不足时则会跳转苹果支付收银台，如果余额充足则会优先消耗钻石；如未接入过钻石兑换，则用户会直接使用苹果支付。
1. **用户需要退款，小游戏可以发起么？**
不可以，用户退款需要去苹果官方申请。
1. **苹果支付可以指定商户号收款么？**
苹果支付不支持指定商户号收款，平台默认使用苹果支付开通时进件的商户号收款。仅支持一次进件无法更换商户主体，请谨慎选择商户主体完成进件，避免税务相关问题产生。产生。

tt.openAwemeCustomerService([options]);