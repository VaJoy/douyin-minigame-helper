---
title: "WebGL方案兼容性评估"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/access-engine-advice/sc_webgl_compatibility
update_time: 2024-11-25
---

> 文档说明：本文档描述抖音Unity小游戏WebGL方案接入说明与兼容性评估。
> *了解更多：*[抖音Unity小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide)** **

## 支持引擎版本
建议使用Unity 2021及以上版本，有很多针对WebGL方案的优化
## 运行环境与性能限制
- Android 基于v8，[Android WebGL2.0支持](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/android-webgl2)。
- iOS上对标微信高性能模式，在iOS 15.0后版本支持WebGL 2.0。支持JIT
- 不支持多线程
- 性能大概是Native的 **1/3**
- 在iOS上内存很受限制，代码分包是必要优化 [Wasm分包工具说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/code-upload/sc_webgl_split)

建议先将游戏导出为WebGL在手机浏览器上运行，性能和兼容性可以接受，再使用本方案
如果在Android上性能无法达标，可以在Android平台使用native方案，流畅性有极大的提高
## 功能支持

| **功能** | **是否支持** | **解决方案** |
| --- | --- | --- |
| Unity基础功能 | 支持 | 基于webgl，引擎基础功能都支持。 |
| 渲染管线 | 部分支持 | 支持标准渲染管线、URP。 依赖WebGL2.0的特性iOS已支持，[Android WebGL2.0支持](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/android-webgl2)。 |
| 第三方插件 | 部分支持 | 支持托管类型的dll插件、C#源码插件，不支持非托管类型（如C++编译的）dll |
| 热更方案 Lua PuerTS | 政策不支持 LUA/ILRuntime等热更方案在Unity WebGL性能急剧下降 | 小游戏环境中**不允许**使用热更方案，包括xlua，ilruntime，puerts等。原因： 小游戏运营策略不允许动态变更代码，包括热更 如果是运营引入游戏，已使用了大量脚本，向对接运营备案后使用，但不允许线上发布热更。 |
| 协程/async/await | 支持 |  |
| 多线程 | 不支持 | 改用异步等其他方式实现 |
| 网络接口 | 需调整 | 不支持 [System.Net](https://learn.microsoft.com/en-us/dotnet/api/system.net) 接口，参考 [网络通信适配](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_network) 调整。 HTTP：使用 UnityWebRequest。 TCP：需替换成 WebSocket。可以使用 [UnityWebSocket](https://github.com/jirihybek/unity-websocket-webgl)。 UDP：需替换成 StarkSDK 提供的接口。 |

## 想用WebGL方案上iOS
  先考虑清楚：优化的不好，用户的加载时长高，取消率高，使用时长短，可能对整体分发（包括android用户）有负向效果
  当前ios系统限制，对性能要求较高。为了用户更好的体验，**所以对iPhone XR以下机型没有打开可见性入口**
  ios上的录屏功能会有权限申请，还有性能消耗，**不建议使用**。一定要使用，dau达到10w后，跟平台运营同学联系开白名单。（**平台只要求android上要录屏分享**）
## 性能优化
[抖音小游戏 Unity WebGL 适配方案](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/sc_webgl_overall)
[WebGL方案优化建议](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/sc_webgl_optimization_suggestion)

## FAQ
Q：WebGL在iOS15.4版本下无法正常运行的问题：
A：该问题为 Unity 与 iOS 15.4 的 BUG，推荐使用我们提供的 WebGL[分包工具](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/code-upload/sc_webgl_split)或采用Unity WebGL官方论坛的修复方案:
https://forum.unity.com/threads/ios-15-webgl-2-issue.1176116/page-2
