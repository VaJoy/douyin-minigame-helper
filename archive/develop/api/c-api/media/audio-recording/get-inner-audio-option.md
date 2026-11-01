---
title: "GetInnerAudioOption"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/media/audio-recording/get-inner-audio-option
update_time: 2026-08-25
---

## TT.GetInnerAudioOption
> TTSDK 6.9.0 开始支持本方法，这是一个异步方法。
查询小游戏当前音频播放路由状态，包括是否外放及当前音频路由。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 当前不支持 Android，调用会返回 999988 /  The feature is not available in current operating system。 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### 语法

```csharp
public static void GetInnerAudioOption(TTGetInnerAudioOptionParam param)
```

### 参数说明
param 为 TTGetInnerAudioOptionParam 类型，属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| success | Action<TTGetInnerAudioOptionResult> |  | 否 | 接口调用成功的回调函数 | TTSDK 6.9.0 |
| fail | Action<ErrorInfo> |  | 否 | 接口调用失败的回调函数 | TTSDK 6.9.0 |
| complete | Action |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） | TTSDK 6.9.0 |

### 回调成功
TTGetInnerAudioOptionResult 类型，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| speakerOn | bool | 当前是否扬声器外放。 | TTSDK 6.9.0 |
| route | string | 当前真实物理路由：speakerphone/earpiece/headset/bluetooth/unknown。 | TTSDK 6.9.0 |
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
| 21210 | getInnerAudioOption is not supported on current host version | 当前宿主版本不支持该能力，建议先使用 CanIUse 探测。 | TTSDK 6.9.0 |
| 21212 | get audio option failed | iOS 查询音频路由失败。 | TTSDK 6.9.0 |
| 21214 | internal error | 内部错误。 | TTSDK 6.9.0 |
| 10302 | The feature is not available in current operating system | Android 当前操作系统不支持 GetInnerAudioOption。 | TTSDK 6.9.0 |

### 代码示例

```csharp
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
```
