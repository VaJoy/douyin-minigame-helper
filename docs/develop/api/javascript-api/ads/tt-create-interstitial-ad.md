---
title: "tt.createInterstitialAd"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/tt-create-interstitial-ad
update_time: 2024-07-24
---

## 语法

```js
tt.createInterstitialAd(params)
```
基础库 1.71.0 开始支持本方法，这是一个**同步**方法。
创建插屏广告，开发者可以在小游戏中使用插屏广告获得收入。插屏广告是由客户端原生渲染，由开发者控制广告组件的显示。该能力支持竖屏版和横屏版小游戏。

## 示例代码
```js
const ad = tt.createInterstitialAd({
  adUnitId: "YOUR_UNIT",
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| params | Object | 是 |  | 1.71.0 | object 类型，属性如下：  **对象字段** - **adUnitId**（string）：广告单元 id |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| InterstitialAdInstance | Object | [InterstitialAd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/interstitial-ad/interstitial-ad)实例。 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 10301 | feature is not supported in app |  |  |
| 21300 | context exception |  |  |
| 1003 | internal error |  |  |
| 1003 | current activity is null, can not create game banner |  |  |
| 1003 | Please apply for an adUnitId |  |  |
| 1003 | can not create game banner |  |  |
| 1006 | The scene does not support advertising |  |  |
| 1001 | The adUnitId is empty |  |  |
| 1008 | The adUnitId is closed |  |  |
| 1007 | The adUnitId is prohibit |  |  |
| 1002 | The adUnitId is invalid |  |  |
| 1003 | Create repeated |  |  |
| 1003 | A usable ad already exists |  |  |
| 20000 | internal error |  |  |
| 21000 | host app not supported |  |  |
| 21000 | ad not found |  |  |
| 21000 | unitid is illegal |  |  |
| 1003 | host app not supported |  |  |
| 1003 | The adUnitId is empty |  |  |
| 1003 | The adUnitId is invalid |  |  |
| 1003 | unknown ad type |  |  |
| 1003 | ad not found |  |  |
| 1000 | request ad failed @1 |  |  |
| 1000 | request ad failed @2 |  |  |
| 1000 | request ad failed @3 |  |  |
| 1000 | request ad failed @4 |  |  |
| 1000 | request ad failed @7 |  |  |
| 1003 | request ad failed @5 |  |  |
| 1003 | request ad failed @6 |  |  |
| 1003 | request ad failed @8 |  |  |
| 1003 | request ad failed @9 |  |  |
| 1003 | request ad failed @10 |  |  |
| 1003 | request ad failed @50001/30001/20000 |  |  |
| 1001 | request ad failed @20001 |  |  |
| 1004 | request ad failed @50002 |  |  |

## 使用限制
目前只能在抖音使用该方法，今日头条等宿主暂不支持。

## 注意事项
- 出现 2002 错误码意味着至少需要等待 30 秒后再重新请求，建议开发者在代码中自行处理。
- 插屏广告组件每次创建都会返回一个全新的实例，默认是隐藏的，需要调用 [InterstitialAd.show](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/interstitial-ad/interstitial-ad-show) 将其显示。

## 前置条件
接入本能力需要先开通【**流量主**】能力，请前往小游戏开发者后台

1. 在「**商业化**」> 「**流量主**」申请开通能力
2. 在「**流量主**」> 「**广告管理**」中创建插屏广告位，获取广告位id

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/ads/tt-create-interstitial-ad) / [本地体验路径](tt-create-interstitial-ad)
