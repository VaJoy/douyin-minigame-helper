---
title: "RecorderManager.onFrameRecorded"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/record/recorder-manager/recorder-manager-on-frame-recorded
update_time: 2024-12-10
---

## 语法

```js
RecorderManager.onFrameRecorded(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
监听已录制完指定帧大小的文件事件。如果 RecorderManager.start 设置了 frameSize，则会回调此事件，不设置则没有此回调。

## 示例代码
```js
const recorderManager = tt.getRecorderManager();
recorderManager.onFrameRecorded((res) => {
  console.log("录音帧数据大小 " + res.frameBuffer.byteLength);
});
recorderManager.start({
  duration: 60000,
  sampleRate: 12000,
  numberOfChannels: 1,
  encodeBitRate: 25000,
  frameSize: 100,
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.0.0 | 监听器  **对象字段** - **params**（Object）：object 类型，属性如下： |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 使用限制
android 仅支持 pcm 格式，iOS 支持 aac 和 pcm 格式

## 注意事项
若设置的 frameSize 大于整个音频的大小，则在音频结束时一次性输出

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
