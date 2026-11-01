---
title: "复访版-接入指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/feed/minigame-feedpush-setting-guide
update_time: 2026-02-06
---

## 能力简介
推荐流直玩能力，是抖音为小游戏开发者打造的**场景化用户召回&获客的解决方案，**其中复访版服务于用户召回场景，整体接入流程需约 2～5 天。

> **推荐流直玩复访版核心优势--高价值信息触达+无缝衔接体验**

1. 以游戏内的高价值信息作为历史玩家召回的抓手，利用游戏进程中不同场景下的重点信息进行高效触达。
1. 基于小游戏容器预加载能力，将预加载完成的游戏在推荐流中分发给用户，实现抖音推荐流无缝进入游戏的交互体验。
### 示例介绍

| 全链路动态实机演示 （百炼英雄） | 用户抖音上玩小游戏 | 用户玩游戏过程中体力耗尽后退出游戏，用户刷抖音 | 游戏离线恢复体力，体力恢复后用户刷到游戏推荐卡片，提示用户游戏体力恢复 | 用户点击游戏推荐卡片直接进入游戏游玩 |
| --- | --- | --- | --- | --- |

### 接入收益

| 数据效果 | 活跃用户留存 | 新增付费用户留存 |
| --- | --- | --- |
| 收益说明 | 活跃用户次日留存 +10% 活跃用户7日留存 +25% | 新增付费用户次日留存 +5% 新增付费用户7日留存 +8% |

## 能力接入
### 能力申请入口

| **示意图** | **描述** |
| --- | --- |
|  | **开始接入：** Step 1：点击「运营」板块-「能力中心」 Step 2：找到「运营能力」模块-点击「推荐流游戏直玩」即可开始接入 Step 3：进入后选择「复访能力」tab Step 4：了解相关内容后，点击「开始接入」，即开始复访接入流程 |

### 接入流程简述

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/3b2fefc2222f4cb681bed7a0324ca76f~tplv-9nona0m7ha-image.image)

### 配置流程视频指引

视频链接：[https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/bef032a47c284b818dee4b9d17b2d91d~tplv-9nona0m7ha-image.image](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/bef032a47c284b818dee4b9d17b2d91d~tplv-9nona0m7ha-image.image)

开发者服务器接入流程

视频链接：[https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/268e98e8a4fa4a42b4e50f216f89880f~tplv-9nona0m7ha-image.image](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/268e98e8a4fa4a42b4e50f216f89880f~tplv-9nona0m7ha-image.image)

开发者服务器托管接入流程

### 接入流程详情
#### Step 1：方案提报
##### Step 1.1：方案提报-方案设计
1. 竖屏游戏设计规范

| 规范项 | 设计规范 | 描述 |
| --- | --- | --- |
| 游戏画布规范 |  | 游戏画面作为背景，平台交互框架置于顶层。平台交互框架包括游戏名称、文案、「继续游戏/立即去玩」按钮等。 开发者需把牵引用户的核心内容展示在「画布信息区」，更能吸引用户点击转化。 示例： |

1. 横屏游戏设计规范

| 规范项 | 设计规范 | 描述 |
| --- | --- | --- |
| 游戏画面展示规范 |  | 推荐流直玩容器会将游戏画面裁切为4:3画面尺寸，中间部分作为推荐流展示的游戏画面 开发者需把牵引用户的核心内容集中在中间的4:3画面尺寸中，避免平台裁切丢失信息 示例： |
| 游戏画布规范 |  | 画布展示区域：画面尺寸左侧宽度2/3，高度4/5区域； 游戏角色主体：展示在画面左侧1/3区域，高度为画面高度的65%； 游戏对话气泡：展示在画面左侧2/3区域，高度为画面高度80%，避开游戏主要行动按钮（开始游戏）； 游戏角色展示半身像，角色主体与对话气泡需添加投影； 游戏画面叠加40%不透明度 `#000000` 蒙层； |

##### Step 1.2：方案提报

| **步骤** | **示意图** | **描述** |
| --- | --- | --- |
| 方案提报 |  | **操作流程：** 选择需要通过「推荐流直玩游戏」能力提醒的信息场景 在对应场景下，配置文案信息和上传 UI图片 游戏内的订阅文案及订阅授权弹窗 UI图片 在抖音推荐流展示的文案+UI（含游戏内的气泡提醒） |
| 订阅 ID 生成 |  | **操作流程：** 平台将会自动生成 Content_id **重要 ：Content_id 在接入 API 开发时需要使用** 点击「下一步」进入下一流程 |

#### Step 2：研发 接入

|  | **技术架构与时序图** | **关键描述** |
| --- | --- | --- |
| 整体技术架构 | Feed复访技术架构 | **架构重点：** 采用「开发者服务器接入」方式 潜在风险：高峰期会有高并发流量查询用户就绪场景 建议方案： 接入服务端托管能力 进行完备的性能测试，并在接入配置中评估&填写最高能承载的查询 QPS 通过「获取启动信息」API 能力，判断用户是否从推荐流直玩启动，进而进行就绪场景的游戏场景加载。 游戏客户端完成对应就绪场景加载完成后，需调用「上报加载完成时机」API 进行加载完成事件上报，否则游戏不会在用户的抖音推荐流中展示。 |
| 接入时序图 | 关键 API 调用时序图 | **操作流程：** Step 1：接入「[查询订阅状态](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/check-feed-subscribe-status)」、「[订阅](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/request-feed-subscribe)」 API 能力 Step 2：接入「[获取启动信息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/lifecycle/tt-get-launch-options-sync)」API能力 Step 3：接入「[上报加载完成时机](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/data-analysis/tt-report-scene)」API能力 Step 4：接入「[预览流进入](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/tt-feed-status-change)/[退出](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/off-feed-status-change)小游戏事件」API能力 Step 5：接入「[服务端API](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/feed-game/open-api)」或者 免服务端 能力 |

##### Step 2.1：API 接入 - 客户端 SDK 部分
- 接入「推荐流直玩订阅」 API 能力，使用游戏内相关道具资源，激励用户订阅「推荐流直玩游戏提醒」，目前支持单场景/全场景订阅。
  - 查询订阅状态：[tt.checkFeedSubscribeStatus](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/check-feed-subscribe-status)（JS API）｜ [TT.checkFeedSubscribeStatus](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/direct-play)(C# API)
  - 展示订阅弹窗：[tt.requestFeedSubscribe](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/request-feed-subscribe)（JS API） ｜ [TT.requestFeedSubscribe](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/direct-play)(C# API)
> 以下是百炼英雄的示范案例，可以利用游戏内道具作为奖励（非必选），引导用户完成对推荐流直玩的订阅

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/eff21f623e734ace8e22432342bd0f48~tplv-9nona0m7ha-image.image)

用户链路示意

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/857d8ef20e8a4d698e1e02fe4bd94a42~tplv-9nona0m7ha-image.image)

参考流程图
「推荐流直玩订阅」 API 能力接入步骤详细说明：

| 步骤 | 解释 |
| --- | --- |
| 步骤一： 判断是否展示奖励入口 | 通过[tt.canIUse](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/tt-can-i-use/)("checkFeedSubscribeStatus.object.allScene")，判断用户当前的抖音版本是否支持全局订阅能力：  若返回值为 false ，表示不支持 若返回值为 true ，表示支持 |
| 步骤二： 奖励展示 | 调用 [tt.checkFeedSubscribeStatus](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/check-feed-subscribe-status) \| [TT.checkFeedSubscribeStatus](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/direct-play)，入参 allScene 设置为 true，用于查询用户的全场景订阅状态： 若返回字段 status = true，表示已订阅，不展示订阅引导入口 若返回字段 status = false，表示未订阅，展示订阅引导入口 |
| 步骤三： 引导用户点击订阅 | 用户点击「去订阅」按钮时，在[tt.onTouchEnd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/click-event/tt-on-touch-end/)回调中同步调用 [tt.requestFeedSubscribe](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/request-feed-subscribe) \| [TT.requestFeedSubscribe](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/direct-play)，入参 allScene 设置为 true，用于拉起订阅面板：  若用户点击面板上的「允许」按钮则完成订阅，平台侧回调订阅结果 success = true，用户已完成订阅；  若用户点击面板上的「拒绝」按钮，平台侧回调订阅结果 success = false，用户未完成订阅。 |

- 接入「[获取启动信息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/lifecycle/tt-get-launch-options-sync)」API能力，获取当前小游戏的【启动场景scene】和【自定义的信息query】字段，从而判断当前游戏启动是否是推荐流直玩场景启动，并自动加载到相关的就绪场景。

| 能力名称 | 场景信息字段 |  | 类型 | 字段值 | 字段描述 |  |
| --- | --- | --- | --- | --- | --- | --- |
| JS API：[tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-get-launch-options-sync/) C# API：[​TT.GetLaunchOptionsSync​](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/system/game-launch-params) | scene |  | string | xx3041 | 用于判断是否为推荐流直玩场景（xx为可变的数字，判断后四位是 3041 即可确认为推荐流直玩） |  |
|  | query | feed_game_scene | number | 1 | 离线收益场景 |  |
|  |  |  |  | 2 | 体力恢复场景 |  |
|  |  |  |  | 3 | 重要事件掉落 |  |
|  |  | feed_game_extra | string | 自定义 | 开发者自定义字段，可通过 [推荐流直玩能力 OpenAPI 接入文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/feed-game/open-api) 接口的 extra 字段进行赋值 |  |
|  |  | feed_game_content_id | string | 平台生成 | 本次启动对应的文案 ID |  |
|  |  | feed_game_channel | number | 1 | 复访用户 |  |
|  |  |  |  | 2 | 获客用户 |  |

- 接入「[上报加载完成时机](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/data-analysis/tt-report-scene)」API能力，游戏客户端完成对应就绪场景加载完成后，需调用「上报加载完成时机」API 进行加载完成事件上报，否则游戏不会在用户的抖音推荐流中展示。

| 能力名称 | 场景信息字段 | 类型 | 字段值 | 字段描述 |
| --- | --- | --- | --- | --- |
| JS API：[tt.reportScene](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/data-analysis/tt-report-scene) C# API：[​TT.ReportScene​](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/data-analysis#86bffde4) | sceneId | number | **固定为：7001** | 标识游戏场景加载完成，达到用户可交互状态 |

- 接入「[预览流进入](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/tt-feed-status-change)/[退出](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/off-feed-status-change)小游戏事件」API能力
> 备注：该能力仅在较新的抖音版本支持，厂商需要自行做好低版本兼容。（低版本可以通过监听用户首次触摸事件进行兼容）
「预览流进入/退出小游戏事件」API能力可以监听用户从推荐流进入/退出小游戏的事件，进而判断用户是否真实启动游戏，即是否为真实活跃用户。

| 能力名称 | 字段描述 |
| --- | --- |
| JS API：[tt.onFeedStatusChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/tt-feed-status-change) C# API：[TT.OnFeedStatusChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/direct-play#cfcded26) | 通过callback的type enum表示用户交互动作 feedEnter：从 推荐流进入小游戏 feedExit：退出小游戏回到推荐流 |

伪代码示例

```js
// 判断启动渠道为推荐流直玩场景
if (getLaunchOptionsSync.scene equal xx3041) {
    // 游戏侧上报预启动数据
    reportData('preboot');
    
    let firstEnter = true;
    // 启动监听
    onFeedStatusChange(({ type }) => {
        // 用户首次从预览流进入游戏
        if (firstEnter && type equal 'feedEnter') {
            firstEnter = false;
            // 游戏侧上报用户活跃数据
            reportData('Activity');
        }
    })
}
```

##### Step 2.2：研发接入 - 托管测试账号配置
开发者构造并提供可达复访全场景就绪状态的游戏账号，供平台链路测试验证确保功能正常；若无法提供可留空。

| 步骤 | 示意图 | 描述 |
| --- | --- | --- |
| 测试账号配置 （非必填项） |  | **操作流程：** 点击「账号设置」右侧对话框填写账号信息 |

##### Step 2.3：研发接入 - 服务端配置选项
- 接入方式1：服务端托管能力（免开发者服务端接入）

> 开发者通过 SDK 上报游戏就绪场景时机，平台自动根据用户就绪场景召回用户

**🌟 能力接入优势 🌟**
📢 **节省开发成本：**无需单独开发服务端**，**直接点击开通即可**，节省开发者1-2天接入时长**
📢 **超稳定性能**：无需担心服务端压力无法承载及性能问题，保证用户体验，**提升复访曝光**
> 备注：当前托管场景**仅支持****「根据时长判断」****就绪场景，**具体接入示例如下：

| 定时体力恢复场景 | 定时领取礼包 |
| --- | --- |
| 当用户体力恢复到满值时 判定为就绪状态 | 当用户有机会获得奖励后 判定为就绪状态 |

1. 托管能力开通入口：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/4938e0c6e463497db98f99fb81558633~tplv-9nona0m7ha-image.image)

  托管能力开通入口
1. 托管能力接入前后的时序图差异：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/971eb05500bf4927aa832c0875013791~tplv-9nona0m7ha-image.image)

托管能力时序图

| **步骤** | **描述** |
| --- | --- |
| 步骤一： 复访托管能力开启 | 操作流程**：** Step 1：点击「**服务端配置**」-**「未开通」**-**「确定」** |
| 步骤二： 接入「[tt.storeFeedData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/tt-store-feed-data)」API，托管游戏推荐流直玩用户场景就绪状态 | 接入示例：假设scene为1 ，contentID为contentID123，用户在时间戳1744949793000后该场景可就绪，则开发者可按照下述示例，调用接口向平台上报用户场景就绪时间。 |
| 步骤三（可选）： 接入 「[tt.getFeedData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/tt-get-feed-data)」API， 查询用户场景就绪状态 | 接入示例：假设要获取scene为1，contentID为contentID123的游戏场景当前是否就绪，开发者可按照下述示例调用接口，获取当前时刻对应场景的就绪状态。 |

- 接入方式2：开发者服务器接入

> 若服务端托管能力无法满足（如：用户就绪状态需实时判断），平台也支持通过 SPI 接口回查开发者服务器，获取用户就绪场景列表后，实现用户召回。

| **步骤** | **示意图** | **描述** |
| --- | --- | --- |
| 服务器信息配置 |  | **操作流程：** Step 1：完成服务器：「Domain」、「Path」及「测试用户 OpenID」 Step 2：点击「功能测试」，将会自动校验服务器功能是否完备 Step 3：填写自身接口可承载的 QPS 上限 Step 4：点击「性能测试」，将会自动进行接口压测 |
| 接口功能及性能检测 |  | **操作流程：** 按上述流程进行测试后，将会在 2min 内自动生成测试结果 **仅当「功能测试」及「性能测试」均通过时**，才可进行下一步 |

#### Step 3：测试体验

| 步骤 | 示意图 | 描述 |
| --- | --- | --- |
| 测试设备信息配置 |  | 操作流程： Step 1：点击「前往开通」可跳转至通用调试设备管理页面添加测试设备 Step 2：使用抖音扫描屏幕二维码完成设备信息的添加 |
| 进入测试模式进行调试 |  | 操作流程： Step 1：选择测试的方案及版本，配置测试模式所需环境，点击「生成二维码」按钮，可生成测试入口二维码 Step 2：测试用户游玩小游戏，让游戏场景处于就绪状态后，使用抖音扫描屏幕二维码进入测试模式 Step 3：根据测试模式内弹窗指引，完成能力接入调试，无法刷到直玩卡的问题平台会有弹窗提示，开发者可以根据提示进行定位。 |

#### Step 4：测试报告检查

| **步骤** | **示意图** | **描述** |
| --- | --- | --- |
| 测试报告检查及确认 |  | **操作流程：** 完成测试验证后，平台将会自动生成测试用例报告 开发者需根据实际的测试情况，确认已完成该测试项的测试 测试报告检查确认完成后，可点击「申请上线」 申请上线要求：游戏版本和相关服务发布后，点击申请上线按钮 |

#### Step 5：发布线上小流量验证

| **步骤** | **示意图** | **描述** |
| --- | --- | --- |
| 发布线上小流量验证 |  | **操作流程：** 仅一个方案上线通过后，系统将自动发起「线上小流量验证」 小流量验证期间可随时点击「中止验证」中止当前小流量验证，进行方案增加或删除等操作 小流量验证主要检查上线后用户对游戏的实际反馈，当用户的正点击率达到准入要求后可自动全量上线 |
| 小流量验证结果 | 小流量验证通过   小流量验证未通过 | 验证信息：正CTR 标准：曝光PV达到5000 |

#### Step 6：功能全量上线

| **步骤** | **示意图** | **描述** |
| --- | --- | --- |
| 小流量验证通过后，申请推全 |  | **操作流程：** 小流量验证通过后，将自动申请全量上线，后续可直接查看该游戏的直玩数据效果 |

### 开发者数据分析指引（可选接入）
> 如果开发者有自建的用户数据分析能力，需接入本能力；如果没有自建的用户数据分析能力，则无需接入
在推荐流直玩场景，分为两个启动阶段：
1. 「直玩预启动」阶段：用户无感知，此时用户还未真实进入游戏。
1. 「直玩点击启动」阶段：用户刷到直玩并且点击“继续游戏”，此时用户已真实进入游戏，可计算为真实活跃。
为了帮助开发者更好地识别用户处于哪个启动阶段，是否有真实进入游戏，进而校准用户活跃相关统计数据。平台提供了用户在「直玩预启动」和「直玩点击启动」两个转化行为的开发者感知能力。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/f9a3b6e7c07b438aa1cb41ea66bdfd62~tplv-9nona0m7ha-image.image)

- 接入「[获取启动信息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/lifecycle/tt-get-launch-options-sync)」API能力，获取当前小游戏的【启动场景scene】和【自定义的信息query】字段，从而判断当前游戏启动是否是推荐流直玩场景启动，并自动加载到相关的就绪场景，并对用户活跃统计埋点做特殊处理。

| 能力名称 | 场景信息字段 |  | 类型 | 字段值 | 字段描述 |  |
| --- | --- | --- | --- | --- | --- | --- |
| JS API：[tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-get-launch-options-sync/) C# API：[​TT.GetLaunchOptionsSync​](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/system/game-launch-params) | scene |  | string | xx3041 | 用于判断是否为推荐流直玩场景（xx为可变的数字，判断后四位是 3041 即可确认为推荐流直玩） |  |
|  | query | feed_game_scene | number | 1 | 离线收益场景 |  |
|  |  |  |  | 2 | 体力恢复场景 |  |
|  |  |  |  | 3 | 重要事件掉落 |  |
|  |  | feed_game_extra | string | 自定义 | 开发者自定义字段，可通过 [推荐流直玩能力 OpenAPI 接入文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/feed-game/open-api) 接口的 extra 字段进行赋值 |  |
|  |  | feed_game_content_id | string | 平台生成 | 本次启动对应的文案 ID |  |
|  |  | feed_game_channel | number | 1 | 复访用户 |  |
|  |  |  |  | 2 | 获客用户 |  |

- 接入「[预览流进入](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/tt-feed-status-change)/[退出](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/off-feed-status-change)小游戏事件」API能力
> 备注：该能力仅在较新的抖音版本支持，厂商需要自行做好低版本兼容。（低版本可以通过监听用户首次触摸事件进行兼容）
「预览流进入/退出小游戏事件」API能力可以监听用户从推荐流进入/退出小游戏的事件，进而判断用户是否真实进入游戏，即是否为真实活跃用户，对用户活跃统计埋点做特殊处理。

| 能力API | 字段描述 |
| --- | --- |
| JS API：[tt.onFeedStatusChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/tt-feed-status-change) C# API：[TT.OnFeedStatusChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/direct-play#cfcded26) | 通过callback的type enum表示用户交互动作 feedEnter：从 推荐流进入小游戏 feedExit：退出小游戏回到推荐流 |

伪代码示例

```js
// 判断启动渠道为推荐流直玩场景
if (getLaunchOptionsSync.scene equal xx3041) {
    // 游戏侧上报预启动数据
    reportData('preboot');
    
    let firstEnter = true;
    // 启动监听
    onFeedStatusChange(({ type }) => {
        // 用户首次从预览流进入游戏
        if (firstEnter && type equal 'feedEnter') {
            firstEnter = false;
            // 游戏侧上报用户活跃数据
            reportData('Activity');
        }
    })
}
```

## FAQ
[推荐流直玩游戏能力 FAQ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/feed/faq)

开发者服务器托管接入流程