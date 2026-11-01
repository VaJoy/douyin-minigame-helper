---
title: "RecorderManager.offResume"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/record/recorder-manager/recorder-manager-off-resume
update_time: 2024-12-10
---

## 语法

```js
RecorderManager.offResume(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
取消监听录音继续事件。

## 示例代码
```js
const recorderManager = tt.getRecorderManager();

function callback(){
   console.log("继续录音");
}

recorderManager.onResume(callback);
recorderManager.offResume(callback);

recorderManager.start();
// 暂停录音不触发回调
setTimeout(() => {
  recorderManager.pause();
  console.log("暂停录音");
}, 2000);
tt.onTouchEnd(() => {
  recorderManager.resume();
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 1.0.0 | 取消监听录音继续事件的回调函数 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
