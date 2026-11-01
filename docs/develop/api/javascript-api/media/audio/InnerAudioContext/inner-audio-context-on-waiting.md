---
title: "InnerAudioContext.onWaiting"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/InnerAudioContext/inner-audio-context-on-waiting
update_time: 2024-10-23
---

## 语法

```js
InnerAudioContext.onWaiting(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
音频加载中事件，当音频因为数据不足，需要停下来加载时会触发。

## 示例代码
```js
const dataUrl = "https://someaudiourl"; // 合法的音频资源地址

const innerAudioContext = tt.createInnerAudioContext();
innerAudioContext.autoplay = true;
innerAudioContext.src = dataUrl;
innerAudioContext.onError((error) => {
  tt.showModal({
    title: "音频播放出错",
    content: `错误详细信息：${error.errMsg}`,
  });
});

innerAudioContext.onWaiting(() => {
  tt.showModal({
    title: "Waiting",
    content: "正在加载，请耐心等待",
  });
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.0.0 | 回调方法 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/media/audio/InnerAudioContext/inner-audio-context-on-waiting) / [本地体验路径](inner-audio-context-on-waiting)
