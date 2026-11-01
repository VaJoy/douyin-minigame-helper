---
title: "视频拍摄器"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/forward/video
update_time: 2025-07-16
---

本文主要是通过代码示例来说明如何调起视频发布器。
## 主动调用
主动调用是指通过 [tt.shareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-share-app-message) 调起视频发布器，传入该方法的参数为 [ShareParam](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param) 类型。

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

## 被动调用
被动调用是指通过 [tt.onShareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-on-share-app-message) 监听用户点击分享的行为，然后在回调函数中返回一个[ShareParam](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param)对象。

```js
tt.onShareAppMessage((res) => {
  console.log(res.channel); // 如果用户触发了视频发布器，channel值为"video"
  return {
    success: (res) => {
      console.log("分享视频成功");
    },
  };
});
```

> 被动调用时，不支持修改 ShareParam 的 channel 值。
## 设置视频话题
如果想在视频分享时加上一些话题，可以通过 `extra` 参数的 `hashtag_list` 字段设置：

```js
tt.shareAppMessage({
  title: "my title",
  channel: "video",
  extra: {
    hashtag_list: ["custom tag 1", "custom tag 2"],
  },
});
```

> 只有抖音拍视频支持话题设置功能。
> 只有抖音拍视频支持传 title。
## 获取视频封面图
如果将 `extra` 参数的 `withVideoId` 字段设置为 `true` ，可以获得 `videoId`。

```js
tt.shareAppMessage({
  extra: {
    withVideoId: true,
  },
  success: (res) => {
    console.log(res.videoId);
  },
});
```

## 视频分享成功后跳转到视频播放页
获得 `videoId` 后，可用于 [tt.navigateToVideoView](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-navigate-to-video-view) 方法，跳转到视频播放页。

```js
tt.navigateToVideoView({
  videoId: res.videoId,
  fail: (res) => {
    console.log(res);
    // 可根据 res.errCode 处理失败case
  },
});
```

> 当完成拍视频得到 videoId 后如果立即跳转播放页，因为服务端延迟一般是会失败的，建议先将 videoId 存到服务端，稍后再根据业务需要跳转播放页面。
## 录屏分享
可以将录屏得到的文件，进行分享。

```js
const recorder = tt.getGameRecorderManager();

recorder.onStop((res) => {
  console.log(res.videoPath);
  tt.shareAppMessage({
    title: "my title",
    channel: "video",
    extra: {
      videoPath: res.videoPath, //录屏后得到的文件地址
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
});

recorder.stop();
```

## Bug&Tip
- Tip: [分享报错 "can not be shared without clicking by user"](https://forum.microapp.bytedance.com/mini-game/posts/5fd71c34d1ce3f028545d1e3)
- Tip: 在抖音或其他 APP 中分享视频，可以在发布出去的视频中带上小游戏锚点（即左下角小游戏链接），但是需要保证当前小游戏已经发布存在线上版本，并且有在当前宿主上线，发布时选择默认发布，而非选择日常。发布完成后，可以使用其他账号（非发布视频账号）查看发布后视频，会带上锚点。因为系统策略原因，安卓和 IOS 建议分开查看。
