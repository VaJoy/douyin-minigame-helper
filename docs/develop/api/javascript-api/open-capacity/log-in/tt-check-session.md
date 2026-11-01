---
title: "tt.checkSession"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/log-in/tt-check-session
update_time: 2025-11-24
---

基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
用户的登录态具有时效性，随着用户未使用小游戏的时间增加，用户的登录态越容易失效；反之，则用户登录态可持续保持有效。使用该 API 可检查用户当前的 session 状态是否有效，登录态过期后开发者可以再调用 [tt.login](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/log-in/tt-login) 获取新的用户登录态。

## 示例代码
```js
tt.checkSession({
  success() {
    console.log(`session 未过期`);
  },
  fail() {
    console.log(`session 已过期，需要重新登录`);
    tt.login({
      success: (res) => {
        console.log("登录成功", res);
      },
      fail: (err) => {
        console.log("登录失败", err);
      },
    });
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下  **对象字段** - **errMsg**（string）："checkSession:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下  **对象字段** - **errMsg**（string）："checkSession:fail " + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21101 | session is empty |  |  |
| 21102 | session is expired |  |  |
| 21100 | no valid session |  |  |
| 10403 | unknown error |  |  |
| 20000 | internal error |  |  |
| 21000 | session is empty |  |  |
| 21000 | session is expired |  |  |

## 注意事项
只有成功调用 [tt.login](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/open-interface/log-in/tt-login/) 才会生成 session，tt.checkSession 也会因此进入 success 回调，当用户退出登录会清除 session

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-capacity/log-in/tt-check-session) / [本地体验路径](tt-check-session)
