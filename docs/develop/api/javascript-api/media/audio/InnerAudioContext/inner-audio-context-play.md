---
title: "InnerAudioContext.play"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/InnerAudioContext/inner-audio-context-play
update_time: 2024-10-23
---

基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
播放音频。

## 示例代码
【代码示例1】：播放网络音频文件
```js
const dataUrl = "https://someaudiourl";
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
```
【代码示例2】：播放本地临时路径音频文件
```js
const innerAudioContext = tt.createInnerAudioContext();
const dataUrl = "https://someaudiourl"; // 合法的音频资源地址

tt.downloadFile({
  url: dataUrl, // 待下载的音频文件，需要在小程序开发者平台配置downloadFile 合法域名
  success: (res) => {
    if (res.statusCode === 200) {
      // 下载到本地的文件临时地址
      console.log("下载成功", res.tempFilePath);
      innerAudioContext.src = res.tempFilePath;
      innerAudioContext.onError((error) => {
        tt.showModal({
          title: "播放出错",
          content: `详细错误信息：${error.errMsg}`,
        });
        console.log("播放出错", error);
      });
      innerAudioContext.play();
    }
  },
  fail: (err) => {
    console.log("下载失败", res.errMsg);
    tt.showModal({
      title: "下载失败",
      content: err.errMsg,
      showCancel: false,
    });
  },
});
```

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | params $paramName is required |  |  |
| 20000 | params $paramName type is not $paramType type |  |  |
| 20000 | $paramName is invalid |  |  |
| 21102 | audio not exist |  |  |
| 21100 | operation not success |  |  |
| 10401 | internal error |  |  |
| 20000 | Unknown command |  |  |
| 10401 | audio init fail/audio create fail |  |  |
| 10501 | app in background |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-play) / [本地体验路径](inner-audio-context-play)
