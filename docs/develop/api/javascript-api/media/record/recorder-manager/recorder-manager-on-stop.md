---
title: "RecorderManager.onStop"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/record/recorder-manager/recorder-manager-on-stop
update_time: 2024-12-10
---

## 语法

```js
RecorderManager.onStop(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
监听录音停止事件。

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

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.0.0 | 监听录音停止事件的回调函数  **对象字段** - **params**（Object）：object 类型，属性如下： |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 注意事项
如果在录音结束的 onStop 回调中立即通过 createInnerAudioContext 或者 getAudioContext 系列能力播放音频，可能会出现音频无法正常播放的情况。这是某些情况下，录音音频文件尚未完全写完导致的，可以增加一定延时来播放音频文件。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
