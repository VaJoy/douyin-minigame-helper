# 常用 API 配方

> **适用**：8 个高频场景的最小可用写法（登录、激励视频、分享邀请、支付、存储、音频、系统信息、侧边栏），可直接粘进 Cocos 导出的工程。
> **源文档**：`docs/develop/api/javascript-api/` 与 `docs/develop/guide/open-ability/` 的相关页面。
> **关联**：方法版本与授权要求见 `api-index.md`；能力开通前提见 `ads.md` / `payment.md` / `social.md`。

写法约定：

- 示例用回调风格；抖音小游戏的 API **同时支持 Promise**（不传 `success`/`fail` 时返回 Promise）。
- 调用较新的 API 前先 `tt.canIUse('方法名')` 判断，低版本宿主直接跳过功能，而不是报错。
- **本文的代码是权威版本**：其他 reference 里的同类示例如果与本文冲突，以本文为准，改也只改这一处。

## 1. 登录换 openid

`tt.login` 只拿到**临时凭证**（有效期 3 分钟），openid 必须由服务端换取，前端拿不到。

```js
tt.login({
  force: true,                 // 未登录时是否强制拉起登录框，默认 true
  success(res) {
    // res.code：端已登录时才有，用来换 openid
    // res.anonymousCode：未登录也有，同一台设备恒定，可换 anonymous_openid
    // res.isLogin：当前宿主 App 是否已登录
    tt.request({
      url: 'https://your-server/api/login',
      method: 'POST',
      data: { code: res.code },
      success(r) { console.log('服务端返回 openid', r.data.openid); },
    });
  },
  fail(res) { console.warn('登录失败', res.errMsg); },
});
```

要点：
- 只有端已登录的用户 `success` 里才有 `code`，否则只有 `anonymousCode`。
- `code` 有效期 3 分钟，拿到要立刻发给服务端，不要缓存。
- 服务端用 `code2session` 换 `openid` / `session_key`，见 `server.md`。

## 2. 激励视频广告（完整闭环）

```js
// 建议全局只创建一次，重复创建会多耗资源
const videoAd = tt.createRewardedVideoAd({ adUnitId: 'YOUR_UNIT_ID' });

videoAd.onError((err) => console.warn('广告错误', err.errCode, err.errMsg));

videoAd.onClose((res) => {
  // res.isEnded === true 才代表完整看完，可以发奖励
  if (res.isEnded) grantReward();
  else console.log('用户中途关闭，不发奖');
});

function showRewardAd() {
  videoAd.show().catch(() => {
    // 首次 show 失败通常是没有预加载，load 之后再试一次
    videoAd.load().then(() => videoAd.show()).catch((e) => console.warn(e));
  });
}
```

要点：
- 必须在 `onClose` 里判断 `isEnded`，不能只看 `show()` 成功。
- 广告播放期间 JS 逻辑与渲染都会暂停；iOS 会额外触发 `onShow`/`onHide`，安卓不会，**不要**用这两个事件做暂停恢复的唯一依据。
- 广告位要先在开发者后台「商业化 > 流量主」开通并创建，否则报 1002/1008 一类错误。
- 返回 1004 等错误时平台会自动拉起录屏分享兜底，分享成功同样回调 `onClose`。

## 3. 主动分享 / 邀请好友

```js
tt.shareAppMessage({
  channel: 'video',            // 分享渠道，可选值见 ShareParam
  title: '来玩我的游戏',
  desc: '一起冲榜',
  imageUrl: 'https://cdn.example.com/share.png',
  query: 'from=share&uid=123', // 会被拼进启动参数 query
  success(res) { console.log('分享成功', res); },
  fail(res) { console.warn('分享失败', res.errMsg); },
});
```

要点：
- 分享图片优先取后台「运营能力 > 必接能力 > 分享配置」的图片，没配就用兜底图。
- 分享链接有效期 45 天，过期后报 `get shareInfo return null`。
- 被动分享（用户点右上角菜单）要用 `tt.onShareAppMessage` 返回内容，两者不是一回事。
- 部分渠道要求「用户点击」才能触发，脚本直接调用会报 21102。

## 4. 发起支付

```js
tt.requestGamePayment({
  mode: 'game',          // 目前只支持购买游戏币
  env: 0,                // 0 = 正式环境
  currencyType: 'CNY',
  platform: 'android',
  buyQuantity: 60,       // 游戏币数量，必须满足「数量 × 单价 = 限定价格档位」
  zoneId: '1',
  customId: orderId,     // 自定义订单号，必须唯一，服务端回调会带回
  extraInfo: JSON.stringify({ roleId }),  // 可选，≤256 字符
  success(res) { console.log('支付成功', res); },
  fail(res) { console.warn('支付失败', res); },
});
```

要点：
- 调用前先用 `tt.checkSession` 确认登录态，未登录下单会导致订单关联不上账号。
- `customId` 不传或重复会报错，支付回调里也拿不到订单号，道具就发不出去。
- 到账可能延迟，建议拿到回调后每 3 秒轮询一次余额、持续约 1 分钟；**不要**把查余额做成进游戏的前置条件。
- PC 端只支持钻石支付。

## 5. 本地存储

```js
tt.setStorageSync('save_v1', JSON.stringify(saveData));
const raw = tt.getStorageSync('save_v1');
const save = raw ? JSON.parse(raw) : null;
```

要点：
- 同步版会阻塞主线程，大对象（>100KB）建议用异步版 `tt.setStorage`。
- 存储上限与清理时机由平台控制，**不要**把它当唯一存档，重要进度要上云。
- 键名加版本前缀（`save_v1`），方便后续结构升级时丢弃旧档。

## 6. 音频播放

```js
const audio = tt.createInnerAudioContext();
audio.src = 'https://cdn.example.com/bgm.mp3';
audio.loop = true;
audio.onError((e) => console.warn('音频错误', e));
audio.play();
// 切后台时手动 pause，回前台再 play，避免被系统打断后状态错乱
```

要点：
- 采样率只支持 44.1k / 22.05k / 11.025k / 8k / 16k / 24k / 32k / 48k，不在范围内会**静默不播**。
- 每个实例占资源，音效多时用对象池复用，不用了调 `destroy()`。

## 7. 系统信息与启动参数

```js
const sys = tt.getSystemInfoSync();
// sys.platform: 'ios' | 'android' | 'openHarmony'
// sys.SDKVersion: 基础库版本，做兼容判断用
// sys.deviceScore: 机型评分，(0,7.3) 低端 / [7.3,8.51) 中端 / [8.51,+∞) 高端，取不到为 -1
// sys.safeArea: 刘海屏安全区

const launch = tt.getLaunchOptionsSync();
// launch.scene: 启动场景值；launch.query: 分享/链接带过来的参数
```

要点：
- 所有宽高都是**逻辑分辨率**，物理分辨率 = 逻辑分辨率 × `pixelRatio`。
- `deviceScore` 是分档做画质/特效降级的首选依据，比机型白名单靠谱。

## 8. 侧边栏复访（必接能力）

```js
tt.checkScene({
  scene: 'sidebar',
  success(res) {
    if (!res.isExist) return;            // 当前宿主不支持侧边栏
    tt.navigateToScene({
      scene: 'sidebar',
      success() { console.log('已跳转侧边栏'); },
      fail(e) { console.warn('跳转失败', e); },
    });
  },
});
```

要点：
- 这是平台「必接」能力，影响推荐权重，上线前要接。
- `scene` 目前只支持 `sidebar`。
- 必须在用户点击后调用，冷启动直接跳会被拒。
