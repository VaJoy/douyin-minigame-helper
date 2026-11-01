---
title: "旧版 StarkSdk API 迁移 TTSDK API"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/starksdkmigrationguide/starksdk-migration-guide
update_time: 2025-05-26
---

## 背景
抖音 Unity 小游戏提供的 C# SDK，在版本 6.0.0 之后升级了 API 的调用方式，由原来的 `StarkSDK.API` 升级为 `TT` 的调用形式。
原 StarkSDKSpace 名称空间的 `StarkSDK.API `依然可正常使用，但之后版本会逐渐废弃，建议开发者尽快升级到 `TT` 的调用形式。
**推荐：**
- 新接入 Unity C# SDK 的开发者，直接使用 TTSDK 名称空间 `TT` 的 API 调用形式。
- 已经使用低版本 StarkSDKSpace 名称空间 `StarkSDK.API`的开发者，升级后可更改为使用 `TT` 的 API 调用形式，抖音小游戏也提供了脚本文件方便修改升级。

## 新旧API迁移
可使用 [抖音 Unity 小游戏 SDK API 升级工具](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/ttsdk-api-upgrade-guide) 对脚本进行批量修改。

> **必须修改的部分重点说明**：
> - using **StarkSDK**.UNBridgeLib.LitJson -> using **TTSDK**.UNBridgeLib.LitJson 。
> - using **StarkSDK**.SimpleJSON -> using **TTSDK**.SimpleJSON 。
> - 使用 RTCEngineManager 必须引入 **TTSDK **替换原来的 **StarkSDK **。

解决建议： 在命名空间有冲突时用 using XXX = StarkSDKSpace.XXX 实现最小代码改动解决冲突。
### 初始化

| **说明** | **StarkSDK 接口名称** | ** TTSDK  接口名称** |
| --- | --- | --- |
| 运行环境 | StarkSDK.s_IsInContainer | TT.InContainerEnv |
| sdk 初始化 | StarkSDK.Init() | TT.InitSDK() |
| 回调类型名字 | OnStarkContainerInitCallback | TT.OnTTContainerInitCallback |
| 设置初始化的回调 | StarkSDK.API.SetContainerInitCallback(OnStarkContainerInitCallback callback); | 不再提供单独接口，回调作为初始化的可选参数 TT.InitSDK(OnTTContainerInitCallback callback) |

### 系统信息

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| stark_unitysdk 版本号 | StarkSDK.API.SDKVersion | TT.TTSDKVersion |
| 游戏版本号 (webGL 从 PlayerSettings、Native 从 AndroidManifest） | StarkSDK.API.GameVersion | TT.GameVersion |
| 游戏发布版本号 “getGamePublishVersion”调用 or PlayerSettings | StarkSDK.API.GamePublishVersion | TT.GamePublishVersion |
| 获取container sdk 版本号 | StarkSDK.API.GetStarkContainerVersion() | TT.GetTTContainerVersion() |
| 获取小程序启动时的参数 | StarkSDK.API.GetLaunchOptionsSync() | TT.GetLaunchOptionsSync() |
| 返回类型名字 | StarkSDK.API.StarkSystemInfo | TTSystemInfo |
| 获取系统信息。类似小程序开发平台 tt.getSystemInfoSync 接口返回值 | StarkSDK.API.StarkSystemInfo GetSystemInfo() | TT.GetSystemInfo() |
| 游戏发布版本号 “getGamePublishVersion”调用 or PlayerSettings | StarkSDK.API.GamePublishVersion | TT.GamePublishVersion |

### Debug UI 能力

| **说明** | **StarkSDK 接口名称** | ** TTSDK  接口名称** |
| --- | --- | --- |
| 是否显示调试Toast提示 | StarkSDK.API.EnableStarkSDKDebugToast | TT.EnableTTSDKDebugToast |
| 接入sdk的debugpanel面板 | StarkSDK.API.RegisterCommandEvent(Action<string, IList<string>> onCommand) | TT.RegisterCommandEvent(Action<string, IList<string>> onCommand) |

### 数据分析

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| 自定义分析数据上报接口 | StarkSDK.API.ReportAnalytics<T>(string eventName, System.Collections.Generic.Dictionary<string, T> param = null) | TT.ReportAnalytics<T>(string eventName, System.Collections.Generic.Dictionary<string, T> param = null) |
| 广告上报 SendtoTAQ 能力 | StarkSDK.API.StarkSendToTAQ(JsonData data) | TT.SendToTAQ(JsonData data) |
| 获取系统信息。类似小程序开发平台 tt.getSystemInfoSync 接口返回值。 | StarkSDK.API.ReportScene(JsonData param,  Action<JsonData> success = null,  Action<int, string> failed = null,  Action complete = null) | TT.ReportScene(JsonData param,  Action<JsonData> success = null,  Action<int, string> failed = null,  Action complete = null) |

### 客服能力

| **说明** | **StarkSDK 接口名称** | ** TTSDK  接口名称** |
| --- | --- | --- |
| 打开客服聊天页 | StarkSDK.API.OpenCustomerServicePage(Action<bool> csCallback) | TT.OpenCustomerServicePage(Action<bool> csCallback) |
| 小游戏客服能力 | StarkSDK.API.OpenCustomerServiceConversation(JsonData param, Action<bool> callback) | TT.OpenCustomerServiceConversation(JsonData param, Action<bool> callback) |
| 通过客服页面发起支付 | StarkSDK.API.OpenAwemeCustomerService(JsonData options, Action success, Action<int, string> failed) | TT.OpenAwemeCustomerService(JsonData options, Action success, Action<int, string> failed) |

### 广告

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| 获取广告模块 | StarkSDK.API.GetStarkAdManager() | 废弃 |
| 展示激励视频广告单个/多个 | StarkSDK.API.GetStarkAdManager().ShowVideoAdWithId(...) | TT.CreateRewardedVideoAd |
| 创建Banner广告 | StarkSDK.API.GetStarkAdManager().CreateBannerAd(...) | TT.CreateBannerAd |
| 显示 | StarkBannerAd.Show() | TTBannerAd.Show() |
| 隐藏 | StarkBannerAd.Hide() | TTBannerAd.Hide() |
| 销毁 | StarkBannerAd.Destroy() | TTBannerAd.Destroy() |
| 改变样式 | StarkBannerAd.ReSize(...) | TTBannerAd.ReSize(...) |
| 是否有效 | StarkBannerAd.IsInvalid() | TTBannerAd.IsInvalid() |
| 创建并播放插屏广告 | StarkSDK.API.GetStarkAdManager().CreateInterstitialAd(...) | TT.CreateInterstitialAd(string interstitialAdId,     Action<int, string> errCallback = null, Action closeCallback = null, Action loadedCallback = null) |
| 加载 | StarkInterstitialAd.Load() | TTInterstitialAd.Load() |
| 显示 | StarkInterstitialAd.Show() | TTInterstitialAd.Show() |
| 是否已加载 | StarkInterstitialAd.IsLoaded() | TTInterstitialAd.IsLoaded() |
| 销毁 | StarkInterstitialAd.Destroy() | TTInterstitialAd.Destroy() |

### 账号

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| 获取账号模块 | StarkSDK.API.GetAccountManager() | 废弃 |
| 登录-获取临时登录凭证 | StarkSDK.API.GetAccountManager().Login(...) | TT.Login(...) |
| 检查用户当前的 session 状态是否有效 | StarkSDK.API.GetAccountManager().CheckSession(...) | TT.CheckSession(...) |
| 获取已登录用户的基本信息或特殊信息 | StarkSDK.API.GetAccountManager().GetScUserInfo(...) | TT.GetScUserInfo(...) |
| 判断用户是否已经授权给当前游戏读取个人信息 | StarkSDK.API.GetAccountManager().GetUserInfoAuth(...) | TT.GetUserInfoAuth(...) |
| 主动打开获取用户信息的授权界面 | StarkSDK.API.GetAccountManager().OpenSettingsPanel(...) | TT.OpenSettingsPanel(...) |
| 打开设置页面, 获取用户已经授权过的配置。 | StarkSDK.API.GetAccountManager().OpenSetting(...) | TT.OpenSetting(...) |
| 获取用户已经授权过的配置。 | StarkSDK.API.GetAccountManager().GetSetting(...) | TT.GetSetting(...) |
| 用户在实名认证弹窗完成实名认证后回调 | StarkSDK.API.GetAccountManager().SetRealNameAuthenticationCallback(...) | TT.SetRealNameAuthenticationCallback(...) |
| 获取已登录用户的基本信息或特殊信息/是否获取加密信息以及 CloudId | StarkSDK.API.GetAccountManager().GetScUserInfo | TT.GetUserInfo |
| 拉起实名认证窗口 | StarkSDK.API.GetAccountManager().AuthenticateRealName(...) | TT.AuthenticateRealName(...) |
| 提供小游戏获取抖音权限的能力 | StarkSDK.API.GetAccountManager().ShowDouyinOpenAuth(...) | TT.ShowDouyinOpenAuth(...) |

### 录屏

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| 获取录屏模块 | StarkSDK.API.GetStarkGameRecorder() | TT.GetGameRecorder() |
| 开启/关闭录屏 | StarkGameRecorder.SetEnabled(bool enabled) | GameRecorder.SetEnabled(bool enabled) |
| 获取录屏开启状态 | StarkGameRecorder.GetEnabled() | GameRecorder.GetEnabled() |
| 开始录屏 | StarkGameRecorder.StartRecord(...) | GameRecorder.Start(...) |
| 停止录屏 | StarkGameRecorder.StopRecord(...) | GameRecorder.Stop(...) |
| 获取录屏时长 | StarkGameRecorder.GetRecordDuration() | GameRecorder.GetRecordDuration() |
| 分享视频 | StarkGameRecorder.ShareVideo(...) | 录屏模块不再持续支持分享相关（但当前依然可以调用到) |
| 分享视频 | StarkGameRecorder.ShareVideoWithTitleTopics(...) |  |
| 分享视频 | StarkGameRecorder.ShareVideoWithJson(...) |  |
| 获取录屏状态 | StarkGameRecorder.GetVideoRecordState() |  |
| 获取视频分享状态 | StarkGameRecorder.GetVideoShareState() |  |

### Rtc 模块
只要将 import 命名空间从 StarkSDK 改为 TT 即可

### 网络请求

| **说明** | **StarkSDK 接口名称** | ** TTSDK  接口名称** |
| --- | --- | --- |
| 获取网络请求模块 | StarkSDK.API.GetStarkRequest() | 废弃 |
| 发起一个网络请求。网络相关的 API 在使用前需要配置域名白名单。 | StarkSDK.API.GetStarkRequest().Request(...) | TT.Request(...) |

### 分享

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| 获取分享模块 | StarkSDK.API.GetStarkShare() | 废弃 |
| 通用分享 | StarkSDK.API.GetStarkShare().ShareAppMessage(...) | TT.ShareAppMessage(...) |
| 监听用户点击右上角菜单中的“转发” | StarkSDK.API.GetStarkShare().OnShareAppMessage(...) | TT.OnShareAppMessage(...) |
| 取消监听用户点击右上角菜单的“转发”按钮时触发的事件 | StarkSDK.API.GetStarkShare().OffShareAppMessage(...) | TT.OffShareAppMessage(...) |
| 通用分享给好友 | StarkSDK.API.GetStarkShare().ShareMessageToFriend(...) | TT.ShareMessageToFriend(...) |
| 设置小游戏转发按钮为显示状态 | StarkSDK.API.GetStarkShare().ShowShareMenu(...) | TT.ShowShareMenu(...) |
| 设置小游戏转发按钮为隐藏状态 | StarkSDK.API.GetStarkShare().HideShareMenu(...) | TT.HideShareMenu(...) |

### 支付

| **说明** | **StarkSDK 接口名称** | ** TTSDK  接口名称** |
| --- | --- | --- |
| 获取支付服务模块 | StarkSDK.API.GetStarkPayService() | 废弃 |
| 初始化支付接口 | StarkSDK.API.GetStarkPayService().PayModuleInit() | 废弃 |
| 旧支付接口 | StarkSDK.API.GetStarkPayService().Pay(...) | 废弃 |
| 小游戏平台的支付接口 | StarkSDK.API.GetStarkPayService().RequestGamePayment(...) | TT.RequestGamePayment(...) |

### 平台开放能力

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| 关注抖音号 | StarkSDK.API.FollowDouYinUserProfile(...) | TT.OpenAwemeUserProfile |
| 是否已关注抖音号 | StarkSDK.API.IsFollowDouyin(...) | TT.CheckFollowAwemeState |
| 是否在小程序开发者后台绑定了抖音号 | StarkSDK.API.HasBoundDouyin(...) | TT.CheckBoundAweme(...) |
| 创建快捷方式 | StarkSDK.API.CreateShortcut(...) | TT.AddShortcut |
| 快捷方式是否已经创建 | StarkSDK.API.IsShortcutExist(...) | TT.CheckShortcut |
| 跳转到抖音视频 | StarkSDK.API.NavigateToVideoView(...) | TT.NavigateToVideoView(...) |
| 调用宿主方法 | StarkSDK.API.CallHostMethod(...) | TT.CallHostMethod(...) |
| 通过openSchema 来唤起特定 APP 的特定功能，需要联系StarkSDK开发者开通白名单 | StarkSDK.API.OpenSchema(...) | TT.OpenSchema(...) |
| 获取 Room 信息 | StarkSDK.API.GetRoomInfo() | TT.GetRoomInfo() |
| 请求订阅消息 | StarkSDK.API.RequestSubscribeMessage(...) | TT.RequestSubscribeMessage(...) |
| 获取菜单按钮（右上角胶囊按钮）的布局位置信息。坐标信息以屏幕左上角为原点。 | StarkSDK.API.GetMenuButtonLayout() | TT.GetMenuButtonLayout() |
| 同步获取 AppInfo | StarkSDK.API.GetAppInfoSync() | TT.GetAppInfoSync() |
| 向用户发出授权请求 | StarkSDK.API.Authorize(...) | TT.Authorize(...) |

### 互推格子模块

| **说明** | **StarkSDK 接口名称** | ** TTSDK  接口名称** |
| --- | --- | --- |
| 获取互推格子模块 | StarkSDK.API.GetStarkGridGamePanelManager() | 废弃 |
| 游戏互推组件能力 | StarkSDK.API.GetStarkGridGamePanelManager().CreateGridGamePanel(...) | TT.CreateGridGamePanel(...) |

### 宿主事件监听

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| 获取宿主事件监听 | StarkSDK.API.GetStarkHostEvent() | 废弃 |
| 添加宿主事件监听 | StarkSDK.API.GetStarkHostEvent().AddHostEventListener(...) | TT.AddHostEventListener(...) |
| 移除宿主事件监听 | StarkSDK.API.GetStarkHostEvent().RemoveHostEventListener(...) | TT.RemoveHostEventListener(...) |

### 游戏生命周期

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| 获取生命周期模块 | StarkSDK.API.GetStarkAppLifeCycle() | TT.GetAppLifeCycle() |
| 监听游戏切到前台 | StarkSDK.API.GetStarkAppLifeCycle().onAppShow | 待处理 |
| 监听游戏切到后台 | StarkSDK.API.GetStarkAppLifeCycle().onAppHide | <u>待处理</u> |
| 监听游戏切到前台,统一所有平台，并携带参数 | StarkSDK.API.GetStarkAppLifeCycle().OnShow | TTAppLifeCycle.OnShow |
| 监听游戏切到后台，统一所有平台 | StarkSDK.API.GetStarkAppLifeCycle().OnHide | TTAppLifeCycle.OnHide |
| 监听游戏到前台，统一所有平台，携带参数的格式为字典，可以根据指定key获取指定数据 | StarkSDK.API.GetStarkAppLifeCycle().OnShowWithDict | 废弃 |
| 监听游戏退出 | StarkSDK.API.GetStarkAppLifeCycle().SetOnBeforeExitAppListener(...) | TTAppLifeCycle.SetOnBeforeExitAppListener(...) |

### 好友排行榜

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| 获取排行榜 | StarkSDK.API.GetStarkRank() | 废弃 |
| 在关键的游戏场景，设置写入用户的排行榜数据（游戏成绩信息），该数据会上传到服务端（新版） | StarkSDK.API.GetStarkRank().SetImRankDataV2(...) | TT.SetImRankData(...) |
| 获取排行榜列表，调用 API 后， 根据参数自动绘制游戏好友排行榜（新版） | StarkSDK.API.GetStarkRank().GetImRankListV2(...) | TT.GetImRankList(...) |
| 获取排序好的「好友/总榜」数据源，开发者基于数据源自行渲染返回的数据（新版） | StarkSDK.API.GetStarkRank().GetImRankDataV2(...) | TT.GetImRankData(...) |
| 在关键的游戏场景，设置写入用户的排行榜数据（游戏成绩信息），该数据会上传到服务端（旧版） | StarkSDK.API.GetStarkRank().SetImRankData(...) | 不支持 |
| 获取排行榜列表，调用 API 后， 根据参数自动绘制游戏好友排行榜（旧版） | StarkSDK.API.GetStarkRank().GetImRankList(...) | 不支持 |
| 获取排序好的「好友/总榜」数据源，开发者基于数据源自行渲染返回的数据（旧版） | StarkSDK.API.GetStarkRank().GetImRankData(...) | 不支持 |

### 抖音云模块

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| 获取抖音云模块 | StarkSDK.API.GetStarkDouyinCloudManager() | TT.CreateCloud |
| 请求抖音云服务端接口 | StarkSDK.API.GetStarkDouyinCloudManager().CallContainer(...) | TTDouyinCloud.CallContainer |
| 获取抖音云文件访问地址 | StarkSDK.API.GetStarkDouyinCloudManager().GetTempFileUrl(...) | TTDouyinCloud.GetTempFileUrl(...) |
| 抖音云文件删除 | StarkSDK.API.GetStarkDouyinCloudManager().DeleteFile(...) | TTDouyinCloud.DeleteFile(...) |
| 抖音云文件上传 | StarkSDK.API.GetStarkDouyinCloudManager().UploadFile(...) | TTDouyinCloud.UploadFile(...) |
| 下载抖音云文件 | StarkSDK.API.GetStarkDouyinCloudManager().DownloadFile(...) | TTDouyinCloud.DownloadFile(...) |
| 返回抖音云操作数据库对象 | StarkSDK.API.GetStarkDouyinCloudManager().CloudDb() | TTDouyinCloud.CloudDb() |

### 侧边栏模块

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| 获取侧边栏模块 | StarkSDK.API.GetStarkSideBarManager() | 废弃 |
| 确认当前宿主版本是否支持跳转某个小游戏入口场景 | StarkSDK.API.GetStarkSideBarManager().CheckScene(...) | TT.CheckScene(...) |
| 调用该API可以跳转到某个小游戏入口场景 | StarkSDK.API.GetStarkSideBarManager().NavigateToScene(...) | TT.NavigateToScene(...) |
| 注册用户参与复访营销活动。当前只支持侧边栏复访活动 | StarkSDK.API.GetStarkSideBarManager().RequestPromotionActivity(...) | TT.RequestPromotionActivity |
| 领取营销活动中完成任务后的奖励。当前只支持侧边栏复访活动 | StarkSDK.API.GetStarkSideBarManager().ReceiveCoupon(...) | TT.ReceiveCoupon |

### 敏感词

| **说明** | **StarkSDK 接口名称** | ** TTSDK  接口名称** |
| --- | --- | --- |
| 白名单方法，检测敏感词 | StarkSDK.API.SensitiveWordCheck(...) | TT.SensitiveWordCheck(...) |
| 替换敏感词 | StarkSDK.API.ReplaceSensitiveWords(...) | TT.ReplaceSensitiveWords(...) |

### 键盘管理器

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| 获取键盘管理器（仅WebGL支持） | StarkSDK.API.GetStarkKeyboard() | 废弃 |
| 显示软键盘（仅WebGL平台下支持） | StarkSDK.API.GetStarkKeyboard().ShowKeyboard | TT.ShowKeyboard |
| 收起软键盘（仅WebGL平台下支持） | StarkSDK.API.GetStarkKeyboard().HideKeyboard | TT.HideKeyboard |
| 更新键盘，只有当键盘处于拉起状态时才会产生效果。 | StarkSDK.API.GetStarkKeyboard().UpdateKeyboard | TT.UpdateKeyboard |
| 监听键盘输入事件 | StarkSDK.API.GetStarkKeyboard().onTTKeyboardInputEvent | TT.OnKeyboardInput |
| 监听用户点击键盘确定按钮时的事件 | StarkSDK.API.GetStarkKeyboard().onTTKeyboardConfirmEvent | TT.OnKeyboardConfirm |
| 监听键盘收起事件 | StarkSDK.API.GetStarkKeyboard().onKeyboardCompleteEvent | TT.OnKeyboardComplete |

### 输入模块

| **说明** | **StarkSDK 接口名称** | **  TTSDK 接口名称** |
| --- | --- | --- |
| 获取输入模块（仅 WebGL 支持） | StarkSDK.API.GetStarkInput() | 废弃 |
| 监听开始触摸事件 | StarkSDK.API.GetStarkInput().OnTouchStart(...) | TT.OnTouchStart(...) |
| 监听触点移动事件 | StarkSDK.API.GetStarkInput().OnTouchMove(...) | TT.OnTouchMove(...) |
| 监听触摸结束事件 | StarkSDK.API.GetStarkInput().OnTouchEnd(...) | TT.OnTouchEnd(...) |
| 监听触点失效事件 | StarkSDK.API.GetStarkInput().OnTouchCancel(...) | TT.OnTouchCancel(...) |
| 取消监听开始触摸事件 | StarkSDK.API.GetStarkInput().OffTouchStart(...) | TT.OffTouchStart(...) |
| 取消监听触点移动事件 | StarkSDK.API.GetStarkInput().OffTouchMove(...) | TT.OffTouchMove(...) |
| 取消监听触摸结束事件 | StarkSDK.API.GetStarkInput().OffTouchEnd(...) | TT.OffTouchEnd(...) |
| 取消监听触点失效事件 | StarkSDK.API.GetStarkInput().OffTouchCancel(...) | TT.OffTouchCancel(...) |

### 邀请模块

| **说明** | **StarkSDK 接口名称** | **  TTSDK  接口名称** |
| --- | --- | --- |
| 获取邀请模块 | StarkSDK.API.GetStarkInvite() | 废弃 |
| 抖音好友邀请 | StarkSDK.API.GetStarkInvite().CreateInvitePanel(...) | TT.CreateInvitePanel(...) |
| 监听邀请状态变化事件 | StarkSDK.API.GetStarkInvite().onInviteStateChanged | TT.onInviteStateChanged |

### 文件系统模块

| **说明** | **StarkSDK 接口名称** | **  TTSDK 接口名称** |
| --- | --- | --- |
| 获取文件系统 | StarkSDK.API.GetStarkFileSystemManager() | TT.GetFileSystemManager() |
| 将字符串/二进制写入文件（同步） | StarkFileSystemManager.WriteFileSync(...) | TTFileSystemManager.WriteFileSync(...) |
| 将字符串/二进制写入文件（异步） | StarkFileSystemManager.WriteFile(...) | TTFileSystemManager.WriteFile(...) |
| 从本地文件读取字符串数据（同步） | StarkFileSystemManager.ReadFileSync(...) | TTFileSystemManager.ReadFileSync(...) |
| 读取本地文件内容（异步） | StarkFileSystemManager.ReadFile(...) | TTFileSystemManager.ReadFile(...) |
| 判断文件/目录是否存在（同步） | StarkFileSystemManager.AccessSync(...) | TTFileSystemManager.AccessSync(...) |
| 判断文件/目录是否存在（异步） | StarkFileSystemManager.Access(...) | TTFileSystemManager.Access(...) |
| 复制文件（同步） | StarkFileSystemManager.CopyFileSync(...) | TTFileSystemManager.CopyFileSync(...) |
| 复制文件（异步） | StarkFileSystemManager.CopyFile(...) | TTFileSystemManager.CopyFile(...) |
| 重命名文件（同步） | StarkFileSystemManager.RenameFileSync(...) | TTFileSystemManager.RenameFileSync(...) |
| 重命名文件（异步） | StarkFileSystemManager.RenameFile(...) | TTFileSystemManager.RenameFile(...) |
| 删除文件（同步） | StarkFileSystemManager.UnlinkSync(...) | TTFileSystemManager.UnlinkSync(...) |
| 删除文件（异步） | StarkFileSystemManager.Unlink(...) | TTFileSystemManager.Unlink(...) |
| 创建目录（异步） | StarkFileSystemManager.Mkdir(...) | TTFileSystemManager.Mkdir(...) |
| 创建目录（同步） | StarkFileSystemManager.MkdirSync(...) | TTFileSystemManager.MkdirSync(...) |
| 删除目录（同步） | StarkFileSystemManager.RmdirSync(...) | TTFileSystemManager.RmdirSync(...) |
| 删除目录（异步） | StarkFileSystemManager.Rmdir(...) | TTFileSystemManager.Rmdir(...) |
| 读取文件描述信息（同步） | StarkFileSystemManager.StatSync(...) | TTFileSystemManager.StatSync(...) |
| 读取文件描述信息（异步） | StarkFileSystemManager.Stat(...) | TTFileSystemManager.Stat(...) |
| 获取保存的用户目录文件列表（仅WebGL平台可用） | StarkFileSystemManager.GetSavedFileList(...) | TTFileSystemManager.GetSavedFileList(...) |
| 根据url链接获取本地缓存文件路径（仅WebGL平台可用） | StarkFileSystemManager.GetLocalCachedPathForUrl(...) | TTFileSystemManager.GetLocalCachedPathForUrl(...) |
| 判断该url是否有本地缓存文件（仅WebGL平台可用） | StarkFileSystemManager.IsUrlCached(...) | TTFileSystemManager.IsUrlCached(...) |
| 使用本地文件 | StarkFileSystemManager.CanUseLocalStorage() | TTFileSystemManager.CanUseLocalStorage() |
| 数据是否已迁移 | StarkFileSystemManager.IsDataMigrated() | TTFileSystemManager.IsDataMigrated() |
| 迁移数据 | StarkFileSystemManager.MigratingData() | TTFileSystemManager.MigratingData() |

### PlayerPrefs模块

| **说明** | **StarkSDK 接口名称** | **  TTSDK 接口名称** |
| --- | --- | --- |
| PlayerPrefs模块 | StarkSDK.API.PlayerPrefs | TT.PlayerPrefs |
| 写 int | PlayerPrefs.SetInt(...) | PlayerPrefs.SetInt(...) |
| 获取 int | PlayerPrefs.GetInt(...) | PlayerPrefs.GetInt(...) |
| 写 float | PlayerPrefs.SetFloat(...) | PlayerPrefs.SetFloat(...) |
| 获取 float | PlayerPrefs.GetFloat(...) | PlayerPrefs.GetFloat(...) |
| 写 string | PlayerPrefs.SetString(...) | PlayerPrefs.SetString(...) |
| 获取 string | PlayerPrefs.GetString(...) | PlayerPrefs.GetString(...) |
| 是否包含 | PlayerPrefs.HasKey(...) | PlayerPrefs.HasKey(...) |
| 删除 key | PlayerPrefs.DeleteKey(...) | PlayerPrefs.DeleteKey(...) |
| 删除所有 | PlayerPrefs.DeleteAll() | PlayerPrefs.DeleteAll() |
| 写到磁盘 | PlayerPrefs.Save() | PlayerPrefs.Save() |

### 收藏模块

| **说明** | **StarkSDK 接口名称** | **  TTSDK 接口名称** |
| --- | --- | --- |
| 获取收藏引导模块 | StarkSDK.API.GetStarkFavorite() | 废弃 |
| 游戏收藏 | StarkSDK.API.GetStarkFavorite().Collect(...) | TT.Collect(...) |
| 取消游戏收藏 | StarkSDK.API.GetStarkFavorite().CancelCollection(...) | TT.CancelCollection(...) |
| 游戏是否已收藏 | StarkSDK.API.GetStarkFavorite().IsCollected() | TT.IsCollected() |
| 收藏引导,默认为底部弹窗 | StarkSDK.API.GetStarkFavorite().ShowFavoriteGuide(...) | TT.ShowFavoriteGuide(...) |
| 调起引导用户复访的提示弹窗 | StarkSDK.API.GetStarkFavorite().ShowRevisitGuide(...) | TT.ShowRevisitGuide(...) |

### 剪贴板模块

| **说明** | **StarkSDK 接口名称** | **  TTSDK 接口名称** |
| --- | --- | --- |
| 获取剪贴板 | StarkSDK.API.GetStarkClipboard() | 废弃 |
| 设置剪贴板信息 | StarkSDK.API.GetStarkClipboard().SetClipboardData(...) | TT.SetClipboardData(...) |
| 获取剪贴板信息 | StarkSDK.API.GetStarkClipboard().GetClipboardData(...) | TT.GetClipboardData(...) |

### 群聊模块

| **说明** | **StarkSDK 接口名称** | **  TTSDK  接口名称** |
| --- | --- | --- |
| 获取群聊模块 | StarkSDK.API.GetStarkGroup() | 废弃 |
| 查询用户通过小游戏平台创建的群的信息 | StarkSDK.API.GetStarkGroup().CheckGroupInfo(...) | TT.CheckGroupInfo(...) |
| 在平台创建群聊，获得 groupid 后，游戏内通过这个方法引导用户加入抖音群 | StarkSDK.API.GetStarkGroup().JoinGroup(...) | TT.JoinGroup(...) |

### 方向监听

| **说明** | **StarkSDK 接口名称** | **  TTSDK  接口名称** |
| --- | --- | --- |
| 获取方向模块 | StarkSDK.API.GetStarkDeviceMotion() | 废弃 |
| 开始监听设备方向变化 | StarkSDK.API.GetStarkDeviceMotion().StartDeviceMotionListening(...) | TT.StartDeviceMotionListening(...) |
| 停止监听设备方向变化 | StarkSDK.API.GetStarkDeviceMotion().StopDeviceMotionListening(...) | TT.StopDeviceMotionListening(...) |

### 屏幕模块

| **说明** | **StarkSDK 接口名称** | **  TTSDK** ** 接口名称** |
| --- | --- | --- |
| 获取屏幕模块 | StarkSDK.API.GetStarkScreenManager() | 废弃 |
| 设置是否保持屏幕常亮状态 | StarkSDK.API.GetStarkScreenManager().SetKeepScreenOn(...) | TT.SetKeepScreenOn(...) |
| 获取屏幕亮度。 | StarkSDK.API.GetStarkScreenManager().GetScreenBrightness(...) | TT.GetScreenBrightness(...) |
| 设置屏幕亮度 | StarkSDK.API.GetStarkScreenManager().SetScreenBrightness(...) | TT.SetScreenBrightness(...) |

### 游戏金币

| **说明** | **StarkSDK 接口名称** | **  TTSDK** **  接口名称** |
| --- | --- | --- |
| 获取游戏金币模块 | StarkSDK.API.GetStarkGoldCoinGameManager() | 废弃 |
| 金币发放or扣除 | StarkSDK.API.GetStarkGoldCoinGameManager().RequestGoldOrder(...) | TT.RequestGoldOrder(...) |

### 应用退出重启

| **说明** | **StarkSDK 接口名称** | **  TTSDK  接口名称** |
| --- | --- | --- |
| 退出程序 | StarkSDK.API.ExitApp(...) | TT.ExitMiniProgram() |
| 重启小游戏 | StarkSDK.API.RestartApp(...) | bool TT.RestartMiniProgramSync() |

### 游戏信息暂存

| **说明** | **StarkSDK 接口名称** | **  TTSDK   接口名称** |
| --- | --- | --- |
| 保存游戏数据接口，所有游戏数据保存上限50M | StarkSDK.API.Save(...) | TT.Save(...) |
| 加载游戏数据接口，返回数据类型需为Serializable | StarkSDK.API.LoadSaving(...) | TT.LoadSaving(...) |
| 删除游戏数据接口 | StarkSDK.API.DeleteSaving(...) | TT.DeleteSaving(...) |
| 删除所有游戏数据 | StarkSDK.API.ClearAllSavings() | TT.ClearAllSavings() |
| 获取游戏数据磁盘总大小 | StarkSDK.API.GetSavingDiskSize() | TT.GetSavingDiskSize() |

### 兼容性判断接口

| **说明** | **StarkSDK 接口名称** | **  TTSDK  接口名称** |
| --- | --- | --- |
| 接口兼容性判断 | CanIUse.xxx | CanIUse.xxx |

### 音频类

| **说明** | **StarkSDK 接口名称** | **  TTSDK  接口名称** |
| --- | --- | --- |
| 音频类 | StarkAudioManager() | Audio 模块不再支持 StarkAudioManager 模式， 推荐直接使用 Unity AudioSource |
| 是否可使用本地音频功能 | StarkAudioManager.CanUseNativeAudio() |  |
| 函数设置 url 前缀 | StarkAudioManager.SetAudioUrlPrefix() |  |
| 创建 InnerAudioContext | StarkAudioManager.CreateInnerAudioContext(...) |  |

### 陀螺仪

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| 获取陀螺仪模块 | StarkSDK.API.GetStarkGyroscope() | 废弃 |
| 开始监听陀螺仪 | StarkSDK.API.GetStarkGyroscope().StartGyroscope(...) | TT.StartGyroscope(...) |
| 停止监听陀螺仪 | StarkSDK.API.GetStarkGyroscope().StopGyroscope(...) | TT.StopGyroscope(...) |
| 监听回调 | StarkSDK.API.GetStarkGyroscope().OnGyroscopeChangedHandler | TT.OnGyroscopeChange |

### UDP webGL

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| 创建一个 UDP Socket 实例 | StarkSDK.API.CreateUDPSocket() | CreateUDPSocket() |
| 绑定一个系统随机分配的可用端口，或绑定一个指定的端口号 | StarkUDPSocket.Bind() | TTUDPSocket.Bind() |
| 关闭 UDP Socket 实例 | StarkUDPSocket.Close() | TTUDPSocket.Close() |
| 预先连接到指定的 IP 和端口 | StarkUDPSocket.Connect() | TTUDPSocket.Connect() |
| 监听收到消息的事件 | StarkUDPSocket.OnMessage() | TTUDPSocket.OnMessage() |
| 移除收到消息事件的事件监听函数 | StarkUDPSocket.OffMessage() | TTUDPSocket.OffMessage() |
| 监听关闭的事件 | StarkUDPSocket.OnClose() | TTUDPSocket.OnClose() |
| 移除关闭事件的事件监听函数 | StarkUDPSocket.OffClose() | TTUDPSocket.OffClose() |
| 监听错误的事件 | StarkUDPSocket.OnError() | TTUDPSocket.OnError() |
| 移除错误事件的事件监听函数 | StarkUDPSocket.OffError() | TTUDPSocket.OffError() |
| 监听开始监听数据包的事件 | StarkUDPSocket.OnListening() | TTUDPSocket.OnListening() |
| 移除开始监听数据包事件的事件监听函数 | StarkUDPSocket.OffListening() | TTUDPSocket.OffListening() |
| 向指定 IP 和端口发送消息 | StarkUDPSocket.Send() | TTUDPSocket.Send() |
| 字符串表示 | StarkUDPSocket.ToString() | TTUDPSocket.ToString() |

### 震动

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| 可以配置震动周期的手机震动接口 | StarkSDK.API.Vibrate(...) | TT.Vibrate(...) 兼容webGl 和 Native 的震动接口参数 |

### 加速度

| **说明** | **StarkSDK 接口名称** | ** TTSDK 接口名称** |
| --- | --- | --- |
| 开始监听加速度数据 | StarkSDK.API.StartAccelerometer(...) | TT.StartAccelerometer(...) |
| 停止监听加速度数据 | StarkSDK.API.StopAccelerometer(...) | TT.StopAccelerometer(...) |
