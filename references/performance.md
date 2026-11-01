# 性能优化

> **适用**：启动慢、包体超限、掉帧、发热、内存崩溃。
> **源文档**：`docs/develop/guide/performance-optimization-both/performance-optimization/`（23 篇，另 22 篇 Unity 已归档）。
> **关联**：分包配置见 `config.md`；高性能模式与机型分档见本文末。

## 先看标准：什么算达标

平台按机型分高/中/低三档给指标（`小游戏性能评测标准`）：

| 指标 | 高端机达标 | 中端机达标 | 低端机达标 |
|---|---|---|---|
| 首包大小 | 分包 4MB / 不分包 20MB | 同左 | 同左 |
| 总启动耗时 TTI（可交互） | ≤ 11000 ms | ≤ 14900 ms | ≤ 20000 ms |
| 首帧到达 FP80 | ≤ 3620 ms | ≤ 5110 ms | ≤ 7980 ms |
| FPS 均值 | ≥ 56 | ≥ 55 | ≥ 54 |
| 内存均值 | ≤ 2400 MB | ≤ 1800 MB | ≤ 1500 MB |
| 内存异常退出率 | ≤ 0.1% | ≤ 1.2% | ≤ 4.8% |

**首包是第一优先级**：超过 4MB（用分包）或 20MB（不用分包）直接过不了。

## 启动优化

按阶段拆，每段都有对应的优化手段：

| 阶段 | 手段 |
|---|---|
| 代码包下载 | 分包（`subPackages`）+ 首包只放引擎核心与首场景；资源上 CDN |
| 代码注入 | 关掉不必要的 Polyfill；减小首包 JS；避免巨型单文件 |
| 首屏渲染准备 | 首场景不要挂重资源；Loading 界面用纯色/单图；异步初始化非关键系统 |
| 可交互 | 首帧后再加载音频、广告 SDK、埋点、排行榜等 |

具体做法：
- **分包**：主包只留启动必需，关卡/皮肤/大图放分包，`tt.loadSubpackage` 按需拉。
- **资源按需**：首屏只加载首屏用到的图集，其余进游戏后再加载。
- **延迟初始化**：广告实例、分享、支付、统计全部延后到首帧之后。
- **避免同步 IO**：`readFileSync`、大 JSON `JSON.parse` 放到分包加载后的空档。

## 运行优化

- **渲染**：合批（同图集同材质）、减少 drawcall、避免每帧创建对象（用对象池）、控制同屏粒子数。
- **CPU**：主循环里不做字符串拼接与深拷贝；把寻路/物理预计算丢给 Worker（见 `runtime.md`）。
- **GC**：避免频繁分配临时对象，尤其是 `new Vec2()`、闭包、数组 `map`。`tt.triggerGC()` 可主动触发，但别当常规手段。
- **发热**：降帧（30fps 模式）、降分辨率、减少透明叠加与全屏后处理。
- **内存**：纹理压缩、及时 `destroy` 不再使用的资源、监听 `tt.onMemoryWarning` 主动释放。

### 降帧要真的降下去

`game.frameRate = 30` 不是「逻辑上少调几次 update」，它会一路传到宿主：

```
cocos/game/game.ts:416-426            // set frameRate → this._pacer.targetFrameRate
pal/pacer/pacer-minigame.ts:50-60     // set targetFrameRate → minigame.setPreferredFramesPerSecond(...)
```

也就是说宿主会把 `requestAnimationFrame` 真的降到 30Hz，省电省热，而不是「仍然 60 次回调、只算一半」。低端机上这是性价比最高的一档开关，配合 `deviceScore` 做分档（见下节）。

两个细节：

- **运行中改帧率会重启 rAF 循环**（`pacer-minigame.ts:55-58` 里 `stop()` 再 `start()`），所以别在每帧或频繁变化的场景里反复赋值，会白掉帧。要改就在切场景、切画质档这种一次性时机改。
- 把它设成 120 之类的值，在没有高刷屏的设备上没有任何效果——`frameRate` 只表示**期望值**。

## 高性能模式（iOS 专项）

iOS 没有 JIT，性能一直是短板。高性能模式让小游戏跑在浏览器内核里、拿到 JIT 能力，官方内测数据：**80 分位 FPS 平均提升 69%**（32.53 → 54.98）。CPU 压力越大的游戏收益越明显。

### 开启与确认

`game.json`：

```json
{
  "deviceOrientation": "portrait",
  "enableIOSHighPerformanceMode": true
}
```

- **局域网预览不支持**高性能模式，预览时别勾「开启局域网快速预览」。
- 判断是否生效：`GameGlobal.isIOSHighPerformanceMode === true`（普通模式是 `undefined`）；或看 vConsole 颜色——绿色=普通，蓝色=高性能。
- 高性能模式下跑在浏览器内核里，**兼容性、内存、稳定性都要重新测**，不能复用普通模式的测试结论。

### 它提速的是你的 JS，不是引擎的生命周期调度

这条很容易误解，单独说清楚：Cocos 有两条生命周期调用路径，用构建期常量 `SUPPORT_JIT` 二选一——`true` 走 `new Function` 编译出的直调函数，`false` 走普通调用（`cocos/scene-graph/component-scheduler.ts:274-304`、`cocos/scene-graph/node-activator.ts:66-76`）。

而 `SUPPORT_JIT` 的取值是：

```
!(($PREVIEW && !$NATIVE) || $MINIGAME || $RUNTIME_BASED || $OPEN_HARMONY)
```

——`cc.config.json:699-703`。**只要是小游戏，`SUPPORT_JIT` 恒为 `false`**，抖音也一样。

推论：

- 高性能模式带来的是宿主 JS 引擎的 JIT 能力（你的业务代码跑得快），**不会**把引擎的 `onLoad/update` 调度切回 JIT 路径，因为那是**打包时就定死**的常量，运行时无法翻转。
- 所以「开了高性能模式」≠「引擎开销也降了」。低端机上真正压帧的往往是组件数量与 `update` 调用次数本身，这两项要另外优化。
- 想在代码里判断，直接 `import { SUPPORT_JIT } from 'cc/env'`，在抖音构建里它永远是 `false`，别写成运行时开关。

### 代价是内存更紧

超过阈值会被系统直接杀进程，峰值必须压住：

| 机型 | RAM | 内存上限 |
|---|---|---|
| iPhone 6s / 7 / 8 | 2 GB | **1 GB** |
| iPhone 7P / 8P / X / XR / XS Max / 11 | 3 GB | **1.4 GB** |

内存没优化好就别开高性能模式，iOS 低端机会频繁异常退出。

### 内存构成与优化抓手

运行时内存大致六块：JavaScript Heap、WASM 资源、基础库 + Canvas、音频、GPU 资源、字体。

| 部分 | 量级 / 优化手段 |
|---|---|
| 基础库 | 常驻约 **65 MB**，不可优化 |
| Canvas | 与宽高成正比；降低渲染分辨率倍数是最直接的手段 |
| 引擎 | 用编辑器「项目设置 → 功能裁剪」砍掉不用的模块 |
| 音频 | 单个双通道实例约 **20 MB**；播完释放，或用单通道 |
| 字体 | 中文 TTF 加载后 **≥10 MB**；优先系统字，或换 Bitmap / SDF 字体 |
| 图片 | iOS 建议 **ASTC** 压缩纹理，内存比 PNG 小 50%+（但文件更大、增加包体）；配合禁用动态合批可释放 image 内存 |
| 脚本 | 业务代码 + 配置表，只能自己精简 |

TTF 渲染文本会创建 Canvas 对象并进缓存池，字号越多池越大，引擎不回收——字重多的游戏优先换 Bitmap 字体。对象池要设上限，别无限创建。

### 内存告警别监听错对象

`game.on(Game.EVENT_LOW_MEMORY, ...)` 在抖音上**永远不会回调**。这个事件全引擎只有一个 emit 点，在原生平台：

```
cocos/game/game.ts:224                    // 事件定义
platforms/native/engine/jsb-game.js:38    // 唯一的 emit
```

小游戏上只能自己听 `tt.onMemoryWarning`（`res.level` 仅 Android 提供），收到后主动释放贴图缓存、音频实例、临时对象，不要等系统杀进程。见 `runtime.md`。

### 诊断工具

| 工具 | 用法 |
|---|---|
| Xcode Instruments | Activity Monitor 选设备 → 过滤 `webkit`，看 CPU/内存 |
| Perfdog | 选进程名看性能曲线 |
| 抖音开发者工具 | Profiles 面板：Heap snapshot、Allocation instrumentation、实时内存诊断（录制看内存块生灭，垃圾桶按钮触发 GC） |

**注意进程名**：高性能模式含 `WebContent`，普通模式含 `Aweme`，抓错进程会看不到数据。

## 机型分档与降级

`tt.getSystemInfoSync().deviceScore` 是官方给的性能评分：

- `(0, 7.30)` 低端机
- `[7.30, 8.51)` 中端机
- `[8.51, +∞)` 高端机
- `-1` 取不到（当作中端处理）

用它做画质分档，比维护机型白名单靠谱：

```js
const { deviceScore } = tt.getSystemInfoSync();
const tier = deviceScore < 0 ? 'mid' : deviceScore < 7.3 ? 'low' : deviceScore < 8.51 ? 'mid' : 'high';
applyQuality(tier); // 低端关特效/降分辨率，高端开满
```

## 排查工具

| 工具 | 用途 |
|---|---|
| 实时日志 | 线上真机日志回传，看崩溃与耗时 |
| 反馈日志 | 用户侧问题回溯 |
| 性能测试工具 | 采集启动/运行指标，对照上面的标准 |
| `tt.getPerformance()` | 代码里打点，统计各阶段耗时 |
| IDE 真机调试支持矩阵 | 确认某个调试能力在目标机型是否可用 |

## 常见误区

- **只看模拟器**：模拟器没有真实 GPU 与内存压力，结论不可用。
- **只优化首屏**：进游戏后掉帧同样流失用户。
- **滥用预加载**：全部资源预加载会把首包撑爆，得不偿失。
- **忽略低端机**：低端机占比不低，且是内存异常退出的主要来源。
