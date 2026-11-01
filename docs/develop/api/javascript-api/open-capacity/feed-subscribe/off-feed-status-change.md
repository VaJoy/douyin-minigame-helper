---
title: "tt.offFeedStatusChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/feed-subscribe/off-feed-status-change
update_time: 2025-02-14
---

## 语法

```js
tt.offFeedStatusChange(callback)
```
基础库 3.59.0 开始支持本方法，这是一个**同步**方法。
取消监听 Feed 流进入/退出小游戏事件。

## 示例代码
```js
function feedChangeCallback({ type }) {
    console.log('feed流事件', type)
}
// 注册事件监听
tt.onFeedStatusChange(feedChangeCallback);
// 取消事件监听
tt.offFeedStatusChange(feedChangeCallback);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 3.59.0 | 取消监听直玩内外流切换的事件。不传时将取消所有事件监听 |

## 使用限制
使用场景仅限推荐流直玩场景，只支持抖音平台

## 相关课程
[推荐流直出小游戏能力接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/minigame-feedpush-setting-guide)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
