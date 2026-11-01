---
title: "InnerAudioContext.offPlay"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/InnerAudioContext/inner-audio-context-off-play
update_time: 2024-10-23
---

## 语法

```js
InnerAudioContext.offPlay(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
取消监听 play 事件。

## 示例代码
音频开始播放时没有弹窗提示。
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

function onplay() {
  tt.showToast({ title: "开始播放" });
}
innerAudioContext.onPlay(onplay);
innerAudioContext.offPlay(onplay);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.0.0 | 取消回调的方法 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/inner-audio-context-off-play) / [本地体验路径](inner-audio-context-off-play)
