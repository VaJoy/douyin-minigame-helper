---
title: "权限"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/basic-function/permission
update_time: 2025-09-11
---

部分接口需要经过用户授权同意才能调用。我们把这些接口按使用范围分成多个 `scope` ，用户选择对 `scope` 进行授权，当授权给一个 `scope` 之后，其对应的所有接口都可以直接使用。
此类接口调用时：
- 如果用户未接受且未拒绝过此权限，系统会弹窗询问用户，用户点击同意后方可调用接口；
- 如果用户已授权，开发者可以直接调用接口；
- 如果用户已拒绝授权，则不会出现弹窗，而是直接进入接口 `fail` 回调。**请开发者兼容用户拒绝授权的场景。**
## 获取用户授权设置
开发者可以使用 [tt.getSetting](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/set/tt-get-setting) 获取用户当前的授权状态。
### 打开设置界面
用户可以在小游戏设置界面（「右上角」- 「更多」 - 「设置」）中控制对该小游戏的授权状态。
开发者可以调用 [tt.openSetting](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/set/tt-open-setting)  打开设置界面，引导用户开启授权。

### 提前发起授权请求
开发者可以使用 [tt.authorize](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/authorization/tt-authorize) 在调用需授权 API 之前，提前向用户发起授权请求。如果用户之前有授权，该接口直接返回成功

### scope 列表

详见[scope列表](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/basic-function/authorization)

| scope | 对应接口 | 描述 |
| --- | --- | --- |
| scope.userInfo | tt.getUserInfo | 是否授权用户信息 |
| scope.userLocation | tt.getLocation | 是否授权地理位置 |
| scope.record | tt.getRecorderManager.start tt.requestMicrophone | 是否授权麦克风功能 |
| scope.album | tt.saveImageToPhotosAlbum，tt.saveVideoToPhotosAlbum | 是否授权保存到相册 |
| scope.camera | tt.scanCode，tt.chooseImage，tt.chooseVideo | 是否授权摄像头 |
| scope.screenRecord | tt.getGameRecorderManager | 是否授权录屏，默认为开。在 onError 里面报错提示没有录屏权限时，可以尝试主动调用 |
| scope.calendar | tt.addPhoneCalendar | 是否授权向系统日历添加事件 |

### 小游戏隐私保护协议

需授权的接口涉及用户隐私，注意查阅[小游戏开发者平台信息保护声明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/agreement-and-norms/privacy-policy)
