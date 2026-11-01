---
title: "开发小游戏"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/develop
update_time: 2026-02-27
---

## 一、下载安装开发者工具
开发者可以在[开发者工具下载](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/developer-instrument-update-and-download)，根据所使用的操作系统选择相应的版本下载安装。安装完成后即可打开小程序开发者工具，目前支持手机登录和邮箱登录。
- 更多操作指南可以参考小游戏[小游戏开发辅助](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/development-assistance/mini-app-developer-instrument/)。
- 小游戏支持的能力可查看[官方开发文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/log-in/tt-login)。
- 有任何关于开发者问题可通过右下角「开发者助手」咨询，或通过[问题反馈渠道](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/contactus/feedbacks)咨询。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/7777ffc664064d518ae8a444120f3b7b)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/566826c0e85149aa844bb5b2c1a69317)

## 二、开发小游戏
在开发者工具登录平台账号后，点击「**创建一个小程序**」，即可新建工程。根据提示设置项目类型、 工程目录、工程名称、appID（查看「**开发者平台** -> **开发管理** ->**开发设置**」）。点击「**确认**」，进入编译主界面。
一站式开发小游戏后端服务：
[**抖音云**](https://cloud.douyin.com/?from=doc-minigame)[托管](https://cloud.douyin.com/?from=doc-minigame)提供小游戏后端服务托管，打造稳定性更高、安全性更强的服务。同时帮助降低开发门槛，提供一站式开发体验。
- 场景1：一行代码实现将游戏进度进行云端存档，杜绝用户投诉。详情可查看 [小游戏如何使用云数据库存储用户游戏进度](https://developer.open-douyin.com/docs/resource/zh-CN/developer/tools/cloud/scene/deploy/mini-game-how-to-use-cloud)。
- 场景2：一体机式的后端服务开发体验，弹性免运维，轻松应对游戏爆量。
- 场景3：小游戏前端请求小游戏服务端免登录，小游戏服务端请求开放能力免鉴权，提升研发效率。

> **注意**
> - 游戏引擎：目前小游戏支持主流游戏引擎，Cocos，Laya 以及 Egret。开发者在游戏引擎中开发完成后，发布时选择发布到小游戏，即可在字节跳动平台运行。此外，如果开发者不依赖游戏引擎，需要将工程文件打包成小游戏，目录结构需与平台保持一致，包含 `project.config.json` 和 `game.json` 即可运行。
> - 游戏能力：上线前需接入[必接能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/-retention/sidebar)。平台支持缓存后离线打开小游戏，厂商可根据需求适配离线运行功能。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d38d84c97b054bffb8a00b878442716a)

目前支持两种编译预览方式：
- **IDE 预览**：当小游戏代码发生变动后会自动触发编译，可以在左侧的游戏界面看到最新的效果。另外开发者也可以手动点击编译按钮，触发编译。
- **真机预览**：点击开发者工具菜单中的「**预览**」按钮，生成预览二维码后，可以用抖音、今日头条、火山等客户端的扫一扫功能，在手机上体验。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/60ae455c0b654d8d9aa5fbf0ce1f1e87)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b23ae717575540d9a6394add5c61242d)

## 三、上传小游戏

> **注意**
> 测试版本最多支持上传 25 个版本。

在开发者工具中开发调试完成后，可以点击【上传】按钮，按流程填写相关信息将游戏内容上传至开发者后台提交审核、发布小游戏。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/11d8722e4e454c96923dd244407c8487)

上传时可以勾选 `选择测试通道` 复选框来选择测试通道，测试通道允许多个测试版本同时存在，方便小游戏的测试。测试完成后开发者可以在开发者后台选择一个测试版本进行提审、发布上线。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/96a090ad5b504c99bf84e62924f70e35)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/c6959f773f0849d7b1c9fcbec060fee0)