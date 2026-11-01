---
title: "直播能力"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/live-manager
update_time: 2025-09-01
---

## 
| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

## TT.GetLiveManager
> TTSDK 6.2.5 及以上版本支持该能力
获取直播能力管理对象。
#### 语法

```csharp
TT.GetLiveManager()
```

#### 参数说明
无
#### 返回值

| **类型** | **说明** |
| --- | --- |
| TTLiveManager | TTLiveManager 对象 |

以下接口能力全部通过 `TT.GetLiveManager()` 获取到的 **TTLiveManager** 对象调用。
## TTLiveManager.CheckRoomIsValid
> TTSDK 6.2.5 及以上版本支持该能力
检查直播间是否有效。回调成功即表示直播间有效，可以进入。
#### 语法

```json
TT.GetLiveManager().CheckRoomIsValid(JsonData param, 
    Action<JsonData> successCallback = null,
    Action<int, string> failedCallback = null,
    Action completeCallback = null);
```

#### 参数说明
JsonData 类型的 param 可以传入以下参数：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| roomID | string |  | 是 | 直播间ID。可以从`GetLiveStatus`中获取主播直播间id。 |

#### 使用示例

```csharp
var param = new JsonData
{
    ["roomID"] = roomId
};
TT.GetLiveManager().CheckRoomIsValid(param, 
    data =>
    {
        Debug.Log($"CheckRoomIsValid success,{data.ToJson()}");
    }, 
    (errCode, errMsg) =>
    {
        Debug.Log($"CheckRoomIsValid failed, errCode:{errCode}, errMsg:{errMsg}");
    }, () =>
    {
        Debug.Log("CheckRoomIsValid complete");
    });
```

## TTLiveManager.NavigateToLive
> TTSDK 6.2.5 及以上版本支持该能力
跳转到指定直播间。
### 语法

```json
TT.GetLiveManager().NavigateToLive(JsonData param,
    Action<JsonData> successCallback = null,
    Action<int, string> failedCallback = null,
    Action completeCallback = null)
```

### 参数说明
JsonData 类型的 param 可以传入以下参数：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| roomID | string |  | 是 | 直播间ID。可以从`GetLiveStatus`中获取主播直播间id。 |

### 使用示例

```csharp
var param = new JsonData
{
    ["roomID"] = roomId
};
TT.GetLiveManager().NavigateToLive(param, 
    data =>
    {
        Debug.Log($"NavigateToLive success,{data.ToJson()}");
    }, 
    (errCode, errMsg) =>
    {
        Debug.Log($"NavigateToLive failed, errCode:{errCode}, errMsg:{errMsg}");
    }, () =>
    {
        Debug.Log("NavigateToLive complete");
    });
```

## TTLiveManager.GetLiveStatus
> TTSDK 6.2.5 及以上版本支持该能力
查询小游戏关联的小玩法主播直播信息。
#### 语法

```json
TT.GetLiveManager().GetLiveStatus(GetLiveStatusParam)
```

#### 参数说明
NavigateToLiveParam 类包含参数如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| OpenIdList | List<string> |  | 是 | 要查询的主播openId列表 |
| Success | Delegate GetLiveStatusSuccessCallback |  | 否 | 接口调用成功的回调函数 |
| Fail | Action<ErrorInfo> |  | 否 | 接口调用失败的回调函数 |
| Complete | Action |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

Success 是一个 delegate，接收`GetLiveStatusSuccessResult` 类型参数，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| LiveStatus | Dictionary<string, TTLiveStatus> | 传入的OpenIdList对应的主播直播信息列表 |

`TTLiveStatus` 包含以下属性：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| OpenId | string | 主播的openId |
| IsOnLive | bool | 是否正在直播 |
| NickName | string | 昵称 |
| AppId | string | 对应玩法的Id |
| AvatarUrl | string | 主播头像 |
| RoomId | string | 直播间Id |

#### 使用示例

```csharp
TT.GetLiveManager().GetLiveStatus(new GetLiveStatusParam()
{
    OpenIdList = openIds,
    Success = data =>
    {
        Debug.Log($"getLiveStatus success,{data.ToJson()}");
    },
    Fail = error =>
    {
        Debug.Log($"getLiveStatus failed, errCode:{error.ErrorCode}, errMsg:{error.ErrMsg}, errorType: {error.ErrorType}");
    }
});
```

## TTLiveManager.OnXScreenSizeChange
> TTSDK 6.2.5 及以上版本支持该能力
监听 X 分屏，全屏/半屏 切换事件。
#### 语法

```csharp
void OnXScreenSizeChange(OnXScreenSizeChangeCallback callback);
```

#### 参数说明
##### **callback**
callback 是一个 delegate，接收的参数如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| Type | XScreenType enum | 当前X分屏变化事件类型 |

Type 为 enum 类型，其枚举值如下：

| 枚举值 | **说明** |
| --- | --- |
| EnlargeBegin | X分屏开始由半屏变为全屏 |
| EnlargeEnd | X分屏由半屏变为全屏结束 |
| ReduceBegin | X分屏开始由全屏变为半屏 |
| ReduceEnd | X分屏由全屏变为半屏结束 |

#### 返回值
无
#### 使用示例

```csharp
private void OnXScreenChange(OnXScreenSizeChangeResult result)
{
    Debug.Log($"OnXScreenChange, type:{result.Type}");
}

private void OnXScreenChange()
{
    TT.GetLiveManager().OnXScreenSizeChange(OnXScreenChange);
}
```

## **TTLiveManager.OffXScreenSizeChange**
> TTSDK 6.2.5及以上版本支持该能力
取消监听 X 分屏，全屏/半屏 切换事件。
#### 语法

```csharp
void OffXScreenSizeChange(OnXScreenSizeChangeCallback callback = null);
```

#### 参数说明
##### **callback**
callback 是一个 delegate，接收的参数如下（不传则会删除所有 callback）：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| Type | XScreenType enum | 当前X分屏变化事件类型 |

#### 返回值
无
#### 使用示例

```csharp
TT.GetLiveManager().OffXScreenSizeChange();
```

## **TTLiveManager.GetLiveSetting**
> TTSDK 6.5.3 及以上版本支持该能力
获取直播环境配置信息。
#### 语法

```csharp
TT.GetLiveManager().GetLiveSetting(GetLiveSettingParam param)
```

#### 参数说明
GetLiveSettingParam 类包含参数如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| Success | Action<GetLiveSettingResult> |  | 否 | 接口调用成功的回调函数 |
| Fail | Action<ErrorInfo> |  | 否 | 接口调用失败的回调函数 |
| Complete | Action |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

Success 接收 GetLiveSettingResult 类型参数，属性如下：

| 属性名 | 类型 | 说明 |  |
| --- | --- | --- | --- |
| ErrMsg | string | "LiveManager.getLiveSetting:ok" |  |
| IsVideoLive | bool | 当前是否为直播场景 |  |
| IsAnchor | bool | 当前玩家身份是否是主播 |  |
| InstantPlay | bool | 是否开通即看即玩能力并且主播端开关已打开 |  |

#### 使用示例

```csharp
TT.GetLiveManager().GetLiveSetting(new GetLiveSettingParam()
{
    Success = data =>
    {
        Debug.Log($"getLiveSetting success, {data.ToJson()}");
    },
    Fail = error =>
    {
        Debug.Log($"getLiveSetting failed, errCode:{error.ErrorCode}, errMsg:{error.ErrMsg}, errorType: {error.ErrorType}");
    }
});
```

## **TTLiveManager.UploadGameProgress**
> TTSDK 6.5.3 及以上版本支持该能力
上传主播游玩场景配置。

| 前提条件 | 使用前，请先前往游戏开放后台，申请开通直播即看即玩能力 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 仅在直播场景下可调用 |
| 注意事项 | 无 |
| 相关教程 | [直播即看即玩能力技术指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/instant-play-introduce) |

#### 语法

```csharp
TT.GetLiveManager().UploadGameProgress(UploadGameProgressParam param)
```

#### 参数说明
UploadGameProgressParam 类包含参数如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| Data | string |  | 是 | 游玩进度配置信息，长度不超过512KB |
| Success | Action<UploadGameProgressResult> |  | 否 | 接口调用成功的回调函数 |
| Fail | Action<ErrorInfo> |  | 否 | 接口调用失败的回调函数 |
| Complete | Action |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

Success 接收 UploadGameProgressResult 类型参数，属性如下：

| 属性名 | 类型 | 说明 |  |
| --- | --- | --- | --- |
| ErrMsg | string | "LiveManager.uploadGameProgress:ok" |  |

#### 错误码

| errNo | errMsg | 说明 |
| --- | --- | --- |
| 20001 | invalid param | 参数类型错误 |
| 21100 | can only call in video live | 仅在视频直播和伴侣挂载启动场景下可调用 |
| 21101 | can only call in anchor side | 仅在主播端可调用 |
| 21102 | the game's instant play is closed. | 游戏未开通即玩能力 |
| 21103 | anchor's instant play is closed | 主播未打开即玩开关 |
| 21104 | frequency limit | 频控限制 (10s/每次） |
| 21105 | data is too large | 数据过大（512KB） |
| 21106 | server error | 服务端错误 |

#### 使用示例

```csharp
TT.GetLiveManager().UploadGameProgress(new UploadGameProgressParam()
{
    Data = "foobar",
    Success = data =>
    {
        Debug.Log($"uploadGameProgress success, {data.ToJson()}");
    },
    Fail = error =>
    {
        Debug.Log($"uploadGameProgress failed, errCode:{error.ErrorCode}, errMsg:{error.ErrMsg}, errorType: {error.ErrorType}");
    }
});
```

## **TTLiveManager.SyncGameProgress**
> TTSDK 6.5.3 及以上版本支持该能力
观众侧同步主播游玩进度配置信息。

| 前提条件 | 使用前，请先前往游戏开放后台，申请开通直播即看即玩能力 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 仅在直播场景下可调用 |
| 注意事项 | 在一次小游戏启动周期内，data 的值不会发生变化，只有重新进入游戏才会刷新 |
| 相关教程 | [直播即看即玩能力技术指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/instant-play-introduce) |

#### 语法

```csharp
TT.GetLiveManager().SyncGameProgress(SyncGameProgressParam param)
```

#### 参数说明
SyncGameProgressParam 类包含参数如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| Success | Action<SyncGameProgressResult> |  | 否 | 接口调用成功的回调函数 |
| Fail | Action<ErrorInfo> |  | 否 | 接口调用失败的回调函数 |
| Complete | Action |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

Success 接收 SyncGameProgressResult 类型参数，属性如下：

| 属性名 | 类型 | 说明 |  |
| --- | --- | --- | --- |
| ErrMsg | string | "LiveManager.uploadGameProgress:ok" |  |
| Data | string | 主播游玩进度配置信息 |  |

#### 错误码

| errNo | errMsg | 说明 |
| --- | --- | --- |
| 21100 | can only call in video live | 仅在主播视频开播或伴侣挂载启动游戏开播场景下可调用 |
| 21101 | can only call in audience side | 仅在观众端可调用 |
| 21102 | the game's instant play is closed | 游戏未开通即玩能力 |
| 21103 | anchor's instant play is closed | 主播未打开即玩开关 |
| 21104 | serve error | 服务端错误 |

#### 使用示例

```csharp
TT.GetLiveManager().SyncGameProgress(new SyncGameProgressParam()
{
    Success = data =>
    {
        Debug.Log($"syncGameProgress success, {data.ToJson()}");
    },
    Fail = error =>
    {
        Debug.Log($"syncGameProgress failed, errCode:{error.ErrorCode}, errMsg:{error.ErrMsg}, errorType: {error.ErrorType}");
    }
});
```

## TTLiveManager.OnInstantPlayStatusChange
> TTSDK 6.5.3 及以上版本支持该能力
注册即看即玩开关状态变化监听函数。

| 前提条件 | 使用前，请先前往游戏开放后台，申请开通直播即看即玩能力 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 仅在直播场景下可调用 |
| 注意事项 | 无 |
| 相关教程 | [直播即看即玩能力技术指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/instant-play-introduce) |

#### 语法

```csharp
void OnInstantPlayStatusChange(OnInstantPlayStatusChangeCallback callback);
```

#### 参数说明
##### **callback**
callback 是一个 delegate，接收的参数如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| InstantPlayStatus | bool | 主播即玩开关状态 |

#### 返回值
无
#### 使用示例

```csharp
void OnInstantPlayStatusChangeCallback(OnInstantPlayStatusChangeResult result)
{
    Debug.Log($"OnInstantPlayStatusChangeResult: {result.ToJson()}");
}

TT.GetLiveManager().OnInstantPlayStatusChange(OnInstantPlayStatusChangeCallback);
```

## TTLiveManager.OffInstantPlayStatusChange
> TTSDK 6.5.3 及以上版本支持该能力
取消监听即看即玩开关状态变化。

| 前提条件 | 使用前，请先前往游戏开放后台，申请开通直播即看即玩能力 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 仅在直播场景下可调用 |
| 注意事项 | 无 |
| 相关教程 | [直播即看即玩能力技术指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/instant-play-introduce) |

#### 语法

```csharp
void OffInstantPlayStatusChange(OnInstantPlayStatusChangeCallback callback = null);
```

#### 参数说明
##### **callback**
callback 是一个 delegate，同 `TTLiveManager.OnInstantPlayStatusChange`。（不传则会删除所有 callback）。
#### 返回值
无
#### 使用示例

```csharp
TT.GetLiveManager().OffInstantPlayStatusChange();
```
