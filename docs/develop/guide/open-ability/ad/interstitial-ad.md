---
title: "插屏广告"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/ad/interstitial-ad
update_time: 2025-04-24
---

插屏广告是由客户端原生渲染，由开发者控制广告组件的显示。
开发者可以调用 [tt.createInterstitialAd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/tt-create-interstitial-ad) 创建插屏广告组件。每调用一次该方法，返回的都是一个全新实例。
### 广告创建
插屏广告组件默认是隐藏的。

```js
const ad = tt.createInterstitialAd({
  adUnitId: "YOUR_UNIT",
});
```

### 广告拉取成功与失败
开发者需要手动调用 [InterstitialAd.load()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/interstitial-ad/interstitial-ad-load) 拉取广告数据。
如果拉取成功，通过 [InterstitialAd.onLoad()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/interstitial-ad/interstitial-ad-on-load) 注册的回调函数会执行，回调函数没有参数传递。

```js
const interstitialAd = tt.createInterstitialAd({
  adUnitId: "YOUR_AD_UNITID",
});
interstitialAd.onLoad(() => {
  console.log('interstitialAd load')
})
interstitialAd.load()
```

如果拉取失败，通过 [InterstitialAd.onError()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/interstitial-ad/interstitial-ad-on-error) 注册的回调函数会执行，回调函数的参数是一个包含错误信息的对象。[常见异常错误参考文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/interstitial-ad/interstitial-ad-on-error)

```js
interstitialAd.onError(({ errCode, errMsg }) => {
    console.log('监听到错误', errCode, errMsg)
})
```

### 显示/隐藏
插屏广告组件默认是隐藏的，开发者需要调用 [InterstitialAd.show()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/interstitial-ad/interstitial-ad-show) 进行显示。如果广告拉取失败或触发频率限制，[InterstitialAd.show()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/interstitial-ad/interstitial-ad-show) 方法会返回一个rejected Promise，开发者可自行监听错误信息。[常见异常错误参考文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/interstitial-ad/interstitial-ad-on-error)

```js
const ad = tt.createInterstitialAd({
  adUnitId: "YOUR_UNIT",
});
ad.load()
  .then(() => {
    ad.show().then(() => {
      console.log("插屏广告展示成功");
    });
  })
  .catch((err) => {
    console.log(err);
  });
```

用户可以主动关闭插屏广告。开发者不可控制插屏广告组件的隐藏。
### 监听用户关闭广告
如果广告被关闭，通过 [InterstitialAd.onClose()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/interstitial-ad/interstitial-ad-on-close) 注册的回调函数会执行，回调函数没有参数传递。

```js
interstitialAd.onClose(() => {
    console.log('插屏广告关闭')
})
```

### 注意事项
#### 插屏广告频控
对于插屏广告的展示，有一定的频率控制，具体如下：

```js
1. 小游戏启动后的前30s（秒），不能展示插屏广告。
2. 已经展示一次插屏广告后，第二次展示需要距离上一次展示60s。
3. 展示过一次激励视频广告后，后续需要展示插屏广告的情况下，需要与激励视频广告的展示间隔60s。
```

#### 展示异常处理
对于插屏广告的展示，对于异常情况的处理有以下注意：

```js
1. 插屏广告的show调用时，如果出现错误，该错误可以通过onError或者 Promise.catch 捕获，该错误一般为频控错误，建议等待一段时间（参考频控）后再次调用 load->onLoad-> show
```

```js
interstitiaAd.onLoad(onLoadHandle);function onLoadHandle() {
  interstitiaAd
    .show().then(() => {
      console.log("插屏广告展示成功");}).catch((err) => {// 这里出现错误，可以等待一定时间后再次load->onLoad-> show。});
  console.log("广告加载完成");}
```

```js
2. 为保证双端体验，建议始终监听onError，如果需要，可以在 onError 中等待一定时间后再次调用load->onLoad-> show（参考频控和展示逻辑） 。
```

#### 最佳实践

```js
const interstitiaAd = tt.createInterstitialAd();
canReTry = true;
interstitiaAd.onLoad(onLoadHandle); //创建会自动loadfunction onLoadHandle() {
  interstitiaAd.show().then(() => {
    console.log("插屏广告展示成功");});}
interstitiaAd.onError(onErrorHandle); // 自动load 的失败会走到这里function onErrorHandle(err) {// 这里要等待一定时间后，或者等待下次需要展示的时候，参考频控，尝试一次，或者几次，不能一直尝试。if (canReTry) {
    canReTry = false;
    interstitiaAd.load(); //如果需要，这里等待一定时间后，或者等待下次需要展示的时候，再次 load->onLoad-> show。} else {
    tt.showToast({title: "暂无广告",icon: "none",});}}
```

interstitialAd.onLoad(() => {
console.log('插屏 广告加载成功')})

1. 当前插屏广告只有被展示后，才能销毁。

1.  在首次创建插屏广告后，会自动进行一次load，可以用来直接show。
2.  成功展示插屏广告后，再次展示，需要销毁当前插屏后新建，才能显示下一个。

// 第一次展示成功
interstitiaAd.onLoad(onLoadHandle);functiononLoadHandle() {
interstitiaAd.show().then(() => {
console.log("插屏广告展示成功");});}//...要开始第二次展示
interstitiaAd.destroy(); //先销毁当前插屏const interstitiaAd2 = tt.createInterstitialAd(); //新建需要展示的
interstitiaAd2.onLoad(onLoadHandle); //加载后开始展示function onLoadHandle2() {
interstitiaAd2.show().then(() => {
console.log("插屏广告展示成功");});}

interstitiaAd.onLoad(onLoadHandle);functiononLoadHandle() {// interstitiaAd.destroy();  这里未展示情况下，销毁会失败}

interstitialAd.onError(err => {
console.log(err)})
