---
title: "激励视频广告"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/ads/rewardedvideoad
update_time: 2025-12-17
---

开发者可以在小游戏中使用视频广告获得收入。

> 注意：
> - 该模块对应 [旧版Unity SDK激励视频广告文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#8cabf6ef)
> - 与旧版本不同， 6.0.0 版本之后，激励视频要先创建，再 `.Show` 才会展示广告，开发者需要特别注意

| 前提条件 | 接入本能力需要先开通【**流量主**】能力，请前往小游戏开发者后台 在「**商业化**」> 「**流量主**」申请开通能力 在「**流量主**」> 「**广告管理**」中创建激励视频广告位，获取广告位 id |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 只支持一个实例的激励视频播放，申请多个激励视频广告位是无效的 |
| 注意事项 | 建议开发者在创建广告 CreateRewardedVideoAd 的方法参数中监听广告的状态变化。  视频广告是由客户端原生渲染，覆盖在整个小游戏 Canvas 区域之上。 广告是全屏展示，广告的加载和关闭会触发 OnLoad 和 OnClose, OnError 事件。 在激励广告播放期间，游戏逻辑和渲染都会被暂停，用户不能操作小游戏。  Video 广告目前支持竖屏展示。如果是横屏游戏在展示时会先切到竖屏。 在广告未加载时会发起异步请求，弱网情况下会进行重试。 |
| 相关教程 | 无 |

## TT.CreateRewardedVideoAd
> 6.0.0 开始支持本方法
获取激励广告相关接口。
### **语法**

```csharp
public static TTRewardedVideoAd CreateRewardedVideoAd(CreateRewardedVideoAdParam param)
```

> **注意**
> 以下示例代码对应 TTSDK 版本 <= `6.2.0`，已过时。

```csharp
public static TTRewardedVideoAd CreateRewardedVideoAd(
    string videoAdId,
    Action<bool, int> closeCallback = null,
    Action<int, string> errCallback = null,
    bool multiton = false,
    string[] multitonRewardMsg = null,
    int multitonRewardTime = 0,
    bool progressTip = false
)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| videoAdId | string | -- | 是 | 广告aid |
| closeCallback | Action<bool, int> | null | 否 | 视频广告关闭回调 参数1 bool：广告是否播放完成 参数2 int：关闭code |
| errCallback | Action<int, string> | null | 否 | 视频广告错误回调 参数1 int：errCode 错误码 参数2 string： errMsg 错误描述 |
| multiton | bool | false | 否 | 是否开启再得广告模式 只支持安卓系统的抖音和抖音极速版 |
| multitonRewardMsg | string[] | null | 否 | 再得广告的奖励文案，玩家每看完一个广告都会展示，如【再看1个获得xx】xx就multitonRewardMsg中的文案，按顺序依次展示，单个文案最大长度为 7,multiton为true时必填 |
| multitonRewardTime | int | 0 | 否 | 额外观看广告的次数，合法的数据范围为1-4，multiton为true时必填 |
| progressTip | bool | false | 否 | 是否开启进度提醒，开启时广告文案为【再看N个获得xx】，关闭时为【 再看1个获得xx】。N表示玩家当前还需额外观看广告的次数。 |

### 返回值说明
返回值为 TTRewardedVideoAd 类型。
### 错误码
导航 [错误码](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/rewarded-video-ad/rewarded-video-ad-on-error#c4bb4064) 详情。

> 注意：
> 1004 错误可能是由于广告请求被限制了次数，需要跟广告投放沟通。

### 代码示例
#### 创建激励视频广告
创建激励视频广告，获取 TTRewardedVideoAd，加载、展示、销毁视频等见 TTRewardedVideoAd的代码示例。

```csharp
private TTRewardedVideoAd ad1;

public void TestCreatAd1()
{
    string videoAdId = "xxx";
    var param = new CreateRewardedVideoAdParam { AdUnitId = videoAdId };
    ad1 = TT.CreateRewardedVideoAd(param);
    ad1.OnClose += (ended, count) => Debug.Log($"激励视频关闭 ended: {ended}, count: {count}");
    ad1.OnError += (errorCode, errorMessage) => Debug.Log($"激励视频错误 errorCode: {errorCode}");
}
```

> **注意**
> 以下示例代码对应 TTSDK 版本 <= `6.2.0`，已过时。

```csharp
public void TestCreatAd1()
{
    string videoAdId = "xxx";
    TTRewardedVideoAd ad1 = TT.CreateRewardedVideoAd(
        videoAdId,
        (isClose, closeCode) => { Debug.Log("激励视频关闭 state: " +  isClose + ", code: " +  closeCode); },
        (errorCode, errorMsg) => { Debug.Log("激励视频错误 " + errorCode);}
    );
}
```

#### 创建激励视频（再得）广告

```csharp
private TTRewardedVideoAd ad1;

public void TestCreatAd1()
{
    string videoAdId = "xxx";
    var param = new CreateRewardedVideoAdParam
    {
        AdUnitId = videoAdId,
        Multiton = true,
        MultitonRewardTimes = 3,
        MultitonRewardMsg = ... ,
        ProgressTip = true,
    };
    ad1 = TT.CreateRewardedVideoAd(param);
    ad1.OnClose += (ended, count) => Debug.Log($"激励视频关闭 ended: {ended}, count: {count}");
    ad1.OnError += (errorCode, errorMessage) => Debug.Log($"激励视频错误 errorCode: {errorCode}");
}
```

> **注意**
> 以下示例代码对应 TTSDK 版本 <= `6.2.0`，已过时。

```csharp
public void TestCreatAd2()
{
    string videoAdId = "xxx";
    TTRewardedVideoAd ad2 = TT.CreateRewardedVideoAd(
        videoAdId,  
        (bComplete, count) =>
        {
            Debug.Log("激励视频关闭 " + bComplete + ",Count:" + count);
        }, 
        OnAdError, 
        true, 
        ultitonRewardMsg, 
        3, 
        true);
}
```

## TTRewardedVideoAd
### 代码示例前提
根据 TT.CreateRewardedVideoAd 接口获取广告对象后，将其存放在变量 TTRewardedVideoAd ad1 中，后续的代码示例为对变量 ad1 进行加载，展示，销毁等。

```csharp
public class TestTTRewardedVideoAd: MonoBehaviour
{
    private TTRewardedVideoAd ad1;
    public void TestCreatAd1()
    {
        string videoAdId = "xxx";
        var param = new CreateRewardedVideoAdParam { AdUnitId = videoAdId };
        ad1 = TT.CreateRewardedVideoAd(param);
        ad1.OnClose += (ended, count) => Debug.Log($"激励视频关闭 ended: {ended}, count: {count}");
        ad1.OnError += (errorCode, errorMessage) => Debug.Log($"激励视频错误 errorCode: {errorCode}");
    }
}
```

> **注意**
> 以下示例代码对应 TTSDK 版本 <= `6.2.0`，已过时。

```csharp
public class TestTTRewardedVideoAd: MonoBehaviour
{
    private TTRewardedVideoAd ad1;
    public void TestCreatAd1()
    {
        string videoAdId = "xxx";
        ad1 = TT.CreateRewardedVideoAd(
            videoAdId,
            (isClose, closeCode) => { Debug.Log("激励视频关闭 state: " +  isClose + ", code: " +  closeCode); },
            (errorCode, errorMsg) => { Debug.Log("激励视频错误 " + errorCode);},
        );
    }
}
```

### TTRewardedVideoAd.Load
加载激励视频广告。
#### 语法

```csharp
public abstract void Load();
```

#### 代码示例

```csharp
void TestLoad()
{
    Debug.Log("加载激励视频：");
    ad1.Load();
}
```

### TTRewardedVideoAd.Show
播放激励视频广告。
#### 语法

```csharp
public abstract void Show();
```

#### 代码示例

```csharp
void TestShow()
{
    Debug.Log("展示激励视频：");
    ad1.Show();
}
```

### TTRewardedVideoAd.Destroy
销毁激励视频广告。
#### 语法

```csharp
public abstract void Destroy();
```

#### 代码示例

```csharp
void TestDestroy()
{
    Debug.Log("销毁激励视频：");
    ad1.Destroy();
}
```

### TTRewardedVideoAd.OnLoad (事件)
绑定 load 事件的监听器。 广告组件成功拉取广告素材时会触发 load 事件的监听器。
> 6.2.1 版本开始支持
#### 语法

```csharp
public delegate void AdLoadDelegate();

event AdLoadDelegate OnLoad;
```

### TTRewardedVideoAd.OnError (事件)
绑定 error 事件的监听器。 广告组件拉取广告素材时如果发生错误，会触发 error 事件的监听器。
> 6.2.1 版本开始支持
#### 语法

```csharp
/// <summary>
/// 绑定 error 事件的监听器。 广告组件拉取广告素材和其他情况下如果发生错误，会触发 error 事件的监听器。
/// <param name="code">错误码</param>
/// <param name="message">错误信息</param>
/// </summary>
public delegate void AdErrorDelegate(int code, string message);

event AdErrorDelegate OnError;
```

### TTRewardedVideoAd.OnClose (事件)
绑定 close 事件的监听器。 当用户点击了 Video 广告上的关闭按钮时，会触发 close 事件的监听器。
> 6.2.1 版本开始支持
#### 语法

```csharp
/// <summary>
/// 绑定 close 事件的监听器。 当用户点击了 Video 广告上的关闭按钮时，会触发 close 事件的监听器。
/// <param name="isEnded">用户是否完整观看了视频</param>
/// <param name="count">用户完整观看了几次视频</param>
/// </summary>
public delegate void RewardedAdClosedDelegate(bool isEnded, int count);

event RewardedAdClosedDelegate OnClose;
```

## CreateRewardedVideoAdParam
> 6.2.1 版本开始支持
### 语法

```csharp
public class CreateRewardedVideoAdParam
{
    /// <summary>
    /// 广告aid
    /// </summary>
    public string AdUnitId;

    /// <summary>
    /// 是否开启再得广告模式（只支持安卓系统的抖音和抖音极速版）
    /// </summary>
    public bool Multiton;

    /// <summary>
    /// 再得广告的奖励文案，玩家每看完一个广告都会展示，如【再看1个获得xx】xx就multitonRewardMsg中的文案，按顺序依次展示，单个文案最大长度为 7,multiton为true时必填
    /// </summary>
    public List<string> MultitonRewardMsg;

    /// <summary>
    /// 额外观看广告的次数，合法的数据范围为1-4，multiton为true时必填
    /// </summary>
    public int MultitonRewardTimes;

    /// <summary>
    /// 是否开启进度提醒，开启时广告文案为【再看N个获得xx】，关闭时为【 再看1个获得xx】。N表示玩家当前还需额外观看广告的次数。
    /// </summary>
    public bool ProgressTip;
}
```
