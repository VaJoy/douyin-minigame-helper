---
title: "BannerAd.onResize"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/banner-ad/banner-ad-on-resize
update_time: 2024-09-19
---

## 语法

```js
BannerAd.onResize(callback)
```
基础库 1.3.0 开始支持本方法，这是一个**同步**方法。
绑定 resize 事件的监听器。

开发者除了可以在创建 bannerAd 实例时指定广告的 style，还可以在获得实例后修改其 style 属性中的属性值。一旦广告尺寸发生变化，会触发 resize 事件的监听器。监听器会获得一个包含 width 和 height 属性的对象参数，该参数表征广告的实际渲染尺寸。

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

// 尺寸调整时会触发回调，通过回调拿到的广告真实宽高再进行定位适配处理
// 注意：如果在回调里再次调整尺寸，要确保不要触发死循环！！！
bannerAd.onResize((size) => {
  // good
  console.log(size.width, size.height);
  bannerAd.style.top = windowHeight - size.height;
  bannerAd.style.left = (windowWidth - size.width) / 2;

  // bad，会触发死循环
  // bannerAd.style.width++;
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.3.0 | 监听器函数  **对象字段** - **data**（Object）：object类型，属性如下： |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |

## 注意事项
注意不要在该监听器内修改广告样式尺寸，否则会导致广告渲染死循环。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
