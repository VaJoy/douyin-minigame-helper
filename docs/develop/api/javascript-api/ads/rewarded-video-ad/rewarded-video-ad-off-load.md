---
title: "RewardedVideoAd.offLoad"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/rewarded-video-ad/rewarded-video-ad-off-load
update_time: 2024-07-24
---

## 语法

```js
RewardedVideoAd.offLoad(callback)
```
基础库 1.3.0 开始支持本方法，这是一个**同步**方法。
解除[绑定 load 事件](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/rewarded-video-ad/rewarded-video-ad-on-load)的监听器。

## 示例代码
```js
const videoAd = tt.createRewardedVideoAd({
  adUnitId: "YOUR_UNIT",
});

function listener() {
  console.log('load emit')
}

videoAd.onLoad(listener); //这里监听广告的 load 事件

videoAd.load();

//不需要的时候
videoAd.offLoad(listener);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.3.0 | [load 事件](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/rewarded-video-ad/rewarded-video-ad-on-load)监听器 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
