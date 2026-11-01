---
title: "滚轮"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/device/wheel
update_time: 2025-01-02
---

| 前提条件 | [PC 端小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/tutorial) |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 仅支持 PC 端小游戏环境。 仅支持 WebGL 方案。 |
| 注意事项 | 也支持直接使用 [`Input.GetAxis()`](https://docs.unity3d.com/2021.3/Documentation/ScriptReference/Input.GetAxis.html) 等 Unity API 获取滚轮状态。 |
| 相关教程 | 无 |

## TT.OnWheel
> 6.2.1 开始支持该方法
监听鼠标滚轮事件，仅适用于 PC 平台。
### 语法

```csharp
public static void OnWheel(Action<OnWheelListenerResult> result)
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| result | Action<OnWheelListenerResult> | -- | 是 | 鼠标滚轮的回调函数 |

### 回调参数

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| x | double | 事件触发时鼠标所在的位置横坐标 |
| y | double | 事件触发时鼠标所在的位置纵坐标 |
| deltaX | double | 滚轴 x 轴方向滚动量 |
| deltaY | double | 滚轴 y 轴方向滚动量 |
| deltaZ | double | 滚轴 z 轴方向滚动量 |
| timeStamp | long | 高精度时间戳的整数部分 例如：15380 |

### 代码示例

```csharp
private void Test(){
    TT.OnWheel(Callback_OnWheel);
}

private void Callback_OnWheel(OnWheelListenerResult result)
{
    Debug.Log("OnWheel: " + result);
}
```

## TT.OffWheel
> 6.2.1 开始支持该方法
取消鼠标滚轮事件监听，仅适用于 PC 平台。
### 语法

```csharp
public static void OffWheel(Action<OnWheelListenerResult> result)
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| result | Action<OnWheelListenerResult> | -- | 是 | 鼠标滚轮的回调函数 |

### 代码示例

```csharp
private void Test(){
    TT.OffWheel(Callback_OnWheel);
}

private void Callback_OnWheel(OnWheelListenerResult result)
{
    Debug.Log("OnWheel: " + result);
}
```
