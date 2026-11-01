---
title: "构建与调试"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/packaging-release/sc_build
update_time: 2026-03-30
---

## **构建**
Unity 菜单栏选择：`ByteGame` → `TTSDKTools` → `Build Tool`。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/5c132ed686c8461584d7278ec078c84d)

*图1：构建工具位置*
### **Android Native构建**
#### 界面

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f9c39491f3b44596a9da166024d2fc82)

#### 界面描述
##### 配置项
- **运行框架选择：**当前使用的构建平台，目前有Native 和 WebGL两种
- **游戏AppId：**当前游戏的AppId（可在 [**小程序开发者平台**](https://developer.open-douyin.com/) 中查询），**不可为空。**
（检查：AppId 的数字结尾必须是 07，且长度是 20 位。如果不满足条件，需要重新申请。）
- **宿主选择：**头条、抖音、抖音Lite（单选：在哪个宿主下运行,为调试时所使用的宿主，不影响发布时的宿主选择）
- **运行版本选择：**当前只有Latest** (测试版) **环境（单选，且只能选这个）
- **文件名：**构建APK的文件名前缀。构建APK时必须填写，否则构建按钮将无法使用
- **输出目录**： 构建APK的输出目录路径，若目录不存在会构建APK时尝试创建目录。
- **开发者工具路径：**最新版本支持使用[抖音开发者工具](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/developer-instrument-update-and-download)发布，如果需要使用抖音开发者工具发布时，可配置此项。此路径为[抖音开发者工具](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/developer-instrument-update-and-download)的的可执行文件的路径，请安装后进行选择，Windows下以exe结尾，Mac下以app结尾。与`开发者工具发布`按钮配合可跳转至抖音开发者工具进行发布操作。
- **上线前参数确认**：主要用于发布APK时需要确认的构建参数（可以点击**一键设置**，自动设置为发布APK时需要的构建参数。）
   1. **脚本实现：**需要为 IL2CPP
   1. **CPU架构：**需要为 All
   1. **最低Android版本：**根据实际情况选择
   1. **Strip Engine Code：**不能勾选
- **其它设置**（仅调试用）：
   1. **Dev版本：**是否构建 Development 版本
   1. **压缩方法：**可选择，**None**(不压缩)、**LZ4**、**LZ4HC**
##### 功能按钮
- **导出小游戏包: **导出 Android 工程，构建出`launcher-release.`APK以及`il2cppOutput.zip`，这两个文件可用于后续的版本发布（但无法通过高级选项中的【运行本地APK】运行此APK）
- **构建完整**APK**：**构建出一个完整的APK文件。构建完成后，可选择跳转至开发者工具进行预览调试，也可在当前工具直接调试（需连接手机，且开启USB调试）。
- **版本发布：**将跳转至版本发布界面
- **开发者工具发布：**将启动前面配置的`开发者工具路径`的抖音开发者工具，并将工程导入抖音开发者工具中
- **运行本地**APK**：**选择本地APK在真机宿主中运行调试。APK须为完整的APK文件，通过Unity自带的构建以及【构建并真机】运行出来的APK可以通过此按钮运行，导出小游戏包的APK不可以通过此按钮运行（需连接手机，且开启USB调试）
- **清除版本缓存：**清除手机上的抖音Unity小游戏缓存文件，可选择**Latest版本**和**所有版本**（需连手机，且开启USB调试）
### WebGL构建
#### 界面

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/c22ee19878864e01987c6842c300499b~tplv-9nona0m7ha-image.image)

#### 界面描述
##### 配置项
- **构建选项选择：**与 Unity 提供的 BuildOption 选项一致，无特殊需求选择None即可。
- **WebGL输出目录**： 构建WebGL时必须填写，若目录不存在会构建WebGL时尝试创建目录。
基本参数填写完毕后已具备构建条件。
- **是否采用旧格式打包**： 早期Unity的包体格式是一个zip包，后续架构升级，包体格式升级为与普通小游戏包体格式类似。详情见：[Unity包体格式更新](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/unity-new)
- **UnityHeap：**设置WebAssembly的初始内存的大小，建议根据游戏类型设置合理的数值，不建议游戏过程中频繁触发增长，详情见：[WebGL 中的内存](https://docs.unity.cn/cn/current/Manual/webgl-memory.html)
- **音频资源url： **开发者在使用音频时如若出现问题可尝试此方案。为游戏资源CDN url前缀，目前主要是用在播放网络音频url文件时会用到。详情可以参考[音频适配指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc-webgl-audio)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/25abfc6a911c4a20a87880dcb0bed9cf)

- **复制音频文件：**是否将工程中的音频文件复制出来。如果勾选，在构建WebGL成功后，会自动将工程中的音频文件复制到WebGL输出目录下的名为Assets子目录中。可以直接将该目录上传到CDN上。
- **WebGL2：**iOS支持15.0及以上系统，[Android WebGL2.0支持](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/android-webgl2)。
- **是否Brotli压缩：**使用Brotli压缩，可以将包体减小，但是打包速度会有所下降。未经过压缩的包只能用于发布测试版本，正式上线需勾选，否则会影响线上加载效率。
- **首包资源加载方式**：6.7.2版本之前均为Package（即data文件默认在data-package文件夹下，随包体下发），6.7.2版本新增CDN模式，data文件被剥离出data-package，只保留game.js。data需要开发者自行上传到指定CDN上，并在编辑器的【游戏资源CDN】中填入CDN前缀，运行时会自动拼接url进行下载。这是为了规避新包体格式总大小30MB的限制。
- **缓存资源域名列表：**如果有下载的资源需要自动缓存的，在此区域填写相应的域名信息，不支持通配符。比如下载资源url是https://cdn.bytedance.com/resource.data，这个文件需要被缓存下载，此处填写域名cdn.bytedance.com，这样当下载这个资源时底层会自动缓存下来。更多相关信息请查看[使用新文件系统说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_new_file_system)
- **不自动缓存的文件：**你有不想缓存的资源文件，比如像aa资源的catalog.json文件，那么你可以在"**不自动缓存的文件**"列表中填写文件信息，匹配规则是文件名后缀匹配，你可以填写.json，也可以填写catalog.json，不支持通匹符。
##### 功能按钮
- **构建WebGL：**构建后，在`WebGL的输出目录`将生成`webgl_package.zip`文件，可用于发布。另外同级目录还会包含WebGL文件夹，可运行于本地搭建的Http服务器用于调试。
- **Wasm分包：**Wasm分包功能主要是为了减小游戏运行时的首包大小，将原始wasm二进制文件拆分为2个，运行时先加载一个较小的wasm二进制文件，以较快速度进入主场景中。更多相关信息请查看：[Wasm分包工具说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/code-upload/sc_webgl_split)
- **转换WebGL包：**此功能可以将Unity构建出的内容转换成可以发布的WebGL包体，它将读取`WebGL输出目录`下的webgl文件夹，以此文件夹下内容作为输入，将其转换为可发布的WebGL包体。
- **版本发布：**将跳转至版本发布界面
- **开发者工具发布：**将启动前面配置的`开发者工具路径`的抖音开发者工具，并将工程导入抖音开发者工具中
## 调试

> 已支持多种方案的预览调试，开发者无需发布版本即可进行预览调试。

具体调试流程可见文档：[Unity小游戏扫码预览调试](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/development-assistance/unity-game-preview)
WebGL 模拟器使用方法可见文档：[Unity Webgl 模拟器](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/development-assistance/unity-webgl-simulator)
