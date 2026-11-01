---
title: "更新日志"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/basic-library/update-log
update_time: 2025-03-31
---

## 版本及更新内容
### 3.65.0
2025-03-31
- game.json 新增 plugins 预留字段。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/mini-game-configuration)
### 3.55.0
2025-01-02
- 新增 tt.getRealtimeLogManager 接口。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/debugging/tt-get-realtimelog-manager)
- 新增 tt.getLogManager 接口。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/debugging/tt-get-log-manager)
### 3.5.0
2023-11-14
- 新增 setImRankData 接口的 zoneId 字段。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/game-rank/setImRankData)
- 新增 getImRankList 接口的 zoneId 字段。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/game-rank/getImRankList)
- 新增 getImRankData 接口的 zoneId 字段。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/game-rank/getImRankData)
- 新增 setImRankDataInOpenContext 接口的 zoneId 字段。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/game-rank/set-im-rank-data-in-open-context)

### 3.1.0
2023-09-20
- 新增 FileSystemManager.truncate/truncateSync 接口。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-truncate)
- 新增 FileSystemManager.appendFile/appendFileSync 接口。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-append)
- 更新 FileSystemManager.stat/statSync 接口支持递归获取目录下每个文件的stat信息。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-stat)
### 2.94.0
2023-07-26
- 新增 tt.showRevisitGuide 接口，游戏内展示复访引导弹窗。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/collect/favorite/tt-show-revisit-guide)
### 2.92.0
2023-07-19
- tt.onShow 接口支持返回包含 `scene、launch_from、location`的更细粒度入口信息。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-on-show)
### 2.90.0
2023-06-07
- 新增 FileSystemManager.readZipEntry 接口。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-read-zip-entry)
- tt.shareAppMessage 支持抖音系宿主的图文发布能力，新增 picture 类型 channel。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/share-param)
### 2.82.0
2023-02-02
- 新增 小游戏互推组件 能力。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/grid-game-panel/Gamerecommend)
### 2.74.0
2022-11-16
- 激励广告-再得能力开放。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/ads/rewardagainintroduce)
### 2.70.0
2022-10-19
- 优化性能数据上报功能。
### 2.68.0
2022-09-07
- 新增重启API，tt.restartMiniProgramSync。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-restart-mini-program-sync)
### 2.66.0
2022-08-24
- 新增平台提供的小游戏客服能力API。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/customer-contact/openCustomerServiceConversation)
### 2.56.0
2022-06-16
- 抖音桌面快捷方式入口可以细分微端入口，详见 [tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-get-launch-options-sync)
### 2.52.0
2022-05-05
- 新增添加日历事件 API，详见[tt.addPhoneCalendar](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/calendar/tt-add-phone-calendar)
### 2.51.0
2022-04-20
- 新增好友邀请组件，助力游戏快速裂变，详见[分享能力介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/social/all)
### 2.50.0
2022-04-13
- 修复 tt.onGyroscopeChange 多次调用无法停止的问题
- 补充分享逻辑 `title 和 desc`说明，[详见](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/logic)
### 2.49.0
2022-04-06
- 获取地理位置功能优化
### 2.48.0
2022-03-30
- rtc 功能优化
### 2.47.0
2022-03-23
- 支付新增启动场景信息
### 2.46.0
2022-03-16
- 新增`tt.createInteractiveButton` API，支持创建`Native` 按钮，该按钮在录屏时不会被采集
- 支持添加到桌面的相关 API，tt.addShortcut 和tt.checkShortcut。[详情](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/shortcut/add-shortcut)
### 2.45.0
2022-03-09
- 修复 iOS 端 vConsole 的 JS Crash 信息显示不全的问题
### 2.44.0
2022-03-02
- 支持`tt.canIUse`API，[tt.canIUse](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/tt-can-i-use)
### 1.31.0
2019-08-13
- 广告组件支持关闭事件 `bindclose` 属性
- Canvas 支持 `createLinearGradiant` API
### 1.30.0
2019-08-06
- 增加关注头条号 API `followOfficialAccount`
### 1.28.0
2019-07-23
- 小游戏增加 `onMemoryWarning` API
- Web-view 组件支持 `progressbarColor` 属性
- Web-view 组件支持 load 事件
- 新增 `compressImage` API
- 新增 `chooseLocation` API
- 新增 `onUserCaptureScreen` 和 `offUserCaptureScreen` API
- Canvas 新增 `beginPath` 和 `fillRect` API
### 1.27.0
2019-07-16
- 增加背景音 API `getBackgroundAudioManager`
### 1.25.0
2019-07-02
- 小程序增加 API：`getMenuButtonLayout`, `getMenuButtonBoundingClientRect`
### 1.23.0
2019-06-18
- 小游戏新增互跳组件
### 1.22.2
2019-06-18
- 小程序新增互动组件 API（用于 feed 入口评论、点赞场景）
### 1.21.0
2019-06-06
- 修复 input 组件在自定义组件内无法触发 bindinput 的 bug
### 1.20.1
2019-06-04
- 修复 `innerAudio` 在安卓平台从后台切回前台时播放状态异常的问题
- 修复 Text 组件在安卓平台选中后点击页面其他区域无法取消选中的问题
- 修复 Textarea 组件在设置 padding 后高度异常的问题
### 1.20.0
2019-05-27
- 扩展视频裁剪功能，支持自定义裁剪排序并新增相关参数
- 修复 `innerAudio` 在安卓平台切换其他应用后音频仍在播放的问题
- 修复 `downloadFile` 方法在 iOS 和安卓平台表现不一致的问题
