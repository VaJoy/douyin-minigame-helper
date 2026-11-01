---
title: "RecorderManager.resume"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/record/recorder-manager/recorder-manager-resume
update_time: 2024-12-10
---

基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
继续录音。在调用[暂停录音](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/record/recorder-manager/recorder-manager-resume)之后，可以调用 RecorderManager.resume 继续录音，继续录音的内容会拼接到上一次暂停录音之后。

## 示例代码
```js
const recorderManager = tt.getRecorderManager();
let isRecording = false;
recorderManager.start();
isRecording = true;
tt.showToast({ title: "开始录音" });
tt.onTouchEnd(() => {
  if (isRecording) {
    recorderManager.pause();
    tt.showToast({ title: "暂停录音" });
    isRecording = false;
  } else {
    recorderManager.resume();
    tt.showToast({ title: "继续录音" });
    isRecording = true;
  }
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
