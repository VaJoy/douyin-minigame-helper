---
title: "触发GC"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/basics/performance/trigger-gc
update_time: 2025-09-05
---

## TT.TriggerGC
> 6.5.4开始支持本方法
加快触发 JS 引擎 Garbage Collection（垃圾回收），GC 时机是 JS 引擎控制的，并不能保证调用后马上触发 GC。但是建议不要频繁触发，否则可能会影响性能。可以结合OnMemoryWarning一起使用。
### 语法

```csharp
public static void TriggerGC()
```

### 代码示例

```csharp
private void Test() {
    TT.OnMemoryWarning(OnMemoryWarning);
}

private void OnMemoryWarning(OnMemoryWarningListenerResult result)
{
    TT.TriggerGC();
}
```
