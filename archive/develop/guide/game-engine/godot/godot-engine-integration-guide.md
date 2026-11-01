---
title: "接入指引"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/godot/godot-engine-integration-guide
update_time: 2025-12-15
---

## 接入流程概览

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/e7d78e4f828a497fb3b5d0670fe2dfe0~tplv-9nona0m7ha-image.image)

## 一、前期准备
### 入驻与备案

> **接入抖音小游戏**之前请**阅读下述材料**，进入开发前需要先完成**小游戏的入驻和创建**（获得 App Id），游戏上线前需要完成**小游戏接入**和**备案申报**。

- [了解抖音小游戏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/introduction)
- [注册与入驻](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/register)
- [创建与信息完善](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/improve-information)
- [小游戏备案申报](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/game-filing-application-works)
- [ICP 备案指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/icp-filings)
- [ICP 备案变更及注销](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/icp-change)

### 引擎版本

> 目前抖音小游戏仅支持**特定版本的 Godot 引擎**（不支持自定义），未来可能会逐渐扩大适配范围。请在开发前选择合适的版本，或迁移到对应的版本。

目前支持的 Godot 引擎版本如下：
- **Godot 4.5（推荐）**

## 二、小游戏适配

> Godot 在**以小游戏的形式运行**与 PC Web 等其它平台有一些**差异和限制**，需要开发者**自行完成上层适配（**例如触摸操作、基于WebGL2渲染等）。

### 兼容性一览

> 小游戏运行环境目前以**移动端 Web **为基准，请先完成移动端 Web 环境的适配（即可以在手机浏览器运行）。

| 类别 | 条目 | 移动端Web | 抖音小游戏 |
| --- | --- | --- | --- |
| **系统特性** | Graphic API | WebGL2.0 | WebGL2.0 |
|  | TCP/UDP | 不支持 | 不支持 |
|  | 多线程 | 可选 | **不支持** |
| **引擎特性** | GDExtension | 可选 | **暂不支持** |
|  | gdscript | 支持 | 支持 |
|  | C# 及其他语言 | 不支持 | 不支持 |
| 渲染 | 渲染器 | Compatibility | Compatibility |
|  | 纹理格式 | 支持 ASTC/ETC2 | 支持 ASTC/ETC2 |
|  | OcclusionCulling | 不支持 | 不支持 |
| 音频 | Audio Player | 基于 AudioWorklet | 基于 ScriptProcessor 部分旧版本不支持 STREAM 模式 |
| 输入 | 键盘 | IME / VirtualKeyboard | 仅 VirtualKeyboard |
|  | 麦克风 | 支持 | **暂不支持** |
| 文件 | FileAccess | 基于 indexDB | 支持包内目录（只读） 支持用户目录（`user://`）（读写） |
| 网络 | HttpRequest | 支持 | 支持 |
|  | WebSocket | 支持 | 支持 |
|  | WebRTC | 支持 | **暂不支持** |
| 其他 | Remote Debugger | 支持 | 支持 |
| **用户界面** | 屏幕大小 |  | 需要适配 |
|  | 安全区域 |  | 需要适配 |
|  | 横竖屏 |  | 暂时仅竖屏 |

### 适配指引

> **详细适配方案请参考文档：**[**抖音Godot小游戏适配指引**](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/godot/adaptation-checklist)

## 三、小游戏接入

> 平台提供** Godot 开发者插件**方便开发者**接入抖音开放能力**，并将项目**导出为小游戏格式**发布到抖音。
> **详细使用说明请参考文档：**[**抖音Godot小游戏SDK使用说明**](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/godot/sdk-usage-guide)

### 开放能力

> 开发者可以从 gdscript **通过 SDK **提供的接口**调用平台提供的开放能力**。

开放能力介绍：（**推荐接入**）
- [商业化激励再得能力介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/rewardagainintroduce)
- [「必接」侧边栏复访能力技术指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/Introduction-for-tech)
- [订阅消息能力介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/introduce)

如果游戏有后端能力需求，可以查看[抖音云](https://cloud.douyin.com/?from=doc-minigame)提供的一站式后端服务托管能力。

### 构建与测试

> 开发者完成功能开发和接入后，**通过 Godot 开发者插件导出抖音小游戏项目**，并通过**抖音开发者工具**进行项目的调试和上传。

抖音开发者工具请参考：
- [抖音开发者工具 - 概览](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/mini-app-developer-instrument)
- [抖音开发者工具 - 下载](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/developer-instrument-update-and-download)
- [抖音开发者工具 - 调试控制台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/game-debug/v-console)
- [抖音开发者工具 - 真机调试](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/game-debug/real-machine-adjust)
- [抖音开发者工具 - 版本上传](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/mini-app-developer-instrument#a0e1724d)
## 四、提审和发布
请参考：
- [版本提审指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/examineguide)
- [发布小游戏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/release)

## 五、线上运营
请参考：
- [运营指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/operationalguidelines)
- [运营文档站](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/user-service/user-feedback-guide)

## 六、联系我们
**路径一：**

[开发者平台](https://microapp.bytedance.com/)-点击右下角「开发者助手」- 描述问题；
客服工作时间：周一至周日 10:00-19:00

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/1efbbb43a6424295bddfa447c1e9bad5~tplv-9nona0m7ha-image.image)

**路径二：**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/9e1ae75af26f49219ffe81205ae2ea7c~tplv-9nona0m7ha-image.image)

抖音小游戏-开发者官方**技术**交流群

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/36d802819f3b43f09da258f49274deac~tplv-9nona0m7ha-image.image)

抖音小游戏-开发者官方**运营**交流群
