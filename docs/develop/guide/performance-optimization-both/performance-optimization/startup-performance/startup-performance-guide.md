---
title: "启动性能优化指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/performance-optimization/startup-performance/startup-performance-guide
update_time: 2025-06-17
---

## 启动加载时序

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2bb479768612498180c9df7773a7f8ec)

## 启动阶段

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/96cf88c709e84f20aaf7cbcfef157169)

| 阶段 | 平均耗时 | 开发者可优化点 |
| --- | --- | --- |
| 准备阶段 | 500 ~ 1000 ms | 无 |
| **下载阶段** | **3000ms-20000ms** | 缩减首包：指引文档：[启动性能优化](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/sc_webgl_start_progress) |
| 解压阶段 | 1400ms ～ 2901ms | 缩减首包，同上 |
| 编译阶段+callmain | 编译:293～380ms callmain:1000~1500ms | 分包 |
| 游戏内加载 | 需游戏主动上报tti | 减少初次进入所需要的资源大小：[将贴图，模型，声音，字体等资源，改为用到时再下载](https://docs.unity.cn/cn/Packages-cn/com.unity.autostreaming@2.0/manual/) 官方优化指引：[Unity小游戏接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide)、[启动性能优化](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/sc_webgl_start_progress) 接入新文件系统：[使用新文件系统说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_new_file_system) |

## 关键指标
- 首次加载时长
- 平台平均加载时长（包含首次加载和非首次加载）
- 标准参考： [小游戏性能评测标准](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/game-performance-standard)

### 如何提升启动速度
- [提升普通小游戏启动速度](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/startup-performance/boost-game-speed)
- [提升Unity WebGL游戏启动速度](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/sc_webgl_start_speed)

### 设置封面图优化体验
[定制启动封面](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/experience-and-data/sc_webgl_loading_page)

### wasm的代码分包
如果非 H5 小游戏，是基于 WebAssembly 的游戏，可以通过 Wasm 的分包，减少首包的大小[Wasm分包工具说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/code-upload/sc_webgl_split)

### 启动场景上报
为了能够帮助游戏开发者主动发现游戏可交互前的各个阶段的性能、留存情况，现提供官方的上报接口 tt.reportscene，让开发者实现自定义启动场景数据的上报。
[启动场景上报分析](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/startup-performance/startup-scene-analysis)
