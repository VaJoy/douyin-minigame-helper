---
title: "优化Unity WebGL的渲染性能"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/running/sc_webgl_render_optimization
update_time: 2024-11-25
---

> 针对小游戏情况，可能存在较多中低端机型，因此对于渲染的优化非常必要，以下是几个可能会有帮助的建议

关于渲染的优化，可以参考官方
> https://docs.unity3d.com/cn/2019.3/Manual/MobileOptimizationPracticalRenderingOptimizations.html
> https://mp.weixin.qq.com/s?__biz=MzI3MzA2MzE5Nw==&mid=2668923519&idx=1&sn=2c0ac594cac7bd4a63333b4dd720a88f&chksm=f1c9260dc6beaf1bad287bb6c15f6dcb4d072fb509143bdd5adf0f7914c8bc605ead7727296a&scene=178&cur_album_id=1950061584714661889#rd
## 一. 渲染管线
### 1.1 Built-in 渲染管线
内置渲染管线功能较为全面，且各平台移植性强，但是相较于URP在图形质量和渲染特性上有所缺失，如对渲染没有太大的要求，内置渲染管线基本可以应对大多数情况，**适用小游戏**。
### 1.2 URP 渲染管线
针对URP渲染管线的优化可以参考官方的视频
[[Unity 教程]-URP中优化项目的7种方法](https://www.bilibili.com/video/BV1Ea4y1j7gu/?vd_source=fb1527df236e25eae03c3d9f35d0eb0f)

URP渲染管线是Unity官方提供的轻量级渲染管线，提供了良好的性能和平台移植性，同时支持自定义配置来选择启用或禁用某些渲染特性，**适用小游戏**。
但是对于小游戏而言，URP的许多高级渲染特性还是过于冗余，小游戏的体量无法承载如Fog，Motion_Vector，和一些高级的后处理效果等高消耗的渲染特性。一种优化方向是定制精简版的，适用于小游戏的URP渲染管线。
#### 1.2.1 定制URP渲染管线
针对小游戏情况，需要对渲染性能做尽可能的优化，而URP管线中许多复杂特性并不会在小游戏中应用，因此需要定制精简版的适合小游戏的URP管线。
### 1.3 HDRP 渲染管线
HDRP通常用于创建高质量的渲染效果，包括实时光线追踪，全局光照等，开销极大，**不适用小游戏**。
### 1.4 SRP 自定义渲染管线
SRP是一种可编程的渲染管线，它允许开发者根据项目需求自定义和扩展渲染管线的各个阶段，为项目提供更高的自定义性和可扩展性。需要注意的是，SRP的开发和配置相对复杂，需要一定的渲染编程知识和经验。因此，在选择SRP时，开发者需要权衡项目需求、开发资源和时间限制，**自行评估决定是否使用**。

## 二. 光照
光照是渲染中非常昂贵的一个环节，对于小游戏情况，应在大多数情况**避免使用光照相关功能**。
如果游戏中无法避免使用光照，需要做较大的取舍和精简，**尽量少使用实时光照**，对于shading，**尽量避免使用PBR-BRDF计算量较大的光照模型**。
为了尽可能保留渲染效果，通用的做法是，预计算相关的光照信息，如Light Map预计算光照信息存为一张纹理，在运行时采样纹理获取光照信息，或者基于预计算的实时全局光照Light Probe，通过预计算探针位置光照信息，在运行时对于需要光照信息的物体，插值计算距离最近的探针。预计算可以极大地减少运行时消耗，但是对于Light Map和Light Probe得到设置上仍然有很多可以优化的地方。
对光照的优化可以参考：
> https://developer.android.com/games/optimize/lighting-for-mobile-games-with-unity?hl=zh-cn#light-probes
### 2.1 Light Map
Light map的限制是只能应用于静态的物体和静态的光源。
Light Map的优化可以参考官方的文档
> https://unity.com/how-to/advanced/optimize-lighting-mobile-games
关于光照贴图烘焙各个参数详细解释，及合适的配置，可以参考
> https://zhuanlan.zhihu.com/p/157992819
几个通用的优化建议
- 设置较低的光照贴图的分辨率。
- 在Renderer组件的Lightmap Parameters选项中单独指定烘焙预设参数，建议使用较低配置。
### 2.2 Light Probe
- 尽可能的少放置探针，只在对光照要求比较高且光线变化密集的地方放置探针。只在对实时全局光照有要求的区域考虑放置探针。
对于光照探针的优化可以参考
> https://blog.unity.com/technology/static-lighting-with-light-probes
## 三. 阴影
和光照相似，阴影也是渲染中性能消耗较大的一环节，大多数游戏对于阴影的处理基本上都是另起一个额外的pass来渲染实时阴影。对于小游戏情况而言，**要做到尽可能避免实时计算**。
对于静态的物体，使用阴影贴图，对于动态的物体，选用基于shadowMap的开销相对较小的方案。
对于阴影方向的优化可以参考
> https://www.yisu.com/zixun/563323.html
针对小游戏情况，几个通用的阴影优化方向：
- 降低阴影分辨率和减少阴影投射距离，二者最终都可以减少阴影贴图的大小，从而减少渲染负载，具体参数的调配，可以参考官方关于参数的详细解释[阴影贴图 - Unity 手册](https://docs.unity3d.com/cn/2021.2/Manual/shadow-mapping.html)，[阴影距离 - Unity 手册](https://docs.unity3d.com/cn/2021.2/Manual/shadow-distance.html)。
- 增加阴影距离裁剪的范围，可以在摄像机组件上进行设置。
- 尽量采用阴影级联，相较于在整个阴影中使用高分辨率贴图，渲染开销大大降低了，但阴影级联的层数不宜过高，具体信息可以参考[Cascaded Shadow Maps - Win32 apps](https://learn.microsoft.com/en-us/windows/win32/dxtecharts/cascaded-shadow-maps)，Unity中具体阴影级联的参数解释可以参考[Unity - Manual: Shadow Cascades](https://docs.unity3d.com/2021.3/Documentation/Manual/shadow-cascades.html)
## 四 .shader代码优化
对于shader代码上的优化策略可以参考
> https://zhuanlan.zhihu.com/p/352910464
> https://www.khronos.org/opengl/wiki/GLSL_Optimizations
- 减少使用`if,else`，或者循环等可能会导致分支的代码，if 语句 可以尝试使用 step 内置函数替代，原因是分支可能会打断GPU并行。
- 尽可能使用低精度的浮点值，如 fixed/lowp 的计算速度是 float/highp 的四倍以上。
- 优先使用Swizzle，而非独立操作单个通道，合理运用Mul_Add以减少不必要的移动指令。
- 删除shader中没用到的关键字，避免生成不必要的着色体变体，详细可以参考[Declaring and using shader keywords in HLSL - Unity 手册](https://docs.unity3d.com/cn/2021.3/Manual/SL-MultipleProgramVariants.html)
