---
title: "激励视频广告"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/ad/incentive-ads
update_time: 2025-04-24
---

Video 广告是由客户端原生渲染，覆盖在整个小游戏 Canvas 区域之上。观看广告时会暂停所有 JS 逻辑。Video 广告展示的时候用户不能操作小游戏。
开发者可以调用 [tt.createRewardedVideoAd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/tt-create-rewarded-video-ad) 创建激励视频广告组件。该方法返回的是一个全局单例。

```js
const videoAd = tt.createRewardedVideoAd({
  adUnitId: "xxxxxxxxxxx",
  multiton: true,
  multitonRewardMsg: ['更多奖励1', '更多奖励2', '更多奖励3'],
  multitonRewardTimes: 3,
  progressTip: false,
});
videoAd.show().then(() => {
  console.log("视频广告展示");
});
```

为避免滥用广告资源，目前每个用户每天可观看激励式视频广告的次数有限，建议展示广告按钮前先判断广告是否拉取成功。
### 广告拉取成功与失败
开发者需要调用 [RewardedVideoAd.load()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/rewarded-video-ad/rewarded-video-ad-load) 拉取广告数据。
如果拉取成功。[RewardedVideoAd.onLoad()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/rewarded-video-ad/rewarded-video-ad-on-load) 会执行，[RewardedVideoAd.show()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/rewarded-video-ad/rewarded-video-ad-show) 返回的 Promise 也会是一个 resolved Promise。两者的回调函数中都没有参数传递。

```js
const videoAd = tt.createRewardedVideoAd({
  adUnitId: "YOUR_UNIT",
});
function listener() {
  console.log('load emit')
}
videoAd.onLoad(listener); //这里监听广告的 load 事件
videoAd.load();
//不需要的时候
videoAd.offLoad(listener);
```

如果拉取失败，通过 [RewardedVideoAd.onError()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/rewarded-video-ad/rewarded-video-ad-on-error) 注册的回调函数会执行，回调函数的参数是一个包含错误信息的对象。[常见异常错误参考文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/rewarded-video-ad/rewarded-video-ad-on-error)

```js
const videoAd = tt.createRewardedVideoAd({
  adUnitId: "YOUR_UNIT",
});
function listener() {
  console.log('error emit')
}
videoAd.onError(listener);
//不需要的时候
videoAd.offError(listener);
```

[RewardedVideoAd.show()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/rewarded-video-ad/rewarded-video-ad-show) 返回的 Promise 也会是一个 rejected Promise。
### 显示/隐藏
激励视频广告组件默认是隐藏的，需要调用 [RewardedVideoAd.show()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/rewarded-video-ad/rewarded-video-ad-show) 进行显示。

```js
const videoAd = tt.createRewardedVideoAd();
videoAd.show().then(() => {
  console.log("视频广告展示");
});
```

只有在用户点击激励视频广告组件上的 `关闭广告` 按钮时，广告才会关闭。开发者不可控制激励视频广告组件的隐藏。
### 监听用户关闭广告
只有在用户点击激励视频广告组件上的 `关闭广告` 按钮时，广告才会关闭。这个事件可以通过 [RewardedVideoAd.onClose()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/rewarded-video-ad/rewarded-video-ad-on-close) 监听。
[RewardedVideoAd.onClose()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/rewarded-video-ad/rewarded-video-ad-on-close) 的回调函数会传入一个参数 res，`res.isEnded` 描述广告被关闭时的状态。

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| isEnded | boolean | 视频是否是在用户完整观看的情况下被关闭的，true 表示用户是在视频播放完以后关闭的视频，false 表示用户在视频播放过程中关闭了视频 |

开发者可以根据 `res.isEnded` 判断是否视频是否播放结束、可以向用户下发奖励。

```js
const videoAd = tt.createRewardedVideoAd({
  adUnitId: "YOUR_UNIT",
  multiton: true,
  multitonRewardedMsg: "观看下一个可领取更多奖励",
});
function listener(res) {
  if (res.isEnded) {
    // do something
  }
  if (res.count) {
    //在支持多例模式的版本上会返回该字段，并且是否返回该字段与multiton是否为true无关
    //判断观看了几次广告
  }
}
videoAd.onClose(listener); //这里监听广告的close 事件
//.... do something
//不需要的时候
videoAd.offClose(listener);
```

### 注意事项
#### 广告展示
说明：开发者可以调用 videoAd.show 用于广告展示
##### 注意 1：
为了保证广告价值，广告创建后可以在用户操作时直接调用 show 进行广告的显示，而不需再次调用 load。
#### 广告加载
说明：开发者可以调用 videoAd.load 用于广告加载，但建议直接使用 show 进行展示，而不用 load->触发 onLoad->show 的链路。
##### 注意 1：
第一次通过 tt.createRewardedVideoAd() 创建广告对象后，videoAd 不会抛出任何事件，目前也不会自动加载。所以，不要采用下面的代码：

```js
const videoAd = tt.createRewardedVideoAd();
videoAd.onLoad(() => {
  videoAd.show();
  console.log("广告加载完成");});
```

因为广告创建后初始化处于一个无状态对象状态，创建后没有调用 load 方法而去监听了 onLoad 事件，会导致上面广告一直无法展示。
##### 注意 2：
任何针对 onload 事件的监听，都需要确保有调用 videoAd.load() 主动去加载的行为;
##### 注意 3:
为了保证最佳实践，正确的广告调用顺序应该是先注册 onLoad 回调函数后，再去调用 load 方法主动加载广告。如下代码

```js
//最佳实践const videoAd = tt.createRewardedVideoAd();
videoAd.onLoad(() => {
  videoAd.show();
  console.log("广告加载完成");});
videoAd.load();
```

否则，如果先调用 load 方法再去注册 onLoad 回调，可能导致 load 成功事件抛出时，还不存在 onLoad 注册。

```js
const videoAd = tt.createRewardedVideoAd();
videoAd.load();//这样会存在问题，load调用后，广告可能会立即加载完成抛出成功事件，//但是此时onLoad 回调还未绑定，所以下面的onLoad代码永远不会触发。
videoAd.onLoad(() => {
  videoAd.show();
  console.log("广告加载完成");});
```

##### 注意 4:
针对注意 3 所提到的调用顺序，开发者也可以通过 load.then() 的方式来规避，因为 load 方法返回的是一个 Promise，Promise.then 的异步机制能够保证 load 成功后，必定会进入到 then()中。

```js
const videoAd = tt.createRewardedVideoAd();
videoAd.load().then(() => {
  console.log("手动加载成功");
  videoAd.show();});
```

#### 广告错误
说明：开发者可以调用 videoAd.onError 监听广告展示中出现的错误
##### 注意 1:
为了保证稳定性，建议监听该事件，对广告的异常进行处理。

rewardedVideoAd.show().catch(err =>console.log(err))

rewardedVideoAd.onLoad(() => {
console.log('激励视频 广告加载成功')})

rewardedVideoAd.show().then(() => console.log('激励视频 广告显示'))

rewardedVideoAd.onLoad((res) => {// res: { useFallbackSharePage: true }if (res && res.useFallbackSharePage) {
console.log('使用兜底分享页')}})

rewardedVideoAd.load().then(() => rewardedVideoAd.show())

rewardedVideoAd.show().catch(err => {
rewardedVideoAd.load().then(() => rewardedVideoAd.show())})

rewardedVideoAd.onError(err => {
console.log(err)})

let rewardedVideoAd = wx.createRewardedVideoAd({ adUnitId: 'xxxx' })

rewardedVideoAd.show().catch(err => console.log(err))

rewardedVideoAd = wx.createRewardedVideoAd({adUnitId: 'xxxx',disableFallbackSharePage: true})
