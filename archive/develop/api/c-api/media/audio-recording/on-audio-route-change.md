---
title: "OnAudioRouteChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/media/audio-recording/on-audio-route-change
update_time: 2026-08-25
---

## TT.OnAudioRouteChange
> TTSDK 6.9.0 开始支持本方法。
监听小游戏音频播放路由或音频设备变化事件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 仅在录音 RecorderManager 期间返回 route 变化事件。 Android OnAudioRouteChange 仅保留设备变化 reason，不承诺真实 route。 |
| 相关教程 | 无 |

### 语法

```csharp
public static void OnAudioRouteChange(TTAudioRouteChangeCallback callback)
```

### 参数说明
#### callback

| 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| TTAudioRouteChangeCallback |  | 是 | 音频路由或设备变化事件的回调函数； iOS 返回真实 route/speakerOn/reason； Android route 固定 unknown、speakerOn 固定 false，仅 reason 表示设备变化原因。 | TTSDK 6.9.0 |

callback 接收 TTAudioRouteChangeResult 类型参数，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| route | string | iOS 当前真实物理路由；Android 固定为 unknown。 | TTSDK 6.9.0 |
| speakerOn | bool | iOS 当前是否外放；Android 固定为 false。 | TTSDK 6.9.0 |
| reason | string | 路由或设备变化原因。 | TTSDK 6.9.0 |

### 返回值
无
### 代码示例

```csharp
TTAudioRouteChangeCallback onAudioRouteChange = result =>
{
    Debug.Log($"AudioRouteChange, route={result.route}, speakerOn={result.speakerOn}, reason={result.reason}");
};

TT.OnAudioRouteChange(onAudioRouteChange);
```

## TT.OffAudioRouteChange
> TTSDK 6.9.0 开始支持本方法。
取消当前 OnAudioRouteChange 监听。当前 Unity 封装仅保留最近一次注册的回调；调用 OffAudioRouteChange 时，无论是否传入 callback，都会取消当前监听。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | Recorder stop 不会自动清除 Unity callback；不再需要监听时应显式调用 OffAudioRouteChange。 Android OnAudioRouteChange 仅保留设备变化 reason，不承诺真实 route。 |
| 相关教程 | 无 |

### 语法

```csharp
public static void OffAudioRouteChange(TTAudioRouteChangeCallback callback = null)
```

### 参数说明
#### callback

| 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| TTAudioRouteChangeCallback |  | 否 | 当前 Unity 封装仅保留最近一次注册的回调；调用 OffAudioRouteChange 时，无论是否传入 callback，都会取消当前监听。 | TTSDK 6.9.0 |

callback 接收 TTAudioRouteChangeResult 类型参数，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| route | string | iOS 当前真实物理路由；Android 固定为 unknown。 | TTSDK 6.9.0 |
| speakerOn | bool | iOS 当前是否外放；Android 固定为 false。 | TTSDK 6.9.0 |
| reason | string | 路由或设备变化原因。 | TTSDK 6.9.0 |

### 返回值
无
### 代码示例

```csharp
TT.OffAudioRouteChange(onAudioRouteChange); // 取消当前监听
TT.OffAudioRouteChange(); // 取消当前监听
```
