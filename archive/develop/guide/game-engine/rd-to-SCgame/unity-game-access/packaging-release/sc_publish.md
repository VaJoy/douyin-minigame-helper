---
title: "发布"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/packaging-release/sc_publish
update_time: 2025-12-11
---

> 文档说明：本文档描述抖音 Unity 小游戏的构建，本地测试及发布各环节。
> *了解更多：*[**抖音 Unity 小游戏接入指南**](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide)** 。**

## **使用必读**
- 为了体验更好，提供的首包（32 位+64 位）尽量要**小于 60**M（关闭 StripEngineCode）。
- 安全性考虑，**不允许**在项目中加入原生 Java 代码库。
- 有限支持部分开源且著名的第三方 so 库。
- **会做安全性扫描，如对抖音有破坏性行为，会封停账号，保留追究司法责任的权利。**
## **如何发布抖音 Unity 小游戏**
发布需要以下流程，前面已经讲过如何进行构建，本章将重点介绍如何进行**送测：**
1. 构建：通过 TTSDKTools **构建（Build）**[**构建与调试**](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_build)。
1. 送测：通过 【TTSDKTools】或【抖音开发者工具】发布 latest 版本到测试环节。
1. 提审：登录[**抖音开放平台**](https://developer.open-douyin.com/)**，**跳转至【版本管理】**，**进行测试，完毕后点击【**提交审核**】。
1. 发布：审核通过之后，登录[**抖音开放平台**](https://developer.open-douyin.com/)**，**跳转至【版本管理】，点击【**发布**】。

> 送测版本统一称为 latest 版本，后续将不再赘述。

### 使用抖音开发者工具发布

> 需要提前下载好[抖音开发者工具](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/developer-instrument/download/developer-instrument-update-and-download)，版本不低于 **4.2.2，TTSDK 不低于 6.2.0。**

开发者可使用抖音开放平台账号登录抖音开发者工具，在上传时开发者工具可自动获取对应开发者账号下的 uid，开发者无需手动填入。同时，开发者工具也可自动获取对应开发者账号下的小游戏 AppID 列表，开发者无需手动填入 AppID。
#### 入口
在构建工具界面的开发者发布按钮，如图所示：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/26d509fde9b6499ba9db4a36c62a0300)

#### 跳转至抖音开发者工具
跳转至抖音开发者工具前，需要配置开发者工具路径，Windows 下是以 exe 结尾的，Mac 下是以 App 结尾的路径。如下图所示：

Windows：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/6392bdeb12c3412682a8366cc806af70)

Mac：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/5c2084f274e742e19a1c4880f9d064b0)

抖音开发者工具将自动将 Unity 工程导入。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4c93afb06944489190187a19c0011f5e)

#### 登录开发者工具
开发者可选择使用在抖音开放平台注册的邮箱或者手机账号登录抖音开发者工具。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b997c9b35488430e948fe9287a91b67a)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b559eb0c69c7423093cd78860cb94ef6)

#### 进行发布
- 点击左上方的【上传】按钮即可进行发布操作。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f8e01e13a9744fef827104ec90c8f4e7)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/875f040362874f5096b73f33f93153eb)

- 选择右上方【详情】按钮，可选择发布方案、产物、胶囊按钮颜色和屏幕方向等信息。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/8ed6521cf0b9489ba4262200b0de3e22)

- 为满足开发者多项目并行测试的需求，支持最多同时上传 25 个测试版本，上传时分为“默认通道”和“通道 1-24”。
   1. 未开启“选择测试通道”时，系统将在上传成功后覆盖“默认通道”已有的测试版本。
    
![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/64499bbec6764f69b3e75f735a808d58)

   1. 开发者如需同时保留多个测试版本，可以开启“选择测试通道” ，并根据需求选择默认通道或通道 1 - 24 进行上传。系统将在上传成功后覆盖所选通道的测试版本。默认通道和通道 1 - 24 通道的测试版本互不影响。
    
![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4410777efd2f4028aed254fe1601815a)

   1. 除开发者工具外，[CLI](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/development-assistance/ide-cli#d6dd6956) 也支持指定测试通道进行上传。
   1. 如果当前版本号 ＋ 通道号已经上传过小游戏，则无法被覆盖。例如，1.3.20-通道 1 已经上传成功，那么无法再次上传 1.3.20-通道 1 版本，可上传 1.3.20-通道 2/3/...等版本。
   1. 多测试版本能力只支持抖音、抖音极速版、抖音火山版（>=31.6.0）。如想在其他宿主上测试：
    - 需要保证默认通道上有上传测试版本。
    - 无论扫哪个测试通道的二维码，最终都只会打开默认通道上的测试版本，故请将要扫码体验的测试版本上传到默认通道。
#### 其他
- 如何修改 AppID。
  - 可在项目文件中的 project.config.json 以及项目详情中进行修改。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1d42d3f7df0d465b87404a3df181a681)

  - 也可点击抖音开发者工具右上方的详情按钮，选择当前登录的开发者账号下有权限的 AppID。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/61771b76fceb491897036e841245a614)

- 获取测试二维码。
  - 可点击抖音开发者工具工具栏的`测试二维码按钮`获取最近一次发布的 Unity 小游戏二维码，开发者可使用抖音客户端扫码查看效果。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f9d143775af14370b0d4cfc900084917)

### **使用 TTSDKTool 发布**
> 在版本 4.0.2 之后，TTSDKTool 将不再支持发布能力，建议开发者尽早将发布能力迁移至抖音开发者工具。
#### **入口**
菜单栏选择 ByteGame => TTSDKTools => Publishing Tool。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/09bd2bcc149e4a74a63ec87a68321950)

#### 发布界面

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b5e0a1adda314a868fb736f87513fa63)

##### **Uid：**
请使用抖音开发者工具，打开项目后，在右上角点击详情后获取。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a12e9996cc9b4c93b1cb6ae5655497a7)

##### **游戏 AppId:**
在开发者平台申请的小游戏 AppID（检查：AppID 的数字结尾必须是 07，且长度是 20 位。如果不满足条件，需要重新申请）。
##### **版本号：**
1. 点击『**获取可发布版本号**』按钮，可以获取**线上测试版**的版本号并+1 作为新的版本号进行填充。
1. **自动版本号：**勾选自动版本号后，会隐藏『获取可发布版本号』按钮，版本号填充区域将不可编辑，在打开此发布界面或者后续的提交发布时，会自动地获取当前测试版本号并自动+1 作为新的版本号填充。
  第一次选择自动版本号会遇到以下问题，无需担心，版本号会自动补充 0.0.1。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/6cd8719ec610400da8ed3c9706529668)

1. **手动填写：**版本号应大于当前测试版本的版本号。
##### **方案类型：**
此选项代表可发布的方案类型，共提供了 6 种发布方案的类型供开发者选择。选择不同的方案类型，下方出现的文件选择框也将不同。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/2c5c5bb127314240bd90e8bfffdaaf1b)

- Android Native Only（仅 Android Native 方案）。
- Android Native ＋ iOS WebGL（Android Native ＋ iOS WebGL 方案）。
- Android WebGL ＋ iOS WebGL（Android ＋ iOS WebGL 方案）。
- Android WebGL Only（仅 Android WebGL 方案）。
- Unity Instant Game Only（仅 Instant Game 方案，IG方案已不再支持，请勿接入，仅保留更新入口）。
- Unity Instant Game ＋ iOS WebGL（Instant Game ＋ iOS WebGL 方案，IG方案已不再支持，请勿接入，仅保留更新入口）。
其中文件选择框将会包含以下几种：
  **IL2CPP 文件：**【导出小游戏包】生成的 il2cppOutput.zip 文件。
  **Apk 文件：**【导出小游戏包】生成的 illauncher-release.apk 文件。
  **WebGL 文件：**【构建 WebGL】或【转换 WebGL 包】生成的 WebGL 的 zip 文件。
  **IG 文件：**只能选择 Json。
**注意事项：**
Unity 发布工具支持仅发布 Android 端，或支持发布 Android+iOS 双端。但请注意，如果游戏支持双端，每次发布时，不论 iOS 或 Android 游戏包是否有更新，都需要上传游戏包（即，Android 与 iOS 的包都需要包含），否则会导致 iOS 端游戏被下线。
举例：如果之前线上支持 Android、iOS 双端，本次发布仅选择了 Android 端（比如 Native 方案的 apk），则在审核时就不会有 iOS 端的游戏版本，审核通过后也就没有了 iOS 端的入口。
原因：Android 和 iOS 是作为一个“游戏版本”来发布的，线上只能有一个游戏版本，每次发布是一个原子操作。
##### **屏幕方向：**
根据游戏实际情况选择。
##### **胶囊深浅色：**
主要是指游戏运行时，小游戏的框架按钮的颜色。

浅色：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/5d5a89c1fe1f43e68ba3f07e69924aa6)

深色：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/7f10e86c55ea474087f762dbd0b2f293)

游戏开发者可以根据自己的游戏选择胶囊的深浅色来让用户获得沉浸式的体验。
其配置相当于[小游戏配置](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/mini-game-configuration)中的`MenuButtonStyle`字段。
##### **发布描述：**
游戏发布的描述。
#### **进行发布**
需要解决红色警告后提交发布按钮才会可用。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/08bf879f40274aabbe54a02727dd67ff)

##### **提交发布：**
**信息确认：**

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/029adbae043e45ec89eeec21b76a73e0)

在弹出信息确认框内需确认以下元素：
**文件名：**确认是否正确。
**文件大小：Native 方案**最大不能超过 100M， **WebGL 方案**最大不能超过 100M。
**版本号：***如版本号是手动填写，建议检查版本号是否在上次基础上 +1。*
确认无误后点击 **“发布”** 按钮，否则取消返回修改。
发布成功后将进入**测试**环节。
发布方案中包含 Android Native 方案时将会比较慢，会逐步显示发布状态。最终发布成功将出现以下信息展示：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e1541101ac5d4ec0884c22ac967dec34)

##### **生成二维码：**
发布成功后，可以生成二维码，然后使用抖音等 App 扫码测试。
*刚发布的 Apk 生成的二维码建议等待 2-5 分钟后再扫码。*
##### **查询状态**：
查询发布状态。点击该按钮会向服务器端请求当前发布状态，并将结果显示到界面上。

### **测试环节**
发布成功之后，游戏版本会自动进入测试环节。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/9ef9a98e9e764bbc93904ccb248b0e60)

*图 9：测试版本。*
- 登录[**抖音开放平台**](https://developer.open-douyin.com/)**，**跳转至【版本管理】进行测试。
- 测试完毕后，点击【提交审核】来进入审核环节。具体请参考：[**审核指引**](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/unitygame/examine-verify)**。**

### **审核环节**
提交审核后，进入审核环节。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/6733dad258c64dc98bd3e13f4c8aa00e)

*图 10：审核中。*
- 登录[**抖音开放平台**](https://developer.open-douyin.com/)**，**跳转至【版本管理】进行查看。
- 审核通过后可进入发布环节。

### **发布环节**
版本审核通过后，开发者点击“发布”，小游戏即可发布上线。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/9b7049de34914f6888b65318c5a019fc)

*图 11：发布。*
登录[**抖音开放平台**](https://developer.open-douyin.com/)**，**跳转至【版本管理】，找到审核通过的游戏，点击【发布】。
请参考[**发布指南**](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/release)**。**

## [**FAQ**](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_faq)
- **Q：**首次接入的游戏，本地调试的时候出现扫码白屏『游戏加载失败』现象。
- **A：**先发布到测试环境，然后扫码调试。
- **Q**：是否支持 CI 构建？
- **A**：可以调用 TTSDKTool.API.BuildManager.Build接口，详情更多可查看 [CI 自动化](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/ci_openapi)。

#
