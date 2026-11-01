---
title: "tt.onHide"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/lifecycle/tt-on-hide
update_time: 2024-07-24
---

## 语法

```js
tt.onHide(cb)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
监听小游戏隐藏到后台的事件。锁屏、按 HOME 键退到桌面等操作会触发此事件。

## 示例代码
```js
tt.onHide(() => {
  console.log("小游戏隐藏");
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| cb | Function | 是 |  | 1.0.0 | 小游戏隐藏到后台的事件回调。该回调函数没有参数。 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/system/lifecycle/tt-on-hide) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-on-hide%22%7D)
