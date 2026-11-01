---
title: "BannerAd.offResize"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/banner-ad/banner-ad-off-resize
update_time: 2024-09-19
---

## 语法

```js
BannerAd.offResize(callback)
```
基础库 1.3.0 开始支持本方法，这是一个**同步**方法。
解除绑定 resize 事件的监听器。

## 示例代码
```js
const { windowWidth, windowHeight } = tt.getSystemInfoSync();
const targetBannerAdWidth = 200;

// 创建一个居于屏幕底部正中的广告
let bannerAd = tt.createBannerAd({
  adUnitId: "YOUR_AD_UNIT_ID",
  style: {
    width: targetBannerAdWidth,
    top: windowHeight - (targetBannerAdWidth / 16) * 9, // 根据系统约定尺寸计算出广告高度
  },
});
// 也可以手动修改属性以调整广告尺寸
bannerAd.style.left = (windowWidth - targetBannerAdWidth) / 2;

function resize(size) {
  console.log(size.width, size.height);
  bannerAd.style.top = windowHeight - size.height;
  bannerAd.style.left = (windowWidth - size.width) / 2;
}

bannerAd.onResize(resize);
bannerAd.offResize(resize);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.3.0 | 通过 [BannerAd.onResize](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/banner-ad/banner-ad-on-resize) 绑定的监听器 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
