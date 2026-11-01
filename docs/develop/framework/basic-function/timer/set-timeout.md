---
title: "setTimeout"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/basic-function/timer/set-timeout
update_time: 2024-08-21
---

## 语法

```js
setTimeout(callback, delay, arg1,arg2,...,argN)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
设置一个定时器，在一定延时后触发回调函数。

## 示例代码
```js
var timer = setTimeout(() => {
  console.log("hello");
}, 10000);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.0.0 | 回调函数 |
| delay | number | 否 | 0 | 1.0.0 | 延时时间，回调函数会在该延时后执行，单位 ms |
| arg1,arg2,...,argN | Promise | 否 |  | 1.0.0 | 附加参数，它们会作为参数传递给回调函数 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| timerID | number | 定时器 ID，这个值可以传给 [clearTimeout](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/timer/clear-timeout/) 取消定时器。 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/framework/basic-function/timer/setTimeout) / [本地体验路径](setTimeout)
