---
title: "GainNode"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/gain-node
update_time: 2024-07-24
---

GainNode 表示音量的变化。它是一个 AudioNode 音频处理模块，它可以在输入数据传播到输出之前将给定的增益应用于输入数据。 GainNode 总是只有一个输入和一个输出，两者都有相同数量的通道。可以通过 [AudioContext.createGain](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-gain) 创建。
## 属性
继承其父类 AudioNode 的属性
| 属性名 | 类型 | 读写特性 | 默认值 | 说明 | 最低支持版本 |
| ------ | ---------- | -------- | ------ | -------------------------------------------------------------------------------------- | ------------ |
| gain | AudioParam | 可读写 | 1 | 一个 a-rate AudioParam，表示要应用的增益量。必须设置 AudioParam.value 来改变增益的效果 | 1.34.0 |
## 方法
继承其父类 AudioNode 的方法。
