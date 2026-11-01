---
title: "tt.getImRankData"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/game-rank/getImRankData
update_time: 2024-07-24
---

## 语法

```js
tt.getImRankData(zoneId, dataType, relationType, pageSize, rankType, pageNum)
```
基础库 2.70.0 开始支持本方法，这是一个**异步**方法。
获取排序好的「好友/总榜」数据源，开发者基于数据源自行渲染返回的数据。

## 示例代码
```js
tt.getImRankData({
  relationType: "friend",
  dataType: 0,
  rankType: "month",
  pageNum: 1,
  pageSize: 40,
  zoneId: 'default',
  success(res) {
    console.log(`getImRankData success res: ${res}`);
  },
  fail(res) {
    console.log(`getImRankData fail res: ${res.errMsg}`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| zoneId | string | 否 | default | 2.70.0 | 排行榜分区标识，取值可以是 'default' 或 'test' 或其他开发者自定义字符串。'default' 表示为默认的线上分区，不同分区的排行榜数据存在数据隔离，如 zoneId='test' 设置的数据不会影响通过 zoneId='default' 的排行榜，可用于测试环境。目前每个小游戏除了 default 和 test， 最多可支持 10 个分区（未包括默认的线上分区） |
| dataType | number | 是 |  | 2.70.0 | 可选值： 0 或 1。0 表示返回数据被解析为 number。1 表示返回数据被解析为 string |
| relationType | number | 是 |  | 2.70.0 | 排行榜类型  **可选值：** friend=当前登录用户的好友的游戏数据排行；all=总榜 |
| pageSize | number | 是 |  | 2.70.0 | 每页长度，大于 0 小于 40 |
| rankType | string | 是 |  | 2.70.0 | 可选值：day、week、month、all |
| pageNum | number | 是 |  | 2.70.0 | 页码，从 1 开始 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **data**（Object）：接口调用结果 - **errMsg**（string）："getImRankData:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getImRankData:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | 暂不支持该能力 |  |  |
| 20001 | invalid param |  |  |
| 21101 | user not login |  |  |
| 21103 | internal error |  |  |
| 21102 | /s |  |  |
| 20000 | internal error |  |  |
| 10301 | feature is not supported in app xxx |  |  |
| 10601 | not login |  |  |
| 21104 | zone num exceeds limit |  |  |

## 使用限制
该方法需要在开放数据域中使用，请访问 [开放数据域能力介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data-base/)进行通信

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/tt-get-im-rank-data) / [本地体验路径](tt-get-im-rank-data)
