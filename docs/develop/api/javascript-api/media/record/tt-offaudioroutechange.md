---
title: "tt.offAudioRouteChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/record/tt-offaudioroutechange
update_time: 2026-08-06
---

## 语法

```js
tt.offAudioRouteChange(callback)
```
基础库 4.26.0 开始支持本方法，这是一个**同步**方法。
用于取消 onAudioRouteChange 注册的 callback；不传 callback 时取消全部监听。

## 示例代码
```js
tt.offAudioRouteChange(onAudioRouteChange);
// 不传 callback 可取消所有监听
tt.offAudioRouteChange();
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 4.26.0 | 要取消的回调函数，如果不提供则取消所有监听。  **对象字段** - **args_0**（Object）：回调参数为 object 类型，属性如下： |

## 注意事项
Recorder stop 不会自动清除 callback；不再需要监听时应显式调用 offAudioRouteChange。

Android onAudioRouteChange 仅保留设备变化 reason，不承诺真实 route。

RTC 房间内如需切换扬声器/听筒，请使用 [RtcRoomContext.setAudioPlaybackDevice](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/rtc/tt-get-rtc-engine)。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
