---
title: "tt.getClipboardData"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/pasting-board/tt-get-clipboard-data
update_time: 2024-07-24
---

基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
获取系统剪贴板内容。

## 示例代码
```js
tt.getClipboardData({
  success(res) {
    console.log(`${res.data}`);
  },
  fail(res) {
    console.log(`getClipboardData调用失败`);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **data**（string）：剪贴板的内容 - **errMsg**（string）："getClipboardData:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getClipboardData:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21000 | get clipboard failed |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/pasting-board/tt-get-clipboard-data) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-get-clipboard-data%22%7D)
