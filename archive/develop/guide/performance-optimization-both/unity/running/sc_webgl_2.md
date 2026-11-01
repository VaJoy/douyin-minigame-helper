---
title: "WebGL2.0渲染支持说明"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/running/sc_webgl_2
update_time: 2025-09-05
---

## 一. 什么是WebGL2.0
WebGL 是一种用于在 Web 浏览器中渲染图形的 API，基于 OpenGL ES 图形库的功能。WebGL 1.0 大致与 OpenGL ES 2.0 功能相匹配，而 WebGL 2.0 大致与 OpenGL ES 3.0 功能相匹配。根据游戏项目统计，我们发现相对于 WebGL 1.0，更适合以下游戏需求:
- 线性颜色空间渲染
- 使用GPU Instancing提高渲染性能
- 使用SRP Batcher提高渲染性能
- 使用URP PostProcessing效果提升品质
- 存在大量依赖OpenGL ES 3.0以上的Shader难以降低
## 二. WebGL2.0 使用限制
### Unity 小游戏
- iOS：**仅支持iOS 15.0**及以上系统
- Android ：[Android WebGL2.0支持](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/android-webgl2)。
### 普通小游戏
- Android：自基础库 3.70.0.0 版本开始支持
- iOS：
  - 普通模式：自基础库 3.70.0.0 版本开始支持
  - 高性能模式：无基础库版本要求，但仅支持 iOS 15.0 及以上系统版本
  - 高性能+模式：无基础库版本和 iOS 系统版本要求

#
