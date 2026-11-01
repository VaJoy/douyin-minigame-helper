---
title: "调试工具"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/debug-tool/debug-tool
update_time: 2024-10-12
---

该模块包含了开发中可能会用到的调试工具，包括是否显示调试 Toast 提示和接入 SDK 的 DebugPanel 面板。

> 注意：
> 该模块部分内容与 [旧版Unity SDK文档中的【周边】](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#52a79ab1)有重叠。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | TT.EnableTTSDKDebugToast 建议只在调试状态下开启 |
| 相关教程 | 无 |

## TT.EnableTTSDKDebugToast
> 6.0.0 开始支持本方法
是否显示调试 Toast 提示。当调用 TTSDK 相关接口后，获得函数执行状态（主要是失败状态）的反馈。
### **语法 **

```csharp
public static bool EnableTTSDKDebugToast;
```

### 属性说明
设置为 true 则在调用 TTSDK 相关接口后，会自动弹出 Toast 提示。默认不显示。
### 代码示例

```csharp
void Start()
{
    TT.EnableTTSDKDebugToast = false;
}
```

## TT.RegisterCommandEvent
> 6.0.0 开始支持本方法
接入 SDK 的 DebugPanel 面板，注册一些 debug 命令的回调函数。
### **语法 **

```csharp
public static void RegisterCommandEvent(Action<string, IList<string>> onCommand);
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| onCommand | Action<string, IList<string>> | -- | 是 | debug 命令的回调函数 |

### 代码示例

```csharp
void Start()
{
    TT.InitSDK((code, env) =>
    {
        Debug.Log($"Init callback ... Code = {code}");
        TT.RegisterCommandEvent(OnCommand);
    });
}
void OnCommand(string cmd, IList<string> paramLst)
{
    Debug.Log("Custom command: " + cmd + ", params: " + paramLst.Count);
}
```
