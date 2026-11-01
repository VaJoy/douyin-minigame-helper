---
title: "InnerAudioContext.pause"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/InnerAudioContext/inner-audio-context-pause
update_time: 2024-10-23
---

基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
暂停播放。暂停后再次播放时基于此状态继续播放。

## 示例代码
2s 后音频暂停播放。
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

setTimeout(() => innerAudioContext.pause(), 2000);
```

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | Unknown command |  |  |
| 10401 | audio init fail/audio create fail |  |  |
| 10401 | audio state fail |  |  |
| 10401 | audio pause fail |  |  |
| 10401 | internal error |  |  |
| 20000 | params $paramName is required |  |  |
| 20000 | params $paramName type is not $paramType type |  |  |
| 20000 | $paramName is invalid |  |  |
| 21102 | audio not exist |  |  |
| 21100 | operation not success |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-pause) / [本地体验路径](inner-audio-context-seek)
