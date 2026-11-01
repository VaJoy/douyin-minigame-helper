---
title: "LiveManager.getLiveStatus"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/live/live-manager/live-manager-status
update_time: 2025-02-18
---

## 语法

```js
LiveManager.getLiveStatus(openIdList)
```
基础库 3.60.0 开始支持本方法，这是一个**异步**方法。
获取关联玩法的主播/直播间信息

## 示例代码
```js
const liveManager = tt.getLiveManager();

liveManager.getLiveStatus({
    openIdList: ['xxxx'], // 查询主播的openid
    success: (res) => {
        console.log('查询成功，直播间信息如下', res.liveStatus)
    },
    fail: (res) => {
        console.log('查询失败', res)
    },
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| openIdList | Array<string> | 是 |  | 3.60.0 | 要查询的主播 openId 列表 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| liveStatus | Object | 直播间信息。liveStatus为一个对象，key值是主播openId，value值为该主播直播间的查询信息  liveStatus 的 key 值是主播 openId，value 值为该主播直播间的查询信息，其属性如下：  \|  \|  \|  \|  \| \| --- \| --- \| --- \| --- \| \| **属性名** \| **类型** \| **说明** \| **最低支持版本** \| \| open_id \| string \| 主播 openid \| 3.60.0 \| \| is_on_live \| boolean \| 是否正在直播 \| 3.60.0 \| \| nickname \| string \| 主播昵称 \| 3.60.0 \| \| avatar_url \| string \| 头像 url \| 3.60.0 \| \| room_id \| string \| 直播间ID \| 3.60.0 \| \| app_id \| string \| 对应小玩法ID \| 3.60.0 \| |
| errMsg | string | "LiveManager.getLiveStatus:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "LiveManager.getLiveStatus:fail" + 详细错误信息 |

## 前置条件
在使用前需前往直播玩法后台，在能力 - 进阶互动能力中申请【玩法扩展组件能力】。申请后，需选择对应小游戏关联。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
