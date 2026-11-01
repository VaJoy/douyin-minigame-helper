---
title: "tt.addShortcut"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/shortcut/add-shortcut
update_time: 2025-10-20
---

基础库 2.46.0 开始支持本方法，这是一个**异步**方法。
可以将小游戏快捷方式添加到手机桌面上。

## 示例代码
```js
tt.addShortcut({
  success() {
    console.log("添加桌面成功");
  },
  fail(err) {
    console.log("添加桌面失败", err.errMsg);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："addShortcut:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："addShortcut:fail " + 错误详情 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10301 | feature is not supported in app |  |  |
| 21301 | system auth deny |  |  |
| 21302 | get results timed out |  |  |
| 21304 | update deny |  |  |
| 21303 | add shortcut fail |  |  |
| 21305 | user cancel |  |  |
| 20000 | internal error |  |  |
| 21500 | must be invoked by user gesture |  |  |

## 使用限制
目前仅支持抖音，抖音极速版和抖音火山，请在其它 app 做屏蔽。

## 注意事项
该 API 必须要由用户点击触发，也就是只能在tt.onTouchEnd的回调里面同步调用该 API。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/shortcut) / [本地体验路径](tt-add-shortcut)
