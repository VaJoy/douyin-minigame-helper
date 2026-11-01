---
title: "LiveManager.offXScreenSizeChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/live/live-manager/off-x-screen-change
update_time: 2025-02-18
---

## 语法

```js
LiveManager.offXScreenSizeChange(callback)
```
基础库 3.60.0 开始支持本方法，这是一个**同步**方法。
取消监听X分屏全屏/半屏切换事件

## 示例代码
```js
const liveManager = tt.getLiveManager();

function screenChangeCallback({ type }) {
    console.log('监听到X分屏变化，变化事件为:', res.type)
}
// 开始监听
liveManager.onXScreenSizeChange(screenChangeCallback);

// 取消监听
liveManager.offXScreenSizeChange(screenChangeCallback);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 3.60.0 | 取消监听X分屏变化的监听事件。不传时，将取消所有的监听事件 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
