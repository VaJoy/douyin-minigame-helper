---
title: "tt.createInnerAudioContext"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/tt-create-inner-audio-context
update_time: 2024-10-21
---

基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
创建并返回内部 audio 上下文 [innerAudioContext](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context/) 实例，通过它能够操作音频播放。

## 示例代码
```js
const innerAudioContext = tt.createInnerAudioContext();
console.log("创建的 audio 上下文实例为: ", innerAudioContext);
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| InnerAudioContext | Object | [InnerAudioContext](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context/) 对象实例 |

## 使用限制
目前音频支持的采样率为 44.1kHz，22.05kHz，11.025kHz，8kHz，16kHz，24kHz，32kHz，48kHz。如果不在支持的范围内，音频无法正常播放。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/media/audio/tt-create-inner-audio-context) / [本地体验路径](tt-create-inner-audio-context)
