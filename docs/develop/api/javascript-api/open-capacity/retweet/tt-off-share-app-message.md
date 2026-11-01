---
title: "tt.offShareAppMessage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/retweet/tt-off-share-app-message
update_time: 2024-08-19
---

基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
取消监听用户点击右上角菜单的“转发”按钮时触发的事件。

## 示例代码
```js
function onShareAppMessage(res) {
  console.log(res);
}
// 监听菜单按钮“转发”
tt.onShareAppMessage(onShareAppMessage);

// 取消监听菜单按钮“转发”
setTimeout(() => {
  tt.offShareAppMessage(onShareAppMessage);
}, 2000);
```

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/retweet/tt-off-share-app-message) / [本地体验路径](tt-off-share-app-message)
