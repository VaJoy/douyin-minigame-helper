---
title: "BannerAd.offError"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/banner-ad/banner-ad-off-error
update_time: 2024-09-19
---

## 语法

```js
BannerAd.offError(callback)
```
基础库 1.3.0 开始支持本方法，这是一个**同步**方法。
解除绑定 error 事件的监听器。

## 示例代码
```js
function errorCb({ errorCode, errMsg }) {
   console.log(errorCode, errMsg)
}

bannerAd.onError(errorCb);

bannerAd.offError(errorCb);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.3.0 | 通过 [Banner.onError](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/banner-ad/banner-ad-on-error) 绑定的监听器 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | /s |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
