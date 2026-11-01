---
title: "IDE 调试"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/game-debug/ide-debug
update_time: 2025-06-16
---

## 简介
IDE 本地支持多种调试能力，包括模拟器模拟操作，调试器工具调试等。

## 模拟器调试
模拟器是模拟抖音小在抖音 App 真实的逻辑表现和运行环境。绝大部分的 API 在模拟器上的表现与客户端一致。模拟器支持机型、缩放比例、网络等模拟，同时也支持与小能力相关的功能模拟，比如定位、罗盘等。
更多内容可以参考[模拟器](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/mini-app-developer-instrument#aeed33d6)。

## 调试器调试
配合模拟器，IDE 提供了定制化的调试器，在其基础上提供更多扩展。默认展示如下图所示。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/2da821fa30214190a27b535684cdcd70~tplv-9nona0m7ha-image.image)

### Console Panel
开发者可以在此输入和调试代码，程序中的 console 信息也会在 Console Panel 中提示。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/29cd8e3817a44e6d8ad8a3e82de8c4ef~tplv-9nona0m7ha-image.image)

### Sources Panel
Sources Panel 面板用于查看、断点调试项目源码。整个面板分为资源列表、代码编辑区域、调试区域三个部分。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/020dc9392f1244dab8271d595cc98b6e~tplv-9nona0m7ha-image.image)

#### 断点调试
在 Source 面板中可以设置断点，对小游戏进行断点调试。

Sources 面板用于显示当前项目的脚本文件。字节小游戏框架会对脚本文件进行编译的处理，所以开发者在 Sources 面板中看到的文件是经过处理之后的脚本文件。实际上开发者的代码都会被包裹在 define 函数中，并且对于 Page 代码，在尾部会有 require 的主动调用。
> 注意，当代码运行到断点的时候，整个小游戏进入停止状态，此时模拟器会出现白屏或者无法操作的情况。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/9811f1b338954194b396e7781a81ce69~tplv-9nona0m7ha-image.image)

### Network Panel
Network Panel 中展示了 request 和 socket 的请求情况。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/8e335b10dafa401a904641550f909917~tplv-9nona0m7ha-image.image)

### Storage Panel
Storage Panel 用于显示当前项目使用 [tt.setStorage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/data-caching/tt-set-storage) 或者 [tt.setStorageSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/data-caching/tt-set-storage-sync) 后的数据存储情况。可以直接在 Storage Panel 上对数据进行新增、删除（按 delete 键或通过右键菜单）、修改等行为。
修改后的数据将直接影响 [tt.getStorage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/data-caching/tt-get-storage) 或者 [tt.getStorageSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/data-caching/tt-get-storage-sync) 的回调运行结果。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/bdf0311656bb4a18b07ef58000850a9b~tplv-9nona0m7ha-image.image)

### Sensors Panel
Sensors Panel 主要是用于模拟加速度和陀螺仪数据。该面板目前支持模拟 [tt.onAccelerometerChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/jerkmeter/tt-on-accelerometer-change) 和 [tt.onGyroscopeChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/gyroscope/tt-on-gyroscope-change)。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/92ea9f66694b4ff88fad2e6bd6052127~tplv-9nona0m7ha-image.image)
