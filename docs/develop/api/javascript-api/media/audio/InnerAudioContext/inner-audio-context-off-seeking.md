---
title: "InnerAudioContext.offSeeking"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/InnerAudioContext/inner-audio-context-off-seeking
update_time: 2024-10-23
---

## 语法

```js
InnerAudioContext.offSeeking(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
取消监听音频开始进行 [seek](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/media/audio/inner-audio-context/inner-audio-context-seek/) 操作的事件。

## 示例代码
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

function onseeking() {
  tt.showToast({ title: "跳转播放位置" });
}
innerAudioContext.onSeeking(onseeking);
innerAudioContext.offSeeking(onseeking);

setTimeout(() => innerAudioContext.seek(3), 1000);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.0.0 | 取消回调的方法 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-off-seeking) / [本地体验路径](inner-audio-context-off-seeking)
