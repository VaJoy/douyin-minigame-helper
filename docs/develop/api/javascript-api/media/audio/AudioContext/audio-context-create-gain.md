---
title: "AudioContext.createGain"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context-create-gain
update_time: 2024-09-19
---

基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
创建并返回一个新的 [GainNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/media-stream-audio-source-node/) 对象实例，GainNode 是一个 AudioNode 音频处理模块，在输出前使用给定增益应用到输入。

## 示例代码
```js
// 1. 创建一个 AudioContext 和 Audio
const ctx = tt.getAudioContext();
const audio = ctx.createAudio();
audio.src = "xxxx.mp3";
// 2. 创建一个长度为 3s 的正弦波形
const buf = ctx.createBuffer(2, ctx.sampleRate * 3, ctx.sampleRate);
for (let channel = 0; channel < buf.numberOfChannels; channel++) {
  // This gives us the actual array that contains the data
  const arr = buf.getChannelData(channel);
  for (let i = 0; i < buf.length; i++) {
    // 限制峰值，防止混声溢出
    arr[i] = Math.sin((i / ctx.sampleRate) * 400 * Math.PI * 2) * 0.6;
  }
}
const source = ctx.createBufferSource();
source.buffer = buf;

// 创建增益中间节点，并且初始值为0
const gainNode = ctx.createGain();
gainNode.gain.value = 0;
source.connect(gainNode);
gainNode.connect(ctx.destination);

source.start();
source.onended = function () {
  console.log("onended called", this);
};
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| GainNode | Object | [GainNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/analyser-node) 对象实例 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
