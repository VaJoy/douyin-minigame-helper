---
title: "tt.setClipboardData"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/pasting-board/tt-set-clipboard-data
update_time: 2024-07-24
---

## 语法

```js
tt.setClipboardData(data)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
设置系统剪贴板内容。可以和[tt.getClipboardData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/pasting-board/tt-get-clipboard-data)配套使用。

## 示例代码
```js
tt.setClipboardData({
  data: "hello kitty",
  success(res) {
    console.log(`setClipboardData调用成功`);
  },
  fail(res) {
    console.log(`setClipboardData调用失败`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| data | string | 是 |  | 1.0.0 | 剪贴板的内容 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："setClipboardData:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："setClipboardData:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21000 | set clipboard failed |  |  |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/pasting-board/tt-set-clipboard-data) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-set-clipboard-data%22%7D)
