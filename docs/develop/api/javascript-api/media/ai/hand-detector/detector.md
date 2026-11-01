---
title: "Detector"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/ai/hand-detector/detector
update_time: 2024-07-24
---

Detector 是描述手势识别的对象，可以通过接口 [tt.createHandDetector](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/hand-detector/tt-create-hand-detector) 创建，开发者可以传入摄像头返回的视频流进行手势识别。
## 方法
### Detector.detect(Video)
该方法接受摄像头返回的视频流对象，返回手势识别得到的结果，这是一个同步方法
**输入：**
| 属性 | 类型 | 说明 |
| ----- | ------ | ----------------------------------------------------------------------------------------- |
| Video | Object | 通过 [Camera.start](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/camera/camera-start)创建的视频对象 |
**输出：**
| 属性 | 类型 | 说明 |
| ---------------------------------------------------------------------- | ------ | -------------------------- |
| [HandInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/hand-detector/hand-info) | Object | 描述手势关键点和动作的对象 |
#### 语法
```js
var handInfo = Detector.detect(video); // video 是摄像头返回的流对象
```
## Bug & Tip
- Tip： 暂无。
