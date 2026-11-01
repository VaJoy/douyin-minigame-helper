---
title: "鼠标"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/device/mouse
update_time: 2025-01-02
---

| 前提条件 | [PC 端小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/tutorial) |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 仅支持 PC 端小游戏环境。 仅支持 WebGL 方案。 |
| 注意事项 | 也支持直接使用 [`Input.GetMouseButton()`](https://docs.unity3d.com/2021.3/Documentation/ScriptReference/Input.GetMouseButton.html) 等 Unity API 获取鼠标状态。 |
| 相关教程 | 无 |

## TT.OnMouseUp
> 6.2.1 开始支持该方法
监听鼠标按键弹起事件，仅适用于 PC 平台。
### 语法

```csharp
public static void OnMouseUp(Action<OnMouseDownListenerResult> result)
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| result | Action<OnMouseDownListenerResult> | -- | 是 | 鼠标按键弹起的回调函数 |

### 回调参数

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| button | double | 按键类型，0左键，1中键，2右键 |
| x | double | 事件触发时鼠标所在的位置横坐标 |
| y | double | 事件触发时鼠标所在的位置纵坐标 |
| timeStamp | long | 高精度时间戳的整数部分 例如：15380 |

### 代码示例

```csharp
private void Test(){
    TT.OnMouseUp(Callback_OnMouseUp);
}

private void Callback_OnMouseUp(OnMouseDownListenerResult result)
{
    Debug.Log("OnMouseUp: " + result);
}
```

## TT.OffMouseUp
> 6.2.1 开始支持该方法
取消鼠标按键弹起事件监听，仅适用于 PC 平台。
### 语法

```csharp
public static void OffMouseUp(Action<OnMouseDownListenerResult> result)
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| result | Action<OnMouseDownListenerResult> | -- | 是 | 鼠标按键弹起的回调函数 |

### 代码示例

```csharp
private void Test(){
    TT.OffMouseUp(Callback_OnMouseUp);
}

private void Callback_OnMouseUp(OnKeyDownListenerResult result)
{
    Debug.Log("OnMouseUp: " + result);
}
```

## TT.OnMouseDown
> 6.2.1 开始支持该方法
监听鼠标按键按下事件，仅适用于 PC 平台。
### 语法

```csharp
public static void OnMouseDown(Action<OnMouseDownListenerResult> result)
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| result | Action<OnMouseDownListenerResult> | -- | 是 | 鼠标按键按下的回调函数 |

### 回调参数

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| button | double | 按键类型，0左键，1中键，2右键 |
| x | double | 事件触发时鼠标所在的位置横坐标 |
| y | double | 事件触发时鼠标所在的位置纵坐标 |
| timeStamp | long | 高精度时间戳的整数部分 例如：15380 |

### 代码示例

```csharp
private void Test(){
    TT.OnMouseDown(Callback_OnMouseDown);
}

private void Callback_OnMouseDown(OnMouseDownListenerResult result)
{
    Debug.Log("OnMouseDown: " + result);
}
```

## TT.OffMouseDown
> 6.2.1 开始支持该方法
取消鼠标按键按下事件监听，仅适用于 PC 平台。
### 语法

```csharp
public static void OffMouseDown(Action<OnMouseDownListenerResult> result)
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| result | Action<OnMouseDownListenerResult> | -- | 是 | 鼠标按键按下的回调函数 |

### 代码示例

```csharp
private void Test(){
    TT.OffMouseDown(Callback_OnMouseDown);
}

private void Callback_OnMouseDown(OnMouseDownListenerResult result)
{
    Debug.Log("OnMouseDown: " + result);
}
```

## TT.OnMouseMove
> 6.2.1 开始支持该方法
监听鼠标移动事件，仅适用于 PC 平台。
### 语法

```csharp
public static void OnMouseMove(Action<OnMouseMoveListenerResult> result)
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| result | Action<OnMouseMoveListenerResult> | -- | 是 | 鼠标移动的回调函数 |

### 回调参数

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| x | double | 事件触发时鼠标所在的位置横坐标 |
| y | double | 事件触发时鼠标所在的位置纵坐标 |
| movementX | double | 鼠标横坐标偏移量 |
| movementY | double | 鼠标纵坐标偏移量 |
| timeStamp | long | 高精度时间戳的整数部分 例如：15380 |

### 代码示例

```csharp
private void Test(){
    TT.OnMouseMove(Callback_OnMouseMove);
}

private void Callback_OnMouseMove(OnMouseMoveListenerResult result)
{
    Debug.Log("OnMouseMove: " + result);
}
```

## TT.OffMouseMove
> 6.2.1 开始支持该方法
取消鼠标移动事件监听，仅适用于 PC 平台。
### 语法

```csharp
public static void OffMouseMove(Action<OnMouseMoveListenerResult> result)
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| result | Action<OnMouseMoveListenerResult> | -- | 是 | 鼠标移动的回调函数 |

### 代码示例

```csharp
private void Test(){
    TT.OffMouseMove(Callback_OnMouseMove);
}

private void Callback_OnMouseMove(OnMouseMoveListenerResult result)
{
    Debug.Log("OnMouseMove: " + result);
}
```
