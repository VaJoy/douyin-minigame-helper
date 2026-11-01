---
title: "RewardedVideoAd.onLoad"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/rewarded-video-ad/rewarded-video-ad-on-load
update_time: 2024-07-24
---

## 语法

```js
RewardedVideoAd.onLoad(callback)
```
基础库 1.3.0 开始支持本方法，这是一个**同步**方法。
绑定 load 事件的监听器。在手动调用 load 方法后，广告组件会预先加载，当广告组件成功拉取广告素材时会触发 load 事件。

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
| callback | Function | 是 |  | 1.3.0 | 监听 load 事件的回调函数，回调参数是一个空对象 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 注意事项
- 确保监听此事件后，开发者有主动调用 load 方法。
- 从最佳实践上来看，正确顺序需要监听 onLoad 事件后，再调用 load 方法。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
