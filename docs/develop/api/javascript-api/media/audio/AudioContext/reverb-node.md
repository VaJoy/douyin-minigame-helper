---
title: "ReverbNode"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/reverb-node
update_time: 2024-07-24
---

ReverbNode 表示一个混响节点。它是一个 AudioNode 音频处理模块，它可以在输入数据传播到输出之前将给定的混响参数应用于输入数据。可以通过 [AudioContext.createEqualizer](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-reverb) 创建。
## 属性
继承其父类 AudioNode 的属性。
| 属性名 | 类型 | 读写特性 | 默认值 | 说明 | 最低支持版本 |
| ----------- | ------ | -------- | ------ | ------------------------------------------------------------------- | ------------ |
| zoomSize | number | 可读写 | 0.6 | 用于控制产生混响的“空间”大小。范围[0, 1.5] | 1.34.0 |
| dry | number | 可读写 | 0.5 | “干声”，也是直达声，没有经过反射直接传到人耳的声音。范围[-3.0, 3.0] | 1.34.0 |
| wet | number | 可读写 | 0.5 | “湿声”，除了直达声之外的所有发射的声音。范围[-3.0, 3.0] | 1.34.0 |
| damping | number | 可读写 | 0.5 | 混响阻尼调节，这里是高频阻尼。范围[0, 1.5] | 1.34.0 |
| stereoDepth | number | 可读写 | 1.0 | 立体深度。范围[0, 1.0] | 1.34.0 |
| dryGainDB | number | 可读写 | 0.0 | 湿增益，用于平衡混响和干声。范围[-60.0, 60.0] | 1.34.0 |
| wetGainDB | number | 可读写 | 0.0 | 干增益，用于平衡混响和干声。范围[-60.0, 60.0] | 1.34.0 |
## 方法
继承其父类 AudioNode 的方法。
## 常见配置
为了方便使用，以下是一些常见的混响参数配置：
| 名称 | zoomSize | damping | stereoDepth | dry | wet |
| ------- | -------- | ------- | ----------- | ---- | ---- |
| KTV | 1.17 | 0.89 | 0.86 | 1.6 | 0.41 |
| Cristal | 1.5 | 0.84 | 1 | 0.75 | 0.26 |
| Pop | 0.98 | 0.89 | 1 | 0.98 | 0.26 |
| Rock | 1.42 | 0.91 | 0.87 | 1.24 | 0.44 |
