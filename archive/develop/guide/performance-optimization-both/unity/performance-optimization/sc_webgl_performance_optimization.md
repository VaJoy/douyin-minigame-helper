---
title: "性能优化总览"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/performance-optimization/sc_webgl_performance_optimization
update_time: 2025-05-27
---

> 文档说明：本文档描述小游戏研发的性能优化总览
> *了解更多：*[抖音Unity小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide)

## **为何需要进行性能优化？**
- 抖音小游戏天生为"即开即用"，在小游戏生态下玩家对启动耗时更敏感。减少启动耗时最明显的是减小首包资源的大小。
- 在主要分发平台-抖音中，视频是分发载体，游戏入口挂载在视频的锚点上，没有视频就没有用户。而游戏数据如下载阶段的获取效率、游戏时长等表现，会影响视频在推荐系统的评分。
- 如果使用webgl方案，底层基于WebAssembly，属于解释器中运行，性能是原生App的1/3。且Unity并未对WebGL平台做特别裁剪，构建物较大导致编译时间较长，启动较慢。所以需要进一步做性能优化。
## **优化目标**
根据平台在不同游戏类型/机型下的评测，我们给出Unity WebGL小游戏可以参照的的[性能评估标准](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/game-performance-standard) ，开发者依此对游戏的启动与运行性能进行调优。
## **最佳实践**
性能优化主要的4个方向：启动速度，资源加载，内存占用，减少cpu消耗
### **加快游戏启动速度**
- 构建选项中仅勾选首场景，其他场景用到时再下载
- 精简首场景物件，尽快渲染让玩家看到游戏首画面
- 减少代码包体, 剔除不必要的插件
- 使用代码分包工具缩减WebAssembly首次下载包体
- 减少初始化与首帧逻辑，首场景Awake/Start/首次Update不要包含过重逻辑
- CDN必须开启压缩

更多信息请参考：
- [提升Unity WebGL游戏启动速度](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/sc_webgl_start_speed)
- [Wasm分包工具说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/code-upload/sc_webgl_split)

### **资源按需加载**
- 使用 AssetBundle/Addressable/auto streaming 等资源管理方案，资源按需下载
- 检查各级 Resource 目录即 StreamingAssets 目录，避免非必要资源直接打包在首资源包内
- 单个ab的包体不推荐超过2MB；资源请求并发数不超过20个（经验值）
- 网络闲时可做一些预下载功能。
- 更多信息请阅读:
  - [资源按需加载概述](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc_webgl_load_overview)
  - [使用 Addressable 进行资源按需加载](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc_webgl_aa)
  - [使用 AssetBundle 进行资源按需加载](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc_webgl_ab)
#### 
### **降低小游戏内存使用**
- 不要初始化未使用的资源；及时释放不使用的资源
- 贴图maxsize尽量不超过1024，小游戏环境适当降低画质
- 贴图尽量不生成Mipmap
- 贴图尽量不使用可写属性
- 字体文件压缩前最大不超过4MB
- 音频资源尽可能勾选强制单声道

更多信息请阅读:
- [Unity_WebGL 运行时优化建议](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/running/sc_webgl_runtime_optimization)
- [优化Unity WebGL的内存](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/running/sc_webgl_memory_optimization)
- [Unity WebGL内存详解](https://mp.weixin.qq.com/s/sAf2OhZ1VkyiUU6aYB6C4w)
- [Unity小游戏开发攻略](https://mp.weixin.qq.com/s/fyasCiajuwNjMYMWaN7Jlw)
#### 
#### **降低CPU消耗**
- WebGL 方案使用代码分包，减少 JIT 的编译。
- 提前在Unity环境使用Unity Profiler发现问题
- 物理计算较重的游戏使用Fixed Timestep控制计算频率
- 在中低端机型限制帧率以减轻设备发热

更多信息请阅读:
- [Unity性能优化 — 动画模块](https://mp.weixin.qq.com/s/qgaDF4oNTbfF4Iw5L6Dy3Q)
- [Unity中文课堂 | 《Unity性能优化》系列课程](https://mp.weixin.qq.com/s/mxFSsoX085pcAox540525w)
