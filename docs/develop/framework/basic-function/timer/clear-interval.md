---
title: "clearInterval"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/basic-function/timer/clear-interval
update_time: 2024-08-21
---

## 语法

```js
clearInterval(timerID)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
清除一个定时器。

## 示例代码
```js
const timer = setInterval(() => {
  console.log("hello");
}, 1000);

clearInterval(timer);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| timerID | number | 是 |  | 1.0.0 | 使用 [setInterval](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/timer/clear-timeout) 生成的 ID |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/framework/basic-function/timer/clearInterval) / [本地体验路径](clearInterval)
