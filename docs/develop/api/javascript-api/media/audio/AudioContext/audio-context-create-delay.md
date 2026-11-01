---
title: "AudioContext.createDelay"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context-create-delay
update_time: 2024-09-19
---

## 语法

```js
AudioContext.createDelay(delay)
```
基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
创建并返回一个新的 [DelayNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/media-stream-audio-source-node/)，DelayNode 是一个用于延迟的节点，为输入的音频数据推后指定时间。

## 示例代码
```js
// 1. 创建一个 AudioContext 和 Audio
const ctx = tt.getAudioContext();
const audio = ctx.createAudio();
audio.src = "xxxx.mp3";

const source = context.createMediaElementSource(audio);
const delayNode = context.createDelay(10 * 1000);
source.connect(delayNode);
//正常运行的话，音乐会延迟一段时间播放、
delayNode.connect(context.destination);

audio.oncanplay = () => {
  audio.play();
};
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| delay | number | 是 |  | 1.34.0 | 需要延迟的时间，单位 ms（**需大于 50ms，否则会被忽略**） |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| DelayNode | Object | [DelayNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/delay-node) 对象实例 |

## 注意事项
设置后实际生效的时间为： delay/通道数，目前固定为 delay / 2。即设置 delay 为 10s 后，音频会在延迟 5s 后播放。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
