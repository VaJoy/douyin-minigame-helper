---
title: "提升Unity WebGL游戏启动速度"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/startup/sc_webgl_start_speed
update_time: 2025-06-11
---

> 此文档描述如何提升webgl游戏启动速度
> 更多详情见[Unity WebGL 字节小游戏适配方案](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/sc_webgl_overall)

## **为什么要做启动优化**
### **小游戏与手游App的启动差异**
抖音小游戏具有“即开即用“的特性，玩家在下载时只能被动等待，对于启动时长更为敏感，过长的启动时间将导致用户显著流失，从而降低分发效率。
### **优化的目标与标准**
目前普通小游戏普遍启动时间为5~6s，而如果不经优化的Unity WebGL游戏启动时间在20s以上。建议开发者将启动优化作为上线前**关键**事项。经过优化的游戏可以达到 10s。
## **分析小游戏启动速度**
### **查看启动耗时**
游戏在测试环境中进入时，会弹窗显示游戏启动阶段耗时

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/09af62782d20493eaf2ad4edef79df15)

要知道各个阶段的含义，我们必要理解[启动流程](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/sc_webgl_start_progress)
小游戏启动主要由三部分影响：
> 1. 首包资源下载
> 1. wasm代码下载和编译
> 1. 引擎初始化与开发者首帧逻辑
**建议首屏启动时间控制在5~10s甚至更短**。
### **分阶段耗时**
#### **首资源包下载与体积**
首包资源主要有以下组成：
- 代码部分
  - wasm代码：C#代码使用il2cpp生成cpp代码生成的类，方法等信息，再转成wasm代码
  - wasm分包：如果使用了wasm分包，则会包含子包内容（仅Android，iOS通过其他方式下载）
  - wasm胶水代码
- 资源部分
  - unity default resources文件，引擎默认资源，如Arial字体，默认mesh，纹理等
  - unity_builtin_extra
  - Always-included Shaders
  - BuildSettings中所有active的场景
  - Resources文件夹中的资源，以及其中的资源引用到的其他资源
  - 全局设置及引用到的资源，如splash图片等
- 其他配置
  - Unity小游戏配置文件
  - StreamingAssets中部分文件
下列首包资源中webgl开头的文件会通过brotli压缩格式进行压缩：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2178a2eceb17466aab9a5010976dc032)

当首资源包发生变化时，小游戏在启动阶段会重新下载新资源，因此文件大小极为影响游戏的启动速度。
> 1. 网络条件绝大部分为wifi或4G
> 1. 玩家平均下载速度约2MB/s
> 1. 用户存在不少<300KB/s的低网速玩家
> 1. 中文显示需要自定义字体，打包在首资源包或Bundle。**请尽量使用2~3MB以内的精简字体以免影响游戏启动速度**

#### wasm**代码编译**
wasm分包的大小会直接影响代码下载时长以及程序初始化编译的时间，关于wasm代码对启动速度的影响，开发者需要注意：
> 1. 转换工具会将Unity WebGL包自动进行br压缩(压缩至原code包的20%)
> 1. wasm代码下载会随首包资源一起下载
> 1. wasm编译需要CPU资源，对于低端机来说编译时间会较长
**关于代码包的建议如下：**
1. 生成的**原始代码不超过30MB**（Build/webgl_package目录下code.unitywebl文件）
1. 勾选`Strip Engine Code`并设置`Managed Stripping Level`为`High`
1. 使用[代码分包工具](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/code-upload/sc_webgl_split)，减少wasm首包大小，会大大降低编译时间
1. 如果使用Unity2021以上版本，可更改PlayerSettings面板IL2CPP选项为更小尺寸(SIZE)以减少函数量。

#### **引擎初始化与开发者首帧逻辑**
游戏启动阶段耗弹窗显示时即为引擎初始化与开发者首帧逻辑，关于该阶段耗时，开发者需要注意的是：
> 1. MonoBehaviour 脚本的首帧 Start/Awake 方法应尽量少包含逻辑，优先呈现画面
> 1. 初始场景应避免过大，通常呈现 Splash 场景即可
> 1. 初始场景中需要后续主场景或配置加载时可采取分帧策略，切勿在Start/Awake阻塞。

#### **游戏内资源按需加载**
前面我们提到开发者需要将资源从首包分离以较少首屏加载时间，同理，而对于其余的资源开发者推荐使用按需加载的方式进行加载，减少玩家进行核心玩法的等待时间。 优化可参考使用 [Addressable Assets](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc_webgl_aa)或[AssetBundle](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc_webgl_ab)进行资源按需加载。

### **优化总览**
我们总结启动时序及开发者与平台提升启动性能的优化事项如下：

## **常用启动优化技巧**
- [资源按需加载概述](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc_webgl_load_overview)
- [使用 Addressable 进行资源按需加载](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc_webgl_aa)
## **常用启动优化工具**
### **AssetStudio(推荐)**
[https://github.com/Perfare/AssetStudio](https://github.com/Perfare/AssetStudio)
一款开源的资源查看工具，可以检查 data 首包以及 AssetBundle(或新 Addressable)的资源内容，对于分析打包资源正确性和冗余问题具有很好的帮助。
### **BuildReportTool(推荐)**
[https://assetstore.unity.com/packages/tools/utilities/build-report-tool-8162?locale=zh-CN](https://assetstore.unity.com/packages/tools/utilities/build-report-tool-8162?locale=zh-CN)
一个很好的前端工具，用于查看 Unity 编译信息，BRT 显示了编译时包含的每个资源占用的存储空间及未使用资源情况。
### ** Asset Hunter**
[https://assetstore.unity.com/packages/tools/utilities/asset-hunter-pro-135296](https://assetstore.unity.com/packages/tools/utilities/asset-hunter-pro-135296)
资源清理插件，可清理项目中的无用资源。
### ** Unity Addressable Assets System**
[https://docs.unity3d.com/Packages/com.unity.addressables@1.16/manual/index.html](https://docs.unity3d.com/Packages/com.unity.addressables@1.16/manual/index.html) Unity全新资源管理流程
