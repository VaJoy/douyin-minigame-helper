---
title: "tt.onFeedStatusChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/feed-subscribe/tt-feed-status-change
update_time: 2025-02-14
---

## 语法

```js
tt.onFeedStatusChange(callback)
```
基础库 3.59.0 开始支持本方法，这是一个**同步**方法。
监听 Feed 流进入/退出小游戏事件。

## 示例代码
```js
tt.onFeedStatusChange(({ type }) => {
    if (type === 'feedEnter') {
        console.log('触发从Feed流进入小游戏事件回调')
    }

    if (type === 'feedExit') {
        console.log('触发从小游戏退回到Feed流事件回调')
    }
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 3.59.0 | 直玩场景内外流切换的事件回调  **对象字段** - **params**（Object）：回调参数 |

## 使用限制
使用场景仅限推荐流直玩游戏场景，只支持抖音平台

## 相关课程
[推荐流直出小游戏能力接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/minigame-feedpush-setting-guide)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
