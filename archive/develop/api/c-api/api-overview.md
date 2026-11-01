---
title: "API 概览"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/api-overview
update_time: 2025-12-12
---

| 初始化 | [初始化](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/init/init) | TT.InitSDK |  |
| --- | --- | --- | --- |
| 开放能力 | [账号](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/account) | TT.Login |  |
|  |  | TT.CheckSession |  |
|  |  | TT.GetUserInfo |  |
|  |  | TT.AuthenticateRealName |  |
|  |  | TT.SetRealNameAuthenticationCallback |  |
|  |  | TT.GetSetting |  |
|  |  | TT.OpenSetting |  |
|  |  | [AuthSetting](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/set/auth-setting) |  |
|  |  | TT.Authorize |  |
|  |  | TT.ShowDouyinOpenAuth |  |
|  | [侧边栏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/sidebar) | TT.CheckScene |  |
|  |  | TT.NavigateToScene |  |
|  |  | TT.RequestPromotionActivity |  |
|  |  | TT.ReceiveCoupon |  |
|  | [小游戏收藏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/favorites) | TT.ShowFavoriteGuide |  |
|  | [群聊](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/group-chat) | [游戏群聊能力接入介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/im-group/groupchatintroduce) |  |
|  |  | TT.JoinGroup |  |
|  |  | TT.CheckGroupInfo |  |
|  | [平台开放能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/ability-open) | 游戏内关注抖音号 | [关注抖音号能力介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/follow/follow-aweme/followintroduce) |
|  |  |  | TT.CheckFollowAwemeState |
|  |  |  | TT.OpenAwemeUserProfile |
|  |  |  | TT.CheckBoundAweme |
|  |  | 添加到桌面 | TT.AddShortcut |
|  |  |  | TT.CheckShortcut |
|  |  | 视频页跳转 | TT.NavigateToVideoView |
|  |  | 订阅消息 | [订阅消息能力介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/subscribe-message/introduce) |
|  |  |  | TT.RequestSubscribeMessage |
|  |  | TT.GetRoomInfo |  |
|  |  | TT.GetMenuButtonLayout |  |
|  | [直玩能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/direct-play) | TT.RequestFeedSubscribe |  |
|  |  | TT.CheckFeedSubscribeStatus |  |
|  |  | TT.OnFeedStatusChange |  |
|  |  | TT.OffFeedStatusChange |  |
|  | [游戏互推组件](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/grid-game-panel) | [游戏推荐组件能力介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/grid-game-panel/Gamerecommend) |  |
|  |  | TT.CreateGridGamePanel |  |
|  |  | GridGamePanel |  |
|  | [游戏排行榜](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/game-rank) | [游戏排行榜功能介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/game-rank/ImRankIntroduce) |  |
|  |  | TT.SetImRankData |  |
|  |  | TT.GetImRankList |  |
|  |  | TT.GetImRankData |  |
|  | [直播能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/live-manager) | TT.GetLiveManager |  |
|  |  |  | TTLiveManager.CheckRoomIsValid |
|  |  |  | TTLiveManager.NavigateToLive |
|  |  |  | TTLiveManager.GetLiveStatus |
|  |  |  | TTLiveManager.OnXScreenSizeChange |
|  |  |  | TTLiveManager.OffXScreenSizeChange |
|  | [公会群能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/union-group-ability) | TT.GetUnionGroupInfo |  |
|  |  | TT.BindUnionGroup |  |
|  |  | TT.UnbindUnionGroup |  |
|  |  | TT.JoinUnionGroup |  |
|  | [数据分析](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/data-analysis) | TT.ReportAnalytics |  |
|  |  | TT.ReportScene |  |
|  | 客服能力 | TT.OpenCustomerServiceConversation |  |
|  |  | TT.OpenAwemeCustomerService |  |
| 基础 | [兼容性判断接口](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/basics/tt-can-i-use) | CanIUse |  |
| 设备 | [加速度计](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/device/jerkmeter) | TT.StartAccelerometer |  |
|  |  | TT.StopAccelerometer |  |
|  | [剪贴板](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/device/clipboard) | TT.GetClipboardData |  |
|  |  | TT.SetClipboardData |  |
|  | [屏幕亮度 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/device/screen) | TT.SetKeepScreenOn |  |
|  |  | TT.GetScreenBrightness |  |
|  |  | TT.SetScreenBrightness |  |
|  | [震动](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/device/vibration) | TT.Vibrate |  |
|  | [陀螺仪 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/device/gyroscope) | TT.StartGyroscope |  |
|  |  | TT.StopGyroscope |  |
|  |  | TT.OnGyroscopeChange |  |
|  | [设备方向 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/device/device-motion) | TT.StartDeviceMotionListening |  |
|  |  | TT.StopDeviceMotionListening |  |
|  | [键盘](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/device/keyboard) | TT.OnKeyUp |  |
|  |  | TT.OffKeyUp |  |
|  |  | TT.OnKeyDown |  |
|  |  | TT.OffKeyDown |  |
|  | [鼠标](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/device/mouse) | TT.OnMouseUp |  |
|  |  | TT.OffMouseUp |  |
|  |  | TT.OnMouseDown |  |
|  |  | TT.OffMouseDown |  |
|  |  | TT.OnMouseMove |  |
|  |  | TT.OffMouseMove |  |
|  | [滚轮](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/device/wheel) | TT.OnWheel |  |
|  |  | TT.OffWheel |  |
|  | [网络](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/device/network) | TT.GetNetWorkType |  |
| 文件 | [获取文件管理器](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/file/get-file-manager) | TT.GetFileSystemManager |  |
|  | [文件管理器](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/file/file-system-manager) | TTFileSystemManager |  |
|  |  | TTFileSystemManager.Access |  |
|  |  | TTFileSystemManager.AccessSync |  |
|  |  | TTFileSystemManager.GetSavedFileList |  |
|  |  | TTFileSystemManager.CopyFile |  |
|  |  | TTFileSystemManager.CopyFileSync |  |
|  |  | TTFileSystemManager.GetFileInfo |  |
|  |  | TTFileSystemManager.Mkdir |  |
|  |  | TTFileSystemManager.MkdirSync |  |
|  |  | TTFileSystemManager.Readdir |  |
|  |  | TTFileSystemManager.ReaddirSync |  |
|  |  | TTFileSystemManager.ReadFile |  |
|  |  | TTFileSystemManager.ReadFileSync |  |
|  |  | TTFileSystemManager.Rename |  |
|  |  | TTFileSystemManager.RenameSync |  |
|  |  | TTFileSystemManager.Rmdir |  |
|  |  | TTFileSystemManager.RmdirSync |  |
|  |  | TTFileSystemManager.Stat |  |
|  |  | TTFileSystemManager.StatSync |  |
|  |  | TTFileSystemManager.Unlink |  |
|  |  | TTFileSystemManager.UnlinkSync |  |
|  |  | TTFileSystemManager.WriteFile |  |
|  |  | TTFileSystemManager.WriteFileSync |  |
|  |  | TTFileSystemManager.AppendFile |  |
|  |  | TTFileSystemManager.AppendFileSync |  |
|  |  | TTFileSystemManager.ReadDir |  |
|  |  | TTFileSystemManager.ReadDirSync |  |
|  |  | TTFileSystemManager.Truncate |  |
|  |  | TTFileSystemManager.TruncateSync |  |
|  |  | TTFileSystemManager.Open |  |
|  |  | TTFileSystemManager.OpenSync |  |
|  |  | TTFileSystemManager.Close |  |
|  |  | TTFileSystemManager.CloseSync |  |
|  |  | TTFileSystemManager.Write |  |
|  |  | TTFileSystemManager.WriteSync |  |
|  |  | TTFileSystemManager.Read |  |
|  |  | TTFileSystemManager.ReadSync |  |
|  |  | TTFileSystemManager.ReadCompressedFile |  |
|  |  | TTFileSystemManager.ReadCompressedFileSync |  |
|  |  | TTFileSystemManager.Fstat |  |
|  |  | TTFileSystemManager.FstatSync |  |
|  |  | TTFileSystemManager.Ftruncate |  |
|  |  | TTFileSystemManager.FtruncateSync |  |
| 媒体 | [录屏 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/media/record) | TT.GetGameRecorderManager |  |
|  | GameRecorderManager | TTGameRecorderManager |  |
|  |  | TTGameRecorderManager.IsShowShareVideoToast |  |
|  |  | TTGameRecorderManager.SetEnabled |  |
|  |  | TTGameRecorderManager.GetEnabled |  |
|  |  | TTGameRecorderManager.SetCustomKeyFrameInterval |  |
|  |  | TTGameRecorderManager.Start |  |
|  |  | TTGameRecorderManager.Stop |  |
|  |  | TTGameRecorderManager.GetRecordDuration |  |
|  |  | TTGameRecorderManager.GetVideoRecordState |  |
|  |  | TTGameRecorderManager.SetDefaultBgm |  |
|  |  | TTGameRecorderManager.GetVideoShareState |  |
| 网络 | [发起请求 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/internet/tt-request) | TT.Request |  |
|  | [UDPSocket](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/internet/udp-socket) | TT.CreateUDPSocket |  |
|  |  | TTUDPSocket | TTUDPSocket |
|  |  |  | TTUDPSocket.Bind |
|  |  |  | TTUDPSocket.Close |
|  |  |  | TTUDPSocket.Connect |
|  |  |  | TTUDPSocket.OnMessage |
|  |  |  | TTUDPSocket.OffMessage |
|  |  |  | TTUDPSocket.OnClose |
|  |  |  | TTUDPSocket.OffClose |
|  |  |  | TTUDPSocket.OnError |
|  |  |  | TTUDPSocket.OffError |
|  |  |  | TTUDPSocket.OnListening |
|  |  |  | TTUDPSocket.OffListening |
|  |  |  | TTUDPSocket.Send |
|  |  |  | TTUDPSocket.ToString |
| [游戏分享 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/game-share/share-module) | [分享逻辑](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/logic) |  |  |
|  | ShareParam |  |  |
|  | TT.ShareAppMessage |  |  |
|  | TT.ShowShareMenu |  |  |
|  | [视频拍摄器](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/video) |  |  |
|  | [剪映模板](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/capcut-guide) |  |  |
|  | TT.OnShareAppMessage |  |  |
|  | TT.OffShareAppMessage |  |  |
|  | TT.NavigateToVideoView |  |  |
| [数据缓存](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/data-cache/data-caching) | [本地数据缓存](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/other/local-data-caching) |  |  |
|  | TT.Save |  |  |
|  | TT.LoadSaving |  |  |
|  | TT.DeleteSaving |  |  |
|  | TT.ClearAllSaving |  |  |
|  | TT.GetSavingDiskSize |  |  |
| 系统 | [生命周期](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/system/game-lifecycle) | TTAppLifeCycle | OnShow |
|  |  |  | OnHide |
|  | [退出重启](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/system/quit-restart) | TT.RestartMiniProgramSync |  |
|  |  | TT.ExitMiniProgram |  |
|  | [获取启动参数](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/system/game-launch-params) | TT.GetLaunchOptionsSync |  |
|  | [版本号 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/system/version-number) | TT.TTSDKVersion |  |
|  |  | TT.GameVersion |  |
|  |  | TT.GamePublishVersion |  |
|  |  | TT.GetContainerVersion |  |
|  | [系统信息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/system/get-system-info) | TT.GetSystemInfo |  |
|  | [触摸事件](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/system/touch-event) | TTTouch |  |
|  |  | TT.OnTouchStart |  |
|  |  | TT.OnTouchMove |  |
|  |  | TT.OnTouchEnd |  |
|  |  | TT.OnTouchCancel |  |
|  |  | TT.OffTouchStart |  |
|  |  | TT.OffTouchMove |  |
|  |  | TT.OffTouchEnd |  |
|  |  | TT.OffTouchCancel |  |
| 广告 | [商业化激励再得能力介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/rewardagainintroduce) |  |  |
|  | [Banner广告](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/ads/banner-ads) | TT.CreateBannerAd |  |
|  |  | BannerAd |  |
|  | [激励视频广告](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/ads/rewardedvideoad) | TT.CreateRewardedVideoAd |  |
|  |  | RewardedVideoAd |  |
|  | [插屏广告](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/ads/interstitial-ad) | TT.CreateInterstitialAd |  |
|  |  | InterstitialAd |  |
|  | [插屏广告注意事项](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/interstitial-ad/interstitial-ad-notice) |  |  |
| 界面 | [键盘处理器](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/ui/keyboard-processor) | TT.ShowKeyboard |  |
|  |  | TT.HideKeyboard |  |
|  |  | TT.UpdateKeyboard |  |
|  |  | TT.OnKeyboardComplete |  |
|  |  | TT.OnKeyboardConfirm |  |
|  |  | TT.OnKeyboardInput |  |
|  |  | TT.OffKeyboardComplete |  |
|  |  | TT.OffKeyboardConfirm |  |
|  |  | TT.OffKeyboardInput |  |
|  | [敏感词](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/ui/sensitive-words) | TT.SensitiveWordCheck |  |
|  |  | TT.ReplaceSensitiveWords |  |
| 渲染 | [光标样式](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/drawing/cursor-style) | Cursor.SetCursor |  |
|  |  | TT.RequestPointerLock |  |
|  |  | TT.IsPointerLocked |  |
|  |  | TT.ExitPointerLock |  |
|  | [帧率设置](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/drawing/set-frame-rate) | TT.SetPreferredFramesPerSecond |  |
| 支付 | [小游戏支付简介](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-request-game-payment) |  |  |
|  | [接入流程](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/payment/access-process) |  |  |
|  | [支付请求](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/payment/payment-request) | TT.RequestGamePayment |  |
|  |  | [TT.OpenAwemeCustomerService ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/open-ability/customer-contact) |  |
|  | [游戏金币（仅抖音Lite）](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/payment/game-coins-lite) | TT.RequestGoldOrder |  |
|  | [获取游戏币余额](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/acquire-mini-game-coin-balance) |  |  |
|  | [游戏币扣除接口](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/mini-game-coin-deduction-interface) |  |  |
|  | [游戏币赠送接口](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/mini-game-coin-gift-interface) |  |  |
|  | [支付签名生成算法](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/payment-signature-generation-algorithm) |  |  |
|  | [服务端回调接口](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/payment-server-callback) |  |  |
| 抖音云模块 | [抖音云](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/douyin-cloud-module/dycloud) | TT.CreateDouyinCloud |  |
|  |  | TTDouyinCloud | TTDouyinCloud.CallContainer |
|  |  |  | TTDouyinCloud.GetTempFileUrl |
|  |  |  | TTDouyinCloud.DeleteFile |
|  |  |  | TTDouyinCloud.UploadFile |
|  |  |  | TTDouyinCloud.DownloadFile |
|  |  |  | TTDouyinCloud.CloudDb |
| 邀请模块 | [邀请模块](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/invite-module/invite) | TT.CreateInvitePanel |  |
|  |  | TT.OnInviteStateChanged |  |
| PlayerPrefs | [PlayerPrefs](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/playerprefs/playerprefs) | TT.PlayerPrefs |  |
|  |  | PlayerPrefs.SetInt |  |
|  |  | PlayerPrefs.GetInt |  |
|  |  | PlayerPrefs.SetFloat |  |
|  |  | PlayerPrefs.GetFloat |  |
|  |  | PlayerPrefs.SetString |  |
|  |  | PlayerPrefs.GetString |  |
|  |  | PlayerPrefs.HasKey |  |
|  |  | PlayerPrefs.DeleteKey |  |
|  |  | PlayerPrefs.DeleteAll |  |
|  |  | PlayerPrefs.Save |  |
| 调试工具 | [调试工具](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/debug-tool/debug-tool) | TT.EnableTTSDKDebugToast |  |
|  |  | TT.RegisterCommandEvent |  |
| 系统字体 | [系统字体](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/startup/unity-webgl-font) | TT.GetSystemFont |  |
