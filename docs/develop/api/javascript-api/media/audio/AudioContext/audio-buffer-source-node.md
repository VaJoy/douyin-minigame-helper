---
title: "AudioBufferSourceNode"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-buffer-source-node
update_time: 2025-04-10
---

AudioBufferSourceNode 接口继承自 [AudioScheduledSourceNode](https://developer.mozilla.org/zh-CN/docs/Web/API/AudioScheduledSourceNode)，表现为一个音频源，它包含了一些写在内存中的音频数据，通常储存在一个 ArrayBuffer 对象中。可以通过 [AudioContext.createBufferSource](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-buffer-source) 创建。
## 属性

| 属性名 | 类型 | 读写特性 | 默认值 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| buffer | ArrayBuffer | 可读写 | null | 是一个 AudioBuffer，它定义了要播放的音频 | 1.34.0 |
| loop | boolean | 可读写 | false | 当播放完 AudioBuffer 缓冲区中的数据后是否再次重复 | 1.34.0 |

## 方法
### AudioBufferSourceNode.start(number when, number offset, number duration)
开始播放。
#### 语法

```text
AudioBufferSourceNode.start(when, offset, duration)
```

#### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| when | number | 0 | 否 | 声音要开始播放的时间，单位是秒。默认为 0，表示声音立即被播放 | 1.34.0 |
| offset | number | 0 | 否 | 一个偏移量，单位是秒，要从距音频内容起始位置多长的时间开始播放 | 1.34.0 |
| duration | number |  | 否 | 将要播放的声音的持续时间，指定单位为秒。如果这个参数没有被指定，声音播放到自然结束或者使用 AudioBufferSourceNode.stop 方法结束 | 1.34.0 |

#### 返回值
无。
### AudioBufferSourceNode.stop(number when)
停止播放。
#### 语法

```text
AudioBufferSourceNode.stop(when)
```

#### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| when | number | 0 | 否 | 声音应停止播放的时间，单位是秒。默认值是 0，表示声音立即被停止。调用该方法后会在 when-currentTime（参考 AudioContext.currentTime）秒后停止播放音频 | 1.34.0 |

## Bug&Tip
- AudioBufferSourceNode.start 方法中 when 有效时，调用该方法会在 when-currentTime（来自 AudioContext.currentTime）秒后开始播放音频。
