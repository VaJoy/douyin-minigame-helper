---
title: "直播间即看即玩能力技术指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/instant-play-introduce
update_time: 2025-10-17
---

## 能力说明
> 当前能力以白名单方式开放接入，接入前请联系平台运营或发起oncall申请

> 为开发者提供直播间观众即看即玩主播在玩场景的开放能力，提升用户体验与留存、助力主播内容经营

- **观众看播体验更丝滑**：直播间观众点击讲解卡进入小游戏后，能直接体验到主播在玩场景/关卡；
- **丰富主播直播内容**：基于即看即玩能力，主播可口播呼吁观众进入游戏体验同场景，助力直播内容脚本编排；
- **丰富游戏体验**：厂商可基于此能力，尝试拓展观众进入主播同区服、观众进变现转化高的场景游玩等游戏交互体验。

## 技术接入方案
### 参考流程图
#### 主播侧链路

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/eb770c3b9e484959b118797133c046d9~tplv-9nona0m7ha-image.image)

1. 小游戏需要在主播侧进入支持即玩的场景时，**通过tt.reportScene上报场景值，自定义标识即玩场景；**
1. 在小游戏进入即玩场景后，调用`LiveManager.uploadGameProgress`上报即玩的场景进度到观众端。
1. 当主播离开了即玩场景后，至少需要调用一次`LiveManager.uploadGameProgress`上报`data=""`来通知到观众端；
1. 即玩能力只有在**移动端视频开播或伴侣挂载启动游戏开播**的情况下才能使用，其他场景调用会报错，可通过`tt.getLiveSetting`中返回的`isVideoLive=true`来识别。

#### 观众侧链路

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/c9c2e6714e4344f3aae45d9324f8f46c~tplv-9nona0m7ha-image.image)

1. 小游戏需要在观众侧进入支持即玩的场景时，**通过tt.reportScene上报场景值**。
1. 在**主播打开即玩开关**的情况下，在一次小游戏启动周期内，data的值不会发生变化，只有重新进入游戏才会刷新；
1. 即玩能力只有在主播是**移动端视频开播或伴侣挂载启动游戏开播**的情况下才能使用，其他场景调用会报错，可通过`tt.getLiveSetting`中返回的`isVideoLive=true`来识别。

#### 关键API

| **能力** | **是否必接** | **JSAPI** | **Unity C# API** |
| --- | --- | --- | --- |
| 获取直播管理对象 | 是 | [tt.getLiveManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/live/tt-get-live-manager) | [TT.GetLiveManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/live-manager) |
| 获取直播场景下配置 | 是 | [LiveManager.getLiveSetting](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/live/live-manager/livemanager-get-setting) | [TTLiveManager.GetLiveSetting](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/live-manager) |
| 上传主播游玩进度 | 是 | [LiveManager.uploadGameProgress](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/live/live-manager/livemanager-upload-progress) | [TTLiveManager.UploadGameProgress](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/live-manager) |
| 观众侧同步主播游戏进度 | 是 | [LiveManager.syncGameProgress](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/live/live-manager/livemanager-sync-progress) | [TTLiveManager.SyncGameProgress](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/live-manager) |
| 上报场景数据 | 是 | [tt.reportScene](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/data-analysis/tt-report-scene) | TT.ReportScene |
| 监听即看即玩开关状态变化 | 否 | [LiveManager.onInstantPlayStatusChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/live/live-manager/livemanager-on-instant-change) | [TTLiveManager.OnInstantPlayStatusChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/live-manager) |
| 取消监听即玩开关状态变化 | 否 | [LiveManager.offInstantPlayStatusChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/live/live-manager/livemanager-off-instant-change) | [TTLiveManager.OffInstantPlayStatusChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/live-manager) |

### 测试流程
使用开发者工具进行调试，要求开发者工具 **>= 4.4.5** 版本

| **步骤** | **图示** |
| --- | --- |
| 开通平台能力 |  |
| 使用抖音测试账号扫码登录开发者工具。登录账号要求已加入当前游戏的应用测试设备 |  |
| 在开发者工具上方选择**添加编译模式**，【进入场景】指定场景值 **023009 或 023010，**分别表示主播侧启动和观众侧启动游戏 |  |
| 在移动端使用抖音账号开启直播间，并挂载启动当前游戏 |  |
| 在开发者工具中运行游戏，并测试结果 |  |

## 能力扩展
### 即看即玩结合实时语音
#### **场景描述**
观众通过即看即玩能力进入小游戏和主播组队后，主播跟观众在游戏内连麦，实现游玩时的实时沟通，同时其他直播间内观众也能听见游戏内沟通的语音内容，有助于营造直播间内容效果。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/76fb90e55cbe453f95478550cebba5b0~tplv-9nona0m7ha-image.image)

#### **实时语音能力接入**
1、自行根据游戏内需实现语音互动的具体场景进行方案设计；
2、平台通过Native 原生 SDK，提供小游戏官方 RTC 组件，接入方式详见 [RTC实时语音文档介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/rtc/introduce) 。
> - 接入前，需要申请开通 RTC 服务，注册生成 RTC 的 appid 与 token才能正常使用：[注册地址](https://www.volcengine.com/docs/6348/69865)；
> - Token 相关的请参考：[token生成相关](https://www.volcengine.com/docs/6348/70121)；
> - 开通后，可前往技术交流群，告知已开通注册获得token，平台的运营同学核验后，连麦能力即可进行正常调用。
> 
![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/e54fd85d5fd44c1caefefa39e6bacf54~tplv-9nona0m7ha-image.image)