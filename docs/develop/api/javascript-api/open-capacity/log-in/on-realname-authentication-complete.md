---
title: "tt.onRealNameAuthenticationComplete"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/log-in/on-realname-authentication-complete
update_time: 2024-08-21
---

## 语法

```js
tt.onRealNameAuthenticationComplete(callback)
```
基础库 2.25.0 开始支持本方法，这是一个**同步**方法。
监听实名认证成功，在用户未实名的情况下，打开游戏后会主动弹出实名认证弹框，用户完成认证后会回调该方法。

## 示例代码
```js
//监听实名认证完成

tt.onRealNameAuthenticationComplete(function (obj) {
  console.log("实名认证完成回调 ", obj.state);
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 2.25.0 | 监听实名认证完成的回调  **对象字段** - **args_0**（Object）：object类型，属性如下： |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-seek) / [本地体验路径](tt-on-real-name-authentication-complete)
