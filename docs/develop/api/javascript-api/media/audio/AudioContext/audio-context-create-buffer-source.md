---
title: "AudioContext.createBufferSource"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context-create-buffer-source
update_time: 2024-09-19
---

基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
创建一个新的 [AudioBufferSourceNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-buffer/) 节点, 该节点可以播放 [AudioBuffer](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-buffer-source-node/) 对象的音频数据。

AudioBuffer 对象可以通过 [AudioContext.createBuffer](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-buffer/) 来创建或者通过 [AudioContext.decodeAudioData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-decode-audio-data/) 成功解码音轨后获取。

## 示例代码
```js
// 1. 创建一个 AudioContext
const ctx = tt.getAudioContext();

// 2. 创建一个长度为 3s 的正弦波形
const buf = ctx.createBuffer(2, ctx.sampleRate * 3, ctx.sampleRate);
for (let channel = 0; channel < buf.numberOfChannels; channel++) {
  // 获取频道的数据
  const arr = buf.getChannelData(channel);
  for (let i = 0; i < buf.length; i++) {
    // 限制峰值，防止混声溢出
    arr[i] = Math.sin((i / ctx.sampleRate) * 400 * Math.PI * 2) * 0.6;
  }
}
const source = ctx.createBufferSource();
source.buffer = buf;
source.connect(ctx.destination);

source.start();
source.onended = function () {
  console.log("onended called", this);
};
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| AudioBufferSourceNode | Object | [AudioBufferSourceNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-buffer-source-node) 对象实例 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
