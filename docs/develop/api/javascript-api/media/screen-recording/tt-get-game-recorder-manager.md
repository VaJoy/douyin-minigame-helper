---
title: "tt.getGameRecorderManager"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/screen-recording/tt-get-game-recorder-manager
update_time: 2024-11-11
---

基础库 1.6.1 开始支持本方法，这是一个**同步**方法。
获取全局唯一的录屏管理器 ，该功能只能录制到小游戏全局唯一的上屏 canvas 上的内容，即开发者逻辑所绘制的内容。其他的包括客服按钮，任何类型的广告，以及 showToast 等 API 展示的 native 内容，都无法被录制到。

## 示例代码
```js
const recorder = tt.getGameRecorderManager();

recorder.onStart((res) => {
  // do something;
});

recorder.start();
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| GameRecorderManager | Object | 全局唯一的 [GameRecorderManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/screen-recording/game-recorder-manager/game-recorder-manager) 对象。 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | not supported yet |  |  |

## 注意事项
- 录屏可以录制游戏音频，但是暂时不支持录制通过 [tt.createOffscreenVideo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/video/tt-create-offscreen-video/) API 播放的视频声音。
- 注意，开发者工具不支持录屏调试，请在真机上调试录屏相关功能。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/tt-get-game-recorder-manager) / [本地体验路径](tt-get-game-recorder-manager)
