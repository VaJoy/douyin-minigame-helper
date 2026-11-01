# 用户身份与隐私

> **适用**：登录换标识、多游戏打通账号、拿昵称头像、隐私授权与合规上报。
> **源文档**：`docs/develop/guide/open-ability/user-info/`（5 篇）、`docs/develop/api/javascript-api/open-capacity/log-in/`、`docs/develop/server/log-in/`。
> **关联**：服务端换 openid 的接口细节见 `server.md`；敏感数据脱敏见 `security-release.md`。

## 一、三种标识，别用错

| 标识 | 从哪来 | 唯一性范围 | 用途 |
|---|---|---|---|
| `openid` | `code2session` 用 `code` 换 | **单个小游戏内**唯一 | 游戏内的用户主键 |
| `unionid` | `code2session` 一并返回（需已绑定开放平台） | **同一开发者账号下的所有小游戏**通用 | 多游戏打通账号、跨游戏资产 |
| `anonymous_openid` | 用 `anonymousCode` 换 | 同一台设备恒定 | 未登录用户的临时身份 |

`unionid` 的边界很容易踩错，官方明确写了三条：

- 小程序与小游戏**不互通**；
- 抖音、抖音极速版、抖音火山版**不互通**；
- 同一个开发者下的**所有小游戏之间互通**。

也就是说：想用一个账号串起你的三款小游戏，用 `unionid`；想串抖音和极速版，做不到，只能靠用户自己绑定手机号之类的业务手段。

基础 `unionid` 的获取**不强制用户授权**（它跟着登录流程一起返回，不需要弹窗）。

## 二、登录链路

```
tt.login()                    → code（临时凭证，只能用一次，3 分钟过期）
   ↓ POST /jscode2session
服务端 code2session           → openid + session_key (+ unionid)
   ↓
服务端签发自己的登录态 token   → 客户端保存，后续请求带这个 token
```

```js
tt.login({
  force: false,               // 默认 true：未登录会拉起源端登录框
  success(res) {
    // res.code：端已登录才有；res.anonymousCode：任何情况都有
    // res.isLogin：当前宿主 App 是否已登录
    tt.request({
      url: 'https://your-server/api/login',
      method: 'POST',
      data: { code: res.code, anonymousCode: res.anonymousCode },
      success(r) { /* r.data.token 存起来 */ },
    });
  },
});
```

要点：

- **前端永远拿不到 openid**，必须服务端换。谁把 openid 直接下发客户端，等于把用户体系暴露了。
- `code` 只能用一次，重复使用报错；拿到立刻发给服务端。
- 未登录用户只有 `anonymousCode`，适合做「先玩后登录」的游客态，后续再用正式登录合并数据。

## 三、session_key 的三个坑

`session_key` 是会话密钥，服务端保存，**绝不下发客户端**。

1. **会被刷新顶掉**：用户重新 `tt.login` 可能更新 `session_key`，旧的同时失效。平台有最短刷新周期，短时间内重复 login 不一定每次都换。
2. **有效期不告知**：平台按用户活跃度续期，越常玩越长，但不会告诉你什么时候过期。
3. **失效就重登**：用 `tt.checkSession` 校验，失效了重新走登录流程；自建登录态的有效期可以对齐 `session_key`，也可以自己定策略。

## 四、拿昵称头像（要授权）

```js
tt.login({
  success() {
    tt.getUserInfo({
      withCredentials: true,                  // 需要 encryptedData/signature/iv 时置 true
      withRealNameAuthenticationInfo: false,  // 需要实名信息才置 true
      success(res) {
        // res.userInfo：昵称、头像、性别、城市等
        // res.encryptedData / res.iv / res.signature：withCredentials 才有
      },
      fail(res) { /* 用户拒绝，或登录态失效 */ },
    });
  },
});
```

三种状态要分别处理：

| 状态 | 表现 | 做法 |
|---|---|---|
| 从未授权 | 首次调用弹授权窗 | 正常走，同意后拿数据 |
| 已授权 | 直接返回数据 | 可直接用；但昵称头像可能变，建议每次登录都刷新一次 |
| 已拒绝 | **直接进 fail，不再弹窗** | 只能用 `tt.openSetting` 引导用户去设置页手动打开 |

> 录屏权限（`scope.screenRecord`）默认是开的，不用单独申请；被用户关掉后录屏相关接口会在 `onError` 里报权限错误。

### 哪些接口需要授权

以下接口都涉及用户敏感信息，未授权时调用会失败：

`tt.getUserInfo`、`tt.getLocation`、`tt.getRecorderManager().start`、`tt.saveImageToPhotosAlbum`、`tt.saveVideoToPhotosAlbum`、`tt.scanCode`、`tt.chooseImage`、`tt.chooseVideo`、`tt.requestMicrophone`、`tt.getGameRecorderManager`、`tt.addPhoneCalendar`

## 五、隐私合规（会被审核卡）

### 1. 先配隐私政策

**无论是否处理用户个人信息，都必须配**：控制台 → 小游戏 → 基础设置 → 小游戏隐私政策 → 完善。

两类处理方式都要披露：

- **标准 API 处理**：走 `tt.*` 接口拿的信息，按接口勾选对应 scope；
- **非标准 API 处理**：自己表单收集的手机号、地址等，要在「添加其他权限」里额外声明。

### 2. scope 清单

| scope | 含义 | 最低版本 |
|---|---|---|
| `scope.userInfo` | 用户信息 | 1.3.0 |
| `scope.userLocation` | 地理位置 | 1.3.0 |
| `scope.record` | 麦克风 | 1.3.0 |
| `scope.album` | 保存到相册 | 1.3.0 |
| `scope.camera` | 摄像头 | 1.3.0 |
| `scope.screenRecord` | 录屏（默认开） | 1.3.0 |
| `scope.calendar` | 系统日历 | 1.3.0 |
| `scope.gameClub` | 游戏站数据 | 3.77.0 |
| `scope.groupTag` | 群聊标签 | 3.78.0 |

提前查询授权态用 `tt.authorize` / `tt.getSetting`，用户改过设置后用 `tt.openSetting` 打开设置页。

### 3. 自定义隐私弹窗

```js
tt.onNeedPrivacyAuthorization((resolve, eventInfo) => {
  console.log('触发隐私授权的接口：', eventInfo.referrer);
  showPrivacyPopup({
    onAgree: () => resolve({ event: 'agree' }),
    onDisagree: () => resolve({ event: 'disagree' }),
  });
});
```

基础库 **4.17.0+**。不注册这个回调时，平台用官方弹窗。

> ⚠️ 官方 `用户隐私保护` 那篇文档的示例代码里出现了 `wx.requirePrivacyAuthorize`、`wx.openPrivacyContract` —— 那是**微信**的接口，抖音侧只有 `tt.onNeedPrivacyAuthorization`。照抄 `wx.*` 一定跑不通。

## 六、开放数据校验与解密

`tt.getUserInfo({ withCredentials: true })` 返回的 `encryptedData` 是加密的，解密依赖 `session_key`；同时会返回 `signature` 用于防篡改。

校验流程：

1. 客户端把 `rawData`（明文 JSON 字符串）和 `signature` 一起发给服务端；
2. 服务端用该用户的 `session_key`，按官方示例的算法计算签名，与 `signature` 比对；
3. 一致才信任 `rawData` 的内容；
4. 需要敏感字段时，再用 `session_key` + `iv` 解密 `encryptedData`。

注意：**签名与解密的算法细节以官方示例代码为准**，不要自己发明拼接方式。校验失败优先怀疑 `session_key` 过期（见第三节）。

## 七、排查清单

| 现象 | 原因 |
|---|---|
| 登录成功但换不到 openid | `code` 过期（>3 分钟）或被用过一次 |
| 换到了 openid，但两个游戏对不上 | 用了 `openid` 而不是 `unionid` |
| 昵称头像是空的 | 用户拒绝过 `scope.userInfo`，需要 `tt.openSetting` 引导 |
| 签名校验一直失败 | `session_key` 被新的登录刷新顶掉了；或算法拼接顺序不对 |
| 审核说隐私不合规 | 隐私政策没配、或非标准 API 收集没在「其他权限」里声明 |
| 隐私弹窗不弹 | 基础库 < 4.17.0，或没注册 `tt.onNeedPrivacyAuthorization` |
