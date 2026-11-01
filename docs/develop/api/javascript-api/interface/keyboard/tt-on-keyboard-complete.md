---
title: "tt.onKeyboardComplete"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/keyboard/tt-on-keyboard-complete
update_time: 2024-07-24
---

## 语法

```js
tt.onKeyboardComplete(handler)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
监听键盘收起的事件，使用 tt.onKeyboardConfirm 或者 tt.onKeyboardComplete 接口获得的用户输入值，平台会自动进行敏感词检测，将敏感字眼做屏蔽。

## 示例代码
```js
tt.onKeyboardComplete((data) => {
    console.log('键盘输入的当前值', data.value);
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| handler | Function | 是 |  | 1.0.0 | 键盘收起事件的回调函数  **对象字段** - **args_0**（Object）：回调参数 |

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
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/interface/keyboard/tt-on-keyboard-complete) / [本地体验路径](tt-on-keyboard-complete)
