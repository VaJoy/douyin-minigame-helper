---
title: "InteractiveButton.offTap"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/interaction/interactive-button/interactive-button-offtap
update_time: 2024-12-10
---

## 语法

```js
InteractiveButton.offTap(callback)
```
基础库 2.46.0 开始支持本方法，这是一个**同步**方法。
注销按钮点击回调事件。

## 示例代码
点击按钮后解绑事件
```js
let params = {
  type: "text",
  text: "text button",
  style: {},
  success(button) {
    function button_tap(res) {
      console.log(res.buttonid);
      button.offTap(button_tap);
    }
    button.onTap(button_tap);
  },
  fail(res) { },
};
tt.createInteractiveButton(params);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 2.46.0 | 监听事件的回调函数 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/interface/interaction/interactive-button/tt-create-interactive-button) / [本地体验路径](tt-create-interactive-button)
