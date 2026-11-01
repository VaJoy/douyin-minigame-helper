---
title: "tt.createCamera"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/camera/tt-create-camera
update_time: 2025-05-19
---

tt.createCamera()

classGame {
constructor() {
this.init();
this.setCanvasWH();
this.startCamera();
this.run();
}

init() {
this.canvas = tt.createCanvas();
this.ctx = this.canvas.getContext("2d");
this.camera = tt.createCamera();
this.detector = tt.createFaceDetector();
console.log(this.detector);
this.handleDetectionResult();
tt.setKeepScreenOn();
this.frame = 0;
}

setCanvasWH() {
let info = tt.getSystemInfoSync();
this.canvas.width = info.windowWidth;
this.canvas.height = info.windowHeight;
}

startCamera() {
this.camera.setBeautifyParam(1, 1, 1, 1);
this.camera
.start("front", true)
.then((video) => {
console.log(`succeed to open camera`);
this.mediaStream = video;
})
.catch((err) => {
console.log(err);
});
}

startDetector() {
this.mediaStream &&
this.detector
.detectFaces(this.mediaStream)
.then((res) => {
console.log(res); // 对应最下方的人脸信息（检测数据）内容说明
})
.catch((err) => {
console.log(err);
});
}

handleDetectionResult() {
let actions = {
blink: "眨眼",
blink_left: "左眨眼",
blink_right: "右眨眼",
mouth_ah: "嘴巴大张",
head_yaw: "摇头",
head_yaw_indian: "印度式摇头",
head_pitch: "点头",
brow_jump: "眉毛挑动",
mouth_pout: "嘟嘴",
};

this.detector.onActions((detectData) => {
for (let act of detectData.actions) {
console.log(`检测到 ${actions[act]} 动作`);
}
});

this.detector.onBlink((detectData) => {
console.log("检测到眨眼动作");
console.log(detectData);
});
}

paintVideoToCanvas() {
let video = this.mediaStream;
let canvas = this.canvas;

if (video) {
let scale = video.videoHeight / video.videoWidth;
video &&
this.ctx.drawImage(
video,
0,
video.videoWidth,
video.videoHeight,
0,
canvas.width,
canvas.width * scale
);
}

run() {
if (this.frame >= 5) {
this.frame = 0;
this.startDetector(); // detect faces once every five frames
} else {
this.frame++;
}
this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
this.paintVideoToCanvas();
requestAnimationFrame(() => {
this.run();
});
}
newGame();

基础库 1.40.0 开始支持本方法，这是一个**同步**方法。
创建并返回一个 camera 对象实例。

## 示例代码
```js
class Game {
  constructor() {
    this.init();
    this.setCanvasWH();
    this.startCamera();
    this.run();
  }

  init() {
    this.canvas = tt.createCanvas();
    this.ctx = this.canvas.getContext("2d");
    this.camera = tt.createCamera();
    this.detector = tt.createFaceDetector();
    console.log(this.detector);
    this.handleDetectionResult();
    tt.setKeepScreenOn();
    this.frame = 0;
  }

  setCanvasWH() {
    let info = tt.getSystemInfoSync();
    this.canvas.width = info.windowWidth;
    this.canvas.height = info.windowHeight;
  }

  startCamera() {
    this.camera.setBeautifyParam(1, 1, 1, 1);
    this.camera
      .start("front", true)
      .then((video) => {
        console.log(`succeed to open camera`);
        this.mediaStream = video;
      })
      .catch((err) => {
        console.log(err);
      });
  }

  startDetector() {
    this.mediaStream &&
      this.detector
        .detectFaces(this.mediaStream)
        .then((res) => {
          console.log(res); // 对应最下方的人脸信息（检测数据）内容说明
        })
        .catch((err) => {
          console.log(err);
        });
  }

  handleDetectionResult() {
    let actions = {
      blink: "眨眼",
      blink_left: "左眨眼",
      blink_right: "右眨眼",
      mouth_ah: "嘴巴大张",
      head_yaw: "摇头",
      head_yaw_indian: "印度式摇头",
      head_pitch: "点头",
      brow_jump: "眉毛挑动",
      mouth_pout: "嘟嘴",
    };

    this.detector.onActions((detectData) => {
      for (let act of detectData.actions) {
        console.log(`检测到 ${actions[act]} 动作`);
      }
    });

    this.detector.onBlink((detectData) => {
      console.log("检测到眨眼动作");
      console.log(detectData);
    });
  }

  paintVideoToCanvas() {
    let video = this.mediaStream;
    let canvas = this.canvas;

    if (video) {
      let scale = video.videoHeight / video.videoWidth;
      video &&
        this.ctx.drawImage(
          video,
          0,
          0,
          video.videoWidth,
          video.videoHeight,
          0,
          0,
          canvas.width,
          canvas.width * scale
        );
    }
  }

  run() {
    if (this.frame >= 5) {
      this.frame = 0;
      this.startDetector(); // detect faces once every five frames
    } else {
      this.frame++;
    }
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    this.paintVideoToCanvas();
    requestAnimationFrame(() => {
      this.run();
    });
  }
}
new Game();
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| Camera | Object | [Camera](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/camera/camera) 相机对象实例，可以通过设置该对象上的属性和调用该对象上的方法来控制相机。 |

## 用户授权说明
camera.start 时会调起相机的授权弹窗，授权后方可使用。

## 授权要求
无需开发者授权；需要用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/tt-create-camera) / [本地体验路径](tt-create-camera)
