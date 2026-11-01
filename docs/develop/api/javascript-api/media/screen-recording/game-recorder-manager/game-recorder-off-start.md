---
title: "GameRecorderManager.offStart"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/screen-recording/game-recorder-manager/game-recorder-off-start
update_time: 2024-11-08
---

## 语法

```js
GameRecorderManager.offStart(callback)
```
基础库 1.4.1 开始支持本方法，这是一个**同步**方法。
取消监听录屏开始事件。

## 示例代码
```js
const recorder = tt.getGameRecorderManager();

function callback() {
    // do something;
}

recorder.onStart(callback);

recorder.offStart(callback)

// 不触发回调
recorder.start();
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.4.1 | 取消监听事件的回调函数 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
