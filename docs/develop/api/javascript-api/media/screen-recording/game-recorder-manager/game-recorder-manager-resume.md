---
title: "GameRecorderManager.resume"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/screen-recording/game-recorder-manager/game-recorder-manager-resume
update_time: 2024-11-11
---

基础库 1.6.1 开始支持本方法，这是一个**同步**方法。
继续录屏。

## 示例代码
```js
const recorder = tt.getGameRecorderManager();

recorder.start();

// 2s后暂停录屏
setTimeout(() => {
    recorder.pause();
}, 2000);

// 再过2s重新开始录屏
setTimeout(() => {
    recorder.resume();
}, 4000);
```

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 21000 | Recording |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/game-recorder-manager-resume) / [本地体验路径](game-recorder-manager-resume)
