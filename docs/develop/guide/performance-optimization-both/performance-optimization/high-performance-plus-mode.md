---
title: "高性能+模式"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/performance-optimization/high-performance-plus-mode
update_time: 2025-09-25
---

## 简介
iOS “高性能+” 模式是相对于当前“高性能”模式的一种升级模式，主要为了解决 iOS 系统严格的内存限制，以及部分 iOS 版本运行 WebGL2 渲染兼容性问题，而推出的一种更优的运行模式。

**内存不足的表现：**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/48239a171d044deeb078b24762ebc13a~tplv-9nona0m7ha-image.image)

## 性能数据
从内测阶段的数据来看，从高性能模式切换到高性能+模式后：

| **指标** | **优化效果** | **备注** |
| --- | --- | --- |
| 游戏内存大小 | **降低 150 ~ 300 M** | 视游戏复杂度而定 |
| GPU 使用率 | **降低 30%** | 视游戏复杂度而定 |
| 兼容性增强 | **在部分iOS版本上FPS大幅提升** **提升了 WebGL2 的兼容性** **解决部分 iOS 版本渲染内存异常高问题** | 渲染兼容性问题参见本文附录 |

### 当前在观察的数据
从内存空间、渲染兼容性以及运行效率这三个方面而言，高性能+模式均优于高性能模式。
当前之所以未将高性能方案直接全量替换为高性能+，是因为高性能+在 iOS 上采用双线程模式运行，会将游戏部分的渲染内存转移至抖音 App，致使抖音 App 的内存增加。这可能导致用户将抖音 App 切换至后台时，游戏进程的热缓存时间缩短。目前仍在观察其对用户数据的影响。若发现影响不大，平台或许会将高性能模式下架，并全量替换为高性能+模式。

### 运行环境要求
“高性能+”模式版本要求：
- iOS 系统版本：**>= 14.5**
- 抖音软件版本：**>= 32.7.0**
- 客户端基础库版本：**>= ****3.54.0.0**
- 开发者工具版本：**>= 4.3.5**
- tt-minigame-ide-cli 命令行工具版本：**>= 2.0.14**
Unity 小游戏及普通小游戏相同。
## 如何打开高性能+模式

> “高性能+”模式是“高性能”模式的特性升级，要开启“高性能+”模式请先保证游戏已经在“高性能”模式下正常运行。

- “高性能+”模式开关：
在game.json中配置`enableIOSHighPerformanceModePlus`为true：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/998de986d7514791b90eca48c8eac319~tplv-9nona0m7ha-image.image)

- 判断是否开启“高性能+”方法：
普通小游戏、Unity 小游戏【方式一】：
观察 VConsole 颜色，红色的表示开启了高性能+。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/60519b5cf1f24f4db45842d8d661ae05~tplv-9nona0m7ha-image.image)

普通小游戏【方式二】：
高性能+方案中，全局变量 GameGlobal.isIOSHighPerformanceModePlus 为 true。

```js
console.log(GameGlobal.isIOSHighPerformanceModePlus) 
// true
```

## API支持
在【高性能+】模式下支持的 API 数量，比【高性能】模式多，下列 API 在【高性能+】模式下已经可以正常使用的。

| API名称 | 高性能+ 支持情况 |
| --- | --- |
| request/pause/resumeMicrophone | 支持 |
| createCamera | 支持 |
| createFaceDetector | 支持 |
| createHandDetector | 支持 |
| video.paintTo | 支持 |
| video.play | 支持 |

## 常见问题 QA
### Q1. 高性能模式下暂不支持真机调试
A1. IDE 中的「真机调试」能力暂不支持高性能模式，使用该能力时请不要在 game.json 中配置为高性能模式，并且调试中的性能数据无法作为运行时性能的参考。

### Q2. 普通小游戏，js文件路径包含空格、%等特殊字符会加载失败

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/4616783a05784980a45ed0f91cfaffa8~tplv-9nona0m7ha-image.image)

A2. 这个问题是平台 URL 解码的 bug，可以尝试去掉这些特殊字符，抖音版本 <= 33.0.0 版本上存在，抖音版本 >= 33.1.0 上会逐步放量修复解决这个问题。

### Q3. 普通小游戏，高性能开关、高性能+开关，不同组合的表现是什么样的
A3. 参考下列排列组合：

| 【高性能】开关 | 【高性能+】开关 | 实际运行模式 |
| --- | --- | --- |
| 关闭 | 关闭 | 原始模式 |
| 开启 | 关闭 | 高性能模式 |
| 关闭 | 开启 | 高性能+模式 |
| 开启 | 开启 | 高性能+模式 |

### Q4. 渲染兼容问题

| 问题 | 详情 | 解决方案 |
| --- | --- | --- |
| WebGL2 | iOS15.0 以下不支持 WebGL2 | **针对iOS WKWebView存在的渲染问题，推荐使用高性能+模式来解决** |
|  | iOS15.x 版本对 WebGL2 的支持存在兼容问题，导致有些画面无法正常显示 |  |
| 卡顿、帧率低、卡死 | iOS15.4 版本开始默认使用 WebGL via Metal，在iOS15.4-16.4 版本上，相比 OpenGL 存在性能问题，尤其在如 Unity URP 管线下**帧率会很低** |  |
|  | iOS16.7-17.1 版本存在 WebGL context lost 问题，导致游戏切后台回来会渲染异常 |  |
| 内存 | iOS16.7-17.5 版本存在部分渲染兼容问题，导致渲染内存占用特别大 |  |
