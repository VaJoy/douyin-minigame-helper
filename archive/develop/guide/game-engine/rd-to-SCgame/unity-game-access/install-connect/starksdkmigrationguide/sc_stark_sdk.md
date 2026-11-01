---
title: "C# SDK 接口文档"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/starksdkmigrationguide/sc_stark_sdk
update_time: 2025-09-08
---

> **警告**
> - 本文档作为 旧版 StarkSdk API  文档将不再维护，**新版本 API 文档请至 “**[**Unity引擎适配 / C# API**](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/api-overview)** ”目录下查看**。
>   - 迁移说明可参考 [旧版 StarkSdk API 迁移 TTSDK API 说明文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/starksdk-migration-guide)。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/acdb9d269eff4ccb9c45b453e1b2725b)

> 文档说明：本文档描述抖音Unity小游戏接入商业化能力及宿主能力的接口说明
> *了解更多：*[抖音Unity小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide)

### 使用说明
#### API演示工程

附件下载：[StarkSDK-Sample.zip](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/8cd53cd6f6a142feaa3f908922e37e45~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/6cb8fcc95d3a4884a94e7b5f7e044c44)

相关接口通过 StarkSDKSpace.StarkSDK.API 来调用:
StarkSDKSpace.StarkSDK.API.GetStarkAdManager();
每个接口导航过去会有详细的注释，类似这样。在文档中不做重复的讲解

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1c177c88227d43cbb44150f2beccd40b)

### 兼容性处理
- 目前 Unity C# SDK 在各个宿主上的版本有一定差异，开发者需要关注兼容性工作，在低版本上使用不兼容的 API，会出现逻辑错误。
- WebGL 方案和 Native 方案的接口支持情况有一定差异
- 可使用 **StarkSDKSpace.CanIUse** 下的接口判断接口可用性，例如返回 true 表示当前环境支持

```csharp
    StarkSDKSpace.CanIUse.FollowDouYinUserProfile
```

## 功能模块
### 汇总

| **功能** | **广告** | **录屏** | **分享** | **登录** | **支付** | **侧边栏** | 其他 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **必要性** | 可选 | **android必须** | **android必须** | 可选 | 可选 | 抖音**必接** | 无要求 |
| **说明** | 如有广告则**必须**接 | UCG分发需要有录屏 |  | 如需登录则**必须**接 | 接入抖音小游戏担保支付，需要版号 |  |  |

需仔细阅读：[**小游戏自审**](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/agreement-and-norms/norms/standards/)
**大部分接口和普通小游戏共用同个或相似能力：**[体验抖音小游戏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/mini-game/bytedance-mini-game)**，可以作为参考。**
（StarkSDK.API.Xxxx== tt.xxxx）
在[小游戏平台](https://developer.open-douyin.com/console) 里查看自己项目的appid。注意：正确的抖音 Unity 小游戏的 appid 末两位 07
### 广告
开通：[流量主](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/open-capacity/operation/publisher/)
**要使用正确的广告id，在对应的appid下进行运行，才能正确播放广告。**

```java
通过 StarkSDK.API.GetStarkAdManager() 获取广告模块
```

#### 激励视频广告
**只支持一个实例的激励视频播放。**

```java
StarkSDK.API.GetStarkAdManager().ShowVideoAdWithId(string videoAdid, Action<bool> closeCallback = null, Action<int, string> errCallback = null, VideoAdCallback adCallback = null);
```

**激励再得广告**
[功能介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/rewardagainintroduce)

```csharp
/// <param name="multiton">是否开启再得广告模式（只支持安卓系统的抖音和抖音极速版）</param>
/// <param name="multitonRewardMsg">再得广告的奖励文案，玩家每看完一个广告都会展示，如【再看1个获得xx】xx就multitonRewardMsg中的文案，按顺序依次展示，单个文案最大长度为 7,multiton为true时必填</para>
/// <param name="multitonRewardTime">额外观看广告的次数，合法的数据范围为1-4，multiton为true时必填</param>
/// <param name="progressTip">是否开启进度提醒，开启时广告文案为【再看N个获得xx】，关闭时为【 再看1个获得xx】。N表示玩家当前还需额外观看广告的次数。</param>
public abstract void ShowVideoAdWithId(string videoAdid,
    bool multiton,
    string[] multitonRewardMsg,
    int multitonRewardTime,
    bool progressTip,
    Action<bool, int> closeCallback = null,
    Action<int, string> errCallback = null
);
```

#### 插屏广告

```text
/// 创建并播放插屏广告，在广告模块启动15s内不允许展示插屏广告，在任何地方调用API.GetStarkAdManager，就会启动广告模块
/// 两个插屏广告展示间隔不能少于30s
/// 插屏广告支持多实例。简单回调设置，插屏广告完成和错误的回调函数
/// 插屏广告实例只支持展示一次，出现加载错误，或 展示成功，点击关闭按钮或视频广告外的其他地方，广告实例都会自动销毁。下一次需再次创建。
/// 提供接口可以手动销毁
/// 错误码由sdk传出，原因参考
/// https://microapp.bytedance.com/docs/zh-CN/mini-game/develop/open-capacity/ads/tt-create-interstitial-ad
var m_InterAdIns = StarkSDK.API.GetStarkAdManager().CreateInterstitialAd()

void LoadInterstitialAd()
{
    if (m_InterAdIns != null)
        m_InterAdIns.Load();
    else
    {
        PrintText("插屏AD未创建");
    }
}

void ShowInterstitialAd()
{
    PrintText("显示插屏AD");
    if (m_InterAdIns != null)
        m_InterAdIns.Show();
    else
    {
        PrintText("插屏AD未创建");
    }
}

void DestoryInterstitialAd()
{
    PrintText("销毁插屏AD");
    if (m_InterAdIns != null)
        m_InterAdIns.Destory();
    m_InterAdIns = null;
}
```

支持多个实例，每个页面只能展示一个实例，每个实例只能展示一次，销毁后可以再次创建。

注意：广告从网络请求到播放可能失败或因填充率问题无法获取。开发者应始终注册onError监听，**确保处理所有广告异常**。
关闭广告提示toast：

```csharp
StarkAdManager.IsShowLoadAdToast = false
```

### 录屏

```csharp
StarkSDK.API.GetStarkGameRecorder().StartRecord(m_IsRecordAudio, m_MaxRecordTime, OnRecordStart, OnRecordError, OnRecordTimeout)
```

视频分享是抖音 App 的重要分发入口，因此游戏视频的录制和编辑是很重要的功能。
支持游戏录制以及在抖音、头条 App 的分享。
支持传入一系列的时间片段，对录制后的视频进行剪辑。
分享时会利用抖音/头条发布器，可以对视频进行后期处理。

### 绑定抖音号

```csharp
StarkSDK.API.FollowDouYinUserProfile(OnFollowAwemeCallback, OnFollowAwemeError)
```

可跳转至开发者平台绑定的抖音账号，引导用户关注开发者抖音号，便于持续进行游戏内容推广与运营。
由于关注信息涉及用户信息，所以目前只能跳转，无法从回调函数里获取到是否已关注的信息

### 创建快捷方式

```csharp
StarkSDK.API.CreateShortcut(OnCreateShortcut)

void OnCreateShortcut(bool bSuccess)
{
    PrintText("OnCreateShortcut : {0}", bSuccess);
}
```

创建快捷方式在不同机型表现不同，若用户禁用权限，系统会显示引导用户在设置中开启权限的提示框。
### 分享

```nginx
StarkSDK.API.GetStarkShare()
```

可以分享内容到头条圈或抖音。
> **注：**如果只是视频分享，可以直接调用StarkSDK.API.GetStarkGameRecorder().ShareVideo、StarkSDK.API.GetStarkGameRecorder().ShareVideoWithTitleTopics接口。不需要调用StarkSDK.API.GetStarkShare()接口。
> StarkSDK.API.GetStarkShare()是一个通用的分享接口，它可以分享视频，也可以分享其它类型的内容，具体参考小程序开发文档，不过就需要自己封装Json参数。
**该接口以视频分享作为示例：**
参考[小程序通用分享接口参数说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param/)，视频分享参数可以是如下Json内容：

```json
{
    "channel": "video",
    "title": "Some Title",
    "extra": {
        "videoPath": "/xxx/xxx.mp4",//OnRecordComplete拿到 录屏文件 所在路径
        "videoTopics": ["Some Topic1", "Some Topic2"],
        "hashtag_list": ["Some Topic1", "Some Topic2"],
    }
}
```

在C#代码内，封装Json数据并调用分享接口如下：

```csharp
using UNBridgeLib.LitJson;

JsonData shareJson = new JsonData();
shareJson["channel"] = "video";
shareJson["title"] = "Some Title";
shareJson["extra"] = new JsonData();
shareJson["extra"]["videoPath"] = "/xxx/xxx.mp4";//OnRecordComplete拿到 录屏文件 所在路径
JsonData videoTopics = new JsonData();
videoTopics.SetJsonType(JsonType.Array);
videoTopics.Add("Some Topic1");
videoTopics.Add("Some Topic2");
shareJson["extra"]["videoTopics"] = videoTopics;
shareJson["extra"]["hashtag_list"] = videoTopics;
StarkSDK.API.GetStarkShare().ShareAppMessage(() =>
    {
        // Share succeed
    }, (errMsg) =>
    {
        // Share failed
    }, () =>
    {
       // Share cancelled
    }, 
    shareJson);
```

跳转到指定videoId的抖音视频，与分享后返回的videoId (需要在 shareJson中 带上 extraJson["withVideoId"] = true; )配合使用

```csharp
StarkSDK.API.NavigateToVideoView(string videoId) 
```

**菜单面板中分享按钮显示控制**
显示菜单面板中的分享按钮（默认为显示），[对齐小游戏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-show-share-menu/)

```text
StarkSDK.API.GetStarkShare().ShowShareMenu()
```

隐藏菜单面板中的分享按钮，[对齐小游戏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-hide-share-menu)

```text
StarkSDK.API.GetStarkShare().HideShareMenu();
```

### 登录

```csharp
/// <summary>
/// 登录-获取临时登录凭证
/// 强制登录默认为true，即若当前未登录宿主，则会调起宿主的登录窗口, 如果用户点击取消则会调用 fail
/// 如果当前登录宿主，则直接返回success，获取到 code 和 anonymousCode
/// 若强制登录为false，当前登录了宿主则会返回success，可以获取到获取到 code 和 anonymousCode
/// 当前未登录宿主，则只有 anonymousCode
/// code 可以换取 openid, openid 是用户的唯一标识
/// anonymousCode 可以换取 anonymous_openid, 同一台手机 anonymous_openid 是相同的
/// </summary>
/// <param name="forceLogin">未登录时, 是否强制调起登录框</param>
/// <param name="successCallback">登录成功的回调</param>
/// <param name="failedCallback">登录失败的回调</param>
StarkSDK.API.GetAccountManager().Login(OnLoginSuccessCallback successCallback,
                           OnLoginFailedCallback failedCallback,
                           bool forceLogin = true)
```

使用当前宿主的登录信息，如果没有登录，则打开宿主的登录页面进行登录
无法在当前宿主进行其他渠道的登录
code换取openId文档：[文档链接](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/log-in/code-2-session)
### 支付

```csharp

if (CanIUse.StarkPayService.RequestGamePayment)// 有版本需求
{
    Dictionary<string, object> orderInfoParams = new Dictionary<string, object>();
    orderInfoParams["mode"] = "game"; //支付的类型, 目前仅为"game"
    orderInfoParams["env"] = "0"; //环境配置，目前合法值仅为"0"
    orderInfoParams["currencyType"] = "CNY"; // 固定值: CNY。币种
    orderInfoParams["platform"] = "android"; //申请接入时的平台，目前仅为"android"
    orderInfoParams["buyQuantity"] = 1; 
    //金币购买数量，金币数量必须满足：金币数量*金币单价 = 限定价格等级（详见下方 buyQuantity 限制说明。开发者可以在抖音小游戏平台的“支付”tab 设置游戏币单价）
    orderInfoParams["customId"] = (TimeUtils.GetCurrentTimeMs() / 1000).ToString();
    //游戏开发者自定义的唯一订单号，订单支付成功后通过服务端支付结果回调回传
    StarkSDK.API.GetStarkPayService().RequestGamePayment(
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

[支付文档链接](https://developer.open-douyin.com/forum/mini-game/post/639299bfae9fc7233bf53c55)
接入抖音小游戏担保支付。需有版号。
#### 钻石支付
发起抖音钻石支付。

| 前提条件 | 使用前请参考[指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/user-service/douyinIM/)完成IM客服能力接入（运营 - 功能 - 客服管理 - 抖音IM客服），后续充值相关问题用户都会通过该客服进行咨询（**请勿用绑定的抖音号进行支付测试，会导致无法拉起客服界面**）（本步骤未完成报错：`fail im disable`） 接入本能力需要先开通【虚拟支付】和【钻石兑换】能力，请前往开发者平台 在「商业化」>「虚拟支付」申请开通能力 超级管理员通过顶部提示条开通钻石兑换能力 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 支持抖音ios，抖音ios版本大于等于22.5.0时用户可使用 支持抖lite ios，抖lite ios版本大于等于27.5.0时用户可使用 支持 unity 小游戏 |
| 注意事项 | 调用该方法时，需要保证用户已经[登录](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/log-in/tt-login)。可以调用[tt.checkSession](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/log-in/tt-check-session)检测用户登录状态，以避免用户处于未登录状态时支付订单，在登录后无法关联订单与登录后的账户。 异常情况下，充值有可能存在游戏币延迟到账问题，建议游戏在收到支付结果回调后，通过接口 [获取游戏币余额](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/acquire-mini-game-coin-balance) 向服务端轮询最新游戏币余额，间隔 3 秒，持续约 1 分钟，可以根据返回值的 `save_amt` 的变化来确定是否充值成功。 用户成功拉起收银台后即回调成功，未成功拉起收银台即回调失败，与实际支付结果无关，是否支付成功请通过服务端接口查询余额自行保证。 |

**语法**

```csharp
StarkSDK.API.OpenAwemeCustomerService(JsonData options, Action success, Action<int, string>failed);
```

**参数说明**
`options` 为 object 类型，属性如下：

| 属性 | 类型 | 默认值 | 是否必填 | 说明 |
| --- | --- | --- | --- | --- |
| buyQuantity | number |  | 是 | 游戏币购买数量。游戏币数量必须满足：游戏币数量*游戏币单价 = 限定价格等级（详见下方 buyQuantity 限制说明。开发者可以在开发者平台的“支付设置”tab 设置游戏币单价） |
| customId | string |  | 是 | 游戏开发者自定义的唯一订单号，订单支付成功后通过[服务端支付结果回调](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/payment-server-callback)回传 |
| currencyType | string |  | 否 | 币种，目前仅为"DIAMOND" |
| zoneId | string | 1 | 否 | 游戏服务区 id，开发者自定义。游戏不分大区则默认填写"1"。如果应用支持多角色，则角色 ID 接在分区 ID 后，用"_"连接 |
| extraInfo | string |  | 否 | 游戏开发者自定义的其他信息，订单支付成功后通过[服务端支付结果回调](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/payment-server-callback)回传。字符串长度最大不能超过 256。（强烈建议传入） |

**buyQuantity 参数说明**
- 限制说明：购买游戏币的数量，开发者可以在开发者平台的“支付设置”tab 设置游戏币单价, 换算成 RMB 必须满足以下价格档位， 即 buyQuantity * 游戏币单价 = 限定价格等级。如：游戏币单价为 0.1 元，一次购买数量至少是 10 个。

| 限定价格等级（单位：元） | 1 3 6 8 12 18 25 30 40 45 50 60 68 73 78 88 98 108 118 128 148 168 188 198 328 648 998 1288 1998 2998 |
| --- | --- |

- 汇率转换说明：当currencyType为”DIAMOND”时，平台按1:10汇率自动转换。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a725632ec17e411a8b863dedbaf2e5c2)

**回调成功**
object 类型，属性如下：

| 属性 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| errMsg | string | "openAwemeCustomerService:ok"。用户成功拉起收银台即回调成功，与实际支付结果无关。 | 2.64.0 |

**回调失败**
object 类型，属性如下：

| 属性 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| errMsg | string | "openAwemeCustomerService:fail " + 错误详情。用户未拉起收银台即回调失败，与实际支付结果无关。 | 2.64.0 |
| errNo | number | 错误码 | 2.64.0 |

**errNo 的值类型**

| **值** | 说明 | 最低支持版本 |
| --- | --- | --- |
| -1 | 支付失败 | 2.64.0 |
| -2 | 支付取消，用户在确认弹窗点击取消 | 2.64.0 |
| -17001 | 参数检查不通过 | 2.64.0 |
| -17006 | 数量无效 | 2.64.0 |
| -17008 | 获取用户openId失败 | 2.64.0 |
| -17010 | 创建订单失败（常见原因：订单号重复） | 2.64.0 |
| -17011 | 获取分布式锁失败(重复请求) | 2.64.0 |
| -16001 | 暂不支持支付，请按照指引开通能力 | 2.64.0 |
| -15006 | 游戏未在抖音开放平台上进行支付配置（im disable) | 2.64.0 |
| -15098 | 用户未实名 | 2.64.0 |
| -15099 | 用户不能充值 | 2.64.0 |
| -15101 | customId 为空或者不唯一 | 2.64.0 |
| 4 | 网络异常 | 2.64.0 |
| 5 | Android 平台错误，当前平台不支持支付 | 2.64.0 |
| 21113 | face authentication failed，人脸认证失败 | 2.64.0 |

**代码示例**

```csharp
var options = new JsonData
{
    ["buyQuantity"] = 600, // 购买游戏币数量
    ["customId"] = "QWERTYUIDFxxxxx", //开发者自定义唯一订单号。如不填，支付结果回调将不包含此字段，将导致游戏开发者无法发放游戏道具, 基础库版本低于1.55.0没有此字段
    ["currencyType"] = "DIAMOND", // 币种：目前仅为"DIAMOND"
    ["zoneId"] = "1",
    ["extraInfo"] = "{
        userId: "12xxx6", //用户自定义额外信息,支付结果回调信息包含此字段， 基础库版本低于1.55.0没有此字段
        version: "v0.0.0",
        price: "30",
    }" //extraInfo要转成字符串
};

StarkSDK.API.OpenAwemeCustomerService(options, () =>
{
    Debug.Log("OpenAwemeCustomerService success");
}, (errCode, errMsg) =>
{
    Debug.Log($"OpenAwemeCustomerService failed, errCode: {errCode}, errMsg: {errMsg}");
});
```

### 打开客服页
接入小游戏客服消息能力（小6客服）

```csharp
StarkSDK.API.OpenCustomerServicePage(
    (flag) =>
    {
        if (flag)
        {
            PrintTextAppended("成功");
        }
        else
        {
            PrintTextAppended("失败");
        }
    });
```

starksdk5.50.2版本后新增IM客服能力，接口[设计对齐小游戏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/customer-contact/openCustomerServiceConversation)

```sql
JsonData data = new JsonData 
{ 
    ["type"] = 2 
}; 
// data数据：type:(1：小6客服 2:抖音IM 客服(仅支持抖音))sessionFrom:(保留字段，暂时可以不填),例如{"type":1,"sessionFrom":"xxx"}
StarkSDK.API.OpenCustomerServiceConversation(data, (succ) =>{ 
    if (succ) 
    { 
        PrintTextAppended("成功"); 
    } 
    else 
    { 
        PrintTextAppended("失败"); 
    } 
}); 
```

### 自定义事件
`void StarkSDK.API.ReportAnalytics<T>(string eventName, System.Collections.Generic.Dictionary<string, T> param)`
在小程序开发平台-数据分析-自定义分析 中添加事件。
使用 StarkSDK.API.ReportAnalytics 接口上报事件

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/95f5f16ad63a4953a7c7d8e9299953d8)

### 敏感词过滤
> 可以使用敏感词检查接口直接判断是否存在敏感词，并且该接口会返回替换后的文本。
> 在WebGL方案也可以接入`onKeyboardConfirmEvent`与`onKeyboardCompleteEvent`回调，在这两个回调的返回值里会自动替换敏感词文本
**敏感词检查方法**

```csharp
/// <summary>
/// 替换敏感词
/// </summary>
/// <param name="word">要检查和替换的词语</param>
/// <param name="callback">回调
/// int: 返回状态码，0为成功，否则为失败
/// string: 错误信息
/// JsonData：
/// audit_result    int     1: 有敏感内容；0: 无敏感内容
/// audit_content   string  被替换的内容（无敏感内容则返回值与传入的word相同）
/// </param>
[StarkVersion(MinSCAndroidVersion = "1.0.0", IsSupportWebGL = true)]
public abstract void ReplaceSensitiveWords(string word, Action<int, string, JsonData>callback);
```

**键盘监听**

```csharp
/// <summary>
/// 用户点击键盘确定按钮时的事件
/// <param name="value">键盘输入的当前值</param>
/// </summary>
public delegate void OnKeyboardConfirmEvent(string value);

/// <summary>
/// 键盘收起事件
/// <param name="value">键盘输入的当前值</param>
/// </summary>
public delegate void OnKeyboardCompleteEvent(string value);

/// <summary>
/// 监听用户点击键盘确定按钮时的事件
/// </summary>
public OnKeyboardConfirmEvent onKeyboardConfirmEvent;

/// <summary>
/// 监听键盘收起事件
/// </summary>
public OnKeyboardCompleteEvent onKeyboardCompleteEvent;
```

### 周边
可以根据 StarkSDK.s_ContainerEnv 获取宿主，启动入口，版本等相关信息。
可以设置log级别
可以设置在出错时是否显示android下的toast
通过StarkSDK.API.GameVersion 来获取游戏版本号，不要使用 Application.version
**更多功能直接看代码里的接口说明，代码注释比较实时，文档更新可能滞后**
### 排行榜
排行榜功能介绍，同[抖音小游戏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/game-rank/ImRankIntroduce)
Unity侧也提供功能相同，参数相同的接口。（注：使用前请先保证授权登录！）
具体参数可以参照小游戏文档或者StarkSDK的接口注释。

```json
// 在关键的游戏场景，设置写入用户的排行榜数据（游戏成绩信息），该数据会上传到服务端
StarkSDK.API.GetStarkRank().SetImRankData();
// 获取排行榜列表，调用 API 后， 根据参数自动绘制游戏好友排行榜
StarkSDK.API.GetStarkRank().GetImRankList();
```

抖音2770新增排行榜数据分区（zoneId）支持
接口定义

```bash
/// https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/game-rank/setImRankData
/// <summary>
/// 在关键的游戏场景，设置写入用户的排行榜数据（游戏成绩信息），该数据会上传到服务端
/// </summary>
/// <param name="dataType">0：数字类型、1：枚举类型;数字类型（0）往往适用于游戏的通关分数（103分、105分），枚举类型（1）适用于段位信息（青铜、白银）；--(Require)</param>
/// <param name="value">展示出来的数值，dataType == 0 时只能传正数的字符串，否则会报错。value为具体的值，若dataType为0，请传入数字（eg：103、105）；若dataType为1，则传入字符串（eg：青铜、白银）--(Require)</param>
/// <param name="priority">dataType 为 1 时，需要传入这个值判断权重，dataType 为 0 时，不填即可--(Require)</param>
/// <param name="extra">预留字段--(Nullable)</param>
/// <param name="zoneId">排行榜分区标识--(Nullable)默认值为default</param>
/// <param name="paramJson">以上参数使用json格式传入，例如"{"dataType":0,"value":"100","priority":0,"zoneId":"default"}"</param>
/// <param name="action">回调函数</param>
public abstract void SetImRankDataV2(
    JsonData paramJson,
    Action<bool, string> action = null);
    
    
/// <summary>
///获取排行榜列表，调用 API 后， 根据参数自动绘制游戏好友排行榜
/// </summary>
/// <param name="rankType">代表数据排序周期，day为当日写入的数据做排序；week为自然周，month为自然月，all为半年--(Require)</param>
/// <param name="dataType">由于数字类型的数据与枚举类型的数据无法同时排序，因此需要选择排序哪些类型的数据--(Require)</param>
/// <param name="relationType">选择榜单展示范围。default: 好友及总榜都展示，all：仅总榜单--(Nullable)</param>
/// <param name="suffix">数据后缀，最后展示样式为 value + suffix，若suffix传“分”，则展示 103分、104分--(Nullable)</param>
/// <param name="rankTitle">排行榜标题的文案--(Nullable)</param>
/// <param name="zoneId">排行榜分区标识--(Nullable)</param>
/// <param name="paramJson">以上参数使用json格式传入，例如"{"rankType":"week","dataType":0,"relationType":"all","suffix":"分","rankTitle":"","zoneId":"default"}"</param>
/// <param name="action">回调函数</param>
public abstract void GetImRankListV2(JsonData paramJson, 
    Action<bool, string> action = null);
```

使用示例

```bash
void SetImRankDataNew()
{
    var dataType = dataTypeGet.text;
    var value = valueGet.text;
    var priority = priorityGet.text;
    var zoneId = zoneIdGet.text;
    var paramJson = new JsonData
    {
        ["dataType"] = int.Parse(dataType),
        ["value"] = value,
        ["priority"] = int.Parse(priority),
        ["zoneId"] = zoneId
    };
    Debug.Log($"SetImRankData param:{paramJson.ToJson()}");
    StarkSDK.API.GetStarkRank().SetImRankDataV2(paramJson, (isSuccess, errMsg) =>
    {
        if (isSuccess)
        {
        }
        else
        {
        }
    });
}

void GetImRankListNew()
{
    var rankType = rankTypeList.text;
    var dataType = dataTypeList.text;
    var relationType = relationTypeList.text;
    var suffix = suffixList.text;
    var rankTitle = rankTitleList.text;
    var zoneId = zoneIdList.text;
    var paramJson = new JsonData
    {
        ["rankType"] = rankType,
        ["dataType"] = int.Parse(dataType),
        ["relationType"] = relationType,
        ["suffix"] = suffix,
        ["rankTitle"] = rankTitle,
        ["zoneId"] = zoneId,
    }; 
    Debug.Log($"GetImRankList param:{paramJson.ToJson()}");
    StarkSDK.API.GetStarkRank().GetImRankListV2(paramJson, (isSuccess, errMsg) =>
    {
        if (isSuccess)
        {
        }
        else
        {
        }
    });
}
```

### 游戏互推组件能力
[功能介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/grid-game-panel/Gamerecommend)

```sql
///创建组件模块
/// <param name="gridCount">GridGamePanelCount，表示游戏推荐组件的格子数量</param>
/// <param name="query">从组件内打开游戏时附带的query信息</param>
/// <param name="size">GridGamePanelSize，表示组件大小，large：100%，medium：90%，small：80%。仅 gridCount = one | four 时有效。</param>
/// <param name="position">控制游戏推荐组件的展示位置，不传入时默认展示在屏幕右下角。仅 gridCount = one 时有效。</param>
StarkSDK.API.GetStarkGridGamePanelManager().CreateGridGamePanel(GridGamePanelCount gridCount, JsonData query, GridGamePanelSize size, JsonData position)
```

显示

```sql
gridGamePanel.Show();
```

隐藏

```sql
gridGamePanel.Hide();
```

销毁

```sql
gridGamePanel.Destory();
```

### 操作剪贴板
[抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/pasting-board/tt-get-clipboard-data)
**设置剪贴板内容**

```sql
StarkSDK.API.GetStarkClipboard().SetClipboardData(text, (isSucc, errMsg) =>
{
    if (isSucc)
    {
        PrintText("设置成功");
    }
    else
    {
        PrintText("设置失败，"+errMsg );
    }
});
```

**获取剪贴板内容**

```sql
StarkSDK.API.GetStarkClipboard().GetClipboardData((isSucc, contentOrErrMsg) =>
{
    if (isSucc)
    {
        PrintText("获取成功:" + contentOrErrMsg);
    }
    else
    {
        PrintText("获取失败, " + contentOrErrMsg);
    }
});
```

### 屏幕亮度
[对齐小游戏接口](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/screen-intensity/tt-set-keep-screen-on/)
**设置是否保持屏幕常亮状态**

```sql
StarkSDK.API.GetStarkScreenManager().SetKeepScreenOn(true, () =>
{
    PrintText("设置屏幕常亮成功");
}, (msg) =>
{
    PrintText($"设置屏幕常亮失败,{msg}");
});
```

**获取屏幕亮度**

```sql
StarkSDK.API.GetStarkScreenManager().GetScreenBrightness((value) =>
{
    PrintText($"获取屏幕亮度成功,{value}");
}, (msg) =>
{
    PrintText($"获取屏幕亮度失败,{msg}");
});
```

**设置屏幕亮度**

```sql
StarkSDK.API.GetStarkScreenManager().SetScreenBrightness(float.Parse(inputText.text), () =>
{
    PrintText("设置屏幕亮度成功");
}, (msg) =>
{
    PrintText($"设置屏幕亮度失败，${msg}");
});
```

### 启动参数
[tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-get-launch-options-sync/)

```csharp
LaunchOption launchOption = StarkSDK.API.GetLaunchOptionsSync();
```

### 启动场景上报
[tt.reportScene](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/data-analysis/tt-report-scene)

```csharp
/// <summary>
/// 自定义场景数据上报接口
/// </summary>
/// <param name="sceneId">场景ID，int或long类型登录抖音开放平台，进入「数据」-「性能分析」-「启动监控」-「启动场景配置」模块，进入添加事件场景，新建游戏的自定义启动场景。 游戏每次启动只可以上报一次</param>
/// <param name="costTime">场景耗时，单位ms long类型</param>
/// <param name="dimension">自定义维度数据，key在抖音开放平台获取。且序列化后长度不超过1024个字符 </param>
/// <param name="metric">自定义指标数据，key在抖音开放平台获取。且序列化后长度不超过1024个字符 </param>
/// <param name="param">以上参数使用json格式传入，例如"{"sceneId":0,"costTime":10,"dimension":{},"metric":{}}"</param>
/// <param name="success"></param>
/// <param name="failed"></param>
/// <param name="complete"></param>
public void ReportScene(JsonData param,Action<JsonData> success = null,Action<int, string> failed = null, Action complete = null);

//示例
var jsonData = new JsonData();
jsonData["sceneId"] = 100000;
jsonData["costTime"] = 10;
StarkSDK.API.ReportScene(jsonData);
```

## 

### 抖音云相关
> [抖音云托管](https://cloud.douyin.com/)是服务于抖音开放生态的云托管服务，为应用（小程序、小游戏、小玩法）开发者提供后端服务的开发、部署、运行、监控、运维的一站式开发体验。
功能介绍：[抖音云-产品概述](https://developer.open-douyin.com/docs/resource/zh-CN/developer/tools/cloud/introduction/summary)
抖音Unity小游戏C# 接口介绍：[抖音Unity小游戏抖音云接口文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/dycloud-csharp-interface)
### UDPSocket
UDPSocket 为 Unity 小游戏提供了 UDP 通信的能力，该接口仅支持 WebGL 方案。接入参考：[网络通信适配](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_network#1dbceceb)。

```text
StarkSDK.API.CreateUDPSocket();
```

### 触摸事件
[Touch](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/click-event/touch)
触摸监听模块（StarkInput）仅支持WebGL方案，接入参考：[多点触控适配](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc-webgl-touch)。

```csharp
// 监听 TouchStart 事件
StarkSDK.API.GetStarkInput().onTouchStart((StarkTouchEvent touchEvent) => {
    Debug.Log("touchstart: " + touchEvent); 
});
```

### 键盘监听
[tt.showKeyboard](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/keyboard/tt-show-keyboard)
键盘监听模块（StarkKeyboard）仅支持WebGL方案

```csharp
 using StarkSDKSpace;
 using UnityEngine;
 using UnityEngine.UI;

 public class KeyboardTest : MonoBehaviour
 {
     public InputField input;

     private void Start()
     {
         SetInputTexts();
         RegisterKeyboardEvents();
     }

     private void SetInputTexts()
     {
         input.text = "done";
         var comp = input.GetComponent<ClickableInputField>();
         if (comp == null)
         {
             comp = input.gameObject.AddComponent<ClickableInputField>();
         }
         comp.multiple = false;
         comp.confirmType = input.text;
     }

     private void OnDestroy()
     {
         UnregisterKeyboardEvents();
     }

     private void RegisterKeyboardEvents()
     {
         StarkSDK.API.GetStarkKeyboard().onKeyboardInputEvent += OnKeyboardInput;
         StarkSDK.API.GetStarkKeyboard().onKeyboardConfirmEvent += OnKeyboardConfirm;
         StarkSDK.API.GetStarkKeyboard().onKeyboardCompleteEvent += OnKeyboardComplete;
     }

     private void UnregisterKeyboardEvents()
     {
         StarkSDK.API.GetStarkKeyboard().onKeyboardInputEvent -= OnKeyboardInput;
         StarkSDK.API.GetStarkKeyboard().onKeyboardConfirmEvent -= OnKeyboardConfirm;
         StarkSDK.API.GetStarkKeyboard().onKeyboardCompleteEvent -= OnKeyboardComplete;
     }

     private void OnKeyboardInput(string value)
     {
         Debug.Log($"OnKeyboardInput: {value}");
         if (input.isFocused)
         {
             input.text = value;
         }
     }

     private void OnKeyboardConfirm(string value)
     {
         Debug.Log($"OnKeyboardConfirm: {value}");
     }

     private void OnKeyboardComplete(string value)
     {
         Debug.Log($"OnKeyboardComplete: {value}");
     }
 }
 public class ClickableInputField : EventTrigger
 {
     public string confirmType = "done"; // 可选值有: "done", "next", "search", "go", "send"
     public int maxInputLength = 100; // 最大输入长度
     public bool multiple = false; // 是否多行输入
     private InputField _inputField;
     private void Start()
     {
         _inputField = GetComponent<InputField>();
     }
     public override void OnPointerClick(PointerEventData eventData)
     {
         if (_inputField != null)
         {
             if (_inputField.isFocused)
             {
                 StarkSDK.API.GetStarkKeyboard().ShowKeyboard(new StarkKeyboard.ShowKeyboardOptions()
                 {
                     maxLength = maxInputLength,
                     multiple = multiple,
                     defaultValue = _inputField.text,
                     confirmType = confirmType
                 });
             }
         }
     }
 }
```

### 抖音侧边栏复访相关
> SDK底层能力支持开发者调起侧边栏，感知侧边栏进入
小游戏文档：[侧边栏复访能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/-retention/sidebar)
**确认当前宿主版本是否支持跳转到某个小游戏入口场景。**
**接口定义：**

```bash
/// <summary>
/// 确认当前宿主版本是否支持跳转某个小游戏入口场景。
/// </summary>
/// <param name="scene">需要确认的入口场景（目前仅支持的入参为'sidebar'）</param>
/// <param name="success">接口调用成功的回调函数, bool为true说明支持，false表示不支持</param>
/// <param name="complete">接口调用结束的回调函数（调用成功、失败都会执行）</param>
/// <param name="error">接口调用失败的回调函数</param>
public abstract void CheckScene(SceneEnum scene, Action<bool> success, Action complete, Action<int, string> error);
```

**使用案例：**

```bash
StarkSDK.API.GetStarkSideBarManager().CheckScene(StarkSideBar.SceneEnum.SideBar, b =>
{
    PrintText("check scene success，"+b );
}, () =>
{
    PrintText("check scene complete");
}, (errCode, errMsg) =>
{
    PrintText($"check scene error, errCode:{errCode}, errMsg:{errMsg}");
});
```

**调用该API可以跳转到某个小游戏入口场景。**
**接口定义：**

```bash
/// <summary>
/// 调用该API可以跳转到某个小游戏入口场景。
/// </summary>
/// <param name="scene">需要确认的入口场景（目前仅支持的入参为'sidebar'）</param>
/// <param name="success">接口调用成功的回调函数, bool为true说明支持，false表示不支持</param>
/// <param name="complete">接口调用结束的回调函数（调用成功、失败都会执行）</param>
/// <param name="error">接口调用失败的回调函数</param>
public abstract void NavigateToScene(SceneEnum scene, Action success, Action complete, Action<int, string> error);
```

**使用案例：**

```bash
StarkSDK.API.GetStarkSideBarManager().NavigateToScene(StarkSideBar.SceneEnum.SideBar, () =>
{
    PrintText("navigate to scene success");
}, () =>
{
    PrintText("navigate to scene complete");
}, (errCode,errMsg) =>
{
    PrintText($"navigate to scene error, errCode:{errCode}, errMsg:{errMsg}");
});
```

如何感知用户是否是从侧边栏场景进入？
> 首次及从侧边栏场景中进入
  新增OnShowWithDict方法，替代旧的OnShow和onAppShow，返回类型从指定类型改为字典。可以从字典中自行指定获取字段。

| 启动场景 （key） | launchFrom返回值 | location返回值 |
| --- | --- | --- |
| 抖音首页侧边栏 （value） | "homepage" | sidebar_card |

**使用案例：**

```bash
StarkSDK.API.GetStarkAppLifeCycle().OnShowWithDict += OnShowOneParam;

private void OnShowOneParam(Dictionary<string, object> param)
{
    PrintTextAppended($"OnShowOneParam-->${param.ToJson()}");
}
```

> 游戏中途从侧边栏中复访
参照**“23.初始化回调”**中GetLocation和GetLaunchFrom
**使用案例：**

```bash
StarkSDK.s_ContainerEnv.GetLaunchFrom()
StarkSDK.s_ContainerEnv.GetLocation()
```

### 订阅消息能力
[订阅消息能力介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/subscribe-message/introduce)
C# SDK增加订阅消息客户端支持的接口，其余流程参照小游戏文档
**接口定义：**

```bash
/// 请求订阅消息
/// 可以参考 小游戏相关文档 https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/subscribe-message/tt-request-subscribe-message/
/// </summary>
/// <param name="tmplIds">需要订阅的消息模板的 id 的集合，最多支持传入三个 tmplId</param>
/// <param name="success">接口调用成功的回调函数</param>
/// <param name="complete">接口调用结束的回调函数（调用成功、失败都会执行）</param>
/// <param name="failed">接口调用结束的回调函数（调用成功、失败都会执行）</param>
public abstract void RequestSubscribeMessage(List<string> tmplIds,Action<Dictionary<string, string>> success = null,Action complete = null, Action<int, string> failed = null);
```

**使用案例：**

```bash
StarkSDK.API.RequestSubscribeMessage(tmplIds, (data) =>
{
    Debug.Log($"success call request subscribe message, {data.ToJson()}");
    PrintText("success call request subscribe message");
    PrintText(data.ToJson());
    
}, () =>
{
    PrintText("complete call request subscribe message");
}, (errCode, errMsg) =>
{
    PrintText($"complete call requestSubscribeMessage fail,errCode -->{errCode},errMsg-->{errMsg}");
});
```

### 生命周期
[tt.onShow](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-on-show/)
[tt.onHide](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-on-hide)
接口定义

```java
/// <summary>
/// 监听游戏切到后台，统一所有平台
/// </summary>
public OnAppHideEvent OnHide;

/// <summary>
/// 监听游戏到前台，统一所有平台，携带参数的格式为字典，可以根据指定key获取指定数据
/// https://bytedance.feishu.cn/docx/NkzOdcUPXo02bdxl6zqcemGinzb
/// </summary>
public OnShowEventWithDict OnShowWithDict;
```

使用方法

```java
StarkSDK.API.GetStarkAppLifeCycle().OnShowWithDict = (param) =>
{
    Debug.Log($"OnShowOneParam: ${param.ToJson()}");
};

StarkSDK.API.GetStarkAppLifeCycle().OnHide = () => {
    Debug.Log("OnHide");
};
```

### 初始化回调

```java
public class ContainerEnv
{
    public          string              GameAppId               = null;                         // 游戏id
    public          HostEnum            m_HostEnum;                                             // 运行的宿主
    public          LaunchFromEnum      m_LaunchFromEnum;                                       // 启动入口
    
    public SCRuntime GetSCRuntime();
    
    public VersionType GetVersionType();
    
    public string GetLaunchFromStr();
    
    /// <summary>
    /// 获取query字段，即小程序的启动参数，可能为空，使用时需判空
    /// </summary>
    public IReadOnlyDictionary<string, string> GetQueryFromScheme();
    
    /// <summary>
    /// 启动场景（该字段目前只有在「侧边栏」启动场景才会返回，返回的属性值为：sidebar_card）
    /// </summary>
    /// <returns></returns>
    public string GetLocation();
    
    /// <summary>
    /// 启动场景（该字段目前只有在「侧边栏」启动场景才会返回，返回的属性值为：homepage）
    /// </summary>
    /// <returns></returns>
    public string GetLaunchFrom()
    
    /// <summary>
    /// 获取小程序启动时的参数，里面的参数可能为空，使用时需判空; 可以在StarkSDK.init()之后调用，确保得到非空值
    /// </summary>
    public LaunchOption GetLaunchOptionsSync();
}

public delegate void OnStarkContainerInitCallback(ContainerEnv env);

/// <summary>
/// 设置Container初始化成功的回调。获取宿主及入口信息
/// 需要在调用其他api之前调用
/// 非Container下不会有此回调
/// </summary>
/// <param name="callback">初始化完成的回调.</param>
public abstract void SetContainerInitCallback(OnStarkContainerInitCallback callback);
```

### 胶囊按钮位置获取Api
**接口定义**

```bash
/// <summary>
/// 获取菜单按钮（右上角胶囊按钮）的布局位置信息。坐标信息以屏幕左上角为原点。
/// https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/menu/tt-get-menu-button-layout/
/// </summary>
/// <returns>
/// JsonData
/// width  number 宽度，单位：px
/// height number 高度，单位：px
/// top        number 上边界坐标，单位：px
/// right  number 右边界坐标，单位：px
/// bottom number 下边界坐标，单位：px
/// left   number 左边界坐标，单位：px
/// </returns>
public abstract JsonData GetMenuButtonLayout();
```

**使用案例**

```bash
var layoutData = StarkSDK.API.GetMenuButtonLayout();
var width = layoutData.OptGetInt("width");
var height = layoutData.OptGetInt("height");
var top = layoutData.OptGetInt("top");
var left = layoutData.OptGetInt("left");
var pxLeft= Dp2Px(left); 
var pxTop = Dp2Px(top); 
var pxHeight = Dp2Px(height); 
var pxWidth = Dp2Px(width);
GUI.Button(new Rect(pxLeft, pxTop, pxWidth, pxHeight), "不可放置UI", labStyles);
```

### 金币游戏支持（仅抖音lite）
[功能介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/incentive/guidelines)
**接口定义**

```bash
/// <summary>
/// 金币发放or扣除
/// </summary>
/// <param name="type">订单类型,1-发放金币，2-消耗金币, int</param>
/// <param name="bizId">点位ID，在开发者后台中金币配置中获取, string</param>
/// <param name="goldNum">金币数量, int</param>
/// <param name="customId">开发者自定义的订单号, string</param>
/// <param name="paramJson">以上参数使用json的形式传入，例如：{"type":1,"bizId":"xxxxx","goldNum":1,"customId":"xxxx"}</param>
/// <param name="successCallback">执行成功的回调函数，会返回平台订单号,例如：{"orderId":"xxxxx"}</param>
/// <param name="completeCallback">接口调用成功的回调函数</param>
/// <param name="errorCallback">接口调用失败的回调函数</param>
public abstract void RequestGoldOrder(JsonData paramJson,
    Action<JsonData> successCallback, Action completeCallback,
    Action<int, string> errorCallback);
```

**使用案例**

```bash
var bizId = xxx;
var goldNum = xxx;
var customId = xxx;
var paramJson = new JsonData
{
    ["type"] = dropdownEnumsList[dropdownSelectIndex],
    ["bizId"] = bizId,
    ["goldNum"] = goldNum,
    ["customId"] = customId
};
Debug.Log($"RequestGoldOrder param :{paramJson.ToJson()}");
StarkSDK.API.GetStarkGoldCoinGameManager().RequestGoldOrder(paramJson,
    orderId =>
    {
        var printText = $"requestGoldOrder success, {orderId}";
        Debug.Log(printText);
        PrintText(printText);
    }, () =>
    {
        var printText = $"requestGoldOrder complete";
        Debug.Log(printText);
        PrintText(printText);
    },
    (errorCode, errorMsg) =>
    {
        var printText = $"requestGoldOrder error, errorCode :{errorCode}, errorMsg:{errorMsg}";
        Debug.Log(printText);
        PrintText(printText);
    });
```

### 系统字体支持（仅支持WebGL）
游戏中基本上都会使用中文字体，WebGL默认字体中不支持中文。通过系统字体，开发者可无需在包体内引入字体文件，即可使用中文，常用汉字已经过测试，如发现有中文无法支持，请联系开发者进行支持。另外也有可能存在字体无法获取的情况，需开发者做好兜底工作
**接口定义**

```bash
/// <summary>
/// 获取系统字体,仅支持WebGL,AndroidNative方案无需调用此接口，使用默认字体时，便会自动使用系统字体。
/// </summary>
/// <param name="callback">字体资源回调，可为null，开发者需要做好兜底</param>
/// <returns></returns>
public abstract void GetSystemFont(Action<Font> callback);
```

**使用案例**

```bash
public class SystemFont : MonoBehaviour
{
    public Text txt;
    
    void Start()
    {
        StarkSDK.API.GetSystemFont(font =>
            {
                txt.font = font; //将获取到的font赋值给Text组件的font
            }); 
    }
}
```

### 
### 群聊
[抖音普通小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/im-group/joinGroup)，相关解释可以参考该文档
#### 加入群聊
**接口定义**

```bash
/// <summary>
/// 在平台创建群聊，获得 groupid 后，游戏内通过这个方法引导用户加入抖音群
/// </summary>
/// <param name="groupId">群 ID  必填</param>
/// <param name="callback">接口调用成功/失败的回调函数  必填</param>
/// <param name="sessionFrom">会话来源 可空</param>
/// <param name="extraInfo">附加信息 可空</param>
public abstract void JoinGroup(string groupId, Action<bool, string> callback,string sessionFrom = null,string extraInfo = null);
```

**使用案例**

```bash
StarkSDK.API.GetStarkGroup().JoinGroup(groupId, (isSuccess, data) =>
{
    if (isSuccess)
    {
        PrintText($"Call JoinGroup success, {data}");
    }
    else
    {
        PrintText($"Call JoinGroup fail, {data}");
    }
});
```

#### 获取群信息
**接口定义**

```bash
/// <summary>
///查询用户通过小游戏平台创建的群的信息
/// 如游戏开发者在平台创建了群聊 ABC，那么游戏侧可以基于游戏开发者在这个游戏中的 openid，查询其在小游戏平台创建了哪些群，群的状态如何，做游戏内的加群逻辑优化
/// </summary>
/// <param name="openId">建群用户的 openid 必填</param>
/// <param name="onCheckGroupInfoSuccessCallback">接口调用成功的回调函数 必填</param>
/// <param name="onCheckGroupInfoFailCallback">接口调用失败的回调函数 必填</param>
/// <param name="sessionFrom">会话来源 可空</param>
/// <param name="extraInfo">附加信息 可空</param>
public abstract void CheckGroupInfo(string openId,
    OnCheckGroupInfoSuccessCallback onCheckGroupInfoSuccessCallback,
    OnCheckGroupInfoFailCallback onCheckGroupInfoFailCallback,
    string sessionFrom = null,
    string extraInfo = null);
```

**使用案例**

```bash
StarkSDK.API.GetStarkGroup().CheckGroupInfo(openId, (ref List<StarkGroup.GroupInfo> list) =>
{
    PrintText($"Call CheckGroupInfo success, {list.ToJson()}");
}, errMsg =>
{
    PrintText($"Call CheckGroupInfo fail, {errMsg}");
});
```

### 重启游戏
**接口定义**

```text
/// <summary>
/// 重启小游戏
/// </summary>
/// <param name="failCallback">接口调用失败时的回调</param>
public abstract void RestartApp(Action failCallback = null);
```

**使用案例**

```text
StarkSDK.API.RestartApp(() =>
{
    Debug.LogError("重启程序失败");
});
```

### 收藏能力
#### **显示收藏引导**
[功能介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/favorite/tt-show-favorite-guide)
**接口定义**

```csharp
/// <summary>
/// 收藏引导
/// <param name="style">弹窗类型，默认为底部弹窗</param>
/// <param name="content">弹窗文案，仅style为 Tip 时可修改，最多显示 12 个字符。</param>
/// </summary>
public abstract void ShowFavoriteGuide(Style style = Style.BottomBar, string content = "");
```

**使用案例**

```text
StarkSDK.API.GetStarkFavorite().ShowFavoriteGuide(StarkFavorite.Style.TopBar);
```

### 授权相关
#### 获取授权信息
[功能介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/set/tt-get-setting)
**接口定义**

```csharp
/// <summary>
/// 获取用户已经授权过的配置。
/// 结果中只会包含向用户请求过的权限。
/// 与 OpenSetting 的区别是 GetSetting 只会获取配置，而不会打开配置页面。
/// </summary>
/// <param name="onGetSettingSuccess">接口调用成功的回调函数</param>
/// <param name="onGetSettingFail">接口调用失败的回调函数</param>
public abstract void GetSetting(OnGetSettingSuccess onGetSettingSuccess,
    OnGetSettingFail onGetSettingFail);
```

**使用案例**

```csharp
StarkSDK.API.GetAccountManager().GetSetting(
    (auth) => { PrintText($"TestGetSetting info auth: {auth}"); },
    (errMsg) => { PrintText($"TestGetSetting fail: {errMsg}"); });
```

#### 打开授权页面
[功能介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/set/tt-open-setting)
**接口定义**

```csharp
/// <summary>
/// 打开设置页面，返回用户设置过的授权结果。
/// 结果中只会包含用户请求过的权限。
/// 与 GetSetting 的区别是，OpenSetting 会打开设置页面，而 GetSetting 只会返回用户授权的设置信息。
/// <param name="onOpenSettingSuccess">接口调用成功的回调函数</param>
/// <param name="onOpenSettingFail">接口调用失败的回调函数</param>
/// </summary>
public abstract void OpenSetting(OnOpenSettingSuccess onOpenSettingSuccess,
    OnOpenSettingFail onOpenSettingFail);
```

**使用案例**

```csharp
StarkSDK.API.GetAccountManager().OpenSetting(
    (auth) => { PrintText($"TestOpenSetting info new auth: {auth}"); },
    (errMsg) => { PrintText($"TestOpenSetting fail: {errMsg}"); });
```

#### 抖音专用开放能力授权
[功能介绍](https://developer.open-douyhttps://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/authorization/tt-show-douyin-open-auth)
**接口定义**

```csharp
/// <summary>
/// 提供小游戏获取抖音权限的能力，展示出抖音权限授权弹窗。
/// 在使用在接口前，需要小游戏拥有者登录抖音开发平台申请开通小游戏需要的权限。
/// </summary>
public abstract void ShowDouyinOpenAuth(Dictionary<string, DouyinPermissionScopeStatus> scopes,
    OnShowDouyinOpenAuthSuccessCallback successCallback, 
    OnShowDouyinOpenAuthFailedCallback failedCallback);
```

**使用案例**

```csharp
StarkSDK.API.GetAccountManager().ShowDouyinOpenAuth(new Dictionary<string, DouyinPermissionScopeStatus>()
    {
        {"im", DouyinPermissionScopeStatus.Required},
        {"im.media", DouyinPermissionScopeStatus.OptionalUnselected}, 
    },
    (errMsg, ticket, grantPermissions) =>
    {
        PrintText($"TestShowDouyinOpenAuth success. errMsg: {errMsg}, ticket: {ticket}, grantPermissions: {grantPermissions}");
    },
    (errNo, errMsg) =>
    {
        PrintText($"TestShowDouyinOpenAuth fail: {errNo} {errMsg}");
    });
```

### 实名认证
[功能介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/info/authenticate-real-name)
**接口定义**

```csharp
/// <summary>
/// 拉起实名认证窗口。
/// 注意：调用该接口前请确保用户已登录。
/// </summary>
/// <param name="successCallback">实名认证窗口拉起成功回调</param>
/// <param name="failedCallback">实名认证窗口拉起失败回调</param>
public abstract void AuthenticateRealName(OnAuthenticateRealNameSuccessCallback successCallback,
    OnAuthenticateRealNameFailedCallback failedCallback);
```

**使用案例**

```csharp
StarkSDK.API.GetAccountManager().AuthenticateRealName(
    (errMsg) => { PrintText($"TestAuthenticateRealName success: {errMsg}"); },
    (errMsg) => { PrintText($"TestAuthenticateRealName fail: {errMsg}"); });
```

### 复访能力
[功能介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/favorite/tt-show-revisit-guide)
**接口定义**

```csharp
/// <summary>
/// 调起引导用户复访的提示弹窗，目前仅抖音宿主支持。
/// 为了更好的玩家体验，建议在按钮的点击回调中使用。
/// </summary>
/// <param name="callback">调起复访提示回调，true表示成功，false表示失败</param>
public abstract void ShowRevisitGuide(Action<bool> callback);
```

**使用案例**

```csharp
StarkSDK.API.GetStarkFavorite().ShowRevisitGuide((res) => Debug.Log($"ShowRevisitGuide result: {res}"));
```

## 调试运行
### Editor下：
StarkSDKSpace.MockSetting 可以设置开启模拟，可以在editor下对各类回调进行调试

```csharp
//开启关注抖音号API的MOCK
StarkSDKSpace.MockSetting.SwithMockModule(StarkSDKSpace.MockModule.FollowDouyin, true)

//调用API时会弹出调试框
StarkSDK.API.FollowDouYinUserProfile(OnFollowCallback, OnFollowError)
```

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2113526f41d74eefa568e73701794604)

### 真机:
需要bgdt中安装：StarkSDK - Unity Tools
- 连接手机，adb可用的情况下，editor下提供一键构建 - 运行在抖音的工具
- 要注意安装的抖音和build的版本在api上要一致（32位抖音，对应32位游戏。64位抖音对应64位游戏）

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/9ea048c0078545208c9254e977019489)

##### 注意事项
- **要使用自己项目的appid进行测试**，否则广告、关注抖音号、埋点等功能使用的数据会与预期不一致
- 真机调试功能前，必须**先发布一次测试版**才能正常进行调试，否则由于版本号为空，会出现20001错误
- **不支持安卓模拟器**

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2605c891bc88477487a5a5d6f7f4c4a8)

## 发布前check
- 在[小程序开发平台](https://developer.open-douyin.com/)上注册项目；
- 开通激励视频广告等能力；
- 技术指标：
  - 启动游戏后，建议下载不超过 10 MB 资源，可以进入首场景
  - 启动游戏后，建议进入首场景的时间不超过5s
  - 包名不要以.miniapk 结尾
  - 要处理不同宿主下的表现，比如，非抖音环境下，不要显示关注抖音号的提示及入口
  - 关注抖音号功能，平台限制要在日活100以后才能开通，所以入口在没完成开通前，需先关闭

## 发布
[抖音Unity小游戏发布](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_publish)

## 建议开发计划
1. 确认[抖音Unity小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide) 的包体大小要求
1. 分析自身版本的apk包体大小、结合你的资源管理和打包方案，得出是否需要小包化改造、选择改造方案。例如可以粗力度的将场景资源分离，将首次启动不需要的资源分离出来。
1. 接入C# SDK，接入激励视频广告功能，完成在editor下mock的调试方式
1. 完成在抖音中的拉起和广告播放测试

## 四、更新与反馈
### 更新机制
使用bgdt进行各个工具的更新。建议使用最新的stable版本。

### 问题反馈
抖音Unity小游戏意见反馈群:

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/5d860a71fd734687af5cfeb42d8814f3)

## 常见问题
更多问题参见：[抖音Unity小游戏FAQ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_faq)
### 新注册的小游戏，用Editor下的调试工具，可以运行抖音，但是无法运行游戏

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/82d3cff953c145a7a63e507916859684)

  真机调试功能前，必须先发布一次版本才能正常进行调试，不然会出现此错误
### 广告播放出现1004错误
跟广告填充率有关，处理错误回调即可。
### 使用starksdktool进行调试，抖音重启但是不能进入游戏（魅族 Flyme8.1）
解决方案：打开手机管家 - 后台管理，允许抖音在后台运行，即可成功push

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e35b9a6b41e14fd787905bcac1957cef)

### 录制视频结果 errorCode： -109， errMsg：stop record failed
case1： 音频录制有问题, 录制音频需要确保启动录制场景包含至少一个active的audiolistener，如没有，在启动录制时候可能会存在失败，在启动录制前存在如下提示

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a3bcf0504ba1480c93ba9ca29abc91af)

### 录制提示ByteREC init failed， errCode： 202
当前录制不支持Vulkan，通过Project Setting->Players->Android->Other Settings 看下Graphics API是不是开了vulkan，是的话，把vulkan选项移除下。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/74debba1c190459ba647809377b6307f)

### 录制视频黑屏
- 当前录制不支持Vulkan，通过Project Setting->Players->Android->Other Settings 看下Graphics API是不是开了vulkan，是的话，把vulkan选项移除下
- 若未开启Vulkan支持，但录制视频还是为黑屏or录制过程提示GL_INVALID_OPERATION，检查下Project Setting->Players->Android->Resolution and Presentation 中的Blit Type 是否为Never, 若是，确保设置为Always

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d17d055a08464bbda66d0aafeeffc480)

### 使用了URP，录屏后，录制视频不包含2D UI部分
- 解决方案：要把原先Overlay的UI也用URP的渲染管线去渲染。
- 场景里增加相机。Overlay的两个Canvas，都改成用ScreenCamera渲染

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/924165d2eed54efe8308b305baff575e)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/3ba11031fdd44e58b2eb403d8373e530)

MainCamera的Stack里加上这个UICamera

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/57e7a2f9d1dd439fb7d346b53351ee8e)

### 使用添加桌面功能，从桌面启动进入不了游戏 -- 需要先将游戏上线

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/18114d35afe54d7ebae0ec6b6bd81279)

### Native方法，包大小无法达到上传标准
- 不可以使用减少平台架构支持的方法减少包体积
- 可以通过开启il2cpp编译优化来减小il2cpp库的体积

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/cc1d9518dec84da5bd80c12389856788)

StarkAdManager.BannerStyle m_style = new StarkAdManager.BannerStyle();
StarkAdManager.BannerAd m_bannerAdIns = null;
void createBanner()
{
m_style.width = 320;
m_style.left = 10;
m_style.top = 100;
m_bannerAdIns = StarkSDK.API.GetStarkAdManager().CreateBannerAd("your ad id", m_style, 60,
OnAdError, OnBannerLoaded, OnBannerResize);
//m_style.height为只读，其值将由StarkSDK自动更新
}

void OnBannerLoaded()
{
if (m_bannerAdIns != null)
m_bannerAdIns.Show();
}

void changeStyle()
{
int w = m_style.width;                //获取banner宽度大小
int h = m_style.height;               //获取banner高度大小
int sw = px2dp(Screen.width);         //获得屏幕宽度(dp)
int sh = px2dp(Screen.height);        //获得屏幕高度(dp)

m_style.top = sh - h;                //底部
m_style.left = sw / 2 - w / 2;       //中央
m_style.width = w;

m_bannerAdIns.ReSize(m_style);        //使用Resize函数调整位置和大小

}

StarkSDK.API.GetStarkAdManager().CreateBannerAd()

private int px2dp(int px) => (int)(px * (160 / Screen.dpi));
