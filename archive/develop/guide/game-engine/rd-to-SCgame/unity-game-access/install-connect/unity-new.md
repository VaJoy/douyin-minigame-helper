---
title: "Unity包体格式更新"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/unity-new
update_time: 2026-09-07
---

## 一、什么是Unity新旧包体格式
为搭建平台统一服务链路，平台推出了Unity新包体格式，提供完整TT API适用以及和普通小游戏同样的链路，支持上传多引擎产物，需要下载[TTSDK](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/install-sdk) 6.6.3以上版本并以新包体格式打包。
- 旧包体格式：仅针对过往Unity小游戏项目的包体格式，是平台早期为适配Unity引擎单独搭建的服务通道
- 新包体格式：平台统一的小游戏服务链路，支持所有引擎类型（Unity、Cocos等），是「引擎切换」能力的基础支撑通道，新创建的小游戏默认接入此链路。

> **注意**
> **旧包体格式后续不再维护，请尽快切换到新包体格式。**

#### 格式对比

旧格式：（zip文件）
主要产物内容在zip包文件中，game.json以及project.config.json负责项目相关配置。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/086597d2ef12494d9a142241600c08c5~tplv-9nona0m7ha-image.image)

新格式：（产物文件目录）
产物内容以及game.json,project.config.json 在同一文件目录中。其格式与普通小游戏类似

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/43cbf587bdb44cf6a9764e05acc1c1ce~tplv-9nona0m7ha-image.image)

---

## 二、接入评估
> 切换成 Unity 新包体格式依赖 6.6.3 以上版本的 [TTSDK](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/install-sdk)，并且使用“新包体格式”打包。
后续的Unity包体格式都**建议使用新包体格式**，新特性将主要围绕新包体格式进行开发。新格式虽然可以支持更多的特性，但同时也**存在一定的限制**。开发者可根据自身情况来决定是否使用新格式的包体。

| 新包体格式优势 | 新包体格式限制 |
| --- | --- |
| **系统支持：**额外支持鸿蒙系统； **启动优化：**开发者可通过控制 game.js 中的 `gameManager.startGame()` 调用时机来自主控制 Unity 的启动时机； 可动态更新预下载列表，预下载能力平均可降低 TTI 耗时 200ms； 支持自由编辑 JS 文件，相比于旧格式（zip）会更便捷的在抖音开发者工具中调试 JS 逻辑； 支持自定义构建模板，每次构建时会自动导入开发者在构建模板中配置好的文件和目录； 支持自定义加载图，通过自定义“wasm 编译阶段”的 loading 界面，获得更接近游戏原生的用户体验； 支持通过 File 接口读取包体内文件，更方便的利用首包放置游戏的配置文件等内容； 提供完整的 tt api 能力，旧包体格式下存在部分 api 不支持； 支持与普通小游戏相同命令行工具构建方式，使用命令行工具上传确保tt-minigame-ide-cli版本大于等于2.1.1 | **抖音低版本（<35.0.0）不兼容**，低版本用户启动游戏时会通过兜底页提示需要升级抖音版本； 部分宿主 APP 暂不兼容。当前支持抖音（包括鸿蒙）、抖音极速版、抖音火山版、番茄小说、红果短剧、番茄畅听/音乐（仅安卓），**后续将逐步开放其他合作方宿主能力，不支持的宿主app无法运行新包体游戏。** 如果你的项目中依赖了一些没有对外说明的内部全局对象、函数、变量等，在新链路下可能会由于对象不存在从而导致项目报错； |

## 三、接入流程
### 调试环境准备

| 工具 | 下载链接 |
| --- | --- |
| unity构建工具 | TTSDK需要使用6.6.3及以后版本 Unity   团结 |
| 开发者工具 | 抖音开发者工具更新到[最新版本](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/developer-instrument-update-and-download#a6bb6613)（>=4.4.3版本） IDE中需要设置调试基础库版本>=3.77.0.0 |
| 客户端 | 请使用>=35.0.0版本的抖音进行调试 |

### unity产物构建
> 参考文档：
> - 构建流程：https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_build
> - 团结引擎：https://docs.unity.cn/cn/tuanjiemanual/Manual/DouyinSDK.html
#### 2.1 自定义构建模板
平台侧会提供CustomizeTemplate用于游戏侧自定义构建模板配置，同时也会提供DefaultTemplate作为兜底构建模板；

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/fe3ff2ed7bab4462b0e16e579f23794c~tplv-9nona0m7ha-image.image)

- 构建时优先采用 CustomizeTemplate 模板的配置；若 CustomizeTemplate 不存在，则使用 DefaultTemplate 作为兜底构建；若 DefaultTemplate 也不存在，将以代码生成的 js 作为最终兜底方案。
- 每次升级构建插件，都会覆盖还原DefaultTemplate，开发者尽量不要对该目录下的文件内容进行更改。

#### 2.2 打开内测构建面板
构建面板路径：unity菜单栏选择`ByteGame` → `TTSDKTools` → `Build Tool`
#### **2.3 取消勾选** 「采用旧格式打包」
构建面板中**取消勾选** 「采用旧格式打包」，即可构建出新的包体格式结构。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/595008cb6cf54e389f29f9bc68d54326~tplv-9nona0m7ha-image.image)

#### 2.4 Native方案注意事项
**包体存放目录：**新包体格式下 Native构建产物默认与WebGL产物在同一目录下，其文件单独存放在`tt-minigame/native`文件夹下。
文件名以及文件夹固定，不可更改，否则无法识别。
详情见下图：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/0f46cac8a8bf499d9a7c17cdf169e821~tplv-9nona0m7ha-image.image)

**上传**：上传时需要在详情页勾选`Android端使用Native方式渲染`

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/db338e70baf3400994476537d8449751~tplv-9nona0m7ha-image.image)

#### 2.5 包体大小和压缩
切换新包体后，IDE上传包体会有[体积大小限制](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/dev-guide/bytedance-mini-game)（实际请以IDE上传时的报错弹窗为最终判断依据），因此建议打开压缩功能，能显著减少 wasm/data 文件大小，避免上传游戏被拦截。
提示：
- 平台针对这些压缩后的文件有特殊处理逻辑（预下载、预解压），开启压缩不会显著影响启动耗时
- 关于wasm分包大小，如果执行了wasm分包，IDE计算包大小时，会取AndroidWasm分包、iOSWasm分包的最大值，即 `总包大小 = max(AndroidWasm分包, iOSWasm分包) + 其他包`，而不是 `总包大小 = AndroidWasm分包 + iOSWasm分包 + 其他包`，因此不需要担心wasm分包后多出来的平台分包文件会占用多余的包大小

压缩开关位置如下：

| Unity | 团结 |
| --- | --- |

### 工程配置
#### 3.1 配置性能模式
**包含unity引擎构建产物**的游戏必须运行在性能模式下**：**
- 在通过构建工具导出时，会自动为项目配置[高性能模式](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/high-performance-mode)（game.json中的`enableIOSHighPerformanceMode`设置为true）；
- 如果需要设置为[高性能+模式](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/high-performance-plus-mode)，需要游戏侧在构建面板主动勾选；

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/27785baff4dd4cdf86f75519c1352b7f~tplv-9nona0m7ha-image.image)

#### 3.2 配置网络域名白名单
参考开发者文档中的[配置教程](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/basic-function/network)
检查是否配置完所有域名：
1. 首先对代码进行扫描，找到所有网络相关API（request、upload、download、connectSocket）的调用处，遍历url字段的入参，对涉及到的域名进行配置；
1. 开发者工具中**取消勾选**「不校验合法域名······」的配置选项（如下图），通过模拟器/真机预览进行游戏整体流程的测试；
1. 新包格式方案需要对游戏内使用的请求域名做配置申请，不申请的请求会被拦截。如果使用了ip地址做请求的，需要勾选【不校验合法域名】配置。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/f913f97008d742289a47d483c48eb1e6~tplv-9nona0m7ha-image.image)

#### 3.3 自定义启动图
这部分主要介绍启动图各个配置字段可以怎样进行自定义配置。

| 整体配置 | 配置项 | 释义 |
| --- | --- | --- |
|  | disableLoadingPage | true：不展示自定义启动图 false：展示自定义启动图【默认，推荐使用】 |
|  | hideAfterCallmain | true：在callmain阶段结束后立即隐藏封面视频 false：等待首帧渲染回调后隐藏【默认】 |
|  | designWidth designHeight | 设计图稿的宽高，未设置时默认为0，取设备宽高。 |
|  | scaleMode | 缩放模式，有以下取值： default / exactFit：视图完整填满展示区域，可能会因为拉伸而形变 noBorder / fixedWide：保持原有宽高比例，填满整个展示区域，视图部分内容可能被裁减掉 showAll / fixedNarrow：保持原有宽高比例，保证视图完整展示，四周可能存在空白 fixedHeight：保持原有宽高比例，高度填满，宽度可能会被裁减或留白 fixedWidth：保持原有宽高比例，宽度填满，高度可能会被裁剪或留白 |
|  | textConfig: {       firstStartText: '首次加载请耐心等待',       downloadingText: ['正在加载资源'],       compilingText: '编译中',       initText: '初始化中',       completeText: '开始游戏',       textDuration: 1500, }, | 加载阶段的展示文案： webgl子包下载阶段 `downloadingText[n](firstStartText)` 包下载并加载到内存 n个downloadingText循环轮播，轮播速度为textDuration（单位为ms） 编译阶段 `compilingText` wasm编译过程 初始化阶段 `initText` callMain启动unity游戏 初始化完成阶段 `completeText` callMain结束，等待首帧到达。根据hideAfterCallMain配置决定是否移除自定义加载页 |
|  | textConfig: {      // 文字样式       style: {         bottom: 85,         height: 17,         width: 280,         color: '#ffffff',         fontSize: 13,       },     }, // 进度条样式     barConfig: {       style: {         width: 280,         height: 12,         padding: 2,         bottom: 69,         backgroundColor: '#ffffff',       },     },     // 一般不修改，控制icon样式     iconConfig: {       visible: true,       style: {         width: 106,         height: 40,         bottom: 141,       },     }, | 文字、进度条、logo样式。 `bottom`：相对于设计稿底部的偏移 `height`：高度 `width`：宽度 `color`：文字颜色 `fontSize`：文字大小 `padding`：进度栏与进度条的内间距 `backgroundColor`：进度条的颜色 `visible`：logo图是否可见 注： 对于进度条样式而言，width、height和bottom都是**进度栏**的设置 颜色的配置支持三种配置方式： 十六进制：'#ffffff'【推荐使用】 rgb/rgba：'rgb(255,0,0)'、'rgba(166.0, 200.0, 255.0, 0.1)' 部分常见颜色支持语义化配置：'red' 、'green'【不推荐使用】 |
|  | materialConfig: {       backgroundImage: 'images/background.png',        iconImage: 'images/unity_logo.png',  }, | 加载页的素材配置，其中`backgroundImage`为背景图，`iconImage`为logo图。 素材支持三种配置方式： http/https协议：网络图 ttfile协议：通过文件api保存的图 包体内置的图 |

## 四、常见问题（FAQ）
- **Q1：已创建的小游戏项目，如何判断是否需要迁移至Unity新包体格式？**
- A1：平台后续不再维护Unity旧包体格式，请尽快迁移
- **Q2：迁移至Unity新包体格式后，原小游戏的运营数据（如用户数据、收入数据）是否会受影响？**
- A2：不受影响
- **Q3：迁移新包体后，IDE提示包体大小超过限制**
- A3：
  - 优先检查是否开启了包体压缩选项，这会显著降低data/wasm文件的大小
  - 如果开启包体压缩后，IDE 仍警告包体大小超过限制，再考虑 [Data CDN 功能](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/packaging-release/webgl-data-cdn-tutorial) 把 data-package 数据放到厂商自己的 CDN 服务器上，绕开平台的包大小限制
    - 警告：Data CDN 功能会绕开平台的预下载、预解压，导致启动耗时有一定的劣化，请谨慎开启
- **Q4：迁移新包体后，预览码启动速度变慢**
- A4：预览码状态下，由于IDE生成的临时预览包体没有压缩，包体偏大，下载耗时长。目前线上的包体、或者测试包会有压缩，启动速度会基本和旧包体持平。预览码时可以考虑开启局域网调试，加快文件下载速度（缓解问题）。真正要测试启动速度的话，建议使用测试版本，如果测试版本启动速度也变慢了，请联系我们排查。
- **Q5：迁移新包体后，Android 画面清晰度下降**
- A5：可能是历史逻辑中对于双端的 DevicePixelRatio 设置不同导致，建议排查 SetPreferredDevicePixelRatio 接口调用，确认双端传入参数是否相同。
