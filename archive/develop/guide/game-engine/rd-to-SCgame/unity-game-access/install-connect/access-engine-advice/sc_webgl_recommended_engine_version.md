---
title: "推荐的引擎版本"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/access-engine-advice/sc_webgl_recommended_engine_version
update_time: 2025-04-15
---

> 此文档描述开发时引擎版本选择的问题。
> 更多详情见 [接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide)

## **推荐引擎版本**
  使用引擎版本首先确定使用了哪个方案： [使用方案及引擎选择建议](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_engine_selection_suggestion)
- 对于 Native 方案，目前仅支持 2021.3.14f1(c1) 及 2022.3.34f1(c1) 版本；
- 对于 WebGL 方案，对引擎版本支持比较宽泛，选择可参考以下建议。

> **以下内容仅针对 WebGL 方案。**

### **版本兼容性**
Unity WebGL 适配方案是以 WebAssembly 技术为基础，理论上工具支持的 Unity 版本涵盖 2018 之后的所有版本。
但 Unity 2021 之后的版本针对 WebGL 有大量的优化，如增加了对 ASTC 纹理压缩的支持、对音频的压缩等。
所以我们仅**推荐使用 2021 之后的版本，或中国特供版针对性优化的版本**。
并非每个小版本我们都有足够的验证，我们会根据实测情况以及开发者反馈的情况给出建议。

### **推荐版本**

| **引擎版本** | **压缩纹理** | **编译体积** | **已验证小版本** | **其他说明** |
| --- | --- | --- | --- | --- |
| 2020 | 支持DXT/ETC2，不支持ASTC | 100% | 2020.3.1~2020.3.36 | **不推荐** |
| 2021 | 全支持 DXT/ETC2/ASTC | 80% | 2021.3.14 | --- |
| 2022 | 全支持 DXT/ETC2/ASTC | 80% | 2022.3.23 | 仅支持抖音 |
| 团结引擎 | 全支持 DXT/ETC2/ASTC | 60%～80% | 1.5.0 | 1.5.0 开始内置支持抖音小游戏打包，仅支持抖音 |

**备注：**
- 标注为「仅支持抖音」的版本暂时仅可在抖音/抖音极速版中打开，提审上线时请勿勾选今日头条、番茄小说等不支持的宿主以免审核失败。
- Unity 引擎在早期版本如5.x已提供 WebGL 平台导出模式，但主要针对PC浏览器，稳定性和性能无法达到标准，不推荐使用早期版本。
- Unity 2021 开始支持更多特性，如更全的压缩纹理、压缩音频、更快的编译速度与更小的体积，强烈建议。
- [Unity Profiler 内存分析](https://docs.unity.cn/cn/tuanjiemanual/Manual/Memory-Profiler.html)、[AutoStreaming](https://docs.unity.cn/cn/tuanjiemanual/Manual/AutoStreamingLoad.html) 等功能，如有条件尽可能使用。
- 字节没有针对老版本提供压缩纹理等工具，建议使用2021之后的引擎版本。

## **Q&A**
1. 团结引擎相对于其他版本有哪些特别之处？
  团结引擎是 Unity 中国基于 Unity 2022 LTS 定制的引擎，针对小游戏平台提供了引擎轻量化、运行时内存优化、FrameDebugger 真机调试等能力。
  团结引擎 1.5.0 及以上版本内置了抖音小游戏 SDK 下载和打包能力，可参考团结引擎手册[抖音平台支持](https://docs.unity.cn/cn/tuanjiemanual/Manual/Douyin.html)页面使用。抖音小游戏暂不支持团结引擎的 .Net 8 (DotNet Wasm) 方案。
1. Unity 引擎版本是越新越好吗？
  不是，新版本的 Unity 如果发生一些代码逻辑上的变动，需要对 Unity 导出的 js 胶水代码重新进行适配，可能我们无法实时跟进，一般会针对 LTS 版本进行适配，所以建议尽量使用稳定的 LTS 版本。
