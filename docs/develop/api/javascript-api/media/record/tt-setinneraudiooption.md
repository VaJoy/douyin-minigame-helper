---
title: "tt.setInnerAudioOption"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/record/tt-setinneraudiooption
update_time: 2026-08-06
---

## 语法

```js
tt.setInnerAudioOption(speakerOn)
```
基础库 4.26.0 开始支持本方法，这是一个**异步**方法。
用于在 RecorderManager 录音会话内设置小游戏音频播放路由优先从扬声器输出。

## 示例代码
```js
tt.setInnerAudioOption({
  speakerOn: true,
  success(res) {
    console.log('setInnerAudioOption success', res);
  },
  fail(err) {
    console.log('setInnerAudioOption fail', err);
  }
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| speakerOn | boolean | 是 |  | 4.26.0 | true 设置扬声器播放；false 取消扬声器设置，让系统按当前模式和外设状态决定真实输出。 |

## 回调：成功回调
success 回调函数。接口设置成功时触发，可从回调参数中获取设置后的真实音频路由 route。Android 不支持该能力。
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **route**（string）：设置后的真实物理路由（speakerphone/earpiece/headset/bluetooth/unknown） |

## 回调：失败回调
fail 回调函数。接口调用失败时触发，可从回调参数中获取错误码 errNo 和错误信息 errMsg。
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errNo**（number）：错误码 - **errMsg**（string）：错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21210 | setInnerAudioOption is not supported on current host version |  |  |
| 21211 | set audio route failed |  |  |
| 21214 | internal error |  |  |
| 10302 | The feature is not available in current operating system |  |  |

## 使用限制
当前不支持 Android。

## 注意事项
Android 当前不支持 setInnerAudioOption，调用会返回 999988 / The feature is not available in current operating system。

在 RecorderManager 启动录音之后调用，可设置音频是否优先从扬声器输出；

该能力不要与 RTC 路由能力混用；RTC 房间内如需切换扬声器/听筒，请使用 [RtcRoomContext.setAudioPlaybackDevice](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/rtc/tt-get-rtc-engine)。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
