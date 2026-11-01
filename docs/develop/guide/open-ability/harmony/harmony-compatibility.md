---
title: "鸿蒙端抖音小游戏适配指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/harmony/harmony-compatibility
update_time: 2026-09-11
---

## 接入说明
抖音小游戏目前已支持在鸿蒙端（OpenHarmony 5.0+）游玩体验，为了鸿蒙端更好的游戏体验，本文将指引开发者为鸿蒙端进行专项适配。

## 支持范围
### 支持的游戏方案

| 方案 | 是否支持 | 备注 |
| --- | --- | --- |
| 普通小游戏（cocos/laya/egret） | 是 | 抖音36.8.0及以上版本 |
| Unity WebGL | 是 | 抖音39.5.0及以上版本支持，开发者需按照[指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/unity-new)更新为新包体，并将TTSDK升级到6.7.9及以上，如不满足则不允许上线 |
| Unity Native | 否 | 暂无计划支持，但开发者可以按照[指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/unity-new)更新为新包体，并勾选`Android端使用Native方式渲染`，Android端会继续使用Native产物，鸿蒙端（抖音39.9.0及以上版本）和iOS端则会使用WebGL产物来运行游戏，TTSDK需要升级到6.7.9及以上，如不满足则不允许上线 |

### 支持的宿主
当前仅支持抖音；抖音极速版平台适配中，适配完成后已在抖音鸿蒙端上架的游戏将自动上架至抖音极速版鸿蒙端；其他宿主后续开放。

## 平台判断
[tt.getSystemInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/system-information/tt-get-system-info)和[tt.getSystemInfoSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/system-information/tt-get-system-info-sync)返回的`platform`为`openHarmony`。

## 支付
支付API对齐Android，使用[tt.requestGamePayment](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/tt-request-game-payment)，目前仅支持现金支付。
接入了支付能力的游戏需确保支付链路通畅，否则无法通过审核上线。

## 开放能力
鸿蒙端已支持大部分基础的开放能力，以保障小游戏主链路的通畅。暂未支持的开放能力如下：

| 能力 | 接口 | 备注 |
| --- | --- | --- |
| 转发 | [tt.shareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-share-app-message) [tt.showShareMenu](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-show-share-menu) [tt.hideShareMenu](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-hide-share-menu) [tt.onShareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-on-share-app-message) [tt.offShareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-off-share-app-message) [tt.navigateToVideoView](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-navigate-to-video-view) [tt.shareMessageToFriend](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-share-message-to-friend) |  |
| 关注 | [tt.createFollowButton](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/follow/follow-tt/tt-create-follow-button) [tt.checkFollowState](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/follow/follow-tt/tt-check-follow-state) [tt.checkFollowAwemeState](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/follow/follow-aweme/tt-check-follow-state) [tt.openAwemeUserProfile](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/follow/follow-aweme/tt-open-aweme-user-profile) |  |
| 推荐流直出游戏能力 | [tt.requestFeedSubscribe](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/request-feed-subscribe) [tt.checkFeedSubscribeStatus](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/check-feed-subscribe-status) |  |
| 排行榜 | [tt.setImRankData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/game-rank/setImRankData) [tt.getImRankList](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/game-rank/getImRankList) [tt.getImRankData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/game-rank/getImRankData) [tt.setImRankDataInOpenContext](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/game-rank/set-im-rank-data-in-open-context) |  |
| 媒体 | [tt.getGameRecorderManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/screen-recording/tt-get-game-recorder-manager) [tt.requestMicrophone](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/mircophone/tt-request-microphone) [tt.pauseMicrophone](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/mircophone/tt-pause-microphone) [tt.resumeMicrophone](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/mircophone/tt-resume-microphone) [tt.getRtcEngine](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/rtc/tt-get-rtc-engine) [tt.createCamera](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/camera/tt-create-camera) |  |
| 开放数据域 | [tt.getOpenDataContext](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data-area/tt-get-open-data-context) |  |
| 开放数据 | [tt.getCloudStorageByRelation](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data/tt-get-cloud-storage-by-relation) [tt.setUserCloudStorage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/relationship-chain/open-data/tt-set-user-cloud-storage) [tt.getUserCloudStorage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/relationship-chain/open-data/tt-get-user-cloud-storage) [tt.removeUserCloudStorage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data/tt-remove-user-cloud-storage) [tt.getSharedCanvas](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data/tt-get-shared-canvas) [tt.setUserGroup](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/ranking/tt-set-user-group) |  |
| 群聊 | [tt.joinGroup](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/im-group/joinGroup) [tt.checkGroupInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/im-group/checkGroupInfo) |  |
| 公会群 | [tt.getUnionGroupInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/union-group/tt-union-group-info) [tt.bindUnionGroup](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/union-group/tt-bind-group) [tt.unbindUnionGroup](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/union-group/tt-unbind-group) [tt.joinUnionGroup](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/union-group/tt-join-group) |  |
| 游戏站 | [tt.getGameClubData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/game-club/get-game-club-data) |  |
| 直播 | [tt.getLiveManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/live/tt-get-live-manager) |  |
| 客服消息 | [tt.openCustomerServiceConversation](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/customer-contact/openCustomerServiceConversation) [tt.createContactButton](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/customer-contact/tt-create-contact-button) |  |
| 抖音云 | [tt.createCloud](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/douyin-cloud-module/dycloud) |  |
| 基础 | tt.setPreferredFramesPerSecond |  |

对于不支持的接口，抖音会自动弹出 toast 提示给到玩家，同时会返回特定错误码和错误信息给开发者：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/84c251ae32b846f7a4ca854f38ccd190~tplv-9nona0m7ha-image.image)

| errNo | errMsg |
| --- | --- |
| 10302 | %s:fail The feature is not available in current operating system |

## 结算规则
开发者在**鸿蒙系统的广告和内购收入**，适用于[《小游戏结算政策导览》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/revenue/sharingclause/game-settlement-guide)中的现金结算规则、投放金规则（限时激励活动）、任务金规则（限时激励活动）。**鸿蒙系统**的内购收入按照 Android 端内购消费总额规则结算。

## 调试
普通小游戏于抖音开发者工具4.5.0及以上版本支持。
Unity WebGL 新包体于抖音开发者工具4.5.5及以上版本支持；目前可生成预览二维码，抖音鸿蒙端扫码自测。
### 模拟器调试
已增加对应设备的模拟器。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/3e3f269a477b4040a3dcf8418f36c8ab~tplv-9nona0m7ha-image.image)

### 真机调试
抖音鸿蒙端直接扫码即可。

## 问题排查
### WebSocket
- 鸿蒙端 WebSocket 通信偶现消息接收时序错乱，抖音鸿蒙端已在 39.1.0 版本修复。
- 鸿蒙WebSocket默认每30秒发送一个ping，若游戏的服务端不兼容标准WebSocket协议，就会自动断开，抖音鸿蒙端已在 39.8.0 版本修复，不再自动发ping。
