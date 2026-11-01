---
title: "tt.getUserInfo"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/log-in/tt-get-user-info
update_time: 2024-07-24
---

## 语法

```js
tt.getUserInfo(withCredentials, withRealNameAuthenticationInfo)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
获取已登录用户的基本信息或特殊信息，首次使用的用户会弹出授权提示窗，若用户同意，则会返回用户的真实数据。

## 示例代码
```js
tt.login({
  success(_res) {
    console.log("登录成功");
    // 调用 getUserInfo 前, 请确保登录成功

    // 获取用户信息
    tt.getUserInfo({
      // withCredentials: true,
      // withRealNameAuthenticationInfo: true,
      success(res) {
        console.log(`getUserInfo 调用成功`, res.userInfo, res.encryptedData, res.iv, res.signature);
      },
      fail(res) {
        console.log(`getUserInfo 调用失败`, res.errMsg);
      },
    });
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| withCredentials | boolean | 否 | false | 1.0.0 | 是否需要返回敏感数据，如果是则在成功回调的参数中额外返回 `encryptedData`，`signature` 和 `iv` 字段 |
| withRealNameAuthenticationInfo | boolean | 否 | false | 1.0.0 | 是否需要返回用户实名认证状态，如果是则在成功回调参数中额外返回 `realNameAuthenticationStatus` 字段 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **userInfo**（Object）：用户信息 - **rawData**（string）：userInfo 的 JSON 字符串形式 - **signature**（string）：用于校验用户信息是否被篡改，请参考[敏感数据处理](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/info/sensitive-data-process) 。仅在 `withCredentials: true` 时返回 - **encryptedData**（string）：包括敏感信息（如 openId）在内的已加密用户数据，如需解密数据请参考[敏感数据处理](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/info/sensitive-data-process)。仅在 `withCredentials: true` 时返回 - **iv**（string）：加密算法参数，仅在 `withCredentials: true` 时返回 - **realNameAuthenticationStatus**（number）：实名认证情况，仅在 `withRealNameAuthenticationInfo: true` 时返回 - **errMsg**（string）："getUserInfo:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getUserInfo:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 10301 | feature is not supported in app xxx |  |  |
| 10601 | not login |  |  |
| 10603 | invalid session |  |  |
| 10401 | Internal error: service error xxx identity |  |  |
| 10103 | network unavailable |  |  |

## 公告
**用户信息获取规则已调整，参考** [公告](https://developer.open-douyin.com/forum/mini-game/post/63354a56b1d3de363093289d)。

## 前置条件
- 本API依赖于[login](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/log-in/tt-login/)，请确保调用前已经调用了该API

## 用户授权说明
- 本API需要用户授权方可调用，详细信息可参考[用户授权](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/other/user-authorization/)

## 授权要求
无需开发者授权；需要用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-api/info/tt-get-user-info) / [本地体验路径](tt-get-user-info)
