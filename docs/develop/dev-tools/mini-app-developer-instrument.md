---
title: "概览"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/mini-app-developer-instrument
update_time: 2025-10-21
---

## 登录
抖音开发者工具支持开发者使用**手机**、**邮箱**或**抖音扫码**登录。
如果没有注册过，可以先到[抖音开放平台官网](http://developer.open-douyin.com)或抖音 App 注册账号后再登录。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f175f4d17ef845da9084296f6737e0e8)

## 新建项目
当同时满足以下条件时，可点击【+】创建新小游戏。
1. 已拥有一个抖音小游戏的 AppID
1. 所登录的账号是该 AppID 所对应小游戏的开发者

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/9a6b4a8d879347328194b1c676a33ce5)

选择一个空目录，作为工程目录。当选择空目录时，可以选择是否在该目录下生成一个简单的项目。
`AppID` 需要在[小游戏控制台](https://developer.open-douyin.com/console?type=2)获取或者直接使用测试号。

> **注意**
> 测试号只支持预览调试，不支持上传。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4d8c074079aa46e8a5413f3a316f026b)

## 导入项目
在「**小游戏**」界面右上角点击「**导入**」，进入「**导入项目**」界面，然后选择合适的项目。
如果目标目录指向的是合法的抖音小游戏项目，【项目名称】和【AppID】将会被自动填充。如果没有自动填充，只需手动填写【项目名称】和【AppID】，即可将已有项目导入到 IDE 中打开。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b04d0b462cb14b8298801c5afc7384d1~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/de406841b58041db8f65b3e542466ba0~tplv-9nona0m7ha-image.image)

## 管理项目
右键单击项目可以对本地项目进行管理。
- 选择「**删除**」可以移除项目
- 选择「**删除工程及目录**」可以删除项目及本地目录。
- 选择「**使用完整模式打开**」或者「**使用 Lite 模式打开**」即可使用特定模式打开当前项目。

> **说明**
> 删除操作只会在项目列表中移除该项目，并不会删掉对应的项目文件。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/a4f971beaf6d4b4580c8ffaec6d1681b~tplv-9nona0m7ha-image.image)

## 主界面功能介绍
开发者主界面主要由工具栏、模拟器、编辑器、调试器 4 部分组成。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/6d9036e89dfd4a628e2c94bc33fe446d)

### 工具栏
💡 点击「模拟器」、「调试器」、「编辑器」按钮可以隐藏/显示相应的模块，界面中需要至少有一个模块被显示。
- 左侧区域
  - 刷新页面：刷新当前页面
  - 清除缓存：可以清除文件缓存、数据缓存、登录状态和授权数据
  - 编译：编译当前的小游戏项目
  - 预览：生成二维码，预览已上传版本
  - 真机调试：生成真机调试的二维码，开发者使用抖音 App 扫码后即可在Android和iOS手机上进行断点调试。
  - 上传：填入 app 版本号及更新日志，上传小游戏应用内容到服务器
- 右侧区域
  - 详情：展示当前小游戏的 appid、user_id、本地目录、文件系统、基础版本与编译版本，并可以设置是否校验网络请求的域名白名单

### 模拟器
模拟器可以模拟小游戏在客户端真实的逻辑表现，对于绝大部分的 API 均能够在模拟器上呈现出正确的状态。开发者可以选择不同的设备，调试小游戏在不同尺寸机型上的适配问题。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/aa1eb7d37dfc4593b141bfb2e222efd6)

### 编辑器
编辑器模块内可以对当前项目进行代码编写和文件的添加、删除以及重命名等基本操作，并集成了 Git、插件等功能。
- 文件格式：因 iOS 下仅支持 UTF8 编码格式，最新版本的开发者工具会在上传代码时对代码文件做一次编码格式校验
- 文件支持：工具目前可以支持市面上大部分文件类型的编辑以及图片文件的预览
- 目录树：可以查看当前项目的目录结构
### 调试器
调试器包含如下功能模块：
- Console panel：开发者可以在此调试代码。
- Sources panel：Sources panel 用于显示当前项目的脚本文件，同浏览器开发不同，小游戏框架会对脚本文件进行编译的工作，所以在 Sources panel 中开发者看到的文件是经过处理之后的脚本文件，开发者的代码都会被包裹在 define 函数中，并且对于 Page 代码，在尾部会有 require 的主动调用。
- Network panel：Network Panel 用于观察和显示 request 和 socket 的请求情况。
- Storage panel：可以查看 Storage 存储情况。
### 自定义编译条件
编译条件会读取 project.config.json 中的 condition 字段下的相关配置，方便导入编译条件。点击工具栏的普通编译处，在下拉列表中，点击添加编译模式，会弹出填写编译条件窗口，添加自己的定制化的编译条件。在弹出的窗口中，添加模式名称，启动页面，启动参数（即通过 tt.getLaunchOptionsSync 获取的启动参数）以及进入场景几个字段，点击确认，生成新的编译条件。
**工具快捷键：**
- Command + B（Windows: Ctrl + B）：主动触发编译
- Command + R（Windows: Ctrl + R) ：焦点在编辑器时，触发模拟器刷新，焦点在其他位置时，触发整个工作区刷新 。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/42445527b1eb42df97d861171ce01862)

## 上传提审
**注意：平台新增审核预检，将基于接入规范检测游戏代码包中是否存在潜在驳回问题或缺失重点能力，帮助提高版本审核通过率。**
点击工具栏的“上传按钮”，填写版本号及更新日志，进入审核预检与上传流程。
**小游戏版本号规范建议：**
主版本号.子版本号 [.修正版本号]；
英文对照：Major_Version_Number.Minor_Version_Number[.Revision_Number]；

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4b0c930141214bf29438a0b7a4ff95e8)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/5339ff17c11d4091952435bae30f973b)

1. 审核预检项目：将检测游戏内是否接入必接能力、重点推荐能力。**若未接入必接能力，将导致版本上传失败**；若未接入重点推荐能力，平台不会拦截版本上传，但会提示未接入重点能力。

| **能力类型** | **能力清单** | **未接入是否会拦截上传** | **检测原因** |
| --- | --- | --- | --- |
| 必接能力 | 侧边栏复访能力：点击查看[接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/-retention/sidebar) | 会 | 侧边栏复访能力能带动小游戏大盘整体留存提升，平台要求所有小游戏都接入该能力。 |
| 重点推荐能力 | 添加至桌面：点击查看[接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/shortcut/add-shortcut) 订阅消息：点击查看[接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/subscribe-message/tt-request-subscribe-message) 支付能力：点击查看[接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-request-game-payment/) 广告能力：点击查看[接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/tt-create-banner-ad) | 不会； 会提示未接入重点能力 | 添加至桌面、订阅消息能力能提升游戏留存，建议开发者接入；且有计划或正在进行广告投放的游戏，只有接入这些能力后才能获得商业化广告金； 支付能力、广告能力作为游戏的变现能力，推荐所有具备相应资质的游戏都接入。 |

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/6a6277be3382476f88d9b95fb2a4b20a)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/f2b5ae5086ea445f95c1fe56edbbb278)

1. 审核预检原理：
预检审核将检测开发者代码js文件中相关能力的调用。例如，必接能力**侧边栏复访**，要求开发者必须使用`tt.navigateToScene` 调用。其他重点推荐能力类似。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e34b95a091684383a6f2a0e60eae8371)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/36ad9b52f4f240c1a8b7e6893e0a5653)

1. 多版本上传：为满足开发者多项目并行测试的需求，支持最多同时上传 25 个测试版本，上传时分为“默认通道”和“通道1-24”。
   1. 未开启“选择测试通道”时，上传成功后，覆盖“默认通道”已有的测试版本
    
![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/94f50355a20e463283c1aa0423d0f5da)

   1. 开发者如需同时保留多个测试版本，可以开启“选择测试通道” ，并根据需求选择 默认通道 或 通道1 - 24 进行上传。上传成功后，将覆盖所选通道的测试版本。 默认通道 和 通道1 - 24 通道的测试版本互不影响。
    
![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/c78cb009d9dd446abb37caa7438d1a42)

   1. 除开发者工具外，[CLI](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/development-assistance/ide-cli#d6dd6956) 也支持指定测试通道进行上传。
   1. 多测试版本能力只支持抖音、抖音极速版、抖音火山版（>=31.6.0）。如想在其他宿主上测试：
    - 需要保证默认通道上有上传测试版本。
    - 无论扫哪个测试通道的二维码，最终都只会打开默认通道上的测试版本，故请将要扫码体验的测试版本上传到默认通道。
1. 上传成功：上传完成后，进入[抖音小游戏开发者平台](https://microapp.bytedance.com/game/)，在版本管理页面进行版本提审。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/01ae7c3b7d844d75901b9231d43b1c0a)

## Lite模式
更多Lite模式详情请[参考文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/developer-instrument/lite-mode)。
## 设置
设置页由以下功能模块组成：
- [通用设置](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/developer-instrument/settings/common)
- [外观设置](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/developer-instrument/settings/outlook-settings)
- [代理设置](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/developer-instrument/settings/proxy-settings)
- [调试设置](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/developer-instrument/settings/debug)
- [快捷键设置](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/developer-instrument/settings/shortcuts)
- [编辑器设置](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/developer-instrument/settings/edit)
