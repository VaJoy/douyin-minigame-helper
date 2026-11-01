---
title: "LogManager"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/basics/debugging/log-manager/log-manager
update_time: 2025-01-02
---

## TT.GetLogManager
> TTSDK 6.1.4版本支持本方法。
获取日志管理器示例，本文档为API使用介绍，功能简介以及使用限制可以查看：[功能介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/performance-tuning-tool/feedback-log-capability)
### 语法

```csharp
public static TTFeedbackLogManager GetLogManager(GetLogManagerParam param)
```

### 参数说明
GetLogManagerParam 类型主要包含以下参数信息：

| **属性名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| Level | enum TTSDK.LogLevel | 否 | 是否会把一些基础库的运行时信息写入日志 |
| SyncToConsole | bool | 否 | true表示 log 内容会在 vConsole 或 IDE 控制台上展示， false 表示不展示。默认值是 false |

**LogLevel 的合法值：**

| **值** | **说明** |
| --- | --- |
| Verbose | 0，把一些基础库的运行时信息（内容见下方）写入日志 |
| User | 1，不会写入 |

### 代码示例

```csharp
TTFeedbackLogManager _logManager = TT.GetLogManager(new GetLogManagerParam
{
    Level = LogLevel.User,
    SyncToConsole = true
});
```

## Debug
> TTSDK 6.1.4版本支持本方法。
写入 Debug 级别日志
### 语法

```csharp
void Debug(string args)
```

### 代码示例
获取到 TTFeedbackLogManager 实例后：

```csharp
_logManager.Debug("test");
```

## Info
> TTSDK 6.1.4版本支持本方法。
写入 Info 级别日志
### 语法

```csharp
void Info(string args)
```

### 代码示例
获取到 TTFeedbackLogManager 实例后：

```csharp
_logManager.Info("test");
```

## Log
> TTSDK 6.1.4版本支持本方法。
写入 Log 级别日志
### 语法

```csharp
void Log(string args)
```

### 代码示例
获取到 TTFeedbackLogManager 实例后：

```csharp
_logManager.Log("test");
```

## Warn
> TTSDK 6.1.4版本支持本方法。
写入 Warning 级别日志
### 语法

```csharp
void Warn(string args)
```

### 代码示例
获取到 TTFeedbackLogManager 实例后：

```csharp
_logManager.Warn("test");
```

## Error
> TTSDK 6.1.4版本支持本方法。
写入 Error 级别日志
### 语法

```csharp
void Error(string args)
```

### 代码示例
获取到 TTFeedbackLogManager 实例后：

```csharp
_logManager.Error("test");
```
