---
title: "tt.getInnerAudioOption"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/record/tt-getinneraudiooption
update_time: 2026-08-06
---

基础库 4.26.0 开始支持本方法，这是一个**异步**方法。
查询小游戏当前音频播放路由状态，包括是否外放及当前音频路由。

## 示例代码
```js
tt.getInnerAudioOption({
  success(res) {
    console.log(res.speakerOn, res.route);
  },
  fail(err) {
    console.log("getInnerAudioOption fail", err);
  }
});
```

## 回调：成功回调
success 回调函数。接口查询成功时触发，可从回调参数中获取当前是否外放 speakerOn 和真实音频路由 route。Android 不支持该能力。
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **speakerOn**（boolean）：当前是否扬声器外放 - **route**（string）：当前真实物理路由（speakerphone/earpiece/headset/bluetooth/unknown） |

## 回调：失败回调
fail 回调函数。接口调用失败时触发，可从回调参数中获取错误码 errNo 和错误信息 errMsg。
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errNo**（number）：错误码 - **errMsg**（string）：错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21210 | getInnerAudioOption is not supported on current host version |  |  |
| 21212 | get audio option failed |  |  |
| 21214 | internal error |  |  |
| 10302 | The feature is not available in current operating system |  |  |

## 使用限制
当前不支持 Android，调用会返回 999988 / The feature is not available in current operating system。

该能力不要与 RTC 路由能力混用；RTC 房间内如需切换扬声器/听筒，请使用 [RtcRoomContext.setAudioPlaybackDevice](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/rtc/tt-get-rtc-engine)。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
