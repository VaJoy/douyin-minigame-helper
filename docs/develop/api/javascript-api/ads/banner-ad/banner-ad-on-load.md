---
title: "BannerAd.onLoad"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/banner-ad/banner-ad-on-load
update_time: 2024-09-25
---

## 语法

```js
BannerAd.onLoad(callback)
```
基础库 1.3.0 开始支持本方法，这是一个**同步**方法。
绑定 load 事件的监听器。 广告组件成功拉取广告素材时会触发 load 事件的监听器。

## 示例代码
```js
bannerAd.onLoad(() => {
  bannerAd.show().then(() => {
    console.log("广告显示成功");
  });
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.3.0 | load 事件的监听器 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | /s |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
