---
title: "Unity WebGL 运行时优化建议"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/running/sc_webgl_runtime_optimization
update_time: 2025-06-17
---

> Unity WebGL使用 [<u>IL2CPP</u>](https://docs.unity3d.com/cn/2019.4/Manual/IL2CPP.html) 的技术，接受 .NET 字节码(C#脚本)并将其转换为相应的 C++ 源文件，然后使用 [<u>emscripten</u>](https://kripken.github.io/emscripten-site/) 编译器工具链将C++代码编译为 wasm 文件，wasm文件能够直接在浏览器环境中运行。
> 由于Unity WebGL最终运行在虚拟机环境里，且目前**不支持多线程**，测试发现Unity WebGL方案的性能是原生的**1/3**左右，因此针对Unity WebGL方案的优化非常重要。

> 开发者应对Unity WebGL方案做出优化，以达到可以接受的流畅度标准和性能要求，具体的指标及性能基线可以参考[性能评估标准](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/game-performance-standard)

下面给出一些常用的运行时优化建议

## 一. 配置相关
### 1.1 物理
物理相关优化可以参考
> [Performance optimization tips](https://www.youtube.com/watch?v=pTz3LMQpvfA)
> [Unity性能优化 — 物理模块](https://mp.weixin.qq.com/s?__biz=MzI3MzA2MzE5Nw==&mid=2668923519&idx=1&sn=2c0ac594cac7bd4a63333b4dd720a88f&chksm=f1c9260dc6beaf1bad287bb6c15f6dcb4d072fb509143bdd5adf0f7914c8bc605ead7727296a&scene=178&cur_album_id=1950061584714661889#rd)
#### 1.1.1 小建议
以下是几个可以快速提升物理性能的建议：
##### **手动关闭物理模块**
如果游戏中没有使用到物理模块，应关闭Auto Simulation选项，该选项默认开启，会导致不必要的性能浪费。
> Edit->Project Settings->Physics->Auto Simulation
##### 
![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/3b035f243d954ec3a3f0cf11b671dbb0)

**调整物理计算频率**
在Unity自带的物理引擎中，物理模块运行在`FixedUpdate.PhysicsFixedUpdate`中，`FixedUpdate`的时间间隔也代表这物理模块的时间间隔
> Edit->Project Setting->Time
##### 
![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2ba7c1558d7e40b98795a2ec5ec88246)

- Fixed Timestep：决定了FixedUpdate的更新间隔，该值越大，则间隔越大
- Maximum Allow Timestep: 该值会对FixedUpdate的执行此时进行限制
适当调整Fixed Timestep与 Maximum Allowed Timestep降低计算频率
**选用合适的碰撞体类型**
对于物理碰撞精度要求不高时，可以考虑选用开销较低的碰撞体类型，以下是各种常用碰撞体的开销排序
`sphere Collider(最低)`
`capsule Collider`
`box Collider`
`Mesh Collider(开销最大，且远大于前3种)`
#### 1.1.2 性能分析与调试
- 关于物理模块性能分析可以选择Unity内置Profiler
> Window->Analysis->Profiler

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/5676da0412684726bc196b709e88c3fa)

参数细节可见文档
https://docs.unity3d.com/2021.3/Documentation/Manual/ProfilerPhysics.html
- **物理调试可以选择**
> Window->Analysis->Physics Debugger

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d4d196442fcb4d5a8674066b9782a021)

参数细节和使用相关可以参考
https://docs.unity3d.com/2021.3/Documentation/Manual/PhysicsDebugVisualization.html
https://learn.unity.com/tutorial/using-the-physics-debugger-2019-3#

### 1.2 UI
关于UI的优化可以参考
> https://www.youtube.com/watch?v=EK8sX8oCQbw
> Unity官方的优化建议，从[12:46](https://youtu.be/EK8sX8oCQbw?t=766)开始介绍UI模块的优化
> https://learn.unity.com/tutorial/optimizing-unity-ui#5c7f8528edbc2a002053b5a1
> https://mp.weixin.qq.com/s?__biz=MzI3MzA2MzE5Nw==&mid=2668924034&idx=1&sn=7887d7b8ca3e1b303db41d338d753755&chksm=f1c920f0c6bea9e6ee2fda67181a41d52d486a0eff1d6109b17324f856107c48f25be21f2a53&cur_album_id=1950061584714661889&scene=190#rd
#### 1.2.1 使用图集
sprite Atlas是一个图集打包工具，使用Sprite Atlas
- 减少drawcall
- 减少包体大小
- 减少图片运行时的加载时间
如果游戏中大量使用2DSprite，可以考虑使用([Unity - Scripting API: SpriteAtlas](https://docs.unity3d.com/2021.3/Documentation/ScriptReference/U2D.SpriteAtlas.html))，可以参考[Introduction to the Sprite Atlas - Unity Learn](https://learn.unity.com/tutorial/introduction-to-the-sprite-atlas#)
#### 1.2.2 合批与Canvas重建    **合批的规则可以参考：**
> https://zhuanlan.zhihu.com/p/339387759
> https://www.cnblogs.com/moran-amos/p/13858990.html
关于UI合批，对于同一深度，Unity会尽可能将相邻的使用相同材质和贴图的元素合批。
**Canvas重建可以参考：**
https://zhuanlan.zhihu.com/p/448293298
Canvas中的所有元素最终会合并成一个SharedMesh，修改 Canvas中的任意元素会导致整个Canvas重建，一个比较直接的优化方式是**动静分离**，即活动的元素放在一个Canvas下，不可活动的元素放在另一个Canvas下。
#### 1.2.3 **Overdraw相关**
UI是在透明队列中渲染的，任何一个fragment都会计算所有覆盖在该fragment上的所有层级，而大多数情况下只有最上层的才是真正需要的，会导致不必要的消耗。
对于OverDraw检测可以使用Unity内置
> Scene->Shading Mode->Overdraw
也可以使用外部的检测工具如RenderDoc，可以参考
https://docs.unity3d.com/2021.3/Documentation/Manual/RenderDocIntegration.html
#### 1.2.4 一些配置上的小建议
- 如果某个Image组件不需要与点击事件交互，那么应该关闭`Raycast Target`选项。
- 需要`Raycast`交互的元素，不要放在过深的层级里面，原因是`Raycast`将暴力遍历根部的所有Transform层级，并要检测与Transform关联的所有组件，以寻找某个组件是否实现了`ICanvasRaycastFilter`。一个优化方法是在某个偏浅的节点接收`Raycast`，再将信息传递到某个偏深的节点。
- Text组件尽量避免开启`Best Fit`选项，这会导致在运行时实时计算最佳大小。
- 尽量避免使用`mask`组件，会导致额外的drawcall，如果避免不了，可以考虑使用`Rect Mask 2D`，该组件不会影响合批，但是只支持矩形Mask。
#### 1.2.5 性能分析工具
可以使用Unity内置Profiler，通过启用/禁用某些UI，观察性能变化情况
> Window->Analysis->Profiler

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1a588fcb11274f49b867d7f4ca9235db)

具体参数介绍可见文档[Unity - Manual: UI and UI Details Profiler](https://docs.unity3d.com/2021.3/Documentation/Manual/ProfilerUI.html)
也可以使用Unity内置Frame Debuger，其中会显示UI所包括的所用DrawCall。
> Window->Analysis->Frame Debug

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/29a664ba63ba4f46b87d91d2185ad201)

Frame Debugger相关介绍可见[Unity - Manual: Frame Debugger window reference](https://docs.unity3d.com/Manual/frame-debugger-window.html)
### 1.3 图片压缩设置
  图片使用ASTC格式进行压缩。（Unity2021以后的版本支持）
## 二. 代码相关
可参考
> https://docs.unity3d.com/cn/2021.3/Manual/BestPracticeUnderstandingPerformanceInUnity.html
> https://blog.unity.com/cn/games/optimize-your-mobile-game-performance-tips-on-profiling-memory-and-code-architecture-from
### 2.1 **几个常用的代码风格优化手段**
- 避免使用Unity某些内置方法

```csharp
GameObject.SendMessage()
GameObject.BroadcastMessage()
UnityEngine.Object.Find()
UnityEngine.Object.FindWithTag()
UnityEngine.Object.FindObjectOfType()
UnityEngine.Object.FindObjectsOfType()
UnityEngine.Object.FindGameObjectsWithTag()
UnityEngine.Object.FindGameObjectsWithTag()
```

及`Event`等监听函数，如果无法避免，应尽量使用C#内置Event而不是`UnityEvent`
- 善用缓存引用
如果需要多次使用某一个Component，应在第一次获取时就将其缓存，而不是每次都现场获取
- 避免空回调
每次生命周期方法如`Start(),Update()` 都会导致额外的函数压栈出栈，如果某个生命周期方法里什么也没做，那么应该删除整个方法，而不是留一个空方法。
- 装箱拆箱
尽量避免使用 `ArrayList`等非泛型集合，尽量使用`List<T>`等数据类型绑定的泛型集合。
### 2.2 资源加载
Unity WebGL使用单线程，因此Addressables的资源加载和下载等异步操作最终都是运行在同一线程，因此Addressables加载会耗费大量CPU，可参考文档[使用 Addressable 进行资源按需加载](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc_webgl_aa)
### 2.3 实例化
如果需要频繁的使用`Object.Instantiate()`和`Object.Destroy()`可以考虑使用对象池
可以参考
> [Unity - Scripting API: ObjectPool](https://docs.unity3d.com/ScriptReference/Pool.ObjectPool_1.html)
> https://learn.unity.com/tutorial/introduction-to-object-pooling
## 三. 渲染相关
渲染的一个很重要的优化方向是**减少DrawCall**，可以参考文档
> https://docs.unity3d.com/2021.3/Documentation/Manual/optimizing-draw-calls.html
> 其他如LOD、光照、纹理等优化方案，可以参考详细文档[优化Unity WebGL的渲染性能](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/running/sc_webgl_render_optimization)
### 3.1 限制分辨率
可调用对应的C#接口修改为较低的分辨率
### 3.2 启用WebGL2.0
- WebGL2.0支持延迟渲染，可能会对多光源场景有较大优化。
- WebGL2.0支持GPU Instancing，可以进一步合并DrawCall。
WebGl2.0具体可见[WebGL2.0渲染支持说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/running/sc_webgl_2)
### 3.3 SRP Batcher
SRP Batcher**只能运行在WebGL2.0上**
SRP Batcher将材质信息持久化存在显存中，同时批量处理了两个DrawCall之间的绑定操作，大大减少了CPU的消耗，更多信息可以参考官方文档
https://docs.unity3d.com/2021.3/Documentation/Manual/SRPBatcher.html
### 3.3 URP优化
参考 https://github.com/wechat-miniprogram/minigame-unity-webgl-transform/blob/main/Design/CustomURP.md
