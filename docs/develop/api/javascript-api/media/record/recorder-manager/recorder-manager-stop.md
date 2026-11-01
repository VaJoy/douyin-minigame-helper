---
title: "RecorderManager.stop"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/record/recorder-manager/recorder-manager-stop
update_time: 2024-12-10
---

基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
停止录音。

## 示例代码
```js
const recorderManager = tt.getRecorderManager();
recorderManager.start();
console.log("录音开始");
setTimeout(() => {
  recorderManager.stop();
  console.log("录音结束");
}, 2000);
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
