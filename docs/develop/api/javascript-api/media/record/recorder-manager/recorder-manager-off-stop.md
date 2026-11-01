---
title: "RecorderManager.offStop"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/record/recorder-manager/recorder-manager-off-stop
update_time: 2024-12-10
---

## 语法

```js
RecorderManager.offStop(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
取消监听录音停止事件。

## 示例代码
```js
const recorderManager = tt.getRecorderManager();

function callback() {
  console.log("停止录音");
  setTimeout(() => {
    let InnerAudioContext = tt.createInnerAudioContext();
    InnerAudioContext.src = res.tempFilePath;
    InnerAudioContext.play();
    console.log("recorder stop", res);
  }, 2000);
}
recorderManager.onStop(callback);
// 取消停止事件的回调
recorderManager.offStop(callback);

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
| callback | Function | 否 |  | 1.0.0 | 监听录音停止事件的回调函数 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
