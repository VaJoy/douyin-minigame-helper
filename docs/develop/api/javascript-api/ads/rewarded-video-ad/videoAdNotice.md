---
title: "激励视频广告注意"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/rewarded-video-ad/videoAdNotice
update_time: 2024-08-28
---

> tt.createRewardedVideoAd 。
## 背景：
开发者使用 tt.createRewardedVideoAd 创建激励视频广告时，会存在各种不合理情况，导致广告价值和收入降低。为了帮助开发者提高广告收入，针对激励视频广告做些注意事项说明。
## 注意事项：
> const videoAd = tt.createRewardedVideoAd();
### 广告展示
说明：开发者可以调用 videoAd.show 用于广告展示
#### 注意 1：
为了保证广告价值，广告创建后可以在用户操作时直接调用 show 进行广告的显示，而不需再次调用 load。
### 广告加载
说明：开发者可以调用 videoAd.load 用于广告加载，但建议直接使用 show 进行展示，而不用 load->触发 onLoad->show 的链路。
#### 注意 1：
第一次通过 tt.createRewardedVideoAd() 创建广告对象后，videoAd 不会抛出任何事件，目前也不会自动加载。所以，不要采用下面的代码：

```js
const videoAd = tt.createRewardedVideoAd();
videoAd.onLoad(() => {
  videoAd.show();
  console.log("广告加载完成");
});
```

因为广告创建后初始化处于一个无状态对象状态，创建后没有调用 load 方法而去监听了 onLoad 事件，会导致上面广告一直无法展示。
#### 注意 2：
任何针对 onload 事件的监听，都需要确保有调用 videoAd.load() 主动去加载的行为;
#### 注意 3:
为了保证最佳实践，正确的广告调用顺序应该是先注册 onLoad 回调函数后，再去调用 load 方法主动加载广告。如下代码

```js
//最佳实践
const videoAd = tt.createRewardedVideoAd();
videoAd.onLoad(() => {
  videoAd.show();
  console.log("广告加载完成");
});
videoAd.load();
```

否则，如果先调用 load 方法再去注册 onLoad 回调，可能导致 load 成功事件抛出时，还不存在 onLoad 注册。

```js
const videoAd = tt.createRewardedVideoAd();
videoAd.load();
//这样会存在问题，load调用后，广告可能会立即加载完成抛出成功事件，
//但是此时onLoad 回调还未绑定，所以下面的onLoad代码永远不会触发。
videoAd.onLoad(() => {
  videoAd.show();
  console.log("广告加载完成");
});
```

#### 注意 4:
针对注意 3 所提到的调用顺序，开发者也可以通过 load.then() 的方式来规避，因为 load 方法返回的是一个 Promise，Promise.then 的异步机制能够保证 load 成功后，必定会进入到 then()中。

```js
const videoAd = tt.createRewardedVideoAd();
videoAd.load().then(() => {
  console.log("手动加载成功");
  videoAd.show();
});
```

### 广告错误
说明：开发者可以调用 videoAd.onError 监听广告展示中出现的错误
#### 注意 1:
为了保证稳定性，建议监听该事件，对广告的异常进行处理。
