---
title: "光标样式"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/drawing/cursor-style
update_time: 2025-01-02
---

| 前提条件 | [PC 端小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/tutorial) |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 仅支持 PC 端小游戏环境。 仅支持 WebGL 方案。 |
| 注意事项 | 也支持直接使用 `Cursor.lockState` 等 Unity API 锁定/解锁光标。 光标锁定相关的 Unity API 与 TT API 不可混用。 |
| 相关教程 | 无 |

## Cursor.SetCursor
> Unity 引擎自带的 API
设定鼠标指针的样式，仅适用于 PC 平台。
Unity 小游戏不支持通过 TT.SetCursor() 接口设置光标样式，需使用 Unity 引擎提供的 [`Cursor.SetCursor()`](https://docs.unity3d.com/2021.3/Documentation/ScriptReference/Cursor.html) 替代。
### 语法

```csharp
public static void SetCursor(Texture2D texture, Vector2 hotspot, CursorMode cursorMode);
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| texture | Texture2D | -- | 是 | 光标使用的纹理贴图，需要在资产 Import Settings 中将 Texture Type 设为 Cursor。传入 `null` 则还原为默认。 |
| hotsopt | Vector2 | -- | 是 | 光标相对于纹理左上角的偏移量。 |
| cursorMode | CursorMode | -- | 是 | 小游戏环境中只支持 [`CursorMode.ForceSoftware`](https://docs.unity3d.com/2021.3/Documentation/ScriptReference/CursorMode.ForceSoftware.html) |

### 代码示例

```csharp
private void Test()
{
    var texture = Resources.Load("ico_texture") as Texture2D;
    Cursor.SetCursor(texture, Vector2.zero, CursorMode.ForceSoftware);
}
```

## TT.RequestPointerLock
> 6.2.1 开始支持该方法
锁定鼠标指针，锁定后隐藏鼠标，仅适用于 PC 平台。
### 语法

```csharp
public static void RequestPointerLock()
```

### 参数说明
无。
### 代码示例

```csharp
private void Test()
{
    // Unity API: Cursor.lockState = CursorLockMode.Locked;
    TT.RequestPointerLock();
}
```

## TT.IsPointerLocked
> 6.2.1 开始支持该方法
检查鼠标指针是否被锁定，仅适用于 PC 平台。
### 语法

```csharp
public static bool IsPointerLocked()
```

### 参数说明
无。
### 返回值

| **类型** | **说明** |
| --- | --- |
| bool | 是否被锁定。 |

### 代码示例

```csharp
private void Test()
{
    // Unity API: var lock = Cursor.lockState == CursorLockMode.Locked;
    var lock = TT.IsPointerLocked();
    Debug.Log("lock: " + lock);
}
```

## TT.ExitPointerLock
> 6.2.1 开始支持该方法
解除锁定鼠标指针，仅适用于 PC 平台。
### 语法

```csharp
public static void ExitPointerLock()
```

### 参数说明
无。
### 代码示例

```csharp
private void Test()
{
    // Unity API: Cursor.lockState = CursorLockMode.None;
    TT.ExitPointerLock();
}
```
