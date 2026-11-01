---
title: "tt.requestMicrophone"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/mircophone/tt-request-microphone
update_time: 2024-08-29
---

基础库 1.23.0 开始支持本方法，这是一个**同步**方法。
向端上发出麦克风请求，调起麦克风功能。

## 示例代码
```js
async function main() {
  const streamID = await tt.requestMicrophone();
  const context = tt.getAudioContext();
  const sourceNode = context.createMediaStreamSource(streamID);
  // sourceNode.connect(context.destination);

  /**
   * 检测音量以确认麦克风确实起效了
   */
  const volumeDetectionNode = context.createVolumeDetection();
  sourceNode.connect(volumeDetectionNode);
  // volumeDetectionNode.connect(context.destination);

  setInterval(() => {
    const { size, data } = volumeDetectionNode.getVolumeDetectionData();
    const averageVolume =
      data.reduce((prev, volume) => prev + volume, 0) / size;
    console.log(`[API: microphone] average volumn: ${averageVolume}`);
  }, 2000);
}

main();
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | Promise | Promise<number> 对象，其中数字是一个 stream ID |

## 注意事项
- 对于一些声音类游戏，比如声控游戏，需要在录屏分享时带上麦克风声音，请参考 **AudioContext.createMediaStreamSource** 方法使用
- 本 API 在游戏整个生命周期过程中，应当只被调用一次，如果需要暂停恢复，请配合 tt.pauseMicroPhone 和 tt.resumeMicrophone 使用

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/media/microphone) / [本地体验路径](tt-request-microphone)
