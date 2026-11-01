---
title: "GameRecorderManager.clipVideo"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/screen-recording/game-recorder-manager/game-recorder-manager-clip-video
update_time: 2024-11-11
---

## 语法

```js
GameRecorderManager.clipVideo(path, timeRange, clipRange)
```
基础库 1.6.1 开始支持本方法，这是一个**异步**方法。
剪辑精彩的视频片段。

## 示例代码

【代码示例1】简单裁剪，生成最后 10 秒的视频：

```js
const recorder = tt.getGameRecorderManager();
recorder.start({ duration: 60 });

recorder.clipVideo({
  path: res.videoPath,
  timeRange: [10, 0],
  success(res) {
    console.log(res.videoPath); // 生成最后10秒的视频
  },
  fail(e) {
    console.error(e);
  },
});
```

【代码示例2】结合 recordClip，顺序拼接剪辑：

```js
const recorder = tt.getGameRecorderManager();
recorder.start({ duration: 60 });

// start 之后 5 秒调用
recorder.recordClip({
  timeRange: [5, 0],
});

recorder.onStop((res) => {
  recorder.clipVideo({
    path: res.videoPath,
    timeRange: [10, 0],
    success(res) {
      // 由开始5秒 +最后10秒 拼接合成的视频
      console.log(res.videoPath);
    },
    fail(e) {
      console.error(e);
    },
  });
});
```

【代码示例3】自定义拼接顺序：

```js
const recorder = tt.getGameRecorderManager();

const clipIndexList = []; // 剪辑索引列表

// 监听录屏结束事件
recorder.onStop((res) => {
  // 对录制完成的视频进行剪辑
  recorder.clipVideo({
    path: res.videoPath,
    clipRange: clipIndexList.reverse(), // 倒序拼接
    success(res) {
      console.log(res.videoPath); // 生成 最后10秒 + 开始5秒 的视频
    },
    fail(e) {
      console.error(e);
    },
  });
});

recorder.start({
  duration: 30,
});

// 录屏开始 5秒后执行，记录 5s 之前到当前时刻的剪辑时间
recorder.recordClip({
  timeRange: [5, 0],
  success(res) {
    clipIndexList.push(res.index);
  },
});

// stop 之前调用表示裁剪录屏中的最后10s
recorder.recordClip({
  timeRange: [10, 0],
  success(res) {
    clipIndexList.push(res.index);
    recorder.stop();
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| path | string | 是 |  | 1.6.1 | path 的值为停止录屏拿到的视频地址 |
| timeRange | Array<number> | 否 |  | 1.6.1 | 裁剪的范围，用法含义与 [recordClip](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/screen-recording/game-recorder-manager/game-recorder-manager-record-clip) 中的 timeRange 完全相同，只是记录时相对的当前时刻规定为录屏结束时刻 |
| clipRange | Array<number> | 否 |  | 1.6.1 | 指定要裁剪的范围，数组中每一项为调用 recordClip 得到返回值  - 若不传 clipRange 字段，会按照默认的 recordClip 的调用顺序裁剪视频并合并，对于 recordClip 调用时 timeRange 字段可能产生交集的部分会自动合并，确保生成的视频内容是无重复且顺序符合记录顺序。 - 若指定了 clipRange 字段，平台将只会按 clipRange 数据的顺序裁剪合并视频，并对于重复的部分不做处理，开发者可利用该功能实现自定义裁剪片段、自定义拼接顺序（若同时指定了 timeRange，该片段将依旧作为最后一段拼接），对于最终视频可能出现的重复内容，需要开发者自己保证。 - 若指定了 clipRange 字段，需要保证 clipRange 参数的长度需要大于 1。再同时指定了 timeRange 的情况下，timeRange 参数会在内部生成为 recordClip 得到返回值 ，并加入到 clipRange 数组中，即 timeRange 会在内部转换为 clipRange 数组的一项追加到数组末尾。 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| videoPath | string | 剪辑的视频地址 |

## 回调：失败回调
调用失败时的回调函数

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | not record yet |  |  |
| 20000 | single record video can only be cliped once |  |  |
| 20000 | param:trimParam illegal |  |  |
| 20000 | param:range illegal |  |  |
| 20000 | param:videoPath illegal |  |  |
| 20000 | param:operationType illegal |  |  |
| 10402 | App can not call recorder |  |  |
| 21000 | Recording is not over |  |  |
| 20000 | video url is nil |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android