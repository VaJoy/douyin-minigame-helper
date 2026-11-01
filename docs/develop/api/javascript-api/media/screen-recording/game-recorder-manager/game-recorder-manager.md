---
title: "GameRecorderManager"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/screen-recording/game-recorder-manager/game-recorder-manager
update_time: 2024-07-24
---

> 基础库 1.4.1 开始支持。
全局唯一的录屏管理器。通过[tt.getGameRecorderManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/screen-recording/tt-get-game-recorder-manager/)获取。
## 属性说明
| 属性名 | 类型 | 说明 |
| ------------------- | -------- | ------------------------ |
| start | Function | 开始录屏 |
| pause | Function | 暂停录屏 |
| recordClip | Function | 记录精彩时刻 |
| clipVideo | Function | 剪辑精彩时刻 |
| resume | Function | 继续录屏 |
| stop | Function | 停止录屏 |
| onStart | Function | 监听录屏开始事件 |
| onResume | Function | 监听录屏继续事件 |
| onPause | Function | 监听录屏暂停事件 |
| onStop | Function | 监听录屏停止事件 |
| onError | Function | 监听录屏错误事件 |
| onInterruptionBegin | Function | 监听录屏中断结束 |
| onInterruptionEnd | Function | 监听录屏中断开始 |
| getMark | Function | 获取录屏水印图像的宽高值 |
