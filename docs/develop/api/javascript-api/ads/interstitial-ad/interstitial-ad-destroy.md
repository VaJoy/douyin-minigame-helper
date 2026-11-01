---
title: "InterstitialAd.destroy"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/interstitial-ad/interstitial-ad-destroy
update_time: 2024-09-19
---

基础库 1.71.0 开始支持本方法，这是一个**同步**方法。
销毁插屏广告实例。

## 示例代码
```js
const ad = tt.createInterstitialAd({
  adUnitId: "YOUR_UNIT",
});
ad.load()
  .then(() => {
    ad.show().then(() => {
      console.log("插屏广告展示成功");

      ad.destroy();
    });
  })
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | Promise | Promise 对象 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 2005 | Can't destroy a NOT shown ad! |  |  |
| 1003 | current activity is null, can not create game banner |  |  |
| 1003 | Please apply for an adUnitId |  |  |
| 1003 | can not create game banner |  |  |
| 1006 | The scene does not support advertising |  |  |
| 1001 | The adUnitId is empty |  |  |
| 1008 | The adUnitId is closed |  |  |
| 1007 | The adUnitId is prohibit |  |  |
| 1002 | The adUnitId is invalid |  |  |
| 20000 | The adUnitId is closed |  |  |
| 10301 | feature is not supported in app |  |  |
| 1003 | host app not supported |  |  |
| 21000 | host app not supported |  |  |
| 1003 | The adUnitId is empty |  |  |
| 1003 | The adUnitId is invalid |  |  |
| 1003 | unknown ad type |  |  |
| 1003 | ad not found |  |  |
| 21000 | ad not found |  |  |
| 21000 | unitid is illegal |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
