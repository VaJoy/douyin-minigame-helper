---
title: "AudioNode"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-node
update_time: 2024-07-24
---

AudioNode 是一个处理音频的通用模块, 比如一个音频源（如 [MediaElementAudioSourceNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/media-element-audio-source-node/)）, 一个音频地址或者一个中间处理模块 (如 均衡器 [EqualizerNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/equalizer-node/)), 或一个音量控制器如 [GainNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/gain-node/)。多个 AudioNode 可以以模块化的方式动态连接在一起。
## 属性
| 属性名 | 类型 | 读写特性 | 默认值 | 说明 | 最低支持版本 |
| ---------------- | ------------ | -------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| context | AudioContext | 只读 | | 所属的 AudioContext | 1.34.0 |
| channelCount | number | 只读 | 2 | 表示该输出必须包含的通道数，不支持自定义设置 | 1.34.0 |
| channelCountMode | string | 只读 | | 表示当前节点的通道模式，不支持设置 | 1.34.0 |
| isSampleSource | boolean | 读写 | false | 是否为采样节点，参考 [AudioContext.createMediaStreamSource](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-media-stream-source/) | 1.34.0 |
## 方法
### AudioNode.connect(AudioNode destination)
将此节点的一个输出连接到另一个节点的一个输入，返回目标节点。
#### 语法
```
AudioNode.connect(destination)
```
#### 参数说明
| 属性名称 | 数据类型 | 描述 |
| ----------- | --------- | ---------------- |
| destination | AudioNode | 要连接的目标节点 |
#### 返回值
AudioNode
### AudioNode.disconnect()
将这个节点从另一个节点断开连接。
#### 语法
```
AudioNode.disconnect()
```
#### 参数说明
无
#### 返回值
AudioNode
## 代码示例
```js
const audioCtx = tt.getAudioContext();
const oscillator = audioCtx.createOscillator();
const gainNode = audioCtx.createGain();
oscillator.connect(gainNode);
gainNode.connect(audioCtx.destination);
```
## Bug & Tip
暂无。
