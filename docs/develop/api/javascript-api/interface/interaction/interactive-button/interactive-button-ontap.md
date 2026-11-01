---
title: "InteractiveButton.onTap"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/interaction/interactive-button/interactive-button-ontap
update_time: 2024-11-27
---

> 基础库 2.46.0 开始支持本方法。
注册按钮点击回调事件
## 语法

```js
InteractiveButton.onTap(callback);
```

## 参数说明
### callback

| 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| Function |  | 是 | 监听事件的回调函数 | 2.46.0 |

#### 回调函数参数说明
object 类型，属性如下:

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| buttonid | string | 表示按钮的唯一 ID， 用来区别多个 button 的场景 | 2.46.0 |

## 扫码体验

## 代码示例

```js
let params = {
  type: "text",
  text: "text button",
  style: {},
  success(button) {
    function button_tap(res) {
      console.log(res.buttonid);
    }
    button.onTap(button_tap);
  },
  fail(res) {},
};
tt.createInteractiveButton(params);
```

## Bug & Tip
无
