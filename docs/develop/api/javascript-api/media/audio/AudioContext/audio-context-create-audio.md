---
title: "AudioContext.createAudio"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context-create-audio
update_time: 2024-09-19
---

基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
用于新建一个 Audio 对象，对齐 [HTMLAudioElement](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/fading-node)。

## 示例代码
```js
// 创建一个 AudioContext 和 Audio
const ctx = tt.getAudioContext();
const audio = ctx.createAudio();
// 需要先设置event监听 再设置src 确保时序正确
audio.oncanplay = () => {
  console.log("canplay called");
  audio.play();
};
audio.onplaying = () => {
  console.log("playing called");
};
audio.loop = true;
audio.startTime = 0;
audio.autoplay = true;
audio.src = "xxxx.mp3";

// 使用createMediaElementSource 从Audio对象创建一个音频源
const source = ctx.createMediaElementSource(audio);
source.connect(ctx.destination);

audio.onseeking = () => {
  console.log("seeking called");
};
audio.onwaiting = () => {
  console.log("waiting called");
};
audio.onseeked = () => {
  console.log("seeked called");
};
audio.onpause = () => {
  console.log("pause called");
};
audio.onended = () => {
  console.log("ended called");
};
audio.onstop = () => {
  // 跟 web 不同的事件
  console.log("stop called");
};
audio.onerror = (err) => {
  console.log("error called" + err.errMsg);
};
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| audio | Object | [Audio](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio) 对象实例 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
