---
title: "定向分享"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/relationship-chain/directional-share
update_time: 2025-09-11
---

> 提供定向分享能力，支持用户在游戏内向指定好友发起分享，建议结合抖音小游戏里的开放数据开发互动游戏
## 当前限制
目前仅支持 抖音、抖音极速版App
详见[定向分享](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/gain-user/retweet#%E5%AE%9A%E5%90%91%E5%88%86%E4%BA%AB)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/ad7139c749b940698e6d458589b5d871~tplv-9nona0m7ha-image.image)

#### 注意事项

- 注意游戏场景，不要频繁引导分享：定向分享需要与游戏场景强相关，建议结合游戏内的好友系统、互动系统，会起到事半功倍的效果
- 配合“邀请有奖”或“礼物赠送”等功能模式，可以更大程度激发用户的分享意愿（具体实现：通过定向分享能力，入参中传入分享者的 openid（query 字段），并结合 tt.getLaunchOptionsSync 或 tt.onShow 获取启动参数中的 query 来判断是否通过分享链接启动，并给分享人发放对应的奖励）

以下描述中，金币、皮肤为游戏数据，点赞数为托管数据。
A 与 BC 为微信好友。 B 为游戏注册用户；C 为游戏流失或未注册用户。
