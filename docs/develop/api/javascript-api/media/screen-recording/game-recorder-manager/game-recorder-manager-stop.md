---
title: "GameRecorderManager.stop"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/screen-recording/game-recorder-manager/game-recorder-manager-stop
update_time: 2024-11-11
---

基础库 1.6.1 开始支持本方法，这是一个**同步**方法。
停止录屏。可以通过 [GameRecorderManager.onStop](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/screen-recording/game-recorder-manager/game-recorder-manager-on-stop) 接口监听录屏结束事件，获得录屏地址。

## 示例代码
```js
const recorder = tt.getGameRecorderManager();

recorder.onStop((res) => {
  console.log(res.videoPath);
  // do something;
});

recorder.stop();
```

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 10208 | no permission to record screen |  |  |
| 21101 | record is not start |  |  |
| 10401 | internal error |  |  |
| 21000 | Recording is over |  |  |
| 21000 | video url is nil |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/game-recorder-manager-stop) / [本地体验路径](game-recorder-manager-stop)
