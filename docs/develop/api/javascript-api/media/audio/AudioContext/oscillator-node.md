---
title: "OscillatorNode"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/oscillator-node
update_time: 2025-06-13
---

OscillatorNode 代表一个周期性波形，例如正弦波。它是一个 AudioScheduledSourceNode 音频处理模块，可以创建给定波的指定频率 - 实际上是恒定音调，它有一个输出，但没有输入。可以通过[AudioContext.createOscillator](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-oscillator) 创建。
## 属性

| 属性名 | 类型 | 读写特性 | 取值范围 | 默认值 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- | --- |
| frequency | AudioParam | 可读写 | [-22050, 22050] | 440 | 一个 a-rate AudioParam 表示以赫兹(Hz)为单位的振荡频率 | 1.34.0 |
| detune | AudioParam | 可读写 | [-153600, 153600] | 0 | 一个 a-rate AudioParam 代表以分音为单位的振荡失调 | 1.34.0 |
| type | string | 可读写 | 可取值为 "sine", "square", "sawtooth", "triangle" and "custom" | "sine" | 一个字符串，指定要播放的波形的形状 | 1.34.0 |

## 方法
### OscillatorNode.start(number when,number offset,number duration)
开始播放。
#### 参数

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| when | number | 0 | 否 | 声音要开始播放的时间，单位是秒。默认值是 0，表示声音立即被播放 | 1.34.0 |
| offset | number | 0 | 否 | 一个偏移量，单位是秒，要从距起音频始位置多长的时间开始播放 | 1.34.0 |
| duration | number |  | 否 | 将要播放的声音的持续时间，指定单位为秒。如果这个参数没有被指定，声音播放到自然结束或者使用 stop() 方法结束 | 1.34.0 |

### OscillatorNode.stop(number when)
停止播放。
#### 参数

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| when | number | 0 | 否 | 声音应停止播放的时间，单位是秒。默认值是 0，表示声音立即被停止 | 1.34.0 |

## Bug & Tip
- Tip：OscillatorNode.start 方法 when 有效时，调用该方法后会在 when-currentTime（见 AudioContext.currentTime）秒后开始播放音频。
- Tip：OscillatorNode.stop 方法 when 有效时，调用该方法后会在 when-currentTime（见 AudioContext.currentTime）秒后停止播放音频。
