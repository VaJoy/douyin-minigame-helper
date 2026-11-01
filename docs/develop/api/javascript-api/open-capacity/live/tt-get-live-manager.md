---
title: "tt.getLiveManager"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/live/tt-get-live-manager
update_time: 2025-10-10
---

基础库 3.60.0 开始支持本方法，这是一个**同步**方法。
获取直播间管理器对象。

## 示例代码
```js
const liveManager = tt.getLiveManager();
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| LiveManager | Object | LiveManager 对象  **对象字段** - **getLiveStatus**（Function）：查询关联小玩法的主播开播信息 - **checkRoomIsValid**（Function）：检查直播间是否有效 - **navigateToLive**（Function）：跳转到指定直播间 - **onXScreenSizeChange**（Function）：监听X分屏 全屏/半屏 切换事件 - **offXScreenSizeChange**（Function）：取消监听X分屏 全屏/半屏 切换事件 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
