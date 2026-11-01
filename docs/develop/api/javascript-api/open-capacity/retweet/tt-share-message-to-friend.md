---
title: "tt.shareMessageToFriend"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/retweet/tt-share-message-to-friend
update_time: 2024-08-29
---

## 语法

```js
tt.shareMessageToFriend(query, openId, templateId)
```
基础库 2.74.0 开始支持本方法，这是一个**异步**方法。
给指定的好友分享游戏信息。

## 示例代码
```js
let queryObj = {
    'key1': 'value1',
    'key2': 'value2',
};

tt.shareMessageToFriend({
    openId: 'xxxxx',
    templateId: 'xxxxxx',
    query: JSON.stringify(queryObj),
    success(res) {
        console.log('success');
    },
    fail(res) {
        console.log('fail', res);
    },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| query | string | 否 |  | 2.74.0 | 查询字符串，格式为JSONString。从这条转发消息进入后，可通过 [tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-get-launch-options-sync/) 或 [tt.onShow](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-on-show/) 获取启动参数中的 query 用来实现信息透传 |
| openId | string | 是 |  | 2.74.0 | 发送对象的 openId |
| templateId | string | 是 |  | 2.74.0 | 分享素材模板 id，指定通过平台审核的 templateId 来选择分享内容，需在平台设置且通过审核 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："shareMessageToFriend:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："shareMessageToFriend:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 0 | get game user info error |  |  |
| 0 | get share info error |  |  |
| 10502 | cancel |  |  |
| 20001 | invalid param |  |  |
| 20000 | frequency_control |  |  |
| 21500 | get game user info catch error |  |  |
| 21500 | get share info catch error${JSON.stringify(error)} |  |  |
| 10301 | feature is not supported in app |  |  |
| 21101 | sendMessage is in progress, please do not call again |  |  |
| 21000 | container not exist |  |  |
| 21000 | no openID |  |  |
| 21000 | query error |  |  |
| 21000 | schema error |  |  |
| 21000 | query conent error |  |  |
| 21000 | sec_uid not exist |  |  |
| 21000 | get target uid failed |  |  |
| 21000 | sendMessage failed |  |  |
| 20000 | internal error |  |  |
| 10601 | shareMessageToFriend |  |  |
| 21000 | sendGameInviteMessage failed |  |  |
| 10402 | native exception |  |  |
| 20000 | share info entity error |  |  |
| 20000 | game user info entity error |  |  |

## 使用限制
目前仅支持 抖音、抖音极速版 APP

## 注意事项
- **注意游戏场景，不要过度频繁引导分享：**定向分享需要与游戏场景强相关，建议结合游戏内的好友系统、互动系统，会起到事半功倍的效果
- 配合“邀请有奖”或“礼物赠送”等功能模式，可以更大程度激发用户的分享意愿（具体实现：通过定向分享能力，入参中传入分享者的 openid（query 字段），并结合 [tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-get-launch-options-sync/) 或 [tt.onShow](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-on-show/) 获取启动参数中的 query 来判断是否通过分享链接启动的，并给分享人发放对应的奖励）

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
