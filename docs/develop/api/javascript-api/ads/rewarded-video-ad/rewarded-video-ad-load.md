---
title: "RewardedVideoAd.load"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/rewarded-video-ad/rewarded-video-ad-load
update_time: 2024-07-24
---

基础库 1.3.0 开始支持本方法，这是一个**同步**方法。
通过 load 方法主动预加载广告内容。此外，在显示广告出现问题时也可以尝试主动 load 一次。 该方法返回一个 Promise，如果广告已经自动拉取成功，调用该方法返回一个 resolved Promise。

## 示例代码
```js
// 显示广告
const videoAd = tt.createRewardedVideoAd({
  adUnitId: "YOUR_UNIT_ID",
});

videoAd.onLoad(() => {
  console.log("广告加载完成");
});
videoAd.load();

videoAd
  .show()
  .then(() => {
    console.log("广告显示成功");
  })
  .catch((err) => {
    console.log("广告组件出现问题", err);
    // 可以手动加载一次
    videoAd.load().then(() => {
      console.log("手动加载成功");
      // 加载成功后需要再显示广告
      videoAd.show();
    });
  });
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | Promise | Promise 对象 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 1003 | current activity is null, can not create game banner |  |  |
| 1003 | Please apply for an adUnitId |  |  |
| 1003 | can not create game banner |  |  |
| 1006 | The scene does not support advertising |  |  |
| 1001 | The adUnitId is empty |  |  |
| 1008 | The adUnitId is closed |  |  |
| 1007 | The adUnitId is prohibit |  |  |
| 1002 | The adUnitId is invalid |  |  |
| 20000 | internal error |  |  |
| 21000 | ad not found |  |  |
| 21000 | unitid is illegal |  |  |
| 10301 | feature is not supported in app |  |  |
| 1003 | The video advertisement for current adUnitId doesn't exist |  |  |
| 1003 | The adUnitId is empty |  |  |
| 1003 | The adUnitId is invalid |  |  |
| 1003 | unknown ad type |  |  |

## 注意事项
- 为了提高广告内容的价值，建议开发者避免广告浪费，在调用 load 预加载后，保证每次预加载的广告会被展示
- 广告播放结束后不会自动加载下一个广告，需要预加载请开发者主动调用广告 load 方法，不过为了提高广告价值，尽量避免预加载

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
