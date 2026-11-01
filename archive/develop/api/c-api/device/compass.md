---
title: "罗盘"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/device/compass
update_time: 2025-09-02
---

## TT.StartCompass
> 6.5.3开始支持本方法，WebGL也支持该方法
开始监听罗盘数据。罗盘数据会在用户手机发生“朝向变化/加速前进&后退/摇一摇”等手势时触发变化。
### 语法

```csharp
public static void StartCompass(TTStartCompassParam param)
```

### 参数说明
TTStartCompassParam 包含以下参数

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | Action<GeneralCallbackResult> | null | 否 | 成功回调 |
| fail | Action<ErrorInfo> | null | 否 | 失败回调 |
| complete | Action<GeneralCallbackResult> | null | 否 | 完成回调 |

### 回调成功
GeneralCallbackResult包含以下参数：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "startCompass:ok" |

### 回调失败
ErrorInfo包含以下参数：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| ErrorCode | int | 错误码 |
| ErrMsg | string | 错误信息。"startCompass:fail" + 详细错误信息 |

### 代码示例

```csharp
private void Test() {
    TT.StartCompass(new()
    {
        success = (res) =>
        {
            Debug.Log($"StartCompass success, {res.errMsg}");
        },
        fail = (errInfo) =>
        {
            Debug.Log($"StartCompass fail, errorInfo: {errInfo}");
        },
        complete = () =>
        {
            Debug.Log($"StartCompass complete");
        }
    });
}
```

## TT.StopCompass
> 6.5.3开始支持本方法，WebGL也支持该方法
停止监听罗盘数据。
### 语法

```csharp
public static void StopCompass(TTStopCompassParam param)
```

### 参数说明
TTStopCompassParam包含以下参数

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | Action<GeneralCallbackResult> | null | 否 | 成功回调 |
| fail | Action<ErrorInfo> | null | 否 | 失败回调 |
| complete | Action<GeneralCallbackResult> | null | 否 | 完成回调 |

### 回调成功
GeneralCallbackResult包含以下参数：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "stopCompass:ok" |

### 回调失败
ErrorInfo包含以下参数：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| ErrorCode | int | 错误码 |
| ErrMsg | string | 错误信息。"stopCompass:fail" + 详细错误信息 |

### 代码示例

```csharp
private void Test() {
    TT.StopCompass(new()
    {
        success = (res) =>
        {
            Debug.Log($"StopCompass success, {res.errMsg}");
        },
        fail = (errInfo) =>
        {
            Debug.Log($"StopCompass fail, errorInfo: {errInfo}");
        },
        complete = () =>
        {
            Debug.Log($"StopCompass complete");
        }
    });
}
```

## TT.OnCompassChange
> 6.5.3开始支持本方法，WebGL也支持该方法
监听罗盘数据变化事件，罗盘数据会在用户手机发生“朝向变化/加速前进&后退/摇一摇”等手势时触发变化。频率：5 次/秒，接口调用后会自动开始监听，可使用 TT.StopCompass 停止监听。
### 语法

```csharp
public static void OnCompassChange(Action<OnCompassChangedResult> onCompassChanged)
```

### 参数说明
回调 OnCompassChangedResult 包含以下参数

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| direction | double |  |

### 代码示例

```csharp
private void Test() {
    TT.StartCompass();
    TT.OnCompassChanged(OnCompassChangedCallback);
}
    
private void OnCompassChangedCallback(OnCompassChangedResult result)
{
    Debug.Log($"指南针回调数据：{result.ToJson()}");
}
```

## TT.OffCompassChange
> 6.5.3开始支持本方法，WebGL也支持该方法
解绑加速度数据监听器。
### 语法

```csharp
public static void OffCompassChange(Action<OnCompassChangedResult> onCompassChanged = null)
```

### 参数说明
回调 OnCompassChangedResult 包含以下参数

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| direction | double |  |

### 代码示例

```csharp
private void Test() {
    TT.OnCompassChanged(OnCompassChangedCallback);
    TT.OffCompassChanged(OnCompassChangedCallback);
}
    
private void OnCompassChangedCallback(OnCompassChangedResult result)
{
    Debug.Log($"指南针回调数据：{result.ToJson()}");
}
```
