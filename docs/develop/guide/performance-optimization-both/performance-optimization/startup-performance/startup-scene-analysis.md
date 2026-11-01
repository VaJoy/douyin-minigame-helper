---
title: "启动场景上报分析"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/performance-optimization/startup-performance/startup-scene-analysis
update_time: 2024-12-10
---

## **概述 **
用户在体验小游戏时，对启动时长非常敏感，通常随着小游戏启动时间的增长，用户流失会越多。因此启动时间的长短直接影响到新进留存效果的好坏。
为了帮助开发者主动发现游戏可交互前的各个阶段的性能、留存情况，平台提供了从「启动点击」开始到「首屏渲染完成」为止的启动数据分析，开发者可以通过[性能分析-启动数据](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/about-data/performance-analysis/startup-data)了解小游戏的启动时序和查看关键的启动数据。
除此之外，在用户真正与游戏发生交互前，通常还会包含许多游戏的业务资源下载和逻辑处理，开发者也可以通过 [tt.reportScene](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/data-analysis/tt-report-scene)实现自定义启动场景数据的上报。
## **启动场景上报 **
> **说明：** 游戏可交互 - 用户最早可操作游戏的时间；

  将小游戏的系统启动场景与开发者自定义启动场景进行关联，提供从「用户点击」到「游戏可交互」的全流程漏斗分析能力，帮助开发者精确地分析各个启动环节的耗时和留存情况；默认提供多种维度的数据筛选，包括小游戏入口、宿主、设备类型和场景入口。
### **场景说明**
为了帮助开发者更好地统计分析用户的启动阶段耗时以及留存情况，平台将启动场景分为两个部分：
- **系统启动场景**：系统自带场景、维度、指标的上报，无需开发者手动上报；
- **自定义启动场景**：开发者可以通过**主动调用 **[**tt.reportScene**](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/data-analysis/tt-report-scene)**接口上报**自定义的启动场景；
**注意：**启动场景上报能力仅适用于启动阶段分析，对于其他场景的统计上报，可能会无法得出正确结论，不建议使用。
#### **系统启动场景 **
围绕小游戏的启动流程，平台默认提供了部分启动场景，其中大部分场景无需开发者手动上报，但某些场景的统计，需要开发者**主动调用接口**来上报数据，以便平台能够准确统计该场景的耗时情况。具体的场景说明如下表所示：

| 场景ID | 场景名称 | 场景说明 |
| --- | --- | --- |
| 7001 | 游戏可交互 | 资源加载完毕，用户最早可操作游戏画面的时机（如新手引导或游戏主大厅界面） |

## **使用方法 **
### **新建启动场景 **
登录[抖音开放平台](https://developer.open-douyin.com/)，进入「数据」-「性能分析」-「启动监控」-「启动场景配置」模块，添加游戏的自定义启动场景。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/935c95c8d6044f048b81afe9e615823a)

### **上报自定义启动场景 **
更多参数请参考 [tt.reportScene接口文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/data-analysis/tt-report-scene)

```js
// 接口上报示例代码，当基础库版本>=2.88.0才能使用此能力
tt.reportScene({
  sceneId: 1000,  //「必填」sceneId 为「新建场景」后，由系统生成的场景 Id 值，用于区分当前是哪个启动场景的数据
  costTime: 365,  //「非必填」costTime 为当前场景的耗时(ms)，非必填，默认为 0
  dimension: {
    d1: 'test', //「非必填」value仅支持传入String类型。若value表示Boolean，请将值处理为0、1进行上报；若value为Number，请转换为String进行上报
  },
  success(res) {// 上报接口执行完成后的回调，用于检查上报数据是否符合预期，也可通过启动调试能力进行验证
    console.log(res);
  },
  fail(res) {// 上报报错时的回调，用于查看上报错误的原因：如参数类型错误等
    console.log(res);
  },
})
```

C# API请参考 [TT.ReportScene接口文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/data-analysis#86bffde4)

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

## **数据分析 **
分析包含系统启动场景和开发者的自定义启动场景， 登录[抖音开放平台](https://developer.open-douyin.com/)，进入「数据」-「性能分析」-「启动监控」-「启动数据」模块，查看统计上报的数据。
更多详情请参考[性能分析-启动数据](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/about-data/performance-analysis/startup-data)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1c0d8783b7c8497fb75e8d0696c36512)
