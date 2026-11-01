---
title: "RecorderManager"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/record/recorder-manager/recorder-manager
update_time: 2025-05-22
---

全局唯一的录音管理器，通过[tt.getRecorderManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/record/tt-get-recorder-manager)返回。
## 方法

| 方法名 | 说明 | 最低支持版本 |
| --- | --- | --- |
| start | 开始录音 | 1.0.0 |
| pause | 暂停录音 | 1.0.0 |
| resume | 继续录音 | 1.0.0 |
| stop | 停止录音 | 1.0.0 |
| onStart/offStart | 绑定/解绑 录音开始事件的监听器 | 1.0.0 |
| onPause/offPause | 绑定/解绑 录音暂停事件的监听器 | 1.0.0 |
| onResume/offResume | 绑定/解绑 录音继续事件的监听器 | 1.0.0 |
| onStop/offStop | 绑定/解绑录音结束事件的监听器 | 1.0.0 |
| onError/offError | 绑定/解绑 录音错误事件的监听器 | 1.0.0 |
| onFrameRecorded/offFrameRecorded | 绑定/解绑 已录制完指定帧大小的文件事件的监听器。如果设置了 frameSize，则会回调此事件，不设置则不会回调 | 1.0.0 |
