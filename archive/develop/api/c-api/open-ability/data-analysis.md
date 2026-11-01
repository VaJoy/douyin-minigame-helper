---
title: "数据分析"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/data-analysis
update_time: 2024-12-24
---

该模块包含两种上报数据的接口。
## TT.ReportAnalytics
> 6.0.0 开始支持本方法
自定义分析数据上报接口，调用后，会将数据上报到小程序开发者平台，开发者可以在小程序开发者平台中查看上报数据。

> 注意：
> 该接口对应 [旧版Unity SDK文档中的【自定义事件】](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#ccf3fb3e)
> 可参考数据中心文档：[ 数据中心 / 自定义分析 / 事件管理 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/data/data-center/advanced-analysis/events)

| 前提条件 | 在【抖音开放平台】-【数据分析】-【自定义分析】 中添加事件 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 使用前，需要在小程序管理后台事件中新建事件，配置好事件名与字段。 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void ReportAnalytics<T>(string eventName, Dictionary<string, T> param = null);
```

### 参数说明

| 参数名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| eventName | string | -- | 是 | 事件名 |
| param | Dictionary<string, T> | null | 否 | 上报的数据 key: 配置中的字段名. value(number\|string\|boolean) : 上报的数据 |

### 代码示例

```csharp
void ReportTest()
{
    Dictionary<string, string> tmpDic = new Dictionary<string, string>();
    tmpDic.Add("start", "start1");
    TT.ReportAnalytics("startgame", tmpDic);
    Debug.Log("上报自定义埋点：start");
}
```

## TT.ReportScene
> 6.0.0 开始支持本方法
自定义启动场景数据上报接口，调用该接口上报场景数据（场景需在开发者后台配置）后，开发者可以在[抖音开放平台](https://developer.open-douyin.com/)，进入「数据」-「性能分析」-「启动监控」-「启动场景配置」模块，看上报数据，进行数据挖掘分析。使用前请注意阅读[相关说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/startup-performance/startup-scene-analysis)。

| 前提条件 | 登录[抖音开放平台](https://developer.open-douyin.com/)，进入「数据」-「性能分析」-「启动监控」-「启动场景配置」模块，添加游戏的自定义启动场景。 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | [启动场景上报分析](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/startup-performance/startup-scene-analysis) |

### **语法 **

```csharp
public static void ReportScene(JsonData param, 
    Action<JsonData> success = null,
    Action<int, string> failed = null, 
    Action complete = null)
```

### 参数说明

| 参数名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| param | JsonData | -- | 是 | 例如  "{"sceneId":0,"costTime":10} // 必传参数 "sceneId" 场景 ID，int 或 long 类型登录抖音开放平台，进入「数据」-「性能分析」-「启动监控」-「启动场景配置」模块，进入添加事件场景，新建游戏的自定义启动场景。 游戏每次启动只可以上报一次 "costTime" 场景耗时，单位 ms long类型 "{"sceneId":0,"costTime":10,"dimension":{"d1":"value1"}, "metric":{"m1":"value2"}}" // dimension，metric 非必传 "dimension" ，非必需参数，为空则不要传。自定义维度数据，key 在抖音开放平台获取。只支持能够通过 JSON.stringify 序列化的对象，且序列化后长度不超过 1024 个字符  "metric"，非必需参数，为空则不要传。自定义指标数据，key在抖音开放平台获取。只支持能够通过 JSON.stringify 序列化的对象，且序列化后长度不超过 1024 个字符 |
| success | Action<JsonData> | null | 否 | 成功返回 |
| failed | Action<int, string> | null | 否 | 失败返回 |
| complete | Action | null | 否 | 完成返回 |

### 回调成功
Action<JsonData> 类型，为开发者上报的原始数据。
### 回调失败
Action<int, string>  类型，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errCode | int | 错误码 |
| errMsg | string | "reportScene:fail" + 详细错误信息 |

### 错误码

| errNo | errMsg | 说明 |
| --- | --- | --- |
| 20000 | access:fail path is invalid | path 参数错误 |
| 20001 | access:fail param should be xxx, but got xxx | 参数校验错误 |
| 21101 | access:fail permission denied, access {path_value} | 访问路径不可读 |
| 21102 | access:fail no such file or directory, access {path_value} | 访问文件不存在 |

### 代码示例

```csharp
void ReportTest()
{
    var param = new JsonData();
    int id = 7001;
    long time = 100;
    param["sceneId"] = id;
    param["costTime"] = time;
    TT.ReportScene(param, (res) =>
    {
        Debug.Log($"success:{res.ToJson()}");
    }, (code, msg) =>
    {
        Debug.LogError($"fail: code:{code},msg:{msg}");
    }, () =>
    {
        Debug.Log($"completed!");
    });
}
```

#
