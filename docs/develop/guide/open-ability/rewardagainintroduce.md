---
title: "商业化激励再得能力介绍"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/rewardagainintroduce
update_time: 2024-07-24
---

`该能力预计23.4版本上线，安卓12月1号左右支持可用`
> 本文档主要介绍平台开放的“再得广告能力”，预计能够拉收 10%-15%以上，请耐心阅读
## 激励式视频广告为游戏持续创收
目前小游戏常见的广告形式为 banner 广告、插屏广告、以及激励广告，其中激励广告是最主要的变现模式，占据总收入来源的 90%左右
## 激励广告有效的模式
**提高结算奖励：**在游戏结束后，让用户可以选择通过观看一个激励视频广告的方式获得比原本更丰厚游戏奖励
**获得重生机会：**当用户游戏失败的时候，提供“复活机会”，可以保证玩家有非常高的观看意愿，也能规避用户因为失败带来的挫败感
**给予游戏帮助：**当玩家在游戏中遇到困难导致卡住整体的游戏进程时，可以通过观看激励视频广告获得关键性提示或道具帮助过关
**获取游戏内的道具：**对于没有版号做内购的游戏，无法通过玩家充值获得收入，可以选择在商店中嵌入激励视频广告。通过观看激励视频广告，玩家可以获得游戏内虚拟道具（货币、皮肤）
![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1667473583672)
## 如何进一步提高广告收入
除了合理的广告位设计之外，如何进一步提高广告收入，我们基于收入的基础公式出发：
**总收入 = 广告请求次数 * 单用户广告价值**
单用户广告价值一般取决于流量主的出价，而广告请求次数是开发者可以去挖掘的增长点，但实际开发中，开发者会遇到以下的难点
> 看广告次数与用户体验其实相违背，不希望埋入太多的广告点
>
> 可以通过稀有的奖励吸引用户看广告，但对于游戏其实是亏的，因为道具价值>用户单次广告价值
>
> 处理游戏内的基础逻辑已经分身乏术，没有办法去设计更多的广告变现场景
针对以上难点，平台这边提供了“再得广告”的 API 能力，接入后，用户在看完广告后，可以快速选择再看一个广告，实现广告价值的增长，在测试的游戏中，均取得了广告流水提高 15% -30%的效果
![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1667473574902)
## 如何设计再得付费点
在 [tt.createRewardedVideoAd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/tt-create-rewarded-video-ad) 方法中，开发者可以传入值来定义 「是否为再得广告、奖励道具文案、可以额外再看几次广告、是否需要进度提示」，平台也会根据用户行为，如实返回用户看了几次广告
那么，如何设计优秀的再得广告付费点，平台这边给到几个建议
#### **可多次领取的道具，通过再得组件，提高用户体验**
对于一些普通道具，开发者会限制每天的领取次数，此时用户的路径如下：
「点击广告 - 观看广告 - 关闭广告 - 获得奖励 - 再次点击广告 - 观看广告」
此时路径非常冗长，用户要进行多次点击行为，用户容易失去耐心
此时通过激励再得组件，通过简单的参数输入，让用户可以在不退出的情况下连续看多个广告，一口气领完当日的奖励，减少了反复操作的频率，在奖励不变的情况下，用户的观看意愿更强了（大概提升 30%左右），开发者也就能获得更高的收入
![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1667473571505)
#### **通过稀有奖励吸引用户看多次广告**
如“无限体力”、“十连抽”、“史诗皮肤”等稀有的道具，用户是有非常强的消费诉求，但对于开发者而言，需要考虑道具成本与收益是否打平
如下面的例子：通过简单的参数输入，让用户一口气看 3 个广告，即可获得对应的道具，此时，通过让用户消费多次广告，用户获得稀有道具，开发者获得更高的收益，实现开发者与用户的双赢
您可以将 progressTip 字段置为 true，此时游戏内也会实时提醒用户还需要看几个广告，这个数值为「您设置的初始数值 - 用户已观看的数值」
![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1667473583294)
#### **阶梯式的奖励激励**
在部分游戏场景中，可以通过「阶梯奖励」的手段刺激用户消费广告，比如首次观看获得 100 金币，再看一个额外获得 120 金币，再看一个额外获得 150 金币，在阶梯奖励模式下，单次广告获得的道具价值逐渐提高，能够显著提高用户的消费意愿
在这种情况下，可以在奖励文案中传入数组，来展示不同的奖励文案持续激励用户，如下图传入的参数为[500 金币,700 金币,900 金币,1100 金币]
![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1669866255977)
## 具体使用方法
点击文档 [tt.createRewardedVideoAd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/tt-create-rewarded-video-ad) ，根据接口文档进行接入
```js
tt.createRewardedVideoAd({
adUnitId: "998877", //广告位id
multiton:true // 代表创建再得广告
multitonRewardMsg:["500金币","700金币","900金币","1100金币"] //多个奖励道具名
multitonRewardTimes:4 //可以额外再看4次广告
progressTip:true //代表需要进度提示
success(res) {
console.log(res);
},
fail(res) {
console.log(res);
}
});
```
## 温馨提示
我们会建议您在几个地方进行细节处理，给用户带来更好的游戏体验

- 奖励文案请一定要传入，让用户直观地知道再看一个广告能够获得什么；我们非常建议您在“看多次广告获得稀有道具”的模式中，将progressTip设置为true，这样系统会根据进度提示用户 “再看x个获得奖励”，能够对进度有整体的把控，否则可能会出现一个看4次广告可以获得的道具，在用户看完一次广告后，系统提示 “再看1个获得奖励”，或出现实际情况与提示不符的badcase

- 该方法调用后，会在 [RewardedVideoAd.onClose](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/rewarded-video-ad/rewarded-video-ad-on-close) 返回两个数值，您可以根据数值给用户发放对应的奖励（**isEnded：**用户是否完整观看了最后一次拉起的广告” 、 **count：** 用户一共看了几次广告）
- 当一个道具需要观看5次广告时，如果用户看了2次后退出，请保留用户已经看过2次的结果（通过回调的count数值），在游戏画面做进度展示（如 2/5），并在用户想要二次请求广告获得完整奖励的的时候，将 multitonRewardTimes 设置为 3（5-2=3），此时广告系统会提示用户 “再看3个广告获得奖励”，能够给到用户最佳的体验
- 由于目前该方法仅支持安卓，您可以通过 [tt.getSystemInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/system-information/tt-get-system-info/) 方法判断用户当前的操作系统与app，做出差异化兼容，当然，即便您不做兼容，我们也会正常返回给您当前用户看了几次广告（当然始终为1或者0），在您做好上述的处理时，完全不会伤害用户体验
