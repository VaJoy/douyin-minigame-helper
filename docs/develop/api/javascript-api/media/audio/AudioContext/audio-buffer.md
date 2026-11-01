---
title: "AudioBuffer"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-buffer
update_time: 2024-07-24
---

AudioBuffer 接口表示存在内存里的一段短小的音频资源，利用[AudioContext.decodeAudioData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-decode-audio-data)
方法从一个音频文件构建，或者利用 [AudioContext.createBuffer](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-buffer)
从原始数据构建。把音频放入 AudioBuffer 后，可以传入到一个 AudioBufferSourceNode 进行播放。
## 属性
| 属性名 | 类型 | 读写特性 | 默认值 | 说明 | 最低支持版本 |
| ---------------- | ----------- | -------- | --------- | ------------------------------------------------ | ------------ |
| numberOfChannels | number | 只读 | 2048 | 返回存储在缓存区的 PCM 数据的通道数 | 1.34.0 |
| length | number | 只读 | -30 | 返回存储在缓存区的 PCM 数据的采样帧率 | 1.34.0 |
| duration | number | 只读 | -100 | 返回存储在缓存区的 PCM 数据的时长（单位为秒） | 1.34.0 |
| sampleRate | number | 只读 | fftSize/2 | 存储在缓存区的 PCM 数据的采样率，单位为 sample/s | 1.34.0 |
| buffer | ArrayBuffer | 只读 | | AudioBuffer 所对应的缓存区（buffer） | 1.34.0 |
## 方法
### getChannelData(number channel)
返回一个 Float32Array，包含了带有频道的 PCM 数据，由频道参数定义（0 代表第一个频道）。
#### 语法
```
AudioBuffer.getChannelData(channel)
```
#### 参数说明
| 属性名称 | 数据类型 | 必填 | 描述 |
| -------- | -------- | ---- | ------------------ |
| channel | number | 是 | 要获取数据的频道号 |
#### 返回值
一个 Float32Array
## 代码示例
请参考 [AudioContext.createBufferSource 代码示例](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-buffer-source/#代码示例)。
