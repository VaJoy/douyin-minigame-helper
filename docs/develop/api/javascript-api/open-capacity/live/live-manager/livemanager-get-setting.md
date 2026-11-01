---
title: "LiveManager.getLiveSetting"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/live/live-manager/livemanager-get-setting
update_time: 2025-10-10
---

基础库 3.85.0 开始支持本方法，这是一个**异步**方法。
获取直播环境配置信息。

## 示例代码
```js
const liveManager = tt.getLiveManager();

liveManager.getLiveSetting({
    success: (res) => {
        console.log('success', res);
    },
    fail: (res) => {
        console.log('fail', res);
    }
})
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："LiveManager.getLiveSetting:ok" - **isVideoLive**（boolean）：当前是否为直播场景 - **isAnchor**（boolean）：当前玩家身份是否是主播 - **instantPlay**（boolean）：是否开通即看即玩能力并且主播端开关已打开 |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："LiveManager.getLiveSetting:fail" + 详细错误信息 |

## 相关课程
[直播即看即玩能力技术指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/instant-play-introduce)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
