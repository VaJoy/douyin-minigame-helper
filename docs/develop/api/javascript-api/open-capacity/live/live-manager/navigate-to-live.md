---
title: "LiveManager.navigateToLive"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/live/live-manager/navigate-to-live
update_time: 2025-02-18
---

## 语法

```js
LiveManager.navigateToLive(roomID)
```
基础库 3.60.0 开始支持本方法，这是一个**异步**方法。
跳转到指定直播间。

## 示例代码
```js
const liveManager = tt.getLiveManager();

liveManager.navigateToLive({
    roomID: 'xxxx', // 直播间ID
    success: (res) => {
        console.log('跳转直播间成功', res)
    },
    fail: (res) => {
        console.log('跳转直播间失败', res)
    }
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| roomID | string | 是 |  | 3.60.0 | 直播间 ID。可以从 LiveManager.getLiveStatus 中获取主播直播间 id。 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "LiveManager.navigateToLive:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "LiveManager.navigateToLive:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 21001 | live room is closed |  |  |
| 21003 | live room does not exist |  |  |
| 21004 | interact game in the live room is unmount |  |  |
| 10401 | system error, please retry |  |  |
| 10101 | platform auth deny |  |  |

## 前置条件
在使用前需前往直播玩法后台，在能力 - 进阶互动能力中申请【玩法扩展组件能力】。申请后，需选择对应小游戏关联。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
