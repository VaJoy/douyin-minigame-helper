---
title: "InterstitialAd.onError"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/interstitial-ad/interstitial-ad-on-error
update_time: 2024-09-19
---

## 错误码详情

| 代码 | 异常情况 | 理由 |
| --- | --- | --- |
| 2001 | 触发频率限制 | 小程序启动一定时间内不允许展示插屏广告 |
| 2002 | 触发频率限制 | 距离小程序插屏广告或者激励视频广告上次播放时间间隔不足，不允许展示插屏广告 |
| 2003 | 触发频率限制 | 当前正在播放激励视频广告或者插屏广告，不允许再次展示插屏广告 |
| 2004 | 广告渲染失败 | 该项错误不是开发者的异常情况，或因小程序页面切换导致广告渲染失败 |
| 2005 | 广告调用异常 | 插屏广告实例不允许跨页面调用 |

##

## 语法

```js
InterstitialAd.onError(callback)
```
基础库 1.71.0 开始支持本方法，这是一个**同步**方法。
监听插屏错误事件。

## 示例代码
```js
interstitialAd.onError(({ errCode, errMsg }) => {
    console.log('监听到错误', errCode, errMsg)
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.71.0 | 监听器函数  **对象字段** - **data**（Object）：object类型，属性如下： |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
