---
title: "订阅消息能力介绍"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/introduce
update_time: 2026-02-26
---

基于抖音的通知渠道，我们为开发者提供了可以高效触达用户的订阅消息能力，以便实现服务的闭环并提供更佳的体验。
开发者在游戏内，可通过 [tt.requestSubscribeMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/subscribe-message/tt-request-subscribe-message)向用户发起消息订阅请求，开发者需后台自行记录用户是否订阅成功及订阅成功的次数。
用户在小游戏中订阅指定的消息内容后，开发者可以在后台通过[下发消息服务](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/subscribe-notification/notify/)把一条模板消息发送给用户，用户最终在抖音的 “消息-游戏通知” 中收到。
用户成功订阅一次，开发者可在游戏认为场景合适的时机，向该用户下发一条模板消息。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/%E8%AE%A2%E9%98%85%E6%B6%88%E6%81%AF1-5685223228859120.jpeg)

## 功能介绍
**本能力支持抖音。**
#### 一次性订阅消息
一次性订阅消息用于解决用户使用小游戏后，后续服务环节的通知问题。用户自主订阅后，开发者可**不限时间**地下发**一条对应的服务消息**；每条消息可单独订阅或退订。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/WechatIMG1181-5368727273163691.jpeg)

#### 长期订阅消息
一次性订阅消息可满足小游戏的大部分游戏场景需求，但也存在一次性订阅无法满足的场景，如长期的礼包提醒，签到等。为便于服务，我们提供了长期性订阅消息，用户订阅一次后，开发者可长期下发多条消息。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/WechatIMG1182-6629908826517337.jpeg)

#### 订阅消息权限管理
以下几种情况的订阅消息权限可以在【设置--订阅消息管理】页面中进行管理，包括开启与拒绝接受。
- 一次性订阅消息选择“总是保持以上选择，不再询问”后。
- 长期性订阅消息选择“允许”后。
- 长期性订阅消息选择“拒绝，不再询问”后。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/WechatIMG1183-4448819850240146.5.jpeg)

#### 推送说明
- 订阅消息下发条件：用户自主订阅。
- 订阅消息卡片跳转能力：点击查看详情可跳转至该小游戏。
- 推送位置： 【抖音 - 消息 tab - 游戏通知】。
#### 使用说明
#### 步骤一：获取消息 ID
1. 登录[字节开发者平台](https://developer.toutiao.com/) 手动配置获取模板 ID（路径：运营-运营能力-订阅消息）
    
![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/WX20220801-152042@2x-2619422386632741.5.png)

    
![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/WX20220801-152115@2x-6861609150113150.png)

1. 找到合适的模板后，按需勾选关键字，添加后可以获得消息 ID（MSG开头），此时即可发送订阅消息。
#### 步骤二：获取下发权限
详见小游戏服务端消息订阅接口[tt.requestSubscribeMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/subscribe-message/tt-request-subscribe-message/)。
#### 步骤三：调用接口下发订阅消息
详见[发送订阅消息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/subscribe-notification/notify/)。
### 使用规范
（1）使用订阅消息能力进行诱导点击、下发与用户预期不符的内容被视为违规。
（2）针对关注小游戏的用户可以发送 push 与气泡，对恶意诱导关注的行为将视为违规。
- 第一次违规，封禁接口 7 天
- 第二次违规，封禁接口 14 天
- 第三次违规，封禁接口 30 天
- 第四次违规，永久封禁接口
（3）开发者平台暂不支持新增模板、新增关键字的申请，后期将逐步开放。
（4）如对抖音模板库里不存在的模板有强烈诉求，可通过右下角「开发者助手」-输入两次「人工」进行反馈。
