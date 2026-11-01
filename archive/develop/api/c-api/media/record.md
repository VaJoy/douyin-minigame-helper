---
title: "录屏"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/media/record
update_time: 2025-10-31
---

视频分享是抖音下重要的分发入口，所以对游戏视频的录制，编辑是很重要的功能。
支持游戏录制，及在抖音，头条下的分享。
支持传入一系列的时间片段，对录制后的视频进行剪辑。
分享时会利用抖音/头条 发布器，可以对视频进行后期处理。

> 注意
> 该模块对应 [旧版Unity SDK文档 【录屏】](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#3f8161b4)

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

## TT.GetGameRecorder
> 6.0.0 开始支持本方法
获取录屏相关接口
### **语法 **

```csharp
public static TTGameRecorder GetGameRecorder();
```

### 返回值说明
返回值类型为TTGameRecorder，详情如下
### 代码示例

```csharp
public class TTGameRecordTest : MonoBehaviour
{
    TTGameRecorder m_TTGameRecorder;
    void Start()
    {
        m_TTGameRecorder = TT.GetGameRecorder();
    } 
    // 其他变量或函数...           
}
```

注意！后续代码示例中的m_TTGameRecorder都来自于此代码示例
## TTGameRecorder
### TTGameRecorder.IsShowShareVideoToast
是否显示视频分享Toast UI提示，默认显示
#### 语法

```csharp
public bool IsShowShareVideoToast;
```

#### 代码示例

```csharp
void CloseShowShareVideoToast()
{
    m_TTGameRecorder.IsShowShareVideoToast = false;
    Debug.Log($"TTGameRecorder.IsShowShareVideoToast: {m_TTGameRecorder.IsShowShareVideoToast}");
}
```

### TTGameRecorder.SetCustomKeyFrameInterval
设置录屏关键帧插帧问题
内部默认关键帧间隔1s，若需要更小的关键帧间隔精度，可通过该接口设置关键帧间隔。
插帧思路按照帧间隔在超过下述设置阈值后，将自动将对应到来的帧插成关键帧。
在录制前设置，在下次录制时候即生效。
#### 语法

```csharp
public abstract void SetCustomKeyFrameInterval(int millisecond, Action<bool> callBack);
```

#### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| millisecond | int | true | 否 | 视频关键帧插帧间隔 单位ms，默认值-1，为不插帧 |
| callBack | Action<bool> | 600 | 否 | 是否设置成功回调, true 成功，false 失败 |

#### 代码示例

```csharp
void OnSetIntervalButtonTapped()
{
    m_TTGameRecorder.SetCustomKeyFrameInterval(300, b =>
    {
        Debug.Log("设置间隔成功 " + b);
    });
}
```

### TTGameRecorder.Start
开始录屏
#### 语法

```csharp
public abstract bool Start(
    bool isRecordAudio = true,
    int maxRecordTimeSec = 600,
    TTGameRecorder.OnRecordStartCallback startCallback = null,
    TTGameRecorder.OnRecordErrorCallback errorCallback = null,
    TTGameRecorder.OnRecordCompleteCallback timeoutCallback = null);
```

#### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| isRecordAudio | bool | true | 否 | 否录制声音，默认为录制声音 |
| maxRecordTimeSec | int | 600 | 否 | 最大录制时长，单位 s。小于等于 0 则无限制。默认为10分钟 |
| startCallback | TTGameRecorder.OnRecordStartCallback | null | 否 | 视频录制开始回调 |
| errorCallback | TTGameRecorder.OnRecordErrorCallback | null | 否 | 视频录制失败回调 |
| timeoutCallback | TTGameRecorder.OnRecordCompleteCallback | null | 否 | 视频录制超时回调 |

#### 返回值说明

| 类型 | 说明 |
| --- | --- |
| bool | 函数调用状态，调用成功返回true，否则返回false |

#### 代码示例

```csharp
void OnStartButtonTapped()
{
    if (m_TTGameRecorder.GetVideoRecordState() != TTGameRecorder.VideoRecordState.RECORD_STARTED)
    {
        m_TTGameRecorder.Start(m_IsRecordAudio, 
            m_MaxRecordTime, 
            OnRecordStart, 
            OnRecordError, 
            OnRecordTimeout);
    }  
    else
    {
        Debug.Log("Recorder is started");
    }
}
void OnRecordStart()
{
    Debug.Log("OnRecordStart");
}
void OnRecordError(int errCode, string errMsg)
{
    Debug.Log($"OnRecordError - errCode: {errCode}, errMsg: {errMsg}");
}
void OnRecordTimeout(string videoPath)
{
    Debug.Log($"OnRecordTimeout - videoPath: {videoPath}, video duration: {m_TTGameRecorder.GetRecordDuration() / 1000.0f} s");     
}
```

### TTGameRecorder.Stop
停止录屏
#### 语法

```csharp
public abstract bool Stop(
    TTGameRecorder.OnRecordCompleteCallback completeCallback = null,
    TTGameRecorder.OnRecordErrorCallback errorCallback = null,
    List<TTGameRecorder.TimeRange> clipRanges = null,
    bool autoMerge = true);
```

#### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| completeCallback | TTGameRecorder.OnRecordCompleteCallback | null | 否 | 视频录制完成回调 |
| errorCallback | TTGameRecorder.OnRecordErrorCallback | null | 否 | 视频录制失败回调 |
| clipRanges | List<TTGameRecorder.TimeRange> | null | 否 | 停止后需要对视频进行裁剪的时间片段，如果为null或空列表，则不对视频进行裁剪 |
| autoMerge | bool | true | 否 | 是否对视频裁剪片段进行自动合并。 合并规则: 如果有两段重叠的时间片段，并且重叠部分小于等于1秒，则对这两段进行合并为一段 若autoMerge为true，比如时间片段为{[1000, 5000], [4000, 7000]}，会被合并为{[1000, 7000]}。 若autoMerge为false，将按原始传入的时间片段进行裁剪，是否有重叠，由调用方保证。主要用于自定义裁剪。 |

#### 返回值
调用成功返回true，否则返回false
#### 代码示例

```csharp
void OnStopButtonTapped()
{
    m_TTGameRecorder.Stop(OnRecordComplete, OnRecordError);
}
void OnRecordComplete(string videoPath)
{
    Debug.Log($"OnRecordComplete - videoPath: {videoPath}, video duration: {m_TTGameRecorder.GetRecordDuration() / 1000.0f} s");
}
void OnRecordError(int errCode, string errMsg)
{
    Debug.Log($"OnRecordError - errCode: {errCode}, errMsg: {errMsg}");
}
```

### TTGameRecorder.GetRecordDuration
获取录屏时长
#### 语法

```csharp
public abstract int GetRecordDuration();
```

#### 返回值说明

| 类型 | 说明 |
| --- | --- |
| int | 返回录屏时长，单位 ms |

#### 代码示例

```csharp
void PrintRecordDuration()
{
    Debug.Log($"PrintRecordDuration- video duration: {m_TTGameRecorder.GetRecordDuration() / 1000.0f} s");
}
```

### TTGameRecorder.GetVideoRecordState
获取视频录制状态
#### 语法

```csharp
public abstract TTGameRecorder.VideoRecordState GetVideoRecordState();
```

#### 返回值说明

```csharp
/// <summary>录屏状态枚举</summary>
public enum VideoRecordState
{
  /// <summary>录制开始中</summary>
  RECORD_STARTING,
  /// <summary>录制已开始</summary>
  RECORD_STARTED,
  /// <summary>录制暂停中</summary>
  RECORD_PAUSING,
  /// <summary>录制已暂停</summary>
  RECORD_PAUSED,
  /// <summary>录制停止中</summary>
  RECORD_STOPING,
  /// <summary>录制已停止</summary>
  RECORD_STOPED,
  /// <summary>录制结束</summary>
  RECORD_COMPLETED,
  /// <summary>录制错误</summary>
  RECORD_ERROR,
  /// <summary>录制的视频时长太短</summary>
  RECORD_VIDEO_TOO_SHORT,
}
```

#### 代码示例

```csharp
void PrintState()
{
    Debug.Log($"video record state: {m_TTGameRecorder.GetVideoRecordState()}");
}
```

### TTGameRecorder.SetDefaultBgm
设置默认配乐
给录屏分享设置默认的配乐，若链接不符合要求则不生效
#### 语法

```csharp
public abstract void SetDefaultBgm(string defaultBgm);
```

#### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| defaultBgm | string | -- | 是 | 抖音PGC音乐的短链。 形如 "https://v.douyin.com/JmcxWo8/", null 或者 “”表示取消默认配乐 |

### TTGameRecorder.OnRecordStartCallback
开始录屏回调
#### 语法

```java
public delegate void OnRecordStartCallback();
```

### TTGameRecorder.OnRecordErrorCallback
录屏错误回调
#### 语法

```java
public delegate void OnRecordErrorCallback(int errCode, string errMsg);
```

#### 参数说明

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| errCode | int | 错误码 |
| errMsg | string | 错误消息 |

### TTGameRecorder.OnRecordCompleteCallback
录屏完成回调
#### 语法

```java
public delegate void OnRecordCompleteCallback(string videoPath);
```

#### 参数说明

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| videoPath | string | 实际视频路径 |

### TTGameRecorder.TimeRange
时间片段（用于视频裁剪）
#### 属性说明

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| start | int | 开始时间，单位ms |
| end | int | 结束时间，单位ms |

public abstract void SetEnabled(bool enabled);

void SetEnabled()
{
m_TTGameRecorder.SetEnabled(true);
}

public abstract bool GetEnabled();

void PrintEnableState()
{
Debug.Log($"TTGameRecorder enable state: {m_TTGameRecorder.GetEnabled()}");
}
