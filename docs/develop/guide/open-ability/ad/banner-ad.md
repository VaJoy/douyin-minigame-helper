---
title: "Banner广告"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/ad/banner-ad
update_time: 2025-04-24
---

Banner 广告是由客户端原生渲染，覆盖在开发者指定的区域上。
开发者可以调用 [tt.createBannerAd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/tt-create-banner-ad) 创建 Banner 广告实例。Banner 广告组件在创建后会自动拉取广告数据并进行渲染，开发者只需要控制 Banner 广告组件的位置和显示/隐藏即可。

```js
const bannerAd = tt.createBannerAd({
  adUnitId: "xxxx",
})
```

### 显示/隐藏
广告创建后默认是隐藏的，可以通过 [BannerAd.show()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/banner-ad/banner-ad-show) 显示广告。 该方法返回一个 Promise 对象。

```js
const bannerAd = tt.createBannerAd({
  adUnitId: "xxxx",
});
bannerAd.onLoad(() => {
  bannerAd
    .show()
    .then(() => {
      console.log("广告显示成功");
    })
    .catch((err) => {
      console.log("广告组件出现问题", err);
    });
});
```

当切换到没有 Banner 广告组件的场景或页面时，调用 [BannerAd.hide()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/banner-ad/banner-ad-hide) 隐藏 Banner 广告组件。

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

### 广告拉取成功与失败
BannerAd 在创建后会拉取广告。如果拉取失败，通过 [BannerAd.onError()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/banner-ad/banner-ad-on-error) 注册的回调函数会执行，回调函数的参数是一个 rejected Promise。

```js
bannerAd.onError(({ errorCode, errMsg }) => {
   console.log(errorCode, errMsg)
})
```

[BannerAd.show()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/banner-ad/banner-ad-show) 返回的 Promise 也会是一个 rejected Promise。反之，如果拉取成功。[BannerAd.onLoad()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/banner-ad/banner-ad-on-load) 会执行，[BannerAd.show()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/banner-ad/banner-ad-show) 返回的 Promise 会是一个 resolved Promise。两者的回调函数中都没有参数传递。

```js
 bannerAd
    .show()
    .then(() => {
      console.log("广告显示成功");
    })
    .catch((err) => {
      console.log("广告组件出现问题", err);
    });
```

### onResize
开发者除了可以在创建 bannerAd 实例时指定广告的 style，还可以在获得实例后修改其 style 属性中的属性值。一旦广告尺寸发生变化，会触发 [resize 事件的监听器](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/banner-ad/banner-ad-on-resize)。监听器会获得一个包含 width 和 height 属性的对象参数，该参数表征广告的实际渲染尺寸。

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

### 创建新的 BannerAd，销毁旧的 BannerAd
每个 BannerAd 实例在创建后会去拉取一次广告数据并进行渲染，在此之后不再更新。如果想要展示其他内容的 BannerAd，需要创建新的 BannerAd 并将之前的 BannerAd 进行[销毁](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/banner-ad/banner-ad-show)。
如果不对废弃的 BannerAd 进行销毁，则会导致其上的事件监听器无法释放。当没有释放的 BannerAd 积累过多时，将会产生性能问题。

```js
const bannerAd = tt.createBannerAd({
    adUnitId: "xxxx",
})
bannerAd.onLoad(() => {
    bannerAd.show()
    setTimeout(() => {
        bannerAd.destroy()
    }, 3000)
})
```

###

bannerAd.onResize(res => {
bannerAd.style.width = res.width + Math.random()*10})

let bannerAd = wx.createBannerAd({adUnitId: 'xxxx',adIntervals: 30, // 自动刷新频率不能小于30秒// ...})

bannerAd.show()

bannerAd
.show()
.then(() => {
console.log("广告显示成功");
})
.catch((err) => {
console.log("广告组件出现问题", err);
});

let { screenWidth } = wx.getSystemInfoSync()

bannerAd.onResize(res => {
console.log(res.width, res.height)
console.log(bannerAd.style.realWidth, bannerAd.style.realHeight)})
