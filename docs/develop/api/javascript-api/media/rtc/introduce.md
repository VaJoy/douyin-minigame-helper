---
title: "RTC实时语音文档介绍"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/rtc/introduce
update_time: 2026-07-24
---

## 能力简介
火山 RTC 团队与抖音开放平台团队深度合作，共建打造抖音小游戏生态下的语音通话方案最佳实践方案，帮助业务在抖音平台上快速上线具备游戏语音的小游戏，能力目前支持抖音和抖音极速版，其他宿主暂未支持。
## 落地场景
**狼人杀: **线上太空狼人杀、跑跑狼人杀，古风杀等小游戏，玩家可通过语音社交
**剧本杀:** 线上剧本杀、剧情杀等小游戏玩家可通过语音社交
**联合闯关类: **好友搭配联合闯等小游戏，如类森林冰火人等，玩家可通过语音沟通协作

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1664443586977)

## 能力优势
复用抖音直播连麦、聊天室，抖音社交中的语音通话能力，直接使用 Native 原生 SDK，提供小游戏官方 RTC 组件。在开发者体验、延时均低于其他小游戏 RTC 方案

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1664443668809)

## 接入方式
请点击下方接入文档进行能力接入：
[**实时语音接入文档**](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/rtc/tt-get-rtc-engine)
- 接入前，需要申请开通 RTC 服务，注册生成 RTC 的 appid 与 token才能正常使用：[注册地址](https://www.volcengine.com/docs/6348/69865)
- Token 相关的请参考：[token生成相关](https://www.volcengine.com/docs/6348/70121)
- 开通后，联系平台客服，告知已开通注册获得token，平台核验通过后，连麦能力即可进行正常调用

### 完整示例

```js
// 1. 获取实例，需要传入火山平台申请的 RTC AppId
const rtcEngine = tt.getRtcEngine("RTC AppId");

// 2. 监听需要的事件
rtcEngine.onJoinChannelSuccess(() => {});
rtcEngine.onConnectionLost(() => {});
rtcEngine.onWarning(() => {});
rtcEngine.onError(() => {});

// 3. 获取频道（对接开发者服务获取）和 token (参考火山 token 生成)
let channelId = "channelIdtest";
let token = "testToken";

// 4. 广播连麦 channelId，所有用户加入频道
rtcEngine.joinChannel({
  channelId,
  uid: "user1",
  token
});

// 5. 开启本地推流
rtcEngine.enableLocalAudio();

rtcEngine.leaveChannel();

rtcEngine.leaveChannel();
```
