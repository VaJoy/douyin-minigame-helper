---
title: "Detector"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/ai/face-detector/detector
update_time: 2024-07-24
---

## 说明
Detector 是用于人脸检测的对象，可以通过接口[tt.createFaceDetector](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/face-detector/tt-create-face-detector)创建，开发者可以传入摄像头返回的视频流进行人脸检测。
> `需要摄像头开启美颜功能`
## 方法
### Detector.detectFaces(Video)
接受摄像头返回的视频流对象，返回人脸检测结果 [detectData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/face-detector/detect-data) 数组。该方法是一个异步的 promise 方法。
#### 参数
| 属性名称 | 类型 | 说明 |
| -------- | ------ | ------------------------------------------------------------------------------------------ |
| Video | Object | 通过 [Camera.start](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/camera/camera-start) 创建的视频对象 |
#### 返回值
| 参数 | 参数类型 | 说明 |
| ---- | ------------------- | -------------------------------------------------------------------------------------------- |
| res | `Array` | 人脸检测结果 [detectData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/face-detector/detect-data) 数组 |
#### 代码示例
```js
Detector.detectFaces(Video)
.then((res) => {
res.forEach((detectData) => {
console.log(detectData); // 得到人脸信息
});
})
.catch((err) => {
console.log(err);
});
```
### Detector.onActions(function callback(Object detectData))
监听人脸所有发生的动作事件
### Detector.onBlink(function callback(Object detectData))
监听眨眼事件
### Detector.onBlinkLeft(function callback(Object detectData))
监听左眨眼事件
### Detector.onBlinkRight(function callback(Object detectData))
监听右眨眼事件
### Detector.onMouthAh(function callback(Object detectData))
监听嘴巴大张事件
### Detector.onMouthPout(function callback(Object detectData))
监听嘟嘴事件
### Detector.onHeadYaw(function callback(Object detectData))
监听摇头事件
### Detector.onHeadYawIndian(function callback(Object detectData))
监听印度式摇头事件
### Detector.onHeadPitch(function callback(Object detectData))
监听点头事件
### Detector.onBrowJump(function callback(Object detectData))
监听挑动眉毛事件
### Detector.offActions(function callback)
取消监听人脸所有发生的动作事件
### Detector.offBlink(function callback)
取消监听眨眼事件
### Detector.offBlinkLeft(function callback)
取消监听左眨眼事件
### Detector.offBlinkRight(function callback)
取消监听右眨眼事件
### Detector.offMouthAh(function callback)
取消监听嘴巴大张事件
### Detector.offMouthPout(function callback)
取消监听嘟嘴事件
### Detector.offHeadYaw(function callback)
取消监听摇头事件
### Detector.offHeadYawIndian(function callback)
取消监听印度式摇头事件
### Detector.offHeadPitch(function callback)
取消监听点头事件
### Detector.offBrowJump(function callback)
取消监听挑动眉毛事件
## Bug & Tip
- Tip： 目前人脸检测的输入数据仅支持摄像头。
- Tip： 当退出游戏，或者摄像头不再使用，谨记调用 destroy 方法释放摄像头。
