---
title: "视频"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/basic-function/video
update_time: 2025-09-11
---

在抖音小游戏中，存在两种创建视频的方式，分别是[video](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/video/tt-create-video)和[offscreenvideo(离屏视频)](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/video/tt-create-offscreen-video)

## Video

> 视频组件默认位于游戏 Canvas 顶层，因层级高于游戏 UI 元素，故会对其产生遮挡效果
> 通常情况下，video满足大部分播放视频的需求场景。可以使用 [tt.createVideo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/video/tt-create-video)在游戏画布之上插入视频

### 示例代码

```js
const video = tt.createVideo({
  src: "https://example.com/video.mp4",
  width: 320,
  height: 240,
  autoplay: false
});
video.play();
```

注意：建议手动设置宽高为屏幕尺寸
### **注意事项**
- **内存管理**：
1. 视频播放结束后调用 `video.destroy()`释放资源。
## createOffscreenVideo

> `tt.createOffscreenVideo`是抖音小游戏专用的**离屏视频渲染接口**，其核心目标是将视频解码与画面渲染从主线程剥离，通过后台处理避免阻塞游戏主逻辑，同时支持更灵活的层级混合（如视频与UI叠加）。与常规 `tt.createVideo`的直接屏幕渲染不同，离屏渲染需通过 `paintTo()`将视频帧绘制到 Canvas 上实现显示, 抖音小游戏中，原生视频组件默认覆盖 Canvas 上层，无法叠加 UI。`createOffscreenVideo`通过离屏渲染 + `paintTo()`实现视频帧与 Canvas 融合，彻底解决层级冲突问题

#### 示例代码

```js
const offscreenVideo = tt.createOffscreenVideo();
offscreenVideo.src = "https://example.com/video.mp4";

// 将离屏视频绘制到主 Canvas
function renderFrame() {
  offscreenVideo.paintTo(mainCanvas, 0, 0, width, height);
  requestAnimationFrame(renderFrame);
}
offscreenVideo.onPlay(() => renderFrame());
```

### 适用场景

- 游戏内视频背景 + 交互按钮（如暂停/播放控件）；
- AR 特效中实时视频与 3D 模型叠加；
- 动态视频滤镜（如灰度、边缘检测）

### 注意事项
1. **内存泄漏风险**：
  - 离屏视频实例需手动销毁（`video.destroy()`），否则持续占用 GPU 内存。实测未销毁时，内存增长迅速
## WebGL视频适配问题
详见[视频适配](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/video-adapt)
