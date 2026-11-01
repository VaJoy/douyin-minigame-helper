---
title: "侧边栏"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/sidebar
update_time: 2025-03-17
---

侧边栏功能相关接口。

> 注意：
> 该模块对应 [侧边栏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#215b9294) 。

## TT.CheckScene
> 6.0.0 开始支持本方法
确认当前宿主版本是否支持跳转某个小游戏入口场景，目前仅支持「侧边栏」场景。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void CheckScene(TTSideBar.SceneEnum scene, 
    Action<bool> success, 
    Action complete, 
    Action<int, string> error)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 注意 |
| --- | --- | --- | --- | --- |
| scene | TTSideBar.SceneEnum | -- | 是 | 需要确认的入口场景（目前仅支持 'sidebar'） |
| success | Action<bool> | -- | 是 | 接口调用成功的回调函数, bool 为 true 说明支持，false 表示不支持 |
| complete | Action | -- | 是 | 接口调用结束的回调函数（调用成功、失败都会执行） |
| error | Action<int, string> | -- | 是 | 接口调用失败的回调函数 |

### 代码示例

```csharp
public void TestSidebar()
{
    TT.CheckScene(TTSideBar.SceneEnum.SideBar, b =>
    {
        Debug.Log("check scene success，"+b );
    }, () =>
    {
        Debug.Log("check scene complete");
    }, (errCode, errMsg) =>
    {
        Debug.Log($"check scene error, errCode:{errCode}, errMsg:{errMsg}");
    });
}
```

## TT.NavigateToScene
> 6.0.0 开始支持本方法
跳转到某个小游戏入口场景，目前仅支持跳转「侧边栏」场景。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 仅支持抖音宿主。可以通过 TT.CheckScene 判断是否当前宿主是否支持 |
| 注意事项 | 通过侧边栏入口进入小游戏时，[TT.GetAppLifeCycle().OnShow](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/system/game-lifecycle) 会在监听回调中新增两个返回字段 launchFrom = 'homepage' 和 location = 'sidebar_card' ，可用于判断用户是否从该入口场景进入小游戏 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void NavigateToScene(JsonData data, 
    Action success, 
    Action complete,
    Action<int, string> error)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 注意 |
| --- | --- | --- | --- | --- |
| data | JsonData | -- | 是 | 参数例子 {"scene":"sidebar"} |
| success | Action | -- | 是 | 接口调用成功的回调函数 |
| complete | Action | -- | 是 | 接口调用结束的回调函数（调用成功、失败都会执行） |
| error | Action<int, string> | -- | 是 | 接口调用失败的回调函数 |

### 代码示例

```csharp
public void TestSidebar()
{
    var data = new JsonData
    {
        ["scene"] = scene,
        ["activityId"] = cacheActivityId,
    };
    TT.NavigateToScene(data, () =>
    {
        Debug.Log("navigate to scene success");
    }, () =>
    {
        Debug.Log("navigate to scene complete");
    }, (errCode,errMsg) =>
    {
        Debug.Log($"navigate to scene error, errCode:{errCode}, errMsg:{errMsg}");
    });
}
```

## TT.RequestPromotionActivity
> 6.0.0 开始支持本方法
注册用户参与复访营销活动。当前只支持侧边栏复访活动。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void RequestPromotionActivity(JsonData data,
    Action<JsonData> success,
    Action complete,
    Action<int, string> error)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 注意 |
| --- | --- | --- | --- | --- |
| data | JsonData | -- | 是 | 指定用户参与的营销活动id，通过OpenAPI申请得到。未填写时，会由平台选择可用活动,可选，例如{"activityId":"111111"} |
| success | Action<JsonData> | -- | 是 | 接口调用成功的回调函数 |
| complete | Action | -- | 是 | 接口调用结束的回调函数（调用成功、失败都会执行） |
| error | Action<int, string> | -- | 是 | 接口调用失败的回调函数 |

### 代码示例

```csharp
public void TestSidebar()
{
    var data = new JsonData
    {
        ["activityId"] = "11111111"
    };
    Debug.Log($"Test Case RequestPromotionActivity -->{data}");
    
    TT.RequestPromotionActivity(data, (jsonData) =>
    {
        Debug.Log($"Test Case RequestPromotionActivity success callback -->{jsonData}");
        var activityId = jsonData.OptGetString("activityId");
        Debug.Log($"RequestPromotionActivity success, activityId-->{activityId}");
    }, () =>
    {
        Debug.Log($"Test Case RequestPromotionActivity complete");
    }, (errCode, errMsg) =>
    {
        Debug.Log($"Test Case RequestPromotionActivity failed, errCode-->{errCode}, errMsg-->{errMsg}");
    });
}
```

## TT.ReceiveCoupon
> 6.0.0 开始支持本方法
领取营销活动中完成任务后的奖励。当前只支持侧边栏复访活动。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void RequestPromotionActivity(JsonData data,
    Action<JsonData> success,
    Action complete,
    Action<int, string> error)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 注意 |
| --- | --- | --- | --- | --- |
| data | JsonData | -- | 是 | 指定用户参与的营销活动 id，通过 OpenAPI 申请得到。未填写时，会由平台选择可用活动,可选，例如{"activityId":"111111"} |
| success | Action<JsonData> | -- | 是 | 接口调用成功的回调函数 |
| complete | Action | -- | 是 | 接口调用结束的回调函数（调用成功、失败都会执行） |
| error | Action<int, string> | -- | 是 | 接口调用失败的回调函数 |

### 代码示例

```csharp
public void TestSidebar()
{
    var data = new JsonData
    {
        ["activityId"] = cacheActivityId
    };
    Debug.Log($"Test Case ReceiveCoupon -->{data}");
    
    TT.ReceiveCoupon(data, (jsonData) =>
    {
        Debug.Log($"Test Case ReceiveCoupon success callback -->{jsonData}");
    }, () =>
    {
        Debug.Log($"Test Case ReceiveCoupon complete");
    }, (errCode, errMsg) =>
    {
        Debug.Log($"Test Case ReceiveCoupon failed, errCode-->{errCode}, errMsg-->{errMsg}");
    });
}
```
