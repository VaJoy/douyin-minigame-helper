---
title: "tt.createRewardedVideoAd"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/tt-create-rewarded-video-ad
update_time: 2024-07-24
---

#### 录屏分享激励能力
> 该能力从基础库开始 2.20 开始
当激励视频广告返回 1004 等错误，用户无法观看广告时，会自动拉起分享系统。具体逻辑为，本地存在录屏文件时，自动拉起录屏分享，不存在录屏时，拉起默认分享面板（分享给好友）。并在用户分享完成后，通过激励视频广告的 onClose 回调 count == 1 ，对于开发者来说，处理逻辑和之前一样。
**需要注意：**
- 该能力默认为开。
- 对于开发者无需修改，兼容现有广告逻辑，分享成功会回调 onClose 中 count == 1。
- 对于用户来说，表现为点击广告后无广告内容，因此弹出录屏分享或好友分享替代，开发者若有必要可以给予用户一定说明。

### 语法

```js
tt.createRewardedVideoAd(params)
```
基础库 1.3.0 开始支持本方法，这是一个**同步**方法。
开发者可以在小游戏中使用 Video 广告获得收入。Video 广告是由客户端原生渲染，覆盖在整个小游戏 Canvas 区域之上。观看广告时会暂停所有 JS 逻辑。Video 广告展示的时候用户不能操作小游戏。

### 示例代码
## 激励再得能力介绍<blockquote elementtiming="developer-element-timing">

该能力从基础库开始 2.74.0 开始支持，即抖音、抖 lite 版本为 23.4 时支持，预计 12 月生效

</blockquote>

能力介绍：<a href="https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/rewardagainintroduce" target="_blank" rel="nofollow" class="syl-link">详情</a>

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

### 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| params | Object | 是 |  | 1.3.0 | object 类型，属性如下：  **对象字段** - **multiton**（boolean）：是否开启再得广告模式（只支持安卓系统的抖音和抖音极速版）  **功能说明：**[激励再得能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/rewardagainintroduce) - **multitonRewardMsg**（Array<string>）：再得广告的奖励文案，玩家每看完一个广告都会展示，如【再看1个获得xx】  xx 即 multitonRewardMsg 中的文案，按顺序依次展示，单个文案最大长度为 7  **multiton 为 true 时必填** - **multitonRewardTimes**（number）：**额外**观看广告的次数，合法的数据范围为 1-4，**multiton 为 true 时必填** - **progressTip**（boolean）：是否开启进度提醒，开启时广告文案为【再看N个获得xx】，关闭时为【 再看1个获得xx】。  N 表示玩家当前还需额外观看广告的次数。 - **adUnitId**（string）：广告位 id，后续可以在平台基于广告位 id 看数 |

### 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| RewardedVideoAd | Object | [RewardedVideoAd](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/rewarded-video-ad/rewarded-video-ad) 实例 |

### 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10301 | feature is not supported in app |  |  |
| 21300 | context exception |  |  |
| 1003 | current activity is null, can not create game banner |  |  |
| 1003 | Please apply for an adUnitId |  |  |
| 1003 | can not create game banner |  |  |
| 1006 | The scene does not support advertising |  |  |
| 1001 | The adUnitId is empty |  |  |
| 1008 | The adUnitId is closed |  |  |
| 1007 | The adUnitId is prohibit |  |  |
| 1002 | The adUnitId is invalid |  |  |
| 20001 | invalid param |  |  |
| 20001 | multitonRewardTimes must be non-null when multiton is true |  |  |
| 20001 | multitonRewardMsg must have content when multiton is true |  |  |
| 20001 | multitonRewardTimes should greater than 1 |  |  |
| 20001 | multitonRewardTimes should less than 4 |  |  |
| 20001 | multitonRewardMsg is too long |  |  |
| 20000 | internal error |  |  |
| 1003 | Host app does not support |  |  |
| 21000 | Host app not supported |  |  |
| 1003 | The adUnitId is empty |  |  |
| 1003 | The adUnitId is invalid |  |  |
| 1003 | unknown ad type |  |  |
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

### 注意事项
- 建议开发者在广告开发时始终注册 onError 方法的监听，保证对所有广告异常情况的处理。
- 广告是全屏展示，由于不同系统的识别有所区别，在 iOS 端，广告的播放和关闭会触发 onShow 和 onHide 事件，安卓则不会。但无论是否触发，在激励广告播放期间，游戏逻辑和渲染都会被暂停，用户不能操作小游戏。
- Video 广告目前支持竖屏展示。如果是横屏游戏在展示时会先切到竖屏

### 前置条件
接入本能力需要先开通【**流量主**】能力，请前往小游戏开发者后台

1. 在「**商业化**」> 「**流量主**」申请开通能力
2. 在「**流量主**」> 「**广告管理**」中创建激励视频广告位，获取广告位 id

### 授权要求
无需开发者授权；无需用户授权

### 支持平台
iOS、Android

### 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/ads/tt-create-rewarded-video-ad) / [本地体验路径](tt-create-rewarded-video-ad)