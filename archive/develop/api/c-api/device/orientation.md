---
title: "转屏"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/device/orientation
update_time: 2025-04-27
---

切换横竖屏，接口调用成功后会执行开发者配置的回调。

| 前提条件 | 使用该能力前请做好 [CanIUse](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/basics/tt-can-i-use) 判断。 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 以下场景下无法使用该能力： 直播场景 x分屏场景 直玩场景 pad场景 折叠屏场景 |
| 注意事项 | 无 |
| 相关教程 | 无 |

## TT.SetDeviceOrientation
> 6.3.1 开始支持该方法
切换小游戏横竖屏。
### 语法

```csharp
public static void SetDeviceOrientation(SetDeviceOrientationParam param)
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| param | SetDeviceOrientationParam | -- | 是 | 切换数据，包含是横屏还是竖屏，成功回调，失败回调，完成回调 |

SetDeviceOrientationParam 的属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| Value | TTDeviceOrientation | 切换为横屏or竖屏 |
| Success | delegate void SetDeviceOrientationSuccessCallback(SuccessResult result) | 接口调用成功的回调函数 |
| Fail | Action<ErrorInfo> | 接口调用失败的回调函数 |
| Complete | Action | 接口调用结束的回调函数（调用成功、失败都会执行） |

TTDeviceOrientation合法值如下：

| **枚举值名** | **说明** |
| --- | --- |
| Portrait | 竖屏 |
| Landscape | 横屏 |

### 错误码

| **errNo** | **errMsg** | **说明** |
| --- | --- | --- |
| 10401 | internal error | 小游戏框架内部错误，有需要请[创建工单](https://developer.open-douyin.com/work-order-page?tab=workOrderRecord)咨询 |
| 21100 | setDeviceOrientation: can't set device orientation in live | 直播场景下禁止使用该API |
| 21101 | setDeviceOrientation: can't set device orientation in x screen | x分屏场景下禁止使用该API |
| 21102 | setDeviceOrientation: can't set device orientation in direct play | 直玩场景下禁止使用该API |
| 21103 | setDeviceOrientation: can't set device orientation in current device model | 当前机型不支持该 API |

### 代码示例
设置横屏

```typescript
private void SetOrientationLandscape()
{
    var param = new SetDeviceOrientationParam
    {
        Value = TTDeviceOrientation.Landscape,
        Success =  result =>
        {
            Debug.Log("SetDeviceOrientation success");
        },
        Fail = result =>
        {
            Debug.Log($"SetDeviceOrientation fail-->{result.ErrMsg}");
        },
        Complete = () =>
        {
            Debug.Log("SetDeviceOrientation complete");
        }
    };
    TT.SetDeviceOrientation(param);
}
```

设置竖屏

```typescript
private void SetOrientationPortrait()
{
    var param = new SetDeviceOrientationParam
    {
        Value = TTDeviceOrientation.Portrait,
        Success =  result =>
        {
            Debug.Log("SetDeviceOrientation success");
        },
        Fail = result =>
        {
            Debug.Log($"SetDeviceOrientation fail-->{result.ErrMsg}");
        },
        Complete = () =>
        {
            Debug.Log("SetDeviceOrientation complete");
        }
    };
    TT.SetDeviceOrientation(param); 
}
```

## TT.OnDeviceOrientationChange
> 6.3.1 开始支持该方法
添加监听转屏消息。
### 语法

```csharp
public static void OnDeviceOrientationChange(OnDeviceOrientationChangeCallback callback)
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| callback | delegate void OnDeviceOrientationChangeCallback(OnDeviceOrientationChangeResult result) | -- | 是 | 增加该参数到收到转屏消息的回调列表 |

### 代码示例

```csharp
private void OnOrientationChange()
{
    TT.OnDeviceOrientationChange((value) =>
    {
        Debug.Log(value.Value.ToString());
    });
}
```

## TT.OffDeviceOrientationChange
> 6.3.1 开始支持该方法
删除监听转屏消息。
### 语法

```csharp
public static void OffDeviceOrientationChange(OnDeviceOrientationChangeCallback callback = null)
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| callback | delegate void OnDeviceOrientationChangeCallback(OnDeviceOrientationChangeResult result) | null | 否 | 删除该转屏消息监听回调 |

### 代码示例

```csharp
private void OffOrientationChange()
{
    TT.OffDeviceOrientationChange(null);
}
```
