---
title: "LiveManager.onInstantPlayStatusChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/live/live-manager/livemanager-on-instant-change
update_time: 2025-10-10
---

## 语法

```js
LiveManager.onInstantPlayStatusChange(callback)
```
基础库 3.85.0 开始支持本方法，这是一个**同步**方法。
注册即看即玩开关状态变化监听函数

## 示例代码
```js
const liveManager = tt.getLiveManager();

liveManager.onInstantPlayStatusChange((res) => {
    console.log('主播即玩开关发生变化:', res.instantPlayStatus)
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 3.85.0 | 主播即玩开关切换的回调事件  **对象字段** - **params**（Object）：回调参数 |

## 使用限制
仅在直播场景下可调用

## 前置条件
使用前，请先前往游戏开放后台，申请开通直播即看即玩能力

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
