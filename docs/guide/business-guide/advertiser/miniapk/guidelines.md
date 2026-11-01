---
title: "投放指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/advertiser/miniapk/guidelines
update_time: 2024-07-24
---

## 一、**整体流程图**

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661157128828)

- **流量范围：**现仅支持抖音、头条两个客户端投放，其他端选取后无法投出广告，不会产生消耗。
- **转化目标：**支持**激活、付费（包括激活且付费、每次付费、付费ROI）及关键行为**的转化目标，字节内部自行打通数据上报链路，可支持准确归因，**无需广告主进行数据归因与回传对接**
## 二、投放流程
### 阶段一：创建抖音小游戏
> 预计 5-14 天完成，取决于广告主排期
> 说明：抖音小游戏接入流程与审核标准，基本与三方（微信）小游戏对齐，甚至流程效率更高。
**常见 Q&A**
> Q1: 开发者平台是否支持上架同款游戏的马甲包？
> A1:理论上不支持马甲包，但如果客户进行马甲包差异化包装，且有对应的版号的情况下，可支持上架
> Q2:如何接入 iOS 支付？
> A2:微端投放仅支持安卓端投放，无需接入 iOS 支付
**投前准备**

| **说明** | **流程概览** |
| --- | --- |
| 一、前期准备 1、注册开发者账户，创建小游戏 首先需要在[开发者平台](https://microapp.bytedance.com/)创建您自己的账号，然后以开发者身份创建小游戏。详情请参考[注册与入驻](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/register) 2、主体认证 主体认证可选注册为个人主体或者企业主体，流程包含主体资质提交和对公打款验证、主体在结算、资质认证上会有所不同，详情参考[注册与入驻](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/register) 3、完善开发设置 在后台的开发设置获取 appid，配置域名；另可在设置界面添加团队协作者，该权限添加开发者可在[后台](https://microapp.bytedance.com/applist)查看小游戏管理列表（可自由切换列表/图标模式）   二、开发调试 具体可参考：[开发小游戏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/develop) 三、审核上线 登录 [小游戏开发者平台](https://microapp.bytedance.com/)，点击所需小游戏的名称，跳转至 【版本管理 】页面。  目前针对小游戏分为三个版本： 具体可参考：[提审指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/examineguide) 线上版本：面向全部用户的正式版本 审核版本：开发版本的提审阶段，通过之后可以进入灰度测试，否则需要根据驳回原因退回修改，此版本请谨慎对外分享 测试版本：开发版本的测试阶段，开发完成上传之后可以扫码进入测试体验，此版本请谨慎对外分享 |  |

### 阶段二：投放设置
> 预计 1-2 天完成
#### 高频问题
> 1、在开发者平台进行微端包下载，广告主需提前让直客申请微端权限白名单，才可在开放平台看到微端包下载入口
> 2、微端投放不需要广告主进行数据对接和回传，但需在「事件管理」进行事件配置，数据检测自动通过，同时事件管理不需要客户进行联调，可直接开始创建计划投放
> 3、投放前白名单申请广告变现类小游戏（IAA）投放关键行为转化目标之前，需通过直客提报白名单，目前支持 ipu 次数配置内购类小游戏（IAP）投放付费相关转化目标前，需通过直客提报白名单
> 4、创建广告时，选择「推广-创建新广告组-营销链路-行为转化-应用」（注意不要选择“销售线索收集”，会造成无转化数据的情况）
> 5、注意选择站内广告位进行投放（首选抖音信息流投放），避免选择穿山甲投放，穿山甲端小游戏广告无法展示
#### 操作步骤
#### 1、**获取小游戏微端包包名**
在[字节小游戏开发者平台](https://microapp.bytedance.com/game/)创建好小游戏后，进入要投放的小游戏主页，获取小游戏的 appid，得到微端包包名。
包名格式为：com.bytedance.小游戏 appid.miniapk
> 例如：小游戏 A 的小游戏 appid 为 tt54786584aa11b87111，则小游戏 A 的微端包包名为 com.bytedance.tt54786584aa11b87111.miniapk
- 第一步：进入在字节小游戏开发者平台，在【总览】页面获取小游戏appid

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661157432379)

- 第二步：根据小游戏appid获取到小游戏微端包包名为：com.bytedance.小游戏appid.miniapk
#### **2、在巨量后台获取 appid**
在[巨量引擎广告投放平台](https://business.oceanengine.com/brand/index)，填写游戏相关信息，获取巨量 appid
> 注意：
> 1.申请巨量 appid 时，手填的英文名不要使用小游戏 appid，否则检测页面会卡死
> 2.支持平台只能选择“安卓平台”（微端包仅支持安卓投放）
- 第一步：进入广告投放平台-资产-移动应用

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661158829085)

- 第二步：数据检测-前往创建-申请AppID

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661158829075)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661158829058)

#### **3、获取小游戏正式微端包**
**获取正式微端包**
在小游戏开发者平台上的小游戏微端界面，绑定巨量 APPID，获取正式微端包
> 需找直客销售申请加白微端包的权限（小游戏上架后即可申请微端包权限）
> 注意：请检查，包名格式为：com.bytedance.小游戏 appid.miniapk
进入在字节小游戏开发者平台，选择对应的小游戏，在「推广-信息流投放」页面获取小游戏微端包

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661159660029)

**巨量上传应用包**
在巨量引擎广告投放平台，应用管理中心，上传小游戏正式微端包，填写正确的游戏相关信息，提交，等待审核通过
> 注意：
> 1.上传应用时隐私协议的主体必须与填写的主体信息一致
> 2.审核若被打回，可以可根据提示原因整改后申请复审，
进入巨量广告投放平台-资产-移动应用-「我创建的应用」，新建应用包

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661158992331)

注意审核：上传应用时隐私协议的主体必须与填写的主体信息一致
![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661159048917)

应用管理-查看我创建的应用
#### **4、进行应用数据联调（事件管理）**
> 不支持使用转化跟踪
**创建资产**
1. 选择需要创建的资产类型
1. Android应用仅支持选择已上传「应用管理平台」的应用；
**注意：**
> 1.每个应用仅可被作为资产添加一次；
> 2.回传方式选择“SDK 回传”需要 APP_ID
**进入广告投放平台-资产-事件管理（原转化跟踪）-创建资产**

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661159161090)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661159160845)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661159161182)

**创建事件**
1. 创建【激活、play_session、注册、付费、次留】等事件
1. 事件可支持使用场景描述：
- 是否可作为广告计划优化目标使用
- 是否可作（为xx事件的）深层目标使用
**添加事件-选择事件类型，选择要监测的用户事件类型**
添加：激活、play_session、注册、付费

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661159223223)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661159223665)

**数据检测**
> 无需操作，自动通过数据检测
1. 添加事件后，选择“回传方式”，鼠标悬浮“应用SDK回传”，通过“前往检测”进入数据检测；或在资产添加后，点击“立即检测”/“数据检测”进入检测
1. 必检数据：激活、play_session、注册、付费
注意：
> 1.点击“开始检测”进入数据检测，平台会检测当前应用、当前 App ID 在 24h 内的数据上报情况。为非实时检测，因此需先完成对应事件的上报，再进行检测。
> 2.需保证必检项正常上报、实际上报的 package_name 和 APP_ID 申请时的 package_name 一致
> 3.默认检测当前 APP_ID 下所有设备上报记录，点击右上角“检测当前设备数据上报”，可扫码获取 device_id，仅检测当前设备下 24h 内数据上报
**完成联调**
> 非必须，建议直接跳过
1. 多事件批量联调：在联调工具中进行批量联调
1. 用「今日头条APP」或「抖音APP」扫码授权，在对应app信息流中，刷新并找到检测转化上报广告，点击进入应用、快应用、落地页或小程序内完成转化行为，完成联调。
1. 在事件管理后台，可看到是否转化上报成功，如上报正常，点击“结束联调”即可
数据检测旨在检验 SDK 集成、事件调用无误，若存在某些必检事件强制通过的需求，请联系对接的销售进行评估及提报。**事件未通过联调不影响微端正常上报和投放。**
**联调工具-在联调工具中进行批量联调（直接跳过）**

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661160053527)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661160053683)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661160059168)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661160053557)

#### **5、橙子建站落地页搭建**
**在橙子建站创建落地页，并关联小游戏资产**
**注意：**
> 请先在应用管理中，确保五要素的完善，否则落地页会被拒审
> 五要素："应用名称、开发者、版本号、隐私政策、权限列表"
- **第一步：进入广告投放平台-资产-落地页-自定义落地页-橙子落地页页面**

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661160143739)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661160143519)

- **第二步：新建橙子建站落地页**

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661160143077)

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661160143852)

#### 6、**在广告后台进行广告搭建**
三步完成搭建：创建广告组->创建广告计划->创建广告创意
**创建广告组**
推广-创建新广告组-营销链路-行为转化-**应用（注意不要选择“销售线索收集”）**

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661160199663)

**创建广告计划**
投放内容-下载链接：填写微端包对应的下载链接
优先应用商店下载：不启用

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661160274330)

创建广告计划，数据对接方式选择「事件管理」
![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661160302698)

**创建广告创意**
组合方式：自定义（可以上传多个视频/图片和文案，系统将对视频/图片和文案进行优选组合，针对不同的用户选择综合效果更好的组合展现）
广告头像：作为头条、抖音火山版、西瓜和抖音的广告头像展示
广告评论：启用
添加素材

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661160387071)

应用下载详情页：选择橙子建站落地页

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661160405985)

注意：
1. 建议选站内的广告位（暂时不支持投放穿山甲），不推荐选择通投
1. **iaa产品投放目标为关键行为**，**不要投激活**，请提前联系对应直客同学，**沟通抖音小游戏产品运营同学进行配置**，目前已支持**ipu次数+eCPM**配置
1. **iap产品**投放付费转化目标前，一定提前联系直客同学，**沟通抖音小游戏运营同学配置付费上报**，否则无法投放付费相关转化目标
#### 7、开始投放
正式开始投放后，可通过广告投放平台数据看板或小游戏开发者平台数据看板中查看投放相关数据，详见「获取投放数据」模块。
**常见 Q&A**
> Q1:微端目前看数据还是只能在媒体后台吗？
> A1:广告主可以在巨量后台看 7 天内的实时数据，同时可以在小游戏后台看 120 天的离线数据评估整体回收
> Q2:抖音小游戏微端包投放数据广告主可进行归因吗，即实现在广告主后台看注册和付费等？
> A2:现已新增 OPENID 宏参下发，广告主可在事件管理添加三方监测链接（参考[监测链接-事件管理功能介绍](https://event-manager.oceanengine.com/docs/8650/track_url_doc/)），获取 OPENID 进行精准归因，OPENID 宏参格式为 OPENID（左右两边是双英文下划线）。其他宏参（广告计划 id、广告主 id 等）获取参考[监测链接发送服务](https://open.oceanengine.com/labels/7/docs/1696710655781900)。
#### 8、创建小游戏微端分包
1. **前置条件**
小游戏已完成第一个微端主包的创建并进行投放，达到小游戏微端【信息流投放累计消耗超过 5W】，则该小游戏自动开通**额外**「创建微端包」功能。
1. **创建流程**
点击【创建微端包】按钮，增加一个新的微端包卡片

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1664251062216)

**1）微端包名**
默认命名为【游戏名称（微端包_1)】，后续新增的微端包默认命名为【游戏名称（微端包_2)】、【游戏名称（微端包_3)】、【游戏名称（微端包_4)】、【游戏名称（微端包_5)】。最多支持额外创建 5 个微端包，包名默认填充，不支持开发者修改。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661407706735)

**2）巨量引擎 APPID 获取与绑定**
参考小游戏微端首包创建流程，需注意巨量 APPID 申请时，Android 包名对应格式为：
【游戏名称（微端包_1)】：对应的微端包名为【com.bytedance.小游戏 appid_2.miniapk】
【游戏名称（微端包_2)】：对应的微端包名为【com.bytedance.小游戏 appid_3.miniapk】
【游戏名称（微端包_3)】：对应的微端包名为【com.bytedance.小游戏 appid_4.miniapk】
【游戏名称（微端包_4)】：对应的微端包名为【com.bytedance.小游戏 appid_5.miniapk】
【游戏名称（微端包_5)】：对应的微端包名为【com.bytedance.小游戏 appid_6.miniapk】

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661407794490)

**3）应用包检测&数据上报**
参考小游戏微端首包流程