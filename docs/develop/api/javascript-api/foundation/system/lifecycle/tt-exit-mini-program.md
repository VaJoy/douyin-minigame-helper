---
title: "tt.exitMiniProgram"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/lifecycle/tt-exit-mini-program
update_time: 2024-07-24
---

## 语法

```js
tt.exitMiniProgram(isFullExit)
```
基础库 1.12.0 开始支持本方法，这是一个**异步**方法。
退出当前小游戏到后台。

## 示例代码
```js
tt.exitMiniProgram({
  success(res) {
    console.log("调用成功", res.data);
  },
  fail(res) {
    console.log("调用失败", res.errMsg);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| isFullExit | boolean | 否 | false | 1.12.0 | 是否完全关闭小游戏，当该值为 true 时，会完全关闭小游戏，下次打开将重新进入 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："exitMiniProgram:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："exitMiniProgram:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 注意事项
- 调用该方法的预期表现会将小游戏切后台，并不会完全退出小游戏（在 IDE 预览版本表现可能会不一致）。
- 正常调用 exitMiniProgram 退出小游戏时，小游戏实际行为和切后台一致，并不会完全关闭小游戏，再次打开小游戏将立即返回之前的状态。在传入 isFullExit 时，将完全关闭小游戏，下次打开会重新加载打开小游戏。
- isFullExit 为 true 会导致下次打开小游戏的时间变长。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/system/lifecycle/tt-exit-mini-program) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-exit-mini-program%22%7D)
