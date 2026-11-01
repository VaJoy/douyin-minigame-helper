---
title: "BannerAd.show"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/banner-ad/banner-ad-show
update_time: 2024-09-25
---

基础库 1.3.0 开始支持本方法，这是一个**同步**方法。
广告创建后默认是隐藏的，可以通过该方法显示广告。 该方法返回一个 Promise 对象。当广告组件正常获取素材时，该 Promise 对象会是一个 resolved Promise。当广告组件发生错误时，会是一个 rejected Promise，参数与 [error 事件监听器](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/banner-ad/banner-ad-on-error)获得的参数相同。

## 示例代码
```js
const bannerAd = tt.createBannerAd({
  adUnitId: "xxxx",
});
bannerAd.onLoad(() => {
  bannerAd
    .show()
    .then(() => {
      console.log("广告显示成功");
    })
    .catch((err) => {
      console.log("广告组件出现问题", err);
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
| 2002 | Just shown an Ad, can't show now! |  |  |
| 10301 | feature is not supported in app |  |  |
| 21300 | context exception |  |  |
| 1003 | current activity is null, can not create game banner |  |  |
| 1003 | Please apply for an adUnitId |  |  |
| 1003 | can not create game banner |  |  |
| 1006 | The scene does not support advertising |  |  |
| 1001 | The adUnitId is empty |  |  |
| 1008 | The adUnitId is closed |  |  |
| 1007 | The adUnitId is prohibit |  |  |
| 1002 | The adUnitId is invalid |  |  |
| 20000 | internal error |  |  |
| 21000 | Just shown an Ad, can't show now! |  |  |
| 21101 | GridGamePanel with the same gridCount can show most one |  |  |
| 21000 | The banner advertisement has triggered fallback, but fallback ad has shown too many times today |  |  |
| 1003 | The banner advertisement for current adUnitId hasn't completed loading |  |  |
| 21000 | ad is not loaded, try call `show` in `onLoad` method |  |  |
| 21000 | ad not found |  |  |
| 21000 | unitid is illegal |  |  |
| 1003 | The banner advertisement for current adUnitId doesn't exist |  |  |
| 1003 | The adUnitId is empty |  |  |
| 1003 | The adUnitId is invalid |  |  |
| 1003 | unknown ad type |  |  |
| 21000 | type is illegal param |  |  |
| 21000 | app has enter background |  |  |

## 注意事项
必须调用 BannerAd.onLoad 监听广告素材成功拉取后才能调用 BannerAd.show，否则广告将无法及时展示

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
