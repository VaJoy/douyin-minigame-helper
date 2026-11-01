---
title: "tt.offKeyboardInput"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/keyboard/tt-off-keyboard-input
update_time: 2024-07-24
---

## 语法

```js
tt.offKeyboardInput(handler)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
取消监听键盘输入事件。

## 示例代码
```js
function handler(data) {
  console.log(data.value);
}

tt.onKeyboardInput(handler);
tt.offKeyboardInput(handler);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| handler | Function | 是 |  | 1.0.0 | 通过[tt.onKeyboardInput](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/keyboard/tt-on-keyboard-input)监听键盘收起事件的函数 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/keyboard/tt-off-keyboard-input) / [本地体验路径](tt-off-keyboard-input)
