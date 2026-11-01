---
title: "LiveManager.syncGameProgress"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/live/live-manager/livemanager-sync-progress
update_time: 2025-10-10
---

基础库 3.85.0 开始支持本方法，这是一个**异步**方法。
观众侧同步主播游玩进度配置信息。

## 示例代码
```js
const liveManager = tt.getLiveManager();

liveManager.syncGameProgress({
    success: (res) => {
        console.log('当前主播游玩进度信息:', res.data);
    },
    fail: (res) => {
        console.log('获取失败', res);
    },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object类型，属性如下：  **对象字段** - **data**（string）：主播游玩进度配置信息 |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object类型，属性如下：  **对象字段** - **errMsg**（string）："LiveManager.syncGameProgress:fail" + 详细错误信息 - **errNo**（number）：错误码，对应信息可参考错误码说明 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21100 | can only call in video live |  |  |
| 21101 | can only call in audience side |  |  |
| 21102 | the game's instant play is closed |  |  |
| 21103 | anchor's instant play is closed |  |  |
| 21104 | serve error |  |  |

## 使用限制
仅在直播场景下可调用

## 注意事项
在一次小游戏启动周期内，data 的值不会发生变化，只有重新进入游戏才会刷新

## 前置条件
使用前，请先前往游戏开放后台，申请开通直播即看即玩能力

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
