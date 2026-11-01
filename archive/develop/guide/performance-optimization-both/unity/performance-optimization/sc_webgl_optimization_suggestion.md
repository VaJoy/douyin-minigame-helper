---
title: "WebGL方案优化建议"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/performance-optimization/sc_webgl_optimization_suggestion
update_time: 2025-05-27
---

## 一、为何需要更多地进行性能优化？
WebGL 方案相对于 Native 方案，需要开发者更关注性能与体验调优。有以下几点原因：
1. 抖音小游戏定位为"即玩"，对启动耗时有要求。
1. Unity WebGL 底层基于 WebAssembly，算力远不及原生 App，Android 还是建议使用 Native 方案。
1. Unity当前版本并未对 WebGL 平台做特别多的优化，启动和性能都有问题，建议使用最新版并跟进引擎对 WebGL 的优化。
1. iOS 上性能优化不足会导致用户取消率升高、使用时长缩短，可能影响视频内容价值并波及 Android 端分发效果，建议暂缓上线。
因此，相对于 Native 方案，无论从启动还是运行上都需要做进一步性能优化。
## 二、优化目标
考虑到 iOS 上 WebGL 的性能，以及可能带来的负向效果，目前 WebGL 方案只在 iPhone XR 以上的机型开放入口。(预计覆盖60%用户)
Android 如果使用 WebGL 方案，只对 Android 10 以上的机型开放入口(预计覆盖 70%用户)。Native 方案覆盖到 Android 5
#### 建议标准

| 下载时长 | 游戏初始化时长 | 首屏渲染 | 内存 | 帧率 |
| --- | --- | --- | --- | --- |
| <10s | <3s | <15s | <1GB | >24 |

## 三、优化建议
#### 通用建议
- 使用unity 2021.3以上版本，关注最新的 Wasm 优化项
- iOS 建议将帧率上限设置为 30 帧
- 精简首场景物件，尽快渲染让玩家看到游戏首画面
- 减少初始化与首帧逻辑，Awake/Start/首次Update不要包含过重逻辑
- 减少代码包体, 剔除不必要的插件
#### 资源处理建议
- 不要下载或初始化所有未使用的资源
- 单个包体不建议超过2MB
- 贴图 maxsize 尽量不超过1024
- 压缩纹理格式优化：2021.3支持 WebGL 使用 ASTC 压缩
- 使用代码分包工具缩减WebAssembly首次下载包体
#### 进阶优化建议
请参考[性能优化指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/performance-optimization-guide)
