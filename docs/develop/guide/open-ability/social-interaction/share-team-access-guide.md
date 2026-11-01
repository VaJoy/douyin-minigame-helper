---
title: "分享组队接入指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/social-interaction/share-team-access-guide
update_time: 2026-07-24
---

## 能力简介

> “分享组队”是小游戏提供的一种高级社交分享能力。它允许开发者创建一种可动态更新状态的“动态消息”卡片，支持用户通过抖音私信(IM) 私聊或群聊场景快速邀请好友组队进入游戏。

> 从客户端 30.9.0 开始，支持转发动态消息。动态消息对比普通消息的优点是：消息发出去之后，开发者可以通过后台接口修改部分消息内容。
### 适用场景
- 多人组队游戏：如 MOBA、FPS 或“开黑”类游戏，房主创建房间后分享到好友群，群友可看到实时人数变化和游戏状态变化（组队中或者已开始）。
- 社交棋牌游戏：创建棋牌室后邀请牌友，卡片标题显示“好友已就位，就等你补位！”，吸引好友快速加入。
- 限时活动邀请：如“今晚 8 点 Boss 挑战，仅限 10 人”，通过动态消息实时更新剩余名额，营造紧迫感。
### **用户体验**
#### **游戏内发起组队示例(非IM玩法专区入口)**

| 页面描述 | 示意图 |
| --- | --- |
| 用户在游戏内创建房间，发送组队卡片邀请好友组队 | 《眼力达人》游戏内发起组队界面 |
| 被邀请用户收到组队卡片邀请 被邀请用户点击组队卡片，组队即可成功组队 | 《眼力达人》游戏内组队成功界面 |

#### 玩法专区体验示例

| 页面功能描述 | 示意图 |
| --- | --- |
| 用户从 IM 入口进入玩法专区一级页面 用户从玩法专区一级页面进入二级页面 | 一级页面: 单款游戏平均日曝光人数 >1kw，单款游戏日点击人数＞3w，日新增贡献＞2w 二级页面: 单款游戏平均日曝光人数 ≈20w，单款游戏日点击人数＞1k，日新增贡献 ≈500 |
| 邀请用户点击「组队玩」进入组队房间，**自动发出组队邀请卡片** 被邀请用户在聊天界面收到组队卡片 被邀请用户点击组队卡片，即可成功组队 | 《天天台球》玩法专区组队界面 《猛鬼宿舍》玩法专区组队界面 组队成功率＞50%，进一步贡献游戏启动uv |

#### 玩法专区游戏资源位说明
- **保底资源**：已完成组队分享能力接入的小游戏，保证游戏稳定在玩法专区二级页面展示。
- **排序逻辑**：平台将依据游戏的曝光点击转化率、组队发起成功率等核心指标对玩法专区的游戏动态调优排序，转化效率最高的头部优质游戏，有机会晋升至玩法专区一级页面进行展示，获取更高曝光流量倾斜。

### **动作收益**

| 游戏动作 | 游戏收益 （参考40+款已接入游戏的动作前后数据） |
| --- | --- |
| 游戏新增【组队玩法】收益 | 新增激活人数+14%、日启动人数+30% |
| 游戏上架【玩法专区】收益 | 新增激活人数+16%、日启动人数+33% |

## 能力接入
### 接入流程简述

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/6e2b97b5e1a84c91b798fb2b0eed78b6~tplv-9nona0m7ha-image.image)

### 核心特性
- 动态更新：分享卡片发出后，其展示状态和内容（如“1/2组队中”）可通过服务端 API 实时更新，为接收方提供最及时的房间信息。
- 状态流转：消息拥有明确的生命周期（如：招募中 → 已开始 → 已结束），并支持在状态变更时更新卡片点击后的跳转逻辑（`query` 参数）。
- 高效触达：分享以 IM 私信卡片形式发送给指定好友或群聊，对在线用户有强提醒，点击即可直接拉起游戏，路径短、转化高。
- 数据透传：支持通过 `query` 参数在分享和启动链路中传递自定义信息，如房间号、邀请者 ID 等，便于实现自动进房、邀请归因与奖励发放等逻辑。

### 接入流程详情
交互时序图：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/cc7d20b6866f4bcf80a846625742fe7b~tplv-9nona0m7ha-image.image)

##### Step 1：创建房间
- 抖音聊天场景内 - 「一起玩」启动游戏并自动创建房间
游戏客户端需要通过[tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/lifecycle/tt-get-launch-options-sync)` `或者[tt.onShow](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/lifecycle/tt-on-show)来获取启动参数，判断如果是发起者的一键组队启动场景则开始创建房间逻辑。聊天框内一起玩自动发卡的启动参数：key=`_team_action`，value=`create`。
示例代码：

```js
// 在游戏启动时 
launchOptions = tt.getLaunchOptionsSync();
console.log("游戏启动参数:", launchOptions);

if (launchOptions.query && launchOptions.query._team_action == "create") {
    console.log(`一键组队场景`);
   // 执行创建房间的逻辑...
   createRoom(roomId);
}
```

> 特别地，如果需要根据聊天类型(群聊或者私聊)创建不同的组队房间或者其他定制化逻辑，则需要从 `query`中额外获取参数去判断，获取方式同上述 `_team_action`。
> - 从`query`中额外获取 `_chat_type`，其值 1 为 私聊，2 为 群聊
> - 从`query`中额外获取 `_scene`，当其值为`"video_call"`时为音视频（VOIP）场景

游戏内 - 用户主动创建房间
无需和平台侧有交互

##### Step 2：创建 `activity_id`
在每次发起组队分享前，开发者需要通过服务端调用 [createActivityID](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/social-interaction/team-share-ability/create-activity-id) 接口为卡片创建一个唯一标识 `activity_id`。后续更新组队卡片的数据都需要传入这个 `activity_id`。

> 注意：
> - `activity_id` 是后续所有操作（客户端分享、服务端更新）的凭证，请务必妥善保存。
> - 活动到期后（默认 24 小时），分享卡片将自动变为“已结束”状态，且无法再被更新。
> - 如果上一次发卡已经创建过了`activity_id`，且与上一次是同一个组队房间，则请勿重复创建`activity_id`

##### Step 3：发送组队卡
在发起组队场景中，小游戏客户端在获取到 `activity_id` 后，通过调用[tt.shareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/retweet/tt-share-app-message)接口发起分享。此操作在游戏启动期间只应执行1次，避免重复发卡。

| **参数** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| channel | string | - | 是 | “抖音聊天框内 - 「一起玩」自动发卡”场景传`team_up` “游戏房间内 - 发起组队发卡”场景传`invite` |
| query | string | - | 否 | 查询字符串，必须是 `key1=val1&key2=val2` 的格式。从这条转发消息进入后，可通过 `tt.getLaunchOptionsSync` 获取启动参数中的 query 用来实现信息透传 |
| templateId | string | - | 否 | `channel`为`invite`时必传此素材 ID，指定通过平台审核的 `templateId` 来选择分享内容，需在平台设置且通过审核 |
| extra | Extra | - | 是 | 请看`Extra`类型说明 |
| success | function | - | 否 | 分享成功后执行的回调函数 |
| fail | function | - | 否 | 分享失败或者用户取消发布器后执行的回调函数 |
| complete | function | - | 否 | 分享完成（无论成功与否）后执行的回调函数 |

其中 `templateId` 分享素材ID通过如下图进行配置后获取

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/66368ecb79ff46f9834422628428d5aa~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/70a50caf2f4841f499e5798d8ac1393c~tplv-9nona0m7ha-image.image)

图一
图二
**Extra类型说明 **

| **参数** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| useTeamInvitationStyle | boolean | - | 是 | true |
| activityID | string | - | 是 | 从第2步中获取的 `activity_id`。 |
| templateInfo | Array<TemplateInfo> | - | 是 | 数组，组队卡参数。TemplateInfo 对象包含 name 和 value 两个字段。 |
| versionType | string | current | 否 | 指定通过此消息启动的小游戏版本，默认为 `current` (线上版)，可设为 `latest` (开发版) 用于测试。 |

**TemplateInfo类型说明 **

| **参数** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| name | string | - | 是 | 参数名，有效值： `memberCount`——当前房间人数`roomLimit`——房间人数上限 `users`——当前房间内的玩家OpenID |
| value | string | - | 是 | 参数值 |

示例代码：

```js
tt.shareAppMessage({
  channel: "team_up", //识别发卡场景，传team_up或者invite
  query: "roomId=xxx&key2=val2", // 一般需要带上一些房间id之类的字段，由开发者自行定义实现
  extra: {
      activityID: "6800*****",     // 从服务端createActivityID获取
      templateInfo: [
          {
              name: "memberCount",
              value: "1" // 初始人数
          },
          {
              name: "roomLimit",
              value: "4" // 房间人数上限
          },
          {
              name: "users",              value: '[\"grtmlx2dqcmTO7C\"]' // 当前房间内的用户OpenID，为空则传[]
          }
      ],
      versionType: "current"    // 指定通过动态消息进入的小游戏版本：线上版current、测试版latest
  },
  success() {
    console.log("分享成功");
    // 可在此处上报分享成功事件
  },
  fail(e) {
    console.log("分享失败");
  },
});
```

错误码

| errNo | errMsg | 错误原因 |
| --- | --- | --- |
| 20001 | xxx should be xxx, but got xxx | 参数错误 |
| 20002 | missing debug uid for channel "team_up" | 模拟组队时无法读取测试的uid，可能是启动参数_team_debug_mode=1 时缺少_team_debug_uid，或者是弹窗提示输入uid时取消输入 |
| 10401 | server error ${data.err_msg} | 平台服务端错误 |
| 10103 | network unavailable | 网络请求不可达 |

##### Step 4：好友点击卡片进入游戏
被邀请的好友点击组队卡片后，会拉起小游戏。此时，游戏客户端需要通过 [tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/lifecycle/tt-get-launch-options-sync) 或者[tt.onShow](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/lifecycle/tt-on-show)来获取启动参数，判断是否由组队分享卡片进入，
示例代码：

```js
const launchOptions = tt.getLaunchOptionsSync();
console.log("游戏启动参数:", launchOptions);

if (launchOptions.query) {
  const activityID = launchOptions.query.activity_id;
  const roomID = launchOptions.query.room_id;
  console.log(`通过分享卡片进入，activityID为: ${activityID}，roomID为: ${roomID}`);
  
  // 执行加入房间的逻辑...
  joinRoom(roomId);
}
```

如果是发起组队的人关掉游戏，从群聊组队卡进入游戏， 这时候会回到之前的游戏，并触发tt.onShow，开发者可以在tt.onShow的回调参数读到res.query判断是否需要引导用户进房
##### Step 5：更新组队卡状态
当游戏内组队状态发生变化时，由开发者服务端调用 [updateDynamicMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/social-interaction/team-share-ability/update-dynamic-message) 接口来更新已发出的分享卡片，根据 `activity_id` 更新指定组队卡的状态。
消息状态说明 (`target_state`)
消息有3个状态，分别有其对应的文字内容。其中状态 0 可以转移到状态 0 、1和2，状态 1和状态2 无法再转移。

| 字段 | 取值 | 状态说明 | 允许转移的状态 |
| --- | --- | --- | --- |
| target_state | 0 | 组队中 | 0, 1, 2 |
|  | 1 | 组队成功，队伍成员不再发生变更，一般是游戏已开始 | 无 |
|  | 2 | 组队失败，一般是队伍解散 | 无 |

组队卡参数 (`template_info`)：见“Step 3：发送组队卡”，注意`users`需要尽可能保证此数组中最先进房的玩家排在前面，最后进房的玩家排在最后面。
**新增参数 (**`card_version`**)：默认为1即可**
示例代码：

```bash
curl --location 'https://minigame.zijieapi.com/mgplatform/api/apps/share/update_dynamic_message' \
--header 'access-token: 08011218462b4b54307662766c3150454833752b353739513d3d' \
--header 'Content-Type: application/json' \
--data '{
    "access_token": "08011218462b4b54307662766c3150454833752b353739513d3d",
    "activity_id": "562176002",
    "target_state": 0,
    "card_version": 1,
    "query": "?room_id=48796951",
    "version_type": "",
    "template_info": [
        {
            "name": "memberCount",
            "value": "2"
        },
        {
            "name": "roomLimit",
            "value": "3"
        },
        {            "name": "users",            "value": "[\"abc\",\"abc\"]"        }
    ]
}
'
```

### 上线前的预览调试
- 小游戏接入能力，需要发版上线后才有可能在群聊功能的组队玩游戏列表中可见。为了方便开发者在上线前完成调试开发，在上述的接入流程增设以下步骤:
#### 模拟发起组队场景

| 步骤 | 示意图 | 步骤描述 |
| --- | --- | --- |
| 指定启动参数 |  | 在IDE上新增编译模式，指定启动参数 `_team_action=create&_team_debug_mode=1`。 使用该编译模式后会自动更新project.config.json内容，这个时候点击预览或真机调试生成的预览码会带上此启动参数。 |
| 模拟流程说明 |  | 在启动参数存在_team_debug_mode=1 时，调用 tt.shareAppMessage 发送组队卡时的流程会多出一个模拟流程，需要获取被发卡用户的 uid，有两种方式： 如果启动参数存在query._team_debug_uid=${uid}，则会自动取此uid作为测试用户的uid。 如果不存在query._team_debug_uid，则会弹窗提示输入测试用户的uid（弹窗请求输入仅IDE和Android端支持）。 之后组队卡将发送到uid对应用户的私聊界面。 注意**测试用户必须和当前抖音登录用户是好友关系**，该步骤是为了模拟线上从聊天界面点击去组队按钮打开游戏后游戏将组队卡发回给当前聊天界面的流程。 |
| 生成预览码 |  | 在IDE模拟器内的发卡模拟要求使用新版IDE 4.5.1，基础库版本选择4.2.0.0以上，目前还未发布，接入期间请用生成预览码的方式来调试：同样操作指定query参数，`_team_action=create&_team_debug_mode=1&_team_debug_uid=${uid}` ，生成预览码在真机上模拟发送组队卡 |
| 模拟器内完成测试流程 |  | 如果希望在模拟器内就完成发送组队卡的测试，首先需要选择调试基础库在4.2.0以上 上述流程不变，需要前置在模拟器内登录抖音帐号，否则模拟器无法正确获取当前用户的抖音登录态 |

#### 模拟加入组队场景

| 步骤 | 流程说明 |
| --- | --- |
| 模拟加入组队测试 | 在发起组队调用 tt.shareAppMessage 的传参中，需要传 versionType='latest'，且将小游戏代码上传到开发者后台，之后发出去的卡片进入才能进入到测试版 |

### 验收 & 上架「组队一起玩」资源位流程
- 需先按以下步骤和测试要求，由厂商自行完成验收并录屏，梳理能力验收文档
- 由验收后，每周五18:00前完成资源上架

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/33e33260b35b4a6cad20a79ccc2d55e5~tplv-9nona0m7ha-image.image)

- 资源上架后，可通过以下路径查看游戏资源上架情况

| 验收文档步骤名称 | 验收文档详情说明 | 示意图 |
| --- | --- | --- |
| **Step1：梳理游戏基本信息** | 此部分内容包含以下信息： 游戏名称 app_id 提审版本 研发人员（选填，方便后续协助调试） 测试人员（选填，方便后续协助调试） |  |
| **Step2：功能测试** | **场景说明：**「组队一起玩」自动发出分享卡，发起组队 **测试信息：**根据以下测试点准备测试截图及录屏，并确认测试是否通过，未通过备注需备注原因 「组队一起玩」组队卡片成功发出 组队卡片信息展示正确，游戏名称、icon，组队文案等 组队信息正确，房间状态，房间人数 卡片点击可以正常拉起游戏 | 「组队一起玩」组队卡片成功发出、正常拉起游戏示意图 |
|  | **场景说明：**「游戏内组队房间」-用户主动发出分享卡，发起组队 **测试信息：**根据以下测试点准备测试截图及录屏，并确认测试是否通过，未通过备注需备注原因 「游戏内组队房间」组队卡片成功发出 | 「游戏内组队房间」组队卡片成功发出示意图 |
|  | **场景说明：**组队房间信息实时更新测试 **测试信息：**根据以下测试点准备测试截图及录屏，并确认测试是否通过，未通过备注需备注原因 其他玩家加入，卡片信息正常更新 游戏开始，卡片信息变化为 游戏已开始 队伍解散，卡片信息变化 | 组队房间信息实时更新测试 |
| **Step3：是否存在遗留问题** | 如果有遗留问题，需要按照以下内容进行记录 问题描述 优先级 问题状态 当前跟进人 | - |

### FAQ
**Q1：客户端最低版本要求是多少？**
支持「组队一起玩」能力的抖音客户端最低版本为 37.5.0。对于低于此版本的客户端，将无法使用此能力。建议在调用前使用 tt.getSystemInfoSync() 获取基础库版本号后进行判断，基础库的最低支持版本是4.2.0。

**Q2：分享卡片的消息一定能触达用户吗？**
消息会以 IM 私信形式发送。如果接收方好友在线，通常会收到强提醒 Push；如果离线，则会以普通私信形式存在于聊天列表中。触达率受用户网络状况、通知设置等多种因素影响，非 100% 保证。

**Q3：如果 **[updateDynamicMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/social-interaction/team-share-ability/update-dynamic-message)** 接口调用失败怎么办？**
- 检查网络连接和 `access_token` 是否有效
- 根据返回的错误码排查问题，常见错误包括 `activity_id` 不存在或已过期、参数格式错误等。建议设计重试机制，并在多次失败后在游戏内给予用户明确提示（如“同步队伍状态失败，请稍后再试”）
- 严格保证先创建ActivityID，再调用发卡[tt.shareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/retweet/tt-share-app-message)接口去发卡，等待发卡成功且有组队人员变动或者游戏开始等组队状态变动再调用update接口更新组队状态，如果创建完ActivityID就直接调用[updateDynamicMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/social-interaction/team-share-ability/update-dynamic-message) 接口也会报错。
- 组队状态target_state的流转只能从0->0、0->1、0->2，不支持从1->2，即1和2是最终态

**Q4：**[createActivityID](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/social-interaction/team-share-ability/create-activity-id)** 的调用频率有限制吗？如何保证幂等？**
- 平台对 OpenAPI 有通用的频率限制。建议不要在短时间内为同一个业务场景（如同一房间）重复创建 `activity_id`。
- [createActivityID](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/social-interaction/team-share-ability/create-activity-id) 接口本身不保证幂等，如果需要，开发者可以在自己的服务端通过业务逻辑（如检查同一房间是否已有有效的 `activity_id`）来实现。
- 对于 [updateDynamicMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/social-interaction/team-share-ability/update-dynamic-message)，虽然接口本身没有强制幂等，但开发者可以通过传入唯一的业务 ID（如自定义的 `msg_id`）并在服务端做校验来避免重复更新。

**Q5：用户分享出去的卡片，其他人能看到状态更新吗？**
可以。只要是通过同一个 `activity_id` 分享出去的卡片（无论分享给多少人或群），当服务端调用 [updateDynamicMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/social-interaction/team-share-ability/update-dynamic-message) 时，所有这些卡片的状态都会同步更新。

**Q6：如果分享到群里，卡片状态如何展示？**
分享到群聊中的卡片同样支持动态更新。群内所有成员都能看到卡片状态的实时变化，非常适合在公会群、开黑群中组织活动。

**Q7：如何感知用户进入房间？**
当有新玩家加入房间时，由客户端通知服务端，服务端可调用抖音的[updateDynamicMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/social-interaction/team-share-ability/update-dynamic-message)接口，并传入对应的`activity_id`和新的状态（如更新`memberCount`表示当前人数变化），以此感知用户进入房间。同时，被邀请好友点击卡片进入游戏后，游戏客户端通过[tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/lifecycle/tt-get-launch-options-sync) 或[tt.onShow](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/lifecycle/tt-on-show)获取启动参数，判断是否由组队分享卡片进入并获取透传的`query`信息，执行加入房间逻辑，也可确认用户进入房间。

**Q8：access_token怎么获取？失效时间是多长？可以缓存吗？**
- 获取方式参考：https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token。
- 失效时间：当前token失效时间是2小时，前提是2小时内未刷新，如果已经刷新了新的token，那么旧的token会5分钟内过期。因此开发者可以使用缓存，但需要在保证全局token的刷新频率下进行缓存，比如1小时刷新1次，那么合理的缓存时间可以设置为15分钟或者半小时。

**Q9: 如何区分是热启进入组队玩场景，还是从后台切回前台进入？**
通过tt.onShow的query + showFrom 判断，showFrom=0 表示是从后台切回来，不需要发卡，showFrom=10表示点击小游戏入口如组队玩按钮、点击分享卡片等打开，需要发卡

```typescript
tt.onShow((res) => {
    console.log('onShow参数',  res)
    if (res.query._team_action == "create" ) {
        if (res.showFrom === 10) {
            console.log('热启进入， 需要发卡')
        } else if (res.showFrom === 0) {
            console.log('前后台切换，不需要发卡')
        }
    }
})
```

**Q10：怎么测试热启进入发起组队卡的场景？**
A: 联系运营给测试机配置实验打开组队玩面板的游戏入口。开启[调试彩蛋页](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/game-debug/bonus-scene)，配置点击所有入口都进入测试版本的游戏。上传测试版本后，从其他入口冷启进入游戏，点右上角关闭后，打开群聊界面的组队玩专区，点击组队玩按钮，则是热启进入发起组队卡的场景

tt.onShow((res) => {
console.log('onShow参数',  res)
if (res.query._team_action == "create" ) {
if (res.showFrom === 10) {
console.log('热启进入， 需要发卡')
} elseif (res.showFrom === 0) {
console.log('前后台切换，不需要发卡')
}
})

tt.shareAppMessage({
channel: "team_up", //识别发卡场景，传team_up或者invite
query: "roomId=xxx&key2=val2", // 一般需要带上一些房间id之类的字段，由开发者自行定义实现
extra: {
activityID: "6800*****",     // 从服务端createActivityID获取
templateInfo: [
{
name: "memberCount",
value: "1"// 初始人数
},
{
name: "roomLimit",
value: "4"// 房间人数上限
},
{
name: "users",              value: '[\"grtmlx2dqcmTO7C\"]'// 当前房间内的用户OpenID，为空则传[]
}
],
versionType: "current"    // 指定通过动态消息进入的小游戏版本：线上版current、测试版latest
},
success() {
console.log("分享成功");
// 可在此处上报分享成功事件
},
fail(e) {
console.log("分享失败");
},
});

特别地，如果需要根据聊天类型(群聊或者私聊)创建不同的组队房间，则可以从query中额外获取 `_chat_type`，其值 1 为 私聊，2 为 群聊。获取方式同上述 `_team_action`。

- **多人组队游戏**：如 MOBA、FPS 或“开黑”类游戏，房主创建房间后分享到好友群，群友可看到实时人数变化和游戏状态变化（组队中或者已开始）。
- **社交棋牌游戏**：创建棋牌室后邀请牌友，卡片标题显示“好友已就位，就等你补位！”，吸引好友快速加入。
- **限时活动邀请**：如“今晚 8 点 Boss 挑战，仅限 10 人”，通过动态消息实时更新剩余名额，营造紧迫感。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/de71c1832b8d44f1b2d345883a7f5341~tplv-9nona0m7ha-image.image)

curl --location 'https://minigame.zijieapi.com/mgplatform/api/apps/share/update_dynamic_message' \
--header 'access-token: 08011218462b4b54307662766c3150454833752b353739513d3d' \
--header 'Content-Type: application/json' \
--data '{
"access_token": "08011218462b4b54307662766c3150454833752b353739513d3d",
"activity_id": "562176002",
"target_state": 0,
"card_version": 1,
"query": "?room_id=48796951",
"version_type": "",
"template_info": [
{
"name": "memberCount",
"value": "2"
},
{
"name": "roomLimit",
"value": "3"
},
{            "name": "users",            "value": "[\"abc\",\"abc\"]"        }
]
}
'

// 在游戏启动时
launchOptions = tt.getLaunchOptionsSync();
console.log("游戏启动参数:", launchOptions);

if (launchOptions.query && launchOptions.query._team_action == "create") {
console.log(`一键组队场景`);
// 执行创建房间的逻辑...
createRoom(roomId);
}

“分享组队”是小游戏提供的一种高级社交分享能力。它允许开发者创建一种可动态更新状态的“动态消息”卡片，支持用户通过抖音私信(IM) 私聊或群聊场景快速邀请好友组队进入游戏。

**注意**：
- `activity_id` 是后续所有操作（客户端分享、服务端更新）的凭证，请务必妥善保存。
- 活动到期后（默认 24 小时），分享卡片将自动变为“已结束”状态，且无法再被更新。

注意：
- `activity_id` 是后续所有操作（客户端分享、服务端更新）的凭证，请务必妥善保存。
- 活动到期后（默认 24 小时），分享卡片将自动变为“已结束”状态，且无法再被更新。
- 如果上一次发卡已经创建过了`activity_id`，且与上一次是同一个组队房间，则请勿重复创建`activity_id`

一句话介绍：“分享组队”是小游戏提供的一种高级社交分享能力。它允许开发者创建一种可动态更新状态的“动态消息”卡片，支持用户通过抖音私信(IM) 私聊或群聊场景快速邀请好友组队进入游戏。

const launchOptions = tt.getLaunchOptionsSync();
console.log("游戏启动参数:", launchOptions);

if (launchOptions.query) {
const activityID = launchOptions.query.activity_id;
const roomID = launchOptions.query.room_id;
console.log(`通过分享卡片进入，activityID为: ${activityID}，roomID为: ${roomID}`);

// 执行加入房间的逻辑...
joinRoom(roomId);
}

tt.shareAppMessage({
templateId: "", // 替换成通过审核的分享ID
query: "key1=val1&key2=val2", // 使用路径
extra: {
useTeamInvitationStyle: true,    // 标识该消息为组队消息
activityID: "6800*****",     // 从服务端createActivityID获取
templateInfo: [
{
name: "memberCount",
value: "1"// 初始人数
},
{
name: "roomLimit",
value: "4"// 房间上限
}
],
versionType: "current"    // 指定通过动态消息进入的小游戏版本：线上版current、测试版latest
},
success() {
console.log("分享成功");
// 可在此处上报分享成功事件
},
fail(e) {
console.log("分享失败");
},
});

// 引入包 go get github.com/bytedance/douyin-openapi-sdk-go
import (
"fmt"
"testing"
credential "github.com/bytedance/douyin-openapi-credential-go/client"
openApiSdkClient "github.com/bytedance/douyin-openapi-sdk-go/client"
)
func TestShareCreateActivityId(t *testing.T) {
// 初始化SDK client
opt := new(credential.Config).
SetClientKey("tt******").    // 改成自己的app_id
SetClientSecret("cbs***") // 改成自己的secret
sdkClient, err := openApiSdkClient.NewClient(opt)
if err != nil {
t.Log("sdk init err:", err)
return
}

/* 构建请求参数，该代码示例中只给出部分参数，请用户根据需要自行构建参数值
token:
1.若用户自行维护token,将用户维护的token赋值给该参数即可
2.SDK包中有获取token的函数，请根据接口path在《OpenAPI SDK 总览》文档中查找获取token函数的名字
在使用过程中，请注意token互刷问题
header:
sdk中默认填充content-type请求头，若不需要填充除content-type之外的请求头，删除该参数即可
*/
sdkRequest := &openApiSdkClient.ShareCreateActivityIdRequest{}
sdkRequest.SetAccessToken("k23cd*****")
// sdk调用
sdkResponse, err := sdkClient.ShareCreateActivityId(sdkRequest)
if err != nil {
t.Log("sdk call err:", err)
return
}
t.Log(sdkResponse)
}

// 在游戏启动时或 onShow 回调中
const launchOptions = tt.getLaunchOptionsSync();
console.log("游戏启动参数:", launchOptions);

if (launchOptions.query && launchOptions.query.room_id) {
const roomId = launchOptions.query.room_id;
console.log(`通过分享卡片进入，房间号为: ${roomId}`);

// 执行加入房间的逻辑...
joinRoom(roomId);
}
