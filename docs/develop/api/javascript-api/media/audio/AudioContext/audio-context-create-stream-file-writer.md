---
title: "AudioContext.createStreamFileWriter"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context-create-stream-file-writer
update_time: 2024-09-19
---

基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
创建并返回一个新的 [StreamFileWriterNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/media-stream-audio-source-node/)，StreamFileWriterNode 可以将输入节点的一个或多个输入写入到文件。

## 示例代码
```js
// 1. 创建一个 AudioContext 和 Audio
const ctx = tt.getAudioContext();
const audio = ctx.createAudio();
audio.src = "xxxx.mp3";

audio.startTime = 0;
audio.autoplay = true;
const source = ctx.createMediaElementSource(audio);
source.connect(ctx.destination);

const recorder = ctx.createStreamFileWriter();
source.connect(recorder);
audio.onplaying = () => {
  recorder.start(tt.env.USER_DATA_PATH + "targetFile.wav");
  recorder.start(tt.env.USER_DATA_PATH + "targetFile.wav"); //注意，刚刚录制的文件（targetFile.wav将被清除，重新开始新的录制
  recorder.start(tt.env.USER_DATA_PATH + "targetFile2.wav"); //注意，刚刚录制的文件（targetFile.wav）将立即停止录制，并开始新文件（targetFile2.wav）的录制
};
audio.onended = () => {
  recorder.stop();
  console.log("recording stopped");
  audio.onplaying = audio.onended = null;
};
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| StreamFileWriterNode | Object | [StreamFileWriterNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/stream-file-writer-node) 对象实例 |

## 使用限制
本接口不支持 IDE 预览，请使用真机预览或调试

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
