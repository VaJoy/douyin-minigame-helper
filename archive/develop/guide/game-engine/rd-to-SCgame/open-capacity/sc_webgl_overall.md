---
title: "WebGL适配方案"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/sc_webgl_overall
update_time: 2024-12-11
---

> 欢迎使用 Unity WebGL 小游戏适配(转换)方案，本方案设计目的是**降低 Unity 游戏上线到抖音小游戏的研发成本**。基于WebAssembly技术，将原有Unity游戏项目在WebGL平台下的构建产物适配到抖音小游戏。

## **方案特点**

---

- 抖音开放平台能力，如广告，支付，分享，关注抖音号等，以C# SDK方式提供给开发者，快速对接
- 保持Unity开发习惯，工具链及技术栈，无需重写游戏核心逻辑。
- 支持第三方纯C#插件；支持webgl平台的插件；支持JS插件

## **转换案例**

**狂点大作战**
`模拟经营`
> 打开抖音扫码，即刻进入游戏

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/8cdccdd30d2b41c5a024fc25a84453d0)

**球球旅行记**
`模拟经营`
> 打开抖音扫码，即刻进入游戏

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/136793257269478dace43abfcf6a6d15)

**蓝猫机甲狂潮**
`休闲对战`
> 打开抖音扫码，即刻进入游戏

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/7bda3425c21444b9b41fae44f7f0d2b5)

更多转换案例-->[抖音Unity小游戏转换案例](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_translation_case)

## **安装与使用**

---

1. 选择[推荐引擎版本](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/overview-and-compatibility/sc_webgl_recommended_engine_version)，安装Unity引擎，安装WebGL组件
1. [下载Unity插件](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk)，并导入至游戏项目中
1. [创建Unity小游戏项目](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide#0ed0fed7)，在抖音开放平台创建项目
1. 下载接入Demo，查看SDK使用方法。
1. 跑起来测试一下，进行项目的调优。
## **文档总览**

---

[抖音Unity小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide)
[Unity小游戏WebGL方案接入流程](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/overview-and-compatibility/sc_webgl_access_flow)
### **方案概述与兼容性**
[技术原理](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/overview-and-compatibility/sc_webgl_overview)
[兼容性评估](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/overview-and-compatibility/sc_webgl_compatibility)
[推荐引擎版本](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/overview-and-compatibility/sc_webgl_recommended_engine_version)
[更多转换案例](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_translation_case)
[常见问题FAQ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_faq)
### **性能优化**
[WebGL方案优化建议](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/sc_webgl_optimization_suggestion)
[性能优化总览](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/sc_webgl_performance_optimization)[ ](https://github.com/wechat-miniprogram/minigame-unity-webgl-transform/blob/main/Design/PerfOptimization.md)
[性能评估标准](- https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/game-performance-standard)
#### **启动性能 **

> **启动性能核心是减少首次下载的资源和代码**

[启动性能优化指南](- https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/startup-performance/startup-performance-guide)
[提升Unity WebGL游戏启动速度](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/sc_webgl_start_speed)
##### **资源加载优化**
- [资源按需加载概述](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc_webgl_load_overview)
- [使用 TTAssetBundle 优化内存](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc-webgl-tt-ab)
- [使用 Addressable 进行资源按需加载](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc_webgl_aa)
- [使用 AssetBundle 进行资源按需加载](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc_webgl_ab)
##### **代码加载优化**
[Wasm分包工具说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/code-upload/sc_webgl_split)
##### **体验优化和数据监控**
[定制启动封面](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/experience-and-data/sc_webgl_loading_page)
#### **运行性能 **
[Unity_WebGL 运行时优化建议](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/running/sc_webgl_runtime_optimization)
[优化Unity WebGL的内存](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/running/sc_webgl_memory_optimization)
[优化Unity WebGL的渲染性能](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/running/sc_webgl_render_optimization)
[WebGL2.0渲染支持说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/running/sc_webgl_2)
[使用新文件系统说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_new_file_system)
### **版本更新与资源部署**
[小游戏资源部署与缓存](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/changelog-and-resource/sc_webgl_resource)
[资源缓存](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/changelog-and-resource/sc_webgl_resource_cache)
[小游戏版本更新](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/changelog-and-resource/sc_webgl_version_update)
### **能力适配**
[抖音Unity小游戏C# SDK接口文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk)
[加载外部js文件的支持](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_load_js)
[使用新文件系统说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_new_file_system)
[屏幕适配](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_screen)
[输入法适配](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_keyboard)
[后端服务指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_server_guide)
[网络通信适配](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_network)
### **问题反馈 **
[问题反馈与联系我们](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/faq/sc_feedback)
