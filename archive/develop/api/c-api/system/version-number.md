---
title: "版本号"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/system/version-number
update_time: 2024-10-12
---

该模块包含了开发中可能会用到的四种版本号。

> 注意：
> 该模块部分内容与 [旧版Unity SDK文档中的【周边】](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#52a79ab1)有重叠。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 通过TT.GameVersion 来获取游戏版本号，不要使用 Application.version |
| 相关教程 | 无 |

## TT.TTSDKVersion
> 6.0.0 开始支持本方法
TTSDK 对外发布版本号。
### **语法 **

```csharp
public static string TTSDKVersion;
```

### 代码示例

```csharp
void LogTTSDKVersion()
{
    Debug.Log("TTSDK 对外发布版本号: " + TT.TTSDKVersion);
}
```

## TT.GameVersion
> 6.0.0 开始支持本方法
游戏版本号，通过该接口替换 Application.version 获得正确的版本号信息。
### **语法 **

```csharp
public static string GameVersion;
```

### 代码示例

```csharp
void LogGameVersion()
{
    Debug.Log("游戏版本号: " + TT.GameVersion);
}
```

## TT.GamePublishVersion
> 6.0.0 开始支持本方法
发布版本时发布工具中指定的版本号。
### **语法 **

```csharp
public static string GamePublishVersion;
```

### 代码示例

```csharp
void LogGamePublishVersion()
{
    Debug.Log("游戏发布版本号: " + TT.GamePublishVersion);
}
```

## TT.GetTTContainerVersion
> 6.0.0 开始支持本方法
获取端上容器 container sdk 版本号。
### **语法 **

```csharp
public static string GetTTContainerVersion();
```

### 代码示例

```csharp
void LogGetTTContainerVersion()
{
    Debug.Log("端上版本号: " + TT.GetTTContainerVersion());
}
```
