---
title: "BannerAd.hide"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/banner-ad/banner-ad-hide
update_time: 2024-09-25
---

基础库 1.3.0 开始支持本方法，这是一个**同步**方法。
隐藏广告。

## 示例代码
```js
bannerAd.onLoad(() => {
  bannerAd.show().then(() => {
    console.log("广告显示成功");
    setTimeout(() => {
      bannerAd.hide();
      console.log("广告隐藏");
    }, 2000);
  });
});
```

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 1003 | internal error |  |  |
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
| 1003 | The banner advertisement for current adUnitId doesn't exist |  |  |
| 21000 | ad not found |  |  |
| 21000 | unitid is illegal |  |  |
| 1003 | The adUnitId is empty |  |  |
| 1003 | The adUnitId is invalid |  |  |
| 1003 | unknown ad type |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
