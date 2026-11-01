---
title: "AudioContext.createOscillator"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context-create-oscillator
update_time: 2024-09-19
---

基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
创建并返回一个新的 [OscillatorNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/media-stream-audio-source-node/)。 OscillatorNode 节点表示一个振荡器，它产生一个周期的波形信号（如正弦波）。它是一个 [AudioScheduledSourceNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-buffer-source-node/) 音频处理模块， 这个模块会生成一个指定频率的波形信号（即一个固定的音调）。

## 示例代码
```js
// 创建一个 AudioContext
const ctx = tt.getAudioContext();

// 创建振荡器节点
var oscillator = ctx.createOscillator();

oscillator.type = "square";
oscillator.frequency.value = 440; // 赫兹值
oscillator.connect(ctx.destination);
oscillator.start();
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| OscillatorNode | Object | [OscillatorNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/oscillator-node) 对象实例 |

## 使用限制
本接口不支持 IDE 预览，请使用真机预览或调试

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
