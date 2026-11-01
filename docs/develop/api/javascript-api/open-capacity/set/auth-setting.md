---
title: "AuthSetting"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/set/auth-setting
update_time: 2025-12-05
---

| 名称 | 类型 | 对应接口 | 描述 |
| --- | --- | --- | --- |
| scope.userInfo | boolean | tt.getUserInfo | 是否授权用户信息 |
| scope.userLocation | boolean | tt.getLocation | 是否授权地理位置 |
| scope.record | boolean | tt.getRecorderManager.start | 是否授权录音功能 |
| scope.album | boolean | tt.saveImageToPhotosAlbum tt.saveVideoToPhotosAlbum | 是否授权保存到相册 |
| scope.camera | boolean | tt.scanCode tt.chooseImage tt.chooseVideo | 是否授权摄像头 |
| scope.screenRecord | boolean | tt.getGameRecorderManager | 是否授权录屏，默认为开。在 onError 里面报错到没有录屏权限时，可以尝试主动调用 |
| scope.calendar | boolean | tt.addPhoneCalendar | 是否授权添加日历事件 |
| scope.gameClub | boolean | tt.getGameClubData | 是否授权获取游戏站数据 |
| scope.groupTag | boolean | 无 | 是否授权使用群聊标签 |
