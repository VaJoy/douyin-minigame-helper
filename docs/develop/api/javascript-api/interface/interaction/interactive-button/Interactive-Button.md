---
title: "InteractiveButton"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/interaction/interactive-button/Interactive-Button
update_time: 2024-07-24
---

> 基础库 2.46.0 开始支持
该方法创建一个 Native 按钮，位于小游戏层级最上面，覆盖在小游戏 Canvas 画布上。通过该方法创建的按钮在录屏时，不会被采集进录屏画面。开发者可以通过创建此类按钮，优化录屏效果，减少录屏画面的元素内容
## 属性
**buttonid**
按钮的唯一 ID， 用来区别多个 button 的场景
## 方法
显示交互按钮
**InteractiveButton.show()**
隐藏交互按钮
**InteractiveButton.hide()**
销毁按钮
**InteractiveButton.destroy()**
注册点击事件的回调函数
**InteractiveButton.onTap(callback)**
注销点击事件的回调函数
**InteractiveButton.offTap(callback)**
##
