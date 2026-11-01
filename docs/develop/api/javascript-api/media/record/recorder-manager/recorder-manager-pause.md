---
title: "RecorderManager.pause"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/record/recorder-manager/recorder-manager-pause
update_time: 2024-12-10
---

基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
暂停录音

## 示例代码
```js
const recorderManager = tt.getRecorderManager();
const options = {
  duration: 60000,
  sampleRate: 12000,
  numberOfChannels: 1,
  encodeBitRate: 25000,
  frameSize: 100,
};
recorderManager.start(options);
tt.showToast({ title: "开始录音" });
tt.onTouchEnd(function () {
  recorderManager.pause();
  tt.showToast({ title: "暂停录音" });
});
```

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | Operation type is null |  |  |
| 21000 | Operation type is error |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
