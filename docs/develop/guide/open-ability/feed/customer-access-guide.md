---
title: "获客版-接入指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/feed/customer-access-guide
update_time: 2026-02-06
---

## 简介
推荐流直玩能力，是抖音为小游戏开发者打造的**场景化用户召回&获客的解决方案，**其中获客版服务于**拉新获客**场景，整体接入流程需约 2～5 天。

> **推荐流直玩获客版核心优势——拉新流量阵地+无缝体验衔接**

1. 获客版将抖音大盘用户的游戏偏好数据融入推荐算法，让接入直玩获客的游戏获得更广阔的拉新流量阵地。
1. 基于小游戏容器预加载能力，将预加载完成的游戏在推荐流中分发给用户，实现抖音推荐流无缝进入游戏的交互体验。
### 示例介绍

| 用户刷抖音 | 获客卡片展现 | 用户点击进入游戏 | 开启新手剧情 |
| --- | --- | --- | --- |

### 接入收益

| 数据效果 | 新增激活人群 | 新增激活收入 |
| --- | --- | --- |
| 收益说明 | 新增激活总人数贡献占比：**27.5%** | 新增激活总收入贡献占比：**16.8%** |

## 能力接入
### 能力申请入口

| **示意图** | **描述** |
| --- | --- |
|  | **开始接入：** Step 1：点击「运营」板块-「能力中心」 Step 2：找到「运营能力」模块-点击「推荐流直玩游戏能力」即可开始接入 Step 3：进入后选择「获客能力」tab Step 4：了解相关内容后，点击「开始接入」，即开始获客接入流程 |

### 接入流程简述

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/a3aaaaf5b2cb4a5a97613e271b004600~tplv-9nona0m7ha-image.image)

### 全流程视频指引

视频链接：[https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/fa37829d9cba4da1a646e7baf9cd277b~tplv-9nona0m7ha-image.image](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/fa37829d9cba4da1a646e7baf9cd277b~tplv-9nona0m7ha-image.image)

### 接入流程介绍
#### Step 1：方案提报
##### Step1.1：方案提报-方案设计
1. 竖屏游戏设计规范

| 规范项 | 设计规范 | 描述 |
| --- | --- | --- |
| 游戏画布规范 |  | 游戏画面作为背景，平台交互框架置于顶层。平台交互框架包括游戏名称、文案、「继续游戏/立即去玩」按钮等。 开发者需把牵引用户的核心内容展示在「画布信息区」，更能吸引用户点击转化。 示例： |

1. 横屏游戏设计规范

| 规范项 | 设计规范 | 描述 |
| --- | --- | --- |
| 游戏画面展示规范 |  | 推荐流直玩容器会将游戏画面裁切为4:3画面尺寸，中间部分作为推荐流展示的游戏画面 开发者需把牵引用户的核心内容集中在中间的4:3画面尺寸中，避免平台裁切丢失信息 示例： |
| 游戏画布规范 |  | 画布展示区域：画面尺寸左侧宽度2/3，高度4/5区域； 游戏角色主体：展示在画面左侧1/3区域，高度为画面高度的65%； 游戏对话气泡：展示在画面左侧2/3区域，高度为画面高度80%，避开游戏主要行动按钮（开始游戏）； 游戏角色展示半身像，角色主体与对话气泡需添加投影； 游戏画面叠加40%不透明度 `#000000` 蒙层； |

##### Step1.2：方案提报

| **步骤** | **示意图** | **描述** |
| --- | --- | --- |
| 方案提报 |  | **操作流程：** Step 1：开发者上传用于获客拉新的游戏首帧画面图片及文案 |
| 方案填写 |  | **操作流程：** Step 1：完成方案上传后，点击「保存」，点击「下一步」 |

#### Step 2：研发 测试
##### **Step 2.1：API 接入**

|  | **示意图** | **描述** |
| --- | --- | --- |
| 整体技术架构 |  | **整体流程** ： Step 1： 抖音推荐流向用户分发游戏直玩卡时，抖音在后台自动预加载游戏进程，此处建议开发者开发游戏保护机制，游戏保护机制可查看下文的【风险提示（推荐接入）】。 Step2：游戏客户端完成游戏场景加载完成后，需调用「上报加载完成时机」API 进行加载完成事件上报，否则游戏不会在用户的抖音推荐流中展示。 Step3：当用户滑到直玩卡时，游戏前台展示并进入交互流程。 |
| 关键 API 调用时序 |  | **操作流程：** Step 1：接入「[获取启动信息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/lifecycle/tt-get-launch-options-sync)」API能力 Step 2：接入「[上报加载完成时机](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/data-analysis/tt-report-scene)」API能力 Step 3：接入「[预览流进入](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/tt-feed-status-change)/[退出](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/off-feed-status-change)小游戏事件」API能力 |

- 接入「[获取启动信息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/lifecycle/tt-get-launch-options-sync)」API能力，获取当前小游戏的【启动场景scene】和【自定义的信息query】字段，从而判断当前游戏启动是否是推荐流直玩场景启动，并自动加载到相关的游戏场景。

| 能力名称 | 场景信息字段 |  | 类型 | 字段值 | 字段描述 |  |
| --- | --- | --- | --- | --- | --- | --- |
| JS API：[tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-get-launch-options-sync/) C# API：[TT.GetLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/system/game-launch-params) | scene |  | string | xx3041 | 用于判断是否为推荐流直玩场景（xx为可变的数字，判断后四位是 3041 即可确认为推荐流直玩） |  |
|  | query | feed_game_scene | number | 0 | 获客场景 |  |
|  |  | feed_game_extra | string | 自定义 | 开发者自定义字段，可通过 [推荐流](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/feed-game/open-api)[直玩](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/feed-game/open-api)[能力 OpenAPI 接入文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/feed-game/open-api) 接口的 extra 字段进行赋值 |  |
|  |  | feed_game_content_id | string | 平台生成 | 本次启动对应的文案 ID |  |
|  |  | feed_game_channel | number | 1 | 复访用户 |  |
|  |  |  |  | 2 | 获客用户 |  |

- 接入「[上报加载完成时机](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/data-analysis/tt-report-scene)」API能力，游戏客户端完成对应游戏场景加载完成后，需调用「上报加载完成时机」API 进行加载完成事件上报，否则游戏不会在用户的抖音推荐流中展示。

| 能力API | 场景信息字段 | 类型 | 字段值 | 字段描述 |
| --- | --- | --- | --- | --- |
| JS API：[tt.reportScene](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/data-analysis/tt-report-scene) C# API：[TT.ReportScene](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/data-analysis#86bffde4) | sceneId | number | **固定为：7001** | 标识游戏场景加载完成，达到用户可交互状态 |

- 接入「[预览流进入](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/tt-feed-status-change)/[退出](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/feed-subscribe/off-feed-status-change)小游戏事件」API能力
> 备注：该能力仅在较新的抖音版本支持，厂商需要自行做好低版本兼容。（低版本可以通过监听用户首次触摸事件进行兼容）
「预览流进入/退出小游戏事件」API能力可以监听用户从推荐流进入/退出小游戏的事件，进而判断用户是否真实启动游戏，即是否为真实活跃用户。

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

##### **Step 2.2：研发测试**

| 步骤 | 示意图 | 描述 |
| --- | --- | --- |
| 测试设备信息配置 |  | 操作流程： Step 1：点击「开发设置」-「测试管理」可添加测试设备 Step 2：使用抖音扫描屏幕二维码完成设备信息的添加 |
| 进入测试模式进行调试 |  | 操作流程： Step 1：选择测试的方案及版本，配置测试模式所需环境，点击「生成二维码」按钮，可生成测试入口二维码 Step 2：使用抖音扫描屏幕二维码进入测试模式 Step 3：根据测试模式内弹窗指引完成能力接入调试，可通过弹窗对无法刷到直玩卡的情况进行问题定位 |

#### Step 3：测试报告检查

| **步骤** | **示意图** | **描述** |
| --- | --- | --- |
| 测试报告检查及确认 |  | **操作流程：** 完成测试验证后，平台将会自动生成测试用例报告 开发者需根据实际的测试情况，确认已完成该测试项的测试 测试报告检查确认完成后，可点击「申请上线」 申请上线要求：游戏版本和相关服务发布后，点击申请上线按钮 |

#### Step 4：发布线上小流量验证

| **步骤** | **示意图** | **描述** |
| --- | --- | --- |
| 发布线上小流量验证 |  | **操作流程：** 仅一个方案上线通过后，系统将自动发起「线上小流量验证」 小流量验证期间可随时点击「中止验证」中止当前小流量验证，进行方案增加或删除等操作 小流量验证主要检查上线后用户对游戏的实际反馈，当用户的正点击率达到准入要求后可自动全量上线 |
| 小流量验证结果 | 小流量验证通过   小流量验证不通过 | 验证信息：正CTR 标准：曝光PV达到5000 |

#### Step 5：功能全量上线

| **步骤** | **示意图** | **描述** |
| --- | --- | --- |
| 小流量验证通过后，申请推全 |  | **操作流程：** 小流量验证通过后，将自动申请全量上线，后续可直接查看该游戏的直玩数据效果 |

### 风险提示（推荐接入）⚠️

> 推荐流直玩能力采用预加载技术，在游戏尚未展示和用户未进入游戏前，属于**潜在用户阶段**，若开发者游戏侧在此阶段提前进行角色创建等操作，会造成大量非真实用户的请求和资源占用，影响**服务器稳定**及**游戏生态**。

针对上述风险，平台建议的解决思路：
1. 开发者侧对于推荐流直玩预加载的用户暂不做注册创角等消耗资源的请求
1. 用户点击进入游戏后，开发者侧应静默完成用户注册，并实现游戏进程的继承和延续

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/d1952b8e180b4084adf41dd44612ab2d~tplv-9nona0m7ha-image.image)

### 开发者数据分析指引（可选接入）
> 如果开发者有自建的用户数据分析能力，需接入本能力；如果没有自建的用户数据分析能力，则无需接入
在推荐流直玩场景，分为两个启动阶段：
1. 「直玩预启动」阶段：用户无感知，此时用户还未真实进入游戏。
1. 「直玩点击启动」阶段：用户刷到直玩卡并且点击“立即去玩”，此时用户已真实进入游戏，可计算为真实活跃。
为了帮助开发者更好地识别用户处于哪个启动阶段，是否有真实进入游戏，进而校准用户活跃相关统计数据。平台提供了用户在「直玩预启动」和「直玩点击启动」两个转化行为的开发者感知能力。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/5e11348b79724846836c4b30a312e98f~tplv-9nona0m7ha-image.image)

- 接入「[获取启动信息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/lifecycle/tt-get-launch-options-sync)」API能力，获取当前小游戏的【启动场景scene】和【自定义的信息query】字段，从而判断当前游戏启动是否是推荐流直玩场景启动，并自动加载到相关的游戏场景，并对用户活跃统计埋点做特殊处理。

| 能力名称 | 场景信息字段 |  | 类型 | 字段值 | 字段描述 |  |
| --- | --- | --- | --- | --- | --- | --- |
| JS API：[tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-get-launch-options-sync/) C# API：[TT.GetLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/system/game-launch-params) | scene |  | string | xx3041 | 用于判断是否为推荐流直玩场景（xx为可变的数字，判断后四位是 3041 即可确认为推荐流直玩） |  |
|  | query | feed_game_extra | string | 自定义 | 开发者自定义字段，可通过 [推荐流](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/feed-game/open-api)[直玩](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/feed-game/open-api)[能力 OpenAPI 接入文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/feed-game/open-api) 接口的 extra 字段进行赋值 |  |
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