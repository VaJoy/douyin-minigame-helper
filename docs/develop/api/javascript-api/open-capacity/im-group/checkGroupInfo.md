---
title: "tt.checkGroupInfo"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/im-group/checkGroupInfo
update_time: 2024-08-29
---

## 语法

```js
tt.checkGroupInfo(extraInfo, openid, sessionFrom)
```
基础库 2.70.0 开始支持本方法，这是一个**异步**方法。
查询用户通过小游戏平台创建的群的信息
如游戏开发者在平台创建了群聊 ABC，那么游戏侧可以基于游戏开发者在这个游戏中的 openid，查询其在小游戏平台创建了哪些群，群的状态如何，做游戏内的加群逻辑优化

## 示例代码
```js
tt.checkGroupInfo({
  openid: "openid",
  success(res) {
    console.log(res);
  },
  fail(res) {
    console.log(res);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| extraInfo | string | 否 |  | 2.70.0 | 预留字段 |
| openid | string | 是 |  | 2.70.0 | 建群用户的 openid。通过 [tt.login](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/log-in/tt-login/) 接口获取到登录凭证后，开发者可以通过服务器发送请求的方式获取 openid。详情参考 [code2Session](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/log-in/code-2-session) |
| sessionFrom | string | 否 |  | 2.70.0 | 预留字段 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **data**（Object）：查询返回的数据 - **errMsg**（string）："checkGroupInfo:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："checkGroupInfo:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21000 | user not authorized to app |  |  |
| 21002 | service unavailable |  |  |
| 21003 | internal error |  |  |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |
| 10301 | feature is not supported in app |  |  |
| 20000 | openid is nil. |  |  |
| 21000 | user login failed |  |  |
| 21004 | The user has not completed real-name authentication in app |  |  |
| 0 | auth alert view is showing.. |  |  |

## 使用限制
目前仅支持抖音，可以使用 [getSystemInfoSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/system-information/tt-get-system-info-sync) 判断宿主

## 注意事项
查询到的群列表只局限在通过游戏创建的群聊或开发者在平台创建的群聊，其他渠道创建的群聊不会返回

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
