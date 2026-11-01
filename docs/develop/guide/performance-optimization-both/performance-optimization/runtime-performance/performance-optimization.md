---
title: "运行性能优化指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/performance-optimization/runtime-performance/performance-optimization
update_time: 2025-06-17
---

## 概述
### 运行性能与玩家体验
游戏运行性能直接影响玩家体验。玩家如频繁遇到卡顿，发烫，闪退，很快就会流失。优秀的运行性能是玩家留存、在线时长的重要保证。
- 游戏画面品质和运行性能是一个权衡。
- 游戏流畅度，响应速度和设备发热需要权衡。
- 要考虑不同设备，不同环境的运行兼容性。

运行性能需要关注的数据指标可以参考 [小游戏性能评测标准](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/game-performance-standard)。
理解小游戏的运行框架，对提升小游戏的运行性能有很大帮助。在此基础上，再不断了解，使用常见的游戏优化方案来提升性能。

### 运行环境
抖音小游戏运行在 Android 抖音，iOS 抖音，PC IDE，MAC IDE，直播伴侣 PC 版等多个平台上。
运行环境的不同，必然导致相同的游戏内容，在不同平台下的运行性能表现不同，所以需要考虑小游戏在不同平台下的差异。
> 模式对比

|  | 原理 |  | 普通模式 | 高性能模式 | 高性能+模式 |
| --- | --- | --- | --- | --- | --- |
| iOS | 普通小游戏 | 几百k js文件 | （默认模式）帧率低，发热，需要高性能 | 温度降低（CPU降低） 容易内存崩溃 | 崩溃降低。GPU降低，**内存低** |
|  | Unity 小游戏 所有 | 几M wasm 文件 需编译 | 未提供：无法使用，加载慢，帧率低，发热 | （默认模式）启动阶段发热，容易内存崩溃 | 崩溃降低。GPU降低，**内存低** |
| Android |  |  | 安卓基于V8，支持JIT。没有运行模式的区别 |  |  |
| PC |  |  | PC基于V8，支持JIT。没有运行模式的区别 |  |  |

- **运行性能**：iOS系统的普通模式下，没有JIT特性，运行效率低于Android；
  - 普通小游戏默认是运行在普通模式。可以通过配置，自行[开启高性能模式](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/runtime-performance/high-performance-mode)
  - Unity 小游戏默认是运行在高性能模式。由于性能要求高，不支持回退到普通模式。
- **内存限制**：小游戏在 Android 系统下使用独立进程，对内存相对宽松。但iOS下，如果使用了高性能模式，对内存的限制要高很多（低档机需<1G）。
  - 高性能+能够缓解内存压力，在游戏进程，给游戏留出100M～300M的内存。
- **发热**：
  - iOS下，普通模式在运行过程中，长期处于高CPU状态，所以容易发烫。
  - 高性能/高性能+下，启动阶段会进行webassembly的编译，CPU占用较高。编译完成后会降低。所以代码分包能够较好的减少编译阶段的时间。
- **渲染：**当前抖音 Unity 小游戏已经支持WebGL2.0，相当于OpenGLES3.0。未支持WebGPU。[WebGL2.0渲染支持说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/running/sc_webgl_2)

### 小游戏与 App 的性能差异
**小游戏 VS App：本质上是虚拟机与原生系统的运行差异。**
- CPU区别：通常而言，小游戏运行性能是 App 手游性能的1/3，开发者应该特别注意CPU侧的性能瓶颈。
  - JS 或 WASM，是以虚拟机的形式运行在类浏览器环境中，因此CPU算力会受限于虚拟机的执行效率。
  - Unity WebGL目前不支持多线程，导致部分模块比如AI、动画、渲染无法得到多线程的加速。
- GPU区别：小游戏是以 WebGL API 进行渲染，其中 WebGL1.0 相当于 OpenGLES2.0, WebGL2.0 相当于 OpenGLES3.0。
  - WebGL 在原生的渲染API进行封装存在少量负荷带来的开销，但基本的渲染能力与原生 App 接近。
  - 渲染特性如 GPU Instantcing、SRP Batche r需要 WebGL2.0。 （需要注意的是，当 App 手游使用了这些特性时，在小游戏未开启 WebGL2.0 时则会进一步拉大差距）
**普通小游戏 VS Unity 小游戏：本质上是 JS 与 WASM 的性能差异。**
- WASM是强类型语言，这将使得JIT优化能更准确预判运行期类型（所以在iOS的高性能模式下更明显），因此相对于JS能更快达到JIT指令优化后的峰值。通常而言，WASM~=1.5 * JS, 即JS运行效率的150%以上。

## 优化目标
由于小游戏的性能无法完全达到原生 App 的性能水平，不同的游戏对性能的要求也有很大差别。所以开发者需要根据自己的游戏内容，建立不同的最低机型要求和流畅度标准。 建议：
- 轻度休闲游戏应保证低档机型30fps以上，需特别注意机型兼容性(可使用小游戏云测获取兼容性报告)，以达到买量用户覆盖度。
- 中重度游戏应保证中高档机不限帧时达到40fps以上，实际运行可限帧30以保持长时间挂机运行的发热量。
详细的基准机型与性能要求可参考 [小游戏性能评测标准](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/game-performance-standard)，抖音小游戏平台对上线无严格的性能要求，需要开发者根据自身游戏商业化要求制定。

## 优化方向及工具
[性能测试工具](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/performance-testing-tools)
