---
title: "客服能力"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/customer-contact
update_time: 2025-04-22
---

客服能力模块包含三部分，打开客服聊天页，平台提供的小游戏客服能力，通过客服页面发起支付。
## TT.OpenCustomerServicePage
> 6.0.0 开始支持本方法
打开客服聊天页。

> 注意：
> 该模块对应 [旧版Unity SDK文档中的 【打开客服页】 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#d40c332e)

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void OpenCustomerServicePage(Action<bool> csCallback);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| csCallback | Action<bool> | -- | 是 | 打开客服聊天页回调 参数为是否成功，true表示成功，false表示失败 |

### 代码示例

```csharp
void OpenCustomerPage()
{
    if (CanIUse.OpenCustomerServicePage)
    {
        Debug.Log("打开客服页");
        TT.OpenCustomerServicePage(
            (flag) =>
            {
                if (flag)
                {
                    Debug.Log("成功");
                }
                else
                {
                    Debug.Log("失败");
                }
            });
    }
    else
    {
        Debug.Log("AndroidSDK版本不足以打开客服页");
    }
}
```

## TT.OpenCustomerServiceConversation
> 6.0.0 开始支持本方法
平台提供的小游戏客服能力。

> 注意：
> 该模块对应小游戏接口 [小游戏接口：tt.openCustomerServiceConversation](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/customer-contact/openCustomerServiceConversation)
> 该模块对应 [旧版Unity SDK文档中的 【打开客服页】 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#d40c332e)

| 前提条件 | **使用抖音IM客服需要先绑定抖音号，详情请查看：**[**抖音客服能力介绍**](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/user-service/douyinIM) |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 本方法仅支持抖音&抖 lite |
| 注意事项 | 用户必须在登录状态下才能调起IM客服，否则会出现返回成功，但是前端无响应的问题 若当前登录的用户与被绑定的抖音号相同，无法拉起 im 客服 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void OpenCustomerServiceConversation(JsonData param, Action<bool> callback)；
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| param | JsonData | -- | 是 | 这是一个Json格式的字符串，其中字段有： 【type】 1 ：小 6 客服 2 :  抖音IM 客服（仅支持抖音） 3：抖音客服平台（基础库 3.41.0 开始支持） 【sessionFrom】保留字段，暂时可以不填 例如 {"type":1,"sessionFrom":"xxx"} |
| callback | Action<bool> | -- | 是 | 打开客服页面成功或者失败回调 |

### 代码示例

```csharp
void TestOpenCustomerServiceConversation1()
{
    Debug.Log("打开客服页（新）小6");
    OpenCustomerServiceConversation(1);
}
void TestOpenCustomerServiceConversation2()
{
    Debug.Log("打开客服页（新）IM");
    OpenCustomerServiceConversation(2);
}
void OpenCustomerServiceConversation(int type)
{
    JsonData data = new JsonData
    {
        ["type"] = type
    };
    TT.OpenCustomerServiceConversation(data, (succ) =>{
        if (succ)
        {
            Debug.Log("成功");
        }
        else
        {
            Debug.Log("失败");
        }
    });
}
```
