---
title: "tt.addAudioTrack"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/tt-add-audio-track
update_time: 2024-08-15
---

## 语法

```js
tt.addAudioTrack(videoPath, audioParam)
```
基础库 2.16.0 开始支持本方法，这是一个**异步**方法。
调用本方法可为本地视频添加额外的音轨。

## 示例代码
```js
let recoerderVideoPath;

function mixAudioTrack() {
  const task = tt.addAudioTrack({
    videoPath: recoerderVideoPath, // 录屏后文件的路径
    audioParams: [
      {
        audioPath: "ttfile://user//xx.MP3", // 这里填音频的路径
        audioRange: [0, 10000], // 音乐自身的入点，出点，可以填视频的duration
        videoRange: [0, 10000], // 视频自身的入点，出点。这里表示将音频的前10s，与视频的前10s进行混合。
      },
    ],
    success(res) {
      tt.showModal({
        title: "混合成功",
        content: JSON.stringify(res),
      });
      tt.shareAppMessage({
        channel: "video",
        extra: {
          videoPath: res.videoPath,
        },
        success() {
          tt.showModal({
            title: "分享成功",
          });
        },
        fail(e) {
          tt.showModal({
            title: "分享失败",
          });
        },
      });
    },
    fail(res) {
      tt.showModal({
        title: "混合失败",
        content: JSON.stringify(res),
      });
    },
  });
  task.onProgressUpdate((res) => {
    console.log("progress: " + res.progress);
    tt.showToast({
      title: JSON.stringify(res.progress),
    });
  });
}

tt.onTouchEnd((res) => {
  const recorder = tt.getGameRecorderManager();

  recorder.onStop((res) => {
    console.log(res.videoPath);
    recoerderVideoPath = res.videoPath;
    mixAudioTrack();
  });

  recorder.start();
  setTimeout(() => {
    recorder.stop();
  }, 15000);
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| videoPath | string | 是 |  | 2.16.0 | 要混合的视频路径 |
| audioParam | Array<Object> | 是 |  | 2.16.0 | 要混合的音频属性，支持大部分音频格式和 mp4  **对象字段** - **audioPath**（string）：要混合的音频路径 - **audioRange**（Array<number>）：结构为[start:number, end:number]。要混合的音频自身的入点，出点，即选择哪一段音频进行混合 （单位为毫秒） - **videoRange**（Array<number>）：结构为[start:number, end:number]。要混合的视频自身的入点，出点，即要往哪一段视频混合（单位为毫秒） ，建议 audioRange 与 videoRange 保持一致 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | Object | object 类型， 属性如下：  **对象字段** - **onProgressUpdate**（Function）：进度更新回调函数， 入参类型是 { progress: number }, 表示进度 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："addAudioTrack:ok" - **videoPath**（string）：视频地址 - **videoDuration**（number）：视频长度 |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："addAudioTrack:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10301 | The host environment does not support audio mixing |  |  |
| -2000 | invalid params |  |  |
| 10401 | internal error |  |  |
| 10301 | feature not support |  |  |
| 20000 | invalid params |  |  |
| 21501 | pre task is still in progress |  |  |
| 20001 | invalid param |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
