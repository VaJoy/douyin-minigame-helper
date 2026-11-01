---
title: "群标签能力"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/group-tag
update_time: 2025-08-07
---

## TT.SetGroupTag
> 6.4.3 开始支持本方法
设置用户群标签。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void SetGroupTag(TTSetGroupTagParam param)
```

### 参数说明
入参为 TTSetGroupTagParam 类型，属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| openId | string |  | 是 | 用户的 openid |
| tagId | string |  | 是 | 标签的 tagId |
| status | int |  | 是 | 标签状态 |
| success | Action<TTSetGroupTagSuccessCallbackResult> | null | 否 | 成功回调 |
| fail | Action<ErrorInfo> | null | 否 | 失败回调 |
| complete | Action | null | 否 | 完成回调 |

### 回调成功
回调传参为 TTSetGroupTagSuccessCallbackResult 类型，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 固定为"setGroupTag:ok" |
| isSanboxRequest | string | 是否为沙盒环境调用，当标签状态为「待上架」时，返回 true，表示本次调用不会对真实用户设置生效 |

### 回调失败
回调传参为 ErrorInfo 类型，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| ErrorCode | int | 错误码 |
| ErrMsg | string | 错误信息 |

#### 错误码
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/im-group/tt-set-group-tag#%E9%94%99%E8%AF%AF%E7%A0%81)

### 代码示例

```csharp
private void Test() {
    TT.SetGroupTag(new()
    {
        openId = "xxxx",
        status = 1,
        tagId = "xxx",
        success = (res) =>
        {
            Debug.Log($"SetGroupTag success, isSanboxRequest: {res.isSanboxRequest}, errMsg: {res.errMsg}");
        },
        fail = (errInfo) =>
        {
            Debug.Log($"SetGroupTag fail, errorInfo: {errInfo}");
        },
        complete = () =>
        {
            Debug.Log($"SetGroupTag complete");
        }
    });
}
```

## TT.GetUserGroupTagInfo
> 6.4.3 开始支持本方法
获取用户群标签信息。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 已删除的标签不会出现在返回的userGroupTags列表中 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void GetUserGroupTagInfo(TTGetUserGroupTagInfoParam param)
```

### 参数说明
入参为 TTGetUserGroupTagInfoParam 类型，属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| openId | string |  | 是 | 用户的 openid |
| tagId | string |  | 是 | 标签的tagId |
| status | int? | null | 否 | 标签状态 |
| success | Action<TTGetUserGroupTagSuccessCallbackResult> | null | 否 | 成功回调 |
| fail | Action<ErrorInfo> | null | 否 | 失败回调 |
| complete | Action | null | 否 | 完成回调 |

### 代码示例

```csharp
private void Test() {
    TT.GetUserGroupTagInfo(new()
    {
        openId = "xxx",
        success = (res) =>
        {
            Debug.Log($"GetUserGroupTagInfo success, userGroupTagsLength: {res.userGroupTags.Length}, errMsg: {res.errMsg}");
        },
        fail = (errInfo) =>
        {
            Debug.Log($"GetUserGroupTagInfo fail, errorInfo: {errInfo}");
        },
        complete = () =>
        {
            Debug.Log($"GetUserGroupTagInfo complete");
        }
    });
}
```

### 回调成功
回调传参为 TTGetUserGroupTagSuccessCallbackResult 类型，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 固定为"getUserGroupTagInfo:ok" |
| userGroupTags | TTUserTag[] | openId 对应用户的所有群聊标签信息 |

TTUserTag属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| status | int | 佩戴状态 |
| tagId | string | 标签id |

#### status 的合法值
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/im-group/tt-getusergrouptaginfo#%E5%9B%9E%E8%B0%83%E6%88%90%E5%8A%9F)
### 回调失败
回调传参为 ErrorInfo 类型，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| ErrorCode | int | 错误码 |
| ErrMsg | string | 错误信息 |

#### 错误码
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/im-group/tt-getusergrouptaginfo#%E9%94%99%E8%AF%AF%E7%A0%81)
