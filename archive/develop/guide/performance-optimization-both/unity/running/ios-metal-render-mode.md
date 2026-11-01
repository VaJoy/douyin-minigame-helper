---
title: "iOS Metal 渲染模式"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/running/ios-metal-render-mode
update_time: 2026-09-16
---

## 简介
iOS Metal 渲染模式是平台推出的专项性能优化工具，基于 Apple Metal 图形 API 开发，替代传统 OpenGL ES 渲染方式，针对 iOS 设备的图形渲染流程进行深度优化，聚焦小游戏**渲染卡顿、帧率低、功耗高**三大核心痛点，接入过程极简高效，可在分钟级内完成配置与验证，提升小游戏在 iOS 端的运行流畅度和用户体验。
## 背景
现阶段，基于 Unity 引擎构建的抖音小游戏，在技术架构上遵循统一的跨平台实现范式：游戏核心逻辑以 WebAssembly 形式编译运行，以此兼顾跨平台兼容性与执行性能，图形渲染管线则依托 OpenGL ES 标准接口完成绘制逻辑的封装与调用。
以下是iOS渲染路径的流程图：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/6a1c3125c3ab4a31a0e40303bcf2d920~tplv-9nona0m7ha-image.image)

从 iOS 端渲染流程图可直观发现，现有渲染链路存在**两级串行指令转换环节**，是制约渲染性能的关键瓶颈：第一级转换发生在编译与运行层，由 Emscripten 将上层 OpenGL ES 指令转译为 Web 标准的 WebGL 指令；
第二级转换发生在系统底层，鉴于苹果已全面终止 OpenGL ES 的技术维护与迭代，iOS 系统内核需通过兼容层将 WebGL 指令翻译为平台原生 Metal 图形指令，方可交由 GPU 执行渲染。

连续的指令转译与适配过程，会引入显著的 CPU 指令解析开销与 GPU 管线调度损耗，最终造成小游戏帧率波动、渲染延迟升高等性能问题。

## Metal 技术原理与性能收益
面对 iOS 平台传统小游戏渲染架构的固有缺陷，抖音所提供的 Metal 技术方案实现了原生 Metal 渲染后端的直接适配，有效破除了传统链路中两级指令串行转换带来的性能桎梏。项目接入 Metal 原生渲染方案后，全新的渲染执行流程如下：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/55ca2cbed88b49daad80d59beecb470d~tplv-9nona0m7ha-image.image)

### 性能收益

| 优化类别 | 优化收益 |
| --- | --- |
| 帧耗时 | **降低10～15%** |
| 功耗 | **降低10～15%** |

### **前提条件**
1. 安装团结引擎 版本 ≥ 1.6.8；
1. 确保 [TTSDK](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/install-sdk) 版本 ≥ 6.6.8，抖音 app 版本 ≥ 36.5.0，低版本抖音会自动降级为 WebGL；
1. 游戏仅用团结引擎开发，不涉及其他引擎或多引擎混合（Cocos、Unity+Cocos 等）；
1. Android、PC 及抖音开发者工具暂不支持 Metal 渲染，将自动降级为 WebGL；
1. 仅支持在 iOS>=14 的机型上运行，低版本iOS系统会自动降级为 WebGL。

## 接入流程
### SDK 配置
- 在团结引擎中选择 TTSDK 6.6.8 及以上版本，确保 Metal 功能支持。
- 确认平台设置中 “抖音小游戏” 为活跃子平台（Active）。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/aa571bf3627743a6a13a5c6be76763ae~tplv-9nona0m7ha-image.image)

### 团结引擎打包配置调整
- 打开 Project Settings，进入 Other Settings 选项。
- 在 Graphics APIs 中添加 Metal（Experimental），保留现有必要配置。
- 按正常打包流程执行。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/067333ad79c140369bc71501fde2f845~tplv-9nona0m7ha-image.image)

### 验证 game.json 配置
- 打包完成后，上传到抖音开发者工具，检查工程目录下的 game.json 文件。
- 确认文件中包含 graphicsDeviceType 配置，且包含“Metal”字段。
- 不修改 graphicsDeviceType 相关内容，避免 Metal 功能失效。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/9f0aa1e2dfff440cb2b17e24711c7de9~tplv-9nona0m7ha-image.image)

## 注意事项
### 分包相关
若已启用分包能力，则 WebGL 和 Metal 模式均需执行分包收集操作。若需切换至 WebGL 模式，可直接移除`graphicsDeviceType`配置项中关于 Metal 的相关设置，此时打包生成的包体即为 WebGL 模式，即可开展后续分包函数的收集工作。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/7560c7372c82421e98c9ba5ceb0ffad7~tplv-9nona0m7ha-image.image)

## FAQ
### Q1. 如何判断游戏已经启动 iOS Metal 方案？
A1. 打开调试，重启小游戏，查看vConsole的日志。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/8205bcc6ccf0413fbb9560d30830c285~tplv-9nona0m7ha-image.image)

### Q2. 开启 Metal 模式后，存在异常渲染？
A2. 由于 WebGL 与 Metal 底层图形体系存在较大差异，部分渲染管线需完成原生适配改造，如需解决相关问题，欢迎随时与我们团队沟通，协同完成问题排查与适配优化。

### Q3. 开启 Metal 模式后，性能反而变差了？
A3.
1）核查当前场景是否实际启用了分包能力；
2）验证分包逻辑的生效范围，确认是否仅在 WebGL 模式下执行分包操作，Metal 模式未开启分包机制；
3）若上述排查排除分包为问题诱因，则判定大概率是 Metal 方案的适配问题，建议与我方团队联动，共同开展问题定位与排查工作。

### Q4. 启用 Metal 模式后，录屏与视频播放功能表现异常？
A4. 当前 Metal 模式下暂未支持录屏和视频播放功能，因此使用时会出现异常。相关功能开发已全部完成，计划于 10 月正式对外上线。

## 联系我们
如有任何问题请咨询平台对接人
