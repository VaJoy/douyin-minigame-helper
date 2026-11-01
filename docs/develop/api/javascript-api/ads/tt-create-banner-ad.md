---
title: "tt.createBannerAd"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/tt-create-banner-ad
update_time: 2024-07-24
---

## 语法

```js
tt.createBannerAd(params)
```
基础库 1.3.0 开始支持本方法，这是一个**同步**方法。
开发者可以在小游戏中使用 Banner 广告获得收入。Banner 广告是由客户端原生渲染，覆盖在开发者指定的区域上。

## 示例代码
```js
const bannerAd = tt.createBannerAd({
  adUnitId: "xxxx",
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| params | Object | 是 |  | 1.3.0 | params为 object 类型，属性如下：  **对象字段** - **adIntervals**（number）：广告自动刷新的间隔时间，单位为秒，参数值必须大于等于 30（该参数不传入时 Banner 广告不会自动刷新） - **style**（Object）：广告位区域，包括left、top、width字段 - **adUnitId**（string）：广告位id |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| BannerAdInstance | Object | [BannerAd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/banner-ad/banner-ad)实例对象 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10301 | feature is not supported in app |  |  |
| 21300 | context exception |  |  |
| 1003 | current activity is null, can not create game banner |  |  |
| 1006 | The scene does not support advertising |  |  |
| 1003 | can not create game banner |  |  |
| 1001 | The adUnitId is empty |  |  |
| 1003 | Please apply for an adUnitId |  |  |
| 1008 | The adUnitId is closed |  |  |
| 1007 | The adUnitId is prohibit |  |  |
| 1002 | The adUnitId is invalid |  |  |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |
| 1003 | Host app does not support |  |  |
| 1003 | The adUnitId is invalid |  |  |
| 1003 | unknown ad type |  |  |
| 21000 | host app not supported |  |  |
| 1003 | The adUnitId is empty |  |  |
| 21000 | unitid is illegal |  |  |
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
| 1000 | network unavailable |  |  |

## 注意事项
- 每个广告实例只会与一条固定的广告素材绑定。开发者如果想要展示另一条广告，需要创建一个新的 bannerAd 实例。
- adIntervals 自动刷新并不会保证必须刷新，也不会无限刷新。
- 竖屏情况下，Banner 广告 接受的最小宽度是 300（设备像素），最大宽度是 Math.floor(屏幕宽度）。
- 横屏情况下，Banner 广告 接受的最小宽度是 128（设备像素），最大宽度是 208（设备像素）。开发者可以在这之间自由指定广告宽度。广告组件会自动等比例缩放素材。

## 前置条件
接入本能力需要先开通【**流量主**】能力，请前往小游戏开发者后台

1. 在「**商业化**」> 「**流量主**」申请开通能力
2. 在「**流量主**」> 「**广告管理**」中创建Banner广告位，获取广告位id

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
