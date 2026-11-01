---
title: "tt.getMenuButtonLayout"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/menu/tt-get-menu-button-layout
update_time: 2024-07-24
---

基础库 1.25.0 开始支持本方法，这是一个**同步**方法。
获取菜单按钮（右上角胶囊按钮）的布局位置信息。坐标信息以屏幕左上角为原点。

## 示例代码
```js
let res = tt.getMenuButtonLayout();
console.log("宽度：" + res.width);
console.log("高度：" + res.height);
console.log("上边界坐标：" + res.top);
console.log("右边界坐标：" + res.right);
console.log("下边界坐标：" + res.bottom);
console.log("左边界坐标：" + res.left);
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | Object | 菜单按钮的布局位置信息  **对象字段** - **width**（number）：宽度，单位：dp - **height**（number）：高度，单位：dp - **top**（number）：上边界坐标，单位：dp - **bottom**（number）：下边界坐标，单位：dp - **right**（number）：右边界坐标，单位：dp - **left**（number）：左边界坐标，单位：dp |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/interface/menu/tt-get-menu-button-layout) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-get-menu-button-layout%22%7D)
