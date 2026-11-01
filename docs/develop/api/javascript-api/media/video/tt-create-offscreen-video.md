---
title: "tt.createOffscreenVideo"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/video/tt-create-offscreen-video
update_time: 2025-03-10
---

> 基础库 1.37.0 开始支持本方法，这是一个同步方法。
创建一个离屏视频对象，与上屏视频对象自动绘制视频不同，离屏对象需要自行绘制。
## 语法

```text
tt.createOffscreenVideo()
```

## 参数说明
暂无
## 返回值

| 类型 | 说明 | 最低支持版本 |
| --- | --- | --- |
| object | [Video](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/video/video) 对象 | 1.37.0 |

## 代码示例
【代码示例 1】：离屏 video 渲染到指定 canvas

```js
let canvas = tt.createCanvas();
let context = canvas.getContext("2d");
let video = tt.createOffscreenVideo();
video.src = "xxxxxx"; //这里传入要播放的视频的路径，可以是tt开头本地路径也可以是其他网络路径
video.onCanplay(() => {
  video.play();
  function drawVideo() {
    requestAnimationFrame(drawVideo);
    // 离屏video需要绘制
    video.paintTo(canvas, 0, 0, 0, 0, video.width, video.height);
  }
  drawVideo();
});
```

【代码示例 2】：离屏 video 作为纹理在 cocos 2.x 上下文渲染

```typescript

@ccclass
export default class HomeLogic extends cc.Component {
  onLoad() {
    this.showCamera();
  }
  update() {
    if (this.video && this.videoTexture) {
      this.videoTexture.update({
        image: this.video,
        // ...
      });
    }
  }

  private cameraNode;
  private video;
  private videoTexture: cc.Texture2D;

  private showCamera() {
    this.cameraNode = new cc.Node();
    this.cameraNode.addComponent(cc.Sprite);
    this.node.insertChild(this.cameraNode, 0);
    if (typeof globalThis.tt !== "undefined") {
      this.playVideo();
    }
  }

  private playVideo() {
    this.video = globalThis.tt.createOffscreenVideo();
    // 传入视频src
    this.video.src = "your video url";
    this.video.onCanplay(() => {
      this.video.play();
      this.videoTexture = new cc.Texture2D();
      this.videoTexture.initWithElement(this.video);
      this.videoTexture.handleLoadedTexture();
      this.cameraNode.getComponent(cc.Sprite).spriteFrame = new cc.SpriteFrame(
        this.videoTexture
      );
      this.cameraNode.width = cc.view.getVisibleSize().width;
      this.cameraNode.height =
        (this.video.videoHeight / this.video.videoWidth) *
        this.cameraNode.width;
    });
  }
}
```

【代码示例 2】：cocos 3.x 版本需要调整一下绘制方式

```typescript
this.video = globalThis.tt.createOffscreenVideo();
// 传入视频src
this.video.src = "your video url";
this.video.onCanplay(() => {
  const imgAsset = new ImageAsset();
  imgAsset.reset(this.video);
  this.videoTexture = new Texture2D();
  this.videoTexture.image = imgAsset;
  const spFrame = new SpriteFrame();
  spFrame.texture = this.videoTexture;
  this.videoSpriteNode.getComponent(Sprite).spriteFrame = spFrame;
  const width = view.getVisibleSize().width;
  this.video.width = width;
  this.video.height = this.video.videoHeight / this.video.videoWidth * width;
  const uiTransform = this.videoSpriteNode.getComponent(UITransform);
  uiTransform.width = this.video.width;
  uiTransform.height = this.video.height;
  this.video.play();
});
```

## Bug & Tip
无
