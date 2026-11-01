---
title: "AudioContext.createFastForward"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context-create-fast-forward
update_time: 2024-09-19
---

基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
创建并返回一个新的 [FastForwardNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/media-stream-audio-source-node/)，FastForwardNode 可以快速将上游节点的输出写入到文件。

## 示例代码
```js
// 创建一个 AudioContext 和 Audio
const ctx = tt.getAudioContext();
const audio = ctx.createAudio();
const source = context.createMediaElementSource(audio);

const ffwdNode = ctx.createFastForward(); //创建FastForwardNode

tt.downloadFile({
  url: "https://xxxx.mp3", // 合法的音频文件路径
  success(res) {
    audio.src = res.tempFilePath; //预下载临时路径
    audio.loop = true;
    audio.startTime = 0;
    audio.autoplay = true;

    source.connect(ffwdNode); //连接到快速输出节点

    ffwdNode.onended = () => {
      //快速录制完成回调，此时输出文件可用
    };

    ffwdNode.start(
      `${tt.env.USER_DATA_PATH}/FFWDFile.wav`,
      ctx.sampleRate * 10
    );
    //需要指定输出路径和样本数
  },
  fail(err) {
    tt.showModal({
      title: "下载失败",
      content: `失败原因： ${err.errMsg}`,
    });
  },
});
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| FastForwardNode | Object | [FastForwardNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/stream-file-writer-node) 对象实例 |

## 使用限制
本接口不支持 IDE 预览，请使用真机预览或调试

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
