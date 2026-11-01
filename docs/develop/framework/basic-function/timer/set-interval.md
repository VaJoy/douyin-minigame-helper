---
title: "setInterval"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/basic-function/timer/set-interval
update_time: 2024-08-21
---

## 语法

```js
setInterval(callback, interval, arg1,arg2,...,argN)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
设定一个定时器。按照指定的周期（以毫秒计）来执行注册的回调函数。

## 示例代码
```js
const timer = setInterval(() => {
  console.log("hello");
}, 1000);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.0.0 | 回调函数 |
| interval | number | 否 | 0 | 1.0.0 | 每隔一段时间执行回调函数，单位 ms |
| arg1,arg2,...,argN | Promise | 否 |  | 1.0.0 | 附加参数，它们将作为参数传递给回调函数 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| timerID | number | 返回值 timerId 是一个正整数，表示定时器 ID，这个值可以传给 [clearInterval](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/timer/clear-interval) 取消定时器 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/framework/basic-function/timer/setInterval) / [本地体验路径](setInterval)
