---
title: "tt.requestPointerLock"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/drawing/cursor-style/tt-request-pointer-lock
update_time: 2025-01-03
---

基础库 3.54.0 开始支持本方法，这是一个**同步**方法。
锁定鼠标指针，锁定后隐藏鼠标

## 示例代码
```js
tt.onTouchEnd(() => {
    tt.requestPointerLock();
})
```

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 999976 | must be invoked by user tap gesture |  |  |
| 999988 | The feature is not available in current operating system |  |  |

## 使用限制
仅适用于 PC 平台，且需要在用户点击的回调([tt.onTouchEnd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/click-event/tt-on-touch-end))内才能使用该能力

## 相关课程
[PC 端小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/tutorial)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/cursor) / [本地体验路径](tt-cursor)
