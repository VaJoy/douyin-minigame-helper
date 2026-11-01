---
title: "触摸事件"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/system/touch-event
update_time: 2024-10-12
---

输入模块，仅 webgl 支持。

> 注意：
> 该模块对应 [输入模块](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#76989268)

| 前提条件 | Unity WebGL 小游戏 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

## TT.OnTouchStart
> 6.0.0 开始支持本方法，仅 webgl 支持
监听开始触摸事件。
### **语法 **

```csharp
public static void OnTouchStart(TTInput.TouchEventCallback callback)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| callback | TTInput.TouchEventCallback | -- | 是 | 监听事件处理 |

### 代码示例

```csharp
public void TestInput()
{
    TT.OnTouchStart(evt =>
    {
        Debug.Log($"OnTouchStart {evt}");
    });
}
```

## TT.OnTouchMove
> 6.0.0 开始支持本方法，仅 webgl 支持
监听触点移动事件。
### **语法 **

```csharp
public static void OnTouchMove(TTInput.TouchEventCallback callback)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| callback | TTInput.TouchEventCallback | -- | 是 | 监听事件处理 |

### 代码示例

```csharp
public void TestInput()
{
    TT.OnTouchMove(evt =>
    {
        Debug.Log($"OnTouchMove {evt}");
    });
}
```

## TT.OnTouchEnd
> 6.0.0 开始支持本方法，仅 webgl 支持
监听触摸结束事件。
### **语法 **

```csharp
public static void OnTouchEnd(TTInput.TouchEventCallback callback)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| callback | TTInput.TouchEventCallback | -- | 是 | 监听事件处理 |

### 代码示例

```csharp
public void TestInput()
{
    TT.OnTouchEnd(evt =>
    {
        Debug.Log($"OnTouchEnd {evt}");
    });
}
```

## TT.OnTouchCancel
> 6.0.0 开始支持本方法，仅 webgl 支持
监听触点失效事件。
### **语法 **

```csharp
public static void OnTouchCancel(TTInput.TouchEventCallback callback)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| callback | TTInput.TouchEventCallback | -- | 是 | 监听事件处理 |

### 代码示例

```csharp
public void TestInput()
{
    TT.OnTouchCancel(evt =>
    {
        Debug.Log($"OnTouchCancel {evt}");
    });
}
```

## TT.OffTouchStart
> 6.0.0 开始支持本方法，仅 webgl 支持
取消监听开始触摸事件。
### **语法 **

```csharp
public static void OffTouchStart(TTInput.TouchEventCallback callback = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| callback | TTInput.TouchEventCallback | null | 否 | 监听事件处理 |

### 代码示例

```csharp
public void TestInput()
{
    TT.OffTouchStart();
}
```

## TT.OffTouchMove
> 6.0.0 开始支持本方法，仅 webgl 支持
取消监听触点移动事件。
### **语法 **

```csharp
public static void OffTouchMove(TTInput.TouchEventCallback callback = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| callback | TTInput.TouchEventCallback | null | 否 | 监听事件处理 |

### 代码示例

```csharp
public void TestInput()
{
    TT.OffTouchMove((evt) =>
    {
        Debug.Log($"OnTouchMove {evt}");
    };);
}
```

## TT.OffTouchEnd
> 6.0.0 开始支持本方法，仅 webgl 支持
取消监听触摸结束事件。
### **语法 **

```csharp
public static void OffTouchMove(TTInput.TouchEventCallback callback = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| callback | TTInput.TouchEventCallback | null | 否 | 监听事件处理 |

### 代码示例

```csharp
public void TestInput()
{
    TT.OffTouchMove((evt) =>
    {
        Debug.Log($"OffTouchMove {evt}");
    };);
}
```

## TT.OffTouchCancel
> 6.0.0 开始支持本方法，仅 webgl 支持
取消监听触点失效事件。
### **语法 **

```csharp
public static void OffTouchCancel(TTInput.TouchEventCallback callback = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| callback | TTInput.TouchEventCallback | null | 否 | 监听事件处理 |

### 代码示例

```csharp
public void TestInput()
{
    TT.OffTouchCancel((evt) =>
    {
        Debug.Log($"OffTouchCancel {evt}");
    };);
}
```
