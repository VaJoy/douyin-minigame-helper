---
title: "tt.joinGroup"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/im-group/joinGroup
update_time: 2024-07-24
---

## 语法

```js
tt.joinGroup(extraInfo, groupid)
```
基础库 2.70.0 开始支持本方法，这是一个**异步**方法。
在平台创建群聊，获得 groupid 后，游戏内通过这个方法引导用户加入抖音群

## 示例代码
```js
tt.joinGroup({
    groupid: "998877", //加入的群id，可在平台创建群聊后获得
    sessionFrom: "sessionFrom",
    extraInfo: "extraInfo",
    success(res) {
        console.log(res);
    },
    fail(res) {
        console.log(res);
    }
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| extraInfo | string | 否 |  | 2.70.0 | 附加信息 |
| groupid | string | 是 |  | 2.70.0 | 群 ID |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **data**（Object）：加群信息 - **errMsg**（string）："joinGroup:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："joinGroup:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21000 | the group is not authorized to the app |  |  |
| 21001 | internal error |  |  |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |
| 10301 | feature is not supported in app |  |  |
| 20000 | groupid is nil. |  |  |
| 21000 | user login failed |  |  |
| 21003 | internal error. |  |  |

## 使用限制
- 目前仅支持抖音及抖音极速版
- **该 API 必须要由用户点击触发，只能在 tt.onTouchEnd 的回调里面同步调用该 API**

## 前置条件
使用本 API 前需要先在开发者平台创建群聊获取 groupid。具体可参考[游戏群聊能力接入介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/im-group/groupchatintroduce)

1. 前往开发者平台，「运营 - 运营能力 - 粉丝群能力 」，申请开通能力
2. 扫码绑定抖音号后，点击「新建群聊」以获得对应的群 ID

## 相关课程
[游戏群聊能力接入介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/im-group/groupchatintroduce)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/im-group/tt-join-group) / [本地体验路径](tt-join-group)
