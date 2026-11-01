---
title: "剪映模版"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/forward/capcut-guide
update_time: 2025-05-29
---

## 剪映模板
本文主要是介绍小游戏结合剪映模板能力的使用。具体接入可以参考 [录屏添加剪映视频模板能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/gain-user/capcut-with-game)
### 最低支持版本

| 系统 | 抖音版本 | 抖音极速版版本 | 基础库版本 |
| --- | --- | --- | --- |
| `Android` | `12.2` | `18.5.0` | `1.74.0` |
| `IOS` | `12.5` | `18.5.0` | `1.77.0` |

### 静默合成后分享
> 说明: 在传入 videoPath 的情况，可以直接对传入的视频进行处理后分享，调用后会直接合成应用了剪映模板的视频，用户可以直接发布，与现在录屏后分享视频流程一致。
#### 主动调用
主动调用是指通过 [tt.shareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-share-app-message) 调起视频分享，传入该方法的参数为 [ShareParam](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param) 类型。

```js
tt.shareAppMessage({
    ......
    channel: "video",
    extra: {
        ......
        cutTemplateId: "123456...",    //剪映模板ID，在后台配置获取
        videoPath: "xxx.mp3",   //视频地址，可以是本地已有视频路径或者是通过录屏得到
        withVideoId: true,   //使用剪映时，需要传入true
        abortWhenCutTemplateUnavailable: true,  //控制当传入的剪映模板 ID 无效的时候的行为。若是true，则剪映模板 ID 无效时会回调失败，false否则会走普通的分享流程。
    },
},
```

#### 被动调用
被动调用是指通过 [tt.onShareAppMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-on-share-app-message) 监听用户点击分享的行为，然后在回调函数中返回一个[ShareParam](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param)对象。

```js
tt.onShareAppMessage((res) => {
    return {
        ......
        extra: {
            ......
            cutTemplateId: "123456...",    //剪映模板ID，在后台配置获取
            videoPath: "xxx.mp4",   //视频地址，可以是本地已有视频路径或者是通过录屏得到
            withVideoId: true,   //使用剪映时，需要传入true
            abortWhenCutTemplateUnavailable: true,  //控制当传入的剪映模板 ID 无效的时候的行为。若是true，则剪映模板 ID 无效时会回调失败，false否则会走普通的分享流程。
        },
    };
});
```

### 通过剪映模板分享
#### 调用方式
**与 静默合成后分享** 中的主动调用和被动调用两种方式一样，开发者可以只传入 cutTemplateId 来直接跳转剪映模板详情页，不需要传入 videoPath (其他参数保持一致)。
### 常见问题
- **Q1：在通过剪映模板分享的方式中，不添加 videoPath 使用剪映模板未进入模板详情页，但回调 success 是为什么？**
  - A1：如下任一情况出现都出导致上述问题： 剪映模板不可用/剪映模板 ID 无效，调用 代码有问题，分享代码未在 extra 中设置 cutTemplateId。
- **Q2：剪映模板 ID 无效指的什么？**
  - A3：如下任一情况对应的都是剪映模板 ID 无效： 这个剪映模板 ID 没有对应的剪映模板。 该小程序无指定剪映模板 ID 的权限，该模板未在后台审核通过 ，未绑定到当前小程序上，参考说明文档 [说明文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/gain-user/capcut-with-game)
- **Q3: 为什么出现调用失败？**
  - 请并下载下方的专用制作包进行模板制作（注意不要开启软件自动更新，超过 7.0.0 版本的剪映包无法制作模板）
  - 确保模板素材数量与游戏内的视频素材数量一致
  - 视频时长需要大于模板的时长
### 剪映专用包
为避免在小游戏中出现模板调用不成功的情况，请下载剪映模板制作专用版 apk 进行模板创作和提交，**下载下方版本进行模板制作（商店下载的无法进行制作），电脑下载后发送到手机进行安装即可**

**推荐使用 （v6.9）：**

附件下载：[jianying.apk](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/88abd1c2c85545d4be09456fe2b30bcd)

**若上面制作失败，可尝试使用下面的版本（V 5.3）：**

附件下载：[剪映模版制作安卓 (1).apk](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4c6b0e5c752c468fa0062562aae330e9)

**Notice**：
1 、关闭软件自动更新，应用商店下载的版本无法发布制作模板
2 、请确保录屏时长大于剪映模板时长，否则会报错
3 、请确保素材数量一致，如“录屏内容”为 1 段视频，那么模板的原始素材也应为 1 段视频，当然你也可以通过官方api对视频进行裁切
### Bug&Tip
- Tips： 设置 abortWhenCutTemplateUnavailable 为 true 时，如果是静默合成，那么即使剪映模板不可用，也会继续进行分享，不会触发回调 fail 回调。
