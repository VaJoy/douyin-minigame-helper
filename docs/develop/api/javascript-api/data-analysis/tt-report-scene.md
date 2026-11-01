---
title: "tt.reportScene"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/data-analysis/tt-report-scene
update_time: 2024-09-26
---

## 语法

```js
tt.reportScene(costTime, sceneId, dimension, metric)
```
基础库 2.88.0 开始支持本方法，这是一个**异步**方法。
自定义启动场景数据上报接口，调用该接口上报场景数据（场景需在开发者后台配置）后，开发者可以在[抖音开放平台](https://developer.open-douyin.com/)，进入「数据」-「性能分析」-「启动性能」-「启动场景配置」模块，看上报数据，进行数据挖掘分析。使用前请注意阅读[相关说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/startup-performance/startup-scene-analysis)。 ​

## 示例代码
```js
tt.reportScene({
  sceneId: 1000,
  costTime: 350,
  dimension: {
    d1: '2.1.0', // value仅支持传入String类型。若value表示Boolean，请将值处理为'0'、'1'进行上报；若value为Number，请转换为String进行上报
  },
  metric: {
    m1: '546', // value仅支持传入数值且需要转换为String类型进行上报
  },
  success(res) {
    // 上报接口执行完成后的回调，用于检查上报数据是否符合预期
    console.log(res)
  },
  fail(res) {
    // 上报报错时的回调，用于查看上报错误的原因：如参数类型错误等
    console.log(res)
  }
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| costTime | number | 否 | 0 | 2.88.0 | 场景耗时，单位ms |
| sceneId | number | 是 |  | 2.88.0 | ​场景ID，登录[抖音开放平台](https://developer.open-douyin.com/)，进入「数据」-「性能分析」-「启动性能」-「启动场景配置」模块，添加游戏的自定义启动场景。 游戏每次启动只可以上报一次​ |
| dimension | Object | 否 | {} | 2.88.0 | 自定义维度数据。只支持能够通过 JSON.stringify 序列化的对象，且序列化后长度不超过 1024 个字符 ​ |
| metric | Object | 否 | {} | 2.88.0 | 自定义指标数据。只支持能够通过 JSON.stringify 序列化的对象，且序列化后长度不超过 1024 个字符 ​ |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："reportScene:ok" - **data**（Object）：开发者上报的原始数据 |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："reportScene:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |
| 20001 | params.${name} cannot exceed ${DATA_STRINGIFY_LENGTH_LIMIT} characters |  |  |

## 前置条件
登录[抖音开放平台](https://developer.open-douyin.com/)，进入「数据」-「性能分析」-「启动性能」-「启动场景配置」模块，添加游戏的自定义启动场景。

## 相关课程
[启动场景上报分析](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/startup-performance/startup-scene-analysis)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/open-capacity/data-analysis/tt-report-scene) / [本地体验路径](tt-report-analytics)
