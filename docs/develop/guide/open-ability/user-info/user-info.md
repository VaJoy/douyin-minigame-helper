---
title: "用户信息获取"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/user-info/user-info
update_time: 2025-08-25
---

用户信息指的是抖音用户的昵称、头像、性别等个人信息。
### 首次获取
个人信息是用户的敏感信息,小游戏会对用户信息进行严格的保护，开发者仅在用户同意授权的情况下才能进行下述 API 的使用：
- [tt.getUserInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/info/tt-get-user-info)
- [tt.getLocation](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/location/tt-get-location/)
- [tt.getRecorderManager.start](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/record/tt-get-recorder-manager/)
- [tt.saveImageToPhotosAlbum](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/picture/tt-save-image-to-photos-album/)
- [tt.saveVideoToPhotosAlbum](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/video/tt-save-video-to-photos-album/)
- [tt.scanCode](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/scan-code/tt-scan-code/)
- [tt.chooseImage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/picture/tt-choose-image/)
- [tt.chooseVideo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/video/tt-choose-video/)
- [tt.requestMicrophone](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/mircophone/tt-request-microphone/)
- [tt.getGameRecorderManager](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/screen-recording/tt-get-game-recorder-manager/)
- [tt.addPhoneCalendar](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/calendar/tt-add-phone-calendar)
### 已授权的情况下获取

如果用户已经授权过个人信息给小游戏，开发者可以把用户的个人信息记录在业务后台。但用户有可能修改昵称头像，为了保证个人信息不出现过期失效的情况，需要再次获取用户信息，因此可以提前使用[tt.authorize](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/authorization/tt-authorize)进行判断，然后使用[tt.getUserInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-api/info/tt-get-user-info)获取用户信息
### 已拒绝的情况下获取

除非用户手动在设置页中点击授权 —— 该次调用会直接进入 fail 回调。用户之后如果又通过设置页修改了授权，再次调用结果也会随之变化。
录屏权限默认为开启。

### 推荐的使用方式
先使用[tt.login](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/open-interface/log-in/tt-login)获取 code，同时调用[tt.getUserInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-api/info/tt-get-user-info)获取用户信息
