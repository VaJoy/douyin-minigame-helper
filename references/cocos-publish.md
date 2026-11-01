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
| 小游戏整体（整个目录） | 20 MB |
| 单个主包 | **4 MB** |
| 单个分包 | 20 MB |
| 开放数据域文件/目录 | **4 MB** |

不分包的话，代码包总大小上限是 20MB——但主包一旦超 4MB，启动就很吃力。

### 平台版本要求

| 产品 | Android | iOS |
|---|---|---|
| 抖音 | v13.6.0 | v13.7.0 |
| 今日头条 | v7.9.9 | v7.9.8 |

开发者工具 **≥ 2.0.6 且 < 3.0.0**，调试基础库 **≥ 1.88.0**。

> 宿主版本不够时不会报错，引擎会把分包当成普通 Asset Bundle 加载——表现是「分包没省下启动时间」，排查时先看宿主版本。

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

## 常见坑

| 现象 | 原因 |
|---|---|
| 开发者工具打不开 | 打开的是 Cocos 工程目录，应该打开 `build/bytedance-mini-game` |
| 手改 `game.json` 没生效 | 构建时会被重新生成，要改 Cocos 侧选项 |
| 竖屏变横屏 | 构建面板「设备方向」没设，或 `game.json` 被覆盖 |
| 开了 `CLEANUP_IMAGE_CACHE` 后合图失效 | 该选项与动态合图互斥 |
| 分包没提速 | 宿主版本低于要求，降级成了普通 Bundle |
| 排行榜是空白 | 没挂 `SubContextView`，或没勾「生成开放数据域工程模板」 |
