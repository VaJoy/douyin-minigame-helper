---
title: "线上调试彩蛋页"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/game-debug/bonus-scene
update_time: 2025-06-16
---

**支持 App 版本： **
**抖音 iOS: 27.3.0 以上版本**
**抖音 Android: 27.1.0 以上版本**

> **注意**
> 如果抖音号在控制台测试账号中被删除，会自动关闭`全入口打开指定版本小游戏`功能。
> 如果“扫码指定”的版本过期，系统会自动关闭`全入口打开指定版本小游戏`功能。
> 如果“测试版本”被删除或提交审核，会自动关闭`全入口打开指定版本小游戏`功能。

小游戏开发过程中会遇到一些线上的异常问题无法排查，包括从线上的某个入口进入时，小游戏异常，但是线下扫码时候并没有问题等场景。

## 彩蛋页的作用
我们可以在彩蛋页中打开`全入口打开指定版本小游戏`的入口。打开之后，重启抖音 App，从任何入口进入小游戏，访问的都是指定版本小游戏，我们可以用此方法在抖音主端的各个入口调试小游戏。

## 彩蛋页的打开方法
### 加入测试设备
1. 登录 [开发者运营平台](https://developer.open-douyin.com/)。
1. 打开【控制台】- 【xxx 小游戏详情】-【开发】-【开发设置】-【测试管理】，使用抖音扫码加入测试账号。
1. 每个应用可以添加不超过100台测试设备。
1. 为了方便你管理设备，建议为测试设备手动添加“备注”信息。
注意:
- 加入新的小游戏测试账号时，抖音版本需大于等于 27.1.0。
- 按原先 did 方式已加入调试设备的旧版本抖音不受影响。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/af019340656d479a9f14ebb141cbd3bf~tplv-9nona0m7ha-image.image)

### 指定小游戏版本
1. 加入测试设备后，在抖音客户端中点击【我】- 底部【更多功能】，在底部找到 【开发者模式】并点击，进入开发者模式页面。首次加入测试账号时系统会自动引导跳转到该页面。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f705948f31fb404eaa9686f3adbf1a0e)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d0a3e424422e43529858d6ad654437f8)

1. 打开【开发者模式】开关（Android版需要重启才能生效）。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e9c3174f5bc84571aaedf4c8acfd2181)

1. 点击需要指定版本的小游戏，进入详情页。打开【全入口打开指定版本小游戏】的开关。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/847c75757660426bbb42844f94e3639a~tplv-9nona0m7ha-image.image)

1. 选择“IDE上传的测试版本”或者“扫码选择指定版本”。
  - 如果选择“IDE上传的测试版本”，将会加载控制台“版本管理”页面上的“测试版本”。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/6713313b44cf4f3d923564e3144ad055~tplv-9nona0m7ha-image.image)

  - 如果选择“扫码选择指定版本”，则可以扫描IDE上的“预览”二维码。（只支持“预览-->扫码预览”）。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/8c711bfca25b49768cee0d8a56c802e3~tplv-9nona0m7ha-image.image)

1. 完成以上设置后，退出抖音。再次开启抖音后，从任何入口点击进入小游戏，则都是你刚才指定的版本了。
