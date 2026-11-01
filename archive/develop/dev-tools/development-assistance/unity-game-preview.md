---
title: "Unity小游戏预览调试"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/development-assistance/unity-game-preview
update_time: 2025-06-04
---

## 功能概述
使用抖音开发者工具扫码调试 Unity 小游戏，相比于使用 SC StarkTool 工具先上传 Unity 项目，再扫描测试版二维码来说更加便捷:
1. **统一鉴权登录：**抖音开发者工具使用统一的鉴权登录，无需开发者手动获取uid；同时开发者工具能自动获取开发者名下的应用列表，无需手动填充 appid。
1. **无需重复发布：**扫码预览调试无需开发者输入版本号和上传日志，避免了调试次数过多导致的无用版本号较多和版本号较大问题。
1. **速度更快的局域网调试：**扫码预览调试提供了本地局域网调试的模式，相对于走线上远程编译，局域网编译有着更快的速度，能够更快地获取预览二维码。
1. **无需连接真机：**当选择 Android Native 相关方案时，扫码预览调试无需使用数据线连接安卓真机，通过抖音客户端扫码的方式即可完成调试。
1. **项目协作更友好：**同一游戏的多位开发者可以使用不同版本同时进行预览，互不影响。
## 支持版本
**抖音开发者工具**需要 **4.2.7** 及以上版本，SC StarkTool 需要 3.30.7 及以上版本，Android & iOS 抖音客户端需要 27.3.0 及以上版本。
## 导入Unity项目
当开发者使用 SC StarkTool 构建Android Native 游戏或者 WebGL 游戏后，构建工具会在项目根目录下生成`project.config.json`和`game.json`文件。当生成以上两个文件后，开发者就可以将Unity游戏项目导入到抖音开发者工具，并通过抖音开发者工具进行预览调试和上传。

构建webgl

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/45355df0fbda4311aa3cb737029950f4)

导入开发者工具后的项目目录

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ca886220f9fc4099b6b5179679ca9952)

### 操作引导
1. 打开抖音开发者工具，选择小游戏tab，然后点击导入

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e689592da9d240a9af2cab932bf3c8ea)

1. 选择经过 SC StarkTool 构建后的 Unity 项目目录路径（路径下存在`project.config.json`和`game.json`文件），然后点击**导入**按钮。此时便已完成导入工作。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a9b1542a0a614dc6a7c1399ca0a2f412)

## 扫码调试预览
### 操作引导
1. 点击扫码调试按钮。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/bdc5ff8a772d4bcea03c292cc361a026)

1. 点击右上方【详情】按钮，可选方案、产物文件位置、屏幕方向和胶囊按钮颜色。
   1. Android Native 方案，需要传入`完整 APK `文件，具体构建方法请见下文。
   1. Webgl 方案需要传入 starkSDK Unity 调试工具构建的 `zip` 产物文件。
   1. Instant Game 需要传入构建的 `json` 文件。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e7212329ac2349f99bb892f63b044cbb)

1. 点击【预览调试】按钮后，会进行构建产物文件的上传和编译，最后获得扫码预览调试二维码。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f45219d85ed4498682ec22ebdbd89454)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ee5bca3a6bdd49398682d1d60409bf8c)

1. 当构建新的产物并需要重新生成预览二维码，开发者可点击返回设置按钮，重新选择、填写配置。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/0a595a339f97438f89379a1a265bab00)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4af59d5346f0492eadd6521953948061)

### 局域网快速调试
设备和开发者工具在同一局域网中时，可使用局域网快速调试。开启后可显著提高出码速度。有多个本地网卡时，可手动切换IP，确保局域网设备可访问。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1b9bf3de93a84658ac38fd6579d2a298)

**注：**
- 开发者若首次使用扫码预览调试功能时，请先使用广域网调试（即不勾选局域网快速调试）。否则可能出现获取不到二维码的情况。
- Android Native 方案不支持局域网快速调试。
### Android Native方案

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/46a42b6617ad413787668ec01bd140d9)

当开发者在预览时选择了Android Native相关方案时，需要使用SC StarkTool 3.30.7 及以上版本构建一个完整的apk文件，apk产物文件也需要选择对应的完整apk文件，无需上传il2cpp文件。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/cb929394f3ce4acc94248296a4d854b3)

### 添加编译模式
C# SDK 提供接口获取 Unity 小游戏的[启动参数](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#e939bf70)：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/5f7fde460bd6468a8c48a777f3c0036f)

在抖音开发者工具（** 4.2.8 **及以上版本支持）中，开发者可通过添加编译模式，模拟设置启动参数和启动场景值：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/5ef8c15dbd194835952084ac0367181c)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a0bfd7d87fc74df6a48b51cac032675c)

设置完毕后，点击预览按钮，填写相关配置并扫码，即可模拟获取启动参数和场景值。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a5e26b9535b248d59652174c26c646f7)

## IDE 命令行工具
[查看文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/development-assistance/ide-cli)
## 注意事项
1. 当出现以下几种情况时，手机端会提示**加载失败。**
   1. 若勾选局域网快速调试，请确保手机和运行抖音开发者工具的 PC 处于同一局域网下。若两个设备不在同一局域网下，开启局域网快速调试手机端扫描预览调试二维码后，手机端会提示加载失败。请开发者确认手机和运行抖音开发者工具的 PC 是否处于同一局域网下。
   1. 当选择仅安卓的发布方案（仅安卓 native，仅安卓 webgl，仅 instant game）时，使用 iOS 设备扫描二维码，手机端会提示加载失败。请开发者选择 iOS 相关的发布方案或者使用安卓设备扫码预览调试。

**iOS**

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/de96330a201c43bc94d363f74b035ef7)

**安卓**

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/323979089e5141df9f3f4e0ad9679c98)
