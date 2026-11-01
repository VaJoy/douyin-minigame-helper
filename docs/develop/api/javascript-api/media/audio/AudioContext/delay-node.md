---
title: "DelayNode"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/delay-node
update_time: 2024-07-24
---

DelayNode 接口代表延迟线。它是一个 AudioNode 音频处理模块，在输入数据到达和传播到输出之间产生延迟。 DelayNode 总是只有一个输入和一个输出，两者都有相同数量的通道。可以通过 [AudioContext.createDelay](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-delay) 创建。
## 属性
继承其父类 AudioNode 的属性。
| 属性名 | 类型 | 读写特性 | 默认值 | 说明 | 最低支持版本 |
| ------ | ------ | -------- | ------ | -------------------------- | ------------ |
| delay | number | 可读写 | 0 | 时间长度，表示要延迟的长短 | 1.34.0 |
## 方法
继承其父类 AudioNode 的方法。
