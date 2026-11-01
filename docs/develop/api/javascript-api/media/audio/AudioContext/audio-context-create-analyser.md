---
title: "AudioContext.createAnalyser"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-context-create-analyser
update_time: 2024-09-19
---

基础库 1.34.0 开始支持本方法，这是一个**同步**方法。
创建并返回一个新的 [AnalyserNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/media-stream-audio-source-node/) 对象实例。可以用来获取音频时间和频率数据，以及实现数据可视化。

## 示例代码

【代码示例 1】：创建 AnalyserNode 并 connect 到音频源节点,将音频数据画到画板上。

```js
const ctx = tt.getAudioContext();
const audio = ctx.createAudio();
audio.src = "xxxx.mp3";
audio.oncanplay = () => {
  audio.play();
};
const source = ctx.createMediaElementSource(audio);

const analyser = ctx.createAnalyser();
source.connect(analyser);

var bufferLength = analyser.frequencyBinCount;
var dataArray = new Uint8Array(bufferLength);
analyser.getByteTimeDomainData(dataArray);

// 获取画板
var canvas = tt.createCanvas();
var canvasCtx = canvas.getContext("2d");

// 把音频数据画到canvas上
function draw() {
  requestAnimationFrame(draw);

  analyser.getByteTimeDomainData(dataArray);

  canvasCtx.fillStyle = "rgb(200, 200, 200)";
  canvasCtx.fillRect(0, 0, canvas.width, canvas.height);
  canvasCtx.lineWidth = 2;
  canvasCtx.strokeStyle = "rgb(0, 0, 0)";
  canvasCtx.beginPath();

  var sliceWidth = (canvas.width * 1.0) / bufferLength;
  var x = 0;

  for (var i = 0; i < bufferLength; i++) {
    var v = dataArray[i] / 128.0;
    var y = (v * canvas.height) / 2;
    if (i === 0) {
      canvasCtx.moveTo(x, y);
    } else {
      canvasCtx.lineTo(x, y);
    }
    x += sliceWidth;
  }

  canvasCtx.lineTo(canvas.width, canvas.height / 2);
  canvasCtx.stroke();
}

draw();
```

【代码示例 2】：通过 createAnalyser 方式获取音量数据，如果遇到 VolumeDetectionNode 延迟较大的情况下可以尝试此方法。

```js
const ctx = tt.getAudioContext();
const audio = ctx.createAudio();
audio.src = "xxxx.mp3";
audio.oncanplay = () => {
  audio.play();
};
const source = ctx.createMediaElementSource(audio);

const analyser = ctx.createAnalyser();
source.connect(analyser);

var bufferLength = analyser.frequencyBinCount;
var array = new Uint8Array(bufferLength);
analyser.getByteFrequencyData(array);

let values = 0;
const arrlength = array.length;

// 获取频率振幅
for (let i = 0; i < arrlength; i++) {
  values += array[i];
}
//通过平均值去到当前音量数据
const average = values / arrlength;
const data = average;
//返回数据
var volume = {
  data: new Float32Array([data]),
  size: 1,
  time: new Float32Array([Date.now()]),
};

const systemInfo = tt.getSystemInfoSync();
if (systemInfo.platform === "ios") {
  tt.onShow(() => {
    source.connect(analyser);
  });

  tt.onHide(() => {
    source.disconnect(analyser);
  });
}
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| AnalyserNode | Object | [AnalyserNode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/analyser-node) 对象实例 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android