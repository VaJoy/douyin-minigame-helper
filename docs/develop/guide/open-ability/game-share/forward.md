---
title: "转发"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/game-share/forward
update_time: 2025-04-14
---

用户在使用小游戏过程中，可转发消息给其他用户或群聊。

## 转发菜单
点击右上角“更多”按钮，会弹出菜单，菜单中的“分享”按钮默认展示。通过 [tt.showShareMenu()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-show-share-menu) 和 [tt.hideShareMenu()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-hide-share-menu) 可动态显示、隐藏“分享”按钮。

## 被动分享
点击右上角“更多”按钮，会弹出菜单，菜单中的“分享”按钮默认展示。通过 [tt.showShareMenu()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-show-share-menu) 和 [tt.hideShareMenu()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-hide-share-menu) 可动态显示、隐藏“分享”按钮。
如果你想要分享转发你的小游戏，请主动调用`tt.showShareMenu`：

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

## 
## 主动分享
游戏内可通过 [tt.shareAppMessage()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-share-app-message) 接口直接调起分享界面，与被动分享类似，可以自定义分享卡片内容。
### 使用审核通过的分享模板
可在开发者后台-运营能力-分享设置，管理可使用的分享素材模板。平台审核通过后，可在代码中通过`templateId`指定分享时使用的素材模板。

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

### 视频分享
当传入的 `channel` 为 `video` 时，会自动调起视频发布器。在 `extra` 中传入 `videoPath` ，可实现录屏分享。

```js
tt.shareAppMessage({
  title: "my title",
  channel: "video",
  extra: {
    videoTopics: ["test1 videoTopics", "test2 videoTopics"], // 抖音或头条小视频话题列表
    videoPath: "",
    withVideoId: true,
  },
  success(res) {
    tt.showModal({
      title: "分享成功",
      content: JSON.stringify(res),
    });
  },
  fail(e) {
    tt.showModal({
      title: "分享失败",
      content: JSON.stringify(e),
    });
  },
});
```
