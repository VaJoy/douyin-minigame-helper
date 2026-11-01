---
title: "兼容性判断接口"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/basics/tt-can-i-use
update_time: 2024-10-12
---

## CanIUse
> 6.0.0 开始支持本方法，WebGL也支持该方法
判断小游戏的 API、回调、参数、组件等是否在当前版本可用。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 目前container方案在各个宿主上的版本有一定差异，开发者需要关注兼容性工作，在低版本上使用不兼容的api，会出现逻辑错误问题。 WebGL方案和native方案的接口支持情况有一定差异 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static bool CanIUse.TT方法名
public static bool CanIUse.TT类名.方法名
```

### 返回值

| **类型** | **说明** |
| --- | --- |
| bool | 在当前版本是否可用 |

### 代码示例

```csharp
void Test() {
    Debug.Log($"GetUserInfoAuth: {CanIUse.GetUserInfoAuth}");
    Debug.Log($"GetSystemInfo: {CanIUse.GetSystemInfo}");
}
```
