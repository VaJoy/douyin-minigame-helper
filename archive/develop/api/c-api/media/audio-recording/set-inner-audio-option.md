---
title: "SetInnerAudioOption"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/media/audio-recording/set-inner-audio-option
update_time: 2026-08-25
---

## TT.SetInnerAudioOption
> TTSDK 6.9.0 开始支持本方法，这是一个异步方法。
用于在 RecorderManager 录音会话内设置小游戏音频播放路由优先从扬声器输出。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 当前不支持 Android。 |
| 注意事项 | Android 当前不支持 SetInnerAudioOption，调用会返回 999988 / The feature is not available in current operating system。 在 RecorderManager 启动录音之后调用，可设置音频是否优先从扬声器输出； |
| 相关教程 | 无 |

### 语法

```csharp
public static void SetInnerAudioOption(TTSetInnerAudioOptionParam param)
```

### 参数说明
param 为 TTSetInnerAudioOptionParam 类型，属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| speakerOn | bool |  | 是 | true 设置扬声器播放；false 取消扬声器设置，让系统按当前模式和外设状态决定真实输出。 | TTSDK 6.9.0 |
| success | Action<TTSetInnerAudioOptionResult> |  | 否 | 接口调用成功的回调函数 | TTSDK 6.9.0 |
| fail | Action<ErrorInfo> |  | 否 | 接口调用失败的回调函数 | TTSDK 6.9.0 |
| complete | Action |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） | TTSDK 6.9.0 |

### 回调成功
TTSetInnerAudioOptionResult 类型，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| route | string | 设置成功后的真实物理路由：speakerphone/earpiece/headset/bluetooth/unknown。 | TTSDK 6.9.0 |
| errMsg | string | 错误信息。 | TTSDK 6.9.0 |

### 回调失败
ErrorInfo 类型，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| ErrorCode | int | 旧版本错误码，对应 JS 文档中的 errNo。 | TTSDK 6.9.0 |
| ErrMsg | string | 错误信息。 | TTSDK 6.9.0 |
| ErrorType | ErrorType | 错误类型。 | TTSDK 6.9.0 |
| errorCode | int | 新错误码字段。 | TTSDK 6.9.0 |
| errMsg | string | 等价于 ErrMsg，用于 API 规范化。 | TTSDK 6.9.0 |

### 错误码

| ErrorCode | ErrMsg | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| 21210 | setInnerAudioOption is not supported on current host version | 当前宿主版本不支持该能力，建议先使用 CanIUse 探测。 | TTSDK 6.9.0 |
| 21211 | set audio route failed | Recorder 未启动、外设占用或 iOS 系统设置失败。 | TTSDK 6.9.0 |
| 21214 | internal error | 内部错误。 | TTSDK 6.9.0 |
| 10302 | The feature is not available in current operating system | Android 当前操作系统不支持 SetInnerAudioOption。 | TTSDK 6.9.0 |

### 代码示例

```csharp
TT.SetInnerAudioOption(new TTSetInnerAudioOptionParam
{
    speakerOn = true,
    success = result =>
    {
        Debug.Log($"SetInnerAudioOption success, route={result.route}, errMsg={result.errMsg}");
    },
    fail = error =>
    {
        Debug.Log($"SetInnerAudioOption fail, errNo={error.ErrorCode}, errMsg={error.ErrMsg}, errorCode={error.errorCode}");
    },
    complete = () =>
    {
        Debug.Log("SetInnerAudioOption complete");
    }
});
```
