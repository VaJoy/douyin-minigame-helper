---
title: "优化Unity WebGL的内存"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/running/sc_webgl_memory_optimization
update_time: 2025-06-11
---

## 内存与崩溃
Unity WebGL 游戏通常比普通小游戏占用更大的内存，在操作系统的控制策略下超出阈值时非常容易被 OOM。
为了提高游戏在中低端机型的稳定性，内存优化极为重要。
由于系统限制，iOS 上我们推荐高性能模式，而高性能模式下的内存限制非常严格，如果超出则很有可能被系统终止。相对而言，Android 机型的内存更为宽松。
> iOS内存限制：低档机 < 1G, 中高档机 < 1.4G

## Unity WebGL 适配小游戏的内存结构
Unity WebGL 内存结构可先参考：
[Unity博客：了解 Unity WebGL 中的内存 (Understanding Memory in Unity WebGL)](https://blogs.unity3d.com/2016/09/20/understanding-memory-in-unity-webgl/?_ga=2.221731928.1756133398.1638172136-1917727044.1634213664)
[Unity博客：Unity WebGL 内存：Unity 堆 (Unity WebGL Memory: The Unity Heap)](https://blog.unity.com/technology/unity-webgl-memory-the-unity-heap)

在小游戏容器里，通常内存占比分布如下：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ecd1db31f9bd47f3b79b9b912d4225b9)

Unity WebGL 是以 WebAssembly + WebGL 技术为基础的应用，运行在浏览器环境，因此游戏内存的分配也是完全托管在这个环境中。
适配在小游戏后，小游戏进程也就成为了“容器”，虽然不再是标准的浏览器，但内存组成结构与上图基本一致，典型游戏的内存占用如下图所示：
- 基础库+Canvas：在小游戏环境中并不存在DOM，但依然会存在一些基本消耗，比如小游戏公共库，Canvas画布等。典型地，小游戏公共库约占用内存70~90MB，Canvas 画布与设备物理分辨率相关，比如iPhone 11 Pro Max占用约80MB。
- Unity Heap: 托管堆、本机堆与原生插件底层内存。举例，游戏逻辑分配的C#对象等托管内存、Unity管理的AssetBundle和场景结构等本机内存、第三方原生插件(如lua)调用的malloc分配。
- WASM编译: 代码编译与运行时指令优化产生的内存，在 Android v8、iOS JavaScriptCore 中还需要大量内存进行 JIT 优化。所以游戏内存紧张的游戏，在上线前使用平台的分包功能非常必要。
- GPU内存：纹理或模型Upload GPU之后的显存占用, 由于Unity2021之前不支持ASTC压缩，纹理内存会造成明显膨胀。
- 其他：
  - 音频：Unity将音频传递给容器（浏览器或小游戏）后，播放音频时将占用的内存。特别地请避免使用fmod播放长音频。
  - Emscripten使用[文件系统](https://emscripten.org/docs/api_reference/Filesystem-API.html)模拟Linux/POSIX接口，代价是占用与文件同等大小的内存。 请勿使用首资源包、Addressable Cache机制、WWW.LoadFromCacheOrDownload等Cache API
  - 网络请求造成的浏览器端JS临时内存、垃圾回收
- 注：如果是 iOS 上的高性能+模式，则 GPU 内存会移到抖音进程，为游戏提供更多内存空间。

## 内存查看工具
我们从大到小各个角度去监控和分析游戏的内存情况：
- 进程级别：Android Studio、 Xcode Instrument。
- UnityHeap(CPU主内存)：性能面板、Profiling、JavaScript Heap。
- 引擎与资源：UnityProfiler。

### 进程总内存
查看总内存时，我们需要先确定监控的小游戏进程名称：
- Android：minigame0 - minigame3
- iOS: WebContent

Xcode Instruments (iOS)：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/687608869c4f4778aeaf5df9ff9da08a)

使用“Activity Monitor”，选择对应的设备 - all processes - 捕捉，即可看到所有进程的 CPU 与内存情况：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/93efbea2a1554c548a57817629968a55)

### UnityHeap
UnityHeap 非常关键，典型由以下几部分组成：
- 托管堆， C#对象托管对象、游戏状态
- 本机堆， Unity Native 产生，引擎内部对象
- 原生内存，第三方插件（如lua）直接调用malloc产生
每项指标有三个数值：当前帧、最小值、最大值。
通常而言：MonoHeap + NativeReserved + 原生插件内存 = DynamicMemory，因此开发者需要关注这几部分内存。
Unity 引擎视角：
- MonoHeapReserved：托管堆的内存预留内存
- MonoHeap：托管堆 (如 C# 业务逻辑)当前的内存使用量
- NativeReserverd：本机堆 (Native) 内存分配峰值
- NativeUnused：本机堆 (Native) 空闲内存值
- NativeAllocated：本机堆 (Native) 当前的内存使用量
- 注意：第三方原生插件 (如 lua) 分配内存并未呈现，需开发者自行分析。
底层分配器视角：
- TotalHeapMemory: UnityHeap 总预分配内存大小
- DynamicMemory：UnityHeap 使用上限
- UsedHeapMemory：UnityHeap 真实使用量
- UnAllocatedMemory：UnityHeap 预留量

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/30419da117034626846ca215bdf255b2)

底层分配器：
- 绿色为空闲内存或碎片，底层分配器会尽量复用
- 白色为预留部分，可被使用
- 其他颜色，已被业务使用

### Unity Profiler
当发现 UnityHeap (尤其是 Native) 占用比较高时，可通过 UnityProfiler 进一步分析问题所在。关于该工具在小游戏的使用请查阅使用 Unity Profiler 性能调优。

### JavaScript Heap
由于 Unity WebGL 是托管在浏览器环境中，因此 JavaScript Heap 包含了大部分（并非全部）我们关注的内存，通常我们可以使用浏览器自带的内存工具。 但需要注意的是 JavaScript Heap 通常无法看出具体内存使用，发现该部分内存明显大于我们预留的 UnityHeap，应检查是否有使用 Unity Cache 进行文件缓存，务必避免这样使用。
iOS Safari Timeline (PC or iOS)：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/96c7a08f297a4ecbaceac8fca13268a6)

## 内存优化方案
> 内存计算公式：
> 小游戏基础库 + Canvas + 编译内存 + UnityHeap + Gfx 显存 + 音频 + JavaScript 内存。
> UnityHeap = max(托管/Mono内存) + max(Native/Reserved内存 + C原生代码内存)
以 iOS 为例，一款代码 (导出目录 /webgl/Build/xxx.code.unityweb 或 code.wasm) 大小为 30MB 的游戏占用内存为： 小游戏基础库 (100MB) + Canvas(70MB) + 编译内存 (300MB) + UnityHeap + Gfx 显存 + 音频 + JavaScript (通常 <100MB)。
假如游戏需要支持低档机型，将内存控制到 1G 以内，业务侧 (UnityHeap, Gfx 显存，音频，JavaScript) 需控制在 500MB 左右。我们此处给出转换游戏中最容易遇到的内存问题与解决方案，如果开发者遇到内存问题时请逐个排查优化。

### WASM代码编译内存
- 问题原因：Unity WebGL将所有代码(引擎、业务代码、第三方插件)编译为跨平台的WebAssembly二进制代码，运行时需进行编译执行。编译所占用内存占用非常大（如在iOS系统，30MB未压缩代码需300MB运行时编译内存）。
- 解决办法：
  - [使用代码分包工具](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/code-upload/sc_webgl_split)能降低原编译代码内存50%以上
  - 手动删除多余插件，减少不必要的Unity模块引入(如物理、Unity数据统计等)

### GPU内存
- 问题原因：Unity 2021才开始支持移动平台的压缩纹理，使用RGBA、DXT等纹理格式将导致巨大的内存开销与运行时解压消耗。
- 解决办法：
  - 使用高性能+模式
  - 升级引擎至2021使用ASTC压缩纹理
  - 关闭HDR，标准渲染管线在"GraphicsSetting-tier2"（WebGL使用tier2），取消勾选"Use HDR"，URP管线通过renderer配置取消

### UnityHeap
- 问题原因：UnityHeap是用于存储所有状态、托管的对象和本机对象，往往由于场景过大或由于业务原因造成瞬间内存峰值。由于Unity WebGL在单帧内无法GC，单帧内瞬间的内存使用非常容易造成crash。同时，Heap是只增不减且存在内存碎片的。游戏应该尽可能的不造成UnityHeap的增长，Heap在不足时的grow行为会导致内存存在尖刺，极易导致内存崩溃
- 解决办法：
  - 在BuildTool中，设置合适的UnityHeap。（具体数值可以参考测试中的Profiler面板的数值，比如测试中位200MB左右，则可以将UnityHeap设置为256MB）
  - 使用[TTAssetBundle加载资源](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc-webgl-tt-ab)，可以有效的防止UnityHeap的增长
  - 避免场景过大导致瞬间峰值
  - 避免过大的AssetBundle导致瞬间峰值
  - 避免单帧内分配过多的对象, 切忌产生跳跃峰值

### 首资源包与AssetBundle内存
- 问题原因：首资源包永远占用内存且无法释放；首资源包和AssetBundle自带的cache机制都会使用Emscripten使用的[文件系统](https://emscripten.org/docs/api_reference/Filesystem-API.html)，应避免使用。
- 解决办法：
  - 减少首资源包大小，此部分始终占用内存无法释放, 使用AssetBundle
  - AssetBundle按需加载，及时释放以节省内存，AssetBundle使用时被解压占用Unity Native内存，应减少AssetBundle大小，应尽可能使用[TTAssetBundle](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc-webgl-tt-ab)
  - 避免使用Unity自带的文件缓存机制， 首资源包和AssetBundle都不应使用文件Cache
  - 文件访问应使用[平台提供的文件系统](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_new_file_system)，不使用系统的File、PlayerPrefs接口

### 音频内存
- 问题原因：音频将占用小游戏环境的内存
- 解决办法：
  - 不要使用fmod播放长音频，如游戏BGM
  - 控制音效数量，同时存在的音频数不应该超过20个
  - 尽量强制使用单声道音频，双声道会产生2倍内存消耗

### 其他常见优化手段
- [性能优化，进无止境-内存篇（上）](https://blog.uwa4d.com/archives/optimzation_memory_1.html)
- [性能优化，进无止境-内存篇（下）](https://blog.uwa4d.com/archives/optimzation_memory_2.html)
- [全面理解Unity加载和内存管理](https://gameinstitute.qq.com/community/detail/100741)
## QA
- Q: 如何解决iOS出现内存过大导致游戏关闭，常见优化步骤如何？
  - OS由操作系统管理内存上限，在3G RAM机型上限是1.5G，安全内存峰值是1.2-1.3G左右
  - 进程内存离1.5G上限还有较大差距就崩溃了，请检查“UnityHeap预留内存“是否足够
  - 请使用Xcode Instrument查看WebContent进程内存是否在安全范围内
  - 进程内存中的业务内存(UnityHeap, GPU)是每个项目的主要差异点：打开性能面板查看DynamicMemory，峰值不要超过500M；
  - 请务必使用代码分包、压缩纹理（2021以上可使用引擎ASTC）
- Q: 在Unity Profiler看到内存才200MB+，是否代表游戏内存无问题
  - 不是。游戏占用内存必须以真机环境为准，使用Xcode Instruments测试对应进程的内存占用。
  - Unity Profiler 仅能看到 Unity Heap 相关内存，并不包含小游戏公共库、Canvas、WebAssembly 编译以及容器其他内存。
- Q: 转换面板设置内存值多少合适？
  - 请看前文关于UnityHeap预留内存的说明
