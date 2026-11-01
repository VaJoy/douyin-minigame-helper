---
title: "AudioContext.createF0Detection"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context-create-f0-detection
update_time: 2024-09-19
---

基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
创建并返回一个新的 [F0DetectionNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/media-stream-audio-source-node/)，F0DetectionNode 是一个用于获取输入源的音高检测数据。约 20ms 检测一次。音高数据最多保存 2 秒，每次调用获取的是最近 2s 的数据。

## 示例代码
```js
// 1. 创建一个 AudioContext 和 Audio
const ctx = tt.getAudioContext();
const audio = ctx.createAudio();
audio.src = "xxxx.mp3";

const source = context.createMediaElementSource(audio);
const f0DetectionNode = context.createF0Detection();
source.connect(f0DetectionNode);
f0DetectionNode.connect(context.destination);

audio.oncanplay = () => {
  audio.play();
};

setInterval(() => {
  const data = f0DetectionNode.getF0DetectionData();
  console.log(`[API: audio] size of data: ${data.size}`);
  console.log(`[API: audio] time: ${data.time}`);
  console.log(`[API: audio] data: ${data.data}`);
}, 2000);
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| F0DetectionNode | Object | [F0DetectionNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/f0-detection-node) 对象实例 |

## 使用限制
本接口不支持 IDE 预览，请使用真机预览或调试

## 注意事项
音高检测的范围目前为 0 到 采样率/30，开发者可以根据自己需要过滤特定范围内的音高数据

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
