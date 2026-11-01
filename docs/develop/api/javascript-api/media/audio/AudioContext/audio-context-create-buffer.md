---
title: "AudioContext.createBuffer"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context-create-buffer
update_time: 2024-09-19
---

## 语法

```js
AudioContext.createBuffer(channels, length, sampleRate)
```
基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
新建一个空白的 [AudioBuffer](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-buffer/) 对象，以便用于填充数据，通过 [AudioBufferSourceNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-buffer-source-node/) 播放。

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

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| channels | number | 是 |  | 1.34.0 | 一个定义了 buffer 中包含的声频通道数量的整数 |
| length | number | 是 |  | 1.34.0 | 一个代表 buffer 中的样本帧数的整数 |
| sampleRate | number | 是 |  | 1.34.0 | 线性音频样本的采样率，即每一秒包含的关键帧的个数。可以设置为 44100 或者 22050 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| AudioBuffer | Object | [AudioBuffer](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-buffer) 对象实例 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
