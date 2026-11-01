---
title: "tt.showKeyboard"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/keyboard/tt-show-keyboard
update_time: 2024-07-24
---

## 语法

```js
tt.showKeyboard(maxLength, defaultValue, multiple, confirmHold, confirmType)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
显示软键盘。

## 示例代码
```js
tt.showKeyboard({
  defaultValue: "hello world", // 键盘输入框显示的默认值
  maxLength: 20, // 键盘中文本的最大长度
  multiple: true, // 是否为多行输入
  confirmHold: true, // 当点击完成时保持键盘不收起
  confirmType: "done", // 键盘右下角 confirm 按钮的类型
  success: (res) => console.log(res),
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| maxLength | number | 是 |  | 1.0.0 | 键盘中文本的最大长度 |
| defaultValue | string | 是 |  | 1.0.0 | 键盘输入框显示的默认值 |
| multiple | boolean | 是 |  | 1.0.0 | 是否为多行输入 |
| confirmHold | boolean | 是 |  | 1.0.0 | 当点击完成时键盘是否收起。 true 为点击完成后保持键盘为不收起的状态， false 为点击完成后收起键盘 |
| confirmType | number | 是 |  | 1.0.0 | 键盘右下角 confirm 按钮的类型，只影响按钮的文本内容  **可选值：** search=

搜索

；done=

完成

；next=

下一个

；go=

前往

；send=

发送

 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："showKeyboard:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："showKeyboard:fail" + 报错信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10401 | internal error |  |  |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |

## 注意事项
- 请在用户完整输入信息后（比如昵称起名环节），使用[tt.onKeyboardConfirm](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/keyboard/tt-on-keyboard-confirm) 或者[tt.onKeyboardComplete](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/keyboard/tt-on-keyboard-complete) 接口来获取用户输入的信息，此时的信息经过平台敏感词检测，能够确保业务安全
- 该方法并不会返回用户输入，需要用[tt.onKeyboardInput](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/interface/keyboard/tt-on-keyboard-input/)监听用户输入。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/interface/keyboard/tt-show-keyboard) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-show-keyboard%22%7D) / [在线试玩](https://developer.open-douyin.com/docs/playground?project_id=tma-demo&version=1.0.0.10&entry=tt-show-keyboard&codes_select=js&type=mini-game&sdk_version=1.0.0.205)