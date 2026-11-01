---
title: "设备兼容手册"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/performance-optimization/device-compatibility
update_time: 2025-06-17
---

随着抖音小游戏底层能力的持续优化以及用户设备的持续更新换代，玩家对于游戏品质的期望日益攀升。在致力于提升游戏品质的同时，还得确保游戏能够广泛覆盖绝大多数游戏用户群体，这已然成为所有开发者都无法回避的重要课题。本文从大盘设备状况展开数据的收集与剖析，其核心目的在于助力广大游戏开发者制定出更为科学合理的技术选型策略。

> 数据周期：24年10月

## 01 大盘操作系统分布
从操作系统层面我们发现，抖音小游戏大盘以安卓用户居多，占比64.59%，iOS用户占比35.41%。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/6f2b4a8cae3548c98e5c1a519e79b310)

## 02 设备概况-Android
### 机型档位
从机型档位层面我们发现，抖音小游戏大盘安卓用户的设备档位主要集中在高端机型，高端机占比**61.92%**，中端机占比**29.80%**，低端机占比**8.28%**。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/80f722df7ab5413f9e12c32104eee247)

### 操作系统版本
从用户设备机型的操作系统版本角度来看，我们发现，**Android 10及以上版本**的用户，占据了抖音小游戏大盘**97%**以上的用户，在开发过程中，开发者应该时刻关注Android操作系统版本的变化，并注意不同版本之间可能存在的差异和不兼容的问题。
在发布抖音小游戏之前，也应该对游戏进行全面的测试，确保小游戏在不同的Android版本下都能够正常运行，开发者也可依据游戏自身的特点，通过[tt.getSystemInfoSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/device/system-information/tt-get-system-info-sync)获取用户设备系统版本，选择是否向下低版本的用户兼容相关游戏玩法。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2396117eeaf042289f941785b2c6741e)

### 设备内存
从用户设备机型内存层面来看，我们发现，当前**8G内存**机型的用户覆盖面最广，覆盖用户数占比达46.81**%**，**6G及以上**的内存成为抖音小游戏主流的设备内存，整体占比达到97.17**%**，4G用户占比2.67%，3G及以下的用户只有0.16%。
开发者应当适当关注4G及以下设备的用户，这些设备的内存容量较小，会一定程度上影响游戏的功能和运行效率，在开发过程中，可以通过[tt.getDeviceInfoSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/device/system-information/tt-get-device-info-sync/)获取用户设备的内存配置，尽可能适配这些设备，并对游戏进行全面的测试，确保抖音小游戏能够在这些设备上正常运行。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/281613ffa4294c9286aeab3f7c246e49)

## 03 设备概况-iOS
### 机型
从抖音小游戏大盘用户的机型层面来看，我们发现，占比前三的机型是**iPhone 13（12.6%）**，**iPhone 15 Pro Max（8.81%）** 和 **iPhone 14 Pro Max（8.22%）。**
iOS用户设备进行分布较为广泛，开发者在开发过程中应充分考虑用户的设备机型、档位分布、操作系统等各方面的因素，优先对主流设备进行游戏特性适配，而对于占比较小的机型，可以考虑进行适当的优化和简化游戏设计，以保证游戏流畅度和用户体验。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e14350c0d29b45b2a0126d0d71ac13e6)

### 机型档位
从机型档位层面我们发现，抖音小游戏大盘iOS用户中，高端机的设备占比高达**69.42%**，中端机占比**26.25%**，低端机占比**4.33%**。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/be751717ad1343679b4990c20e200e4e)

### 操作系统版本
从用户设备的操作系统版本分布来看，我们发现，**iOS17是目前占比最高的操作系统版本，占比达59.94%**，iOS16占比16.56%，iOS18占比11.90%，iOS15占比7.56**%**，iOS14占比2.86**%**，iOS13及以下的版本占比较低。在开发过程中，开发者应该关注不同版本之间差异，注意兼容一些早期版本无法支持的高级功能，以确保游戏的用户覆盖面更广。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/6d383ef6ef4d4747a9a43006f0647439)

### 设备内存
从用户设备机型内存层面来看，我们发现，**4G及以上内存**的设备机型占比较高，达93.6**%**，3G和2G内存的占比相对较低，分别是6.38**%**和0.06**%**。总体来看，抖音小游戏大盘用户的设备内存普遍较高，对于开发者来说，可以设计更为复杂、功能更强大的小游戏。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/bba7efdda4804a38ab6c25bc260c4185)
