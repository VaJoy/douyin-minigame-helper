---
title: "视频适配"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/video-adapt
update_time: 2025-06-06
---

**本文档主要说明 WebGL 方案**下视频能力的限制并给出适配建议。
## 适配情况
在WebGL方案中，Unity VideoPlayer能力从【发布工具TTSDK 6.3.6版本】开始支持。
这些基础VideoPlayer能力验证可用：
- 播放、暂停、恢复、跳转、循环播放
- 事件：PrepareComplete/LoopPointReached/Started/SeekCompleted/ErrorReceived

## 功能限制
- 无法调节视频播放速率（平台能力不支持）
- 不可播放VideoClip（WebGL方案不支持）
- 【iOS webgl 高性能模式】（默认）、【iOS webgl 高性能+模式】无法调节视频音量

## 优化建议
- 视频格式推荐mp4，其他视频格式兼容性视具体平台存在差异
- 网络视频体积不建议太大，过大的网络视频会需要较长的缓冲时间才能 prepared，有时会导致跳转后缓冲时间过长才能继续播放
  - 建议使用本地视频资源，或者把视频下载到本地后再播放

## 已知问题
- 基础库版本 < [3.72.0.0](http://3.72.0.0) 时，存在下列问题
  - 【Android webgl】、【iOS webgl 高性能+】 seekCompleted 事件无法触发，历史遗留 bug
  - 建议通过 GetSystemInfo 的 sdkVersion 参数判断基础库版本
- ErrorReceived事件中，【Android webgl】、【iOS webgl 高性能+】的video报错信息和标准web video的报错信息并非完全对齐，因此仅用作无法播放的事件通知。
- Android Native保持原有的VideoPlayer能力，本次改动并未涉及，如果出现崩溃等稳定性问题，建议咨询unity官方解决方案，例如[Unity论坛讨论问题](https://discussions.unity.com/t/android-crash-when-videoplayer-stop-is-executed/900249)、[Unity 官方 issue 案例](https://issuetracker.unity3d.com/issues/android-application-crashes-when-changing-the-source-url-of-a-video-player-in-android)
- 当前unity webgl环境暂不支持 tt.createVideo() 播放屏上video
