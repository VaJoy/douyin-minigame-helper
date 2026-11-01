---
title: "tt.createInteractiveButton"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/interaction/interactive-button/create-interactive-button
update_time: 2024-11-27
---

## 语法

```js
tt.createInteractiveButton(image, text, type, style)
```
基础库 2.46.0 开始支持本方法，这是一个**异步**方法。
该方法创建一个 Native 按钮，位于小游戏层级最上面，覆盖在小游戏 Canvas 画布上。通过该方法创建的按钮在录屏时，不会被采集进录屏画面。开发者可以通过创建此类按钮，优化录屏效果，减少录屏画面的元素内容。

## 示例代码
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
      // button.hide();
      // button.offTap(button_tap);
      // button.destroy();
    }
    button.onTap(button_tap);
  },
  fail(res) {
    console.log("创建失败", res.errMsg);
  },
};
tt.createInteractiveButton(params);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| image | string | 否 |  | 2.46.0 | 按钮上显示图片的路径， 可以接受网络地址，本地 ttfile:// 协议地址，以及相对路径。按钮类型为 image ，该字段必填 |
| text | string | 否 |  | 2.46.0 | 按钮上显示的文本。按钮类型为 text，这个字段必须填 |
| type | string | 是 |  | 2.46.0 | 按钮类型：text 、image |
| style | Object | 是 |  | 2.46.0 | 设置按钮的大小，位置，字体，颜色等属性  **对象字段** - **width**（number）：宽度 - **height**（number）：高度 - **top**（number）：y 轴坐标 - **left**（number）：x 轴坐标 - **fontSize**（number）：字体大小 - **backgroundColor**（string）：背景颜色 - **borderColor**（string）：边框颜色 - **borderWidth**（number）：边框宽度 - **textAlign**（string）：文本对齐方式：left，center 和 right - **textColor**（string）：字体颜色 - **lineHeight**（number）：多行文本的间距 - **borderRadius**（number）：边框圆角 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| InteractiveButton | Object | [InteractiveButton](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/interaction/interactive-button/Interactive-Button/) 类型 |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："createInteractiveButton:fail" + 详细错误信息 |

## 注意事项
按钮不使用时，务必调用 destroy() 释放资源，destroy() 会自动移除监听事件

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/interface/interaction/interactive-button/tt-create-interactive-button) / [本地体验路径](tt-create-interactive-button)
