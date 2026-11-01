---
title: "tt.getAudioContext"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/tt-get-audio-context
update_time: 2024-11-08
---

基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
获取并返回音频处理模块对象 [AudioContext](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context)。

## 示例代码
```js
const audioContext = tt.getAudioContext();
console.log("获取的音频处理模块对象为: ", audioContext);
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| AudioContext | Object | [AudioContext](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context) 对象 |

## 使用限制
目前音频支持的采样率为 44.1kHz，22.05kHz，11.025kHz，8kHz，16kHz，24kHz，32kHz，48kHz。如果不在支持的范围内，音频无法正常播放。

## 注意事项
- 小游戏的 AudioContext 接口设计是按照 W3C 的[Web Audio API](https://developer.mozilla.org/zh-CN/docs/Web/API/Web_Audio_API)设计实现，这部分内容开发者也可以参照 Web Audio API 部分了解自己感兴趣的内容和使用方法。
- 除此之外提供了一些额外的接口方便开发者使用，包括 DelayNode，EqualizerNode，EqualizerNod，F0DetectionNode，VolumeDetectionNode，StreamFileWriter，FastForwardNode。
- 如果为了保证最大的兼容性，可以使用 44.1kHz, 96Kbps 参数的 mp3。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/media/audio/tt-get-audio-context) / [本地体验路径](tt-get-audio-context)
