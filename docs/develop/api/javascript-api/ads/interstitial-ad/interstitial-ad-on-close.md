---
title: "InterstitialAd.onClose"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/interstitial-ad/interstitial-ad-on-close
update_time: 2024-09-19
---

## 语法

```js
InterstitialAd.onClose(callback)
```
基础库 1.71.0 开始支持本方法，这是一个**同步**方法。
监听插屏广告关闭事件。

## 示例代码
```js
interstitialAd.onClose(() => {
    console.log('插屏广告关闭')
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.71.0 | 监听器函数 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
