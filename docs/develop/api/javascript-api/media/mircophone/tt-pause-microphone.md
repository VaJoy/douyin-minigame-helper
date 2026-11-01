---
title: "tt.pauseMicrophone"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/mircophone/tt-pause-microphone
update_time: 2024-08-29
---

基础库 2.4.0 开始支持本方法，这是一个**同步**方法。
暂停麦克风的使用。

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

  setTimeout(() => {
    //这里5秒后，会释放麦克风暂用，下面的日志打印会输出默认值
    tt.pauseMicrophone();
  }, 5000);

  setInterval(() => {
    const { size, data } = volumeDetectionNode.getVolumeDetectionData();
    const averageVolume =
      data.reduce((prev, volume) => prev + volume, 0) / size;
    console.log(`[API: microphone] average volumn: ${averageVolume}`);
  }, 2000);
}

main();
```

## 注意事项
调用该 API 后，会释放麦克风设备权限的占用，建议开发者在不需要麦克风的场景下主动调用，合理使用麦克风权限。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/media/microphone) / [本地体验路径](tt-request-microphone)
