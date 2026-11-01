---
title: "iOS高性能、高性能+真机调试"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/game-debug/ios-debug-performance
update_time: 2025-09-29
---

## 背景
小游戏在 iOS 上支持 [高性能](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/high-performance-mode) 、 [高性能+](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/high-performance-plus-mode) 模式，提升 JS 代码的运行效率。
此前这两种模式下， iOS 无法进行真机调试。
现在已经支持这两种模式的真机调试能力，Mac 、Windows 均可以使用。

## 版本要求
- 开发者工具 IDE 版本 >= 4.4.6
- 抖音版本 >= 36.1.0
- 基础库版本 >= 3.88.0.0
- iOS 系统版本 >= 16.4

## 支持能力
1. iOS高性能模式、高性能+模式真机调试
1. 调试面板支持 Console 、Sources 、 Network 、 Storage
1. Network 支持查看 tt.request、tt.downloadFile、tt.uploadFile 数据

## 前置准备
其他前置条件，例如配置真机调试设备权限等，请先参考 [普通模式真机调试](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/game-debug/real-machine-adjust) 。
这里只说明高性能、高性能+特有的前置准备。

### Mac 前置准备
1. 确保 IDE 所在的 Mac 电脑已安装如下包：
  - libplist
  - libusbmuxd
  - libimobiledevice
命令行示例：
`brew install libplist libusbmuxd libimobiledevice`

1. 配置 iOS 设备，开启网页检查器：【设置】-> 【Safari浏览器】->【高级】-> 【网页检查器】

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/9f561ca2dac6492eb2f9ffcef892762f~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/f8ef54b7f2694c6f86bffb6ab26d39e4~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/07a11a59ab9141809666a6159f13f6ca~tplv-9nona0m7ha-image.image)

1. 通过 USB 数据线，将 iOS 设备连接到 IDE 所在 Mac 电脑，iOS 设备信任Mac，Mac允许配件连接

1. 确认 iOS 和 Mac 连接正常
   1. 参考 [Enabling Web Inspector ](https://webkit.org/web-inspector/enabling-web-inspector/)开启 Mac Safari 的【开发】子菜单
   1. iOS 手机上用 Safari 任意打开一个网页
   1. 确认 Mac 上的 【Safari】-> 【开发】-> 【你的iPhone】，能看到手机上打开的网页，如下图

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/61c539f6862c4206908231f221df5257~tplv-9nona0m7ha-image.image)

### Windows 前置准备
1. 安装 iTunes，以下两种安装方法任选其一：
   1. Windows 商店安装
   1. 或者 [Apple iTunes 官网](https://www.apple.com/itunes/) 下载安装包，获取安装包路径如下：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/c4b8796b94d0496490ffccbb939c6f80~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/8095e99f09b047f999bd00bf1f1764cb~tplv-9nona0m7ha-image.image)

1. 配置 iOS 设备，开启网页检查器：【设置】-> 【Safari浏览器】->【高级】-> 【网页检查器】
（同上面的 Mac ）

1. 通过 USB 数据线，将 iOS 设备连接到 IDE 所在 Windows 电脑，iOS 设备信任 Windows 电脑，Windows 允许手机连接

1. 确认 iOS 和 Windows 连接正常
   1. Windows 打开 iTunes ，确认能看到 iOS 手机（可能要稍等几分钟），如下图
   1. 如果看不到手机，建议重启 Windows 电脑，或者安装 Apple 官网的 iTunes 版本后重试

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/44280c10a533489e8f1b1157e65e3b32~tplv-9nona0m7ha-image.image)

## 开始调试
前置条件均满足时，按照正常流程，点击“真机调试”生成二维码，iOS扫二维码即可，game.json 配置小游戏高性能模式（或者高性能+）。
**注意**：只支持一台 iOS 设备和电脑 USB 连接，请拔除调试设备外的其他iOS设备。

## 已知问题
1. Windows 电脑生成真机调试二维码时，会出现防火墙提示，允许即可。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/8addd285e1ef401983709a4ee949053f~tplv-9nona0m7ha-image.image)

1. iOS 调试设备如果出现网络断连，无法像普通模式那样点击“重连”按钮继续调试，只能重新扫码开启新的调试。
1. 高性能、高性能+ 真机调试同时要求网络连接和 USB 连接，两条链路承担的功能不同，缺一不可。
1. 如果扫码后，出现真机调试失败弹窗，提示 USB 连接有问题。除了检查 USB 连接之外，也请确保相关前置条件已满足，例如【 Mac 依赖包是否安装】、【 Windows 是否已安装 iTunes 】，这些前置步骤失败也会导致 USB 通信出现问题。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/9b278a141932498c8b466723833d3a3f~tplv-9nona0m7ha-image.image)

1. 调试工具 Console 面板中，函数声明后，无法在全局空间中使用，这是由于高性能、高性能+模式的沙盒限制导致的。如果要在全局使用函数，建议使用变量赋值存储函数，如下图：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/48d76ec833ba4b18afb24ebb4da57e7b~tplv-9nona0m7ha-image.image)
