---
title: "好友邀请组件"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/gain-user/invite
update_time: 2025-09-01
---

支持抖音/抖 lite，20.6.0 版本可正常调用

您可以通过好友邀请组件引导用户进行好友分享，当 channel 为 invite 时，可以在游戏内绘制按钮，触发后会拉起好友邀请面板，展示玩家的好友信息，用户可快捷进行分享，游戏内可以基于分享回调（success / cancel），给用户发放激励（如邀请好友有奖），被分享的用户会收到私信 IM 卡片及 app 内的 push 提醒

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/WechatIMG953-7700881474632437.jpeg)

```js
tt.shareAppMessage({
  channel: "invite", // 好友邀请
  templateId: "1fidnqkeari9dnd18o", // 替换成通过审核的分享ID
  title: "画家活下去",
  desc: "在这里爱上画画",
  query: "",
  success() {
    console.log("分享成功")
  },
  fail(e) {
    console.log("分享失败")
  },
})
```

PS：后续该组件会持续优化，如“展示用户的在线状态”，不断提高该组件的分享率，建议游戏可以接入使用。
