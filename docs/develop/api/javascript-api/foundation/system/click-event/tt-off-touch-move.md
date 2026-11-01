---
title: "tt.offTouchMove"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/click-event/tt-off-touch-move
update_time: 2025-10-10
---

## 语法

```js
tt.offTouchMove(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
取消监听触点移动事件。

## 示例代码
```js
function touchCallback({
  touches,
  changedTouches,
  timeStamp
}) {
  console.log('触点移动回调', touches, changedTouches, timeStamp)
};

tt.onTouchMove(touchCallback);
tt.offTouchMove(touchCallback);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 1.0.0 | 监听事件的回调函数  **对象字段** - **TouchData**（Object）：callback回调接收参数对象 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/system/system-information/tt-off-touch-move) / [本地体验路径](tt-off-touch-move)
