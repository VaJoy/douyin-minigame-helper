# 配置文件与分包

> **适用**：`game.json`、`project.config.json`、`subPackages` 的结构与坑。
> **源文档**：`docs/develop/framework/mini-game-configuration.md`、`docs/develop/guide/basic-function/subpackages/`、`docs/develop/dev-tools/code-edit/`。
> **关联**：分包加载 API 见 `api-index.md`；包体与启动优化见 `performance.md`。

## game.json

根目录下的 JSON，决定运行时行为。全部字段：

| 字段 | 类型 | 默认 | 说明 | 最低版本 |
|---|---|---|---|---|
| `deviceOrientation` | string | `landscape` | 屏幕方向：`portrait` / `landscape` | – |
| `showStatusBar` | boolean | `false` | 是否显示状态栏 | – |
| `networkTimeout` | object | – | 各类请求超时时间（毫秒） | – |
| `workers` | string | – | Worker 代码所在目录 | – |
| `openDataContext` | string | – | 开放数据域目录 | 1.11.0 |
| `subPackages` | array | – | 分包配置 | 1.88.0 |
| `menuButtonStyle` | string | – | 右上角更多面板深浅色 | 3.16.0 |
| `enableIOSHighPerformanceMode` | boolean | `false` | iOS 高性能模式 | 3.43.0 |
| `plugins` | object | – | 插件配置（内测，不用的删掉，否则可能编译报错） | 3.65.0 |
| `ttNavigateToMiniGameAppIdList` | string[] | – | 已废弃，不要用 | 1.23.0 |

**最容易踩的一条**：`deviceOrientation` 默认是 **landscape**。竖屏游戏不写这一行，真机上就是横的。

```json
{
  "deviceOrientation": "portrait",
  "openDataContext": "openDataContext",
  "networkTimeout": { "request": 10000, "downloadFile": 30000 }
}
```

## project.config.json

工程级配置，主要是 AppID 与编译开关：

```json
{
  "description": "项目描述",
  "appid": "ttxxxxxxxxxxxxxxxx",
  "setting": { "es6": true }
}
```

- `setting.es6` 决定是否走 ES6 转 ES5，老设备兼容性靠它。
- 这个文件由开发者工具生成/维护，手改容易被覆盖。
- Cocos 构建产物默认不带 `project.config.json`，导入时由工具补。

## 分包（subPackages）

基础库 **1.88.0+**，开发者工具 **2.0.6+**。目的：主包体积压到限制内，把非首屏资源拆出去。

```json
{
  "subPackages": [
    { "name": "stage1", "root": "stage1/" },
    { "name": "stage2", "root": "stage2.js" }
  ]
}
```

| 字段 | 说明 |
|---|---|
| `name` | 分包别名，`tt.loadSubpackage({ name })` 用它 |
| `root` | 分包根目录（自动加载目录下的 `game.js`）或单个 js 文件 |

注意是 **`subPackages` 驼峰**，写成 `subpackages` 不生效且不报错。

加载：

```js
const task = tt.loadSubpackage({
  name: 'stage1',
  success() { console.log('分包加载完成'); },
  fail(e) { console.warn('分包失败', e); },
});
task.onProgressUpdate((res) => console.log(res.progress)); // 0-100
```

要点：
- `tt.loadSubpackage` 返回 `LoadSubpackageTask`，可以拿进度做 loading 条。
- 分包里的资源路径是相对分包根的，跨包引用要在主包里留索引。
- 分包不是「懒加载一切」的银弹：主包仍要放引擎核心与首场景，否则启动会二次等待。
- **用 Cocos 的话不用手写这段配置**：在资源管理器把文件夹「配置为 Bundle」、压缩类型选「小游戏分包」，构建时会自动生成 `subPackages`。配置步骤与体积限制见 `cocos-publish.md`。

## 灰度

后台「版本管理」支持按比例灰度发布，见 `docs/develop/guide/basic-function/subpackages/game-gray.md`。灰度期间新旧版本共存，**服务端协议要向前兼容**，不能假设客户端一定是新版本。

## 版本兼容

- `tt.getSystemInfoSync().SDKVersion` 是判断基础库版本的唯一可靠来源，格式 `x.y.z`。
- 比较版本不要用字符串比较（`'1.10.0' < '1.9.0'` 会为 true），要按段转数字比。
- 新 API 一律 `tt.canIUse('方法名')` 先判断，再决定降级路径。
