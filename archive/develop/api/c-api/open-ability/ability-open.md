---
title: "平台开放能力"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/ability-open
update_time: 2024-11-11
---

> 注意：
> 该模块主要包含与平台开放能力相关。

## TT.OpenAwemeUserProfile
> 6.0.0 开始支持本方法
关注抖音号。

| 前提条件 | 该功能为抖音专有 API，使用该功能前开发者需要绑定想要查看的抖音号，参考[游戏内关注抖音号能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/-retention/follow-douyin/)接入指南 需要在开发者平台-设置中绑定抖音号 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 目前该接口只支持抖音，所以请在**抖音**或**抖音Lite** APP中调用 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void OpenAwemeUserProfile(Action followCallback, 
    Action<int, string> errCallback,
    bool showToastTipsIfFailed = true)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| followCallback | Action | -- | 是 | 完成打开抖音号的回调。涉及用户信息，无法获取用户是否关注了抖音号的状态 |
| errCallback | Action<int, string> | -- | 是 | 打开抖音号失败的回调。errCode: CODE_ERROR = -1 CODE_NOT_SUPPORT = -2 CODE_NOT_LOGIN = -3 CODE_NO_ACTIVITY = -4 CODE_UID_ERROR = -5 |
| showToastTipsIfFailed | bool | true | 否 | 当关注抖音号失败，是否显示Toast弹窗提示，默认显示 |

### 代码示例

```csharp
public void TestDouyin()
{
    TT.OpenAwemeUserProfile(()=>{
        Debug.Log("OnFollowAwemeCallback");
    }, 
    (errCode, errMsg) ={
        Debug.Log("OnFollowAwemeError errCode " +  errCode + " errMsg "+ errMsg);
    });
}
```

## TT.CheckFollowAwemeState
> 6.0.0 开始支持本方法
是否已关注抖音号。

| 前提条件 | 该功能为抖音专有 API，使用该功能前开发者需要绑定想要查看的抖音号，参考[游戏内关注抖音号能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/-retention/follow-douyin/)接入指南 前往小游戏开发者后台，进入“设置-基础设置”模块，在“抖音号绑定”一栏点击“去绑定” 进入“抖音号绑定”页面，使用需绑定的抖音号，打开手机使用抖音 APP 扫一扫。 （绑定成功暂不支持更换，请谨慎选择需绑定的抖音号） |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 目前该接口只支持抖音，所以请在**抖音**或**抖音Lite** APP中调用 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void CheckFollowAwemeState(Action<bool> callback)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| callback | Action<bool> | -- | 是 | 返回是否关注抖音结果 |

### 代码示例

```csharp
public void TestDouyin()
{
    TT.CheckFollowAwemeState(follow => {         
        Debug.Log("IsFollowDouyin: " + follow); 
    });
}
```

## TT.CheckBoundAweme
> 6.0.0 开始支持本方法
是否在小程序开发者后台绑定了抖音号。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void CheckBoundAweme(Action<bool> callback)
```

### **参数说明 **
### 代码示例

```csharp
public void TestDouyin()
{
    TT.CheckBoundAweme((isBinded) => { 
        Debug.Log("IsBindDouyin: \nisBinded: " + isBinded); 
    });
}
```

## TT.AddShortcut
> 6.0.0 开始支持本方法
可以将小游戏快捷方式添加到手机桌面上。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 目前仅支持抖音和抖 lite，请在其它 app 做屏蔽 |
| 注意事项 | 该 API 必须要由用户点击触发 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void AddShortcut(Action<bool> csCallback, 
    bool showToastTipsIfFailed = true)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| csCallback | Action<bool> | -- | 是 | 创建快捷方式回调，参数为是否成功，true表示成功，false表示失败 |
| showToastTipsIfFailed | bool | true | 否 | 当创建失败，是否显示Toast弹窗提示，默认显示 |

### 代码示例

```csharp
public void TestDouyin()
{
    TT.AddShortcut(bSuccess =>{
        Debug.Log("OnCreateShortcut : "+  bSuccess);
    });
}
```

## TT.CheckShortcut
> 6.0.0 开始支持本方法
快捷方式是否已经创建。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 目前仅支持抖音和抖 lite，请在其它 app 做屏蔽 仅在Android上支持 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void CheckShortcut(Action<bool> isExistCallback)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| isExistCallback | Action<bool> | -- | 是 | 是否存在的回调，参数表示是否已创建，true表示已创建，false表示未创建 |

### 代码示例

```csharp
public void TestDouyin()
{
    TT.CheckShortcut(exist => { 
        Debug.Log("Shortcut exist: " + exist); 
    });
}
```

## TT.NavigateToVideoView
> 6.0.0 开始支持本方法
跳转到抖音视频。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void NavigateToVideoView(string videoId, Action<bool> jumpCallback)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| videoId | string | -- | 是 | 抖音视频 videoId，复制抖音视频链接到浏览器即可得到 |
| jumpCallback | Action<bool> | -- | 是 | 跳转结果，参数为是否成功 |

### 代码示例

```csharp
public void TestDouyin()
{
    string videoId = "xxxxxx";
    TT.NavigateToVideoView(videoId,
        success =>
        {   
            Debug.Log("NavigateToVideoView: issuccess  " + success);
        });
}
```

## 
## TT.GetRoomInfo
> 6.0.0 开始支持本方法
查询直播房间信息。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void GetRoomInfo(Action<bool, JsonData> statusCallback)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| statusCallback | Action<bool, JsonData> | -- | 是 | 调用结果 |

### 代码示例

```csharp
public void TestDouyin()
{
    
    TT.GetRoomInfo((isSuccess, data) =>
    {
        if (isSuccess)
        {
            Debug.Log($"Call GetRoomInfo success, {data.ToJson()}");
        }
        else
        {
            var errCode = data["errCode"];
            var errMsg = data["errMsg"];
            Debug.Log($"Call GetRoomInfo fail, errCode:{errCode}, errMsg:{errMsg}");
        }
    });
}
```

## TT.RequestSubscribeMessage
> 6.0.0 开始支持本方法
调起客户端订阅消息界面，返回用户订阅消息的操作结果。当用户勾选了订阅面板中的 “总是保持以上选择，不再询问” 时，或是点击了订阅面板中 “拒绝，不再询问” 时，模板消息会被添加到用户的小程序设置页，用户可以在设置页面进行管理。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void RequestSubscribeMessage(List<string> tmplIds,
    Action<Dictionary<string, string>> success = null, 
    Action complete = null,
    Action<int, string> failed = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| tmplIds | List<string> | -- | 是 | 需要订阅的消息模板的 id 的集合，最多支持传入三个 tmplId |
| success | Action<Dictionary<string, string>> | null | 否 | 接口调用成功的回调函数 |
| complete | Action | null | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |
| failed | Action<int, string> | null | 否 | 接口调用失败的回调函数 |

### 代码示例

```csharp
public void TestDouyin()
{
    var tmplIds = new List<string>();
    tmplIds.Add("xxxxxxxx");
    
    TT.RequestSubscribeMessage(tmplIds, (data) =>
    {
        Debug.Log($"success call request subscribe message, {data.ToJson()}");
    }, () =>
    {
        Debug.Log("complete call request subscribe message");
    }, (errCode, errMsg) =>
    {
        Debug.Log($"complete call requestSubscribeMessage fail,errCode -->{errCode},errMsg-->{errMsg}");
    });
}
```

## TT.GetMenuButtonLayout
> 6.0.0 开始支持本方法
获取菜单按钮（右上角胶囊按钮）的布局位置信息。坐标信息以屏幕左上角为原点。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static JsonData GetMenuButtonLayout()
```

### 返回说明

| 属性名 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| width | int | -- | 宽度，单位：dp |
| height | int | -- | 高度，单位：dp |
| top | int | -- | 上边界坐标，单位：dp |
| bottom | int | -- | 下边界坐标，单位：dp |
| right | int | -- | 右边界坐标，单位：dp |
| left | int | -- | 左边界坐标，单位：dp |

### 代码示例

```csharp
public void TestDouyin()
{
    var json = TT.GetMenuButtonLayout();
    Debug.Log(json != null ? $"menu layout: {json.ToJson()}" : "menu layout is null");
}
```

## TT.Authorize
> 6.0.0 开始支持本方法
提前向用户发出授权请求。该方法不会调用对应接口，只会弹框咨询用户是否授权或者获取用户信息。如果用户之前有授权，该接口直接返回成功，不会跟用户产生交互。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void Authorize(string scope, 
    Action<string, JsonData> success,
    Action<string, string> fail)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| scope | string | -- | 是 | 需要预授权的 scope，详见 [用户授权_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/user-information/authorization/authorization) |
| success | Action<string, JsonData> | -- | 是 | 接口调用成功的回调函数 |
| fail | Action<string, string> | -- | 是 | 接口调用失败的回调函数 |

### 代码示例

```csharp
public void TestDouyin()
{
    TT.Authorize("scope.userInfo",(errMsg, data) =>
    {
        Debug.Log("Msg " + errMsg + " data " + data.ToJson());
    }, (code, message) =>
    {
        Debug.Log("Code " + code + " Message " + message);
    });
}
```
