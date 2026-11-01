# 引擎适配层的坑（源码核实）

> **适用**：在 Cocos Creator 上跑抖音小游戏时，出现「代码看着没问题、平台文档也都照做了，就是不工作」的现象。
> **源**：工作区内 `cocos-engine-3.8.6/` 引擎源码，逐条给 `file:line`，不是平台文档的转述。**文中引擎路径都相对于 `cocos-engine-3.8.6/`，且写到能唯一定位为止**——同名文件在 `taobao` / `wechat` / `xiaomi` 目录下各有一份，简写会指错文件。
> **关联**：平台判定与能力矩阵见 `cocos-publish.md`；分包与加载见 `config.md`；调优见 `performance.md`；开放数据域见 `social.md`。

引擎在抖音上不是「直接跑」的。`platforms/minigame/platforms/bytedance/` 下有一层 wrapper，把 `document` / `canvas` / `localStorage` / `XMLHttpRequest` / `WebSocket` 全换成 `tt.*` 实现，再对若干引擎行为打补丁：`platforms/minigame/platforms/bytedance/wrapper/engine/index.js` 挂了 `fs-utils`、`VideoPlayer`、`Label` 三个抖音专属补丁，并引入小游戏通用补丁 `platforms/minigame/common/engine/index.js`（`Editbox`、`AssetManager`）。下面这些坑全部来自这两层，平台文档不会写。

## 现象 → 根因 → 处置

| 现象 | 根因 | 处置 |
|---|---|---|
| `onPlay` 回调了，但还是听不到声 | 抖音的 `onPlay`/`onPause`/`onStop`/`onSeeked` 是引擎**同步伪造**的 | 别拿 `onPlay` 判断真的出声，见第一节 |
| 偶尔某个音效永远没声、控制台无报错 | 音频加载有 **8 秒超时静默放行** | 自己加业务级超时与重试，见第一节 |
| 切后台回来音乐自己响了 / 该响的没响 | 音频打断是引擎用 hide/show 模拟的 | 不要自己再监听一遍，见第一节 |
| Label 纹理错乱、截图空白 | 抖音上所有 Label 共用**单例 canvas** | 见第二节 |
| 视频调不了音量、画面比例被锁死 | 抖音 VideoPlayer 走软件路径 | 见第三节 |
| 输入框里的文字不出现在节点上 | EditBox 走系统键盘，节点只是占位 | 见第四节 |
| `performance.now()` 精度只有 1ms | 被替换成 `Date.now` | 见第五节 |
| `game.on(Game.EVENT_LOW_MEMORY)` 从不回调 | 小游戏根本不发这个事件 | 改用 `tt.onMemoryWarning` |
| `sys.restartJSVM()` 调用后没反应 | 小游戏上是空实现，只 warn | 见第六节 |

## 一、音频

### 1. 回调是伪造的，不代表真的出声

抖音的 `InnerAudioContext` 缺 `onPlay` / `onPause` / `onStop` / `onSeeked`，引擎用 polyfill 在一个**方法调用瞬间同步补一次回调**：

```
pal/minigame/bytedance.ts:104-109      // polyfillConfig: { onPlay: true, onPause: true, onStop: true, onSeek: true }
pal/utils.ts:54+                        // createInnerAudioContextPolyfill：改写 play/pause/stop/seek，调用即回调
```

所以：

- 用 `AudioSource` 的 `play` 事件做「音乐真的开始了」的业务判断，在抖音上不成立——回调在 `play()` 返回前就发出了。
- 直接 `tt.createInnerAudioContext()` 拿到的**是没有这层 polyfill 的原生对象**，回调行为与 Cocos 封装的不一致。业务代码统一走 `AudioSource` / `AudioSource.playOneShot`，别混用。
- `playOneShot` 每次调用都会新建一个 `InnerAudioContext`（`pal/audio/minigame/player-minigame.ts:282-290`），播完才 destroy。同屏大量短音效（连击、金币）要自己限流，不能靠引擎合并。

### 2. 加载有 8 秒超时，超时后「假装成功」

```
pal/audio/minigame/player-minigame.ts:253-281
```

`loadNative` 里挂了 `setTimeout(..., 8000)`：8 秒内没等到 `onCanplay` 也照样 `resolve`。结果是**没有 error、没有日志、后续 play 无声**。

排查「某个音效在低端机上不出声」时，先怀疑这里，别先怀疑音频格式。规避方式是加载后自己验一次 `duration` 是否 > 0（注意 `duration` 本身也有已知问题，见下）。

### 3. 打断事件是引擎用 hide/show 模拟的

```
pal/audio/minigame/player-minigame.ts:130-131   // systemInfo.on('hide'/'show')
pal/audio/minigame/player-minigame.ts:209-232   // _onInterruptedBegin / _onInterruptedEnd
```

引擎把「切后台」当成音频打断：hide 时 `pause` 并发 `INTERRUPTION_BEGIN`，show 时自动 `play` 回来并发 `INTERRUPTION_END`。

两点推论：

- **宿主的 `onAudioInterruptionBegin` / `onAudioInterruptionEnd` 在抖音上没有被引擎接管**（只有微信、淘宝的 wrapper 克隆了这两个方法：`platforms/minigame/platforms/{wechat,taobao-mini-game}/wrapper/unify.js`）。接电话、系统提示音这类**不切后台**的打断，引擎不知道，你的 BGM 可能直接哑掉且不恢复。
- 「回前台自动续播」是引擎给的默认行为，不是你的代码做的。想自己控制，监听 `AudioSource` 的 `interruptionBegin`/`interruptionEnd` 并覆盖。

### 4. 拿不到 PCM、拿不到采样率

```
pal/audio/minigame/player-minigame.ts:323-329   // sampleRate 返回 0，getPCMData 返回 undefined
```

频谱可视化、音频波形、`AudioBufferManager` 那套在抖音上不可用，只能自己用固定曲线做假波形。

## 二、文本与 Label：共用一块 canvas

```
platforms/minigame/platforms/bytedance/wrapper/engine/Label.js:6-21
```

抖音把 `Label._canvasPool` 换成了「永远返回同一块 canvas，`put()` 什么也不做」。也就是说**所有 Label 在同一帧内串行复用同一块画布**（画完就上传，否则后一个会盖掉前一个的内容）。

会踩的场景：

- 对 Label 做「先渲染、下一帧再读 canvas」这种异步操作，读到的一定是别的 Label 的内容。
- 自己写扩展组件去拿 `Label` 的 canvas 做二次处理（描边、投影、SVG 化），拿到的不是本节点的内容。
- Label 数量多时不要指望「每个 Label 一块缓存画布」，缓存池在抖音上是失效的。

需要稳定拿到文字纹理时，用 `Label` → 渲染到 `RenderTexture` 的路线，而不是去碰 canvas 池。

## 三、视频：`hasFeature` 说 false，但其实能用

```
pal/system-info/minigame/system-info.ts:209   // Feature.VIDEO_PLAYER = WECHAT || WECHAT_MINI_PROGRAM || OPPO —— 不含 BYTEDANCE
platforms/minigame/platforms/bytedance/wrapper/engine/VideoPlayer.js   // 但引擎完整实现了它
```

这是一处**能力探测与实际实现不一致**：按 `sys.hasFeature(sys.Feature.VIDEO_PLAYER)` 判断要不要用 `VideoPlayer`，在抖音上会误判为「不支持」；而实际引擎走的是 `tt.createOffscreenVideo()` + 每帧 `Texture2D.uploadData(video)` 的软件路径（`platforms/minigame/platforms/bytedance/wrapper/engine/VideoPlayer.js:358-362`）。

能用，但限制比微信多：

| 限制 | 证据 |
|---|---|
| **音量不可控**，调 `volume` 只打一条 warn | `platforms/minigame/platforms/bytedance/wrapper/engine/VideoPlayer.js:244-246` |
| 强制等比缩放，改不了 | `platforms/minigame/platforms/bytedance/wrapper/engine/VideoPlayer.js:354-356` |
| 倍速只有 0.5 / 0.8 / 1.0 / 1.25 / 1.5 五档 | `platforms/minigame/platforms/bytedance/wrapper/engine/VideoPlayer.js:235-241` |
| 「隐藏」是靠 `video.width = 0` 实现的 | `platforms/minigame/platforms/bytedance/wrapper/engine/VideoPlayer.js:220` |
| 每条视频**每帧一次纹理上传**，全屏视频非常吃带宽 | `platforms/minigame/platforms/bytedance/wrapper/engine/VideoPlayer.js:358-362` |

结论：抖音上**不要用 VideoPlayer 做全屏过场动画**，用序列帧 / 帧动画；或者绕开组件，直接用宿主的上屏 Video（`tt.createVideo`）自己控制位置与层级。

## 四、输入：EditBox 是系统键盘，节点只是占位

```
platforms/minigame/common/engine/Editbox.js:149-165   // _showKeyboard → __globalAdapter.showKeyboard
platforms/minigame/common/engine/Editbox.js:10        // KEYBOARD_HIDE_TIME = 600
platforms/minigame/common/engine/Editbox.js:9         // MAX_VALUE = 65535
```

- 文字是在**系统键盘自带的输入条**里输入的，不是画在你的 EditBox 节点里。节点上的文字样式（颜色/字号/对齐）在编辑期间**不生效**，只在 `textChanged` 之后才反映到节点。
- 切换两个 EditBox 有 **600ms** 的键盘隐藏保护期（`_ensureKeyboardHide`），连点会感觉「卡了一下」，不是掉帧。
- `maxLength < 0` 会被替换成 65535，不是无限。
- 单行/多行由 `inputMode === ANY` 决定，映射到 `multiple` 参数（`platforms/minigame/common/engine/Editbox.js:152-156`）。

## 五、时间、可见性与本地存储

| 事实 | 证据 | 影响 |
|---|---|---|
| `performance.now()` 就是 `Date.now()` | `platforms/minigame/platforms/bytedance/wrapper/builtin/WindowProperties.js:15-17` | 时间精度只有 **1ms**；自己做帧耗时统计、限流器、动画曲线时不要假设亚毫秒精度 |
| `document.visibilityState` 恒为 `'visible'` | `platforms/minigame/platforms/bytedance/wrapper/builtin/document.js:13-15` | 任何依赖 `visibilitychange` / `document.hidden` 的暂停逻辑在抖音上永远不触发 |
| `localStorage.getItem` 对不存在的 key 返回 `''` | `platforms/minigame/platforms/bytedance/wrapper/builtin/localStorage.js:14-16` | 不是 `null`；`if (localStorage.getItem(k) === null)` 这种写法在抖音上永远不成立，存档迁移逻辑会静默出错 |

> 另外两处**浏览器能力替换**也和适配强相关，但属于发布/适配范畴，为避免两处维护，只在 `cocos-publish.md` 写一遍：`innerWidth/innerHeight` 等于 `screenWidth/screenHeight`（「适配的三个平台差异」第 1 条）、`window.WebAssembly` 就是 `TTWebAssembly`（WASM 一节）。

## 六、生命周期与重启

### `game.restart()` 不是「重启小游戏」

```
cocos/game/game.ts:623-642
```

抖音分支（非微信）会走 `SplashScreen.createInstance().init()`：重置 `director`、把待销毁对象真正销毁掉（`Object._deferredDestroy()`）、暂停再恢复、重新加载启动场景，并**再走一遍闪屏**。但 **JS VM 不会重开**——模块级变量、全局缓存、挂在宿主对象上的监听器全都还在。写「重启游戏」按钮时，要么自己清干净全局状态，要么老实提示用户重进。

### `sys.restartJSVM()` 在抖音上是空实现

```
pal/system-info/minigame/system-info.ts:314-318   // 只 warn 'restartJSVM is not supported.'
```

想「真·重启进程」只能让用户退出小游戏再进——小游戏平台上引擎没有提供进程级重启能力。

### `sys.exit()` → 退出小游戏

```
pal/system-info/minigame/system-info.ts:320-329   // exitMiniProgram
```

### 内存告警不会走引擎事件

`Game.EVENT_LOW_MEMORY` 全引擎只有原生平台会 emit：

```
cocos/game/game.ts:224                        // 事件定义
platforms/native/engine/jsb-game.js:38        // 唯一的 emit 点
```

所以在抖音上 `game.on(Game.EVENT_LOW_MEMORY, ...)` **永远不会触发**。必须自己 `tt.onMemoryWarning`，见 `runtime.md` 与 `performance.md`。

## 七、启动参数与物理

### 引擎没有封装启动参数

全引擎搜不到 `getLaunchOptions` / `launchOptions` —— Cocos 不替你取分享带过来的 query。必须在首帧前自己调 `tt.getLaunchOptionsSync()` 并缓存；热启动（从后台或分享重新拉起）时这份值会更新，所以还要在 `tt.onShow` 的回调里刷新，别一直用启动时那份。见 `quickstart.md` 生命周期一节。

### 3D 物理走宿主私有加载分支

`templates/bytedance-mini-game/game.ejs` 里，引擎在 `require('./web-adapter')` **之前**先尝试加载原生物理：

- 宿主提供 `getPhysx` 时：拿到后用 `GameGlobal.nativePhysX` 挂上，再 `loadCC()`；
- Android 且宿主有 `getLoader()` 时：走 `loader.load('physics', appid, 'token', cb)`；
- 两者都没有才直接 `loadCC()`。

对 2D 游戏无影响（没开 PhysX 就不会生成这段）。需要注意它的容错方式是**全部降级、从不报错**：`getPhysx` 的 fail 分支、loader 的失败回调，最终都只是 `loadCC()` 继续启动。所以线上出现「3D 物理行为不同 / 性能突然变差 / 碰撞不对」时，先确认原生物理到底有没有挂上——`appid` 是从构建参数注入的，注入错了也只会静默降级。

## 八、构建产物里的默认值

这两个模板是产物里 `game.json` / `project.config.json` 的底稿，构建栏的选项会覆盖它们：

```
templates/bytedance-mini-game/game.json
templates/bytedance-mini-game/project.config.json
```

值得注意的默认值：

| 字段 | 默认 | 说明 |
|---|---|---|
| `deviceOrientation` | `portrait` | 模板写死竖屏，构建面板的「设备方向」会覆盖它。手写 `game.json` 且不写此字段时平台按横屏处理；Cocos 产物永远显式写值，不会落到那个默认 |
| `networkTimeout.downloadFile` | `500000` | 下载超时是 500 秒，别指望它快速失败 |
| `networkTimeout.request` | `5000` | 普通请求 5 秒 |
| `showStatusBar` | `false` | 不显示状态栏 |
| `openDataContext` | `""` | 空串即未启用开放数据域 |
| `setting.es6` | `false` | 产物是已转译的代码，别在开发者工具里再开 ES6 转 ES5 |
| `setting.urlCheck` | `true` | **域名校验开着**——真机请求失败、模拟器正常，先查这个与后台域名白名单 |
