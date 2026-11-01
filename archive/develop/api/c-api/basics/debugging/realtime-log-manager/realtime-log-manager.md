---
title: "RealtimeLogManager"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/basics/debugging/realtime-log-manager/realtime-log-manager
update_time: 2025-01-02
---

## TT.GetRealtimeLogManager
> TTSDK 6.1.4版本支持本方法。
获取实时日志管理器实例，本文档为API使用介绍，功能简介以及使用限制可以查看：[功能介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/performance-tuning-tool/real-time-log)
### 语法

```csharp
public static TTRealtimeLogManager GetRealtimeLogManager(GetRealtimeManagerParam param)
```

### 参数说明
GetRealtimeManagerParam 类型主要包含以下参数信息：

| **属性名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| SyncToConsole | bool | 否 | true表示 log 内容会在 vConsole 或 IDE 控制台上展示， false 表示不展示。默认值是 false |

### 代码示例

```csharp
TTRealtimeLogManager_realtimeLogManager = TT.GetRealtimeLogManager(new GetRealtimeManagerParam
{
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
获取到 TTRealtimeLogManager 实例后：

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
获取到 TTRealtimeLogManager 实例后：

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
获取到 TTRealtimeLogManager 实例后：

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
获取到 TTRealtimeLogManager 实例后：

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
获取到 TTRealtimeLogManager 实例后：

```csharp
_logManager.Error("test");
```

## AddFilterMsg
> TTSDK 6.1.4版本支持本方法。
添加过滤关键字，用于设置多个过滤关键字。**最多加5个过滤关键字， 每个长度限制64个字符**
### 语法

```csharp
void AddFilterMsg(string msg);
```

### 代码实例
获取到 TTRealtimeLogManager 实例后：

```csharp
_realtimeLogManager.AddFilterMsg("tag");
```

## SetFilterMsg
> TTSDK 6.1.4版本支持本方法。
设置过滤关键字。每次调用会把前面通过RealtimeLogManager.addFilterMsg 和RealtimeLogManager.setFilterMsg设置的关键字覆盖
### 语法

```csharp
void SetFilterMsg(string msg);
```

### 代码实例
获取到 TTRealtimeLogManager 实例后：

```csharp
_realtimeLogManager.SetFilterMsg("tag");
```
