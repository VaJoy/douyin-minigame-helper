---
title: "BannerAd.offLoad"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/banner-ad/banner-ad-off-load
update_time: 2024-09-19
---

## 语法

```js
BannerAd.offLoad(callback)
```
基础库 1.3.0 开始支持本方法，这是一个**同步**方法。
解除绑定 load 事件的监听器。

## 示例代码
```js
function loadCallback() {
  bannerAd.show().then(() => {
    console.log("广告显示成功");
  });
}

bannerAd.onLoad(loadCallback);

bannerAd.offLoad(loadCallback)
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.3.0 | 通过 [BannerAd.onLoad](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/banner-ad/banner-ad-on-load) 绑定的事件监听器 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
