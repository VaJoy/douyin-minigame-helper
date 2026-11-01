---
title: "tt.checkShortcut"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/shortcut/check-shortcut
update_time: 2024-07-24
---

基础库 2.46.0 开始支持本方法，这是一个**异步**方法。
检查小游戏快捷方式是否已添加到手机桌面上。

## 示例代码
```js
tt.checkShortcut({
  success(res) {
    console.log("检查快捷方式", res.status);
  },
  fail(res) {
    console.log("检查快捷方式失败", res.errMsg);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **status**（Object）：桌面快捷方式状态 - **errMsg**（string）："checkShortcut:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："checkShortcut:fail " + 错误详情 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10301 | feature is not supported in app |  |  |
| 21101 | check shortcut fail |  |  |
| 20000 | internal error |  |  |
| 10402 | context environment error |  |  |

## 使用限制
仅在Android上支持

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/shortcut) / [本地体验路径](tt-add-shortcut)
