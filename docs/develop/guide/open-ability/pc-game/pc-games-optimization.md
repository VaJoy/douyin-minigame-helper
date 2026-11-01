---
title: "PC端小游戏性能优化"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/pc-game/pc-games-optimization
update_time: 2025-08-20
---

## 概述
PC小游戏在台式机或笔记本运行时，同样需要进行性能优化。本文档将主要介绍开发者需要重点关注的优化方向和推荐的优化手段。
## 优化指引
### 纹理压缩格式
纹理压缩是大部分小游戏都会使用的提升性能的手段。一般而言使用压缩纹理的好处有：
- 能够降低内存占用，降低内存峰值
- 因为避免了 CPU 侧对纹理进行软解，游戏的卡顿率也会降低。
在移动端，因为 ASTC 压缩纹理格式在移动端有非常好的兼容性，所以大部分小游戏都会默认使用 ASTC 作为压缩纹理格式。在而在PC、Mac等场景，因为**硬件层面不支持 ASTC 压缩纹理格式**，引擎通常会对纹理自动解码成RGBA的格式来保证渲染的正常，而ASTC软解对性能的影响非常大。
因此针对PC小游戏，我们推荐两种优化思路：
1. 针对PC小游戏单独打压缩格式为DXT的包
1. 用团结引擎的 [TextureManager](https://docs.unity.cn/cn/tuanjiemanual/Manual/TextureManager.html) 方案，方便调整不同平台上的纹理压缩格式。

### 避免限帧
大部分开发者会通过setPreferredFramesPerSecond接口来限制移动端小游戏帧率，从而避免发热和卡顿问题。然而PC平台上一般可以忽略功耗带来的发热问题。所以我们建议PC小游戏可以放开不必要的限帧。

### 开启更高清的画质
和【避免限帧】同理，在PC上开发者可以开启更高清的画质并参考[文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_screen)做好适配，给用户更好的游戏体验。
