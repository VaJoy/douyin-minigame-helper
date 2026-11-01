---
title: "通过Worker异步计算优化CPU使用"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/performance-optimization/runtime-performance/worker-async-cpu-optimize
update_time: 2025-06-17
---

## 为什么需要降低JS线程消耗
抖音小游戏在平台侧是运行在JS线程中的，JS代码不仅需要处理业务逻辑，也需要执行渲染指令，在一个需要60帧运行的游戏上，每一帧的耗时不能超过16毫秒，而这其中渲染耗时至少需要6毫秒，那么处理业务逻辑的JS代码需要控制在10毫秒以内。
然而在实际运行过程中，很难保证JS的代码逻辑可以稳定控制在10毫秒以内，并且由于iOS系统限制，在普通模式下不支持JIT，导致运行性能格外吃紧。

## 分帧策略
对于计算性能造成游戏帧率下降或卡顿的场景，大多数开发人员会选择分帧策略，将执行时间较长的函数拆分成多个执行时间短的子任务，将子任务分配到每一帧中，按计划顺序执行，直到全部子任务执行完毕。分帧策略虽然对部分场景有效果，但是依旧存在如下问题：
- 不是所有计算逻辑都能够被拆分。比如数组排序, 树的递归查找, 图像处理算法等, 执行中需要维护当前状态, 且调用上非线性, 无法轻易地拆分为子任务。
- 可以拆分的逻辑难以把控力度。拆分的子任务在高性能机器上可以控制在 16ms 内, 但在性能落后的机器上表现并不一定理想。 16ms 的用户感知时间, 并不会因为用户手上机器的差别而变化。
- 拆分的子任务并不稳定。计算逻辑可能会随着业务场景发生变化，将同步计算逻辑拆分成子任务，可能会造成每次改动业务都需要review多个子任务的代码。
这个时候，可以使用Worker 的多线程能力, 从宏观上将整个同步 JS 任务异步化。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/42e1b8da2e5b43068ba3047de8c4f6e8~tplv-9nona0m7ha-image.image)

## 多线程 Worker
> 详细接口文档参考：[Worker API](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/worker/worker/)
一些异步处理的任务，可以放置于 Worker 线程中运行，待运行结束后，再把结果返回到小游戏主线程。
Worker 线程运行于一个单独的全局上下文与线程中，会全局暴露一个 worker 对象。
Worker 线程与主线程之间的数据传输，双方使用 [Worker.postMessage()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/worker/worker-post-message/) 来发送数据，[Worker.onMessage()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/worker/worker-on-message) 来接收数据，传输的数据并不是直接共享，而是被复制的。
### 注意事项
1. Worker 最大并发数量限制为 1 个，创建下一个前请用 [Worker.terminate()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/worker/worker-terminate) 结束当前 `Worker`。
1. Worker 内代码只能 require 配置的 `Worker` 路径内的文件，无法引用其它路径文件。
1. Worker 内不支持`tt`系列的 API。
1. Worker 内不支持`globalThis`、`window`，返回值均为 `null`。
1. Worker 线程内支持 `console` 能力，目前仅支持 `info`、`log`、`debug`、`warn`、`error`。
1. 可以在 Worker 中使用 [TTWebAssembly ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/optimization/#ce7021f3)相关能力。
1. 可以在 worker 中使用定时器相关 API：[setTimeout](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/basic-function/timer/set-timeout)、[clearTimeout](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/basic-function/timer/clear-timeout)、[setInterval](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/basic-function/timer/set-interval)、[clearInterval](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/basic-function/timer/clear-interval)。

### 接口差异
小游戏环境下的 Worker 能力与主线程存在一定的差异，具体对比如下：

| 能力 | Worker | 主线程 |
| --- | --- | --- |
| 渲染能力 | 不支持 | 支持 |
| JS(tt) API | 不支持 | 支持 |
| 网络/IO | 不支持 | 支持 |
| 定时器 | 支持 | 支持 |
| TTWebAssembly | 支持 | 支持 |
