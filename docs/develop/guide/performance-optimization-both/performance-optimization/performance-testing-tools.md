---
title: "性能测试工具"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/performance-optimization/performance-testing-tools
update_time: 2025-07-11
---

## 概述：
  最近越来越多的开发者反馈自己小游戏在运行阶段会有卡顿、掉帧、黑白屏等异常情况，为了帮助开发者更快发现运行过程中的性能问题，协助开发者提升小游戏在启动、运行时的性能指标和用户体验，抖音开放平台新增”性能测试工具“功能，在开发阶段提供适配不同机型和系统的性能测试方法，并提供丰富的测试数据和运行时指标，来满足开发者在开发阶段的性能指标感知和优化建议。
## 使用方法：
1. 在抖音开发者工具(4.2.5)版本中，点击性能测试进入使用：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/41bdc2cf9ab246fbaebd00b8d8ae61dc)

1. 点击运行，使用抖音(30.1.0版本及以上)进行扫码，并体验该小游戏：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/66c25373af6042a08c46676775da4af1)

1. 开发者工具中该页面会记录本次测试的时间及设备信息，同时在小游戏中会提示"性能测试中"

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/da9c3a344b2c4df2826875c588cd16c6)

1. 在测试完毕时，点击"停止"按钮或退出小游戏，可完成测试，之后在该页面可查看本次性能检测报告，检测报告包含：启动、运行、网络(如有请求)三个部分，详细解析请参考下文"指标解析"部分。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/af941549bb3245cfa54522c940252375~tplv-9nona0m7ha-image.image)

## 指标解析：
### 启动阶段：
- 首屏出现时间：首屏时间是指用户从打开小游戏看到第一屏主要内容的时间，首屏时间太长会导致用户长时间loading等待，影响使用体验。
- 首次可交互时间：小游戏点击到小游戏进入游戏画面，用户可操作游戏或可以开始游戏画面的耗时
- 代码注入时间：加载小游戏game.js的耗时，受初始代码大小的影响，代码注入时间过长会影响首屏出现时间。
- 渲染时间：从代码注入完成到看到首屏游戏画面的耗时，耗时过长会影响首屏出现时间，出现这一情况时，校验首屏资源复杂度，尽快渲染首屏。
- 小游戏包大小：包过大会影响小游戏启动耗时，应删除无用的图片资源及无用代码，并使用分包进行包大小优化，部分IAP游戏应符合分包限制。
### 运行阶段：
- 平均帧率：采样时间段内的屏幕渲染帧数/采样时间，可以使用纹理压缩、图集合并、渲染节点复用、降低模型复杂度、减少DrawCall数量等进行优化。
- 最大卡顿率：小游戏运行过程中的卡顿程度，卡顿时间/采集时间，控制计算复杂度与频率，避免密集任务扎堆，减少对象的临时创建，降低GC回收负担。
- 是否出现卡死：小游戏运行过程中是否出现JS线程卡死。
- 是否出现白屏：小游戏是否处于纯色屏，长时间纯色屏会导致用户离开。
### 网络请求：
- 网络请求次数：短时间内发起太多请求会触发小游戏并行请求数量的限制，同时太多请求也可能导致加载慢等问题，应合理控制请求数量，甚至做请求的合并等。
- 请求失败次数：检验一下上行参数是否准确，做好QPS评估，尽量保障服务器稳定。
- 请求最大耗时：host链接；请求的耗时太长会让用户一直等待甚至离开，应当优化好服务器处理时间、减小回包大小，让请求快速响应。
## Tips：
1、**unity 小游戏**性能测试工具需要将开发者工具更新至 **4.3.4** 版本及以上，并且保证抖音客户端版本为** 32.8.0** 及以上。
2、**普通小游戏**请使用抖音 30.1.0 及以上版本进行扫码，建议使用 **32.8.0** 及以上版本的抖音客户端：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/8bc286e9a77c4e39a5d0fdae59657cfb)

3、如有其他性能优化问题，请参考[性能优化文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/startup-performance/startup-scene-analysis)。
