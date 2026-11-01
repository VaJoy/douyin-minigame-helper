---
title: "分享逻辑"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/forward/logic
update_time: 2025-08-22
---

本文档会说明分享过程相关的主要逻辑，api 之间的调用关系。
## 名词解释
### ShareOption
`ShareOption` 是指系统调用开发者(通过 [tt.onShareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-on-share-app-message) )注册的回调时，传递给回调函数的参数，会包括 channel 字段。
### ShareParam
`ShareParam` 是指开发者最终传递给发布器的数据，可以根据约定传入部分自定义数据。具体字段可查阅[ShareParam](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param) 对象说明。
## 入口控制

- 可以通过 [tt.showShareMenu](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-show-share-menu) 和 [tt.hideShareMenu](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-hide-share-menu) 控制更多菜单中是否出现分享按钮。
- 开发者在开发小游戏时，可以在图形界面绘制自定义按钮，在按钮的回调中调用 [tt.shareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-share-app-message) 来直接调起发布器。

## 分享调用流程图
![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/other/1a0df84aa5bbbf50944d6dd279485cb2_image.png)
如上图所示，调用可大体分为主动调用（D）和被动调用（A、B、C）两种模式。小程序只能使用被动调用，小游戏可以使用主动和被动两种。
### 主动调用
主动调用是指 —— 开发者直接通过 ​`tt.shareAppMessage(shareParam)​` 方法，将 `shareParam` 传递给系统发布器即可。
### 被动调用
被动调用是指 —— 无论用户点击何种入口，小游戏框架均会将 `shareOption` 带给 ​`tt.onShareAppMessage(callback)`​ 方法中注册的 ​callback​ 回调。开发者可以在回调函数中根据接收的参数处理相应逻辑，最后返回 `shareParam` 即可。
## 分享效果预览
### 常规分享
默认分享方式, channel 为空字符串或者不传，即通过抖音的好友分享面板，分享成功后在 IM 聊天界面出现游戏卡片（仅支持抖音、抖 lite、抖音火山、头条、头 lite）
![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/WechatIMG954-3268771818437772.5.jpeg)
### 社交好友邀请（channel == invite）
仅支持抖音 & 抖 lite，20.6.0 版本可正常调用
channel 为 invite 时，可以在游戏内绘制按钮，触发后会拉起好友邀请面板，展示玩家的好友信息，用户可快捷进行分享，游戏内可以基于分享回调（success / cancel），给用户发放激励（如邀请好友有奖），被分享的用户会收到私信 IM 卡片及 app 内的 push 提醒
### ![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/WechatIMG953-1387500789302083.jpeg)
PS：后续该组件会持续优化，如“展示用户的在线状态”，不断提高该组件的分享率，建议游戏可以接入使用
### 录屏分享（channel == video）
仅支持抖音 & 抖 lite，开发者使用录屏分享时，如果未使用剪映模版和录屏配音(defaultBgm 字段) 能力时，将触发一键分享逻辑，将会弹出一键分享弹框，如下：
![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/WechatIMG955-2571750176842859.5.jpeg)
用户在点击一键分享后，将直接分享视频到宿主，完成分享能力。

- Tip：一键分享暂时只支持抖音安卓端。

## 分享说明
### title & desc 抖音端展示效果说明
```js
tt.shareAppMessage({
title: "这是设置的tittle",
desc: "这小游戏还挺有意思，点击就能玩",
imageUrl: "",
query: "",
success() {
console.log("分享成功");
},
fail(e) {
console.log("分享失败");
},
});
```
以上面代码为例，在抖音端，`title` 和 `desc` 的展现效果如下。
![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/image-9028908067856858.png)
分享文案为代码中的 `desc` 或者 后台模版配置中的**分享文案。**

- Tips: 关于后台模板配置，可见[小游戏内容转发分享](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/gain-user/retweet)。
- Tips: 同时使用代码和模板时，优先级为：代码指定分享内容 > 后台模板配置。
