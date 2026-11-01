---
title: "运营指引"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/operationalguidelines
update_time: 2025-12-02
---

## 一、用户获取
> 同一小游戏可以同步上线多个宿主端（宿主：即小游戏可上线的字节 APP），为开发者节省大量的人力和时间。目前已经逐步开放今日头条、抖音、火山、西瓜视频、头条极速版，更多字节系产品在陆续接入中。新游上线，抖音小游戏平台均会给到冷启动量，后期会根据产品数据，转化率等数据，通过去中心化算法模块精准匹配、直接触达用户，为游戏持续给量。

#### 搜索相关资源配置
> 配置指引：[搜索相关资源配置_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/gain-user/search)
- 搜索关键词：
「搜索」是小游戏重要的自然流量入口，是用户对玩小游戏目标明确、意图直接的需求表达，运营好该入口，能够免费获取粘性强、游玩深度高、变现价值高的用户，提升游戏经营指标。
目前，当用户精准搜索您的小游戏名称时，已支持展示入口卡片。但除此之外，还存在大量的泛需求、模糊需求场景，通过设置搜索关键词，能够增加用户搜到您的小游戏的概率。
- 搜索结果图：
「搜索结果图」是重要的搜后透传信息之一，当用户首次搜索该款游戏时予以展示。您可上传包含小游戏玩法、版本、IP联名等信息的图片，该能力可以有效辅助用户搜后决策，提升点击率。

#### 直玩获客
> 配置指引：[获客版-接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/feed/customer-access-guide)
直玩获客是抖音小游戏基于「推荐流直出游戏能力」开启的「获客拉新」应用。将大盘游戏用户画像等数据接入推荐算法，为接入获客能力的游戏推荐适配新用户，帮助小游戏厂商开拓流量池。直玩获客使用预加载技术，需注意游戏角色创建等操作应在用户点击进入直玩容器后进行。

#### 好友邀请组件
> 配置指引：[好友邀请组件_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/gain-user/invite)
抖音小游戏的「好友邀请组件」是一种内置社交功能，允许玩家通过分享链接、弹窗提示或按钮直接邀请微信/抖音好友加入游戏，提升用户活跃度和裂变传播。

#### 内容转发分享
> 配置指引：[内容转发分享_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/gain-user/retweet)
抖音小游戏的「内容转发分享」是指玩家将游戏内容以图文/视频形式分享至抖音或其他社交平台的功能，旨在通过用户自发传播提升游戏曝光和拉新。

#### 小游戏互推资源位能力
> 配置指引：[小游戏互推资源位能力_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/gain-user/recommended)
为用户畅玩更多游戏提供清晰的产品路径，除了用户本身心智外，作为游戏产品，需要给到用户清晰的产品路径，让用户更快速准确地畅玩更多游戏，平台经过实验判断，最合适的推荐场景是在游戏内，这条路径明显会有更多的优势。
游戏内直接可以跳转到其他游戏，路径简洁；
开发者可以根据自己的游戏品类去提前判断用户的兴趣偏好，给到更精准的游戏推荐；
游戏内容有限或用户感到乏味时，其他的游戏推荐能够为用户带来更新鲜的刺激，延长用户的使用时长；
针对以上信息，平台提供了“游戏推荐组件”的 API 能力，接入后可以在游戏内快捷拉起游戏推荐面板，让用户能够在游戏内直接打开另一款小游戏。

#### 抖音小游戏录屏带配乐能力
> 配置指引：[抖音小游戏录屏带配乐能力_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/gain-user/record-with-bgm)
开发者可以使用此功能，在游戏的录屏分享中指定一首乐曲作为默认配乐：当玩家拉起分享录屏的发布器时，在背景音乐中自动配上开发者预设的乐曲。
建议开发者使用抖音近期热门的音乐，并经常更新配乐可显著提升录屏分享的视频播放量和锚点点击量

#### 录屏与分享
> 配置指引：[录屏与分享_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/gain-user/record-share)
【视频录制及分享】是字节跳动系平台独有的也是最核心的内容展示能力及产品分发能力。我们希望通过平台提供的视频相关 api 接口能力，能让小游戏发行和平台能力充分结合，更好的利用，帮助小游戏在本平台获得更多用户及更好收益，新游上线平台会配给一定的冷启动流量作为小游戏上线的起始流量，开发者可以通过使用视频录制能力，充分利用这批冷启动量，通过平台内容分发机制给小游戏带来更多后续流量。

#### 录屏添加剪映视频模板能力
> 配置指引：[录屏添加剪映视频模板能力_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/gain-user/capcut-with-game)
为更好帮助开发者利用录屏分享视频推广小游戏，抖音小游戏面向开发者推出“录屏添加剪映视频模板”的能力（仅支持抖音）
开发者可通过在后台绑定剪映号并持续更新创作剪映模板，实现以录屏分享为分发核心的流量变现渠道。同时，用户直接在游戏内生成的录屏内容嵌套剪映模板进行发布，发布优质录屏视频也更容易获取流量。
开发者完成配置后，将审核通过的模板 id 传入对应的检验接口，即可将剪映模板自动嵌套在用户的分享视频内
## 二、用户留存
#### 【必接】侧边栏
> 接入指引：[「必接」侧边栏复访能力_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/-retention/sidebar)
随着抖音小游戏复访能力的完善，抖音首页侧边栏日活持续增高，平台推荐开发者均接入抖音首页侧边栏复访功能，引导用户从首页侧边栏进入游戏，养成打开抖音->打开首页侧边栏->快速访问小游戏的心智，通过侧边栏留存的提升，带动小游戏大盘整体留存提升，平均提升次日留存率 12%+、7 日留存率 8%+。
此能力已于「2023 年 11 月 24 日」起开启「必接审核」，届时未接入该能力的小游戏在「新游首发」&「版本更新」环节会有「拒审」风险，为避免影响游戏上线&更新节奏，同时也为了提升小游戏留存，请尽快规划接入时间，感谢您的配合。

#### 订阅消息能力
> 接入指引：[订阅消息能力_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/-retention/subscribe-message)
抖音小游戏的"订阅消息"能力是平台为开发者提供的用户触达工具，允许游戏获得玩家授权后，通过系统级消息通道向玩家推送游戏相关通知。

#### 小游戏抖音版本更新提醒能力
> 接入指引：[小游戏抖音版本更新提醒能力_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/-retention/reminding)
为更好帮助开发者提升小游戏留存，抖音小游戏面向开发者推出【小游戏抖音版本更新提醒】的能力。平台会通过抖音小游戏官方号【游戏通知】为完成相关配置的开发者提供版本更新（仅抖音）推送能力，轻松触达玩家：用户通过点击推送消息即可进入游戏，形成复玩通道。

#### 直玩复访
> 接入指引：[推荐流直出小游戏能力接入指引_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/feed/minigame-feedpush-setting-guide)
直玩复访能力以游戏内的高价值信息为玩家召回抓手，使用游戏进程中的不同场景掉落的重点信息进行玩家触达，通过预加载能力，将预加载完成的游戏在推荐流中分发给符合条件的用户，实现抖音推荐预览流无缝进入游戏的体验，吸引用户留存。

#### 游戏排行榜能力介绍
> 接入指引：[游戏排行榜能力介绍_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/-retention/rankintroduce)
小游戏无需下载、即点即玩的特点，非常适合邀请抖音的好友进行互动，排行榜是小游戏必不可少的元素，朋友间的对比能够有效激发用户的游戏动力和传播动力，根据实验发现，上线了好友排行榜功能的游戏，整体活跃时长+8%，留存+3%，新增活跃用户数+14.5%，是非常正向的能力

#### 游戏内关注抖音号能力
> 接入指引：[游戏内关注抖音号能力_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/-retention/follow-douyin)
开发者在游戏中往往可通过接入群聊、游戏客服等沟通渠道，收集用户反馈、与用户互动
在抖音的环境中，比较常见且有效的交流方式为“主粉关系”，即用户作为粉丝关注抖音号，消费抖音号所制作的内容，长期形成较高的忠诚度与用户粘性
该能力打通游戏与抖音号，开发者可实现游戏内将用户转化为抖音号粉丝，并通过抖音号持续的内容运营实现“游戏-视频”闭环，使视频成为游戏强有力的裂变方式（新增/复玩），给予玩家实时的反馈入口
因此如果游戏开发者能够运营好自己的抖音号，在游戏中引导用户进行关注，并且长期通过抖音号发布游戏相关的视频，做好持续运营，将使玩家更愿意持续投入到游戏中，收获更好的效果

#### 粉丝群聊能力
> 接入指引：[粉丝群聊能力_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/-retention/group)
小游戏想要形成良好的生态，在持续优化自己的游戏质量之外，也要重视并运营好自己的玩家群体。在游戏行业中，游戏群聊、游戏排行、开发者座谈等能够为游戏的“长线氛围建设”提供有效的帮助。

#### 绑定头条号
> 接入指引：[绑定头条号_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/-retention/binding-toutiao-account)
抖音小游戏的"绑定头条号"能力是指开发者可以将旗下小游戏与今日头条账号进行关联，实现跨平台内容分发和用户导流的官方功能。
- 核心价值
  - 流量互通：打通抖音与头条系产品的用户池
  - 内容同步：游戏动态可同步展示在头条号内容中
  - 数据共享：获取更全面的用户行为数据分析
  - 品牌统一：建立跨平台的游戏品牌认知

#### 小游戏站
> 接入指引：[「小游戏站」能力接入指引_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/-retention/game-site/game-station-guide)
> 运营指南：[「小游戏站」运营指南_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/-retention/game-site/mini-game-guide)
「小游戏站」是提供给开发者在抖音经营玩家的私域运营阵地，支持开发者通过发布活动、攻略、版更、礼包等内容长线运营玩家，同时也在游戏外场景为玩家提供交流互动、游戏反馈等社区能力；
小游戏站作为独立产品形态，会在抖音多个场景曝光，帮助游戏积累更多私域用户。

## 三、数据管理
抖音小游戏平台为开发者提供了完整的自运营工具链+深度数据分析能力，涵盖拉新、留存、变现、调优全生命周期管理，并为达到条件的小游戏提供支持。关于小游戏运营效果的数据分析，可以通过平台提供的数据分析看板进行查看，更多内容可见[《数据基础介绍》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/about-data/intro)
## 四、买量推广
抖音小游戏为开发者提供了高效、精准的买量推广工具，通过平台海量用户数据和智能投放系统，帮助游戏快速获取优质用户，对于有推广需求的开发者，平台也开放了相应的买量机制，详情可见[《小游戏发行人计划》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/advertiser/pub/introduction)。
## 五、终止运营
如需停止对外运营小游戏，可进入开发后台基础[设置管理页面点击下架](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/norms/in-game-operation-norms)。 注意：提前60天向用户发布公告。