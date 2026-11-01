---
title: "GetTTRecorderManager"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/media/audio-recording/get-ttrecorder-manager
update_time: 2026-08-25
---

## TT.GetTTRecorderManager
> TTSDK 6.5.3 开始支持本方法。
获取全局唯一的 TTRecorderManager。通过 TTRecorderManager 进行录音操作和管理。该 API 多次调用时返回同一个实例，多处使用时会操作同一个录音上下文对象。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 返回值为全局唯一实例，不需要重复创建；事件监听会保留在该实例上，不再需要时请调用对应 Off 方法或 ClearCallbacks 清理。 |
| 相关教程 | 无 |

### 语法

```csharp
public static TTRecorderManager GetTTRecorderManager()
```

### 参数说明
无
### 返回值

| 类型 | 说明 | 最低支持版本 |
| --- | --- | --- |
| TTRecorderManager | 录音管理器实例。 | TTSDK 6.5.3 |

### 代码示例

```csharp
private void Test()
{
    TTRecorderManager recorderManager = TT.GetTTRecorderManager();
}
```
