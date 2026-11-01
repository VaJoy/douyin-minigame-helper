---
title: "DetectData"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/ai/face-detector/detect-data
update_time: 2024-07-24
---

DetectData 是描述人脸关键信息的对象，通过 [Detector.detectFaces(Video)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/face-detector/detector) 方法创建，在 Detector 的监听函数中可以被拦截获取。
## 实例属性
| 属性名 | 类型 | 说明 |
| ------------ | -------------- | --------------------------------------------- |
| id | number | 人脸标识 |
| score | number | 识别置信度，取值范围为 0 到 1 |
| boundingBox | object | 人脸包围盒 |
| actions | Array[string]] | 面部动作 |
| face | Array[object] | 面部轮廓关键点 33 个，每个点的值为坐标（x,y） |
| leftEye | Array[object] | 左眼睛关键点 9 个 ,每个点的值为坐标（x,y) |
| leftEyebrow | Array[object] | 左眉毛关键点 9 个 ,每个点的值为坐标（x,y) |
| nose | Array[object] | 鼻子关键点 15 个 ,每个点的值为坐标（x,y) |
| mouth | Array[object] | 嘴巴关键点 20 个 ,每个点的值为坐标（x,y) |
| rightEye | Array[object] | 右眼睛关键点 9 个 ,每个点的值为坐标（x,y) |
| rightEyebrow | Array[object] | 右眉毛关键点 9 个 ,每个点的值为坐标（x,y) |
| yaw | number | 人脸水平转动角度，取值范围为 -99 到 99 |
| pitch | number | 人脸俯仰角，取值范围为 -99 到 99 |
| roll | number | 人脸歪头角度，取值范围为 -99 到 99 |
**boundingBox 属性**
| 属性名 | 类型 | 属性说明 | 备注 |
| ------ | ------ | ---------------------- | ----------------------------------------- |
| x | number | 包围盒左上角 x 坐标 | 坐标原点(0, 0)位于左上角，向右为 x 轴正向 |
| y | number | 包围盒左上角 y 坐标 | 坐标原点(0, 0)位于左上角，向下为 y 轴正向 |
| width | number | 包围盒宽度 | right-left 得到 |
| height | number | 包围盒高度 | top-bottom 得到 |
| left | number | 矩形框距离屏幕左边距离 | - |
| right | number | 矩形框距离屏幕右边距离 | - |
| top | number | 矩形框距离屏幕上边距离 | - |
| bottom | number | 矩形框距离屏幕下边距离 | - |
**actions 属性**
| 取值 | 取值说明 |
| --------------- | ---------- |
| blink | 眨眼 |
| blink_left | 左眨眼 |
| blink_right | 右眨眼 |
| mouth_ah | 嘴巴大张 |
| head_yaw | 摇头 |
| head_yaw_indian | 印度式摇头 |
| head_pitch | 点头 |
| brow_jump | 眉毛挑动 |
| mouth_pout | 嘟嘴 |
### 使用提示
检测信息返回的坐标值可能需要进行缩放处理
```js
const { width, height } = canvas; //要绘制的canvas
const scalar = width / video.videoWidth; //video为摄像头返回的视频流对象
//例如，使用人脸包围盒时，需要以下处理：
var boundindBoxX = boundingBox.x * scalar;
```
## Bug & Tip
- Tip：坐标轴的原点（0，0）位于设备的左上角，向右为 x 轴正向，向下为 y 轴正向。
- Tip：DetectData 中的 actions 属性只有在 onActions 方法的回调中才有。
