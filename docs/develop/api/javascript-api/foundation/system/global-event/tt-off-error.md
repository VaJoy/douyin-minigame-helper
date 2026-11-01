---
title: "tt.offError"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/global-event/tt-off-error
update_time: 2024-08-29
---

## 语法

```js
tt.offError(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
取消监听全局错误事件。

## 示例代码
```js
function errorCallback({ message, stack }) {
  console.log('catch error', message, stack)
}

tt.onError(errorCallback);
tt.offError(errorCallback);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.0.0 | 通过 [tt.onError](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/global-event/tt-on-error) 注册的事件回调 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/interface/keyboard/tt-on-error) / [本地体验路径](tt-on-error)
