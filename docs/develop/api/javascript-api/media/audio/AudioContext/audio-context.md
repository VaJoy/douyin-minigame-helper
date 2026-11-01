---
title: "AudioContext"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context
update_time: 2024-07-24
---

`AudioContext` 实例，可通过 [tt.getAudioContext](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/basic-library/compatibility-description/) 接口获取实例。
## 属性

| 属性名 | 类型 | 默认值 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| sampleRate | number |  | 采样率（每秒采样数）， 同一个 AudioContext 中的所有节点采样率相同，所以不支持采样率转换 | 1.34.0 |
| currentTime | number | 0 | 返回以秒为单位的时间，当获取 AudioContext 的时候初始值为 0，并实时增加。所有的预定时间都和它相关。这不是一个可以开始、暂停、和重定位的时间，它总是增加的 | 1.34.0 |
| destination | object |  | 表示音频图形在特定情况下的最终输出地址（通常为扬声器），使用方式详见[destination](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context/#destination) | 1.34.0 |

### destination
一般使用步骤如下：

- 输入音频源 audio
- 音频源连接到 AudioNode 做额外处理
- AudioNode 再连接到 AudioContext.destination 上做输出

## 方法
### [AudioContext.createAudio](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-audio)
创建一个 Audio 对象。
### [AudioContext.createBuffer](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-buffer)
新建一个空白的 AudioBuffer 对象，用于填充数据，可通过 [AudioBufferSourceNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-buffer-source-node/) 播放。
### [AudioContext.createBufferSource](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-buffer-source)
创建一个新的 [AudioBufferSourceNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-buffer-source-node/) 节点, 该节点可以通过 [AudioBuffer](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-buffer/) 对象来播放音频数据。
### [AudioContext.createMediaElementSource](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-media-element-source)
创建并返回一个新的 [MediaElementAudioSourceNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/media-element-audio-source-node/) 对象节点。
### [AudioContext.createMediaStreamSource](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-media-stream-source)
创建并返回一个新的 [MediaStreamAudioSourceNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/media-stream-audio-source-node) 对象节点。
### [AudioContext.createAnalyser](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-analyser)
创建并返回一个新的 [AnalyserNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/analyser-node/) 对象实例。
### [AudioContext.createGain](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-gain)
创建并返回一个新的 [GainNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/gain-node/) 对象实例。
### [AudioContext.createReverb](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-reverb)
创建并返回一个新的 [ReverbNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/reverb-node/) 对象实例。
### [AudioContext.createEqualizer](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-equalizer)
创建并返回一个新的 EqualizerNode 对象节点。
### [AudioContext.createDelay](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-delay)
创建并返回一个新的 [DelayNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/delay-node/) 对象节点。
### [AudioContext.createF0Detection](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-f0-detection)
创建并返回一个新的 [F0DetectionNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/f0-detection-node/) 对象节点。
### [AudioContext.createVolumeDetection](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-volume-detection)
创建并返回一个新的 [VolumeDetectionNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/volume-detection-node/) 对象节点。
### [AudioContext.createOscillator](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-oscillator)
创建并返回一个新的 [OscillatorNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/oscillator-node/) 对象节点。
### [AudioContext.createFading](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-fading)
创建并返回一个新的 [FadingNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/fading-node/) 对象节点。
### [AudioContext.createStreamFileWriter](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-stream-file-writer/)
创建并返回一个新的 [StreamFileWriterNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/stream-file-writer-node/) 对象节点。
### [AudioContext.createFastForward](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-fast-forward)
创建并返回一个新的 [FastForwardNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/fast-forward-node/) 对象节点。
### [AudioContext.decodeAudioData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-decode-audio-data)
decodeAudioData 方法可用于异步解码， 以 ArrayBuffer 的形式返回音频文件中的内容。
