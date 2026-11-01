---
title: "tt.onKeyboardInput"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/keyboard/tt-on-keyboard-input
update_time: 2024-07-24
---

## 语法

```js
tt.onKeyboardInput(handler)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
监听键盘输入事件。

## 示例代码
```js
tt.onKeyboardInput(data => {
  console.log('键盘输入的当前值', data.value);
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| handler | Function | 是 |  | 1.0.0 | 监听键盘输入事件的回调函数  **对象字段** - **args_0**（Object）：回调参数 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |

## 注意事项
- 请在用户完整输入信息后（比如昵称起名环节），使用 [tt.onKeyboardConfirm](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/keyboard/tt-on-keyboard-confirm) 或者[tt.onKeyboardComplete](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/keyboard/tt-on-keyboard-complete) 接口来获取用户输入的信息，此时的信息经过平台敏感词检测，能够确保业务安全。仅使用 tt.onKeyboardInput 逐字获取输入信息，会导致敏感词检测的逻辑无法触发。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/interface/keyboard/tt-on-keyboard-input) / [本地体验路径](tt-on-keyboard-input)
