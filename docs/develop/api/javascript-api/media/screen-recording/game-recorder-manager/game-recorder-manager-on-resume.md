---
title: "GameRecorderManager.onResume"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/screen-recording/game-recorder-manager/game-recorder-manager-on-resume
update_time: 2024-11-11
---

## 语法

```js
GameRecorderManager.onResume(callback)
```
基础库 1.6.1 开始支持本方法，这是一个**同步**方法。
监听录屏继续事件。

## 示例代码
```js
const recorder = tt.getGameRecorderManager();

recorder.start();

recorder.onResume(() => {
    console.log('Record Resume');
})

// 2s后暂停录屏
setTimeout(() => {
    recorder.pause();
}, 2000);

// 再过2s重新开始录屏
setTimeout(() => {
    recorder.resume();
}, 4000);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 1.6.1 | 监听录屏继续事件的回调函数 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/game-recorder-manager-on-resume) / [本地体验路径](game-recorder-manager-on-resume)
