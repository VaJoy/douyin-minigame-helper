# 从零跑通（Cocos 路线）

> **适用**：第一次把 Cocos Creator 项目发布成抖音小游戏。
> **源文档**：`docs/develop/guide/dev-guide/`（3 篇）、`docs/develop/guide/game-engine/cocos-laya-egret.md`、`docs/develop/dev-tools/`、`docs/guide/minigame/`。
> **关联**：配置文件字段见 `config.md`；提审与资质见 `security-release.md`。

## 0. 前置条件

| 事项 | 说明 |
|---|---|
| 开发者账号 | 开放平台注册 + 主体认证（个人/企业），个人主体能做的类目有限 |
| 小游戏 AppID | 后台创建小游戏后获得，导出时必须填对 |
| 开发者工具 | 「抖音小游戏开发者工具」，导出后用它打开产物目录 |
| 引擎 | Cocos Creator 3.x（平台已完成引擎适配，无需自己写 adapter） |

## 1. 抖音小游戏的本质

它不是一个网页，而是一个**绑定了一批 `tt` API 的 JavaScript 虚拟机**：

- **没有 `BOM` / `DOM`**：`window`、`document`、`localStorage` 都不存在；
- 画布只能通过 `tt.createCanvas()` 拿，第一次调用返回的是**上屏 Canvas**（与屏幕等宽等高），全局有且仅有一个；
- 文件读写走 `FileSystemManager`，不是 `fs`；
- 触摸事件走 `tt.onTouchStart/Move/End/Cancel`。

Cocos 之所以能直接跑，是因为引擎内置了一层 adapter，把 `document.createElement('canvas')` 这类调用映射到 `tt.createCanvas` / `tt.createImage` 上。**这层是引擎做的，不要自己再抹平一遍。**

## 2. 最小项目结构

```
├── game.js              // 入口，先执行
├── game.json            // 小游戏配置（屏幕方向、分包、Worker…）
└── project.config.json  // 工程配置（appid、ES6 开关…）
```

其余目录（`assets`、`js`、`audio`、`images`）可自由组织。三个文件缺一不可，缺 `game.json` 直接起不来。

## 3. Cocos 导出

1. Cocos Creator 打开项目 → **构建发布**，平台选「字节跳动小游戏 / 抖音小游戏」；
2. 填 AppID，选择是否远程资源（`build/bytedance-mini-game` 目录）；
3. 构建完成后，用抖音开发者工具「导入项目」，指向构建产物目录（不是 Cocos 工程目录）；
4. 首次导入若提示缺 `project.config.json`，让工具自动生成并补上 AppID。

> 构建产物里的 `game.js` 是 Cocos 的启动壳，真正的引擎代码在 `cocos-js/` 下，**不要手改**，改了下次构建就没了。

## 4. 生命周期

| 时机 | 用什么 |
|---|---|
| 冷启动参数（分享带过来的 query、场景值） | `tt.getLaunchOptionsSync()`，**必须在首帧前取** |
| 切后台 / 回前台 | `tt.onHide` / `tt.onShow` |
| 内存告警 | `tt.onMemoryWarning` |

冷启动与热启动的差别很大：热启动是进程还在、从后台恢复，不会重新执行 `game.js`。所以**不要把「初始化」写死在脚本顶层**，要区分「首次进入」和「恢复」。

## 5. 预览与调试

- **模拟器**：开发者工具内直接跑，快但**不代表真机表现**（尤其性能、音频、广告）。
- **真机预览**：扫码在抖音里打开，是最接近线上的验证方式。
- **vConsole / 实时日志**：见 `devtools.md`。
- 上线前至少覆盖：iOS + Android 各一台中低端机、弱网、切后台再回来。

## 6. 上传与提审

1. 开发者工具「上传」→ 填版本号与备注；
2. 后台「版本管理」提交审核，需要先完成：类目、资质、备案、隐私协议、适龄提示；
3. 审核通过后发布。首次发布前必须接入「必接能力」（侧边栏复访等），否则会被驳回。

细节见 `security-release.md`。

## 7. 常见启动失败

| 现象 | 原因 |
|---|---|
| 白屏，无报错 | `game.js` 里首帧渲染前抛异常，被引擎吞了；开 vConsole 看 |
| 提示找不到 `game.json` | 导入的是 Cocos 工程目录而不是构建产物 |
| 屏幕方向反了 | `game.json` 的 `deviceOrientation` 默认是 `landscape`，竖屏游戏必须显式写 `portrait` |
| 真机闪退 | 包体超限或内存超限，见 `performance.md` |
| 广告/支付调不通 | 后台能力未开通，代码没问题 |
