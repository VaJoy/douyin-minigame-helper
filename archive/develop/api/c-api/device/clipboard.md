---
title: "剪切板"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/device/clipboard
update_time: 2024-10-12
---

> 注意：
> 该模块对应 [旧版Unity SDK文档中的 【操作剪切板】 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#496da772)

## TT.SetClipboardData
> 6.0.0 开始支持本方法，WebGL也支持该方法
设置剪切板信息。
### **语法 **

```csharp
public static void SetClipboardData(string data, Action<bool, string> action = null)
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| data | string | -- | 是 | 设置的内容 |
| action | Action<bool, string> | null | 否 | bool = true设置成功，反则关注错误信息 |

### 代码示例

```csharp
private void Test() {
    TT.SetClipboardData(text, (b, s) =>
    {
        if (b)
        {
            Debug.Log("设置成功");
        }
        else
        {
            Debug.Log("设置失败，"+s );
        }
    });
}
```

## TT.GetClipboardData
> 6.0.0 开始支持本方法，WebGL也支持该方法
获取剪切板信息。
### **语法 **

```csharp
 public static void GetClipboardData(Action<bool, string> action)
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| action | Action<bool, string> | -- | 是 | bool = true获取成功，反则关注错误信息 |

### 代码示例

```csharp
private void Test() {
    TT.GetClipboardData((b, s) =>
    {
        if (b)
        {
            Debug.Log("获取成功:"+s);
        }
        else
        {
            Debug.Log("获取失败, "+s);
        }
    });
}
```
