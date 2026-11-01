---
title: "插屏广告注意事项"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/interstitial-ad/interstitial-ad-notice
update_time: 2024-07-24
---

> tt.createInterstitialAd 。
## 背景：
开发者使用 tt.createInterstitialAd 创建使用插屏广告时，需要注意以下事项
## 注意事项：
> const interstitiaAd = tt.createInterstitialAd();
### 插屏广告频控
对于插屏广告的展示，有一定的频率控制，具体如下：
1. 小游戏启动后的前30s（秒），不能展示插屏广告。
2. 已经展示一次插屏广告后，第二次展示需要距离上一次展示60s。
3. 展示过一次激励视频广告后，后续需要展示插屏广告的情况下，需要与激励视频广告的展示间隔60s。
### 展示异常处理
对于插屏广告的展示，对于异常情况的处理有以下注意：
1. 插屏广告的show调用时，如果出现错误，该错误可以通过onError或者 Promise.catch 捕获，该错误一般为频控错误，建议等待一段时间（参考频控）后再次调用 load->onLoad-> show
```js
interstitiaAd.onLoad(onLoadHandle);
function onLoadHandle() {
interstitiaAd
.show()
.then(() => {
console.log("插屏广告展示成功");
})
.catch((err) => {
// 这里出现错误，可以等待一定时间后再次load->onLoad-> show。
});
console.log("广告加载完成");
}
```
2. 为保证双端体验，建议始终监听onError，如果需要，可以在 onError 中等待一定时间后再次调用load->onLoad-> show（参考频控和展示逻辑） 。
### 展示逻辑
1. 在首次创建插屏广告后，会自动进行一次load，可以用来直接show。
2. 成功展示插屏广告后，再次展示，需要销毁当前插屏后新建，才能显示下一个。
```js
// 第一次展示成功
interstitiaAd.onLoad(onLoadHandle);
function onLoadHandle() {
interstitiaAd.show().then(() => {
console.log("插屏广告展示成功");
});
}
//...要开始第二次展示
interstitiaAd.destroy(); //先销毁当前插屏
const interstitiaAd2 = tt.createInterstitialAd(); //新建需要展示的
interstitiaAd2.onLoad(onLoadHandle); //加载后开始展示
function onLoadHandle2() {
interstitiaAd2.show().then(() => {
console.log("插屏广告展示成功");
});
}
```
### 销毁逻辑
1. 当前插屏广告只有被展示后，才能销毁。
```js
interstitiaAd.onLoad(onLoadHandle);
function onLoadHandle() {
// interstitiaAd.destroy(); 这里未展示情况下，销毁会失败
}
```
## 最佳实践
```js
const interstitiaAd = tt.createInterstitialAd();
canReTry = true;
interstitiaAd.onLoad(onLoadHandle); //创建会自动load
function onLoadHandle() {
interstitiaAd.show().then(() => {
console.log("插屏广告展示成功");
});
}
interstitiaAd.onError(onErrorHandle); // 自动load 的失败会走到这里
function onErrorHandle(err) {
// 这里要等待一定时间后，或者等待下次需要展示的时候，参考频控，尝试一次，或者几次，不能一直尝试。
if (canReTry) {
canReTry = false;
interstitiaAd.load(); //如果需要，这里等待一定时间后，或者等待下次需要展示的时候，再次 load->onLoad-> show。
} else {
tt.showToast({
title: "暂无广告",
icon: "none",
});
}
}
```
