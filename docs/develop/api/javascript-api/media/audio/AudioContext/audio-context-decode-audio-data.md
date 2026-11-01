---
title: "AudioContext.decodeAudioData"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context-decode-audio-data
update_time: 2024-09-19
---

## 语法

```js
AudioContext.decodeAudioData(audioData)
```
基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
用于异步解码音频文件， 并以 ArrayBuffer 的形式返回音频文件中的内容。该方法返回一个 Promise 对象。

其中，音频文件数据可以通过 XMLHttpRequest 来获取。解码得到的 AudioBuffer 的数据可以通过 [AudioBufferSourceNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-buffer-source-node/) 进行播放。

## 示例代码
```js
//  创建一个 AudioContext
const ctx = tt.getAudioContext();
let request = new XMLHttpRequest();
request.open("GET", "test.ogg", true);
request.responseType = "arraybuffer";

request.onload = function () {
  let audioData = request.response;
  ctx
    .decodeAudioData(audioData)
    .then((audioBuffer) => {
      console.log(audioBuffer);
      const source = ctx.createBufferSource();
      source.buffer = audioBuffer;
      source.connect(ctx.destination);
      source.loop = true;
      source.start();
      source.onended = function () {
        console.log("onended called", this);
      };
    })
    .catch((err) => {
      console.error("解码出错", err);
    });
};

request.send();
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| audioData | ArrayBuffer | 是 |  | 1.34.0 | 要解码的音频数据 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| data | Promise | Promise对象，解码完成后返回 ArrayBuffer 格式的数据。 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
