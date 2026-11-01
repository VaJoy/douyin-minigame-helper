---
title: "社交分享能力接入指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/social-interaction/social-share-guide
update_time: 2026-01-27
---

## 能力说明
小游戏“社交分享”是一项核心的开放能力，旨在帮助开发者利用抖音平台的社交关系链，通过用户的分享行为将游戏内容以多种形式分享给好友或发布到抖音推荐流中，实现用户裂变增长。
**适用场景与效果**：

| **常规分享** | 玩家通过小游戏右上角更多菜单进行分享，支持分享给站内的抖音好友或群聊，站外的微信好友或朋友圈、QQ好友或空间、复制链接等多种分享形式。 |
| --- | --- |
| **普通IM分享** | 玩家可以通过抖音私信将游戏分享给指定好友或群聊。接收方会看到一个游戏卡片，点击即可直接启动游戏。这是最常用的社交裂变方式，尤其适用于“邀请好友得奖励”等活动。 |
| **组队IM分享** | “组队IM分享”是小游戏提供的一种高级社交分享能力。它允许开发者创建一种可动态更新状态的“动态消息”卡片，用于在抖音私信中邀请好友。与普通分享不同，这种卡片的内容（如队伍人数、房间状态）可以在用户分享后，由游戏服务端进行实时修改，非常适合需要多人协作、状态实时同步的游戏场景。 |
| **视频/录屏分享** | 玩家可以将自己的游戏过程录制下来，或使用游戏内的视频素材，发布为一条带有关联话题和游戏锚点（即小游戏启动链接）的抖音视频，吸引视频观众转化为游戏玩家。 |
| **图文分享** | 支持玩家将游戏内的图片（如精彩瞬间截图、成就海报等）配合文字和话题，发布为图文动态，提供更丰富的分享形式。 |
| **点对点私信** | 提供定向分享能力，支持玩家在游戏内向指定好友发起分享，建议结合抖音小游戏里的开放数据开发互动游戏。 |

## 接入流程简述

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/8ad1c60748b84722930328742c9b6e3a~tplv-9nona0m7ha-image.image)

- 被动分享是指无论用户点击何种入口，SDK均会将 `shareOption` 带给`tt.onShareAppMessage(callback)` 方法中注册的 callback 回调。开发者可以在回调函数中根据接收的参数处理相应逻辑，最后返回 `shareParam` 给到系统发布器。
- 主动分享是指开发者直接通过调用 `tt.shareAppMessage(shareParam)` 方法，将 `shareParam` 传递给系统发布器。
## 接入流程详情
### 分享配置（可选）
**一、获取分享素材 ID**
开发者可以提前通过开发者后台配置分享图片、标题、文案，并由平台进行审核。审核通过的素材会生成对应的 templateId，给到开发者调用。
审核通过的分享内容，在线上的转发行为依然会受平台监管，请开发者遵守运营规范相关要求。
获取路径：[开发者平台](https://microapp.bytedance.com/app/applist) -> 选择对应小游戏 -> 运营 ->运营能力 -> 分享设置 -> 新建分享 ->获取分享ID

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/70d7a9616de244d5ad70a488ad96ebc3~tplv-9nona0m7ha-image.image)

**二、分享内容定义**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/93c4872d33a5409b8bb0fb55f0908668~tplv-9nona0m7ha-image.image)

| 分享内容 | 字段 | 名称 | 使用建议 | 内容定义 | 最低版本 |
| --- | --- | --- | --- | --- | --- |
| 分享标题 | title | 分享标题 | 不超过 14 个中文字符 | 一句话介绍小游戏 |  |
| 分享文案 | desc | 分享文案 | 不超过 28 个中文字符 | 结合游戏特征、分享场景，以玩家口吻邀请好友加入游戏。 | 1.30.0.1 |

**三、各宿主建议长度**

| 字段 | 头条 | 抖音 |
| --- | --- | --- |
| title | 14 个汉字以内 | 8 个汉字以内 |
| desc | 28 个汉字以内 | 14 个汉字以内 |

**四、分享内容指定方式**
平台支持不同形式来指定转发的内容（图片、标题、文案），最终按照优先级规则进行选择
1. 代码指定分享内容（title、desc）
1. 代码指定审核通过的模板素材 templateId
**五、分享内容优先级**

| 场景 | 优先级 |
| --- | --- |
| 端内分享 | 代码指定 > 模板指定 > 平台默认 |
| 端外分享 | 模板指定 > 平台默认 |

### 常规分享
常规分享指玩家通过点击右上角“更多”按钮弹出菜单，点击菜单中的“分享”按钮进行的分享行为。
常规分享属于被动分享，一般情况不需要开发者调用，不过SDK提供了一些能力给开发者按需调整该能力：
- 通过 [tt.showShareMenu()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-show-share-menu) 和 [tt.hideShareMenu()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-hide-share-menu) 可动态显示、隐藏“分享”按钮。
- 通过 [tt.onShareAppMessage()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/retweet/tt-on-share-app-message) 和 [tt.offShareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/retweet/tt-off-share-app-message) 可监听、取消监听“分享”事件以修改用户的分享内容。
**tt.showShareMenu**
显示当前小游戏页面的转发按钮，转发按钮位于小游戏页面右上角的“更多”中。
调用示例：

```js
tt.showShareMenu({
  success(res) {
    console.log("已成功显示转发按钮");
  },
  fail(err) {
    console.log("showShareMenu 调用失败", err.errMsg);
  },
  complete(res) {
    console.log("showShareMenu 调用完成");
  },
});
```

**tt.hideShareMenu**
隐藏转发按钮。
调用示例：

```js
tt.hideShareMenu({
  success(res) {
    console.log("已成功隐藏转发按钮");
  },
  fail(err) {
    console.log("hideShareMenu 调用失败", err.errMsg);
  },
  complete(res) {
    console.log(`hideShareMenu 调用完成`);
  },
});
```

**tt.onShareAppMessage**
监听用户点击平台提供的分享入口时触发的事件（如右上角更多面板中的分享、排行榜中的分享），以指定用户的分享内容。
调用示例：

```js
tt.onShareAppMessage(function (res) {
  console.log(res.channel);
  // do something
  const shareData = {
    success() {
      console.log("分享成功");
    },
    fail(e) {
      console.log("分享失败", e);
    },
  };
  const r = Object.assign({ channel: res.channel }, shareData);
  //channel值无法修改，并会在调用tt.shareAppMessage时自动带上
  switch (res.channel) {
    case "video":
      r.extra = {
        videoTopics: ["test1 videoTopics", "test2 videoTopics"], // 抖音小视频话题列表
        videoPath: "videotest.mp4", // 如果为抖音或者头条小视频，可以直接传本地视频路径
        //以抖音为例，使用videoPath后，用户点击拍抖音时会去分享开发者指定的视频。
      };
      break;
    default:
        if (res.extra.position === "top") {    // 为用户点击右上角更多面板中的分享
            r.templateId = "",     // 替换为审核通过的templateId
        } else {    // 为用户点击游戏内平台拉起的分享，如排行榜中的分享
             r.templateId = "",     // 替换为审核通过的templateId
        }
      break；
  }
  return r;
});
```

**tt.offShareAppMessage**
取消监听用户点击右上角菜单的“分享”按钮时触发的事件。
调用示例：

```js
function onShareAppMessage(res) {
  console.log(res);
}
// 监听菜单按钮“转发”
tt.onShareAppMessage(onShareAppMessage);
// 取消监听菜单按钮“转发”
setTimeout(() => {
  tt.offShareAppMessage(onShareAppMessage);
}, 2000);
```

### 主动分享
支持`抖音/抖音极速版`当传入的 channel 为 invite 时，触发后会拉起好友邀请面板。
开发者在开发小游戏时，可以在游戏界面绘制自定义按钮，在按钮的回调中调用，直接调起对应的分享发布方式，开发者直接通过 `tt.shareAppMessage(shareParam)` 方法，将 `shareParam` 传递给系统发布器即可。
调用示例：

```js
tt.shareAppMessage(options)
```

#### 普通IM分享
分享小游戏卡片给抖音好友或群聊。
调用示例（指定channel=invite）：

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

#### 组队IM分享
分享小游戏卡片给抖音好友或群聊，邀请好友组队玩小游戏，可以通过游戏服务端动态修改卡片内容。
调用示例（channel=invite，指定useTeamInvitationStyle=true）：

```js
tt.shareAppMessage({
  channel: "invite",
  templateId: "", // 替换成通过审核的分享ID
  extra: {
      useTeamInvitationStyle: true,    // 标识该消息为组队消息
      activityID: "",     // 组队消息的唯一标识
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

#### 视频/录屏分享
录屏分享，开发者可以通过平台提供的接口实现自动/手动录屏，详见 [录屏与分享](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/gain-user/record-share/)，录屏结束后可把录屏视频发布到抖音推荐流，为小游戏带来更大流量。
调用示例（指定channel=video）：

```js
// 录屏分享
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

#### 图文分享
分享小游戏图片内容到图文社区，同时挂载上小游戏锚点支持观众点击直接启动小游戏。
调用示例（指定channel=picture）：

```js
tt.shareAppMessage({
  channel: "picture",
  query: "",
  extra: {
    picturePath: ["ttfile://temp/test.png"], 
    contentTitle: "作品标题",
    contentDescription: "作品描述信息"
  },
  success() {
    console.log("分享图文成功");
  },
  fail(e) {
    console.log("分享图文失败");
  },
});
```

#### 点对点私信
**tt.shareMessageToFriend**
给指定的好友分享游戏信息。
调用示例：

```js
let queryObj = {
    'key1': 'value1',
    'key2': 'value2',
};
tt.shareMessageToFriend({
    openId: 'xxxxx',
    templateId: 'xxxxxx',
    query: JSON.stringify(queryObj),
    success(res) {
        console.log('success');
    },
    fail(res) {
        console.log('fail', res);
    },
});
```

## 注意事项
- 端外分享不支持通过代码设置自定义分享内容。
- 如果需要获取视频信息或者跳转视频播放页，以及获取抖音视频排行榜时，需要填写 withVideoId 为 true。
- 头条拍视频不支持设置 title 。

tt.hideShareMenu({
success(res) {
console.log("已成功隐藏转发按钮");
},
fail(err) {
console.log("hideShareMenu 调用失败", err.errMsg);
},
complete(res) {
console.log(`hideShareMenu 调用完成`);
},
});

tt.shareAppMessage({
channel: "picture",
query: "",
extra: {
picturePath: ["ttfile://temp/test.png"],
contentTitle: "作品标题",
contentDescription: "作品描述信息"
},
success() {
console.log("分享图文成功");
},
fail(e) {
console.log("分享图文失败");
},
});

let queryObj = {
'key1': 'value1',
'key2': 'value2',
};
tt.shareMessageToFriend({
openId: 'xxxxx',
templateId: 'xxxxxx',
query: JSON.stringify(queryObj),
success(res) {
console.log('success');
},
fail(res) {
console.log('fail', res);
},
});

functiononShareAppMessage(res) {
console.log(res);
}
// 监听菜单按钮“转发”
tt.onShareAppMessage(onShareAppMessage);
// 取消监听菜单按钮“转发”
setTimeout(() => {
tt.offShareAppMessage(onShareAppMessage);
}, 2000);

tt.showShareMenu({
success(res) {
console.log("已成功显示转发按钮");
},
fail(err) {
console.log("showShareMenu 调用失败", err.errMsg);
},
complete(res) {
console.log("showShareMenu 调用完成");
},
});

tt.shareAppMessage(options)

tt.onShareAppMessage(function (res) {
console.log(res.channel);
// do something
const shareData = {
success() {
console.log("分享成功");
},
fail(e) {
console.log("分享失败", e);
},
};
const r = Object.assign({ channel: res.channel }, shareData);
//channel值无法修改，并会在调用tt.shareAppMessage时自动带上
switch (res.channel) {
case"video":
r.extra = {
videoTopics: ["test1 videoTopics", "test2 videoTopics"], // 抖音小视频话题列表
videoPath: "videotest.mp4", // 如果为抖音或者头条小视频，可以直接传本地视频路径
//以抖音为例，使用videoPath后，用户点击拍抖音时会去分享开发者指定的视频。
};
break;
default:
if (res.extra.position === "top") {    // 为用户点击右上角更多面板中的分享
r.templateId = "",     // 替换为审核通过的templateId
} else {    // 为用户点击游戏内平台拉起的分享，如排行榜中的分享
r.templateId = "",     // 替换为审核通过的templateId
}
break；
}
return r;
});

// 录屏分享
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

tt.shareAppMessage({
templateId: "", // 替换成通过审核的分享ID
extra: {
useTeamInvitationStyle: true,    // 标识该消息为组队消息
activityID: "",     // 组队消息的唯一标识，详见参数说明
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
