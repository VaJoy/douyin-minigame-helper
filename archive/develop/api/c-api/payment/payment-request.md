---
title: "支付请求"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/payment/payment-request
update_time: 2025-12-09
---

## TT.OpenAwemeCustomerService
> 6.0.0 开始支持本方法
通过客服页面发起支付。

> 注意：
> 该模块对应小游戏接口 [小游戏接口：tt.openAwemeCustomerService](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-open-aweme-service#d4b5133e)
> 该模块对应 [旧版Unity SDK文档中的 【钻石支付】 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#8510021e)

| 前提条件 | 使用前请参考[指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/user-service/douyinIM/)完成IM客服能力接入（运营 - 功能 - 客服管理 - 抖音IM客服），后续充值相关问题用户都会通过该客服进行咨询（**请勿用绑定的抖音号进行支付测试，会导致无法拉起客服界面**）（本步骤未完成报错：`fail im disable`） 接入本能力需要先开通【虚拟支付】和【钻石兑换】能力，请前往开发者平台 在「商业化」>「虚拟支付」申请开通能力 超级管理员通过顶部提示条开通钻石兑换能力 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 支持抖音iOS，抖音 iOS版本大于等于22.5.0时用户可使用 支持抖lite iOS，抖lite iOS版本大于等于27.5.0时用户可使用 支持 unity 小游戏 |
| 注意事项 | 调用该方法时，需要保证用户已经[登录](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/account)。可以调用[tt.checkSession](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/account#2508f57b)检测用户登录状态，以避免用户处于未登录状态时支付订单，在登录后无法关联订单与登录后的账户。 异常情况下，充值有可能存在游戏币延迟到账问题，建议游戏在收到支付结果回调后，通过接口 [获取游戏币余额](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/acquire-mini-game-coin-balance) 向服务端轮询最新游戏币余额，间隔 3 秒，持续约 1 分钟，可以根据返回值的 `save_amt` 的变化来确定是否充值成功。 用户成功拉起收银台后即回调成功，未成功拉起收银台即回调失败，与实际支付结果无关，是否支付成功请通过服务端接口查询余额自行保证。 |
| 相关教程 | 支付能力接入：[支付能力接入介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/payment/access-process) 钻石支付接入：[钻石兑换介绍及接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/diamonds) |

### **语法 **

```csharp
public static void OpenAwemeCustomerService(OpenAwemeCustomerServiceParam param)
```

> **注意：**
> 以下示例代码对应 TTSDK 版本< `6.1.1`，已过时。

```csharp
public static void OpenAwemeCustomerService(JsonData options, 
    Action success, 
    Action<int, string> failed);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| options | JsonData | -- | 是 | 格式详情 |
| success | Action | -- | 是 | 打开客服页成功 |
| failed | Action<int, string> | -- | 是 | 打开客服聊天页回调，参数为是否成功，true表示成功，false表示失败。 |

**JsonData 内容格式：**

|  | 格式 | 默认值 | 是否必填 | 说明 |
| --- | --- | --- | --- | --- |
| buyQuantity | number | -- | 是 | 金币购买数量，金币数量必须满足：金币数量*金币单价 = 限定价格等级（详见下方 buyQuantity 限制说明。） |
| customId | string | -- | 是 | 游戏开发者自定义的唯一订单号，订单支付成功后通过服务端支付结果回调回传 |
| currencyType | string | -- | 否 | 币种，枚举值 •DIAMOND - 表示钻石，目前仅支持该类型 注意-如果要感知用户实际支付的币种类型，请参考[服务端支付结果回调](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/payment-server-callback)回传信息中的currency字段信息 |
| zoneId | string | 1 | 否 | 游戏服务区 id，开发者自定义。游戏不分大区则默认填写"1"。如果应用支持多角色，则角色 ID 接在分区 ID 后，用"_"连接 |
| extraInfo | string | null | 否 | 游戏开发者自定义的其他信息，订单支付成功后通过服务端支付结果回调回传。字符串长度最大不能超过 256。（强烈建议传入） |
| goodType | number |  | 否 | 支付场景 |
| goodName | string |  | 否 | goodType为道具直购场景时，代表道具名称，长度限制小于等于10个字符，用于区分道具类型 |
| orderAmount | number |  | 否 | goodType为道具直购场景时必传，代表道具现金价格，单位为【分】，如道具价格为0.1元，则回传10 |

**buyQuantity 限制说明：**
购买游戏币的数量，开发者可以在字节小游戏平台的“支付”tab 设置游戏币单价，换算成 RMB 必须满足以下价格档位， 即 buyQuantity * 游戏币单价 = 限定价格等级。如：游戏币单价为 0.1 元，一次购买数量至少是 10 个。

| 限定价格等级（单位：元） | 1 3 6 8 12 18 25 30 40 45 50 60 68 73 78 88 98 108 118 128 148 168 188 198 328 648 998 1998 2998 |
| --- | --- |

**orderAmount 参数说明：**
由于 goodType 需要在 TTSDK 6.0.8 及以上版本、基础库版本 3.47.0 及以上才可支持，可使用：

```text
CanIUse.OpenAwemeCustomerServiceParams.GoodType
```

来判断是否支持，与其他支付方式做好版本兼容。
goodType 合法值：
- 0：默认值，表示游戏币场景
- 1：游戏币场景
- 2：[道具直购场景 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/payment/access-process#2fe5ff8e)

### 错误码
该接口错误码请参考[小游戏API tt.openAwemeCustomerService 错误码](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-open-aweme-service#d4b5133e)。
### OpenAwemeCustomerServiceParam
> 6.1.1版本开始支持
#### 语法

```csharp
public class OpenAwemeCustomerServiceParam
{
    /// <summary>
    /// 必填（道具直购场景除外） 金币购买数量，金币数量必须满足：金币数量*金币单价 = 限定价格等级（详见下方 buyQuantity 限制说明。开发者可以在字节小游戏平台的“支付”tab 设置游戏币单价）
    /// </summary>
    public int BuyQuantity;
    /// <summary>
    /// 必填   游戏开发者自定义的唯一订单号，订单支付成功后通过服务端支付结果回调回传
    /// </summary>
    public string CustomId; 
    /// <summary>
    /// 非必填 币种, 目前仅为"DIAMOND"
    /// </summary>
    public string CurrencyType; 
    /// <summary>
    /// 非必填 游戏服务区 id，默认值为1，开发者自定义。游戏不分大区则默认填写"1"。如果应用支持多角色，则角色 ID 接在分区 ID 后，用"_"连接
    /// </summary>
    public string ZoneId;
    /// <summary>
    /// 非必填 游戏开发者自定义的其他信息，订单支付成功后通过服务端支付结果回调回传。字符串长度最大不能超过 256。（强烈建议传入）
    /// </summary>
    public string ExtraInfo;     
    /// <summary>
    /// 非必填（道具直购场景必填） 默认游戏币。 游戏币：0 | 1，道具直购：2。若goodType为道具直购场景，不可传buyQuantity
    /// </summary>
    public int GoodType;
    /// <summary>
    /// 非必填（道具直购场景必填） 道具价格，人民币，单位分  
    /// </summary>
    public int OrderAmount;
    /// <summary>
    /// 非必填 道具名称     
    /// </summary>
    public string GoodName;
    /// <summary>
    /// 非必填 （礼包场景必填）礼包Id
    /// </summary>
    public string GoodsId;
    /// <summary>
    /// OpenAwemeCustomer 成功回调
    /// </summary>
    public OpenAwemeCustomerSuccessCallback Success;
    /// <summary>
    /// OpenAwemeCustomer 失败回调
    /// </summary>
    public Action<ErrorInfo> Fail;
    /// <summary>
    /// 接口调用完成回调
    /// </summary>
    public Action Complete;
}

public class OpenAwemeCustomerSuccessResult
{
    /// <summary>
    /// 错误信息
    /// </summary>
    public string ErrMsg;
    /// <summary>
    /// 支付时间
    /// </summary>
    public long PayTime;
}
```

### 代码示例

```csharp
if (CanIUse.OpenAwemeCustomerServiceParams.GoodType)
{
    // 道具直购
    var param = new OpenAwemeCustomerServiceParam
    {
        CustomId = (TimeUtils.GetCurrentTimeMs() / 1000).ToString(),
        CurrencyType = "DIAMOND",
        ZoneId = "1",
        ExtraInfo = "sc diamond pay test extra",
        GoodType = 2,
        GoodName = "测试商品",
        OrderAmount = int.Parse(inputPrice.text),
        Success = successResult =>
        {
            Debug.Log($"OpenAwemeCustomerService Success , errMsg: {successResult.ErrMsg}, " +
                       $"GiftId: {successResult.Gift?.GiftId} , GiftCode: {successResult.Gift?.GiftCode}, status: {successResult.Gift?.Status}" );
        },
        Fail = failResult =>
        {
            Debug.Log($"OpenAwemeCustomerService Fail , errMsg: {failResult.ErrMsg}, " +
                              $"errCode: {failResult.ErrorCode} , errorType: {failResult.ErrorType}");
        },
        Complete = () =>
        {
            Debug.Log("OpenAwemeCustomerService Complete");
        }
    };
    TT.OpenAwemeCustomerService(param);
}
else
{
    // 钻石支付
    var param = new OpenAwemeCustomerServiceParam
    {
        BuyQuantity = int.Parse(inputPrice.text),
        CustomId = (TimeUtils.GetCurrentTimeMs() / 1000).ToString(),
        CurrencyType = "DIAMOND",
        ZoneId = "1",
        ExtraInfo = "sc diamond pay test extra",
        Success = successResult =>
        {
            Debug.Log($"OpenAwemeCustomerService Success , errMsg: {successResult.ErrMsg}, " +
                       $"GiftId: {successResult.Gift?.GiftId} , GiftCode: {successResult.Gift?.GiftCode}, status: {successResult.Gift?.Status}" );
        },
        Fail = failResult =>
        {
            Debug.Log($"OpenAwemeCustomerService Fail , errMsg: {failResult.ErrMsg}, " +
                              $"errCode: {failResult.ErrorCode} , errorType: {failResult.ErrorType}");
        },
        Complete = () =>
        {
            Debug.Log("OpenAwemeCustomerService Complete");
        }
    };
    TT.OpenAwemeCustomerService(param);
}
```

> **注意**
> 以下示例代码对应 TTSDK 版本< `6.1.1`，已过时。

```csharp
if (CanIUse.OpenAwemeCustomerServiceParams.GoodType)
{
    var quantity = int.Parse(inputPrice.text);
    var options = new JsonData
    {
        ["customId"] = (TimeUtils.GetCurrentTimeMs() / 1000).ToString(),
        ["currencyType"] = "DIAMOND",
        ["zoneId"] = "1",
        ["extraInfo"] = "sc diamond pay test extra",
        ["goodType"] = 2,
        ["orderAmount"] = quantity,
        ["goodName"] = "测试商品"

    };
    TT.OpenAwemeCustomerService(options, () =>
    {
        Debug.Log("OpenAwemeCustomerService success");
    }, (errCode, errMsg) =>
    {
        Debug.Log($"OpenAwemeCustomerService failed, errCode: {errCode}, errMsg: {errMsg}");
    });
}
else
{
    var quantity = int.Parse(inputPrice.text);
    var options = new JsonData
    {
        ["buyQuantity"] = quantity,
        ["customId"] = (TimeUtils.GetCurrentTimeMs() / 1000).ToString(),
        ["currencyType"] = "DIAMOND",
        ["zoneId"] = "1",
        ["extraInfo"] = "sc pay test extra"
    };
    TT.OpenAwemeCustomerService(options, () =>
    {
        Debug.Log("OpenAwemeCustomerService success");
    }, (errCode, errMsg) =>
    {
        Debug.Log($"OpenAwemeCustomerService failed, errCode: {errCode}, errMsg: {errMsg}");
    });
}
```

## TT.RequestGamePayment
> 6.0.0 开始支持本方法，WebGL也支持该方法
发起支付。
**支付接入流程：**
[https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/access-process](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/payment/access-process)。
**抖音开发者平台接口文档：**
[https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-request-game-payment](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-request-game-payment)。
> 提示
> 调用该方法时，需要保证用户已经[登录](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/log-in/tt-login/)。可以调用[tt.checkSession](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/log-in/tt-check-session)检测用户登录状态，以避免用户处于未登录状态时支付订单，在登录后无法关联订单与登录后的账户。
> 异常情况下，充值有可能存在游戏币延迟到账问题，建议游戏在收到支付结果回调后，向服务端轮询最新游戏币余额，间隔 3 秒，持续约 1 分钟，可以根据返回值的 save_amt 的变化来确定是否充值成功。 同时也存在一些异常情况，导致充值成功后结果回调失败，因此建议游戏在启用游戏时主动[查询游戏币余额](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/acquire-mini-game-coin-balance)，并且提供给用户主动刷新余额的功能。（不要将查询余额作为进入游戏的必要条件，查询失败时，可在显示余额的界面显示异常，不要拒绝用户进入游戏，更不要直接显示 0） 强烈建议请求中填入 customId 和 extraInfo 字段（字段意义见下方表格），如果未填，支付结果回调将不包含游戏开发者的订单号，导致开发者无法确定回调是对应哪个订单，从而影响游戏道具发放。如果遇到此类问题，开发者可调用[queryPayState 接口](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/order-status-check)进行订单状态确认。
> 以上三条均属建议，供游戏参考。
### **语法**

```csharp
public static void RequestGamePayment(RequestGamePaymentParam param)
```

> **注意：**
> 以下示例代码对应 TTSDK 版本< `6.1.1`，已过时。

```csharp
public static void RequestGamePayment(Dictionary<string, object> orderInfo,
    Action payCallback = null,
    Action<int, string> errCallback = null)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| orderInfo | Dictionary<string, object> | - | 是 | 订单信息，包含 mode、env、currencyType、platform、buyQuantity、zoneId、customId、extraInfo等信息 |
| payCallback | Action | null | 否 | 支付成功回调 |
| errCallback | Action<int, string> | null | 否 | 支付失败回调，由错误码和错误信息组成 |

**orderInfo 的属性如下：**

| 属性名 | **类型** | **默认值** | **是否必填** | **说明** |
| --- | --- | --- | --- | --- |
| mode | string | -- | 是 | 支付的类型, 目前仅为"game" |
| env | string | -- | 是 | 环境配置，目前合法值仅为"0" |
| currencyType | string | -- | 是 | 币种, 目前仅为"CNY" |
| platform | string | -- | 是 | 申请接入时的平台，目前仅为"android" |
| buyQuantity | number | -- | 是 | 金币购买数量，金币数量必须满足：金币数量*金币单价 = 限定价格等级（详见下方 buyQuantity 限制说明。开发者可以在字节小游戏平台的“支付”tab 设置游戏币单价） |
| zoneId | string | 1 | 否 | 游戏服务区 id，开发者自定义。游戏不分大区则默认填写"1"。如果应用支持多角色，则角色 ID 接在分区 ID 后，用"_"连接 |
| customId | string | -- | 是 | 游戏开发者自定义的唯一订单号，订单支付成功后通过[服务端支付结果回调](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/payment-server-callback)回传  必须具有唯一性，如果不传或重复传相同值，则会报错 |
| extraInfo | string | null | 否 | 游戏开发者自定义的其他信息，订单支付成功后通过[服务端支付结果回调](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/payment-server-callback)回传。字符串长度最大不能超过 256。 |
| goodType | number | 0 | 否 | 支付场景 |
| orderAmount | number |  | 否 | goodType为道具直购场景时必传，代表道具现金价格，单位为【分】，如道具价格为0.1元，则回传10 |
| goodName | string |  | 否 | goodType为道具直购场景时，代表道具名称，长度限制小于等于10个字符，用于区分道具类型 |

**errCode 的值类型：**

| **值** | **说明 ** |
| --- | --- |
| -1 | 支付失败 |
| -2 | 支付取消 |
| -15001 | 缺少参数 |
| -15002 | 请求参数不合法 |
| -15003 | App 不支持小游戏支付 |
| -15006 | App 没有支付权限 |
| -15009 | 内部错误，支付失败 |
| -15098 | 当前用户未通过实名认证 |
| -15099 | 当前用户累计支付金额超过限制 |
| -15101 | customId 为空或者不唯一 |
| -16000 | 用户未登录 |
| -20002 | 交易存在风险，被风控策略拦截 |
| 2 | 正在支付同一订单时，又发起了一笔支付请求 |
| 3 | 调起收银台失败 |
| 4 | 网络异常 |
| 5 | iOS 平台错误，当前平台不支持支付 |
| 6 | 其他错误 |
| 21113 | 检测到疑似未成年下单，拉起人脸核验，人脸验证不通过 |

**buyQuantity 限制说明：**
购买游戏币的数量，开发者可以在字节小游戏平台的“支付” tab 设置游戏币单价，换算成 RMB 必须满足以下价格档位， 即 buyQuantity * 游戏币单价 = 限定价格等级。如：游戏币单价为 0.1 元，一次购买数量至少是 10 个，详见[小游戏接入流程说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/payment/access-process)。

**orderAmount 参数说明：**
由于 goodType 需要在 TTSDK 6.0.8 及以上版本、基础库版本 3.47.0 及以上才可支持，可使用：

```text
CanIUse.OpenAwemeCustomerServiceParams.GoodType
```

来判断是否支持，与其他支付方式做好版本兼容。

| 值 | 说明 |
| --- | --- |
| 0 | 默认值，表示游戏币场景 |
| 1 | 游戏币场景 |
| 2 | [道具直购场景](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/payment/access-process#2fe5ff8e) |

### RequestGamePaymentParam
> 6.1.1版本开始支持
#### 语法
> 参数解释与旧接口参数解释一致

```csharp
public class RequestGamePaymentParam
{
    /// <summary>
    /// 必填  支付的类型, 目前仅为"game"
    /// </summary>
    public string Mode;             
    /// <summary>
    /// 必填  环境配置，目前合法值仅为"0"
    /// </summary>
    public int Env;                 
    /// <summary>
    /// 必填  币种, 目前仅为"CNY"
    /// </summary>
    public string CurrencyType;
    /// <summary>
    /// 必填  申请接入时的平台，目前仅为"android"
    /// </summary>
    public string Platform; 
    /// <summary>
    /// 必填（道具直购场景除外）金币购买数量
    /// </summary>
    public int BuyQuantity;
    /// <summary>
    /// 非必填 游戏服务区 id，
    /// </summary>
    public string ZoneId;           
    /// <summary>
    /// 必填  游戏开发者自定义的唯一订单号，订单支付成功后通过服务端支付结果回调回传
    /// </summary>
    public string CustomId; 
    /// <summary>
    /// 非必填 游戏开发者自定义的其他信息，订单支付成功后通过服务端支付结果回调回传。字符串长度最大不能超过 256
    /// </summary>
    public string ExtraInfo;
    /// <summary>
    /// 非必填（道具直购场景必填）默认游戏币。goodType 与 buyQuantity 任一传递即，可游戏币：0 或 1，道具直购：2
    /// </summary>
    public int GoodType;
    /// <summary>
    /// 非必填（道具直购场景必填）道具价格，人民币，单位分
    /// </summary>
    public int OrderAmount;
    /// <summary>
    /// 非必填（道具直购场景必填）道具名称
    /// </summary>
    public string GoodName; 
    /// <summary>
    /// 非必填 （礼包场景必填）礼包Id
    /// </summary>
    public string GoodsId; 
    /// <summary>
    /// 支付成功回调
    /// </summary>
    public RequestGamePaymentSuccessCallback Success;
    /// <summary>
    /// 支付失败回调
    /// </summary>
    public Action<ErrorInfo> Fail;
    /// <summary>
    /// 接口调用完成回调
    /// </summary>
    public Action Complete;
}

public class RequestGamePaymentSuccessResult
{
    /// <summary>
    /// 错误信息
    /// </summary>
    public string ErrMsg;
    /// <summary>
    /// 支付时间
    /// </summary>
    public long PayTime; 
}
```

### 代码示例

```csharp
if (CanIUse.RequestGamePaymentParams.GoodType)
{
    var param = new RequestGamePaymentParam {
        Mode = "game",
        Env = 0,
        CurrencyType = "CNY", // 固定值: CNY。币种
        Platform = "android",
        GoodType = 2,
        OrderAmount = int.Parse(inputPrice.text),
        GoodName = "测试商品",
        CustomId = (TimeUtils.GetCurrentTimeMs() / 1000).ToString(),
        Success = successResult =>
        {
            Debug.Log($"Pay Success , errMsg: {successResult.ErrMsg}, " +
                            $"GiftId: {successResult.Gift?.GiftId} , GiftCode: {successResult.Gift?.GiftCode}, status: {successResult.Gift?.Status}" );
        },
        Fail = failResult =>
        {
            Debug.Log($"Pay Fail , errMsg: {failResult.ErrMsg}, " +
                            $"errCodeP: {failResult.ErrorCode} , errorType: {failResult.ErrorType}");
        },
        Complete = () =>
        {
            Debug.Log("RequestGamePayment Complete");
        }
    };
    TT.RequestGamePayment(param);
}
else
{
    var param = new RequestGamePaymentParam {
        Mode = "game",
        Env = 0,
        CurrencyType = "CNY", // 固定值: CNY。币种
        Platform = "android",
        BuyQuantity = int.Parse(inputPrice.text),
        CustomId = (TimeUtils.GetCurrentTimeMs() / 1000).ToString(),
        Success = successResult =>
        {
            Debug.Log($"Pay Success , errMsg: {successResult.ErrMsg}, " +
                            $"GiftId: {successResult.Gift?.GiftId} , GiftCode: {successResult.Gift?.GiftCode}, status: {successResult.Gift?.Status}" );
        },
        Fail = failResult =>
        {
            Debug.Log($"Pay Fail , errMsg: {failResult.ErrMsg}, " +
                            $"errCode: {failResult.ErrorCode} , errorType: {failResult.ErrorType}");
        },
        Complete = () =>
        {
            Debug.Log("RequestGamePayment Complete");
        }
    };
    TT.RequestGamePayment(param);
}
```

> **注意：**
> 以下示例代码对应 TTSDK 版本< `6.1.1`，已过时。

```csharp
if (CanIUse.RequestGamePayment)
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
