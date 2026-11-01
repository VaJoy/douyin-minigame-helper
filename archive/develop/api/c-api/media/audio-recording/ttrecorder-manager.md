---
title: "TTRecorderManager"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/media/audio-recording/ttrecorder-manager
update_time: 2026-08-25
---

TTRecorderManager 提供录音开始、停止、暂停、恢复、事件监听与回调清理能力。调用前可通过 TT.GetTTRecorderManager() 获取实例。

| 方法名 | 说明 | 最低支持版本 |
| --- | --- | --- |
| TTRecorderManager.Start | 开始录音。 | TTSDK 6.5.3 |
| TTRecorderManager.Stop | 停止录音。 | TTSDK 6.5.3 |
| TTRecorderManager.Pause | 暂停录音。 | TTSDK 6.5.3 |
| TTRecorderManager.Resume | 继续录音。 | TTSDK 6.5.3 |
| TTRecorderManager.OnStart / TTRecorderManager.OffStart | 监听 / 取消监听录音开始事件。 | TTSDK 6.5.3 |
| TTRecorderManager.OnStop / TTRecorderManager.OffStop | 监听 / 取消监听录音结束事件。 | TTSDK 6.5.3 |
| TTRecorderManager.OnPause / TTRecorderManager.OffPause | 监听 / 取消监听录音暂停事件。 | TTSDK 6.5.3 |
| TTRecorderManager.OnResume / TTRecorderManager.OffResume | 监听 / 取消监听继续录音事件。 | TTSDK 6.5.3 |
| TTRecorderManager.OnError / TTRecorderManager.OffError | 监听 / 取消监听录音错误事件。 | TTSDK 6.5.3 |
| TTRecorderManager.OnFrameRecorded / TTRecorderManager.OffFrameRecorded | 监听 / 取消监听已录制完指定帧大小的文件事件。需要帧数据时建议显式传入大于 0 的 frameSize，并使用 pcm 格式。 | TTSDK 6.5.3 |
| TTRecorderManager.ClearCallbacks | 清除当前 TTRecorderManager 实例上的全部录音事件回调。 | TTSDK 6.5.3 |

## TTRecorderManager.Start
> TTSDK 6.5.3 开始支持本方法。
开始录音。调用前可通过 TT.GetTTRecorderManager() 获取录音管理器实例。

| 前提条件 | 该方法需要用户授权方可调用，详细信息可参考[用户授权](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/other/user-authorization/)。 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 录音格式由宿主能力决定；基础库默认 Android 使用 pcm，其他平台使用 aac。需要帧数据时建议显式传入大于 0 的 frameSize，并使用 pcm 格式；是否触发以宿主侧最终生效参数和平台能力为准。 |
| 注意事项 | sampleRate 与 encodeBitRate 需要满足有效组合；建议显式传入 duration，未传入时默认录制 600000 ms，传入小于 0 或超过宿主限制时按 600000 ms 处理。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void Start(TTStartRecordParam param)
```

### 参数说明
param 为 TTStartRecordParam 类型，属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| duration | int? | 600000 | 否 | 录音自动结束时长，单位 ms。默认值为 600000，即 10 分钟。 | TTSDK 6.5.3 |
| sampleRate | int? | 8000 | 否 | 采样率。 | TTSDK 6.5.3 |
| numberOfChannels | int? | 2 | 否 | 录音通道数，支持 1 个通道或 2 个通道。 | TTSDK 6.5.3 |
| encodeBitRate | int? | 48000 | 否 | 码率。不同采样率对应不同有效码率范围，设置不合法会导致录音失败。 | TTSDK 6.5.3 |
| frameSize | int? | 8000 | 否 | 帧大小，单位 KB。如果设置了值，每当录音内容达到帧大小时会通过 TTRecorderManager.OnFrameRecorded 返回内容。 | TTSDK 6.5.3 |
| format | string | Android 默认 pcm；其他平台默认 aac | 否 | 录音格式，可选值包括 aac、pcm、wav。按帧处理 PCM 数据时建议设置为 pcm。 | TTSDK 6.7.3 |

### 返回值
无
### 代码示例

```csharp
public void Test()
{
    var param = new TTStartRecordParam
    {
        duration = 3000,
        sampleRate = 8000,
        numberOfChannels = 2,
        encodeBitRate = 48000,
        frameSize = 100,
        format = "pcm"
    };

    TT.GetTTRecorderManager().Start(param);
}
```

## TTRecorderManager.Stop
> TTSDK 6.5.3 开始支持本方法。
停止录音。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 停止成功后会触发 OnStop 监听，返回录音临时文件路径。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void Stop()
```

### 参数说明
无
### 返回值
无
### 代码示例

```csharp
public void Test()
{
    TT.GetTTRecorderManager().Stop();
}
```

## TTRecorderManager.Pause
> TTSDK 6.5.3 开始支持本方法。
暂停录音。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 暂停成功后会触发 OnPause 监听。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void Pause()
```

### 参数说明
无
### 返回值
无
### 代码示例

```csharp
public void Test()
{
    TT.GetTTRecorderManager().Pause();
}
```

## TTRecorderManager.Resume
> TTSDK 6.5.3 开始支持本方法。
继续录音。在调用 Pause 暂停录音之后，可以调用 Resume 继续录音，继续录音的内容会拼接到上一次暂停录音之后。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 恢复成功后会触发 OnResume 监听。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void Resume()
```

### 参数说明
无
### 返回值
无
### 代码示例

```csharp
public void Test()
{
    TT.GetTTRecorderManager().Resume();
}
```

## TTRecorderManager.OnStart
> TTSDK 6.5.3 开始支持本方法。
监听录音开始事件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 同一个回调重复注册会重复触发；不再需要监听时请调用 OffStart。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void OnStart(Action onStart)
```

### 参数说明
#### onStart

| 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| Action |  | 是 | 录音开始事件的回调函数。 | TTSDK 6.5.3 |

### 返回值
无
### 代码示例

```csharp
public void Test()
{
    TT.GetTTRecorderManager().OnStart(OnStart);
}

private void OnStart()
{
    Debug.Log("开始录音");
}
```

## TTRecorderManager.OffStart
> TTSDK 6.5.3 开始支持本方法。
取消监听录音开始事件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 需要传入与 OnStart 注册时相同的回调实例。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void OffStart(Action onStart)
```

### 参数说明
#### onStart

| 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| Action |  | 是 | 要取消的录音开始事件回调函数。 | TTSDK 6.5.3 |

### 返回值
无
### 代码示例

```csharp
TT.GetTTRecorderManager().OffStart(OnStart);
```

## TTRecorderManager.OnStop
> TTSDK 6.5.3 开始支持本方法。
监听录音结束事件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 同一个回调重复注册会重复触发；不再需要监听时请调用 OffStop。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void OnStop(Action<OnStopCallbackResult> onStop)
```

### 参数说明
#### onStop

| 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| Action<OnStopCallbackResult> |  | 是 | 录音结束事件的回调函数。 | TTSDK 6.5.3 |

onStop 接收 OnStopCallbackResult 类型参数，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| tempFilePath | string | 录音文件的临时路径。 | TTSDK 6.5.3 |

### 返回值
无
### 代码示例

```csharp
public void Test()
{
    TT.GetTTRecorderManager().OnStop(OnStop);
}

private void OnStop(OnStopCallbackResult result)
{
    Debug.Log($"Recorder stopped successfully. Temp file path: {result.tempFilePath}");
}
```

## TTRecorderManager.OffStop
> TTSDK 6.5.3 开始支持本方法。
取消监听录音结束事件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 需要传入与 OnStop 注册时相同的回调实例。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void OffStop(Action<OnStopCallbackResult> onStop)
```

### 参数说明
#### onStop

| 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| Action<OnStopCallbackResult> |  | 是 | 要取消的录音结束事件回调函数。 | TTSDK 6.5.3 |

### 返回值
无
### 代码示例

```csharp
TT.GetTTRecorderManager().OffStop(OnStop);
```

## TTRecorderManager.OnPause
> TTSDK 6.5.3 开始支持本方法。
监听录音暂停事件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 同一个回调重复注册会重复触发；不再需要监听时请调用 OffPause。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void OnPause(Action onPause)
```

### 参数说明
#### onPause

| 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| Action |  | 是 | 录音暂停事件的回调函数。 | TTSDK 6.5.3 |

### 返回值
无
### 代码示例

```csharp
public void Test()
{
    TT.GetTTRecorderManager().OnPause(OnPause);
}

private void OnPause()
{
    Debug.Log("暂停录音");
}
```

## TTRecorderManager.OffPause
> TTSDK 6.5.3 开始支持本方法。
取消监听录音暂停事件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 需要传入与 OnPause 注册时相同的回调实例。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void OffPause(Action onPause)
```

### 参数说明
#### onPause

| 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| Action |  | 是 | 要取消的录音暂停事件回调函数。 | TTSDK 6.5.3 |

### 返回值
无
### 代码示例

```csharp
TT.GetTTRecorderManager().OffPause(OnPause);
```

## TTRecorderManager.OnResume
> TTSDK 6.5.3 开始支持本方法。
监听继续录音事件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 同一个回调重复注册会重复触发；不再需要监听时请调用 OffResume。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void OnResume(Action onResume)
```

### 参数说明
#### onResume

| 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| Action |  | 是 | 录音继续事件的回调函数。 | TTSDK 6.5.3 |

### 返回值
无
### 代码示例

```csharp
public void Test()
{
    TT.GetTTRecorderManager().OnResume(OnResume);
}

private void OnResume()
{
    Debug.Log("继续录音");
}
```

## TTRecorderManager.OffResume
> TTSDK 6.5.3 开始支持本方法。
取消监听录音恢复事件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 需要传入与 OnResume 注册时相同的回调实例。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void OffResume(Action onResume)
```

### 参数说明
#### onResume

| 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| Action |  | 是 | 要取消的录音恢复事件回调函数。 | TTSDK 6.5.3 |

### 返回值
无
### 代码示例

```csharp
TT.GetTTRecorderManager().OffResume(OnResume);
```

## TTRecorderManager.OnError
> TTSDK 6.5.3 开始支持本方法。
监听录音错误事件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 同一个回调重复注册会重复触发；不再需要监听时请调用 OffError。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void OnError(Action<OnErrorCallbackResult> onError)
```

### 参数说明
#### onError

| 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| Action<OnErrorCallbackResult> |  | 是 | 录音错误事件的回调函数。 | TTSDK 6.5.3 |

onError 接收 OnErrorCallbackResult 类型参数，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| errMsg | string | 录音错误信息。 | TTSDK 6.5.3 |

### 返回值
无
### 代码示例

```csharp
public void Test()
{
    TT.GetTTRecorderManager().OnError(OnError);
}

private void OnError(OnErrorCallbackResult result)
{
    Debug.Log($"Recorder error: {result.errMsg}");
}
```

## TTRecorderManager.OffError
> TTSDK 6.5.3 开始支持本方法。
取消监听录音错误事件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 需要传入与 OnError 注册时相同的回调实例。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void OffError(Action<OnErrorCallbackResult> onError)
```

### 参数说明
#### onError

| 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| Action<OnErrorCallbackResult> |  | 是 | 要取消的录音错误事件回调函数。 | TTSDK 6.5.3 |

### 返回值
无
### 代码示例

```csharp
TT.GetTTRecorderManager().OffError(OnError);
```

## TTRecorderManager.OnFrameRecorded
> TTSDK 6.5.3 开始支持本方法。
监听已录制完指定帧大小的文件事件。建议需要帧数据时显式传入大于 0 的 frameSize，并使用 pcm 格式；未显式设置时，不同运行环境可能不会触发帧数据回调。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 建议在 Start 参数中显式设置大于 0 的 frameSize，并使用 pcm 格式；是否触发以宿主侧最终生效参数和平台能力为准。 |
| 注意事项 | 若设置的 frameSize 大于整个音频大小，则在音频结束时一次性输出。Unity 层可直接读取 frameBuffer 获取 byte[] 帧数据。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void OnFrameRecorded(Action<OnFrameRecordedCallbackResult> onFrameRecorded)
```

### 参数说明
#### onFrameRecorded

| 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| Action<OnFrameRecordedCallbackResult> |  | 是 | 录音帧事件的回调函数。 | TTSDK 6.5.3 |

onFrameRecorded 接收 OnFrameRecordedCallbackResult 类型参数，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| isLastFrame | bool | 是否为最后一帧。 | TTSDK 6.5.3 |
| frameBufferBase64 | string | 录音分片数据的 Base64 字符串，主要用于承接 JS 侧帧数据。 | TTSDK 6.7.3 |
| frameBuffer | byte[] | 录音分片数据。Unity 层首次访问时由 frameBufferBase64 懒解码生成。 | TTSDK 6.7.3 |

### 返回值
无
### 代码示例

```csharp
public void Test()
{
    TT.GetTTRecorderManager().OnFrameRecorded(OnFrameRecorded);
}

private void OnFrameRecorded(OnFrameRecordedCallbackResult result)
{
    var frameLength = result.frameBuffer != null ? result.frameBuffer.Length : 0;
    Debug.Log($"isLastFrame={result.isLastFrame}, frameLength={frameLength}");
}
```

## TTRecorderManager.OffFrameRecorded
> TTSDK 6.5.3 开始支持本方法。
取消监听录音帧事件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 需要传入与 OnFrameRecorded 注册时相同的回调实例。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void OffFrameRecorded(Action<OnFrameRecordedCallbackResult> onFrameRecorded)
```

### 参数说明
#### onFrameRecorded

| 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| Action<OnFrameRecordedCallbackResult> |  | 是 | 要取消的录音帧事件回调函数。 | TTSDK 6.5.3 |

### 返回值
无
### 代码示例

```csharp
TT.GetTTRecorderManager().OffFrameRecorded(OnFrameRecorded);
```

## TTRecorderManager.ClearCallbacks
> TTSDK 6.5.3 开始支持本方法。
清除当前 TTRecorderManager 实例上的全部录音事件回调。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 会清空 OnStart、OnStop、OnError、OnPause、OnResume 和 OnFrameRecorded 注册过的回调。 |
| 相关教程 | 无 |

### 语法

```csharp
public abstract void ClearCallbacks()
```

### 参数说明
无
### 返回值
无
### 代码示例

```csharp
TT.GetTTRecorderManager().ClearCallbacks();
```

public static void OffAudioRouteChange(TTAudioRouteChangeCallback callback = null)

public static void OnAudioRouteChange(TTAudioRouteChangeCallback callback)

TT.OffAudioRouteChange(onAudioRouteChange); // 取消当前监听
TT.OffAudioRouteChange(); // 取消当前监听

public static void SetInnerAudioOption(TTSetInnerAudioOptionParam param)

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

TTAudioRouteChangeCallback onAudioRouteChange = result =>
{
Debug.Log($"AudioRouteChange, route={result.route}, speakerOn={result.speakerOn}, reason={result.reason}");
};

TT.OnAudioRouteChange(onAudioRouteChange);

TT.GetInnerAudioOption(new TTGetInnerAudioOptionParam
{
success = result =>
{
Debug.Log($"GetInnerAudioOption success, speakerOn={result.speakerOn}, route={result.route}, errMsg={result.errMsg}");
},
fail = error =>
{
Debug.Log($"GetInnerAudioOption fail, errNo={error.ErrorCode}, errMsg={error.ErrMsg}, errorCode={error.errorCode}");
},
complete = () =>
{
Debug.Log("GetInnerAudioOption complete");
}
});

private void Test()
{
TTRecorderManager recorderManager = TT.GetTTRecorderManager();
}

public static void GetInnerAudioOption(TTGetInnerAudioOptionParam param)

public static TTRecorderManager GetTTRecorderManager()
