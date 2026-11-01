---
title: "InteractiveButton.destroy"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/interaction/interactive-button/Interactive-button-destroy
update_time: 2024-12-10
---

基础库 2.46.0 开始支持本方法，这是一个**异步**方法。
销毁按钮，释放相关的资源。

## 示例代码
点击隐藏并销毁按钮
```js
let params = {
  type: "text",
  text: "text button",
  style: {
    left: 100,
    top: 100,
    width: 200,
    height: 20,
    textColor: "#111111",
  },
  success(button) {
    function button_tap(res) {
      logger.log("button_tap:" + res.buttonid);
      button.hide();
      // button.offTap(button_tap);
      button.destroy();
    }
    button.onTap(button_tap);
  },
  fail(res) {
    console.log("创建失败", res.errMsg);
  },
};
tt.createInteractiveButton(params);
```

## 回调：成功回调
调用成功时的回调函数

## 回调：失败回调
调用失败时的回调函数

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/interface/interaction/interactive-button/tt-create-interactive-button) / [本地体验路径](tt-create-interactive-button)
