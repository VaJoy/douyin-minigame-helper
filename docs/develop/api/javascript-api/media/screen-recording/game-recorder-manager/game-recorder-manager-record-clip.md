---
title: "GameRecorderManager.recordClip"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/screen-recording/game-recorder-manager/game-recorder-manager-record-clip
update_time: 2024-11-11
---

## 语法

```js
GameRecorderManager.recordClip(timeRange)
```
基础库 1.6.1 开始支持本方法，这是一个**异步**方法。
记录精彩的视频片段，调用时必须是正在录屏，以调用时的录屏时刻为基准，指定前 x 秒，后 y 秒为将要裁剪的片段，可以多次调用，记录不同时刻。在结束录屏时，可以调用 [clipVideo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/screen-recording/game-recorder-manager/game-recorder-manager-clip-video) 接口剪辑并合成记录的片段。

## 示例代码

录制一段包含第 10 秒到第 25 秒内容的视频

```js
const recorder = tt.getGameRecorderManager();
const clipIndexList = []; // 剪辑索引列表

recorder.start({
  duration: 30,
});

recorder.onStop((res) => {
  recorder.clipVideo({
    path: res.videoPath,
    success(r) {
      console.log(r.videoPath);
    },
  });
});

// 假设录制第15秒时，执行第一次 recordClip
recorder.recordClip({
  timeRange: [5, 3],
  success(r) {
    console.log(r.index); // 裁剪唯一索引
    clipIndexList.push(r.index);
  },
});

// 录制到第20秒时，再次执行recordClip
recorder.recordClip({
  timeRange: [3, 5],
  success(r) {
    console.log(r.index); // 裁剪唯一索引
    clipIndexList.push(r.index);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| timeRange | Array<number> | 否 | [3, 3] | 1.6.1 | 数组的值表示记录这一时刻的前后时间段内的视频，单位是 s |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **index**（number）：裁剪片段的唯一索引，用于 [tt.clipVideo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/screen-recording/game-recorder-manager/game-recorder-manager-clip-video) 接口调用时指定裁剪拼接顺序。 |

## 回调：失败回调
调用失败时的回调函数

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 20000 | not start record |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android