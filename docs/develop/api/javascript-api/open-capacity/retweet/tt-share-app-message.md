---
title: "tt.shareAppMessage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/retweet/tt-share-app-message
update_time: 2025-11-18
---

> 基础库 1.0.0 开始支持本方法，这是一个异步方法。
本API为主动调用转发相关方法（游戏内主动拉起发布器、好友邀请、录屏分享等）；被动分享（用户点击右上角更多面板内的分享按钮）时指定分享内容详见[tt.onShareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-on-share-app-message)。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 参数 options 是一个 [ShareParam](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param) 对象分享图片取自「开发者后台-运营能力-必接能力-分享配置」的配置图片，若无该配置，平台将使用兜底图片替代生成的分享链接有效期为 45 天，过期后链接失效报错返回 'get shareInfo return null' 时为获取分享信息失败，可能为获取分享信息时网络请求超时，或者是当前 appID 的分享状态异常，比如被封禁导致，可以检查站内信或通过运营群进行反馈（接入指南 -[联系我们](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/contactus/feedbacks)） |
| 相关教程 | [内容转发分享](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/gain-user/retweet) |

### 语法

```js
tt.shareAppMessage(options)
```

### 参数说明
options 为 object 类型，属性详见 [ShareParam](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param)
### 回调成功
object 类型，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| data | array | 仅当入参 options 中 channel='invite' 时返回，包含邀请对象的用户名和用户头像。(当邀请多个好友或群聊时，目前仅会返回一个好友的信息，群聊的信息暂不支持返回) | 2.54.0 |

##### data 类型说明
object 类型，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| name | string | 分享对象的用户名 | 2.54.0 |
| icon | string | 分享对象的用户头像 | 2.54.0 |

### 回调失败
object 类型，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| errMsg | string | "shareAppMessage:fail" + 错误信息 | 1.0.0 |

#### 错误码

| errNo | errMsg | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| 21101 | permission denied,channel: %s |  | 1.0.0 |
| 21102 | can not be shared without clicking by user |  | 1.0.0 |
| 21103 | file not exist path:%s |  | 1.0.0 |
| 21104 | file not readable path:%s |  | 1.0.0 |
| 21105 | video file is too short path:%s |  | 1.0.0 |
| 10200 | auth deny |  | 1.0.0 |
| 21107 | stickerId and cutTemplateId are mutually exclusive |  | 1.0.0 |
| 21108 | stickerId unavailable %s |  | 1.0.0 |
| 21109 | cutTemplateId unavailable %s |  | 1.0.0 |
| 21110 | use cut template fail |  | 1.0.0 |
| 21111 | share permission denied |  | 1.0.0 |
| 21112 | share image feature not support |  | 1.0.0 |
| 10403 | onBusinessError unknown biz error | 小游戏框架内部错误，有需要请[创建工单](https://developer.open-douyin.com/work-order-page?tab=workOrderRecord)咨询 | 1.0.0 |
| 20001 | invalid param | 参数错误 | 1.0.0 |
| 10401 | Invalid CommonInfo. | 小游戏框架内部错误，有需要请[创建工单](https://developer.open-douyin.com/work-order-page?tab=workOrderRecord)咨询 | 1.0.0 |
| 10301 | feature is not supported in app |  | 1.0.0 |
| 10401 | Internal error: show board error / Share error | 小游戏框架内部错误，有需要请[创建工单](https://developer.open-douyin.com/work-order-page?tab=workOrderRecord)咨询 | 1.0.0 |
| 10502 | cancel |  | 1.0.0 |
| 20000 | not support channel:video |  | 1.0.0 |
| 20000 | not support channel:picture |  | 1.0.0 |
| 20001 | should not pass in useTmeaInvitationStyle and shareImagePath together |  | 1.0.0 |
| 20001 | TaskGameId Not Found |  | 1.0.0 |
| 10103 | network unavailable |  | 1.0.0 |

### 代码示例
【示例一】使用审核通过的分享素材

```js
tt.shareAppMessage({
  templateId: "", // 替换成通过审核的分享ID
  query: "",
  success() {
    console.log("分享成功");
  },
  fail(e) {
    console.log("分享失败");
  },
});
```

【示例二】邀请好友

```js
tt.shareAppMessage({
  channel: "invite", // 拉起邀请面板分享游戏好友
  templateId: "", // 替换成通过审核的分享ID
  query: "",
  success(res) {
    console.log("分享成功" + JSON.stringify(res));
  },
  fail(e) {
    console.log("分享失败");
  },
});
```

【示例三】组队分享

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

【示例四】视频分享

```js
// 视频分享
tt.shareAppMessage({
  channel: "video",
  query: "",
  templateId: "1fidnqkeari9dnd18o", // 替换成通过审核的分享ID
  title: "画家活下去",
  desc: "在这里爱上画画",
  extra: {
    videoTopics: ["画家活下去"],
  },
  success() {
    console.log("分享视频成功");
  },
  fail(e) {
    console.log("分享视频失败");
  },
});
```

【示例五】录屏分享

```js
// 视频分享
tt.shareAppMessage({
  channel: "video",
  query: "",
  templateId: "1fidnqkeari9dnd18o", // 替换成通过审核的分享ID
  title: "画家活下去",
  desc: "在这里爱上画画",
  extra: {
    videoPath: "ttfile://temp/test.mp4", // 可用录屏得到的本地文件路径
    videoTopics: ["画家活下去"],
  },
  success() {
    console.log("分享视频成功");
  },
  fail(e) {
    console.log("分享视频失败");
  },
});
```

tt.shareAppMessage({
templateId: "", // 替换成通过审核的分享ID
title: "测试分享",
desc: "测试描述",
query: "",
success() {
console.log("分享视频成功");
},
fail(e) {
console.log("分享视频失败");
},
});

tt.shareAppMessage({
title: "测试分享",
desc: "测试描述",
query: "",
success() {
console.log("分享成功");
},
fail(e) {
console.log("分享失败");
},
});

#### 语法

```js
tt.shareAppMessage(title, desc, extra, channel, query, templateId)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
主动调用转发相关方法（拉起发布器、好友邀请、录屏分享等）

#### 示例代码
## 【示例一】使用审核通过的分享素材
```js
tt.shareAppMessage({
  templateId: "", // 替换成通过审核的分享ID
  query: "",
  success() {
    console.log("分享成功");
  },
  fail(e) {
    console.log("分享失败");
  },
});
```

【示例二】代码指定分享内容（图片、标题、描述）

```js
tt.shareAppMessage({
  title: "测试分享",
  desc: "测试描述",
  query: "",
  success() {
    console.log("分享成功");
  },
  fail(e) {
    console.log("分享失败");
  },
});
```
## 【示例三】同时使用模板 templateId 和 分享内容
```js
tt.shareAppMessage({
  templateId: "", // 替换成通过审核的分享ID
  title: "测试分享",
  desc: "测试描述",
  query: "",
  success() {
    console.log("分享视频成功");
  },
  fail(e) {
    console.log("分享视频失败");
  },
});
```

【示例四】邀请好友

```js
tt.shareAppMessage({
  channel: "invite", // 拉起邀请面板分享游戏好友
  title: "测试分享",
  desc: "测试描述",
  query: "",
  success(res) {
    console.log("分享成功" + JSON.stringify(res));
  },
  fail(e) {
    console.log("分享失败");
  },
});
```

【示例五】口令分享

```js
tt.shareAppMessage({
  channel: "token",
  title: "测试分享口令",
  desc: "测试描述",
  templateId: "", // 替换成通过审核的分享ID
  query: "",
  success() {
    console.log("分享成功");
  },
  fail(e) {
    console.log("分享失败");
  },
});
```

#### 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| title | string | 否 |  | 1.0.0 | 转发标题，不传则默认使用后台配置或当前小游戏的名称 |
| desc | string | 否 |  | 1.0.0 | 分享文案，不传则默认使用后台配置内容或游戏简介 |
| extra | Object | 否 |  | 1.0.0 | 附加信息（仅 channel == video \| picture 时生效）  **对象字段** - **videoTag**（string）：channel = video 时可以设置。分享视频的标签，可以结合获取[抖音视频排行榜](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/-open/function-get-video-list)使用 - **withVideoId**（boolean）：channel = video 时可以设置。是否支持跳转到播放页，以及支持获取视频信息等接口 （为 true 时会在 success 回调中带上 videoId） - **videoPath**（string）：channel = video 时可以设置。视频地址 ，分享一个本地视频。如果 videoPath 不传入会拉起摄像头拍摄界面 - **videoTopics**（Array<string>）：channel = video 时可以设置。视频话题(**仅抖音支持**) ，目前由 hashtag_list 代替  **即将废弃**，为保证兼容性，建议同时设置hashtag_list - **hashtag_list**（Array<string>）：channel = video \| picture 时可以设置。视频话题，字符串中间包含空格会取第一个空格前内容作为话题(**仅抖音支持**) - **defaultBgm**（string）：channel = video 时可以设置。抖音 pgc 音乐的短链(**仅抖音支持，需要基础库版本大于 1.90**) 。形如[https://v.douyin.com/JmcxWo8/](https://v.douyin.com/JmcxWo8/%EF%BC%8C)[，](https://v.douyin.com/JmcxWo8/%EF%BC%8C) 参考 [抖音小游戏录屏带配乐能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/gain-user/record-with-bgm) - **cutTemplateId**（string）：channel = video 时可以设置。抖音上可用的剪映模板 ID， 参考 [录屏添加剪映视频模板能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/gain-user/capcut-with-game) - **picturePath**（Array<string>）：**channel = picture时，本参数必传**。发布的图片地址，仅支持本地图片路径（即游戏包内路径和ttfile://路径） - **contentTitle**（string）：channel = picture 时可以设置。作品标题  ![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/output-203160501465242.66.png) - **contentDescription**（string）：channel = picture 时可以设置。作品描述信息 - **createChallenge**（boolean）：channel = video 时可以设置。是否分享为挑战视频 ( 仅头条支持 ) - **video_title**（string）：channel = video 时可以设置。生成输入的默认文案 - **abortWhenCutTemplateUnavailable**（boolean）：channel = video 时可以设置。剪映模板不可用或者剪映模板 ID 无效的时候是否直接回调失败 |
| channel | string | 否 |  | 1.0.0 | 转发内容类型  \|  \|  \|  \| \| --- \| --- \| --- \| \| 值 \| 说明 \| 支持环境 \| \| - \| 默认分享方式, channel 为空字符串或者不传 \| 通用 \| \| invite \| 拉起邀请面板分享游戏给好友 \| 仅抖音 20.6 及以上版本 \| \| video \| 发布视频内容 \| 通用 \| \| token \| 口令分享，生成一串特定的字符串文本 \| 仅头条 \| \| article \| 发布图文内容 \| 仅头条 \| \| picture \| 发布图文内容，内容由接口参数直接传入 \| 仅抖音、抖音极速版、抖音火山版 25.9 及以上版本 \| |
| query | string | 否 |  | 1.0.0 | 查询字符串，必须是 key1=val1&key2=val2 的格式。从这条转发消息进入后，可通过 [tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-get-launch-options-sync/) 或 [tt.onShow](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-on-show/) 获取启动参数中的 query 用来实现信息透传 |
| templateId | string | 否 |  | 1.0.0 | 分享素材模板 id，指定通过平台审核的 templateId 来选择分享内容，需在平台设置且通过审核。参考[拍摄视频并发布至抖音](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/open-capacity/operation/douyin_task) |

#### 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **data**（Array<Object>）：仅当入参 options 中 channel='invite' 时返回，包含邀请对象的用户名和用户头像。(当邀请多个好友或群聊时，目前仅会返回一个好友的信息，群聊的信息暂不支持返回) |

#### 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："shareAppMessage:fail" + 错误信息 |

#### 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21101 | permission denied,channel: %s |  |  |
| 21102 | can not be shared without clicking by user |  |  |
| 21103 | file not exist path:%s |  |  |
| 21104 | file not readable path:%s |  |  |
| 21105 | video file is too short path:%s |  |  |
| 10200 | auth deny |  |  |
| 21107 | stickerId and cutTemplateId are mutually exclusive |  |  |
| 21108 | stickerId unavailable %s |  |  |
| 21109 | cutTemplateId unavailable %s |  |  |
| 21110 | use cut template fail |  |  |
| 21111 | share permission denied |  |  |
| 21112 | share image feature not support |  |  |
| 10403 | onBusinessError unknown biz error |  |  |
| 20001 | invalid param |  |  |
| 10401 | Invalid CommonInfo. |  |  |
| 10301 | feature is not supported in app |  |  |
| 10401 | Internal error: show board error / Share error |  |  |
| 115900 | ** |  |  |
| 10502 | cancel |  |  |
| 20000 | not support channel:video |  |  |
| 20000 | not support channel:picture |  |  |
| 20001 | should not pass in useTmeaInvitationStyle and shareImagePath together |  |  |
| 20001 | TaskGameId Not Found |  |  |
| 10103 | network unavailable |  |  |

#### 注意事项
- 参数 options 是一个 [ShareParam](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param) 对象
- 分享图片取自「开发者后台-运营能力-必接能力-分享配置」的配置图片，若无该配置，平台将使用兜底图片替代
- 生成的分享链接有效期为 45 天，过期后链接失效
- 报错返回 'get shareInfo return null' 时为获取分享信息失败，可能为获取分享信息时网络请求超时，或者是当前 appID 的分享状态异常，比如被封禁导致，可以检查站内信或通过运营群进行反馈（接入指南 -[联系我们](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/contactus/feedbacks)）

#### 相关课程
[内容转发分享](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/gain-user/retweet)

#### 授权要求
无需开发者授权；无需用户授权

#### 支持平台
iOS、Android