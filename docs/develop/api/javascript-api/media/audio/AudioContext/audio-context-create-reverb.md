---
title: "AudioContext.createReverb"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context-create-reverb
update_time: 2024-09-19
---

基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
创建并返回一个新的 [ReverbNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/media-stream-audio-source-node/) 对象实例，ReverbNode 是一个混响节点，为输入音源添加混响能力。

## 示例代码
```js
// 1. 创建一个 AudioContext 和 Audio
const ctx = tt.getAudioContext();
const audio = ctx.createAudio();
audio.src = "xxxx.mp3";

const source = ctx.createMediaElementSource(audio);
const reverb = ctx.createReverb();
//KTV 效果 一些常见参数可以参考ReverbNode节点内容
reverb.roomSize = 1.17;
reverb.damping = 0.89;
reverb.stereoDepth = 0.86;
reverb.dry = 1.6;
reverb.wet = 0.41;
source.connect(reverb);
reverb.connect(ctx.destination);

audio.oncanplay = () => {
  audio.play();
};
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| ReverbNode | Object | [ReverbNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/analyser-node) 对象实例 |

## 使用限制
本接口不支持 IDE 预览，请使用真机预览或调试

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
