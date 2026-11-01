---
title: "AudioContext.createFading"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context-create-fading
update_time: 2024-09-19
---

基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
创建并返回一个新的 [FadingNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/media-stream-audio-source-node/)，用于控制音频数据淡入淡出的节点。

## 示例代码
```js
// 1. 创建一个 AudioContext 和 Audio
const ctx = tt.getAudioContext();
const audio = ctx.createAudio();
audio.src = "xxxx.mp3";

const source = context.createMediaElementSource(audio);
const FadingNode = context.createFading();
//这里的音频总时间是大于10s的，设置淡入效果时间为2s，淡出效果时间为2s。
FadingNode.setFadingDurations(10 * 1000, 2 * 1000, 2 * 1000);
//淡入效果曲线为log函数，淡出效果曲线为linear效果。
FadingNode.setFadingCurves(0, 1);
source.connect(FadingNode);
FadingNode.connect(context.destination);

audio.oncanplay = () => {
  audio.play();
};
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| FadingNode | Object | [FadingNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/fading-node) 对象实例 |

## 使用限制
本接口不支持 IDE 预览，请使用真机预览或调试

## 废弃说明
该 API 已废弃。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
