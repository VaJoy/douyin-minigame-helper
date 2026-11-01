---
title: "InteractiveButton.show"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/interaction/interactive-button/Interactive-button-show
update_time: 2024-11-27
---

基础库 2.46.0 开始支持本方法，这是一个**异步**方法。
显示按钮。

## 示例代码
点击按钮隐藏，2s 后重新展示
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

      // 隐藏按钮后2s重新展示
      setTimeout(() => {
        button.show();
      });
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
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/interface/interaction/interactive-button/Interactive-button-destroy) / [本地体验路径](tt-create-interactive-button)
