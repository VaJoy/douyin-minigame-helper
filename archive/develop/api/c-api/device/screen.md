---
title: "屏幕亮度"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/device/screen
update_time: 2024-10-12
---

> 注意
> 该模块对应 [旧版Unity SDK文档中的 【屏幕亮度】 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#e789843d)

## TT.SetKeepScreenOn
> 6.0.0 开始支持本方法，WebGL也支持该方法
设置是否保持屏幕常亮状态。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 仅在当前小游戏生效，离开小游戏后设置失效。 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void SetKeepScreenOn(
    bool keepScreenOn, 
    Action successCallback = null,
    Action<string> failCallback = null
    )
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| keepScreenOn | bool | -- | 是 | 是否保持屏幕常亮 |
| successCallback | Action | null | 否 | 接口调用成功的回调函数 |
| failCallback | Action<string> | null | 否 | 接口调用失败的回调函数 |

### 代码示例

```csharp
private void Test() {
    TT.SetKeepScreenOn(true, () =>
        {
            Debug.Log("设置屏幕常亮成功");
        }, (msg) =>
        {
            Debug.Log($"设置屏幕常亮失败,{msg}");
        });
    
    
    TT.SetKeepScreenOn(false, () =>
        {
            Debug.Log("关闭屏幕常亮成功");
        }, (msg) =>
        {
            Debug.Log($"关闭 屏幕常亮失败,{msg}");
        });
}
```

## TT.GetScreenBrightness
> 6.0.0 开始支持本方法，WebGL也支持该方法
获取屏幕亮度。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 在没有设置小游戏屏幕亮度的情况下，默认获取系统屏幕亮度 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void GetScreenBrightness(
    Action<double> successCallback = null,
    Action<string> failCallback = null)
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| successCallback | Action<double> | null | 否 | 接口调用成功的回调函数,屏幕亮度值，范围 0 ～ 1。0 最暗，1 最亮。 |
| failCallback | Action<string> | null | 否 | 接口调用失败的回调函数 |

### 代码示例

```csharp
private void Test() {
    TT.GetScreenBrightness((value) =>
    {
        Debug.Log($"获取屏幕亮度成功,{value}");
    }, (msg) =>
    {
        Debug.Log($"获取屏幕亮度失败,{msg}");
    });
}
```

## TT.SetScreenBrightness
> 6.0.0 开始支持本方法，WebGL也支持该方法
设置屏幕亮度。
### **语法 **

```csharp
public static void SetScreenBrightness(
    float value, 
    Action successCallback = null,
    Action<string> failCallback = null)
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| value | float | -- | 是 | 屏幕亮度值，范围 0 ～ 1。（0 最暗，1 最亮） |
| successCallback | Action<double> | null | 否 | 接口调用成功的回调函数,屏幕亮度值，范围 0 ～ 1。0 最暗，1 最亮。 |
| failCallback | Action<string> | null | 否 | 接口调用失败的回调函数 |

### 代码示例

```csharp
private void Test() {
    TT.SetScreenBrightness(float.Parse(inputText.text), () =>
        {
            Debug.Log("设置屏幕亮度成功");
        }, (msg) =>
        {
            Debug.Log($"设置屏幕亮度失败，${msg}");
        });
}
```
