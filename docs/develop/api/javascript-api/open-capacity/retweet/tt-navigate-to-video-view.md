---
title: "tt.navigateToVideoView"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/retweet/tt-navigate-to-video-view
update_time: 2025-08-22
---

> 基础库版本 1.40.0 开始支持本方法
跳转到分享的视频播放页面。
## 语法

```text
tt.navigateToVideoView(options)
```

## 参数说明
`options` 为 object 类型，属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| videoId | string | - | 是 | [tt.shareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-share-app-message/)分享视频成功后返回 | 1.40.0 |
| success | function |  | 否 | 接口调用成功回调函数 | 1.40.0 |
| fail | function |  | 否 | 接口调用失败回调函数 | 1.40.0 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） | 1.40.0 |

## 回调成功
Object 类型，属性如下：

| 参数 | 参数类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 跳转成功信息，恒为`'navigateToVideoView:ok'` |

## 回调失败
Object 类型， 属性如下：

| 参数 | 参数类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 跳转失败信息，以`'navigateToVideoView:fail'`开头 |
| errCode | number | 错误代码 |

errCode 的可枚举值：

| errCode | 描述 |
| --- | --- |
| 1001 | videoId 类型不正确 |
| 1002 | 视频已经被删除 |
| 1003 | videoId 不正确 |
| 1004 | 获取视频信息错误 |
| 1005 | 其他错误 |
| 1006 | 网络错误 |
| 1007 | 端上其他错误 |
| 1008 | 端上参数错误 |

## 扫码体验

![screenshot](data:image/png;base64,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)

## 代码示例
[开发者工具中预览](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/retweet/tt-navigate-to-video-view)

```js
tt.shareAppMessage({
  channel: "video",
  title: "测试分享视频",
  desc: "测试描述",
  templateId: "", // 替换成通过审核的分享ID
  query: "",
  extra: {
    videoPath: "ttfile://temp/test.mp4", // 可替换成录屏得到的视频地址
    videoTopics: ["话题1", "话题2"],
    withVideoId: true,
  },
  success(res) {
    console.log(res.videoId);
    console.log("分享视频成功");
  },
  fail(e) {
    console.log("分享视频失败");
  },
});

tt.navigateToVideoView({
  videoId: "xxxxxx",
  success: (res) => {
    console.log("done");
  },
  fail: (err) => {
    if (err.errCode === 1006) {
      tt.showToast({
        title: "something wrong with your network",
      });
    }
  },
});
```

## Bug & Tip
- Tip：在 IOS 下的横屏模式小游戏，目前不支持跳转
