---
title: "FAQ"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/sc_faq
update_time: 2025-12-10
---

> 本文旨在帮助开发者更快的查询文档、定位以及解决接入过程中遇到的问题。本文汇总了开发者接入过程中需要查阅的文档和在接入使用过程中常见的问题。
> 接入前请优先阅读[抖音Unity小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide) ，了解抖音Unity小游戏接入的总体流程。如果接入过程中遇到问题，优先查阅下方列出的帮助文档和本文中的FAQ，如未找到答案，可以加入反馈群中提问。

## 文档汇总
### 如何接入抖音Unity小游戏与方案选择
接入指南：[抖音Unity小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide)
#### 方案选择
什么是native方案？什么是WebGL方案？如何选择？请参考文档：
[抖音Unity小游戏使用方案及引擎选择建议](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_engine_selection_suggestion)

### WebGL方案说明
抖音Unity小游戏WebGL方案说明：[抖音Unity小游戏-wasm方案说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/overview-and-compatibility/sc_webgl_compatibility)
抖音Unity小游戏如何接入WebGL：[抖音Unity小游戏WebGL方案接入流程](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/overview-and-compatibility/sc_webgl_access_flow)
分包提高加载速度：[Wasm分包工具说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/code-upload/sc_webgl_split)
新文件系统：[使用新文件系统说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_new_file_system)

### 抖音Unity小游戏C# SDK接入
C# SDK接入文档：[抖音Unity小游戏C# SDK接口文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk)
C# SDK发版记录：[抖音Unity小游戏C# SDK发版记录](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_changelog)

### 开放平台与普通小游戏
抖音开放平台-小游戏：[开放平台小游戏开发者文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/introduction)

---

## 接入与使用问题
接入抖音Unity小游戏，请参考[抖音Unity小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide)

### 接入调试问题
#### 本地调试打开后提示meta服务错误
- 目前需要先发布一个测试版本
#### 通过分享、桌面快捷方式、微端进入游戏提示meta服务错误
- 外部用户渠道，需要有经过审核的线上版本才能进去
- 关注和收藏相关的功能需要提交到线上才可以验证。
- 包括创建的快捷方式拉起，也需要正式发布到线上之后才可以验证。
#### 添加快捷方式/下载快捷方式（miniapk）失败
- Android需要事先允许app创建快捷方式/安装应用
#### miniapk打开后提示meta服务错误
- 先确定游戏是否发布过正式版本，miniapk跳转的是线上正式版本
#### appid的存储空间更改
- 请在反馈群中询问
#### 相同代码，Unity 2021 版本打出的apk包体比Unity 2019打出的包体大
- Unity Build Settings -> IL2CPP Code Generation，切换到**Faster (smaller) builds**

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/fa7e44fc96ec4bcea8c55d4042d88df1)

### C# SDK问题
#### 接口不知道怎么用，有没有demo
- Demo地址：https://sf3-g-cn.dailygn.com/obj/sf-game-lf/testgn/StarkSDK-Sample.zip
#### 怎么判断哪些接口可用
- 使用`StarkSDKSpace.CanIUse`来判断该接口是否可用
#### 抖音Unity小游戏需要额外添加防沉迷和实名认证吗
- 不用，抖音Unity小游戏自带了相关能力
#### 抖音Unity小游戏支持打开外链吗？
- 暂时不支持外链
#### 广告接口返回100x错误
- 查看小程序开发平台关于[广告错误码的说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/rewarded-video-ad/rewarded-video-ad-on-error)
#### 广告返回1004
- 没有适合的广告，属于正常情况，且开发者需要针对这种情况做形态上的兼容。
#### 为什么插屏广告经常看不到？
- 初次进入的时候，需要等待15秒才可以做第一次的展示。
- 后续的插屏广告需要间隔30s
- 同一个广告只能展示一次。
#### 为什么视频广告出不来？
- 需要看下[错误码](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/rewarded-video-ad/rewarded-video-ad-on-error)，根据错误码来排查。
- 提交验收的包需要使用自己正式申请到的appID和相关广告ID。
- 接口相关的使用规则：
  - 新接口从抖音Unity小游戏的3.4版本开始支持：StarkSDK.API.GetStarkAdManager().ShowVideoAdWithId()
    - 抖音宿主: 13.4.0 开始支持
    - 头条宿主: 7.9.6 开始支持
    - 抖音Lite宿主: 7.6.9开始支持
    - 头条Lite宿主：暂不支持
  - 老接口从抖音Unity小游戏的3.10版本开始不再支持：StarkSDK.API.GetStarkAdManager().ShowVideoAd()
#### 关于录屏你需要知道的？
- 录屏时长不能低于3秒。
- 首次加载游戏之后，建议不要默认开启视频分享按钮。
- 分享失败或者其他提醒的时候，建议走toast提示。
#### 录屏分享失败
- 报错信息：ERROR/StarkShareImpl: Share failed, err: -1, errMsg: get shareInfo return null
- 原因：游戏被下架，被封禁分享和搜索
#### Unity游戏是否有域名限制？
- 目前没有，未来可能会加
#### 排行榜提示网络异常
- 需要先确认是否已经登录
#### 支付报错10401
- 支付需要保证用户已经登录，可以调用StarkSDK.API.GetAccountManager().Login接口，也可以调用StarkSDK.API.GetAccountManager().CheckSession检查session有效性

#### 加入群聊失败，返回“OnFailed，code2190004，msg:无权访问”
- 粉丝群的群主到游戏中进行“获取群聊信息”授权，授权后恢复权限

#### 无法测试从侧边栏进入到测试环境的游戏

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e2882c3a82dd492385eb9880a548d045)

- 添加测试设备，加入调试成员后，在抖音【我】右上角更多按钮-更多功能-开发者模式-打开开发者模式-对应的游戏-打开全入口打开指定版本小游戏-扫码选择指定版本，这样就可以在点击侧边栏的时候进入到测试版本
### Native方案
#### Unity支持的版本(Android native方案)
- 2021.3.14f1
- 2022.3.34f1
- 团结引擎1.1.4

### WebGL方案
#### iOS WebGL提示“当前系统版本不支持运行，请升级系统版本”
- iOS 13.4以下以及iOS 15.4.0、15.4.1版本不支持
#### WebGL 如何拉起键盘
- 调用StarkSDK.API.GetStarkKeyboard().ShowKeyboard，并查看该api的相关注释
#### iOS WebGL录屏报错不支持
- 当前iOS系统限制，对性能要求较高。为了用户更好的体验，**所以对iphonexr以下机型没有打开可见性入口**
- iOS上的录屏功能会有权限申请，还有性能消耗，不建议使用。一定要使用，dau达到10万后，跟平台运营同学联系开白名单。（**平台只要求Android上要录屏分享**）
#### WebGL 报错 RuntimeError: Out of bounds memory access (evaluating 'dynCall_xxxx')
这个问题一般有两种可能：
- 使用iOS 15.4.0或15.4.1系统，但没有采用wasm分包。
  - 该问题为 Unity 与 iOS 15.4.x 的 BUG，推荐使用我们提供的[WebGL 分包工具](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/code-upload/sc_webgl_split)或采用Unity WebGL官方论坛的修复方案:
    - https://forum.unity.com/threads/ios-15-webgl-2-issue.1176116/page-2
    - https://forum.zap.works/t/unity-webgl-x-ios-15-4-workaround/8814
- C#代码逻辑有问题，或者C#代码在WebGL平台下不支持。如果是这个问题，需要编译一个带符号的版本重新发布，然后看详细错误信息，需要自行排查是哪个函数报错。
  - 编译带符号版本: PlayerSettings -> Publishing Settings -> Debug Symbols -> Embeded。
#### WebGL Android提示当前32位手机不支持
- WebGL Android仅支持64位
#### WebGL Android部分机型渲染黑屏
- 渲染引擎导致，之后会升级渲染引擎
#### 游戏界面被覆盖或切后台后返回，背景音乐失效，音效失效
- 使用C# SDK内置的音频接口
#### 是否支持WebGL2.0？
- iOS：**仅支持iOS 15.0**及以上系统
- Android WebGL：暂时**不支持**WebGL2.0，如果使用WebGL2.0，Android平台需要使用Native方案
#### iOS 16.7-17.0版本切后台出现渲染卡死问题
- iOS系统bug导致，在切后台一段时间后导致"WebGL: context lost."，致使Unity无法继续渲染。
- 苹果在iOS 17.1版本修复了该问题：https://developer.apple.com/documentation/safari-release-notes/safari-17_1-release-notes
- Unity问题反馈：https://forum.unity.com/threads/webgl-context-lost-ios-17-safari.1501193/
#### iOS 16.7-17.0版本启动出现js报错：null is not an object (evaluating 'result.rangeMin'),_glGetShaderPrecisionFormat
- 同上个问题，context lost导致
#### called non-existent method UnityEngine.Cache报错
- 需要检查是否是使用了UnityEngine.Caching相关的接口：https://docs.unity3d.com/ScriptReference/Caching.html
- 暂时不支持Unity2022版本

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/7ba5c440b11544ec9b516cdc40e472ad)

#### 调用HttpWebRequest导致游戏卡住
- HttpWebRequest在WebGL下不支持，需要替换成UnityWebRequest
#### WebGL 如何设置帧率
[请参阅](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/drawing/set-frame-rate)
#### iOS上HDR贴图花屏
渲染路径在 EXT_texture_compression_bptc 这个 WebGL 拓展上有问题，导致 BC6H 的 HDR 光照贴图出问题，可以先使用 WebGL2.0 原生支持的一些格式规避，比如 RGEBAHalf，RGB9E5。
#### 卡顿问题排查
- YooAsset 资源加载明显卡顿：可以将单次 UniTask.WhenAll 调用拆分，控制单次调用的并发数量，分组控制完成。
- 低端机型明显卡顿：Log 的高频字符串拼接导致的 GC，建议通过宏或修改 Log 调用方式避免频繁拼接字符串。
- 加载新界面时使用动态字体资源导致卡顿：动态字体当原有字形图集不足以容纳新字形时,会删除旧的图集并重建一个更大,容易发生卡顿,建议在交互界面前提前预热。
- Unity推荐移动设备帧时间不超过帧间隔的65%，对于60FPS来说是11ms，对于30帧是22ms，来避免发热保持长时间流畅运行，建议平衡美术规格与性能表现，或者进一步优化渲染性能。
#### 启动问题排查
- 使用xlua时wasm资源较大，导致首包加载时间长：xLua 的 Wrapper 文件占 30%+，且同时导致引擎代码和 mscorlib 等系统库无法有效裁切。建议对占比大调用少的部分手动进行排除。
- webgl.data较大，导致首包加载时间长：精简首场景资源，裁剪built-in package。建议使用团结引擎，有对built-in代码做优化。
- 小游戏启动出现黑屏：可能是加载子包耗时过长，并且开发者没有设置 Loading 画面。如果是开发者模式，则存在超时自动移除 Loading 开屏页的逻辑：当小游戏加载时间超过一定阈值后（30秒左右），会把开屏 Loading 页移除，以便显示 vConsole 入口。
- 新版本发布后启动阶段出现较多卡顿问题：使用wasm分包未彻底玩家触发子包 js 函数导致卡顿，每次发版之后都要重新收集函数分包。
- 部分设备蓝屏问题：关闭msaa，部分设备不支持该功能。目前遇到过的设备包括realme gt neo3、vivo 60等。

---

## 插件工具相关
### 构建工具
#### 请问这个BGDT没有使用权限要怎么处理
- 参考：[BGDT文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/BGDT-handbook/install)
#### 请问点击运行本地apk或者构建并真机运行，都不能启动真机上的程序是什么原因，也没有报错？
- 宿主上的插件还没安装完
  - 针对这类问题，抖音安装好了之后，需要登录下抖音，进入随便运行一个抖音Unity小游戏即可。如果没有发布过可以搜索一下《超级挖坑大师》
- 手机是否是android11的系统，看下push apk包是否成功（通过控制台日志查看）
#### 发布的时候提示uid没有权限？
- 如果是初次发布，版本号需要自定义一下，比如输入0.0.1
- 如果非初次发布，且已经有相关的发布版本，可以直接在话题群咨询。
#### 
### 发布工具
#### 我发布的时候出现了各类问题该如何自查？
- **第一步： **确保你的操作步骤是按照文档来的。
  [C# SDK 文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk)
  [抖音Unity小游戏发布](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_publish)
- **第二步：**检查Unity版本号信息, 抖音Unity小游戏只支持使用指定版本（注意：通过官网，不能通过unityhub下载，要用浏览器下载）
- **第三步：**更新工具版本
  - 更新BGDT工具版本到最新的版本
  - 更新UnitySDKTools 到最新的版本
#### md5检测失败 code:10002 error:apk check failed

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/dd0cd9ec2bb2478f876a242ccd01388f)

- 建议先使用空工程进行发布测试
- 确认使用的unity版本是指定版本。官方下载页面（认准.com域名）：
当前支持 2019.4.35f1 / 2021.3.14f1 [SC使用方案及引擎选择建议](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_engine_selection_suggestion)
- 确认使用il2cpp并且关闭StripEngineCode

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1386d67558ae4fb099ab6e1027a5c19b)

- 关闭DevelopmentBuild

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/947267ca98124555a206e55764a48eea)

#### 文件类型错误 code: 10002 msg: invalid apk file, not support file type: .apk?=
- 一般是使用的文件路径带有中文。更新发布工具可解决

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a8c8adfe6aa54bdca303f8698c66c760)

#### 场景中的Render Mode 选择的是Screen Space -OverLay

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/28a5632ae5ff494788e9d0c41d835214)

URP和builtin管线不同，无法使用CommandBuffer在帧末插入渲染指令，来将Color buffer的内容blit到RenderTexture。使用的是URP内建的_CameraColorTexture来获取屏幕渲染结果。 而使用Overlay方式渲染的UI不会被渲染到这张RT上。这样会影响到录像的结果，导致录像中不显示UI。

将Overlay UI修改成使用Screen Space Camera渲染

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/44e0a62319a84a4a9beba5495e32eff6)

指定对应的Overlay Camera

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/7563a058f4d04f378cda5d2694e05565)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/7bcd2d8d7471465e96d925f9becd4064)

将Overlay Camera加到主相机的Camera Stack中

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/c52f53cfd8594e5d9cc69a265ef1b053)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/45aa7e0423c34fb185a16692e3c8c8db)

这样就可以正常在URP中录制到UI了
## 游戏接入相关
### 基本接入流程：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ce565ee6e8624f778c6e299cd6c46ac8)

### 必备基础知识
#### 1、验收相关：
- 抖音Unity小游戏（unity解决方案）在合规及提审方面的要求与普通小游戏对齐，请务必先阅读抖音开放平台相关文档https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/agreement-and-norms/norms/standards
#### 2、常规的兜底：
- 资源加载失败(弱网、断网)的时候需要有兜底页面，即重试。
- 广告加载失败(弱网、断网)的时候需要有兜底页面，不要一直等待。
#### 3、包体相关：
- 用户启动游戏的时间，一般来说，启动越快，取消率越低，转化率越高。为保证用户体验，在小游戏平台上线，我们对首包大小有如下约束:
- 使用 **原生** 方案，首包包体需 小于100M
- 使用 **Wasm** 方案，首包包体需 小于100M
