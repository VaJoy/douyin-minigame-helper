---
title: "Banner 广告"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/ads/banner-ads
update_time: 2025-10-11
---

> 注意：
> 该模块对应 [旧版Unity SDK Banner广告文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#a065495e)

## TT.CreateBannerAd
[小游戏对应接口描述](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/tt-create-banner-ad)
> 6.0.0 开始支持本方法
创建 Banner 广告，返回 BannerAd 实例。支持多实例，可以在一个页面下展示多个。也可以分页面展示。

| 前提条件 | 接入本能力需要先开通【**流量主**】能力，请前往小游戏开发者后台 在「**商业化**」> 「**流量主**」申请开通能力 在「**流量主**」> 「**广告管理**」中创建Banner广告位，获取广告位id |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 每个广告实例只会与一条固定的广告素材绑定。开发者如果想要展示另一条广告，需要创建一个新的 bannerAd 实例。  adIntervals 自动刷新并不会保证必须刷新，也不会无限刷新。  竖屏情况下，Banner 广告 接受的最小宽度是 300（设备像素），最大宽度是 Math.floor(屏幕宽度）。  横屏情况下，Banner 广告 接受的最小宽度是 128（设备像素），最大宽度是 208（设备像素）。开发者可以在这之间自由指定广告宽度。广告组件会自动等比例缩放素材。 创建Banner示例后，要主动调用show来进行展示 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static TTBannerAd CreateBannerAd(CreateBannerAdParam param)
```

> **注意**
> 以下示例代码对应 TTSDK 版本 <= `6.2.0`，已过时。

```csharp
public static TTBannerAd CreateBannerAd(string bannerAdId,
    TTBannerStyle style, 
    int adIntervals = -1,
    Action<int, string> errCallback = null, 
    Action loadedCallback = null,
    Action<int, int> resizeCallback = null, 
    Action closeCallback = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| bannerAdId | string | -- | 是 | banner 广告位的 adid |
| style | TTBannerStyle | -- | 是 | 样式："style":{"top":0, "left":0, "width":320}， width 在竖屏下会被限制在 [0.8*ScreenWidth, 1.0*ScreenWidth]，横屏下会被限制在[128, 208] |
| adIntervals | int | -1 | 否 | 广告自动刷新的间隔时间，单位为秒，参数值必须大于等于 30（该参数不传入时 Banner 广告不会自动刷新） |
| errCallback | Action<int, string> | null | 否 | 视频广告错误回调 参数1 int: errCode 错误码 参数2 string: errMsg 错误描述 |
| loadedCallback | Action | null | 否 | 广告加载回调 |
| resizeCallback | Action<int, int> | null | 否 | 广告样式改变回调 参数1 int: width 宽度 参数2 int: height 高度 |
| closeCallback | Action | null | 否 | 广告关闭回调，仅在 WebGL 有效 |

**TTBannerStyle **的属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| left | int | 广告位区域左上角横坐标 |
| top | int | 广告位区域左上角纵坐标 |
| width | int | 广告位区域宽度 |
| height | int  { internal set; get; } | 广告位区域高度，受广告内容影响自主变化, 无法由外部指定 |

### 代码示例

```csharp
public void TestCreatAd()
{
    m_bannerAdIns = TT.CreateBannerAd(Common.GetBannerAdId(), m_style, 60,
        OnAdError, OnBannerLoaded, OnBannerResize, OnClose);
}

void OnAdError(int iErrCode, string errMsg)
{
    Debug.LogError(TAG + "错误 ： " + iErrCode + "  " + errMsg);
}

private void OnBannerLoaded()
{
    m_bannerAdIns?.Show();
    m_result.text = m_result.text + "/n" + "banner广告loaded";
}

private void OnBannerResize(int width, int height)
{
    Debug.Log($"OnBannerResize - width:{width} height:{height}");
}

private void OnClose()
{
    Debug.Log（"banner广告关闭"）;
}
```

## TTBannerAd
> 6.0.0 开始支持本方法，WebGL也支持该方法
BannerAd 对象。
通过 TT.CreateBannerAd 创建的广告实例。
### 可用方法

```csharp
/// 显示。如果加载出错，会调用CreateBannerAd的参数 errCallback
public void Show();

/// 隐藏
public void Hide();

/// 销毁
public  void Destroy();

/// 改变样式
/// 成功后会调用CreateBannerAd的参数 resizeCallback
/// 横屏下可以更改位置和宽度，竖屏下只能更改位置。
public void ReSize(TTBannerStyle style);

/// 是否有效，bannerad在load出错的情况下，
/// 如果adInterval为-1，
/// 则无法再进行刷新。此时认为已失效，需要destroy再重新创建
public void IsInvalid();
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

/// <summary>
/// 开发者除了可以在创建 bannerAd 实例时指定广告的 style，还可以在获得实例后修改其 style 属性中的属性值。一旦广告尺寸发生变化，会触发 resize 事件的监听器。监听器会获得一个包含 width 和 height 属性的对象参数，该参数表征广告的实际渲染尺寸。
/// </summary>
event AdResizeDelegate OnResize;
```

### 代码示例

```csharp
private TTBannerStyle m_style = new TTBannerStyle();
private TTBannerAd m_bannerAdIns;

public void TestCreatAd()
{
    m_style.top = 10;
    m_style.left = 10;
    m_style.width = 320;

    if (m_bannerAdIns != null && m_bannerAdIns.IsInvalid())
    {
        m_bannerAdIns.Destroy();
        m_bannerAdIns = null;
    }

    if (m_bannerAdIns == null)
    {
        var param = new CreateBannerAdParam
        {
            BannerAdId = "xxx",
            Style = m_style,
            AdIntervals = 60
        };
        m_bannerAdIns = TT.CreateBannerAd(param);
        m_bannerAdIns.OnError += OnAdError;
        m_bannerAdIns.OnClose += OnClose;
        m_bannerAdIns.OnResize += OnBannerResize;
        m_bannerAdIns.OnLoad += OnBannerLoaded;
    }
    m_bannerAdIns.Show();
}

void OnAdError(int iErrCode, string errMsg)
{
    Debug.LogError(TAG + "错误 ： " + iErrCode + "  " + errMsg);
}

private void OnBannerLoaded()
{
    m_bannerAdIns?.Show();
    m_result.text = m_result.text + "/n" + "banner广告loaded";
}

private void OnBannerResize(int width, int height)
{
    Debug.Log($"OnBannerResize - width:{width} height:{height}");
}

private void OnClose()
{
    Debug.Log（"banner广告关闭"）;
}

//展示
private void ShowBannerAd()
{
    m_bannerAdIns?.Show();
}

//隐藏
private void HideBannerAd()
{
    m_bannerAdIns?.Hide();
}

//修改尺寸
private void ResizeBannerAd()
{
    m_style.top = int.Parse(inputTop.text);
    m_style.left = int.Parse(inputLeft.text);
    m_style.width = int.Parse(inputWidth.text);
    m_bannerAdIns?.ReSize(m_style);
}

//销毁广告实例
private void DestroyBannerAd()
{
    m_bannerAdIns?.Destroy();
}
```

> **注意**
> 以下示例代码对应 TTSDK 版本 <= `6.2.0`，已过时。

```csharp
TTBannerStyle m_style = new TTBannerStyle();
private TTBannerAd m_bannerAdIns;

public void TestCreatAd()
{
    m_style.top = 10;
    m_style.left = 10;
    m_style.width = 320;
    if (m_bannerAdIns == null)
    {
        m_bannerAdIns = TT.CreateBannerAd(Common.GetBannerAdId(), m_style, 60,
            OnAdError, OnBannerLoaded, OnBannerResize, OnClose);
    }
    // 确定之前的 Banner 是否可用， 不可用则直接销毁
    else if (m_bannerAdIns.IsInvalid())
    {
        m_bannerAdIns.Destroy();
        m_bannerAdIns = TT.CreateBannerAd(Common.GetBannerAdId(), m_style, 60,
           OnAdError, OnBannerLoaded, OnBannerResize,OnClose);
    }
    else
    {
        m_bannerAdIns.Show();
    }
}

void OnAdError(int iErrCode, string errMsg)
{
    Debug.LogError(TAG + "错误 ： " + iErrCode + "  " + errMsg);
}

private void OnBannerLoaded()
{
    m_bannerAdIns?.Show();
    m_result.text = m_result.text + "/n" + "banner广告loaded";
}

private void OnBannerResize(int width, int height)
{
    Debug.Log($"OnBannerResize - width:{width} height:{height}");
}

private void OnClose()
{
    Debug.Log（"banner广告关闭"）;
}

//展示
private void ShowBannerAd()
{
    m_bannerAdIns?.Show();
}

//隐藏
private void HideBannerAd()
{
    m_bannerAdIns?.Hide();
}

//修改尺寸
private void ResizeBannerAd()
{
    m_style.top = int.Parse(inputTop.text);
    m_style.left = int.Parse(inputLeft.text);
    m_style.width = int.Parse(inputWidth.text);
    m_bannerAdIns?.ReSize(m_style);
}

//销毁广告实例
private void DestroyBannerAd()
{
    m_bannerAdIns?.Destroy();
}
```

## CreateBannerAdParam
> 6.2.1 版本开始支持
### 语法

```csharp
public class CreateBannerAdParam
{
    /// <summary>
    /// 广告aid
    /// </summary>
    public string BannerAdId;

    /// <summary>
    /// 样式："style":{"top":0, "left":0, "width":320}} width 在竖屏下会被限制在 [0.8*ScreenWidth,1.0*ScreenWidth]，横屏下会被限制在[128, 208]
    /// </summary>
    public TTBannerStyle Style;

    /// <summary>
    /// 广告自动刷新的间隔时间，单位为秒，参数值必须大于等于 30（该参数不传入时 Banner 广告不会自动刷新）.
    /// </summary>
    public int AdIntervals = -1;
}
```

## ErrorCode
错误码详情：

| **值** | **异常** | **说明** | **解决方案** |
| --- | --- | --- | --- |
| 1000 | 后端错误调用失败 | 该项错误不是开发者的异常情况 | 一般情况下忽略一段时间即可恢复 |
| 1001 | 参数错误 | 使用方法错误 | 查看 api 文档 |
| 1002 | 广告单元无效 | 可能是拼写错误、或者误用了其他 App 的广告 ID |  |
| 1003 | 内部错误 | 该项错误不是开发者的异常情况 | 一般情况下忽略一段时间即可恢复 |
| 1004 | 无适合的广告 | 广告不是每一次都会出现，这次没有出现可能是由于该用户不适合浏览广告 | 属于正常情况，且开发者需要针对这种情况做形态上的兼容。 |
| 1005 | 广告组件审核中 | 广告正在被审核，无法展现广告 |  |
| 1006 | 广告组件被驳回 | 广告审核失败，无法展现广告 |  |
| 1007 | 广告能力被禁用 | 广告能力已经被封禁，封禁期间无法展现广告 |  |
| 1008 | 广告单元已关闭 | 该广告位的广告能力已经被关闭 |  |
| 20002 | 不支持 banner 广告 API | 该 App 暂不支持 banner 广告 | 检测对应的应用(appName)进行兼容，抖音暂不支持 banner 广告 |
| 120002 | 广告发送的次数已达当日上限 | 一般第二天会恢复 |  |
