---
title: "用户隐私保护"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/user-info/user-privacy
update_time: 2025-09-11
---

## **一、功能介绍**
为规范开发者的用户个人信息处理行为，保障用户合法权益，小游戏平台提供了标准化用户隐私保护指引与标准的隐私授权上报接口。开发者可通过以下指引完善隐私保护指引的配置及曝光、用户授权结果的上报。
#### **二、流程指引**
- **第一步，自我排查是否存在处理用户个人信息的情况**
1. 用户个人信息是指：以电子或者其他方式记录的与已识别或者可识别的自然人有关的各种信息，不包括匿名化处理后的信息，例如用户昵称、头像、手机号、朋友关系等。涉及小游戏平台为小游戏开发者提供的涉个人信息标准API范围详情可见2.1。
1. 处理行为：包括但不限于个人信息的收集、存储、使用、加工、传输、提供、公开、删除等。
- **第二步,   配置隐私政策**：无论是否处理用户个人信息，都应当前往配置隐私政策，进入控制台 => 小游戏 => 基础设置 => 小游戏隐私政策=> 去完善

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/a4ba0960f2c84b418451424d8f56e039~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/dfeba2419b43441eab3361fe650d1103~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/0b2e77c5258f4bd3b895b77501fe5938~tplv-9nona0m7ha-image.image)

##### **2.1.2 非标准API处理用户个人信息**
泛指游戏内所有通过非 tt API 的方式处理用户个人信息的行为。如游戏内通过自定义表单处理用户个人信息，需要开发者自行适配，并在处理用户信息之前的任意时机通过调用接口请求用户同意隐私政策。
##### **2.1.3 用户隐私保护声明**
以上两类方式处理的用户个人信息均需要在《用户隐私保护指引》中进行合规披露。即使用对应的小游戏账号登录抖音开发者后台（后文简称抖开），在“设置-基本设置-小游戏隐私政策”中完成小游戏隐私政策的填写

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/456eab21ed7044a9939332f63a73813d~tplv-9nona0m7ha-image.image)

**注意**：
通过非标准API的方式处理用户个人信息的行为也需要进行声明，即通过“**添加其他权限**”进行披露。

##### 2.1.4 提前查询授权
  详见[tt.authorize](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/authorization/tt-authorize)
  
| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| scope.userInfo | string | 是否授权用户信息 | 1.3.0 |
| scope.userLocation | string | 是否授权地理位置 | 1.3.0 |
| scope.record | string | 是否授权麦克风功能 | 1.3.0 |
| scope.album | string | 是否授权保存到相册 | 1.3.0 |
| scope.camera | string | 是否授权摄像头 | 1.3.0 |
| scope.screenRecord | string | 是否授权录屏，默认为开。在 onError 里面报错到没有录屏权限时，可以尝试主动调用 | 1.3.0 |
| scope.calendar | string | 是否授权向系统日历添加事件 | 1.3.0 |
| scope.gameClub | string | 是否授权获取游戏站数据 | 3.77.0 |
| scope.groupTag | string | 是否授权使用群聊标签 | 3.78.0 |

  
  **注意**：**若使用到上述接口，建议兼容用户拒绝授权信息的情况，避免影响用户线上体验。**

// game.json
{
officialPrivacyAuthorizationShowingGap: 60 // 隐私弹窗组件最小间隔时间，单位s
}

// 调用wx.requirePrivacyAuthorize拉起自定义隐私弹窗
// 若用户已同意且隐私政策无变更则直接跳过用户确认阶段进入success回调，否则需要拉起隐私弹窗，请求用户确认（通过调用wx.onNeedPrivacyAuthorization注册的回调函数来拉起自定义的隐私弹窗），用户同意后才进入success回调

wx.requirePrivacyAuthorize({
success: res => {
// 进入success回调说明用户已同意隐私政策
// TODO：非标准API的方式处理用户个人信息
},
fail: () => {
// 进入fail回调说明用户拒绝隐私政策
// 游戏需要放弃处理用户个人信息，同时不要阻断游戏主流程
},
complete()
})

wx.onNeedPrivacyAuthorization(resolve => {
// ------ 自定义设置逻辑 ------
// TODO：开发者弹出自定义的隐私弹窗（如果是勾选样式，开发者应在此实现自动唤出隐私勾选页面）
// 页面展示给用户时，开发者调用 resolve({ event: 'exposureAuthorization' }) 告知平台隐私弹窗页面已曝光
// 用户表示同意后，开发者调用 resolve({ event: 'agree' }) 告知平台用户已经同意，resolve要求用户有过点击行为。
// 用户表示拒绝后，开发者调用 resolve({ event: 'disagree' }) 告知平台用户已经拒绝，resolve要求用户有过点击行为。
// 是否需要控制间隔以及间隔时间，开发者可以自行实现
// 勾选样式应以用户确认按钮的点击为准，无需每次勾选都上报
// 如果需要主动弹窗见wx.requirePrivacyAuthorize
})

// 弹窗界面需带上《隐私保护指引》的链接，点击后调用wx.openPrivacyContract打开指引详情

wx.openPrivacyContract({
success: () => {}, // 打开成功
fail: () => {}, // 打开失败
complete: () => {}
})

// 调用wx.requirePrivacyAuthorize拉起弹窗组件
// 若用户已同意且隐私政策无变更则直接跳过用户确认阶段进入success回调，否则需要拉起隐私弹窗，请求用户确认，用户同意后才进入success回调

wx.requirePrivacyAuthorize({
success: res => {
// 非标准API的方式处理用户个人信息
},
fail: () => {},
complete: () => {}
})
