---
title: "EmscriptenGLX 渲染模式"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/running/emscriptenglx
update_time: 2026-09-07
---

## 简介
EmscriptenGLX 是抖音小游戏平台推出的专项性能优化工具，其核心目标在于解决 WASM 与 JavaScript 之间因渲染指令转发而产生的高频通信开销，通过优化底层调用链路，显著提升游戏在小游戏环境中的运行帧率与渲染效率。适用于所有使用 Emscripten 将 C++ 编译为 WASM 并在小游戏平台运行的游戏。对于 Unity/团结引擎而言，当前仅支持 Unity 新包体格式，接入只需要勾选一项配置即可。

## 背景
在抖音小游戏环境中，所有图形渲染最终都需通过平台提供的 WebGL/WebGL2 接口执行。对于不同技术栈开发的游戏，其渲染指令的调用路径存在差异：
- **JavaScript 原生游戏**：调用路径为 `JavaScript (业务逻辑)` → `平台 WebGL 接口` → `GPU`，链路相对直接。
- **WASM 编译型游戏**：传统的适配方案下，调用路径为 `WASM (C++/Unity 逻辑)` → `JS 胶水层` → `平台 WebGL 接口` → `GPU`。
在第二种模式下，“JS 胶水层”扮演着关键的翻译角色。它负责将 Emscripten 从 C/C++ 的 GL/EGL 调用转换成浏览器兼容的 WebGL 调用。然而，对于每一帧都包含成千上万次 GL 调用的重度游戏而言，WASM 与 JavaScript 之间这种高频、密集的跨语言调用会构成显著的性能瓶颈，尤其是在中低端设备上表现更为明显。
因此，为了突破这一瓶颈，我们推出了 EmscriptenGLX 能力，旨在为 WASM 游戏提供一条更高效的渲染“快车道”。通过 EmscriptenGLX 模式，可以将原先 `JS 胶水层` 中的图形调用转换逻辑下沉至 `WASM` 中，将每帧成千上万次跨语言通信减少为个位数，从而显著提升图形渲染效率。

## 性能收益

| 优化类别 | 优化收益 |
| --- | --- |
| 帧耗时 | **降低 5%～15%（跟游戏渲染复杂度相关）** |

从当前的游戏测试情况来看，不同的游戏性能优化收益有差别，通常在渲染越重度的游戏中收益越明显，特别是在中低端设备上。

## 技术原理
在原先的模式下，图形 API 每次调用都会产生一次从 WASM 向 JavaScript 的跨语言调用，而每帧的图形调用次数多了之后，跨语言的高频调用最终会成为性能瓶颈。而在新的 EmscriptenGLX 模式下，图形 API 调用的胶水层转化逻辑在 WASM 内置执行，而每帧需要跨语言调用的次数大大减少，从而显著提升渲染效率：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/4bd7ed7125654d5c8a2e8beccfdba4ce~tplv-9nona0m7ha-image.image)

## 接入流程
### 前提条件
- TTSDK 版本 >= 6.9.3；
- iOS 确保抖音 app 版本 >= 38.3.0，低版本会自动降级为原先的渲染模式；
- Android 确保抖音 app 版本 >= 39.9.0，低版本会自动降级为原先的渲染模式；
- 鸿蒙的支持还在进行中，目前鸿蒙系统会自动降级为原先的渲染模式；
- iOS 仅支持在 iOS >= 14 的机型上运行，低版本 iOS 系统会自动降级为原先的渲染模式；
- iOS 当前仅支持 WebGL 高性能+ 模式，其余模式会自动降级为原先的渲染模式；
- Unity 请确保已开启新包体格式，并确保已在原先的模式下做好了新包体格式的适配；

### SDK 配置
如果用的是 Unity 引擎，请确保勾选了“开启高性能+ 模式”，并且勾选启用 EmscriptenGLX 即可（会自动取消旧包体格式的勾选项）：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/211185e8a1d843d79442dd175833bc66~tplv-9nona0m7ha-image.image)

如果用的是团结引擎，请确保勾选了“开启高性能+ 模式”，并且勾选启用 EmscriptenGLX 即可（旧包体格式即便勾选了也会强行使用新包体格式）：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/52f290301e2c4027884ec25befe9e062~tplv-9nona0m7ha-image.image)

## 注意事项
如果开启了 WASM 分包，请基于 EmscriptenGLX 模式下进行完善的分包函数收集（善用增量收集能力），如果先前未进行过非 EmscriptenGLX 模式下的分包函数收集，则可在不重新构建的情况下，在开发者 IDE 中取消“高性能+ 模式”选项，进行兜底模式的分包函数再收集；

## FAQ
### Q1. 如何判断已开启 EmscriptenGLX？
如何判断是否**支持** EmscriptenGLX：看日志中是否存在“Support EmscriptenGLX: true”：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/d71dd9a084b4475a91b2dde40cf24bd0~tplv-9nona0m7ha-image.image)

如何判断是否**启用** EmscriptenGLX：在“Creating WebGL 1.0/2.0 context”之后，紧接着有 `Initializing EmscriptenGLX` 和 `EmscriptenGLX initialized.` 这两条日志：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/1a0d78a3ac9c4d4892920f22bab599cb~tplv-9nona0m7ha-image.image)

### Q2. 在老版本抖音，或不支持的设备上会有什么表现？
EmscriptenGLX 仅在抖音 iOS 版本 >= 38.3.0、Android 版本 >= 39.9.0 上支持，在老版本的抖音、iOS 系统版本小于 14、未启用高性能+ 模式等情况下，都会自动降级回未开启 EmscriptenGLX 时的表现。

### Q3. 开启 EmscriptenGLX 之后性能反而变差了？
1）核查当前场景是否启用了 WASM 分包能力；
2）验证分包逻辑的生效范围，确认是否仅在 WebGL 模式下执行分包操作，EmscriptenGLX 模式下未进行过分包收集；
3）若上述排查排除分包问题，则判定大概率是 EmscriptenGLX 方案的适配问题，建议与我方团队联系，一起排查问题。

### Q4. 自研引擎如何接入 EmscriptenGLX？
当前暂时只支持 Unity 和团结引擎，自研引擎暂不提供接入支持。

## 联系我们
如有任何问题请咨询平台对接人。
