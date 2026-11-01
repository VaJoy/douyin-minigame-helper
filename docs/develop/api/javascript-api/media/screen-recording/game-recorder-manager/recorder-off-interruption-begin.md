---
title: "GameRecorderManager.offInterruptionBegin"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/screen-recording/game-recorder-manager/recorder-off-interruption-begin
update_time: 2024-11-14
---

## 语法

```js
GameRecorderManager.offInterruptionBegin(callback)
```
基础库 1.6.1 开始支持本方法，这是一个**同步**方法。
取消监听录屏中断开始事件。

## 示例代码
```js
const recorder = tt.getGameRecorderManager();

function callback() {
  console.log('Record Interruption');
}

recorder.onInterruptionBegin(callback);
recorder.offInterruptionBegin(callback);

recorder.start();
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.6.1 | 取消监听录屏中断开始事件的回调函数 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
