# 运行时与框架

> **适用**：理解抖音小游戏的 JS 运行环境、模块系统、生命周期、Worker 与文件系统。
> **源文档**：`docs/develop/framework/`（22 篇）、`docs/develop/guide/basic-function/`（14 篇）。
> **关联**：启动流程见 `quickstart.md`；性能相关见 `performance.md`。

## 运行环境

- 只有 JavaScript，没有 `BOM` / `DOM`：`window`、`document`、`XMLHttpRequest`、`localStorage` 都不存在。
- 不同宿主（抖音、抖音极速版、头条）用的 **JS 引擎不同**，对 ES 新特性的支持程度也不同；基础库内置了一部分 Polyfill，但不能指望它补齐所有语法。
- 结论：**构建时把 target 定低一点**（ES5/ES2015），并在真机上验证，不要只看开发者工具。

### Canvas

```js
const canvas = tt.createCanvas();       // 第一次调用返回上屏 Canvas
const ctx = canvas.getContext('2d');
```

- 上屏 Canvas 全局**有且仅有一个**，与屏幕等宽等高，尺寸不可改。
- 需要离屏渲染时再 `tt.createCanvas()`，拿到的是离屏 Canvas。
- 需要 WebGL 时用 `getContext('webgl')`；Cocos 走的就是这条路。

### 触摸事件

`tt.onTouchStart` / `onTouchMove` / `onTouchEnd` / `onTouchCancel`，坐标系以逻辑分辨率计。多点触控通过事件里的 `touches` 数组拿。

### 时间与可见性：两个被替换掉的浏览器能力

Cocos 的抖音兼容层把这两样改写了，写计时、限流、暂停逻辑时必须知道：

| 事实 | 证据 | 影响 |
|---|---|---|
| `performance.now()` 就是 `Date.now()` | `platforms/minigame/platforms/bytedance/wrapper/builtin/WindowProperties.js:15-17` | 时间精度只有 **1ms**，没有亚毫秒。做帧耗时统计、节流器、动画插值时，别用「小于 1ms 的差值」当判据，也别假设 `now()` 单调递增（`Date.now` 会受系统时间调整影响） |
| `document.visibilityState` 恒为 `'visible'`，`document.hidden` 恒为 `false` | `platforms/minigame/platforms/bytedance/wrapper/builtin/document.js:13-15` | 依赖 `visibilitychange` 或 `document.hidden` 的暂停/恢复逻辑在抖音上**永远不触发**。切后台只能靠 `tt.onHide` / `tt.onShow`，或引擎的 `game.on(Game.EVENT_HIDE/EVENT_SHOW)` |

游戏主循环的时间基准仍以引擎给的 `dt` 为准（`game.deltaTime` / 组件的 `update(dt)`），不要自己用 `performance.now()` 攒时间。

## 模块化

采用 **CommonJS** 规范，和 Node 一致：

```js
// utils.js
const pad = (n) => String(n).padStart(2, '0');
module.exports = { pad };
```

```js
// game.js
const { pad } = require('./utils.js');
```

- 只支持**相对路径** `require`，不支持 `node_modules` 解析（打包工具负责把依赖打平）。
- 循环引用时拿到的是未完成的 `exports` 对象，和 Node 行为一致。
- 引擎侧一般有自己的模块系统（Cocos 用 SystemJS/cc 模块），业务代码按引擎的方式写即可，不必强行改成 CommonJS。

## 生命周期

### 冷启动 vs 热启动

| 类型 | 场景 | 行为 |
|---|---|---|
| 冷启动 | 首次打开 / 进程被回收后重开 | 完整加载资源，重新执行 `game.js` |
| 热启动 | 短时间切走再回来 | 进程还在，从后台恢复，**不会**重新执行入口脚本 |

所以初始化逻辑要幂等，且区分「首次进入」与「恢复」：用模块级变量或 `tt.getLaunchOptionsSync()` 的 `scene` 判断。

### 前后台

```js
tt.onHide(() => { /* 切后台：暂停音乐、停 tick、保存进度 */ });
tt.onShow((res) => { /* 回前台：恢复、可能带新的 launch options */ });
```

- 切到后台后仍可**短时间**运行，之后可能被系统挂起甚至强杀。
- 长时间未返回或内存不足时进程会被终止，下次是冷启动 —— **不要在内存里保存唯一存档**。

### 内存告警

```js
tt.onMemoryWarning((res) => {
  // res.level 仅 Android 提供，对应系统内存告警等级；iOS 没有这个字段
  releaseCaches();
});
```

收到告警应该主动释放贴图缓存、音频实例、临时对象，而不是等系统杀进程。

## 定时器与逐帧

- `setTimeout` / `setInterval` / `clearTimeout` / `clearInterval` 与浏览器一致，但**后台会被节流**，不要用它做游戏主循环。
- 主循环用 `requestAnimationFrame`，与屏幕刷新对齐：

```js
function loop(ts) {
  update(ts);
  render();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

## Worker

- 在 `game.json` 里用 `workers` 指定 Worker 目录，Worker 里可以用 `postMessage` 与主线程通信。
- 适合放：寻路、大量 JSON 解析、加解密、物理预计算。
- 不适合放：任何需要访问 `tt` API 的逻辑（Worker 里没有），以及 UI 渲染。
- Worker 与主线程**不共享内存**（除非用 SharedArrayBuffer，且需宿主支持），数据要序列化传递，大对象传输本身就有开销。

## 文件系统

小游戏有一套沙箱文件系统，通过 `FileSystemManager` 操作：

```js
const fs = tt.getFileSystemManager();
fs.writeFileSync(`${tt.env.USER_DATA_PATH}/save.json`, JSON.stringify(data), 'utf8');
const txt = fs.readFileSync(`${tt.env.USER_DATA_PATH}/save.json`, 'utf8');
```

- 用户目录是 `tt.env.USER_DATA_PATH`，卸载/清缓存会丢。
- 临时文件目录用于下载缓存，系统会在需要时清理。
- 大文件（>10MB）用分片写，`writeFileSync` 一次性写会卡主线程。
- **存储（`tt.setStorageSync`）和文件系统是两套东西**：存储有配额限制、适合小 KV；文件系统适合大对象和二进制资源。
- 如果你在代码里用 `localStorage`（或 `sys.localStorage`）：原生环境并没有它（见上文），是 **Cocos 的兼容层注入了一个垫片**（`platforms/minigame/platforms/bytedance/wrapper/builtin/localStorage.js:14-29`），底层转调存储接口。所以能用，但语义不同：**`getItem` 对不存在的 key 返回空字符串 `''`，不是 `null`**。`if (localStorage.getItem(k) === null)` 这类判断在抖音上永远不成立，存档版本迁移、首次进入检测很容易在这里静默出错——判空请用 `if (!v)` 或 `=== ''`。
- **引擎不会替你把临时文件转成持久文件。** `platforms/minigame/platforms/bytedance/wrapper/fs-utils.js:88-100` 里定义了个 `saveFile()`，它调的是宿主**顶层**的 `saveFile` 接口——这个接口平台文档里没有（文档只提供 `FileSystemManager.saveFile` / `saveFileSync`），而且**全引擎没有任何调用点**，属于死代码；支付宝/淘宝的同名实现甚至直接换成 `copyFile`，源码注释里写着 `my.saveFile` 不可用。所以别照着它写：`tt.downloadFile` 下来的文件在临时目录、会被系统清理，想长期保留必须自己 `tt.getFileSystemManager().saveFileSync(tempFilePath, userPath)`。

## 调试手段

| 手段 | 用途 |
|---|---|
| `console.log` | 开发者工具控制台可见，真机需配合实时日志 |
| vConsole | 真机上的调试面板，见 `devtools.md` |
| 实时日志 | 线上真机日志回传，排查用户侧问题 |
| `tt.getPerformance()` | 取性能打点，做启动耗时统计 |
