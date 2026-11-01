---
title: "WebGL适配方案概述"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/overview-and-compatibility/sc_webgl_overview
update_time: 2024-11-25
---

## **一、技术原理**
### **Unity WebGL是什么**
#### WebGL 简介
  WebGL（Web Graphics Library）是一种能够将 JavsScript 和 OpenGL ES 结合在一起的一种 3D 绘图标准。能够通过 HTML5 的 Canvas 来和 DOM API 相结合来完成图形渲染，而且不需要安装任何插件就可以在浏览器中运行。
#### Unity WebGL
  Unity 主要利用 WebGL 技术，能够将游戏工程代码和资源内容使用 WebGL 选项构建，构建出可以在浏览器中运行的Web应用程序，这些程序可以使用HTML5、JavaScript以及WebGL技术在网页中进行呈现。
### **技术概述**
要能够在浏览器中运行 WebGL 应用程序，所有代码都需要是浏览器可以支持的标准语言。Unity 使用 [Emscripten](https://emscripten.org/) 编译器工具链将 Unity 引擎导出的代码（用 C 和 C++ 编写）编译成 WebAssembly（wasm），并结合 JavaScript 代码来执行。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a901266abd474eb986b35d593475aec8)

对于一个基于 Unity 引擎编写的游戏工程，游戏代码（C# 脚本）最终会被编译为 DLL 文件，Unity 利用其 [<u>IL2CPP</u>](https://docs.unity3d.com/cn/2018.4/Manual/IL2CPP.html) 技术，将 DLL 文件转换为 C++ 源文件，然后使用 Emscripten 编译工具链将 C++ 代码编译并转换为 wasm 文件，转换得到的 wasm 代码文件能够直接在浏览器中执行。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d4dda204c0144c2093f41ee900165cab)

#### **技术限制**
并非所有Unity功能都可用于WebGL方案，主要是由于一些技术的限制：
- 不支持多线程：由于JavaScript中缺少线程支持，因此不支持线程。在 Unity 内部使用线程来加速性能以及在脚本代码和托管的 dll 中使用线程都是不受支持的。实质上不支持 `System.Threading` 命名空间中的任何内容。
- 无法断点调试：无法在 Visual Studio 等IDE中直接调试运行 WebGL 应用程序。
- WebGL 图形 API 等效于 OpenGL ES 2.0 和 3.0，存在一些限制。请参阅：[<u>WebGL 图形</u>](https://docs.unity3d.com/cn/2018.4/Manual/webgl-graphics.html)。
### 平台适配
为了能够让导出包在字节系APP下运行，并使用平台能力，我们提供了以下支持：
- 开发阶段：提供平台能力的Unity C# SDK接口，帮助开发者快速对接平台能力；
- 构建阶段：提供StarkSDK Unity Tool构建工具，一键构建 WebGL应用程序、并进行 JS 胶水层代码配；提供游戏打包和发布工具；
- 调试阶段：提供本地调试工具，在真机进行调试；
- 运行阶段，提供wasm运行能力，图像渲染能力，以及提供JS接口支持与底层宿主的交互。
#### 业务逻辑与架构

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/22241885e84e47789be19f57d689a066)

#### 运行环境
- Android下基于v8引擎及内部渲染引擎；
- iOS下基于WKWebView运行环境，即跟微信一样的**高性能模式**运行；
- 两种系统环境下，wasm 执行都是 JIT 代码。但由于底层虚拟机差异过大以及自身不断迭代，难以横向对比。

## **二、接入流程**
接入流程请参考文档 [抖音Unity小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide)

## **三、参考资料**
1. [https://emscripten.org/](https://emscripten.org/)
1. [https://docs.unity3d.com/Manual/webgl-gettingstarted.html](https://docs.unity3d.com/Manual/webgl-gettingstarted.html)
1. [https://forum.unity.com/forums/webgl.84/](https://forum.unity.com/forums/webgl.84/)
1. [https://webassembly.org/getting-started/developers-guide/](https://webassembly.org/getting-started/developers-guide/)
1. [https://developer.mozilla.org/zh-CN/docs/WebAssembly/C_to_wasm](https://developer.mozilla.org/zh-CN/docs/WebAssembly/C_to_wasm)
