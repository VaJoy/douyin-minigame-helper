---
title: "小游戏组队分享能力"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/retweet/minigameteamshare
update_time: 2025-03-28
---

## 动态消息
从客户端 30.9.0 开始，支持转发动态消息。动态消息对比普通消息，不同点是：
1. 消息发出去之后，开发者可以通过后台接口修改**部分**消息内容。
### 消息属性
动态消息有状态、文字内容、文字颜色。
### 状态
消息有两个状态，分别有其对应的文字内容和颜色。其中状态 0 可以转移到状态 0 和 1，状态 1 无法再转移。

| 状态 | 文字内容 | 允许转移的状态 |
| --- | --- | --- |
| 0 | "成员正在加入，当前 {memberCount}/{roomLimit} 人" | 0, 1 |
| 1 | "已开始" | 无 |

### 状态参数
每个状态转移的时候可以携带参数，具体参数说明如下。

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| memberCount | string | 状态 0 时有效，文字内容模板中 `memberCount` 的值 |
| roomLimit | string | 状态 0 时有效，文字内容模板中 `roomLimit` 的值 |
| query | string | 状态 1 时有效，点击「进入」启动小游戏时使用的路径。对于小游戏，没有页面的概念，可以用于传递查询字符串（query）  必须是 key1=val1&key2=val2 的格式。从这条转发消息进入后，可通过 [tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-get-launch-options-sync/) 或 [tt.onShow](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-on-show/) 获取启动参数中的 query 用来实现信息透传 |
| versionType | string | 状态 1 时有效，点击「进入」启动小游戏时使用的版本。有效参数值为：`current`(线上版), `latest`(开发版) |

## 使用方法
### 一、创建 activity_id
每条动态消息可以理解为一个活动，活动发起前需要通过 [createActivityID](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/dynamic-sharing/create-activity-id) 接口创建 `activity_id`。后续转发动态消息以及更新动态消息都需要传入这个 `activity_id`。
活动的默认有效期是 24 小时。活动结束后，未开始的消息内容会变成统一的样式：
- 文字内容：“已结束”
### 二、在转发之前声明消息类型为动态消息
通过调用 [tt.shareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-share-app-message) 接口，在`extra`中传入` useTeamInvitationStyle: true`，以及 `templateInfo`、`activityID` 参数。其中 `activityID` 从步骤一中获得。
##### extra
**channel 为空字符串/不传/invite** 时，可以通过 extra 设置以下附加信息：

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| useTeamInvitationStyle | boolean | false | 否 | 标识该消息为组队消息 |
| activityID | string |  | 否 | 组队消息 的唯一标识，通过[createActivityId](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/dynamic-sharing/create-activity-id)获取，`useTeamInvitationStyle` 为true时必填 |
| templateInfo | array |  | 否 | 组队消息 的模板信息，Array<[TemplateInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param#0d80faba)>类型，`useTeamInvitationStyle`为true时必填 |
| versionType | string | current | 否 | 指定通过动态消息进入的小游戏版本：线上版`current`、测试版`latest` |

**TemplateInfo类型说明 **
object 类型，属性如下：

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| name | string |  | 是 | 参数名，有效值：当前房间人数`memberCount`、房间人数上限`roomLimit` |
| value | string |  | 是 | 参数值 |

```js
tt.shareAppMessage({
  templateId: "", // 替换成通过审核的分享ID
  extra: {
      useTeamInvitationStyle: true,    // 标识该消息为组队消息
      activityID: "",     // 从步骤一获取
      templateInfo: [
          {
              name: "memberCount",
              value: "1"
          },
          {
              name: "roomLimit",
              value: "4"
          }
      ],
      versionType: "current"    // 指定通过动态消息进入的小游戏版本：线上版current、测试版latest
  },
  success() {
    console.log("分享成功");
  },
  fail(e) {
    console.log("分享失败");
  },
});
```

### 三、修改动态消息内容
动态消息发出去之后，可以通过 [updateDynamicMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/dynamic-sharing/update-dynamic-message) 修改消息内容。
## 低版本兼容
对于不支持动态消息的客户端版本，收到动态消息后会展示成普通消息
