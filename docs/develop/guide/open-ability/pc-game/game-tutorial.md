---
title: "PC 抖音小游戏接入指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/pc-game/game-tutorial
update_time: 2026-05-20
---

## 接入说明
抖音小游戏目前已支持在 PC 端游玩体验，游戏的线上包可直接运行在 PC 抖音客户端上，但为了 PC 端更好的游戏体验，本文会指引开发者为 PC 端进行专项的优化和适配。
## 支持范围
### 支持的客户端版本

| 客户端 | 支持版本 |
| --- | --- |
| Mac 抖音 | 暂不支持 |
| Windows 抖音 | >= 6.8.0 |

### 支持的游戏方案

| 方案 | 是否支持 |
| --- | --- |
| 普通小游戏（cocos/laya/egret/原生） | 是 |
| Unity WebGL | 是 |
| Unity Native | 否 |

### 接入要求
提审时包含抖音端且版本审核通过的虚拟支付类小游戏将**自动接入**。暂不支持纯广告类游戏和云游戏。

## 来源判断
游戏内如果有需要判断 PC 抖音或者系统的场景，可以使用以下方式：
1. 判断环境：根据 [tt.getSystemInfoSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/system-information/tt-get-system-info-sync) 返回的 `appName` 判断，PC 抖音作为新宿主会返回 `douyin_web`；
1. 判断系统：根据 [tt.getSystemInfoSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/system-information/tt-get-system-info-sync) 返回的 `platform` 判断，会返回当前的系统，如 `windows`；
1. 判断场景值：根据 [tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/lifecycle/tt-get-launch-options-sync) 返回的 `scene` 判断，PC 抖音各个入口的场景值参考 [场景值列表](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/scene-value)；
## 能力支持
PC 已支持游戏常用的能力，但有部分能力在 PC 无法适配或者表现与移动端存在差异：

| 能力 | 接口 | 表现 |
| --- | --- | --- |
| 广告 | [tt.createRewardedVideoAd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/tt-create-rewarded-video-ad) [tt.createBannerAd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/tt-create-banner-ad) [tt.createInterstitialAd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/tt-create-interstitial-ad) | 目前抖音 PC 未支持广告能力，调用广告相关接口时会返回不支持的错误信息和错误码。 |
| 支付 | [tt.requestGamePayment](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-request-game-payment) | 支付接口与 Android 一致，但只支持钻石支付，详细说明见接口文档。 |
| 订阅 | [tt.requestSubscribeMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/subscribe-message/tt-request-subscribe-message) | 订阅该小游戏能力建设中。 |
| 收藏 | [tt.showFavoriteGuide](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/collect/favorite/tt-show-favorite-guide) [tt.onFavoriteStateChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/collect/favorite/tt-on-favorite-state-change) [tt.showRevisitGuide](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/collect/favorite/tt-show-revisit-guide) | 收藏该小游戏能力建设中。 |
| 录屏 | [tt.getGameRecorderManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/screen-recording/tt-get-game-recorder-manager) | 暂不支持小游戏内的录屏和录屏分享功能。 |
| 分享 | [tt.shareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-share-app-message) [tt.showShareMenu](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-show-share-menu) | 暂不支持小游戏分享、转发功能。 |
| 群聊 | [tt.checkGroupInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/im-group/checkGroupInfo) [tt.joinGroup](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/im-group/joinGroup) | 暂不支持从小游戏内拉起群聊功能。 |
| 日历 | [tt.addPhoneCalendar](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/calendar/tt-add-phone-calendar/) | 暂不支持从小游戏内拉起日历、设置日历等功能。 |
| 扫码 | [tt.scanCode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/scan-code/tt-scan-code) | 暂不支持小游戏内扫码能力。 |
| 侧边栏 | [tt.navigateToScene](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/sidebar-capacity/tt-navigate-to-scene) [tt.checkScene](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/sidebar-capacity/tt-check-scene) | PC端不支持跳转侧边栏能力。 |
| 震动 | [tt.vibrateShort](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/shake/tt-vibrate-short/) [tt.vibrateLong](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/shake/tt-vibrate-long) | PC端不支持震动体验。 |
| 陀螺仪 | [tt.startGyroscope](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/gyroscope/tt-start-gyroscope) [tt.stopGyroscope](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/gyroscope/tt-stop-gyroscope) [tt.onGyroscopeChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/gyroscope/tt-on-gyroscope-change) [tt.offGyroscopeChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/gyroscope/tt-off-gyroscope-change) | PC端不支持陀螺仪能力。 |
| 罗盘 | [tt.startCompass](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/compass/tt-start-compass) [tt.stopCompass](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/compass/tt-stop-compass) [tt.onCompassChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/compass/tt-on-compass-change) [tt.offCompassChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/compass/tt-off-compass-change) | PC端不支持罗盘能力。 |
| 麦克风 | [tt.requestMicrophone](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/mircophone/tt-request-microphone) [tt.pauseMicrophone](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/mircophone/tt-pause-microphone) [tt.resumeMicrophone](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/mircophone/tt-resume-microphone) | PC端不支持语音输入等操作。 |
| 相机 | [tt.createCamera](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/camera/tt-create-camera) | PC端不支持相机能力。 |
| 人脸检测 | [tt.createFaceDetector](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/face-detector/tt-create-face-detector) | PC端不支持人脸识别等操作。 |
| 手势识别 | [tt.createHandDetector](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/hand-detector/tt-create-hand-detector) | PC端不支持手势识别等操作。 |

对于不支持的接口，抖音会自动弹出 toast 提示给到玩家，同时会返回特定错误码和错误信息给开发者：

| errNo | errMsg |
| --- | --- |
| 10301 | %s:fail The feature is not supported in app |

为了让 PC 端用户获得更好的小游戏体验，我们提供了下列额外接口与功能，可在适配 PC 端时选择使用：

| 能力 | 接口 | 说明 |
| --- | --- | --- |
| 键盘 | [tt.onKeyUp](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/keyboard/tt-key-up) [tt.onKeyDown](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/keyboard/tt-key-down) [tt.offKeyUp](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/keyboard/tt-off-key-up) [tt.offKeyDown](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/keyboard/tt-off-key-down) | 监听/取消监听键盘的点击事件 |
| 鼠标 | [tt.onMouseUp](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/mouse/tt-mouse-up) [tt.onMouseDown](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/mouse/tt-mouse-down) [tt.onMouseMove](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/mouse/tt-on-mouse-move) [tt.offMouseUp](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/mouse/tt-off-mouse-up) [tt.offMouseDown](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/mouse/tt-off-mouse-down) [tt.offMouseMove](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/mouse/tt-off-mouse-move) | 监听/取消监听鼠标的点击事件 |
| 滚轮 | [tt.onWheel](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/wheel/tt-on-wheel) [tt.offWheel](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/wheel/tt-off-wheel) | 监听/取消监听鼠标滚轮的滚动事件 |
| 光标 | [tt.setCursor](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/cursor-style/tt-set-cursor) [tt.requestPointerLock](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/cursor-style/tt-request-pointer-lock) [tt.isPointerLocked](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/cursor-style/tt-is-pointer-locked) [tt.exitPointerLock](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/cursor-style/tt-exit-pointer-lock) | 设置光标样式或者隐藏光标 |

## 调试方式
### 添加调试设备
在后台「开发-开发设置-测试管理-调试设备」处，添加账号到调试白名单；

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/dcf105699c4e4b5585d21b9767d085da~tplv-9nona0m7ha-image.image)

### IDE 打开抖音预览/调试
更新 IDE 到最新版本，在「预览-推送预览-使用 PC 端预览」处可以打开抖音并打开小游戏；

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/d9779bd1a908455aa966d420a37c4936~tplv-9nona0m7ha-image.image)

## 数据查看
PC 小游戏在用户分析、虚拟支持等模块已支持数据查看，筛选 App 为 抖音 PC 即可查看。
## 问题排查
如果游戏在 PC 调试发现无法正常运行，可以根据下面的能力说明进行自测和适配。

#### 性能问题
可以参考 [PC 性能优化文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/pc-game/pc-games-optimization) 进行自查和优化；

#### Socket
[tt.connectSocket](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/websocket/tt-connect-socket/) PC 版本按 WebSocket 标准实现，对比移动端需要注意：
如果入参 `protocols` 传了子协议数组，那么服务端应该返回`Sec-WebSocket-Protocol` ，且取值与游戏发起连接时传的 protocol 取值一致，否则客户端会直接关闭连接。

#### Video
PC 小游戏使用 [createVideo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/video/tt-create-video)`/`[createOffscreenVideo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/video/tt-create-offscreen-video/) 接口时需要注意：Video 只支持 paintTo canvas2d context，不支持 paintTo WebGL context，请自行使用 webgl 纹理绘制视频。

#### 音频
浏览器针对`mp3`、`mp4`资源文件的请求默认会在 header 中带上`accept-encoding=identity;q=1, *;q=0`，服务器响应需要做好适配。
建议在 IDE 或者利用直播伴侣调试验证游戏运行正常后上线。

#### 录屏/录音
录音/录屏基础能力已经支持，但有部分子功能暂不支持。例如不支持裁剪视频，生成的文件类型与移动端可能有出入等。

#### 其他能力
游戏转发分享、收藏、群聊、侧边栏**、**以及**强依赖移动端设备的能力**，如罗盘、加速度计等能力目前均不支持。
此类能力在进行调用时会出现相应的提示——“能力暂不支持”，理论上不影响游戏的正常游玩，如出现特殊情况请做针对性处理。

## 结算规则
开发者在PC端的内购收入适用于[《小游戏结算政策导览》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/revenue/sharingclause/game-settlement-guide)中的现金结算规则、广告金规则（限时激励活动）、任务金规则（限时激励活动），PC端内购收入按照**安卓端内购**消费总额规则结算。

## 常见问题
1. PC 小游戏和移动端游戏表现一致吗？支持了哪些能力？
    PC 已支持游戏常用的能力，但有部分能力在 PC 无法适配或者表现与移动端存在差异。详细请看接入指南-能力支持的部分。
1. 如何接入 PC 小游戏？
    提审时包含抖音端且 PC 版本审核通过的虚拟支付类小游戏将自动接入，无需额外操作。如对接入有其他疑问可联系平台客服。
1. 上线了在哪里查看 PC 小游戏？
    使用 Windows 系统的电脑下载抖音 PC 端，在左侧菜单栏找到小游戏入口或者直接搜索小游戏名称即可查看。
1. 在哪里查看 PC 小游戏的数据表现？
    接入后，在各数据模块筛选 App 为抖音 PC，即可查看具体数据表现。
1. 为什么小游戏移动端的版本更新了，小游戏 PC 版本还未更新？
    移动端与 PC 端审核可能有时间差异，通过后会下发站内信通知。

// getSystemInfoSync 返回值需要注意的字段{appName: "Douyin", // 直播伴侣抖音开播时 appName 为 Douyinbrand: "windows",system: "Windows 10 Pro",platform: "windows"}
