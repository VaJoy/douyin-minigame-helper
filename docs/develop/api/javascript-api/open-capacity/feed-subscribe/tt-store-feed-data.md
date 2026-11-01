---
title: "tt.storeFeedData"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/feed-subscribe/tt-store-feed-data
update_time: 2025-10-27
---

## 语法

```js
tt.storeFeedData(extra, scene, status, contentID, leftValue, operator, rightValue)
```
基础库 3.67.0 开始支持本方法，这是一个**异步**方法。
存储游戏是否直玩就绪状态。

## 示例代码
当前时间戳大于等于1744340968580时，满足直玩就绪条件
```js
tt.storeFeedData({
  scene: 1, // 离线收益场景
  status: 1, // 是否就绪：0-未就绪，1-就绪
  contentID: 'contentID123', // contentID
  leftValue: 'timeStampMs',
  operator: '>=',
  rightValue: '1744340968580',
  success(res) {
    console.log('storeFeedData success', res)
  },
  fail(res) {
    console.log('storeFeedData fail', res)
  },
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| extra | string | 否 |  | 3.67.0 | 自定义补充字段 |
| scene | number | 是 |  | 3.67.0 | 订阅的场景 ID |
| status | number | 是 |  | 3.67.0 | 满足运算公式后，对应直玩场景是否就绪。0：未就绪， 1：就绪  **可选值：** 0=满足运算公式条件后，直玩状态为未就绪；1=满足运算公式条件后，直玩状态为已就绪 |
| contentID | string | 是 |  | 3.67.0 | 自定义文案的 contentID，contentID 在后台申请开通直玩能力后可获取 |
| leftValue | number | 是 |  | 3.67.0 | 运算公式的左值，当前只支持"timeStampMs"，即毫秒级时间戳  **可选值：** timeStampMs=毫秒级时间戳 |
| operator | number | 是 |  | 3.67.0 | 运算符  **可选值：** ==等于；>=大于；>==大于等于；<=小于；<==小于等于；!==不等于 |
| rightValue | string | 是 |  | 3.67.0 | 运算公式的右值 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："storeFeedData:ok" |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："storeFeedData:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："storeFeedData:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  | 3.67.0 |
| 20000 | no permission |  | 3.67.0 |
| 10104 | invoke too frequently |  | 3.67.0 |
| 10401 | internal error |  | 3.67.0 |

## 注意事项
当前接口面向无server小游戏，如果在开通直玩能力过程中配置了 OpenAPI，则无需调用此接口存储直玩状态

## 前置条件
在使用前需前往开发者后台，在运营能力 - 推荐流直出能力中申请开通，并获取对应场景值 scene，素材 contentID

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
