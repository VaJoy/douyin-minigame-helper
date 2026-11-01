---
title: "Audio"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio
update_time: 2024-07-24
---

Audio 对象 对齐 [HTMLAudioElement](https://www.w3.org/TR/2011/WD-html5-author-20110809/the-audio-element.html)，提供类似 HTMLAudioElement 的能力。
## 属性

| 属性名 | 类型 | 读写特性 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- | --- |
| src | string | 可读写 |  | 是 | 播放音频文件路径 | 1.34.0 |
| srcObject | ArrayBuffer | 可读写 |  | 是 | 支持设置二进制数据的音频源，与 src 属性设置效果一致 | 1.34.0 |
| currentTime | number | 可读写 | 0 | 否 | 当前播放的位置，单位为秒。写操作会定位到设置的时间处 | 1.34.0 |
| startTime | number | 可读写 | 0 | 否 | 从何时开始播放，单位为秒 | 1.34.0 |
| duration | number | 只读 | 0 | 否 | 音频总长度，单位为秒 | 1.34.0 |
| volume | number | 可读写 | 1 | 否 | 音频音量，范围为 0 到 1 | 1.34.0 |
| autoplay | boolean | 可读写 | false | 否 | 是否自动播放 | 1.34.0 |
| loop | boolean | 可读写 | false | 否 | 是否循环播放 | 1.34.0 |
| paused | boolean | 只读 | true | 否 | 是否处于暂停或停止状态 | 1.34.0 |
| oncanplay | function | 可读写 |  | 否 | 监听音频进入可以播放状态的事件 | 1.34.0 |
| onseeking | function | 可读写 |  | 否 | 监听音频进行跳转操作的事件 | 1.34.0 |
| onseeked | function | 可读写 |  | 否 | 监听音频完成跳转操作（seek）的事件 | 1.34.0 |
| onplay | function | 可读写 |  | 否 | 监听音频开始播放事件。可能是刚开始播放，也可能是从暂停中恢复播放 | 1.34.0 |
| onpause | function | 可读写 |  | 否 | 监听音频暂停事件，当调用 pause 暂停播放音频时候触发 | 1.34.0 |
| onended | function | 可读写 |  | 否 | 监听音频播放完成事件，当音频播放完毕后触发 | 1.34.0 |
| onstop | function | 可读写 |  | 否 | 监听音频停止事件，当调用 stop 停止播放音频时候触发 | 1.34.0 |
| onwaiting | function | 可读写 |  | 否 | 监听音频加载中的事件，当音频因为数据不足，需要停下来加载时会触发 | 1.34.0 |

## 方法

| 方法名 | 说明 | 最低支持版本 |
| --- | --- | --- |
| play | 播放 Audio 音频 | 1.34.0 |
| pause | 暂停播放 Audio 音频 | 1.34.0 |
| stop | 停止播放 Audio 音频 | 1.34.0 |

## 代码示例
可参考 [AudioContext.createAudio 代码示例](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-audio/#%E4%BB%A3%E7%A0%81%E7%A4%BA%E4%BE%8B)。
