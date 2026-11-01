---
title: "推荐流直出游戏能力"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/direct-play
update_time: 2025-11-17
---

该模块为直玩能力相关。向用户请求授权允许游戏在满足一定的条件后出现在 Feed 流中和查询用户的授权情况。

| 前提条件 | 已申请开通小游戏直玩能力，在申请开通后可以获得 contentID |
| --- | --- |
| 业务背景 | 游戏供给更加偏向中重度，因此以游戏内的「关键节点」为高价值信息牵引用户复访成为效率更高的一种手段  因此，业务侧期望，发挥小游戏的即点即玩特性，且整体无限贴合抖音：刷、推信息本身的体验，尝试为用户提供一种新型的小游戏游玩体验 |
| 使用限制 | 仅支持抖音app。 必须在调用 [TT.Login](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/account) 后才能调用本接口。 本接口存在频控限制，需要注意调用场景和频率。 |
| 注意事项 | 无 |
| 相关教程 | https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/feed/minigame-feedpush-setting-guide |

## **TT.RequestFeedSubscribe**

### **语法 **

```csharp
public static void RequestFeedSubscribe(JsonData param, Action<JsonData> success = null,
    Action<int, string> failed = null, Action complete = null)
```

### **参数说明 **
param 为 JsonData 类型，属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| type | string | -- | 是 | 订阅 Feed 流的类型，目前只支持传 'play' | 5.52.11 |
| scene | int | -- | 否 | 订阅的场景 ID（非全场景下必传） | 5.52.11 |
| contentIDs | Array<string> | -- | 否 | Array<string>，自定义文案 contentID 数组 （非全场景下必传），contentID 在后台申请开通直玩能力后可获取 | 5.52.11 |
| allScene | boolean | false | 否 | 是否为全场景订阅 | 6.0.2 |
| success | Action<JsonData> |  | 否 | 接口调用成功的回调函数 | 5.52.11 |
| failed | Action<int, string> |  | 否 | 接口调用失败的回调函数 | 5.52.11 |
| complete | Action |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） | 5.52.11 |

type 的合法值 ：

| 值 | 说明 |
| --- | --- |
| 'play' | 直玩场景 |

scene 的合法值：

| 值 | 说明 |
| --- | --- |
| 1 | 离线收益场景 |
| 2 | 体力恢复场景 |
| 3 | 重要事件掉落 |

### **回调成功 **
JsonData 类型，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 回调信息 |
| success | bool | 用户的订阅结果（true为成功，false为订阅失败，具体原因看errMsg） |

### **回调失败 **
属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errNo | int | 错误码 |
| errMsg | string | 错误信息 |

### 错误码

| errNo | errMsg | 说明 |
| --- | --- | --- |
| 10301 | feature is not supported in app | 宿主不支持该功能 |
| 21100 | host does not have permission | 该app未开通该能力 |
| 21101 | no permission | 该游戏没有订阅权限 |
| 10601 | not login | 需要调用tt.login登录 |
| 20001 | type is invalid params contentIDs or scene is required （type='play'时才有） | 开发者传参错误 |
| 21102 | network error | 网络环境问题，一般指无网环境 |
| 21103 | service error:具体错误信息 | 网络请求失败 |
| 21104 | internal error:具体错误信息 | 弹窗跳转失败等 |
| 21105 | frequency control | 频控限制 |

### **代码示例 **
发起单场景订阅：

```csharp
public void FeedTest(){
    var contentIDs = JsonData.NewJsonArray();
    contentIDs.Add("CONTENT123");
    contentIDs.Add("CONTENT234");
    
    var param = new JsonData
    {   
        ["type"]: "play", // play=直玩
        ["scene"]: 1, // 一次只能订阅一个
        ["contentIDs"]: contentIDs,
    };
    
    TT.RequestFeedSubscribe(
        param,
        (res) => {
        },
        (errNo, errMsg) => {
        },
        () => {
        }
    );
}
```

发起全场景订阅：

```csharp
public void FeedTest(){
    var param = new JsonData
    {   
        ["type"]: "play", // play=直玩
        ["allScene"]: true, // 全场景订阅
    };
    
    TT.RequestFeedSubscribe(
        param,
        (res) => {
        },
        (errNo, errMsg) => {
        },
        () => {
        }
    );
}
```

## **TT.CheckFeedSubscribeStatus**
### **语法 **

```csharp
public static void CheckFeedSubscribeStatus(JsonData param, Action<JsonData> success = null,
    Action<int, string> failed = null, Action complete = null)
```

### **参数说明 **
param 为 JsonData 类型，属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| type | string | -- | 是 | 订阅 Feed 流的类型，目前只支持传 'play' | 5.52.11 |
| scene | int | -- | 否 | 订阅的模板ID（type="play"时必传） | 5.52.11 |
| allScene | boolean | false | 否 | 是否为全场景订阅 | 6.0.2 |
| success | Action<JsonData> |  | 否 | 接口调用成功的回调函数 | 5.52.11 |
| failed | Action<int, string> |  | 否 | 接口调用失败的回调函数 | 5.52.11 |
| complete | Action |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） | 5.52.11 |

type 的合法值 ：

| 值 | 说明 |
| --- | --- |
| "play" | 直玩场景 |

scene 的合法值：

| 值 | 说明 |
| --- | --- |
| 1 | 离线收益场景 |
| 2 | 体力恢复场景 |
| 3 | 重要事件掉落 |

### **回调成功 **
JsonData 类型，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 回调信息 |
| status | bool | 用户的订阅状态（true为已经订阅，false为用户未订阅） |

### **回调失败 **
属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errNo | int | 错误码 |
| errMsg | string | 错误信息 |

### 错误码

| errNo | errMsg | 说明 |
| --- | --- | --- |
| 10301 | feature is not supported in app | 宿主不支持该功能 |
| 21100 | host does not have permission | 该app未开通该能力 |
| 21101 | no permission | 该游戏没有订阅权限 |
| 10601 | not login | 需要调用tt.login登录 |
| 20001 | invalid params, type is invalid params scene is required （type='play'时才有） *（type='play'时才有）* | 开发者传参错误，客户端主要校验 msgID 为空的情况 |
| 21102 | network error | 网络环境问题，一般指无网环境 |
| 21103 | service error:具体错误信息 | 网络请求失败 |

### **代码示例 **
查询单场景订阅状态：

```csharp
public void FeedTest(){
    var param = new JsonData
    {
        ["type"]: "play",
        ["scene"]: 1,
    };
    
    TT.CheckFeedSubscribeStatus(
        param,
        (res) => {
        },
        (errNo, errMsg) => {
        },
        () => {
        }
    );
}
```

## 查询全场景订阅状态：

```csharp
public void FeedTest(){
    var param = new JsonData
    {
        ["type"]: "play",
        ["allScene"]: true,
    };
    
    TT.CheckFeedSubscribeStatus(
        param,
        (res) => {
        },
        (errNo, errMsg) => {
        },
        () => {
        }
    );
}
```

## TT.OnFeedStatusChange
> TTSDK 6.2.4 及以后版本支持
添加直玩场景内外流的切换的监听。
### 语法

```csharp
public static void OnFeedStatusChange(OnFeedStatusChangeCallback callback)
```

### 参数说明
**callback：**
callback 是一个 delegate，接收的参数如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| Type | enum FeedStatusEnum | 当前进入或退出游戏的事件类型 |

Type 为枚举类型，其枚举值及解释如下：

| **枚举值** | **说明** |
| --- | --- |
| FeedEnter | 从Feed流中进入游戏 |
| FeedExit | 从游戏退回到Feed流 |

### 使用示例

```csharp
private void OnFeedStatusChangeCallback(OnFeedStatusChangeResult result)
{
    Debug.Log($"OnFeedStatusChangeCallback, Type -->{result.Type.ToString()}");
}

private void OnFeedStatusChange()
{
    TT.OnFeedStatusChange(OnFeedStatusChangeCallback);
}
```

## TT.OffFeedStatusChange
> TTSDK 6.2.4 及以后版本支持
删除直玩场景内外流的切换的监听。
### 语法

```csharp
public static void OffFeedStatusChange(OnFeedStatusChangeCallback callback = null)
```

### 参数说明
**callback：**
callback 是一个 delegate，接收的参数如下(不传则会删除所有 callback)：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| Type | enum FeedStatusEnum | 当前进入或退出游戏的事件类型 |

### 使用示例

```csharp
// 删除所有监听
TT.OffFeedStatusChange();
```

## TT.StoreFeedData
> TTSDK 6.3.3 及以后版本支持
存储游戏是否直玩就绪状态
### 语法

```java
public static void StoreFeedData(StoreFeedDataParam param)
```

### 参数说明
param 为 StoreFeedDataParam 类型，属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| scene | int |  | 是 | 订阅的场景 ID | 6.3.3 |
| contentID | string |  | 是 | 自定义文案的 contentID，contentID 在后台申请开通直玩能力后可获取 | 6.3.3 |
| leftValue | string |  | 是 | 运算公式的左值，当前只支持"timeStampMs"，即毫秒级时间戳 | 6.3.3 |
| operator | string |  | 是 | 运算符 | 6.3.3 |
| rightValue | string |  | 是 | 运算公式的右值 | 6.3.3 |
| status | int |  | 是 | 满足运算公式后，对应直玩场景是否就绪。0：未就绪， 1：就绪 | 6.3.3 |
| extra | string |  | 否 | 自定义补充字段 | 6.3.3 |
| success | function |  | 否 | 接口调用成功的回调函数 | 6.3.3 |
| fail | function |  | 否 | 接口调用失败的回调函数 | 6.3.3 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） | 6.3.3 |

#### scene 参数说明

| 值 | 说明 |
| --- | --- |
| 1 | 离线收益场景 |
| 2 | 体力恢复场景 |
| 3 | 重要事件掉落 |

### **回调成功 **
属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 回调信息 |

### **回调失败 **
属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errNo | int | 错误码 |
| errMsg | string | 错误信息 |

### 错误码

| errNo | errMsg | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| 20001 | invalid param | 参数错误 | 6.3.3 |
| 20000 | no permission | 无调用权限，请联系客服添加 | 6.3.3 |
| 10104 | invoke too frequently | 频控限制 | 6.3.3 |
| 10401 | internal error | 小游戏框架内部错误，有需要请[创建工单](https://developer.open-douyin.com/work-order-page?tab=workOrderRecord)咨询 | 6.3.3 |

### 使用示例

```csharp
// 期望 30s 后出卡
var currentTime = DateTimeOffset.UtcNow;
var milliseconds = currentTime.ToUnixTimeMilliseconds();
var targetMilliSeconds = milliseconds + 30 * 1000;

var param = new StoreFeedDataParam()
{
    Scene = 1,
    ContentID = "contentID123",
    LeftValue = "timeStampMs",
    Operator = ">=",
    RightValue = targetMilliSeconds.ToString(),
    Status = 1,
    Extra = "ExtraInfo",
    Success = (_) => { Debug.Log($"StoreFeedData success."); },
    Fail = (err) => { Debug.Log($"StoreFeedData failed: {err}"); }
};
TT.StoreFeedData(param);
```

## TT.GetFeedData
> TTSDK 6.3.3 及以后版本支持
获取游戏是否直玩就绪状态数据。
### 语法

```java
public static void GetFeedData(GetFeedDataParam param)
```

### 参数说明
param 为 GetFeedDataParam 类型，属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| scene | int |  | 是 | 订阅的场景 ID | 6.3.3 |
| contentID | string |  | 是 | 自定义文案的 contentID，contentID 在后台申请开通直玩能力后可获取 | 6.3.3 |
| success | function |  | 否 | 接口调用成功的回调函数 | 6.3.3 |
| fail | function |  | 否 | 接口调用失败的回调函数 | 6.3.3 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） | 6.3.3 |

#### scene 参数说明

| 值 | 说明 |
| --- | --- |
| 1 | 离线收益场景 |
| 2 | 体力恢复场景 |
| 3 | 重要事件掉落 |

### **回调成功 **
属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| errMsg | string | 回调信息 | 6.3.3 |
| extra | string | 补充字段 | 6.3.3 |
| status | int | 当前直玩状态是否就绪 | 6.3.3 |

### **回调失败 **
属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errNo | int | 错误码 |
| errMsg | string | 错误信息 |

### 错误码

| errNo | errMsg | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| 20001 | invalid param | 参数错误 | 6.3.3 |
| 10104 | invoke too frequently | 频控限制 | 6.3.3 |
| 10401 | internal error | 小游戏框架内部错误，有需要请[创建工单](https://developer.open-douyin.com/work-order-page?tab=workOrderRecord)咨询 | 6.3.3 |

### 使用示例

```csharp
var param = new GetFeedDataParam()
{
    Scene = 1,
    ContentID = "contentID123",
    Success = (res) => { Debug.Log($"GetFeedData called successfully. Status: {res.status}, extra: {res.extra}"); },
    Fail = (err) => { Debug.Log($"GetFeedData failed: {err}"); }
};
TT.GetFeedData(param);
```

#
