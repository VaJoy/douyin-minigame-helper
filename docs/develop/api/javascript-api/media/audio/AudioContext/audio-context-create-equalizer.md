---
title: "AudioContext.createEqualizer"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context-create-equalizer
update_time: 2024-09-19
---

基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
创建并返回一个新的 [EqualizerNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/media-stream-audio-source-node/)，EqualizerNode 是一个均衡器节点，为输入的音频数据添加均衡器效果。

## 示例代码
```js
// 创建一个 AudioContext 和 Audio
const ctx = tt.getAudioContext();
const audio = ctx.createAudio();
audio.autoplay = true;
audio.src = "xxxx.mp3";

const source = ctx.createMediaElementSource(audio);
const equalizer = ctx.createEqualizer();
// 或者ctx.createEqualizer(7.0, -8.0, 9.6, 9.6, 5.6, 1.6, -4.0, -8.0, -10.4, -11.2, -11.2)
equalizer.setAMPs(
  7.0,
  -8.0,
  9.6,
  9.6,
  5.6,
  1.6,
  -4.0,
  -8.0,
  -10.4,
  -11.2,
  -11.2
);
source.connect(equalizer);
equalizer.connect(ctx.destination);
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| EqualizerNode | Object | [EqualizerNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/equalizer-node) 对象实例 |

## 使用限制
本接口不支持 IDE 预览，请使用真机预览或调试

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
