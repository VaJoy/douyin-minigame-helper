---
title: "tt.onMessage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/open-data-area/tt-on-message
update_time: 2025-10-10
---

## 语法

```js
tt.onMessage(callback)
```
基础库 1.11.0 开始支持本方法，这是一个**同步**方法。
在开放数据域中调用，监听主域发送的消息。

## 示例代码
```js
tt.onMessage(function (message) {
  console.log("接受到消息");
  console.log(message);
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.11.0 | 监听到主域发送消息时触发的回调函数  **对象字段** - **params**（Object）：通过 [tt.getOpenDataContext().postMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data-area/tt-get-open-data-context/) 方法发送的消息对象 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-capacity/relationship-chain/open-data-area/tt-on-message) / [本地体验路径](tt-on-message)
