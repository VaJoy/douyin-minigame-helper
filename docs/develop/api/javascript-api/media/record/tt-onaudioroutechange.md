---
title: "tt.onAudioRouteChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/record/tt-onaudioroutechange
update_time: 2026-08-06
---

## 语法

```js
tt.onAudioRouteChange(callback)
```
基础库 4.26.0 开始支持本方法，这是一个**同步**方法。
监听小游戏音频播放路由或音频设备变化事件。

## 示例代码
```js
const onAudioRouteChange = (res) => {
  console.log(res.route, res.speakerOn, res.reason);
};
tt.onAudioRouteChange(onAudioRouteChange);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 4.26.0 | 音频路由或设备变化事件的回调函数；  iOS 返回真实 route/speakerOn/reason；  Android route 固定 unknown、speakerOn 固定 false，仅 reason 表示设备变化原因。  **对象字段** - **args_0**（Object）：回调参数为 object 类型，属性如下： |

## 注意事项
仅在录音RecorderManager期间返回route变化事件。

Android onAudioRouteChange 仅保留设备变化 reason，不承诺真实 route。

该能力不要与 RTC 路由能力混用；RTC 房间内如需切换扬声器/听筒，请使用 [RtcRoomContext.setAudioPlaybackDevice](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/rtc/tt-get-rtc-engine)。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
