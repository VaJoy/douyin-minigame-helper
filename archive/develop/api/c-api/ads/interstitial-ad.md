---
title: "插屏广告"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/ads/interstitial-ad
update_time: 2025-01-03
---

> 注意：
> 该模块对应 [旧版Unity SDK 插屏广告文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#1abe3a67)

## TT.CreateInterstitialAd
[小游戏对应接口描述](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/tt-create-interstitial-ad)
> 6.0.0 开始支持本方法
创建并播放插屏广告。

| 前提条件 | 接入本能力需要先开通【**流量主**】能力，请前往小游戏开发者后台 在「**商业化**」> 「**流量主**」申请开通能力 在「**流量主**」> 「**广告管理**」中创建插屏广告位，获取广告位id |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 目前只能在抖音使用该方法，今日头条等宿主暂不支持。 |
| 注意事项 | 在广告模块启动 15s 内不允许展示插屏广告。 两个插屏广告展示间隔不能少于30s。出现 2002 错误码意味着至少需要等待 30 秒后再重新请求，建议开发者在代码中自行处理。 插屏广告支持多实例。插屏广告组件每次创建都会返回一个全新的实例，默认是隐藏的，需要调用 InterstitialAd.Show 将其显示。 插屏广告实例只支持展示一次，出现加载错误，或 展示成功，点击关闭按钮或视频广告外的其他地方，广告实例都会自动销毁。下一次需再次创建。 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static TTInterstitialAd CreateInterstitialAd(CreateInterstitialAdParam param)
```

> **注意**
> 以下示例代码对应 TTSDK 版本 <= `6.2.0`，已过时。

```csharp
public static TTInterstitialAd CreateInterstitialAd(string interstitialAdId,
    Action<int, string> errCallback = null, 
    Action closeCallback = null, 
    Action loadedCallback = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| interstitialAdId | string | -- | 是 | 插屏广告位的adid |
| errCallback | Action<int, string> | null | 否 | 广告视频错误回调，参数含义 errCode, errMsg 表明错误码和错误描述 |
| loadedCallback | Action | null | 否 | 广告加载回调 |
| closeCallback | Action | null | 否 | 广告关闭回调 |

### 代码示例

```csharp
TTInterstitialAd m_InterAdIns = null;
void CreateInterstitialAd()
{
    var param = new CreateInterstitialAdParam { InterstitialAdId = "xxx" };
    m_InterAdIns = TT.CreateInterstitialAd(param);
    m_InterAdIns.OnClose += () => Debug.Log("插屏广告关闭");
    m_InterAdIns.OnLoad += () => Debug.Log("插屏广告加载");
    m_InterAdIns.OnError += (code, message) => Debug.Log($"错误 ： {code}  {message}");
}
```

## TTInterstitialAd
> 6.0.0 开始支持本方法，WebGL也支持该方法
TTInterstitialAd 对象。
通过 TT.CreateInterstitialAd 创建的广告实例。
### 可用方法

```csharp
/// 加载
public void Load();

/// 显示
public void Show();

/// 是否已加载
public bool IsLoaded();

/// 销毁。
public void Destroy();
```

### 可用事件

```csharp
/// <summary>
/// 绑定 load 事件的监听器。 广告组件成功拉取广告素材时会触发 load 事件的监听器。
/// </summary>
event AdLoadDelegate OnLoad;

/// <summary>
/// 绑定 error 事件的监听器。 广告组件拉取广告素材时如果发生错误，会触发 error 事件的监听器。
/// </summary>
event AdErrorDelegate OnError;

/// <summary>
/// 绑定 close 事件的监听器。 当用户点击了 Video 广告上的关闭按钮时，会触发 close 事件的监听器。
/// </summary>
event AdCloseDelegate OnClose;
```

### 代码示例

```csharp
TTInterstitialAd m_InterAdIns = null;
void CreateInterstitialAd()
{
    var param = new CreateInterstitialAdParam { InterstitialAdId = "xxx" };
    m_InterAdIns = TT.CreateInterstitialAd(param);
    m_InterAdIns.OnClose += () => Debug.Log("插屏广告关闭");
    m_InterAdIns.OnLoad += () => Debug.Log("插屏广告加载");
    m_InterAdIns.OnError += (code, message) => Debug.Log($"错误 ： {code}  {message}");
}

void LoadInterstitialAd()
{
    if (m_InterAdIns != null)
        m_InterAdIns.Load();
    else
    {
        Debug.Log("插屏AD未创建");
    }
}

void ShowInterstitialAd()
{
    Debug.Log("显示插屏AD");
    if (m_InterAdIns != null)
        m_InterAdIns.Show();
    else
    {
        Debug.Log("插屏AD未创建");
    }
}

void DestroyInterstitialAd()
{
    Debug.Log("销毁插屏AD");
    if (m_InterAdIns != null)
        m_InterAdIns.Destroy();
    m_InterAdIns = null;
}
```

> **注意**
> 以下示例代码对应 TTSDK 版本 <= `6.2.0`，已过时。

```csharp
TTInterstitialAd m_InterAdIns = null;
void CreateInterstitialAd()
{
    m_InterAdIns = TT.CreateInterstitialAd(Common.GetInterstitialAdId(),
        OnAdError,
        () => { Debug.Log("插屏广告关闭"); }, () => {  Debug.Log("插屏广告加载"); });
}

void OnAdError(int iErrCode, string errMsg)
{
    Debug.Log("错误 ： " + iErrCode + "  " + errMsg);
}

void LoadInterstitialAd()
{
    if (m_InterAdIns != null)
        m_InterAdIns.Load();
    else
    {
        Debug.Log("插屏AD未创建");
    }
}

void ShowInterstitialAd()
{
    Debug.Log("显示插屏AD");
    if (m_InterAdIns != null)
        m_InterAdIns.Show();
    else
    {
        Debug.Log("插屏AD未创建");
    }
}

void DestroyInterstitialAd()
{
    Debug.Log("销毁插屏AD");
    if (m_InterAdIns != null)
        m_InterAdIns.Destroy();
    m_InterAdIns = null;
}
```

## CreateInterstitialAdParam
> 6.2.1 开始支持
### 语法

```csharp
public class CreateInterstitialAdParam
{
    public string InterstitialAdId;
}
```

## ErrorCode
错误码详情：

| **值** | **异常** | **说明** |
| --- | --- | --- |
| 2001 | 触发频率限制 | 小程序启动一定时间内不允许展示插屏广告 |
| 2002 | 触发频率限制 | 距离小程序插屏广告或者激励视频广告上次播放时间间隔不足，不允许展示插屏广告 |
| 2003 | 触发频率限制 | 当前正在播放激励视频广告或者插屏广告，不允许再次展示插屏广告 |
| 2004 | 广告渲染失败 | 该项错误不是开发者的异常情况，或因小程序页面切换导致广告渲染失败 |
| 2005 | 广告调用异常 | 插屏广告实例不允许跨页面调用 |
