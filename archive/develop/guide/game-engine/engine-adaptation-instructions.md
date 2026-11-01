---
title: "小游戏平台引擎适配说明"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/engine-adaptation-instructions
update_time: 2026-02-10
---

## 一、概述
抖音小游戏平台面向多样化的游戏开发需求，构建了统一的小游戏运行与发布体系，支持开发者使用不同游戏引擎或技术方案进行开发，并以一致的平台能力完成构建、发布与运行。
小游戏平台并不直接绑定具体的游戏引擎，而是以**引擎构建产物**作为接入与运行的基础。不同游戏引擎在完成开发后，会生成对应形态的小游戏产物，由平台统一承载并运行。
目前，平台已完成对多种主流游戏引擎及技术方案的适配，包括但不限于[Unity](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/sc_access_guide)、[Cocos](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/cocos-laya-egret)、[Godot](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/godot/godot-engine-integration-guide)、[Laya](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/cocos-laya-egret)、[Egret](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/cocos-laya-egret)。开发者可根据自身技术栈和项目需求，选择合适的引擎进行小游戏开发，并按平台规范完成构建与发布。
**游戏引擎&平台实现方式**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/c223c835a8e24353a03eed4face5751e~tplv-9nona0m7ha-image.image)

在这一统一体系下，平台对不同引擎方案提供一致的基础能力支持。开发者可根据项目需求选择合适的引擎或技术方案，并在符合平台规范的前提下，对小游戏所使用的引擎方案进行调整。

## 二、引擎切换方式说明
在平台的统一架构下，不同游戏引擎生成的小游戏产物，均通过平台基座完成构建、发布与运行。基于这一体系，平台支持开发者在符合规范的前提下，对小游戏所使用的引擎方案进行调整。
#### 1. 从普通小游戏引擎切换至Unity引擎的方案
当小游戏当前使用的是普通小游戏引擎（非 Unity），并计划切换为 Unity 引擎的实现方式时，需满足以下要求：
- 使用Unity引擎完成开发
- 使用 [Unity新包体格式](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/unity-new)打包
- 按对应规范生成小游戏产物并上传发布
该构建方式用于确保 Unity 引擎产物能够与平台现有小游戏体系保持一致的产物规范和运行方式。

---

#### 2. 从 Unity 引擎切换至普通小游戏引擎
当小游戏当前基于 Unity 引擎实现，并计划切换为普通小游戏引擎方案时：
- 使用目标引擎完成开发
- 按普通小游戏引擎的构建规范生成产物
- 直接上传对应产物并发布即可
在该场景下，无需额外配置或特殊构建方式，平台将按普通小游戏引擎产物进行识别和运行。

---

#### 3. 切换为包含 Unity 引擎的「混合引擎」方案
在部分场景下，开发者可能希望在同一小游戏中，同时使用 Unity 引擎与其他引擎或技术方案进行实现。此时，可采用**包含 Unity 引擎的组合式实现方式**。
在该场景下，需满足以下要求：
- 所使用的 Unity 引擎需使用[**Unity新包体格式**](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/unity-new)打包
- 按组合式产物规范完成构建与上传
通过该方式，不同引擎或技术方案生成的产物可在同一小游戏中协同运行：
1. **unity游戏利用非unity首包提升启动速度**：纯unity游戏可通过混合非unity轻量级引擎首包的方式，大幅优化整体启动耗时，进而显著提升启动渗透；
1. **非unity游戏新增unity副玩法丰富游戏体验**：支持非unity引擎的小游戏部分玩法模块迁移为unity实现，提升复杂场景下的建模表现和渲染质量。
> 注：组合式实现方式用于满足复杂项目的架构需求，开发者可根据实际情况选择是否采用。
## 三、混合引擎改造案例实践

> 「混合引擎」是平台推出的进阶拓展能力，基于平台[Unity新包体格式打造](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/unity-new)，支持开发者在同一个小游戏包体中，同时集成并上传多种不同引擎（如Unity、Cocos等）开发的产物，实现多引擎技术优势的融合复用。

本实践案例选取了一种**典型的混合引擎使用场景（Unity+Cocos）**作为示例，用于说明在当前平台规范和能力约束下，不同引擎产物在同一小游戏中的组织方式，以及在接入和适配过程中可能涉及的一些处理思路和注意事项。
### 改造目标
在该示例中，目标是将由不同引擎构建的小游戏产物整合到同一个包体中，并确保其能够在平台环境下正常加载和运行。
改造完成后，Unity 与 Cocos 的游戏产物均位于小游戏包体的根目录顶层。当前平台能力下，暂不支持将 Unity 产物放置在指定子目录中。
#### 最终产物结构示例
最终产物结构如下所示，其中高亮部分为 Unity 原 WebGL 构建产物，其余为 Cocos 构建产物。部分配置文件为两者共用，例如 `project.config.json`、`game.json` 等。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/83362b7a2bcb4ed5bed9c9515b460ba5~tplv-9nona0m7ha-image.image)

### 改造过程
#### 初始状态
在未进行混合引擎改造前，不同引擎的产物分别独立存在，结构示例如下：

| cocos | unity |
| --- | --- |

#### 修改unity game.js
这里以cocos拉起unity游戏为例，因此需要保持cocos的game.js文件不变，修改unity的game.js，改动点如下

| 创建 Unity 原 `game.js` 的副本，命名为 `gameMix.js`，用于后续处理。 |  |
| --- | --- |
| 在 `gameMix.js` 中，对 `main` 函数的入口进行调整，增加参数，用于接收外部传入的 canvas。 |  |
| 在文件末尾取消 `main` 函数的立即执行方式，将其导出，等待由外部逻辑触发。 |  |

#### 拷贝unity必要文件
将 Unity 构建产物中必要的运行文件拷贝至 Cocos 项目中，确保文件命名不产生冲突。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/c7d0fd0ebc24468ab42250b0bb33467c~tplv-9nona0m7ha-image.image)

#### 修改Cocos的game.json
在 Cocos 的 `game.json` 中，引入 Unity 相关的子包及插件配置，以确保 Unity 产物能够被正确加载。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/0704436af8fe45698522ccd242a1f055~tplv-9nona0m7ha-image.image)

#### 修改Cocos框架代码，解决全局变量冲突
在部分场景下，Cocos 对全局对象（如 `document`、`window` 等）存在封装或限制，这可能影响 Unity 对相关对象的修改与使用。因此需要根据实际情况，对 Cocos 框架代码进行适配处理。
以下示例基于一个内部 Demo，仅用于说明可能的处理思路，具体实现需结合项目实际情况进行分析和调整。

| Cocos Canvas 对象处理示例 |  |
| --- | --- |
| 允许 `document`、`window` 等全局变量被覆盖 |  |
| 针对触摸事件的简单处理示例（非最佳方案）：  在 Unity 启动后，由于 Unity 会替换 `document` 对象，可能导致相关逻辑报错。 |  |
| 为便于 Unity 复用屏上 canvas，增加对 canvas 创建过程的监控与共享。同时注入 `startUnity` 全局函数，供 Cocos 侧逻辑调用，用于启动 Unity 游戏。 |  |

#### 从 Unity 拉起 Cocos 样本
在某些场景下，也可能需要从 Unity 启动并切换至 Cocos。整体思路与前述 Cocos → Unity 类似，但在实现细节上存在一定差异，以下重新进行说明，实际代码请根据项目情况灵活调整。
##### 6.1 js代码改动

| 将 Cocos 原有的 `game.js` 重命名为 `gameMixCocos.js`，并将 Cocos 的启动逻辑封装为函数（如 `loadCC`），导出以供外部调用。 |  |
| --- | --- |
| 在新的 `game.js` 中，劫持 `tt.createCanvas`，用于获取屏上 canvas。 |  |
| 同时创建 `startCocos` 全局函数，供 Unity 调用。 | 其中需要注意的点包括： **帧率恢复处理**  Unity 停止运行后，可能会将全局帧率设置为较低值（如 1），导致 Cocos 启动后画面卡顿。可在下一个事件循环中尽快恢复帧率。 **首屏 canvas 复用问题**`firstScreenCanvasForCocosWrapper` 会在后续步骤中使用，用于确保在 Unity 已占用屏上 canvas 的情况下，Cocos 能够正确获取并复用该 canvas。 |
| 在 Cocos 的 canvas wrapper 中，对首屏 canvas 创建逻辑进行适配处理。 | 由于先启动了unity，unity先拿到了屏上canvas，cocos canvas wrapper中直接调用tt.createCanvas是拿不到屏上canvas的，这里做了一点trick改动，让它能拿到真正屏上canvas（firstScreenCanvasForCocosWrapper）。 |

##### 6.2 C#改动

| 在 Unity 的 C# 代码中，增加停止当前游戏的逻辑。 |  |
| --- | --- |
| 同时在 Unity 工程中添加 `jslib`，以支持从 C# 调用 JavaScript 中定义的全局函数，从而启动 Cocos。 |  |
| 在合适的时机，通过 `jslib` 调用对应的 JS 接口，启动 Cocos 游戏，并停止 Unity 的运行。 |  |

## 注意
- 不建议将 Unity 项目文件直接引入 Cocos 工程中参与编译。Unity 构建产物中的 `require` 实现可能与 Cocos 编译过程中的 `require` 机制产生冲突。更推荐的方式是直接处理双方的最终构建产物，通过全局对象或约定接口进行交互。
- 当前 Unity 游戏启动时，会注入部分 polyfill 对象以模拟 Web 环境，可能与开发者自身环境存在冲突。目前已知的 polyfill 对象包括：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/169522e2a02346f9993df557b71c9a42~tplv-9nona0m7ha-image.image)

抖音 unity polyfill 全局对象
