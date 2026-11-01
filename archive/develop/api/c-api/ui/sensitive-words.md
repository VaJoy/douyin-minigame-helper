---
title: "敏感词"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/ui/sensitive-words
update_time: 2025-02-08
---

敏感词相关处理

> 注意
> 该模块对应 [敏感词](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#5ad30368)

## TT.SensitiveWordCheck
> 6.0.0 开始支持本方法
检测敏感词

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void SensitiveWordCheck(string word, 
    Action<Boolean> checkSuccess, 
    Action<string> checkFail)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 注意 |
| --- | --- | --- | --- | --- |
| word | string | -- | 是 | 要检查的词语 |
| checkSuccess | Action<Boolean> | -- | 是 | 检查成功的回调 |
| checkFail | Action<string> | -- | 是 | 检查失败的回调 |

### 代码示例

```csharp
public void TestSensitive()
{
    TT.SensitiveWordCheck("xxxxxxxx", 
    result =>
    {
        Debug.Log(" 是否是敏感词:" + result);
    },
    errMsg =>
    {
        Debug.Log("检测失败，原因:" + errMsg);
    });
}
```

## TT.ReplaceSensitiveWords
> 6.0.0 开始支持本方法
替换敏感词

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void ReplaceSensitiveWords(string word, 
    Action<int, string, JsonData> callback)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 注意 |
| --- | --- | --- | --- | --- |
| word | string | -- | 是 | 要检查和替换的词语 |
| callback | Action<int, string, JsonData> | -- | 是 | int: 返回状态码，0为成功，否则为失败 string: 错误信息 jsonData： audit_result    int     1: 有敏感内容；2: 无敏感内容 audit_content   string  被替换的内容（无敏感内容则返回值与传入的word相同） |

### 代码示例

```csharp
public void TestSensitive()
{
    TT.ReplaceSensitiveWords("xxxx", (code, msg, data) =>
    {
        Debug.Log($"返回code: {code}\n返回msg: {msg}\n返回data: {data?.ToJson()}");
    });
}
```
