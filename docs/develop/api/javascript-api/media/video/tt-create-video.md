---
title: "tt.createVideo"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/video/tt-create-video
update_time: 2024-07-24
---

> 基础库 1.37.0 开始支持本方法，这是一个同步方法。
创建一个上屏 Video 视频对象
## 语法
```
tt.createVideo()
```
## 返回值
[Video](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/video/video) 对象
## 代码示例
【代码示例 1】：渲染指定的视频资源
```js
// 首次调用tt.creatCanvas方法时创建的canvas为上屏canvas，之后创建的均为离屏canvas
let canvas = tt.createCanvas();
let context = canvas.getContext("2d");
// 调用tt.createVideo方法时，必须保证已经存在一个上屏canvas（onScreenCanvas）
let video = tt.createVideo();
// 当设置了的`src`属性之后就能监听视频可播放
video.src = "xxxxxx";
video.onCanplay((scale) => {
video.play();
});
```
【代码示例 2】：渲染摄像头资源
```js
// 调用tt.createVideo方法时，必须保证已经存在一个上屏canvas（onScreenCanvas）
let canvas = tt.createCanvas();
let context = canvas.getContext("2d");
let video = tt.createVideo();
let camera = tt.createCamera();
camera
.start("front", true)
.then((srcObject) => {
video.srcObject = srcObject;
video.play();
})
.catch((err) => {
tt.showToast({
title: "摄像机需要授权",
});
console.log(err);
});
```
## Bug & Tip
- Tip：首次调用 tt.creatCanvas 方法时创建的 canvas 为上屏 canvas，之后创建的均为离屏 canvas。
- Tip：调用 tt.createVideo 方法时，必须保证已经存在一个上屏 canvas。
