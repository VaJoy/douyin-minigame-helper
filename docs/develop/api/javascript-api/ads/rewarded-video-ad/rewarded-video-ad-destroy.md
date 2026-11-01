---
title: "RewardedVideoAd.destroy"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/rewarded-video-ad/rewarded-video-ad-destroy
update_time: 2024-07-24
---

基础库 1.92.0 开始支持本方法，这是一个**同步**方法。
通过 destroy 方法主动销毁广告实例。该方法返回一个 Promise，如果广告已经销毁成功，调用该方法返回一个 resolved Promise；如果是频繁的销毁重建，确保在收到 Promise 保证后再次创建新的。

## 示例代码
```js
const videoAd = tt.createRewardedVideoAd();

videoAd
  .destroy()
  .then(() => {
    //这里再次创建其他adUnitId的广告实例
  })
  .catch((err) => {
    console.log("广告组件出现问题", err);
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
- 通过销毁上一个广告实例后，再次创建时传入新的 adUnitId，可以实现不同 adUnitId 的切换。
- 只要调用销毁，无论销毁成功或者失败，销毁时会自动移除广告对象上监听的所有 loaded，error，close 事件。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
