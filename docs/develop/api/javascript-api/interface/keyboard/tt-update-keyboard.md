---
title: "tt.updateKeyboard"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/keyboard/tt-update-keyboard
update_time: 2024-08-29
---

## 语法

```js
tt.updateKeyboard(value)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
更新键盘，只有当键盘处于拉起状态时才会产生效果。

## 示例代码
```js
tt.showKeyboard({
  defaultValue: "hello world",
  maxLength: 200,
  multiple: false,
  confirmHold: true,
  confirmType: "done",
  success: () => {
    setTimeout(() => {
      tt.updateKeyboard({
        value: "keyboard updated", // 键盘输入框的当前值
      });
    }, 2000);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| value | string | 是 |  | 1.0.0 | 键盘输入框的当前值 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："updateKeyboard:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："updateKeyboard:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10401 | internal error |  |  |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/interface/keyboard/tt-update-keyboard) / [本地体验路径](tt-update-keyboard) / [在线试玩](https://developer.open-douyin.com/docs/playground?project_id=tma-demo&version=1.0.0.10&entry=tt-update-keyboard&codes_select=js&type=mini-game&sdk_version=1.0.0.205)
