---
title: "Lite模式"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/lite-mode
update_time: 2025-05-27
---

## 概述
从 4.1.0 版本开始，我们引入了 Lite 模式。在开发者经常使用外部编辑器（如 VSCode ）的场景下，使用 Lite 模式可以节省内存空间 30%+；在真机调试的场景下，使用 Lite 模式可以简化操作流程。以下内容是关于 Lite 模式的详细介绍。
## Lite 模式功能面板
## 
![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/20230630-143512-8724816077457966.jpeg)

## 开启 Lite 模式
### 使用切换按钮
开发者可以在工程维度选择使用“完整模式”或“Lite 模式”。下载 4.1.0 的新版本后，项目默认仍然以“完整模式”启动，此时打开工作区后，开发者可以点击窗口右上角的“Lite 模式”按钮或模拟器横幅按钮进入 Lite 模式。窗口右上角按钮为常驻按钮，横幅按钮点击后将不再展示。
下面左图为完整模式，右图为 Lite 模式。用户每次重新打开项目时，会延用该工程上一次退出时的模式。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/1-7798303059424072.png)

### 使用设置
如果开发者希望每次新建项目时使用 Lite 模式，可以打开设置并勾选【外观】-【以 Lite 模式打开新工程】

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1687865402345)

### 使用 CLI
若要打开小游戏工程，可以使用 [tt-minigame-ide-cli](https://www.npmjs.com/package/tt-minigame-ide-cli) 工具

```js
tmg open <project-path> --mode=lite
```

### 退出 Lite 模式
在 Lite 模式下，在窗口右上角点击“退出 Lite 模式”可以回到完整模式
## 真机面板
### 使用扫码预览
在工具栏“模拟器/真机”的下拉菜单中，开发者可以选择“真机”切换至真机调试模式。切换后展示效果如下图，此时真机面板处于扫码预览模式

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1687865402258)

或者可使用工具栏的预览按钮预览

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/00fa87aeb35744f2a8969ed634021936)

### 使用扫码调试
在默认状态下打开“开启调试”开关或点击工具栏调试器后，真机面板将处于扫码调试模式。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1687865402675)

建立连接后，真机面板和调试器会分别展示连接状态与调试信息，信息内容与完整模式相同。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1687865402819)

### 使用推送预览
在默认状态下打开“推送至设备”，真机面板将处于推送预览模式。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/2-8989988607185528.png)

在使用抖音扫码建立连接后，开发者有三种方式更新真机中的小程序产物:
1. 点击面板中的“推送并预览”。
1. 点击菜单中的【工具】-【预览】。
1. 使用快捷键（根据设备类型决定，参考菜单中的描述）。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1687865402781)

### 使用推送调试
在默认状态下同时打开“开启调试”和“推送至设备”开关，真机面板将处于推送调试模式。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1687865403077)

建立连接后效果如图

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1687865403201)

在使用抖音扫码建立连接后，开发者有三种方式更新真机中的小程序产物:
1. 点击面板中的“推送并预览”。
1. 点击菜单中的【工具】-【真机调试】。
1. 使用快捷键（根据设备类型决定，参考菜单中的描述）。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1687865403129)

### 局域网调试
在打开“开启调试”开关后，用户可以选择使用“局域网调试”模式。局域网调试功能与操作方法与完整模式相同。
### 默认使用“推送预览”
默认情况下，真机面板会展示“扫码预览”。开发者通过设置将默认表现更改为“推送预览”。设置路径为【设置】-【调试】- 勾选【推送方式】。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1687865403338)

## 模拟器
### 关闭模拟器
开发者在使用真机调试时，如果希望进一步节省空间，可以通过点击下图中的按钮停止模拟器运行。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/3-4260285838697295.5.png)

## 菜单
【工具】菜单的子菜单包含【预览】、【真机调试】和【模拟器】，用于切换不同设备状态

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1687865403494)

## 设置
#### 1.【外观】-【以 Lite 模式打开新工程】
开关打开后，新建工程时将使用 Lite 模式打开工程

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1687865403646)

#### 2.【调试】-【默认真机预览/调试方式】
打开开关后，默认使用推送预览方式在真机中调试

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1687865403527)

## 快捷键

| **功能** | **Mac** | **Windows** |
| --- | --- | --- |
| 切换至模拟器面板 | Shift+Cmd+T | Shift+Ctrl+T |
| 切换真机预览面板 | Shift+Cmd+P | Shift+Ctrl+P |
| 切换真机调试面板 | Shift+Cmd+R | Shift+Ctrl+R |

## 反馈
如果你在 IDE Lite 模式的使用过程中有任何问题，建议与期望，欢迎你使用 IDE 菜单中的【反馈】功能提出宝贵意见。

tma open <project-path> --mode=lite
