---
title: "tt.login"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/log-in/tt-login
update_time: 2025-11-24
---

## 语法

```js
tt.login(force)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
调用该 API 可以获取用户临时的登录凭证。

## 示例代码
```js
tt.login({
  force: true,
  success(res) {
    console.log(`login 调用成功${res.code} ${res.anonymousCode}`);
  },
  fail(res) {
    console.log(`login 调用失败`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| force | boolean | 否 | true | 1.0.0 | 未登录时, 是否强制调起登录框 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **anonymousCode**（string）：用于标识当前设备, 无论登录与否都会返回, 有效期 3 分钟。 - **isLogin**（boolean）：判断在当前 APP（头条、抖音等）是否处于登录状态。 - **code**（string）：临时登录凭证, 有效期 3 分钟。开发者可以通过在服务器端调用[登录凭证校验接口](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/log-in/code-2-session)换取 openid 和 session_key 等信息。 - **errMsg**（string）："login:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："login:fail " + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10401 | getHostSessionFail |  |  |
| 10501 | app in background |  |  |
| 10301 | feature is not supported in app |  |  |
| 20000 | internal error |  |  |
| 21101 | login is in progress, please do not call again |  |  |
| 10401 | Internal error: login failed |  |  |
| 10401 | Internal error: service error xxx |  |  |

## 注意事项
- force 为 true 时(默认值为 true), 如果用户未在端登录(例如未在头条 App 登录), 则会调起端的登录窗口, 如果用户点击取消则会调用 fail
- 只有端登录的用户 success 才有 code, 否则只有 anonymousCode
- code 可以换取 openid, openid 是用户的唯一标识
- anonymousCode 可以换取 anonymous_openid, 同一台手机 anonymous_openid 是相同

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-capacity/log-in/tt-login) / [本地体验路径](tt-login)
