---
title: "RewardedVideoAd.show"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/rewarded-video-ad/rewarded-video-ad-show
update_time: 2024-07-24
---

基础库 1.3.0 开始支持本方法，这是一个**同步**方法。
广告创建后默认是隐藏的，可以通过该方法显示广告。 该方法返回一个 Promise 对象。当广告组件正常获取素材时，该 Promise 对象会是一个 resolved Promise。当广告组件发生错误时，会是一个 rejected Promise，参数与 [error 事件监听器](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/rewarded-video-ad/rewarded-video-ad-on-error)获得的参数相同。

## 示例代码
```js
const videoAd = tt.createRewardedVideoAd();

videoAd.show().then(() => {
  console.log("视频广告展示");
});
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | Promise | 一个 Promise 对象 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 1003 | incentive card show now |  |  |
| 1003 | Video Ad show now |  |  |
| 1003 | current activity is null, can not create game banner |  |  |
| 1003 | Please apply for an adUnitId |  |  |
| 1003 | can not create game banner |  |  |
| 1006 | The scene does not support advertising |  |  |
| 1001 | The adUnitId is empty |  |  |
| 1008 | The adUnitId is closed |  |  |
| 1007 | The adUnitId is prohibit |  |  |
| 21000 | The adUnitId is invalid |  |  |
| 20000 | internal error |  |  |
| 21000 | ad not found |  |  |
| 10301 | feature is not supported in app |  |  |
| 1003 | The video advertisement for current adUnitId doesn't exist |  |  |
| 21000 | unitid is illegal |  |  |
| 1003 | The adUnitId is empty |  |  |
| 1003 | The adUnitId is invalid |  |  |
| 1003 | unknown ad type |  |  |
| 1002 | The adUnitId is invalid |  |  |
| 1003 | There is an Video playing now |  |  |
| 1003 | show fail |  |  |
| 1001 | operate type is invalid |  |  |
| 21000 | The video advertisement for current adUnitId hasn't completed loading. |  |  |
| 20000 | banner ad destroyed, adUnitId: ${this.#adUnitId} |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
