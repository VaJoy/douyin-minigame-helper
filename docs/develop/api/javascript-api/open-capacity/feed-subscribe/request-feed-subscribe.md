---
title: "tt.requestFeedSubscribe"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/feed-subscribe/request-feed-subscribe
update_time: 2024-10-11
---

## 语法

```js
tt.requestFeedSubscribe(scene, contentIDs, allScene, type)
```
基础库 3.34.0 开始支持本方法，这是一个**异步**方法。
向用户请求授权，允许游戏在满足一定的条件后出现在 Feed 流中

## 示例代码

发起单场景订阅

```js
tt.requestFeedSubscribe({
    type: "play",
    scene: 1,
    contentIDs: ["CONTENT123", "CONTENT234"],
    success(res) {
        console.log(res.success)
    },
    fail(res) {
        console.log(res.errMsg)
    },
})
```

发起全场景订阅

```js
tt.requestFeedSubscribe({
    type: "play",
    allScene: true,
    success(res) {
        console.log(res.success)
    },
    fail(res) {
        console.log(res.errMsg)
    },
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| scene | number | 否 |  | 3.34.0 | 订阅的场景 ID（非全场景下必传）  \|  \|  \| \| --- \| --- \| \| 值 \| 说明 \| \| 1 \| 离线收益场景 \| \| 2 \| 体力恢复场景 \| \| 3 \| 重要事件掉落 \| |
| contentIDs | Array<string> | 否 |  | 3.34.0 | Array<string>，自定义文案 contentID 数组（非全场景下必传），contentID 在后台申请开通直玩能力后可获取 |
| allScene | boolean | 否 | false | 3.45.0 | 是否为全场景订阅 |
| type | number | 是 |  | 3.34.0 | 订阅 Feed 流的类型，目前只支持传 'play'  **可选值：** play=

直玩场景

 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："requestFeedSubscribe:ok" - **success**（boolean）：用户的订阅结果（true 为成功，false 为订阅失败，具体原因看 errMsg） |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："requestFeedSubscribe:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10301 | feature is not supported in app |  |  |
| 21100 | host does not have permission |  |  |
| 21101 | no permission |  |  |
| 10601 | not login |  |  |
| 20001 | params contentIDs or scene is required |  |  |
| 21102 | network error |  |  |
| 21103 | service error:具体错误信息 |  |  |
| 21104 | internal error:具体错误信息 |  |  |
| 21105 | frequency control |  |  |
| 21500 | must be invoked by user gesture | 在 tt.touchEnd 回调内调用该接口 | 3.45.0 |

## 使用限制
1. 直玩能力只支持抖音平台。
2. 必须在调用 [tt.login](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/log-in/tt-login) 后才能调用本接口。
3. 本接口存在频控限制，需要注意调用场景和频率。
4. 全场景订阅（allScene 为 true）必须要由用户点击触发，也就是只能在 [tt.onTouchEnd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/click-event/tt-on-touch-end/) 的回调里面同步调用该 API。

## 前置条件
已申请开通小游戏直玩能力，在申请开通后可以获得 contentID

## 背景
1. 游戏供给更加偏向中重度，因此以游戏内的「关键节点」为高价值信息牵引用户复访成为效率更高的一种手段；
2. 业务侧期望，发挥小游戏的即点即玩特性，且整体无限贴合抖音：刷、推信息本身的体验，尝试为用户提供一种新型的小游戏游玩体验；

## 相关课程
[推荐流直出游戏能力接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/feed/minigame-feedpush-setting-guide)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/tt-request-feed-subscribe) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-request-feed-subscribe%22%7D)