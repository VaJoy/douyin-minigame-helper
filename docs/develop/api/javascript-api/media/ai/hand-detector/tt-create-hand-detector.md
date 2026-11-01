---
title: "tt.createHandDetector"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/ai/hand-detector/tt-create-hand-detector
update_time: 2025-01-02
---

### 使用提示
检测信息返回的坐标值可能需要进行缩放处理，缩放参数为：scalar

```js
const { width, height } = canvas; //要绘制的canvas
const scalar = width / video.videoWidth; //video为摄像头返回的视频流对象
//例如，使用包围盒时，需要以下处理：
var boundindBoxX = boundingBox.x * scalar;
```

### 输出结果示意图

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/hand_open-7864911843405662.jpg)

#### 结果说明

```text
1. 矩形框通过HandInfo.boundingBox画出
2. 22个手部关键点由HandInfo.key_points画出
3. 输出的 hand_open 为HandInfo.actions值
```

基础库 1.66.0 开始支持本方法，这是一个**同步**方法。
创建一个手势识别器 Detector 实例对象

## 示例代码
```js
function draw() {
  let camera = tt.createCamera();
  camera.start("front", true, { gesture: true }).then((video) => {
    drawHand(video);
  });
  function drawHand(video) {
    const canvas = tt.createCanvas();
    const ctx = canvas.getContext("2d");
    const detector = tt.createHandDetector();
    const { width, height } = canvas;
    const scalar = width / video.videoWidth;
    video.height = (video.videoHeight * width) / video.videoWidth;
    video.width = width;
    var handInfo;
    function doHandDetect() {
      handInfo = detector.detect(video);
      setTimeout(doHandDetect, 30);
    }
    function draw() {
      requestAnimationFrame(draw);
      video.paintTo(canvas, 0, 0, 0, 0, video.width, video.height);
      ctx.textBaseline = "middle";
      const txtarr = ["", "击拳", "鼓掌"];
      if (handInfo) {
        for (let i = 0; i < handInfo.length; i++) {
          const y = i * 80 + 160;
          var boundingBox = handInfo[i].boundingBox;
          var txt =
            "手势 " + (i + 1) + ": " + handInfo[i].actions + " 动态：" + handInfo[i].seqAction;
          if (handInfo[i].seqAction > 0) {
            ctx.font = "120px monospace";
            ctx.fillStyle = "red";
            ctx.fillText(
              txtarr[handInfo[i].seqAction],
              boundingBox.x * scalar,
              boundingBox.y * scalar - 50,
            );
          }
          ctx.font = "27px monospace";
          ctx.lineWidth = 1;
          ctx.fillStyle = "red";
          ctx.fillRect(0, y - 20, ctx.measureText(txt).width + 30, 41);
          ctx.fillStyle = "white";
          ctx.fillText(txt, 20, y);
          ctx.strokeStyle = "rgba(255,255,0,0.6)";
          ctx.lineWidth = 3;
          ctx.beginPath();
          ctx.rect(
            boundingBox.x * scalar,
            boundingBox.y * scalar,
            boundingBox.width * scalar,
            boundingBox.height * scalar,
          );
          ctx.stroke();
          ctx.lineWidth = 3;
          ctx.strokeStyle = "rgba(215, 255, 255,0.6)";
          let keypoints = handInfo[i].keyPoints;
          for (let i = 0; i < keypoints.length; i++) {
            if (i == 0 || i == 5 || i == 9 || i == 13 || i == 17) {
              if (i != 0) {
                ctx.stroke();
              }
              ctx.beginPath();
              ctx.moveTo(keypoints[0].x * scalar, keypoints[0].y * scalar);
            }
            if (
              i <= 4 ||
              (i > 4 && i <= 8) ||
              (i > 8 && i <= 12) ||
              (i > 12 && i <= 16) ||
              (i > 16 && i <= 20)
            ) {
              ctx.lineTo(keypoints[i].x * scalar, keypoints[i].y * scalar);
            }
            ctx.fillStyle = "purple";
            ctx.fillText(i, keypoints[i].x * scalar + 10, keypoints[i].y * scalar);
            ctx.fillStyle = "red";
            ctx.fillRect(keypoints[i].x * scalar - 6, keypoints[i].y * scalar, 10, 10);
          }
          ctx.stroke();
        }
      }
    }
    draw();
    doHandDetect();
  }
}
draw();
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| detector | Object | [Detector](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/hand-detector/detector) 对象 |

## 注意事项
- 开发者工具中不支持相关功能，请在手机上查看效果。
- 目前手势识别的输入数据仅支持摄像头。
- 手势识别的检测频率为 4 帧一次。
- 除了双手动作外，手势识别目前只支持单手识别，即同时出现两只手，手势识别只能识别先出现的手的动作。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
