---
title: "tt.getRecorderManager"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/record/tt-get-recorder-manager
update_time: 2024-11-27
---

基础库 1.6.1 开始支持本方法，这是一个**同步**方法。
获取**全局唯一**的 recorderManager。通过 recorderManager 进行录音操作和管理。该 api 多次调用时返回的是同一个实例，在多页面使用时，会操作到同一个上下文对象。

## 示例代码
```js
const recorderManager = tt.getRecorderManager();
recorderManager.onStop(() => {
  console.log("停止录音");
  setTimeout(() => {
    let InnerAudioContext = tt.createInnerAudioContext();
    InnerAudioContext.src = res.tempFilePath;
    InnerAudioContext.play();
    console.log("recorder stop", res);
  }, 2000);
});
recorderManager.start();
console.log("开始录音");
setTimeout(() => {
  recorderManager.stop();
  console.log("暂停录音");
}, 2000);
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| RecorderManager | Object | [RecorderManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/record/recorder-manager/recorder-manager) 实例对象 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 注意事项
如果在录音结束的 onStop 回调中立即通过 createInnerAudioContext 或者 getAudioContext 系列能力播放音频，可能会出现音频无法播放。这是某些情况下，录音音频文件尚未完全写完导致的，可以增加一定延时来播放音频文件。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/tt-get-recorder-manager) / [本地体验路径](tt-get-recorder-manager)
