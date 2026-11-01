---
title: "Camera.destroy"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/camera/camera-destroy
update_time: 2025-05-20
---

console.log("开发字节跳动小游戏过程中可以参考以下文档:");
console.log("https://developer.toutiao.com/docs/game/");

const canvas = tt.createCanvas();
const ctx = canvas.getContext("2d");
const camera = tt.createCamera();
console.log("camera 实例", camera);
camera.setBeautifyParam(0.8, 0.79, 0.4, 0.58);
camera
.start("front", true, { matting: true })
.then((video) => {
draw(video);
})
.catch((err) => {
tt.showToast({
title: "相机需要授权",
});
console.log(err);
});
// 5s 后销毁摄像头实例，无法接收新数据，绘制画面停止更新
setTimeout(() => {
camera.destroy();
}, 5000);

functiondraw(video) {
let scale = video.videoHeight / video.videoWidth;
video &&
ctx.drawImage(
video,
0,
video.videoWidth,
video.videoHeight,
0,
canvas.width,
canvas.width * scale,
);
requestAnimationFrame(function () {
draw(video);
});
}

Camera.destroy()

基础库 1.40.0 开始支持本方法，这是一个**同步**方法。
销毁摄像头实例。

## 示例代码
```js
console.log("开发字节跳动小游戏过程中可以参考以下文档:");
console.log("https://developer.toutiao.com/docs/game/");
const canvas = tt.createCanvas();
const ctx = canvas.getContext("2d");
const camera = tt.createCamera();
console.log("camera 实例", camera);
camera.setBeautifyParam(0.8, 0.79, 0.4, 0.58);
camera
  .start("front", true, { matting: true })
  .then((video) => {
    draw(video);
  })
  .catch((err) => {
    tt.showToast({
      title: "相机需要授权",
    });
    console.log(err);
  });
// 5s 后销毁摄像头实例，无法接收新数据，绘制画面停止更新
setTimeout(() => {
  camera.destroy();
}, 5000);
function draw(video) {
  let scale = video.videoHeight / video.videoWidth;
  video &&
    ctx.drawImage(
      video,
      0,
      0,
      video.videoWidth,
      video.videoHeight,
      0,
      0,
      canvas.width,
      canvas.width * scale,
    );
  requestAnimationFrame(function () {
    draw(video);
  });
}
```

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
