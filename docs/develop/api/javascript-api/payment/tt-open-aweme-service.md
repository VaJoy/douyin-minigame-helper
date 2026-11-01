---
title: "tt.openAwemeCustomerService"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/tt-open-aweme-service
update_time: 2026-08-06
---

> 基础库 2.64.0 开始支持本方法，低版本需做[兼容处理](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/basic-library/compatibility-description/)。这是一个异步方法。
发起抖音钻石支付

| 前提条件 | 使用前请参考[指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/user-service/douyinIM/)完成IM客服能力接入（运营 - 功能 - 客服管理 - 抖音IM客服），后续充值相关问题用户都会通过该客服进行咨询（**请勿用绑定的抖音号进行支付测试，会导致无法拉起客服界面**）（本步骤未完成报错：fail im disable） 接入本能力需要先开通【虚拟支付】和【钻石兑换】能力，请前往开发者平台 在「商业化」>「虚拟支付」申请开通能力，详细信息可参考[支付能力接入介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/payment/access-process) 超级管理员通过顶部提示条开通钻石兑换能力，详细信息可参考[钻石兑换介绍及接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/diamonds) |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 支持抖音，版本大于等于22.5.0时用户可使用 支持抖音极速版 iOS，版本大于等于27.5.0时用户可使用 支持红果短剧 iOS（7.0.7 及以上版本），番茄小说 iOS（7.1.1 及以上版本）、汽水音乐 iOS（19.1.0 及以上版本） 支持 unity 小游戏 |
| 注意事项 | 调用该方法时，需要保证用户已经[登录](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/log-in/tt-login)。可以调用 [tt.checkSession](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/log-in/tt-check-session) 检测用户登录状态，以避免用户处于未登录状态时支付订单，在登录后无法关联订单与登录后的账户。 异常情况下，充值有可能存在游戏币延迟到账问题，建议游戏在收到支付结果回调后，通过接口 [获取游戏币余额](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/acquire-mini-game-coin-balance) 向服务端轮询最新游戏币余额，间隔 3 秒，持续约 1 分钟，可以根据返回值的 save_amt 的变化来确定是否充值成功。 用户成功拉起收银台后即回调成功，未成功拉起收银台即回调失败，与实际支付结果无关，是否支付成功请通过服务端接口查询余额自行保证。 |
| 相关教程 | 无 |

## 语法

```js
tt.openAwemeCustomerService(options)
```

## 参数说明
options 为 object 类型，属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| extraInfo | string |  | 否 | 游戏开发者自定义的其他信息，订单支付成功后通过[服务端支付结果回调](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/payment-server-callback)回传。字符串长度最大不能超过 256。（强烈建议传入） | 2.64.0 |
| zoneId | string |  | 否 | 游戏服务区 id，开发者自定义。游戏不分大区则默认填写"1"。如果应用支持多角色，则角色 ID 接在分区 ID 后，用"_"连接 | 2.64.0 |
| currencyType | string |  | 否 | 币种，枚举值 DIAMOND - 表示钻石，目前仅支持该类型 注意-如果要感知用户实际支付的币种类型，请参考[服务端支付结果回调](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/payment-server-callback)回传信息中的currency字段信息 | 2.64.0 |
| buyQuantity | number |  | 否 | 游戏币购买数量。游戏币数量必须满足：**游戏币数量 * 游戏币单价 = 限定价格等级**（详见下方 **buyQuantity 参数说明**。开发者可以在开发者平台的“支付设置”tab 设置游戏币单价） goodType为游戏币场景时必传，其他场景不传 | 2.64.0 |
| goodType | number |  | 否 | 支付场景，详见下方** goodType 说明** | 3.47.0 |
| orderAmount | number |  | 否 | goodType为道具直购场景时必传，代表道具现金价格，单位为【分】 如道具价格为0.1元，则回传10 | 3.47.0 |
| goodName | string |  | 否 | goodType为道具直购场景时，代表道具名称，长度限制小于等于10个字符，用于区分道具类型 | 3.47.0 |
| customId | string |  | 是 | 游戏开发者自定义的唯一订单号，订单支付成功后通过[服务端支付结果回调](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/payment-server-callback)回传 | 2.64.0 |
| success | function |  | 否 | 接口调用成功的回调函数 | 2.64.0 |
| fail | function |  | 否 | 接口调用失败的回调函数 | 2.64.0 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） | 2.64.0 |

### buyQuantity 说明
**限制说明：**购买游戏币的数量，开发者可以在开发者平台的“支付设置”tab 设置游戏币单价, 换算成 RMB 必须满足以下价格档位， 即 **buyQuantity * 游戏币单价 = 限定价格等级**。如：游戏币单价为 0.1 元，一次购买数量至少是 10 个。

| 限定价格等级（单位：元） | 1 3 6 8 12 18 25 30 40 45 50 60 68 73 78 88 98 108 118 128 148 168 188 198 328 648 998 1288 1998 2998 |
| --- | --- |

**汇率转换说明**：当 currencyType 为 “DIAMOND” 时，平台按 1:10 汇率自动转换。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/c2be187b9948445ea38dfd3d93bef538~tplv-9nona0m7ha-image.image)

### goodType 说明
由于 goodType 需要在基础库版本 **3.47.0**及以上才可支持，可使用`tt.canIUse('openAwemeCustomerService.object.goodType')`来判断是否支持，需与其他支付方式做好版本兼容

| 值 | 说明 |
| --- | --- |
| 0 | 默认值，表示游戏币场景 |
| 1 | 游戏币场景 |
| 2 | 道具直购场景 |

## 回调成功
object 类型，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| errMsg | string | "openAwemeCustomerService:ok"，用户支付成功 | 2.64.0 |

## 回调失败
object 类型，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| errMsg | string | "openAwemeCustomerService:fail " + 错误详情 | 2.64.0 |
| errCode | number | 错误码，对应信息可参考**错误码说明** | 2.64.0 |
| errNo | number | 错误码，对应信息可参考**错误码说明** | 2.64.0 |

### 错误码

| errCode | errNo | errMsg | 说明 | 最低基础库版本 |
| --- | --- | --- | --- | --- |
| -1 | 20000 | openAwemeCustomerService:fail 支付失败 | 用户支付失败 | 2.64.0 |
| -2 | 20000 | openAwemeCustomerService:fail 支付取消 | 用户取消支付 | 2.64.0 |
| -15002 | 20000 | openAwemeCustomerService:fail 请求参数不合法 | 请求参数不合法 | 2.64.0 |
| -15009 | 20000 | openAwemeCustomerService:fail 内部错误,支付失败 | 小游戏框架内部错误，有需要请[创建工单](https://developer.open-douyin.com/work-order-page?tab=workOrderRecord)咨询 | 2.64.0 |
| -15098 | 20000 | openAwemeCustomerService:fail 当前用户未通过实名认证 | 当前用户未通过实名认证 | 2.64.0 |
| -15099 | 20000 | openAwemeCustomerService:fail 当前用户累计支付金额超过限制 | 当前用户累计支付金额超过限制 | 2.64.0 |
| -15101 | 20000 | openAwemeCustomerService:fail customId 为空或者不唯一 | customId 为空或者不唯一 | 2.64.0 |
| -16000 | 20000 | openAwemeCustomerService:fail 用户未登录 | 用户未登录 | 2.64.0 |
| -16001 | 20000 | openAwemeCustomerService:fail 不支持iOS支付功能 | 暂不支持支付，请按照指引开通能力 | 2.64.0 |
| -17006 | 20000 | openAwemeCustomerService:fail buyQuantity illegal | buyQuantity参数异常 | 2.64.0 |
| -20002 | 20000 | openAwemeCustomerService:fail 交易存在风险 | 交易存在风险，被风控策略拦截 | 2.64.0 |
| 21113 | 20000 | openAwemeCustomerService:fail face authentication failed | 人脸校验失败 | 2.64.0 |
| 3 | 20000 | openAwemeCustomerService:fail error_tip_start_cash_register_fail | 拉起收银台失败，小游戏框架内部错误，有需要请[创建工单](https://developer.open-douyin.com/work-order-page?tab=workOrderRecord)咨询 | 2.64.0 |
| 4 | 20000 | openAwemeCustomerService:fail 网络异常 | 用户网络异常 | 2.64.0 |
| 99 | 20001 | openAwemeCustomerService:fail params.buyQuantity should be number, but got undefined | buyQuantity参数错误，其他参数错误也会有类似错误信息 | 2.64.0 |

## 扫码体验
无
## 代码示例
道具直购场景

```js
if (tt.canIUse("openAwemeCustomerService.object.goodType")) {
  // 道具直购场景
  tt.openAwemeCustomerService({
    goodType: 2, // 道具直购
    orderAmount: 10, // 道具现金价值，单位分
    goodName: "道具名称", // 道具名称
    currencyType: "DIAMOND", // 币种：目前仅为"DIAMOND"
    zoneId: "1",
    customId: "QWERTYUIDFxxxxx", //开发者自定义唯一订单号。如不填，支付结果回调将不包含此字段，将导致游戏开发者无法发放游戏道具, 基础库版本低于1.55.0没有此字段
    extraInfo: '{"userId":"12xxx6","version":"v0.0.0","price":"30"}', //extraInfo要转成字符串
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
tt.openAwemeCustomerService({
  currencyType: "DIAMOND", // 币种：目前仅为"DIAMOND"
  buyQuantity: 600, // 购买游戏币数量
  zoneId: "1",
  customId: "QWERTYUIDFxxxxx", //开发者自定义唯一订单号。如不填，支付结果回调将不包含此字段，将导致游戏开发者无法发放游戏道具, 基础库版本低于1.55.0没有此字段
  extraInfo: '{"userId":"12xxx6","version":"v0.0.0","price":"30"}', //extraInfo要转成字符串
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

| **方案** | **说明** | **图示** | **注意事项** |
| --- | --- | --- | --- |
| 在IDE中调用支付接口 | 在开发者工具中调用支付接口时，可验证接口传入参数有效性。 参数校验通过后模拟器将展示支付二维码，对应真机上表现为拉起收银台 |  | 此二维码只用作能力模拟，无法真实进行扫码支付 |
| 在IDE中使用Mock面板 | 在开发者工具中调用支付相关JSAPI时，可通过该能力Mock多个支付场景，帮助开发者快速调试接口。 |  | 抖音开发者工具4.4.1版本及以上支持该功能，只用作能力模拟，无法真实进行支付 |
| 扫码/真机调试**（推荐）** | 完整测试支付链路，使用开发者工具中的【预览/真机调试】功能，扫码后可在真机上拉起收银台 |  | 目前暂不支持测试**沙盒环境**，在真机测试的过程中将使用**真实金额**进行支付，建议选择小额支付进行测试，大额场景检查收银台支付金额是否正确即可 用户在不同App端或系统支付时收银台样式存在差异，开发者无需关注 |

tt.canIUse('openAwemeCustomerService.object.goodType')

### 语法

```js
tt.openAwemeCustomerService(extraInfo, zoneId, currencyType, buyQuantity, goodType, orderAmount, goodName, customId)
```
基础库 2.64.0 开始支持本方法，这是一个**异步**方法。
发起抖音钻石支付

### 示例代码
```js

if (tt.canIUse('openAwemeCustomerService.object.goodType')) {
  // 道具直购场景
  tt.openAwemeCustomerService({
    goodType: 2, // 道具直购
    orderAmount: 10, // 道具现金价值，单位分
    goodName: "道具名称", // 道具名称
    currencyType: "DIAMOND", // 币种：目前仅为"DIAMOND"
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
} else {
  // 游戏币
  tt.openAwemeCustomerService({
    currencyType: "DIAMOND", // 币种：目前仅为"DIAMOND"
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
}
```

### 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| extraInfo | string | 否 |  | 2.64.0 | 游戏开发者自定义的其他信息，订单支付成功后通过[服务端支付结果回调](https://microapp.bytedance.com/docs/zh-CN/mini-game/develop/api/payment/payment-server-callback)回传。字符串长度最大不能超过 256。（强烈建议传入） |
| zoneId | string | 否 |  | 2.64.0 | 游戏服务区 id，开发者自定义。游戏不分大区则默认填写"1"。如果应用支持多角色，则角色 ID 接在分区 ID 后，用"_"连接 |
| currencyType | string | 否 |  | 2.64.0 | 币种，目前仅为“DIAMOND”   （注意-如果要感知用户实际支付的币种类型，请参考[服务端支付结果回调](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/payment-server-callback)回传信息中的currency字段信息） |
| buyQuantity | number | 否 |  | 2.64.0 | 游戏币购买数量。游戏币数量必须满足：游戏币数量*游戏币单价 = 限定价格等级（详见下方 buyQuantity 参数说明。开发者可以在开发者平台的“支付设置”tab 设置游戏币单价）  goodType为游戏币场景时必传，其他场景不传  - 限制说明：购买游戏币的数量，开发者可以在开发者平台的“支付设置”tab 设置游戏币单价, 换算成 RMB 必须满足以下价格档位， 即 buyQuantity * 游戏币单价 = 限定价格等级。如：游戏币单价为 0.1 元，一次购买数量至少是 10 个。  \|  \|  \| \| --- \| --- \| \| 限定价格等级（单位：元） \| 1 3 6 8 12 18 25 30 40 45 50 60 68 73 78 88 98 108 118 128 148 168 188 198 328 648 998 1288 1998 2998 \|  - 汇率转换说明：当 currencyType 为 “DIAMOND” 时，平台按 1:10 汇率自动转换。  ![](https://p9-developer-sign.bytemaimg.com/obj/developer-inner/open_admin/1718615036313/blob?x-expires=4872215036&x-signature=rccg%2BoE45PZQcyAU6L1db6YKjp8%3D) |
| goodType | number | 否 |  | 3.47.0 | 支付场景 |
| orderAmount | number | 否 |  | 3.47.0 | goodType为道具直购场景时必传，代表道具现金价格，单位为【分】，如道具价格为0.1元，则回传10  - 由于 goodType 需要在基础库版本 3.47.0 及以上才可支持，可使用  ``` tt.canIUse('openAwemeCustomerService.object.goodType') ```  来判断是否支持，与其他支付方式做好版本兼容。  - goodType 合法值  - 0：默认值，表示游戏币场景 - 1：游戏币场景 - 2：道具直购场景 |
| goodName | string | 否 |  | 3.47.0 | goodType为道具直购场景时，代表道具名称，长度限制小于等于10个字符，用于区分道具类型 |
| customId | string | 是 |  | 2.64.0 | 游戏开发者自定义的唯一订单号，订单支付成功后通过[服务端支付结果回调](https://microapp.bytedance.com/docs/zh-CN/mini-game/develop/api/payment/payment-server-callback)回传 |

### 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object类型，属性如下：  **对象字段** - **errMsg**（string）："openAwemeCustomerService:ok"。用户支付成功 |

### 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object类型，属性如下：  **对象字段** - **errMsg**（string）："openAwemeCustomerService:fail " + 错误详情 - **errNo**（number）：错误码，对应信息可参考错误码说明 |

### 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | zoneId should not be empty |  |  |
| 20001 | invalid param |  |  |
| 999988 | only support iOS |  |  |
| 20000 | platform auth deny |  |  |
| 20000 | 用户未登录 |  |  |
| 20000 | 请求参数不合法 |  |  |
| 20000 | app 不支持小游戏支付 |  |  |
| 20000 | 内部错误,支付失败 |  |  |
| 20000 | 当前用户未通过实名认证 |  |  |
| 20000 | 当前用户累计支付金额超过限制 |  |  |
| 20000 | 支付失败 |  |  |
| 20000 | 交易存在风险 |  |  |
| 21113 | face authentication failed |  |  |
| 20000 | pay:fail error_tip_start_cash_register_fail |  |  |
| 20000 | 支付取消 |  |  |
| 20000 | 缺少参数 |  |  |
| 20000 | 其他错误 |  |  |
| 20000 | internal error |  |  |
| 20000 | 调起收银台失败 |  |  |
| 111017 | app 没有支付权限 |  |  |
| 111018 | customId 为空或者不唯一 |  |  |
| 111019 | 订单状态不对 |  |  |
| 999988 | 不支持iOS支付功能 |  |  |
| 111012 | 正在支付一起订单时,又发起了一笔支付请求 |  |  |
| 999985 | 网络异常 |  |  |
| 111020 | 付费礼包库存不足 |  |  |

### 使用限制
- 支持抖音ios，版本大于等于22.5.0时用户可使用
- 支持抖音极速版 ios，版本大于等于27.5.0时用户可使用
- 支持 unity 小游戏

### 注意事项
- 调用该方法时，需要保证用户已经[登录](https://microapp.bytedance.com/docs/zh-CN/mini-game/develop/open-capacity/log-in/tt-login/)。可以调用 [tt.checkSession](https://microapp.bytedance.com/docs/zh-CN/mini-game/develop/open-capacity/log-in/tt-check-session) 检测用户登录状态，以避免用户处于未登录状态时支付订单，在登录后无法关联订单与登录后的账户。
- 异常情况下，充值有可能存在游戏币延迟到账问题，建议游戏在收到支付结果回调后，通过接口 [获取游戏币余额](https://microapp.bytedance.com/docs/zh-CN/mini-game/develop/api/payment/acquire-mini-game-coin-balance) 向服务端轮询最新游戏币余额，间隔 3 秒，持续约 1 分钟，可以根据返回值的 save_amt 的变化来确定是否充值成功。
- 用户成功拉起收银台后即回调成功，未成功拉起收银台即回调失败，与实际支付结果无关，是否支付成功请通过服务端接口查询余额自行保证。

### 前置条件
- 使用前请参考[指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/user-service/douyinIM/)完成IM客服能力接入（运营 - 功能 - 客服管理 - 抖音IM客服），后续充值相关问题用户都会通过该客服进行咨询（**请勿用绑定的抖音号进行支付测试，会导致无法拉起客服界面**）（本步骤未完成报错：fail im disable）
- 接入本能力需要先开通【虚拟支付】和【钻石兑换】能力，请前往开发者平台

1. 在「商业化」>「虚拟支付」申请开通能力，详细信息可参考[支付能力接入介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/payment/access-process)
2. 超级管理员通过顶部提示条开通钻石兑换能力，详细信息可参考[钻石兑换介绍及接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/diamonds)

### 授权要求
无需开发者授权；无需用户授权

### 支持平台
iOS、Android
