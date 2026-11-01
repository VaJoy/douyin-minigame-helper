---
title: "公会群能力"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/union-group-ability
update_time: 2025-07-08
---

| 前提条件 | 需要提前调用 [TT.login](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/account) 保证用户已登录宿主 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 目前仅支持抖音，抖音极速版，可以使用 [TT.GetSystemInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/system/get-system-info) 判断宿主 |
| 注意事项 | IDE 上该接口返回模拟结果，请使用真机预览调试 基础库版本 <3.69.0，success 回调仅代表拉起加群成功，是否加群由玩家决定，游戏无法感知 基础库版本 >=3.69.0，可以通过新增的错误码来判断用户取消加群，群满员/封禁导致的加群失败 |
| 相关教程 | [公会群能力指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/union-group-guide) |

## TT.GetUnionGroupInfo
> TTSDK 6.1.1 开始支持本方法
查询指定公会是否绑定公开群。
### 语法

```csharp
TT.GetUnionGroupInfo(GetUnionGroupInfoParam param)
```

### 参数说明
GetUnionGroupInfoParam 包含属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| UnionId | string |  | 是 | 查询绑定群信息的公会 ID，格式限制为字母数字下划线，长度不超过 30 |
| Success | GetUnionGroupInfoSuccessCallback |  | 否 | 接口调用成功的回调函数 |
| Fail | Action<ErrorInfo> |  | 否 | 接口调用失败的回调函数 |
| Complete | Action |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

### 回调成功
Success 包含 GetUnionGroupInfoSuccessResult ，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| ErrMsg | string | "getUnionGroupInfo:ok" |
| BindStatus | boolean | 目前公会的绑定状态，true 则公会已绑定，false 则公会未绑定 |

### 回调失败
ErrorInfo 属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errNo | int | 错误码 |
| errMsg | string | 错误信息 |

[错误码信息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/union-group/tt-union-group-info)
### 代码示例

```csharp
var unionGroupParam = new GetUnionGroupInfoParam
{
    UnionId = "testUnionId",
    Success = successResult =>
    {
        PrintText($"GetUnionGroupInfo成功,BindStatus-->{successResult.BindStatus}," +
                  $"errMsg-->{successResult.ErrMsg}");
    },
    Fail = failResult =>
    {
        PrintText($"GetUnionGroupInfo失败，ErrorCode-->{failResult.ErrorCode}," +
                  $"ErrorMsg-->{failResult.ErrMsg},ErrorType-->{failResult.ErrorType}");
    },
    Complete = () =>
    {
        PrintText($"GetUnionGroupInfo 完成");
    }
};
PrintText($"call GetUnionGroupInfo -->{unionId}");
TT.GetUnionGroupInfo(unionGroupParam);
```

## TT.BindUnionGroup
> TTSDK 6.1.1 开始支持本方法。
给指定公会绑定公开群。
### 语法

```js
TT.BindUnionGroup(BindUnionGroupParam param)
```

### 参数说明
BindUnionGroupParam 包含属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| UnionId | string |  | 是 | 查询绑定群信息的公会 ID，格式限制为字母数字下划线，长度不超过 30 |
| Success | BindUnionGroupSuccessCallback |  | 否 | 接口调用成功的回调函数 |
| Fail | Action<ErrorInfo> |  | 否 | 接口调用失败的回调函数 |
| Complete | Action |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

### 回调成功
Success 包含 BindUnionGroupSuccessResult ，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| BindResult | bool | 是否绑定公开群，true 完成绑定，false 未绑定 |
| ErrMsg | string | "unbindUnionGroup:ok" |

### 回调失败
ErrorInfo 属性如下：
属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errNo | int | 错误码 |
| errMsg | string | 错误信息 |

[错误码信息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/union-group/tt-bind-group)
### 代码示例

```js
var unionGroupParam = new BindUnionGroupParam
{
    UnionId = "testUnionId",
    Success = successResult =>
    {
        PrintText($"BindUnionGroup,BindStatus-->{successResult.BindResult}," +
                  $"errMsg-->{successResult.ErrMsg}");
    },
    Fail = failResult =>
    {
        PrintText($"BindUnionGroup，ErrorCode-->{failResult.ErrorCode}," +
                  $"ErrorMsg-->{failResult.ErrMsg},ErrorType-->{failResult.ErrorType}");
    },
    Complete = () =>
    {
        PrintText($"BindUnionGroup 完成");
    }
};
PrintText($"call BindUnionGroup -->{unionId}");
TT.BindUnionGroup(unionGroupParam);
```

## TT.UnbindUnionGroup
> TTSDK 6.1.1 开始支持本方法。
解除指定公会和公开群的绑定关系。
### 语法

```js
TT.UnbindUnionGroup(UnbindUnionGroupParam param)
```

### 参数说明
UnbindUnionGroupParam 包含属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| UnionId | string |  | 是 | 查询绑定群信息的公会 ID，格式限制为字母数字下划线，长度不超过 30 |
| Success | UnbindUnionGroupSuccessCallback |  | 否 | 接口调用成功的回调函数 |
| Fail | Action<ErrorInfo> |  | 否 | 接口调用失败的回调函数 |
| Complete | Action |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

### 回调成功
Success 包含 UnbindUnionGroupSuccessResult ，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| ErrMsg | string | "unbindUnionGroup:ok" |

### 回调失败
ErrorInfo 属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errNo | int | 错误码 |
| errMsg | string | 错误信息 |

[错误码信息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/union-group/tt-unbind-group)
### 代码示例

```js
var unionGroupParam = new UnbindUnionGroupParam
{
    UnionId = "testUnionId",
    Success = successResult =>
    {
        PrintText($"UnbindUnionGroup, errMsg-->{successResult.ErrMsg}");
    },
    Fail = failResult =>
    {
        PrintText($"UnbindUnionGroup，ErrorCode-->{failResult.ErrorCode}," +
                  $"ErrorMsg-->{failResult.ErrMsg},ErrorType-->{failResult.ErrorType}");
    },
    Complete = () =>
    {
        PrintText($"UnbindUnionGroup 完成");
    }
};
PrintText($"call UnbindUnionGroup -->{unionId}");
TT.UnbindUnionGroup(unionGroupParam);
```

## TT.JoinUnionGroup
> TTSDK 6.1.1 开始支持本方法。
加入指定公会绑定的公开群。
### 语法

```js
TT.JoinUnionGroup(JoinUnionGroupParam param)
```

### 参数说明
JoinUnionGroupParam 包含属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| UnionId | string |  | 是 | 查询绑定群信息的公会 ID，格式限制为字母数字下划线，长度不超过 30 |
| Success | JoinUnionGroupSuccessResult |  | 否 | 接口调用成功的回调函数（ 目前 success 回调代表拉起加群成功，是否加群由玩家决定，游戏无法感知） |
| Fail | Action<ErrorInfo> |  | 否 | 接口调用失败的回调函数 |
| Complete | Action |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

### 回调成功
Success 包含 JoinUnionGroupSuccessResult ，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| ErrMsg | string | "joinUnionGroup:ok" |

### 回调失败
ErrorInfo 属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errNo | int | 错误码 |
| errMsg | string | 错误信息 |

[错误码信息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/union-group/tt-join-group)
### 代码示例

```js
var unionGroupParam = new JoinUnionGroupParam
{
    UnionId = "testUnionId",
    Success = successResult =>
    {
        PrintText($"JoinUnionGroup,errMsg-->{successResult.ErrMsg}");
    },
    Fail = failResult =>
    {
        PrintText($"JoinUnionGroup，ErrorCode-->{failResult.ErrorCode}," +
                  $"ErrorMsg-->{failResult.ErrMsg},ErrorType-->{failResult.ErrorType}");
    },
    Complete = () =>
    {
        PrintText($"JoinUnionGroup 完成");
    }
};
PrintText($"call JoinUnionGroup -->{unionId}");
TT.JoinUnionGroup(unionGroupParam);
```
