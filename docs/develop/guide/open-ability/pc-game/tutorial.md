---
title: "PC 直播伴侣小游戏接入指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/pc-game/tutorial
update_time: 2025-11-06
---

## 接入说明
Windows 直播伴侣已支持运行小游戏，可降低小游戏发行人直播任务参与门槛，提升小游戏投屏、游玩的体验。
- 支持场景：Windows 直播伴侣
- 面向用户：主播
- 接入条件：发布发行人直播任务的小游戏必接

## 支持范围
支持游戏方案：

| 方案 | 是否支持 |
| --- | --- |
| 普通小游戏（cocos/laya/egret/原生） | 是 |
| Unity WebGL | 是 |
| Unity Native | 否 |

支持的伴侣版本：>= 8.2.0

## 入口判断
1. 系统判断：可以通过 [`tt.getSystemInfoSync`](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/system-information/tt-get-system-info-sync/) 的返回值 `platform` 判断是否 PC 环境，目前直播伴侣上 `platform` 返回值为 `windows`。

```js
// getSystemInfoSync 返回值需要注意的字段
{
    appName: "Douyin", // 直播伴侣抖音开播时 appName 为 Douyin
    brand: "windows",
    system: "Windows 10 Pro",
    platform: "windows"
}
```

1. 场景值判断：根据 [tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/lifecycle/tt-get-launch-options-sync) 返回的 `scene` 判断，直播伴侣入口场景值为 `029003`；
## 能力支持情况
目前 PC 小游戏已支持游戏运行必需的渲染能力，但仍有部分开放能力无法适配 PC 或有特殊表现：

| 能力 | 接口 | 表现 |
| --- | --- | --- |
| 广告 | [tt.createRewardedVideoAd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/tt-create-rewarded-video-ad) [tt.createBannerAd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/tt-create-banner-ad) [tt.createInterstitialAd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/tt-create-interstitial-ad) | 当遇到需要看广告才能进行的动作时，默认广告自动完成并下发相应的游戏内奖励道具。 |
| 支付 | [tt.requestGamePayment](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-request-game-payment) [tt.openAwemeCustomerService](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-open-aweme-service) | 支付能力建设中，如果需要进行道具购买等操作，可以先通过抖音手机端启动小游戏进行购买。 注：抖音和直播伴侣需要使用同一个账号登录。 |
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

为了让 PC 端用户获得更好的小游戏体验，我们提供了下列额外接口与功能，可在适配 PC 端时选择使用：

| 能力 | 接口 | 说明 |
| --- | --- | --- |
| 键盘 | [tt.onKeyUp](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/keyboard/tt-key-up) [tt.onKeyDown](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/keyboard/tt-key-down) [tt.offKeyUp](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/keyboard/tt-off-key-up) [tt.offKeyDown](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/keyboard/tt-off-key-down) | 监听/取消监听键盘的点击事件 |
| 鼠标 | [tt.onMouseUp](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/mouse/tt-mouse-up) [tt.onMouseDown](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/mouse/tt-mouse-down) [tt.onMouseMove](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/mouse/tt-on-mouse-move) [tt.offMouseUp](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/mouse/tt-off-mouse-up) [tt.offMouseDown](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/mouse/tt-off-mouse-down) [tt.offMouseMove](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/mouse/tt-off-mouse-move) | 监听/取消监听鼠标的点击事件 |
| 滚轮 | [tt.onWheel](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/wheel/tt-on-wheel) [tt.offWheel](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/wheel/tt-off-wheel) | 监听/取消监听鼠标滚轮的滚动事件 |
| 光标 | [tt.setCursor](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/cursor-style/tt-set-cursor) [tt.requestPointerLock](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/cursor-style/tt-request-pointer-lock) [tt.isPointerLocked](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/cursor-style/tt-is-pointer-locked) [tt.exitPointerLock](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/cursor-style/tt-exit-pointer-lock) | 设置光标样式或者隐藏光标 |

## 调试方式
#### 添加开播测试账号
- 打开「开发设置」-「测试管理」页面，扫码添加开播测试账号。
- 每款游戏最多添加3个测试成员，添加后该账号可获得直播伴侣开播权限及豁免游戏挂载门槛。
- 账号如涉及安全违规，将被取消以上权限，并减少一个测试账号名额。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d4bb9b5f1a9d46a785b95fc8054882e6)

#### IDE 生成游戏链接
打开[抖音开发者工具](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/development-assistance/mini-app-developer-instrument)，预览-扫码预览-复制链接，得到该游戏的链接；
如果扫码预览没有复制链接按钮，请升级开发者工具版本至最新版；

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d49acc2e745a465ea746096439da4729)

#### 直播伴侣调试
建议在直播伴侣调试前先保证在 IDE 上能够正常运行。
打开 Windows 直播伴侣，进入「游戏玩法」页面，点击右上角小扳手打开调试面板，选择小游戏并粘贴第 2 步生成的 schema 打开小游戏进行调试；

**注意**
- 小游戏支持开播前调试和开播后调试，如果选择开播后调试，为防止封禁，开播测试过程中开发者需露脸直播，且始终保证直播间有声音，不允许挂机/完全黑屏。
- 直播伴侣下载链接：[https://streamingtool.douyin.com/](https://streamingtool.douyin.com/)。
- 配置开播测试账号权限【只有开通权限，才能看到小扳手图标】。
- 开播账号必须是私密账号，设置路径：抖音-设置-隐私设置-私密账号。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f2b40a596bfe46418759a39ea165cff0)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/6d8dcb353ffe4e3a82c264c1b22ae8dd)

## 上线 PC
### 上线版本
PC 运行的小游戏版本类型和移动端一致，开发者需要将 PC 适配后的版本提交审核并完成发布；

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/223c826ea46e48aab2b51005fa014e9d~tplv-9nona0m7ha-image.image)

### PC 入口
目前 PC 仅支持直播伴侣，入口在直播伴侣-游戏玩法处，目前支持两种挂载方案：
1. 仅挂载：默认支持，仅挂载直播任务，主播自定义投屏的内容；
1. 挂载启动：需要审核通过，挂载直播任务的同时，启动 PC 版小游戏进行画面采集；

「挂载启动」审核：
提交发行人直播任务时会同时对 PC 适配进行审核，审核通过后会开启「挂载启动」入口，一般为每周三更新；

如果已有发行人直播任务，想开启「挂载启动」入口，或者想切换两种挂载方案，可根据本文档完成 相关能力适配后，重新提交包体审核；

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/89d19354039f4a8e90e61535f94c3338~tplv-9nona0m7ha-image.image)

## 问题排查
如果游戏在 PC 调试发现无法正常运行，可以根据下面的能力说明进行自测和适配。

#### 性能较差
可参考 [PC 端小游戏性能优化](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/pc-game/pc-games-optimization) 自查和优化。

#### Socket
[`tt.connectSocket`](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/websocket/tt-connect-socket/) PC 版本按 WebSocket 标准实现，对比移动端需要注意：
如果入参 `protocols` 传了子协议数组，那么服务端应该返回`Sec-WebSocket-Protocol` ，且取值与游戏发起连接时传的 protocol 取值一致，否则客户端会直接关闭连接。

#### Video
PC 小游戏使用 [`createVideo`](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/video/tt-create-video)`/`[`createOffscreenVideo`](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/video/tt-create-offscreen-video/) 接口时需要注意：Video 只支持 canvas2d context，不支持 paintTo WebGL context，请自行使用 webgl 纹理绘制视频。

#### 音频
浏览器针对`mp3`、`mp4`资源文件的请求默认会在 header 中带上`accept-encoding=identity;q=1, *;q=0`，服务器响应需要做好适配。
建议在 IDE 或者利用直播伴侣调试验证游戏运行正常后上线。

#### 录屏/录音
录音/录屏基础能力已经支持，但有部分子功能暂不支持。例如不支持裁剪视频，生成的文件类型与移动端可能有出入等。

#### 广告
目前直播伴侣 PC 上的小游戏均为无广模式，所有广告会默认返回成功，理论上游戏无需特殊适配，但需要评估广告奖励设置。

#### 其他能力
游戏转发分享、收藏、群聊、侧边栏、**支付、**以及**强依赖移动端设备的能力**，如罗盘、加速度计等能力目前均不支持。
此类能力在进行调用时会出现相应的提示——“能力暂不支持”，理论上不影响游戏的正常游玩，如出现特殊情况请做针对性处理。

// getSystemInfoSync 返回值需要注意的字段
{
appName: "Douyin", // 直播伴侣抖音开播时 appName 为 Douyin
brand: "windows",
system: "Windows 10 Pro",
platform: "windows"
}
