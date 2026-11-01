---
title: "使用方案及引擎选择建议"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/access-engine-advice/sc_engine_selection_suggestion
update_time: 2026-04-20
---

> 文档说明：本文档描述抖音Unity小游戏接入时方案的选择。
> *了解更多：*[抖音Unity小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide) 。

抖音Unity小游戏适配方案以WebAssembly为基础，理论上支持大多数的Unity版本。但由于部分性能优化项仅在Unity2021后才有。所以不推荐使用 Unity2021 前的版本。
## 推荐版本

| **引擎版本** | **压缩纹理格式** | **编译体积** | **已验证小版本** | **其他** |
| --- | --- | --- | --- | --- |
| 2021 | 支持ASTC | 80% | 2021.2.11~2021.3.33 | --- |
| 2022(推荐) | 支持ASTC | 80% | 2022.3.1~2022.3.14 | --- |
| 团结引擎(推荐) | 支持ASTC | 60~80% | 1.5.0 | 基于 Unity 2022，但包体、内存更多优化，支持 FrameDebugger 调试 |

> 如果项目已经上过微信，可以跳过以下内容，仅需适配抖音小游戏的[SDK](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk)，即可发布上线 [Unity小游戏发布](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_publish)

## 前置判断项
### **游戏包体大小改造可能性 **
> 在抖音下，游戏的分发是跟随视频的；如果游戏包体过大，取消率过高，会对视频的分发有负向价值，也影响用户体验。所以需要做小包化。 unity游戏，基于WebAssembly，天然要比JS小游戏的方案包体大，所以需要更多的优化工作。
用户可以**自行选择**小包化方案。如果包体已符合要求（压缩后 小于30M，优秀是6M），则可跳过
- 包体减小，主要在于对资源的分离，可选择的方案包括，**且不限于**
  - Unity 的AssetBundle按需下载
  - [Unity Addressable Asset system](https://docs.unity3d.com/Packages/com.unity.addressables@0.8/manual/index.html)
  - Unity 的 AutoStreaming 方案
- 如果代码过于庞大，导致wasm 过大，也会造成加载和编译时间过长，那要根据实际情况进行评估是否能够删减。
### **游戏逻辑改造的可能性 **
> 不同的方案，对引擎版本，所用插件有一定限制，考虑项目代码层面改造的可能性
- 支持托管类型的dll插件、C#源码插件，**不支持**非托管类型（如C++编译的）dll/so。项目依赖的**必要**插件有Android/iOS平台相关插件或so/framework原生插件，无法转换。
- 性能有限，如果项目中有较多密集运算，物理模拟，脚本，可能要做降级优化。
- iOS下内存受限，如果项目中有较大的贴图，模型，可能要做降级优化。

### 功能项评估
游戏重要的能力支持情况如下：

| 能力 | 是否支持 | 解决方案 |
| --- | --- | --- |
| Unity基础模块 | 支持 | 支持动画、物理、AI、UI等基础模块 |
| 渲染管线与接口 | 支持 | 支持标准渲染管线、URP，WebGL2.0已支持 |
| 资源加载 | 支持 | Addressable、AssetBundle网络异步加载 |
| Lua脚本 | 支持 | 支持标准Lua与常见binding(如xlua, tolua等)， 不支持Luajit。需根据实际游戏在真机验证性能。游戏更新原则上要走平台的审核流程。 |
| PuerTS | 支持 | iOS系统需14.5以上, 支持JIT，但目前不支持import，js代码要放到jslib中。游戏更新原则上要走平台的审核流程。 |
| Unity音频 | 支持 | Unity Audio基本能力支持，支持fmod插件，不支持wwise。直接使用unity的音频组件即可。 |
| 第三方插件 | 部分支持 | 支持大部分插件，C#插件与非平台相关的C原生插件（以源码方式存在的） |
| 网络系统 | 需调整 | 不支持[System.Net](http://system.net/)接口，HTTP使用UnityWebRequest，WebSocket通信替代(如开源的UnityWebSocket插件)，UDP/TCP使用TT SDK适配 |
| 多线程 | 不支持 | 删除多线程用法，使用异步等其他替代方式 |
| 文件系统 | 需调整 | 理论上支持System.File，但会有内存和加载慢问题。后续会禁止使用。应使用抖音小游戏TT SDK实现文件存储，大小限制为最大1G，适配插件已实现资源的自动缓存与更新 |

## 支持的宿主现状
当前支持抖音、抖音极速版、抖音火山版、番茄小说、红果短剧，**后续将逐步开放其他合作方宿主能力。**

## QA
- 原有的Native方案是否还支持？
  - Native方案推出较早，虽有性能优势，但无法支持iOS系统。随着WebGL方案的成熟，Native方案会计划逐步放弃支持，短期**不会**下线发布功能，后期仅在特定场景下支持接入，对于新接入的游戏优先推荐使用WebGL方案。
  - 当前Native方案仅支持 2021.3.14f1， 2022.3.34f1以及团结引擎1.1.4版本。后期不会再新增引擎的支持。
  - Unity InstantGame 方案同Native方案类似，仅支持特定版本，仅支持Android，预计之后不会有更新。会在**24年内**根据情况下线发布功能。
- 项目使用2021以前的版本，是否能支持使用？
  - 2021 对WebGL方案做了较多优化，支持astc，在iOS的内存方面有明显的优势。编译速度快，编译体积小，利于启动速度和运行内存。建议升级到2021后版本。
- WebGL 方案对团结引擎支持情况？
  - 团结引擎 1.5.0 开始内置支持抖音小游戏的 BuildProfile，请参考团结引擎手册[抖音平台支持](https://docs.unity.cn/cn/tuanjiemanual/Manual/Douyin.html)页面。
