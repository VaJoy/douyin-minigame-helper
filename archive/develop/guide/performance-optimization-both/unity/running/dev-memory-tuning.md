---
title: "开发阶段内存调优"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/running/dev-memory-tuning
update_time: 2025-08-27
---

开发过程中，为了方便开发者定位和调试所研发的抖音小游戏的内存问题，本文推荐以下两个工具。
## 一、抖音开发者工具之 Profiles

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/4ca4789685c24a0aa88b3e6c69ce335d~tplv-9nona0m7ha-image.image)

#### Profiles面板
Profiles 面板是 抖音开发者工具 中用于分析和调试网页内存使用情况的工具。通过这个面板，开发者可以检测和优化内存占用情况，识别内存泄漏。主要功能包括：
1. **堆快照（Heap Snapshot）**：拍摄 JavaScript 堆的快照，以查看对象分配情况、找出内存泄漏的根源。
1. **时间轴上的分配检测（Allocation Timeline）**：记录一段时间内内存分配情况，分析对象是在哪些函数中分配的，帮助发现频繁分配和回收的热点区域。
1. **分配采样（Allocation sampling）**：使用采样方法记录内存分配，这种方式对性能的影响较小，适用于长时间运行的操作。
通过这些功能，开发者可以更好地理解和管理运行时的内存使用，从而提高性能和稳定性。
##### Heap snapshot
Heap snapshot 有 Summary、Comparison、Containment 和 Statistics 四种视图。
- Summary 显示按构造函数名称分组的对象。使用它可以根据构造函数名称分组的类型来查找对象（及其内存使用情况）。这对于跟踪 DOM 泄漏特别有用 。 Comparison 显示两个快照之间的差异。使用它可以比较操作之前和之后的两个（或多个）内存快照。通过检查释放的内存中的增量和引用计数，可以确认内存泄漏的存在和原因。
- Containment 允许浏览堆内容。它提供了一个更好的对象结构视图，有助于分析全局命名空间（窗口）中引用的对象，以找出使它们保持不变的原因。用它来分析闭包并从低层次深入研究对象。
- Statistics 显示了当前 js heap 各种类别的资源所占用的内存大小的统计图。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/13ab8552be1b4fa5881336561d58ce44~tplv-9nona0m7ha-image.image)

1. Summary
- Constructor 表示使用此构造函数创建的所有对象。Shallow Size 显示对象本身占用的内存大小。Retained Size 显示删除对象后可以释放的内存大小（依赖项不可再访问）。这个大小其实主要包含了依赖项的大小。Distance 使用节点到根距离的最短路径。展开每一行，将显示其所有实例。@字符后的数字是对象的唯一 ID，可以按对象比较堆快照。
- (global property) – 全局对象和其引用对象的中间对象。
- (roots) – 引用了所选对象的实体对象。引用可能被浏览器引擎出于自身目的所创建。浏览器引擎具备引用缓存，但是这些引用都是弱引用，因此不会阻止所选对象的垃圾回收。
- (closure) – 通过函数闭包对一组对象的引用计数。
- (array, string, number, regexp) – 具有引用数组，字符串，数字或正则表达式的属性的对象类型的列表。
- (compiled code) – 所有与编译代码相关的内容。HTMLDivElement，ArrayBuffer 等 – 对代码引用的特定类型的元素或文档对象的引用。
1. Comparison 通过将多个快照相互比较来查找存在差异的对象。为了验证某个应用程序操作不会造成泄漏（例如，通常是一对直接和反向操作，例如打开一个文档，然后关闭它，不会留下任何垃圾），您可以遵循以下情形：
- 在执行操作之前，录制堆快照（take heap snapshot）。
- 执行一项操作（以您认为会导致泄漏的某种方式与页面进行交互）。
- 执行相反的操作（进行相反的交互并重复几次）。
- 拍摄第二个堆快照，并将其视图更改为“比较”，将其与快照 1 进行比较。在“比较”视图中，显示两个快照之间的差异。展开总条目时，显示添加和删除的对象实例：
1. Containment 本质上是应用程序对象结构的“鸟瞰图”。可以通过它查看函数闭包内部，观察组成 JavaScript 对象的 VM 内部对象，以及了解应用程序在非常低的级别使用了多少内存。该视图提供了几个入口点：
- DOMWindow objects 是代码层面的“全局”对象。
- GC root 是 VM 垃圾回收使用的实际 GC 根目录。GC 根目录可以由内置对象映射，符号表，VM 线程堆栈，编译缓存，句柄作用域，全局句柄组成。
- native object 是 JavaScript 虚拟机内部“推送”以允许自动化的浏览器对象，例如 DOM 节点，CSS 规则。
##### **Allocation instrumentation on timeline**
录制时，请注意“分配时间轴”上是否有蓝色条状显示，如下面的屏幕截图所示。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/3a6e2fc4ad1a4670a343eff8c8f5c0eb~tplv-9nona0m7ha-image.image)

这些蓝色条表示新的内存分配。可以缩放栏以筛选“Constructor”窗格，以仅显示在指定时间范围内分配的对象。展开对象，然后单击其值查看有关它的更多详细信息。

## 二、Unity 运行时之 Profiling
在 Unity 小游戏运行时，提供了一个 Profiling 的能力，其主要是可以帮助开发者发现 Unity 小游戏时的性能问题，包括 UnityHeap 设置的合理性。
1. 入口
入口在 TTSDK 的构建工具面板上，在构建前将`Profiling` 选项勾选上。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/6f1c9114ba0440c0b22f276e2caaa812~tplv-9nona0m7ha-image.image)

1. 查看运行效果
游戏运行时，会有游戏的左上角显示一个性能面板，如下图所示。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/04d9309c771d4b7a9047386c364dce91~tplv-9nona0m7ha-image.image)

1. 性能分析
> 尽量保证 TotalMemory 的大小在游戏运行期间不会变化，在内存变化时会出现内存尖峰，容易导致游戏崩溃。且同时需注意不要设置过大，否则低端机型会出现无法进入游戏的情况。
- WebAssembly
  - TotalMemory：即 UnityHeap， 托管堆、本机堆与原生插件底层内存。举例，游戏逻辑分配的 C# 对象等托管内存、Unity 管理的 AssetBundle 和场景结构等本机内存、第三方原生插件（如 lua）调用的 malloc 分配。
  - Static：静态存储区，取决于编译的代码，因此其大小主要和引擎版本以及项目代码有关系。
  - Stack：堆栈区，其大小一般为 5M 大小
  - DynamicMemory：它包含了游戏过程中开辟的一个或多个托管堆，以及在游戏过程中被释放的内存的。此部分内存只能增长不能缩减。
  - UnAllocated：代表除了 `Static`，`Stack`，以及 `DynamicMemory` 以外，未使用到的内存部分，它与其他几个内存相加将等于 Unity Heap 的大小，即 Total Memory。`Total Memory` = `Static` + `Stack` + `DynamicMemory` + `Unallocated`;

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/1f7b6c5968db4fe7a57e421e0b724c86~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/2c990afa125a436b88a54c2bf03a326a~tplv-9nona0m7ha-image.image)

- Unity 内存
  - GC Reserved：Unity 保留的托管内存大小
  - GC Used：Unity 使用的托管内存大小
  - Total Reserved：Unity 保留的总内存大小
  - Total Used：Unity 使用的内存大小
