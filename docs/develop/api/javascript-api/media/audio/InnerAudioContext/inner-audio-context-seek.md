---
title: "InnerAudioContext.seek"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/InnerAudioContext/inner-audio-context-seek
update_time: 2024-10-23
---

## 语法

```js
InnerAudioContext.seek(options)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
跳转到指定位置播放。

## 示例代码
播放 1s 后跳转到音频 3s 的位置继续播放。
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
setTimeout(() => innerAudioContext.seek(3), 1000);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| options | number | 是 |  | 1.0.0 | 跳转的时间（单位：s） |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-seek) / [本地体验路径](inner-audio-context-seek)
