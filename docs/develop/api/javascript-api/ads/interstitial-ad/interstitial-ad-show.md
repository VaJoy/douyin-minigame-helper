---
title: "InterstitialAd.show"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/interstitial-ad/interstitial-ad-show
update_time: 2024-09-19
---

基础库 1.71.0 开始支持本方法，这是一个**同步**方法。
显示插屏广告。

## 示例代码
```js
const ad = tt.createInterstitialAd({
  adUnitId: "YOUR_UNIT",
});
ad.load()
  .then(() => {
    ad.show().then(() => {
      console.log("插屏广告展示成功");
    });
  })
  .catch((err) => {
    console.log(err);
  });
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | Promise | Promise 对象 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 2005 | There is no Ad to show! |  |  |
| 2005 | An ad can only be displayed once! |  |  |
| 1003 | current activity is null, can not create game banner |  |  |
| 1003 | Please apply for an adUnitId |  |  |
| 1003 | can not create game banner |  |  |
| 1006 | The scene does not support advertising |  |  |
| 1001 | The adUnitId is empty |  |  |
| 1008 | The adUnitId is closed |  |  |
| 1007 | The adUnitId is prohibit |  |  |
| 1002 | The adUnitId is invalid |  |  |
| 20000 | internal error |  |  |
| 21000 | fail Video is playing, can't show now! |  |  |
| 21000 | This AD has already been shown. It needs to be destroyed and rebuilt |  |  |
| 1003 | show fail |  |  |
| 21000 | host app not supported |  |  |
| 21000 | ad not found |  |  |
| 21000 | unitid is illegal |  |  |
| 10301 | feature is not supported in app |  |  |
| 1003 | host app not supported |  |  |
| 1003 | The adUnitId is empty |  |  |
| 1003 | The adUnitId is invalid |  |  |
| 1003 | unknown ad type |  |  |
| 1003 | ad not found |  |  |
| 2006 | InterstitialAd has been destroyed |  |  |
| 2001 | Just started the %s, can't show now! |  |  |
| 2002 | Just shown an Ad, can't show now! |  |  |
| 21000 | The interstitial advertisement for current adUnitId hasn't completed loading. |  |  |

## 注意事项
出现no ad data的错误信息表示服务端无广告返回，通常是平台策略决定的。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
