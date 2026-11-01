---
title: "InnerAudioContext.stop"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/InnerAudioContext/inner-audio-context-stop
update_time: 2024-10-23
---

基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
停止播放。停止后再次播放时从头开始播放。

## 示例代码
2s 后音频停止播放。
```js
const dataUrl = "https://someaudiourl"; // 合法的音频资源地址
const innerAudioContext = tt.createInnerAudioContext();
innerAudioContext.autoplay = true;
innerAudioContext.src = dataUrl;

innerAudioContext.onError((error) => {
  tt.showModal({
    title: "播放出错",
    content: `详细错误信息：${error.errMsg}`,
  });
  console.log("播放出错", error);
});

setTimeout(() => innerAudioContext.stop(), 2000);
```

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | params $paramName is required |  |  |
| 20000 | params $paramName type is not $paramType type |  |  |
| 20000 | $paramName is invalid |  |  |
| 21102 | audio not exist |  |  |
| 21100 | operation not success |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-stop) / [本地体验路径](inner-audio-context-stop)
