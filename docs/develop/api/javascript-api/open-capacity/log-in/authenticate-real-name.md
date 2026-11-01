---
title: "tt.authenticateRealName"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/log-in/authenticate-real-name
update_time: 2024-08-19
---

基础库 1.80.0 开始支持本方法，这是一个**异步**方法。
拉起实名认证窗口。

## 示例代码
```js
tt.login({
  force: true,
  success() {
    console.log("登录成功");
    //实名认证需要用户点击触发
    tt.onTouchEnd(realNameAuth);
  },
});

function realNameAuth() {
  tt.authenticateRealName({
    success(_res) {
      console.log("用户实名认证成功");
    },
    fail(res) {
      console.log("用户实名认证失败", res.errMsg);
    },
  });
}
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："authenticateRealName:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："authenticateRealName:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10402 | empty aid or appId |  |  |
| 21100 | no user login |  |  |
| 21101 | user reject |  |  |
| 21102 | no user tap action |  |  |
| 21110 | network error |  |  |
| 21103 | user already verified |  |  |
| 21111 | real name auth service fail %s |  |  |
| 21120 | internal error |  |  |
| 21112 | real name auth data invalid |  |  |
| 20000 | internal error |  |  |
| 21000 | no platform support |  |  |
| 10601 | not login |  |  |
| 10401 | Internal error: service error xxx(serverCode) identity |  |  |
| 10103 | network unavailable |  |  |
| 10401 | internal error |  |  |

## 注意事项
当前用户是否已经实名认证可以通过 [tt.getUserInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/info/tt-get-user-info) 查询

## 前置条件
调用该接口前请确保用户已登录。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-capacity/user-information/info/authenticate-real-name) / [本地体验路径](tt-authenticate-real-name)
