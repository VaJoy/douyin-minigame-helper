---
title: "关注抖音号能力介绍"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/followintroduce
update_time: 2024-07-24
---

> 本文档主要介绍“抖音号服务”能力，预计能够为开发者私域运营提供较强的助力，欢迎耐心阅读
## 抖音下的主粉关系
开发者在游戏中往往可通过接入群聊、游戏客服等沟通渠道，收集用户反馈、与用户互动
在抖音的环境中，比较常见且有效的交流方式为“主粉关系”，即用户作为粉丝关注抖音号，消费抖音号所制作的内容，长期形成较高的忠诚度与用户粘性
该能力打通游戏与抖音号，开发者可实现游戏内将用户转化为抖音号粉丝，并通过抖音号持续的内容运营实现“游戏-视频”闭环，使视频成为游戏强有力的裂变方式（新增/复玩），给予玩家实时的反馈入
因此如果游戏开发者能够运营好自己的抖音号，在游戏中引导用户进行关注，并且长期通过抖音号发布游戏相关的视频，做好持续运营，将使玩家更愿意持续投入到游戏中，收获更好的效果

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1667467509895)

## **能力案例**
某款小游戏通过关注抖音号能力，一个月抖音号涨粉几十万，开发者通过自己的游戏官方账号视频运营，使视频成为小游戏强有力的新增/复玩入口，并通过抖音号互动，增强了玩家粘性
> 游戏主界面、游戏结算页面的显著位置增加【关注抖音号】入口，使用 tips 形式提醒用户（为避免 tips 一直展示影响用户体验，可让 tips 不常驻），并在用户关注完成后，给到用户奖励

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1667467491679)

[tt.openAwemeUserProfile ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/follow/follow-aweme/tt-open-aweme-user-profile)：快速拉起关注的面板
[tt.checkFollowState](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/follow/follow-aweme/tt-check-follow-state) ：检查用户是否已经关注过抖音号，可以做「关注有礼」，当收到 success 时，可以给用户发放奖励；也可以作为前置判断，若用户已关注，则可以隐藏关注入口
> 若您在平台绑定了抖音号，更多面板会自动出现您的抖音号信息，作为您的常驻流量入口，具体接入指南请看下方
## 接入指南
第一步：登录[小游戏开发者平台](https://microapp.bytedance.com/)，进入“设置-基础设置”模块，在“抖音号绑定”一栏点击“去绑定”

| **绑定要求** | **绑定规则** | **绑定须知** |
| --- | --- | --- |
| 小游戏当前上架状态为「已发布」；近 7 日日均 DAU >= 100 （仅抖音 APP） | 每个小游戏仅支持绑定一个认证抖音号，且暂不支持解绑和换绑；企业主体小游戏支持绑定抖音企业号或个人号，个人主体小游戏仅支持绑定个人号；抖音企业号支持与 10 个同主体小游戏进行绑定，个人号支持与 5 个小游戏进行绑定 | 若选择绑定抖音企业号，请确保小游戏主体资质（统一社会信用代码）与抖音企业号认证主体资质一致；若选择绑定个人抖音号，请确保该抖音号已完成个人实名认证。 |

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1667467486313)

第二步：进入“抖音号绑定”页面，使用需绑定的抖音号，打开手机使用抖音 APP 扫一扫。 （绑定成功暂不支持更换，请谨慎选择需绑定的抖音号）

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1667467486186)

第三步：绑定成功后回到设置页，查看绑定成功的抖音号头像与昵称，企业号有特殊标记。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1667467493009)

#### 技术文档
[游戏内关注抖音号能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/follow/follow-aweme/tt-open-aweme-user-profile) ，若在接入过程中有任何问题，欢迎加群咨询

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a7d932875f2b4866831bd45316123d48)
