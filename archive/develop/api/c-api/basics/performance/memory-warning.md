---
title: "内存不足警告回调"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/basics/performance/memory-warning
update_time: 2025-09-05
---

## TT.OnMemoryWarning
> 6.5.4开始支持本方法
注册监听内存不足警告函数。当手机内存占用过高时，触发注册函数。
### 语法

```csharp
public static void OnMemoryWarning(Action<OnMemoryWarningListenerResult> result)
```

### 参数说明
OnMemoryWarningListenerResult包含以下参数

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| level | double | 仅 Android 有该字段，对应系统内存告警等级宏定义 |

level参数说明

| level | 宏定义 |
| --- | --- |
| 5 | TRIM_MEMORY_RUNNING_MODERATE |
| 10 | TRIM_MEMORY_RUNNING_LOW |
| 15 | TRIM_MEMORY_RUNNING_CRITICAL |

### 代码示例

```csharp
private void Test() {
    TT.OnMemoryWarning(OnMemoryWarning)},
}
private void OnMemoryWarning(OnMemoryWarningListenerResult result)
{
    Debug.Log($"OnMemoryWarning: {result.ToJson()}");
}
```
