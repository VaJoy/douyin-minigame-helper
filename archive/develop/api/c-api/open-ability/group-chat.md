---
title: "群聊"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/group-chat
update_time: 2024-10-12
---

## TT.JoinGroup

> 注意：
> 该模块对应 [旧版Unity SDK文档中的 【加入群聊】 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#e0df5067)

> 6.0.0 开始支持本方法，WebGL也支持该方法
在平台创建群聊，获得 groupid 后，游戏内通过这个方法引导用户加入抖音群。

| 前提条件 | 使用本 API 前需要先在开发者平台创建群聊获取 groupid。具体可参考[游戏群聊能力接入介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/im-group/groupchatintroduce) 前往开发者平台，「运营 - 运营能力 - 粉丝群能力 」，申请开通能力 扫码绑定抖音号后，点击「新建群聊」以获得对应的群 ID |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 目前仅支持抖音及抖音极速版 |
| 注意事项 | 无 |
| 相关教程 | [游戏群聊能力接入介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/im-group/groupchatintroduce) |

### **语法 **

```csharp
public static void JoinGroup(data, action, sessionFrom, extraInfo)
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| groupId | string | -- | 是 | 群 ID |
| action | Action<bool, string> | null | 否 | bool = true设置成功，反则关注错误信息 |
| sessionFrom | string | null | 否 | 会话来源 |
| extraInfo | string | null | 否 | 附加信息 |

### 代码示例

```csharp
private void Test() {
    TT.JoinGroup(groupId, (isSuccess, data) =>
    {
        if (isSuccess)
        {
            Debug.Log($"Call JoinGroup success, {data}");
        }
        else
        {
            Debug.Log($"Call JoinGroup fail, {data}");
        }
    });
}
```

## TT.CheckGroupInfo

> 注意：
> 该模块对应 [旧版Unity SDK文档中的 【获取群消息】 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#50a4b70a)

> 6.0.0 开始支持本方法，WebGL也支持该方法
查询用户通过小游戏平台创建的群的信息。
如游戏开发者在平台创建了群聊 ABC，那么游戏侧可以基于游戏开发者在这个游戏中的 openid，查询其在小游戏平台创建了哪些群，群的状态如何，做游戏内的加群逻辑优化。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 目前仅支持抖音，可以使用 [getSystemInfoSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/system-information/tt-get-system-info-sync) 判断宿主 |
| 注意事项 | 查询到的群列表只局限在通过游戏创建的群聊或开发者在平台创建的群聊，其他渠道创建的群聊不会返回 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void CheckGroupInfo(openId, onCheckGroupInfoSuccessCallback, onCheckGroupInfoFailCallback, sessionFrom, extraInfo)
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| openId | string |  | 是 | 建群用户的 openid |
| onCheckGroupInfoSuccessCallback | delegate void OnCheckGroupInfoSuccessCallback(ref List<GroupInfo> groupInfoList) |  | 是 | 接口调用成功的回调函数 |
| onCheckGroupInfoFailCallback | delegate void OnCheckGroupInfoFailCallback(string errMsg); |  | 是 | 接口调用失败的回调函数 bool = true设置成功，反则关注错误信息 |
| sessionFrom | string | null | 否 | 会话来源 |
| extraInfo | string | null | 否 | 附加信息 |

### 代码示例

```csharp
private void Test() {
    TT.CheckGroupInfo(openId, (ref List<TTGroup.GroupInfo> list) =>
        {
            Debug.Log($"Call CheckGroupInfo success, {list.ToJson()}");
        }, errMsg =>
        {
            Debug.Log($"Call CheckGroupInfo fail, {errMsg}");
        });
}
```
