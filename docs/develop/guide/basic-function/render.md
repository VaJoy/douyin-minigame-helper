---
title: "渲染"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/basic-function/render
update_time: 2025-06-16
---

## 画布类型说明
抖音小游戏采用单上屏画布+多离屏画布的设计模式

```js
// 创建画布对象（首个创建默认为上屏画布） 
const mainCanvas = tt.createCanvas(); 
 
// 后续创建均为离屏画布 
const offscreenCanvas1 = tt.createCanvas(); 
const offscreenCanvas2 = tt.createCanvas();
```

## 绘图上下文
通过 `Canvas.getContext` 可以创建绘图上下文。返回的具体绘图上下文类型可参考 `RenderingContext`。

```js
// 获取2D绘图上下文 
const ctx = mainCanvas.getContext('2d'); 
 
// 获取WebGL上下文（需基础库1.31.0+） 
const gl = mainCanvas.getContext('webgl');
```

## 锁帧
使用 tt.setPreferredFramesPerSecond 接口可以实现锁帧

```js
// 设置目标帧率（30/60fps） 
tt.setPreferredFramesPerSecond(60);
```

## 使用压缩纹理
抖音小游戏在 Android 及 iOS 平台支持 ETC2、ASTC 纹理压缩(历史支持的 ETC、PVR 格式因维护价值较低不再详细描述)

```js
// 加载压缩纹理示例 
const texture = gl.createTexture(); 
gl.compressedTexImage2D(..., texture);
```
