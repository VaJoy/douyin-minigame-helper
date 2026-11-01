---
title: "AudioContext.createMediaElementSource"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context-create-media-element-source
update_time: 2024-09-19
---

## 语法

```js
AudioContext.createMediaElementSource(element)
```
基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
创建并返回一个新的 [MediaElementAudioSourceNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-buffer-source-node)，该对象是由 Audio 对象组成的音频源。它是一个 [AudioNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-buffer/)，充当音频源。

## 示例代码
```js
// 1. 创建一个 AudioContext 和 Audio
const ctx = tt.getAudioContext();
const audio = ctx.createAudio();
audio.src = "xxxx.mp3";

//使用createMediaElementSource 从Audio对象创建一个音频源，然后通过
//volumeDetectionNode传递音频源，然后将其输入AudioDestinationNode用于播放
const source = ctx.createMediaElementSource(audio);
const volumeDetectionNode = ctx.createVolumeDetection();
source.connect(volumeDetectionNode);
volumeDetectionNode.connect(ctx.destination);

audio.oncanplay = () => {
  audio.play();
};

setInterval(() => {
  const data = volumeDetectionNode.getVolumeDetectionData();
  console.log(`[API: audio] size of data: ${data.size}`);
  console.log(`[API: audio] time: ${data.time}`);
  console.log(`[API: audio] data: ${data.data}`);
}, 2000);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| element | Object | 是 |  | 1.34.0 | 一个 Audio 对象，通过 [AudioContext.createAudio](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-audio/) 创建得到的音频源 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| MediaElementAudioSourceNode | Object | [MediaElementAudioSourceNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/media-element-audio-source-node) 对象实例 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
