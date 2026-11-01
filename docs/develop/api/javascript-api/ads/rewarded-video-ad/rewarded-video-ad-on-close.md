---
title: "RewardedVideoAd.onClose"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/rewarded-video-ad/rewarded-video-ad-on-close
update_time: 2024-07-24
---

## 语法

```js
RewardedVideoAd.onClose(callback)
```
基础库 1.3.0 开始支持本方法，这是一个**同步**方法。
绑定 close 事件的监听器。 当用户点击了 Video 广告上的关闭按钮时，会触发 close 事件的监听器。

## 示例代码
```js
const videoAd = tt.createRewardedVideoAd({
  adUnitId: "YOUR_UNIT",
  multiton: true,
  multitonRewardedMsg: "观看下一个可领取更多奖励",
});

function listener(res) {
  if (res.isEnded) {
    // do something
  }
  if (res.count) {
    //在支持多例模式的版本上会返回该字段，并且是否返回该字段与multiton是否为true无关
    //判断观看了几次广告
  }
}

videoAd.onClose(listener); //这里监听广告的close 事件
//.... do something
//不需要的时候
videoAd.offClose(listener);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.3.0 | close 事件的监听器  **对象字段** - **input**（Object）：object 类型 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 注意事项
count 和 isEnded 都能用于判断广告是否观看完成，在普通广告模式下，两个字段功能是重叠的。count 是新增加字段，值代表观看广告的次数，开发者能通过 count 来判断实际观看的次数。建议开发者在返回 count 的情况下，统一使用该字段判断广告是否观看完成。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
