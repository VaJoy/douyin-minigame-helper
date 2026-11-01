---
title: "调起方法"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/video-camera/request-method
update_time: 2025-08-22
---

## 名词解释
1. shareOption——系统调用开发者注册的回调时，传递给回调的数据，包括用户选择的调起方式等
1. shareParam——开发者最终传递给发布器的数据，可以根据约定传入部分自定义数据
## 入口控制
1.如果显示定义了 [Page|tt].onShareAppMessage(callback) 方法，在小程序右上角胶囊按钮里会自动带上「分享」「发头条」等入口。其中小程序里的方法注册在 Page 上，小游戏直接挂在 tt 上
1. 无论是否显示定义上述方法，均可以通过 tt.showShareMenu() 和 tt.hideShareMenu() 控制入口的显示与隐藏。
1. 开发者在开发小程序时，还可以在 TTML/TTML 文件里通过 button 组件自定义入口。其中通过 data-channel 字段指定调起方式（默认为「分享」），如：

```text
<button class="custom-share-button" open-type="share" data-channel="video" data-qrcode="inv34+23==">Click Me!</button>
```

1. 开发者在开发小游戏时，可以在图形界面绘制自定义按钮，在按钮的回调中调用 tt.shareAppMessage(shareParam) 来直接调起发布器。
## 调用逻辑

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/other/1a0df84aa5bbbf50944d6dd279485cb2_image.png)

如上图所示，调用可大体分为主动调用（D）和被动调用（A、B、C）两种模式。小程序只能使用被动调用，小游戏可以使用主动和被动两种。
## 主动调用
开发者直接通过 tt.shareAppMessage(shareParam) 方法，将 shareParam 传递给系统发布器即可。
## 被动调用
无论用户点击何种入口，小程序框架均会将 shareOption 带给 [Page|tt].onShareAppMessage(callback) 方法中注册的 callback 回调。开发者可以在回调中根据参数处理相应逻辑，最后返回 shareParam 即可。如：

```js
Page({
  onShareAppMessage(function (shareOption) {
    switch(shareOption.channel){
      case 'video':
        return {
          extra: {
            videoPath : shareOption.target.dataset.path
          }
        };
        break;
      case 'qrcode':
        ...
        break;
      default:
        ...
        break;
    }
  }),
});
```

其中，shareOption 的结构如下：

```js
{
  from: '',     // 合法值包括 button 和 menu，分别对应两种被动分享方式
  target: null, // 当from=button时，target指向button对象，当from=menu时，target为null
  channel: '',  // 预设的分享方式（通过button分享时，取值自data-channel）
}
```

shareParam 说明
一个典型的 shareParam 的形式如下，大体上分为基础参数和扩展参数 extra 两部分：

```js
{
  channel: '',
  title: '',
  path: '',
  extra: {
    videoPath: ''
  }
}
```

## 基础参数说明
所有的分享/发布内容都需要经过独立的审核后才会放出。
开发者可以在开放平台后台预先设置好一些分享默认内容，当实际代码所指定的内容审核通过前，会展示该默认内容。

| 姓名 | 说明 |
| --- | --- |
| channel | 指定发布器的调用方式，默认为 share。具体内容见下方「特殊参数说明」 |
| title | 想要分享/发布的内容标题。 |
| query/path | 分享/发布的内容会自动与小程序绑定，同时在 UI 上提供进入小程序的入口。开发者如果想为该入口添加参数可以通过设置 query/path 实现。其中小程序需要传递 path 字段，小游戏是 query 字段。 |

## 扩展参数 extra 说明

| 功能描述 | channel | 支持的 app | 基础参数说明 | extra 参数说明 |
| --- | --- | --- | --- | --- |
| 分享面板 | share | 今日头条抖音 | 无 | 无 |
| 发布图文内容 | article | 今日头条 | 无 | 无 |
| 发布视频内容 | video | 今日头条 | 1如果无需指定 videoPath 时请勿为该参数赋值，否则会导致进入错误的发布器页面 | 可以指定一个本地视频直接进入编辑页面 videoPath（类型是 string） |
| 发布视频内容 | video | 抖音 | title 参数在发布过程中对用户透明，经审核后可放出 | 1. 话题列表 videoTopics（类型是 string[]) 2. 可以指定一个本地视频直接进入编辑页面 videoPath（类型是 string） |
