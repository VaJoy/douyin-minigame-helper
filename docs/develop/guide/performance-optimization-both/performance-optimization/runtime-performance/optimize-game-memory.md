---
title: "优化普通小游戏内存"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/performance-optimization/runtime-performance/optimize-game-memory
update_time: 2025-06-17
---

## 内存调优
在开发抖音小游戏过程中，往往会有很多内存问题，比如内存溢出、内存泄露等，尤其在 iOS 平台上，内存压力往往较大。
iOS 平台下，开启高性能模式，能够支持 JIT，对运行性能和发热有优势，但由于运行在 WebContent 进程中，受限于系统对网页进程的内存严格限制，控制游戏的内存占用是开发者必须关注的。使用内存超过 1G，就有内存崩溃的风险。
虽然 Android 平台可用内存较多，但内存十分紧张时，可能会显著变卡。综上，当前机型分布条件下，使用内存控制在 1G 以下，较为妥当。如果游戏复杂，建议多关注线上的内存使用情况以及内存崩溃率。

## 资源纹理压缩
在游戏内存的使用中，图形内存往往是占用的大头。所以对贴图资源的优化是必要的。
最佳实践：选择 ASTC 格式进行纹理压缩。
原理：传统的图片文件格式有 PNG、JPEG 等，这种类型的图片格式无法直接被 GPU 读取，需要先经过 CPU 解码后再上传到 GPU 使用，解码后的数据以 RGB(A) 形式存储，无压缩。
而纹理压缩顾名思义是一种压缩的纹理格式，它通常会将纹理划分为固定大小的块 (block) 或者 tile，每个块单独进行压缩，整体显存占用更低，并且能直接被 GPU 读取和渲染(无需 CPU 解码)。
举例来说，一张 1024x1024 的 JPEG 图片，使用 RGBA 格式，显存占用在 4M~5.3M 左右，而如果采用 ASTC_4x4 纹理压缩格式后，理论内存占用约在 1.3M 左右，相比普通纹理，可以减少 70%+ 内存。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/5f10a0722168437195a51fe194b49185)

过去不同手机，根据机型，对各类纹理压缩格式较为碎片化。相关文档和方案请自行查阅。
到 2024 年，绝大多数的 Android，iOS 机型已支持 ASTC 格式。所以，在小游戏移动平台上应该统一选择 ASTC 即可达到最佳效果。

> 抖音小游戏在 Android 及 iOS，支持 ETC2，ASTC 的纹理压缩。（很早以前的 ETC，PVR 也支持，但维护意义很小，不做描述）

各个游戏引擎，COCOS，LAYA 都提供了对纹理格式的设置。
### Cocos Creator
> [压缩纹理 | Cocos Creator](https://docs.cocos.com/creator/3.8/manual/zh/asset/compress-texture.html?h=%E5%8E%8B%E7%BC%A9%E7%BA%B9%E7%90%86)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b869345ad6af4214a3df1367b2fbca95)

### Laya
> [纹理压缩 · LayaAir3.0文档 · LAYABOX](https://layaair.com/3.0/doc/IDE/uiEditor/textureCompress/readme.html?h=%E7%BA%B9%E7%90%86%E5%8E%8B%E7%BC%A9)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d645ea3026684adf9a6473a57fefefcb)

## 垃圾回收
小游戏中，JavaScript 中的每一个 Canvas 或 Image 对象都会有一个客户端层的实际纹理储存，实际纹理储存中存放着 Canvas、Image 的真实纹理，通常会占用相当一部分内存。
每个客户端实际纹理储存的回收时机依赖于 JavaScript 中的 Canvas、Image 对象回收。在 JavaScript 的 Canvas、Image 对象被回收之前，客户端对应的实际纹理储存不会被回收。
通过调用 [tt.triggerGC()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/performance/tt-trigger-gc) 方法，可以加快触发 JavaScriptCore Garbage Collection（垃圾回收），从而触发 JavaScript 中没有引用的 Canvas、Image 回收，释放对应的实际纹理储存。
但 GC 具体触发时机还要取决于 JavaScriptCore 自身机制，并不能保证调用 [tt.triggerGC()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/performance/tt-trigger-gc) 能马上触发回收，建议在每局游戏开始或结束触发一下。容器会在收到内存不足时调用 GC。
