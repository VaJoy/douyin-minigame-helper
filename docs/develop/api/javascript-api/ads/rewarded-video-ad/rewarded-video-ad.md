---
title: "RewardedVideoAd"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/rewarded-video-ad/rewarded-video-ad
update_time: 2025-11-14
---

全局唯一的视频广告实例，通过[tt.createRewardedVideoAd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/tt-create-rewarded-video-ad)来创建。
## 属性说明

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| show | Function | 展现广告 |
| load | Function | 加载广告 |
| destroy | Function | 销毁广告 |
| onLoad | Function | 监听加载事件 |
| offLoad | Function | 取消监听加载事件 |
| onError | Function | 监听错误事件 |
| offError | Function | 取消监听错误事件 |
| onClose | Function | 监听关闭事件 |
| offClose | Function | 取消监听关闭事件 |

## Bug & Tip
Tip：全局只能有一个视频广告实例，重复创建没有用。需要调用destroy 后再重新创建。
