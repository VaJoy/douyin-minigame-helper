---
title: "键盘"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/device/keyboard
update_time: 2025-01-02
---

| 前提条件 | [PC 端小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/tutorial) |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 仅支持 PC 端小游戏环境。 仅支持 WebGL 方案。 |
| 注意事项 | 也支持直接使用 [`Input.GetKey()`](https://docs.unity3d.com/2021.3/Documentation/ScriptReference/Input.GetKey.html) 等 Unity API 获取键盘输入。 |
| 相关教程 | 无 |

## TT.OnKeyUp
> 6.2.1 开始支持该方法
监听键盘按键弹起事件，仅适用于 PC 平台。
### 语法

```csharp
public static void OnKeyUp(Action<OnKeyDownListenerResult> result)
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| result | Action<OnKeyDownListenerResult> | -- | 是 | 键盘按键弹起的回调函数 |

### 回调参数

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| key | string | 同 Web 规范 KeyEvent key 属性 |
| code | string | 同 Web 规范 KeyEvent code 属性 |
| timeStamp | long | 高精度时间戳的整数部分 例如：15380 |

### 代码示例

```csharp
private void Test(){
    TT.OnKeyUp(Callback_OnKeyUp);
}

private void Callback_OnKeyUp(OnKeyDownListenerResult result)
{
    Debug.Log("OnKeyUp: " + result);
}
```

## TT.OffKeyUp
> 6.2.1 开始支持该方法
取消键盘按键弹起事件监听，仅适用于 PC 平台。
### 语法

```csharp
public static void OffKeyUp(Action<OnKeyDownListenerResult> result)
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| result | Action<OnKeyDownListenerResult> | -- | 是 | 键盘按键弹起的回调函数 |

### 代码示例

```csharp
private void Test(){
    TT.OffKeyUp(Callback_OnKeyUp);
}

private void Callback_OnKeyUp(OnKeyDownListenerResult result)
{
    Debug.Log("OnKeyUp: " + result);
}
```

## TT.OnKeyDown
> 6.2.1 开始支持该方法
监听键盘按键按下事件，仅适用于 PC 平台。
### 语法

```csharp
public static void OnKeyDown(Action<OnKeyDownListenerResult> result)
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| result | Action<OnKeyDownListenerResult> | -- | 是 | 键盘按键按下的回调函数 |

### 回调参数

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| key | string | 同 Web 规范 KeyEvent key 属性 |
| code | string | 同 Web 规范 KeyEvent code 属性 |
| timeStamp | long | 高精度时间戳的整数部分 例如：15380 |

### 代码示例

```csharp
private void Test(){
    TT.OnKeyDown(Callback_OnKeyDown);
}

private void Callback_OnKeyDown(OnKeyDownListenerResult result)
{
    Debug.Log("OnKeyDown: " + result);
}
```

## TT.OffKeyDown
> 6.2.1 开始支持该方法
取消键盘按键按下事件监听，仅适用于 PC 平台。
### 语法

```csharp
public static void OffKeyUp(Action<OnKeyDownListenerResult> result)
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| result | Action<OnKeyDownListenerResult> | -- | 是 | 键盘按键按下的回调函数 |

### 代码示例

```csharp
private void Test(){
    TT.OffKeyDown(Callback_OnKeyDown);
}

private void Callback_OnKeyDown(OnKeyDownListenerResult result)
{
    Debug.Log("OnKeyDown: " + result);
}
```
