---
title: "分享介绍总览"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/social/all
update_time: 2024-07-24
---

提供社交分享能力，通过用户的分享行为为游戏带来裂变与增量
## ShareParam
`ShareParam` 是指开发者最终传递给发布器的数据，可以根据约定传入部分自定义数据，具体字段可查阅 [开发字段](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param)
其中比较关键的为 channel 字段，决定最终的分享类型（常规分享、录屏分享、好友邀请等）
## 分享逻辑
- SDK 右上角更多菜单提供常规分享的能力
- 开发者在开发小游戏时，可以在游戏界面绘制自定义按钮，在按钮的回调中调用，直接调起对应的分享发布方式，开发者直接通过 `tt.shareAppMessage(shareParam)` 方法，将 `shareParam` 传递给系统发布器即可
## 分享效果预览
### 社交好友邀请（channel == invite）
支持`抖音/抖lite`当传入的 channel 为 invite 时，触发后会拉起好友邀请面板，经验证，整体的分享成功率在 75%左右，具体数值视开发者如何将其与游戏相结合，但整体效果优于传统的常规分享， 具体开发方式请点击[转发分享 API](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param)
#### **好友邀请组件核心功能如下：**
> **社交关系分组清晰：**「双关好友、我的粉丝、我的关注」，双关好友排序靠前，分享成功率更高，清晰的社交关系分组更有利于用户进行社交分享
> **在线状态实时展示：**使用「小绿点」标记在线状态，对于社交类游戏而言，方便用户快速识别在线用户，邀请一起玩游戏；对于「分享有奖」之类的游戏内社交裂变功能，在线状态也更容易让用户筛选目标分享用户
> **多人分享：**玩家可以在面板上点击多个按钮进行多次分享，效率更高，更有利于游戏的分享裂变，同时也支持分享到群聊和搜索定向分享
> **消息触达：**被分享的用户会收到 IM 私信卡片，如果是在线用户，会在屏幕上方出现「强提醒的 push」
> **回调信息：**游戏内可以基于分享回调（success / cancel），给用户发放激励（如邀请好友有奖）

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/WechatIMG953-946332021578879.5.jpeg)

### 常规分享
默认分享方式，channel 为空字符串或者不传，即通过抖音的好友分享面板，分享成功后在 IM 聊天界面出现游戏卡片， 具体开发方式请点击[转发分享 API](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/WechatIMG954-2758859562966464.5.jpeg)

### 录屏视频分享（channel == video）
录屏分享，通过发布器将视频分享到社区，带上视频锚点，用户消费后可以点击启动，开发者使用录屏分享时，如果未使用剪映模版和录屏配音(defaultBgm 字段) 能力时，将触发一键分享逻辑，将会弹出一键分享弹框， 具体开发方式请点击[转发分享 API](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/WechatIMG955-1911770932323400.jpeg)
