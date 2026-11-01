---
title: "InnerAudioContext"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/InnerAudioContext/inner-audio-context
update_time: 2025-11-14
---

InnerAudioContext 实例，可通过 [tt.createInnerAudioContext](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/tt-create-inner-audio-context) 接口获取，通过它能够操作音频播放。
## 实例属性

| 属性 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| src | string |  | 音频源地址 |
| autoplay | boolean | false | 是否自动播放 |
| loop | boolean | false | 是否自动循环 |
| obeyMuteSwitch | boolean | true | 是否遵循系统静音开关，当此参数为 false 时，即使用户打开了静音开关，仍会播放声音 |
| duration | number |  | 当前音频总时长，单位 s，只读，只有在当前有合法的 src 时返回 |
| currentTime | number |  | 当前音频进度，单位 s，只读，只有在当前有合法的 src 时返回，时间不取整，保留小数点后 6 位 |
| paused | boolean |  | 当前音频是否处于暂停状态，只读，true 表示暂停或停止，false 表示正在播放 |
| buffered | number |  | 当前音频已缓冲部分，仅保证当前播放时间点到此时间点内容已缓冲，单位百分比，只读 |
| volume | number |  | 当前音量，只读，范围 0~1。 |
| playbackRate | number |  | 播放速度。 |
| referrerPolicy | string |  | `origin`: 发送完整的referrer; `no-referrer`: 不发送。 |

**注意**， src 地址的域名必须在开发者平台 request 域名白名单中配置。
## 方法

| API | 说明 |
| --- | --- |
| [InnerAudioContext.play()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-play) | 播放。 |
| [InnerAudioContext.pause()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-pause) | 暂停。暂停后的音频再播放会从暂停处开始播放。 |
| [InnerAudioContext.stop()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-stop) | 停止。停止后的音频再播放会从头开始播放。 |
| [InnerAudioContext.seek(number position)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-seek) | 跳转到指定位置，单位 s。 |
| [InnerAudioContext.destroy()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-destroy) | 销毁当前实例。 |
| [InnerAudioContext.onCanplay(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-on-canplay) | 监听音频进入可以播放状态的事件。 |
| [InnerAudioContext.offCanplay(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-off-canplay) | 取消监听音频进入可播放状态事件。 |
| [InnerAudioContext.onPlay(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-on-play) | 监听音频播放事件。 |
| [InnerAudioContext.offPlay(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-off-play) | 取消监听音频播放事件。 |
| [InnerAudioContext.onPause(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-on-pause) | 监听音频暂停事件。 |
| [InnerAudioContext.offPause(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-off-pause) | 取消监听音频暂停事件。 |
| [InnerAudioContext.onStop(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-on-stop) | 监听音频停止事件。 |
| [InnerAudioContext.offStop(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-off-stop) | 取消监听音频停止事件。 |
| [InnerAudioContext.onEnded(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-on-ended) | 监听音频自然播放至结束的事件。 |
| [InnerAudioContext.offEnded(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-off-ended) | 取消监听音频自然播放至结束的事件。 |
| [InnerAudioContext.onTimeUpdate(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-on-time-update) | 监听音频播放进度更新事件。 |
| [InnerAudioContext.offTimeUpdate(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-off-time-update) | 取消监听音频播放进度更新事件。 |
| [InnerAudioContext.onError(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-on-error) | 监听音频播放错误事件。 |
| [InnerAudioContext.offError(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-off-error) | 取消监听音频播放错误事件。 |
| [InnerAudioContext.onWaiting(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-on-waiting) | 监听音频加载中事件，当音频因为数据不足，需要停下来加载时会触发。 |
| [InnerAudioContext.offWaiting(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-off-waiting) | 取消监听音频加载中事件（当音频因为数据不足需要停下来加载时触发）。 |
| [InnerAudioContext.onSeeking(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-on-seeking) | 监听音频进行跳转操作的事件。 |
| [InnerAudioContext.offSeeking(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-off-seeking) | 取消监听音频进行跳转操作的事件。 |
| [InnerAudioContext.onSeeked(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-on-seeked) | 监听音频完成跳转操作的事件。 |
| [InnerAudioContext.offSeeked(function callback)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-off-seeked) | 取消监听音频完成跳转操作的事件。 |

## 代码示例

```js
const innerAudioContext = tt.createInnerAudioContext();
innerAudioContext.autoplay = true;
innerAudioContext.src = "https://someaudiourl"; // 音频资源地址
innerAudioContext.onPlay(() => tt.showToast({ title: "开始播放" }));
innerAudioContext.onError((error) => {
  tt.showModal({
    title: "播放出错",
    content: `详细错误信息：${error.errMsg}`,
  });
  console.log("播放出错", error);
});
```

## Bug & Tip
Tip：InnerAudioContext 有个 obeyMuteSwitch 属性，该属性默认为 true，表示遵循系统静音模式。obeyMuteSwitch=true 时，如果手机系统为静音模式，播放时即使调整小程序的音量也会没有声音，请关闭手机静音模式后重试。
