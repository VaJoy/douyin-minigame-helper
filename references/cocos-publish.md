# Cocos 发布与构建

> **适用**：把 Cocos Creator 3.8 工程发布成抖音小游戏、配分包、接开放数据域。
> **源文档**：Cocos Creator 3.8 官方手册 —— `editor/publish/publish-bytedance-mini-game`、`subpackage`、`build-open-data-context`（docs.cocos.com）。
> **关联**：`game.json` 字段见 `config.md`；包体标准与 iOS 内存见 `performance.md`；开放数据域的业务侧用法见 `social.md`。

## 一、发布流程

1. 菜单栏 → **项目** → **构建发布**，平台选「抖音小游戏」；
2. 填 **AppID**（开发者后台 → 开发管理 → 开发设置 里取）和**设备方向**；
3. 点 **构建**，产物在 `build/bytedance-mini-game/`（目录名随构建任务名，可能不同）；
4. 用**抖音开发者工具**打开这个产物目录（不是 Cocos 工程目录），即可预览调试。

产物目录里已经有 `game.json` 和 `project.config.json`，**是构建时生成的**——手动改会在下次构建被覆盖，要改配置就改 Cocos 侧的选项。

## 二、构建面板里值得注意的选项

### 主包设置

| 选项 | 作用 | 命令行字段 |
|---|---|---|
| 初始场景分包 | 首场景及依赖打进 `assets/start-scene` 这个内置 Bundle，提升首屏加载速度 | `startSceneAssetBundle` |
| 资源服务器地址 | 远程资源地址；构建后要**手动**把 `remote/` 目录上传到该地址 | `remoteServerAddress` |

### 引擎设置

| 选项 | 说明 |
|---|---|
| `CLEANUP_IMAGE_CACHE` | 纹理上传 GPU 后删掉内存副本。**开了就不能用动态合图** |
| 物理系统 | 选哪个发布后就用哪个 |
| WebGL 2.0 | 选择 WebGL 版本 |
| 原生代码打包模式 | 统一控制 Spine / 物理等 wasm/asmjs 模块，默认最优，**不建议改** |
| Wasm 3D 物理 | bullet(ammo.js) 时的 WASM 开关，默认开 |
| 引擎原生代码分包 | 把引擎的 WASM/Asm.js 放进子包，**减主包体积** |
| WASM Brotli 压缩 | 减小 WASM 模块体积，代价是加载时多一次解压 |

### 构建选项

| 选项 | 说明 | 命令行字段 |
|---|---|---|
| 生成开放数据域工程模板 | 生成 `openDataContext/` 模板 | `buildOpenDataContextTemplate` |
| AppID | 必填，写进 `project.config.json` | `appid` |
| 设备方向 | Portrait / Landscape，写进 `game.json` | `orientation` |
| 开发者工具打开方式 | 默认 **Lite 模式**，启动更快 | – |

## 三、分包（主包 4MB 的救命方案）

### 怎么配

1. 资源管理器里选中一个**文件夹** → 属性检查器勾「**配置为 Bundle**」；
2. 目标平台选抖音小游戏，**压缩类型选「小游戏分包」**；
3. 「配置为远程包」是**锁死**的——小游戏分包只能放本地；
4. 构建发布面板里把**主包压缩类型**也设为「小游戏分包」。

构建后这些 Bundle 会输出到发布包的 `subpackages/<name>/`，并自动写进 `game.json` 的 `subPackages`。

### 体积限制

| 项 | 上限 |
|---|---|
| 小游戏整体（整个目录） | 20 MB（有文档写「开通虚拟支付后 30 MB」，见下） |
| 单个主包 | **4 MB**（所有文档一致，没有豁免） |
| 单个分包 | 20 MB（同上，30 MB 存疑） |
| 开放数据域文件/目录 | **4 MB**（「类似子包概念」） |

不分包的话，代码包总大小上限是 20MB——但主包一旦超 4MB，启动就很吃力。

> **体积口径有两份文档，且不一致，按更新时间列一下：**
>
> - `docs/develop/guide/dev-guide/bytedance-mini-game.md:96-106`（**2025-06-09，较新**）：普通包 20MB；分包后整体 20 / 主包 4 / 单分包 20；开放数据域文件或目录 **不超过 4MB**（原文「类似子包概念」）。**没提 30MB 豁免。**
> - `docs/develop/guide/basic-function/subpackages/introduction.md:16-18`（**2025-04-15，较旧**）：整体与单个分包「20MB，开通虚拟支付后 30MB」，主包仍 4MB。
>
> 所以 30MB 豁免**存疑**：较新的页面没有记载。真要贴着上限做包，以开发者后台的实际上传校验为准，别只信文档。

### 平台版本要求

| 产品 | Android | iOS |
|---|---|---|
| 抖音 | v13.6.0 | v13.7.0 |
| 今日头条 | v7.9.9 | v7.9.8 |

开发者工具 **≥ 2.0.6 且 < 3.0.0**，调试基础库 **≥ 1.88.0**。

> **出处要分清**（本地抖音文档库逐条查过）：
> - `≥ 2.0.6` 与 `≥ 1.88.0` 有官方原文：`docs/develop/guide/basic-function/subpackages/basic.md:7`（「基础库 1.88.0 及以上开始支持，开发者工具请使用大于等于 2.0.6 的版本」）。
> - **表里的宿主版本（13.6.0 / 13.7.0 / 7.9.9 / 7.9.8）和「< 3.0.0」上限，本地抖音文档 0 命中**，来自 Cocos Creator 手册的抖音小游戏发布页（见本文头部「源文档」）。当参考值用，别当硬约束。

宿主版本不够时不会报错，引擎会把分包当成普通 Asset Bundle 加载——表现是「分包没省下启动时间」，排查时先看宿主版本。

## 四、开放数据域

### 渲染容器：SubContextView

开放数据域只能画在离屏的 `sharedCanvas` 上，所以主域需要一个节点挂 **`SubContextView`** 组件来显示它。

两个属性：

- **设计分辨率**：设为 `640 × 960`，`sharedCanvas` 就是这个尺寸。定制开放数据域时样式里标签的最大宽高不能超过它，否则内容溢出画布。也可以用 `100%` 百分比避免耦合。
- **FPS**：主域把 sharedCanvas 刷到组件上的频率。**别设太高**，频繁上传贴图很吃性能。

渲染时引擎用 `SHOW ALL` 适配，贴图不会被拉伸变形。

### 生成与定制

1. 场景里加好 `SubContextView`；
2. 构建面板勾「**生成开放数据域工程模板**」，构建后产物目录下会多出 `openDataContext/`；
3. 在这个目录里改排行榜逻辑。**再次构建时如果该目录已存在，会直接跳过**，不会覆盖你的定制。

模板结构：

| 文件 | 作用 |
|---|---|
| `index.js` | 入口，把 XML + CSS 交给 Canvas 引擎渲染 |
| `render/dataDemo.js` | 数据源，换成平台的关系链数据 |
| `render/style.js` | CSS 样式 |
| `render/template.js` | doT 模板生成的 XML 文本 |
| `render/avatar.png` | 默认头像占位，可删 |
| `engine.js` | 内置的轻量 Canvas 引擎（minigame-canvas-engine） |

**建议**：`build/` 默认被 git 忽略，想给开放数据域做版本管理，把 `openDataContext` 目录放进项目的 `build-templates/`。

### 与主域通信

子域监听消息时**要先判断来源**，否则会把引擎内部消息当成业务消息：

```js
// 开放数据域内
tt.onMessage((res) => {
  if (!(res && res.type === 'engine')) {
    // 这里才是主域发来的业务消息
  }
});
```

主域发消息时也建议带上 `type`，双方约定好，别混用。

## 五、包体超了怎么办

按顺序试：

1. **分包**：把非首屏资源和脚本拆成 Bundle（上面第三节）；
2. **引擎原生代码分包**：把 WASM 塞进子包；
3. **远程资源**：构建面板填资源服务器地址，把 `remote/` 传上去，引擎会在启动后自动下载并按缓存管理器策略清理；
4. **WASM Brotli 压缩**：换体积，代价是解压耗时。

## 六、引擎适配层（源码核实）

> 本节不是平台文档，是工作区 `cocos-engine-3.8.6/` 的实际实现，判据给 `file:line`。

### 代码里怎么判断「我在抖音上」

两条链，用途不同，别混用：

| 用途 | 写法 | 特点 |
|---|---|---|
| 运行时判断 | `sys.platform === sys.Platform.BYTEDANCE_MINI_GAME` | 保留分支，两种平台代码都在包里 |
| 编译期裁剪 | `import { BYTEDANCE } from 'cc/env'` | 构建时替换为字面量，死代码可被摇掉 |

```ts
import { sys } from 'cc';
import { BYTEDANCE, MINIGAME } from 'cc/env';

const isDouyin = BYTEDANCE && sys.platform === sys.Platform.BYTEDANCE_MINI_GAME;
```

几个必须知道的事实：

- `BYTEDANCE` 是编译期常量（`cc.config.json:574`，`ccGlobal: true`，构建时以字面量注入），构建平台选抖音时为 `true`。引擎内部就是直接写裸的 `BYTEDANCE`，业务代码里用 `import { BYTEDANCE } from 'cc/env'` 拿。
- `MINIGAME` 的表达式含抖音：`$WECHAT || $WECHAT_MINI_PROGRAM || $XIAOMI || $ALIPAY || $TAOBAO || $TAOBAO_MINIGAME || $BYTEDANCE`（`cc.config.json:686-690`）。**写小游戏通用分支用它，写抖音专属分支用 `BYTEDANCE`。**
- 运行期的平台枚举由 `BYTEDANCE` 映射：`currentPlatform = Platform.BYTEDANCE_MINI_GAME`（`pal/system-info/minigame/system-info.ts:47-48`）。
- **`SUPPORT_JIT` 在抖音恒为 `false`**：`!(($PREVIEW && !$NATIVE) || $MINIGAME || $RUNTIME_BASED || $OPEN_HARMONY)`（`cc.config.json:699-703`）。它决定引擎生命周期调用走不走 `new Function` 那条 JIT 路径，而且是**构建期常量**——开 iOS 高性能模式也不会翻转它。详见 `performance.md`。

### 能力矩阵：哪些「不支持」是真的

`sys.hasFeature()` 的值来自 `pal/system-info/minigame/system-info.ts:205-223`，抖音相关项：

| Feature | 抖音 | 证据 | 影响 |
|---|---|---|---|
| `SAFE_AREA` | **true** | `:210`（全平台里只有微信 / 微信小程序 / 抖音为 true） | 可以用 `sys.getSafeAreaRect()`（`cocos/core/platform/sys.ts:371`），但要读适配一节的坑 |
| `VIDEO_PLAYER` | false | `:209` | **但引擎其实实现了**，别拿它当开关，见 `engine-quirks.md` 第三节 |
| `WASM` | 取决于宿主 | `:180-191` | Android 要 SDKVersion ≥ 3.9.0、iOS ≥ 3.8.0，**且** `TTWebAssembly` 存在 |
| `WEB_VIEW` / `IMAGE_BITMAP` / `HPE` | false | `:206-211` | WebView 组件在抖音不可用 |
| `EVENT_GAMEPAD` | false | `:218` | 手柄事件收不到 |

`WASM` 之所以要看宿主：抖音的 `window.WebAssembly` 直接指向 `TTWebAssembly`（`platforms/minigame/platforms/bytedance/wrapper/builtin/index.js:61`），宿主不提供时它就是 `undefined`。Spine wasm、bullet wasm 都吃这个前提——**低版本宿主上它们是「静默跑不起来」而不是报错**。

### 适配的三个平台差异

1. **可视区尺寸取的不是 `windowWidth/windowHeight`。** 抖音分支用 `screenWidth/screenHeight`，微信用 `windowWidth/windowHeight`（`pal/screen-adapter/minigame/screen-adapter.ts:76-95`）。所以 `window.innerWidth/innerHeight` 在抖音上是**物理屏幕尺寸**（`platforms/minigame/platforms/bytedance/wrapper/builtin/WindowProperties.js:3-4`）。自己算画布、截图、RenderTexture 尺寸时不要拿它当「游戏可视区」。
2. **入口模板会二次改画布尺寸。** `game.ejs` 里先按 `screen.width/screen.height` 做一次方向互换兜底，再在 `devicePixelRatio >= 2` 时把 canvas 宽高各乘 2。所以要拿真实画布尺寸，读 `screen.windowSize` / `view.getVisibleSize()`，别读 `canvas.width`。
3. **安全区在 iOS 横屏下是引擎手工算的，而且不全对。** 抖音是少数支持 `Feature.SAFE_AREA` 的平台之一，但平台返回的 `safeArea` 是「**竖屏正方向下**的安全区域」，横屏得换算。引擎对 iOS 横屏做了一次手工旋转（把 `top` / `left` 对调、`right` 重算），源码里自己留了一句 `FIX_ME: wrong safe area when orientation is landscape left`（`pal/minigame/bytedance.ts:112-125`）。

   实际影响：刘海屏横屏时留白可能落到反方向那一边。做适配时别只信 `sys.getSafeAreaRect()` 的返回值——

   - 要么横屏干脆不用它，左右统一留 `max(safeAreaEdge.left, safeAreaEdge.right)` 的对称边距；
   - 要么只信竖屏，横屏自己按设计稿做固定边距。

   竖屏游戏不受这条影响（`FIX_ME` 只在 `isLandscape` 分支里）。

### 资源与脚本的加载路径

小游戏的 AssetManager 被整体替换（`platforms/minigame/common/engine/AssetManager.js`）：

| 事实 | 证据 |
|---|---|
| 下载并发被改成 **12**，每帧最多 **64** 个请求（scene preset 同值） | `:38-41` |
| **禁止加载远程脚本**，直接返回 `Can not load remote scripts` | `:52` |
| 分包 bundle 的配置在 `subpackages/<name>/config.json` | `:170-183` |
| 远程 bundle 的地址是 `<资源服务器地址>remote/<name>`，配置里 `isZip` 时再下 `res.zip` 解压 | `:206`、`:225-228` |
| **bundle 的脚本始终在本地** `src/bundle-scripts/<name>/index.js`，只有资源能远程 | `:203-207` |
| 宿主不支持 `tt.loadSubpackage` 时，降级成 `require('subpackages/<name>/game.js')` | `platforms/minigame/platforms/bytedance/wrapper/fs-utils.js:233-240` |
| 字体加载失败静默回落 `Arial`，不抛错 | `platforms/minigame/common/engine/AssetManager.js:146-149` |

两条最实用的推论：

- **远程包只能放资源。** 想把「代码 + 资源」一起放远程省主包，是不成立的：脚本必须留在本地。要省主包，脚本走分包，资源走远程。
- **字体加载失败没有报错。** 中文 TTF 走远程/分包时如果路径不对，表现是「文字用 Arial 渲染，中文变方框/英文变形」，控制台干净。排查时打印 `loadFont` 返回的 family 确认。

## 常见坑

| 现象 | 原因 |
|---|---|
| 开发者工具打不开 | 打开的是 Cocos 工程目录，应该打开 `build/bytedance-mini-game` |
| 手改 `game.json` 没生效 | 构建时会被重新生成，要改 Cocos 侧选项 |
| 竖屏变横屏 | 构建面板「设备方向」没设，或 `game.json` 被覆盖 |
| 开了 `CLEANUP_IMAGE_CACHE` 后合图失效 | 该选项与动态合图互斥 |
| 分包没提速 | 宿主版本低于要求，降级成了普通 Bundle |
| 排行榜是空白 | 没挂 `SubContextView`，或没勾「生成开放数据域工程模板」 |
