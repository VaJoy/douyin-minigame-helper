---
title: "用户授权"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/basic-function/authorization
update_time: 2025-06-13
---

小游戏会对用户信息进行严格的保护，开发者仅在用户授权的情况下才能进行下述 API 的使用：

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

小游戏仅会在 **首次** 调用上述 API 时，弹窗询问用户 —— 若用户允许则正常调用，否则本次调用失败。无论用户允许与否，该授权设置均会出现在小游戏的授权设置页（右上角 - 更多 - 设置）中。用户在之后使用小游戏的过程中，可以手动打开授权设置页，再次修改授权。
如果开发者调用了某个 API 并且用户拒绝了授权，那么下一次开发者调用该 API 时 —— 除非用户手动在设置页中点击授权 —— 该次调用会直接进入 fail 回调。用户之后如果又通过设置页修改了授权，再次调用结果也会随之变化。
其中录屏权限默认为开启。
> ⚠️ 注意
>
> 只有已经提示过用户授权的权限才会出现在授权设置页面内。
>
> 用户授权设置不会与服务器同步，若用户更换设备，或在同一设备上切换账号，则会重新提示授权。
## 获取用户授权设置
开发者可以通过 [tt.getSetting](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/set/tt-get-setting) 获取用户当前的授权状态。
## 打开设置页面
用户可以在设置页面中控制对该小程序的授权状态。开发者可以通过 [tt.openSetting](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/set/tt-open-setting) 打开设置页面，引导用户授权。
## 提前发起授权请求
开发者可以通过 [tt.authorize](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/authorization/tt-authorize) 在调用需授权 API 之前，提前向用户发起授权请求。
## scope 列表

| scope | 对应接口 | 描述 |
| --- | --- | --- |
| scope.userInfo | tt.getUserInfo | 是否授权用户信息 |
| scope.userLocation | tt.getLocation | 是否授权地理位置 |
| scope.record | tt.getRecorderManager.start tt.requestMicrophone | 是否授权麦克风功能 |
| scope.album | tt.saveImageToPhotosAlbum，tt.saveVideoToPhotosAlbum | 是否授权保存到相册 |
| scope.camera | tt.scanCode，tt.chooseImage，tt.chooseVideo | 是否授权摄像头 |
| scope.screenRecord | tt.getGameRecorderManager | 是否授权录屏，默认为开。在 onError 里面报错到没有录屏权限时，可以尝试主动调用 |
| scope.calendar | tt.addPhoneCalendar | 是否授权向系统日历添加事件 |
