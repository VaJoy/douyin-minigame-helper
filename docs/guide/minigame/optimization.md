---
title: "性能优化"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/optimization
update_time: 2025-05-29
---

## 一、图片资源使用注意事项
不规范的资源管理方式，容易导致游戏加载速度慢、运行内存大，影响游戏的体验和性能。下面列出一些需要注意的地方：
**优先 png 格式**
UI 输出资源时，应该优先使用 png 格式而不是 jpg 格式。png 格式采用无损压缩算法，jpg 使用的是有损压缩算法，用 png 格式输出资源，获得的图片质量是好于使用 jpg 格式的。
如果图片的大小比较大，可以使用 tinypng、pngquant 这类的工具提高压缩率(有损压缩)或者使用 ETC2 等格式的压缩纹理。但是建议使用初始的 png 图片而不是用 tiny 等工具压缩后的 png 图片生成压缩纹理，因为压缩纹理也是采用有损压缩算法。多次对图片使用有损压缩算法进行压缩，会进一步降低图片质量，导致资源效果差。
**控制尺寸**
在保证外观效果的情况下，尽可能地减小图片尺寸。例如下图中的海水这类重复纹理，应尽可能减少尺寸。
控制尺寸的效果有多大？我们来举个例子，假设图片最初尺寸为 512x512，80 张该尺寸的 RGB888 png 图片，需要占用 80x512x512x3byte = 60M 内存，若将尺寸优化成 128x128，则仅需要 80x128x128x3byte = 3.75M 内存。占用内存可减少 93.75%。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651138490766)

**修剪透明部分**
下面左边的图片，一半的面积，都是透明部分，浪费大量的空间，在 UI 输出资源时应该尽量避免，或者用工具修剪掉透明部分。右边是修剪后的图片。尺寸由 750x375 变为 466x284，占用内存减小 50%。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651138489611)

**合并图片**
合并图片的目的是为了减少引擎读取文件的次数，加快加载速度。合图的关键问题是，合出的大图， 空间利用率是否足够高 ，较低的空间利用率，会造成游戏运行内存的增大。合图要注意的几个问题如下：
1.应该尽量只对尺寸比较小的图，进行合图操作。尺寸大于 256x256 的图片，要考虑下。
2.合出的整张大图，尺寸不要太大，一般不大于 1024x1024，建议不要超过 2048x2048。
3.尽量保证合图的利用率，不要低于 75%(越高越好)。实际上 1 和 2 也是可以提高合图利用率的。合图时，记得打开允许旋转选项，这也能够提升利用率。导出格式选用 RGBA8888。
4.尽量保证关联性大的图片合并在一起。比如同一界面的资源，应该优先合在一张图上，而不是放在多张图里，这样子保证可以一次操作就可以读取或者传送整个界面需要的资源。
**资源复用**
对尺寸比较大的资源，尽量进行复用。像界面背景图片这样的资源，应该抽取出，单独出资源。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651138489893)

**九宫格拉伸**
当界面资源要显示的图片尺寸比较大，且中间部分是由连续有规则的像素组成时，通常使用九宫格拉伸的办法，大幅度减小图片尺寸的大小。对于可以进行拉伸的图片，划分成以下 9 个部分：

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651138489540)

拉伸规则如下：
- 四个边角 1、3、7、9 不做任何拉伸；
- 2、4、6、8 做单向拉伸，2、8 做横向拉伸，4、6 做纵向拉伸
- 5 做双向拉伸
下面的图片尺寸是 612x946，*格式是 RGBA8888*，如果使用九宫格拉伸的办法，那么尺寸可以做到小于 300x300，占用内存减小 80%以上。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651138489932)

**压缩纹理**
像场景贴图、界面背景图等资源，占用内存比较大，但为了保证效果，不能去减小尺寸，这种情况下可以考虑使用压缩纹理。压缩纹理采用的是有损的压缩算法，一般效果都是可以接受的。下面是两张对比图：左边是 s3tc 格式的压缩纹理资源，右图是未压缩的图片资源。对比下两张资源图，大部分地方肉眼不容易识别出差别，左边图片在边缘细节上，要差一些（可以双击放大看）。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651138490369)

## 二、纹理内存优化
**内存过大导致的问题**
游戏运行时占用的内存大小，是衡量游戏性能的一个非常重要的指标。游戏如果占用的内存过大，会导致以下的问题：
- 发热，发烫。过多的内存数据传输，是导致游戏发热的主要原因之一。
- 延迟、卡顿。像纹理的加载、传输都需要耗费时间，另外内存资源占用的越多，系统也更加容易触发 gc 操作，导致游戏非预期卡顿。
- 闪退。游戏超过一定的内存上限，操作系统会强制杀死进程。
而纹理占用的内存占整个运行内存的比重非常大，并且容易做优化，所以纹理内存占用的大小是需要重点关注的。
**纹理加载流程**
下面是一张图片加载的整个流程。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651138490323)

可以看出读取非压缩纹理与压缩纹理的主要区别是： **压缩纹理不需要解码** ，数据是可以直接被 gpu 读取；png 等格式图片，不能直接被 gpu 读取，需要解码成未压缩的位数据。不过实际运行中， **并不是所有阶段的数据都需要保存** 。非压缩纹理在 cpu 内存里的编码数据（蓝色区域），在解码后，是不需要再保存的。
**纹理管理方式**
下面列举几种小游戏开发可以使用的纹理管理方案：

| **管理方式** | **优点** | **缺点** |
| --- | --- | --- |
| 将所有资源都加载进 gpu 内存，那么对于非压缩纹理，只需要在 gpu 内存保存一份解码数据，压缩纹理只需要在 gpu 内存保存一份压缩纹理数据。也就是只需要红色区域的部分。 | 运行性能最佳，适合使用 three.js 这种不自动回收 gpu 资源的引擎，并且整个游戏纹理内存占用不大的情况 | 存在一定门槛，要求开发者对 webgl 和所使用的引擎有一定的了解，保证 gpu 内的纹理数据，没有被引擎或者自己释放。 |
| 将所有资源都加载进 cpu 内存，然后在运行时，将所需要绘制的资源，加载进 gpu 内存，不需要绘制时，可以释放掉。 | 运行性能较好。 | 如果引擎未能自动在绘制纹理时，将纹理数据从 cpu 内存 copy 进 gpu 内存，需人工干预。 |
| 将部分资源加载进 cpu 内存，然后在运行时，再将所需要绘制的资源，加载进 gpu 内存。根据需要将资源加载、释放。 | 占用的内存小，适合做多关卡、多场景游戏。 | 需要主动管理好资源的加载与释放问题。一般在加载关卡进度的时候，完成资源的加载。 |

**纹理大小如何计算**
要想优化纹理占用的内存，就要知道如何计算每张纹理的大小。下面用一个例子进行说明。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651138490227)

上面是脸萌的主场景图片，jpg 格式，尺寸为 512512，颜色空间为 RGB888，大小 100kb。解码后占用的内存大小计算公式为：长 *宽 *通道个数 *通道位数，如果解码成 RGB888 格式，那么占用的内存大小为 51251238bit = 0.75M。而对应的 etc2 RGB888 格式的压缩纹理占用的内存大小为 512512\0.5byte = 0.125M（实际大小为 135kb，因为还包含纹理描述信息）。下面的表格列举出几种常用的压缩纹理格式每像素占用的字节数。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651138490582)

**减小纹理占用内存的方法**
那么减少单张图片占用的内存，有以下几个方案：
1.减小图片的尺寸，在满足视觉要求的情况下，尽可能地缩小图片尺寸，比如将一张 256*256 图片缩小成 128*128 尺寸，就减少了 75%的内存占用。
2.降低通道位数，比如 RGB888 格式的图片转换为 RGB565 格式。但是这也依赖于具体的解码方法，现在小游戏引擎，会把图片资源都解码成 RGBA8888 格式，那么即使将 RGB888 格式转换为 RGB565 格式，也不会降低解码后纹理数据占用的内存。
3.使用压缩纹理，但是有几个限制点：首先压缩纹理是有损压缩，会降低一些图片质量（一般不明显）；其次各个平台、不同图形 api 支持的压缩纹理格式，也不尽相同。比如浏览器上可以支持 s3tc 纹理，手机端支持 etc2 纹理（需要支持 opengles3.0），iOS 系统支持 pvrtc 纹理。
像 pngquant、tinypng 等采用 color reduction 方法压缩图片的工具，能够减小文件大小，加快加载速度，编码数据占用的内存也更小。但是在解码方式不变的情况下，并不能减小解码后的图片内存占用大小。
## 三、TTWebAssembly
从基础库版本 3.7.0.0 开始，小游戏在 JS 线程和 Worker 线程中提供了全局的 TTWebAssembly 对象，并且支持加载包内的经过 brotli 压缩过的 wasm 文件（后缀为*.[wasm.br](http://wasm.br/))。
TTWebAssembly 类似 Web 标准的 WebAssembly，在执行计算密集型任务时，与 JavaScript 相比，可以提高一定的性能。
**注意**：iOS 上暂不支持 SIMD 等 WebAssembly 提案。
### API
#### TTWebAssembly.compile(path)
编译一个 WebAssembly 模块，path 必须为包内 wasm 文件路径。
函数返回一个 `Promise` 对象，若文件存在且编译成功，则 resolve 一个 `TTWebAssembly.Module`。若文件读取失败或编译失败，则 reject。
#### TTWebAssembly.instantiate(path, importObject)
创建 WebAssembly 实例，path 必须为包内 wasm 文件路径。
函数返回一个 `Promise` 对象，若文件存在且编译成功，则 resolve 一个对象，对象的 module 属性为 `TTWebAssembly.Module`，instance 属性为 `TTWebAssembly.Instance`。若文件读取失败或编译失败、导入对象不匹配，则 reject。
#### TTWebAssembly.Module
TTWebAssembly Module 类可以通过 `TTWebAssembly.compile` 构造，与 WebAssembly 标准相同。
#### TTWebAssembly.Global
用于 JavaScript 和 Instance 之间传递全局状态，与 WebAssembly 标准相同。
#### TTWebAssembly.Table
用于动态链接不同 Instance，与 WebAssembly 标准相同。
#### TTWebAssembly.Memory
用于 JavaScript 和 Instance 之间共享内存。与 WebAssembly 标准相同。
#### TTWebAssembly.Instance
TTWebAssembly Instance 类可以通过 `TTWebAssembly.instantiate` 或`new TTWebAssembly.Instance(module, importObject)` 构造。暴露 `exports` 属性，包含实例导出的 Table、Global、Memory 或函数。
## 四、使用 Worker
在小游戏中，为了节省处理时间，减少同步操作对主线程的阻塞，如果有一些可以异步处理的任务，可以放置于 [Worker](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/worker/worker/) 线程中运行，待运行结束后，再把结果返回到主线程。
小游戏环境下的 Worker 能力与主线程存在一定的差异，具体对比如下：

| 能力 | Worker | 主线程 |
| --- | --- | --- |
| 渲染能力 | 不支持 | 支持 |
| JS(tt) API | 不支持 | 支持 |
| 网络/IO | 不支持 | 支持 |
| 定时器 | 支持 | 支持 |
| TTWebAssembly | 支持 | 支持 |

其中，TTWebAssembly 自基础库 3.7.0.0 开始支持，[定时器](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/basic-function/timer/set-timeout)相关 API 自 3.45.0.0 开始支持。