---
title: "邀请模块"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/invite-module/invite
update_time: 2024-10-12
---

## TT.CreateInvitePanel
> 6.0.0 开始支持本方法
抖音好友邀请。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void CreateInvitePanel(string roomId, 
    JsonData query = null, 
    JsonData extra = null,
    Action<bool, string> callback = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| roomId | string | -- | 是 | 房间 id |
| query | JsonData | null | 否 | 用于放在 schema 里面的信息，Key-Value 形式 |
| extra | JsonData | null | 否 | 额外扩展信息, Key-Value 形式 |
| callback | Action<bool, string> | null | 否 | 调用结果回调： (isSuccess, errMsg) => {} |

### 代码示例

```csharp
public void TestInvite()
{
    var roomId = "12345";
    JsonData query = new JsonData();
    query["test"] = "ok";
    JsonData extra = new JsonData();
    extra["test2"] = "no";
    
    TT.CreateInvitePanel(roomId, query, extra, (isSuccess, errorMsg) =>
    {
        if (isSuccess)
        {
            Debug.Log("CreateInvitePanel success");
        }
        else
        {
            Debug.Log($"CreateInvitePanel failed, {errorMsg}");
        }
    });
}
```

## TT.OnInviteStateChanged
> 6.0.0 开始支持本方法
监听邀请状态变化事件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static TTInvite.OnInviteStateChanged OnInviteStateChanged
```

### **参数说明 **
无。
### 代码示例

```csharp
public void TestInvite()
{
    TT.OnInviteStateChanged = (state, msg) =>
    {
        Debug.Log($"onInviteStateChanged - state: {state}, msg: {msg}");
    };
}
```
