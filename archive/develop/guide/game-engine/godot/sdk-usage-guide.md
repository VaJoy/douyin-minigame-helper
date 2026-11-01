---
title: "SDK使用说明"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/godot/sdk-usage-guide
update_time: 2026-07-15
---

> 前置阅读：[抖音小游戏Godot接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/godot/godot-engine-integration-guide)

## 一、插件安装
- 下载 zip 包并解压后，将 `ttsdk` 和 `ttsdk.editor` 放到项目的`addons`目录，从 Project Settings 中勾选激活插件即可。
> Godot 插件安装方法请参考 [官方文档](https://docs.godotengine.org/zh-cn/4.x/tutorials/plugins/editor/installing_plugins.html)

| 版本号 | 更新日期 | 更新说明 | 下载链接 |
| --- | --- | --- | --- |
| 1.0.4 | 2026/7/15 | feat: 新增 TTVideoStreamPlayer 支持 mp4 播放 feat: 打包新增 iOS 高性能+ 开关 |  |
| 1.0.3 | 2026/1/28 | fix: 修复音频兼容性问题 |  |
| 1.0.2 | 2026/1/15 | feat: 增加横屏导出支持 |  |
| 1.0.1 | 2025/12/22 | fix：旧版本抖音加载卡住问题 |  |
| 1.0.0 | 2025/11/27 |  | 版本废弃不再使用 |

## 二、TTSDK 使用基础
### 接口说明

> `ttsdk` 插件激活后会注入一个**名为 **`tt`** 的全局对象（Autoload）**，SDK 接口都通过该对象提供。

#### `func is_run_in_tt() -> bool`
- 返回
    - 当前是否运行在抖音小游戏环境中
#### `func mount_ttpkg_file(path: String) -> void`
- 说明
    - 访问包内文件之前须先调用 `mount_ttpkg_file` 将包内文件挂在到虚拟文件系统中
- 参数
    - `path`
- 调用示例

```python
tt.mount_ttpkg_file("in/package/file.pck")
ProjectSettings.load_resource_pack("in/package/file.pck")
```

#### `func create_video_stream(url: String) -> VideoStream`
- 说明
    - 创建一个基于 `tt.createOffscreenVideo` 的 `VideoStream`，配合 `VideoStreamPlayer` 使用
    - 注意这种方式创建的 `VideoStream` 不支持通过`VideoStreamPlayer` 调节音量、播放速度
- 参数
    - `url` 视频文件地址
- 调用示例

```python
@onready var player: VideoStreamPlayer = $VideoStreamPlayer
# volume_db、speed_scale、loop/mute 属性无效
func play_tt_video_with_builtin_player(url: String) -> void:
    var stream := tt.create_video_stream(url)

    player.stream = stream
    player.paused = false
    player.play()

func pause_video() -> void:
    player.paused = true

func resume_video() -> void:
    player.paused = false

func stop_video() -> void:
    player.stop()
```

#### `class TTVideoStreamPlayer`
- 说明
    - 基于 `tt.createOffscreenVideo` 进行视频播放，支持音量调节
    - 可直接作为独立的 `Control` 节点使用
    - 注意在编辑器环境使用的是 mock 代码仅保证不报错，不实际播放视频
- 调用示例

```python
const VIDEO_URL := "https://example.com/video.mp4"
@onready var player: TTVideoStreamPlayer = $TTVideoStreamPlayer
func play_tt_video(url: String) -> void:
    player.canplay.connect(_on_video_canplay)
    player.played.connect(_on_video_played)
    player.paused.connect(_on_video_paused)
    player.stopped.connect(_on_video_stopped)
    player.ended.connect(_on_video_ended)
    player.error.connect(_on_video_error)

    player.autoplay = true
    player.loop = false
    player.muted = false
    player.volume = 1.0
    player.size_mode = TTVideoStreamPlayer.SizeMode.WIDTH_EXPAND

    player.load(VIDEO_URL)

func pause_video() -> void:
    player.set_paused(true)

func resume_video() -> void:
    player.set_paused(false)

func stop_video() -> void:
    player.stop()

func seek_to_10s() -> void:
    player.seek(10.0)
```

### 调用开放能力

> Godot TTSDK 对抖音小游戏 [JavaScript API](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/overview) 进行了调用封装，**相关接口说明直接参考 API 文档即可**。

目前已支持的接口清单请查看 `tt.gd`，其余接口也会陆续上线。
- 代码示例：获取用户信息

```text
extends Node
class_name CallTTSdkSample

func _on_button_pressed():
    var res = await tt.login()
    if res.is_success:
        res = await tt.get_user_info()
        if res.is_success:
            var user_info := res.get_result_success();
            print(user_info)
            
```

#### **2.1 类型转换**
- 通过 Godot SDK 调用 API 时，需要注意参数类型转换。具体规则如下：
  - **大部分情况下，SDK 已经替开发者完成了类型转换**，有少数情况需要开发者自行关注

| JS 类型 | Godot 类型 | 是否直接使用 | 备注说明 |
| --- | --- | --- | --- |
| `number` | `Variant` | 直接使用 | JS 不区分 int 和 float |
| `string` | `String` | 直接使用 |  |
| `boolean` | `bool` | 直接使用 |  |
| `Object` | `JavaScriptObject` |  | Godot -> JS 方向：向 SDK 传入 `Dictionary` 类型即可 JS -> Godot 方向：没有显式标注为其它类型的，可以用 `TTUtils.dictionary_from_js` 方法转成 `Dictionary` |
| `Array` | `JavaScriptObject` |  | Godot -> JS 方向：向 SDK 传入 `Array` 类型即可 JS -> Godot 方向：没有显式标注为其它类型的，可以用 `TTUtils.array_from_js` 方法转成 `Array` |
| `Function` | `JavaScriptObject` |  | Godot -> JS 方向：向 SDK 传入 `Callable` 即可 |
| `ArrayBuffer` | `JavaScriptObject` |  | 暂无此类接口 |

- 举例说明
  - `tt.createBannerAd`

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/d02b7ea7b909459ebc4c229b864b3c73~tplv-9nona0m7ha-image.image)

    - 对应的 JavaScript API 方法签名为：

```typescript

function createBannerAd (param: {
    adIntervals?: number;
    style?: { width: number; left: number; top: number };
    adUnitId: string;
  }): BannerAd;
```

    - Godot 接口调用格式为：

```python
# Godot API 调用
var param : Dictionary = {
    "adIntervals": 1,
    "adUnitId": "ad-unit-id",
    "style": {
       "width": 120
    }
}
# param 在 SDK 内部被转换为 JavaScriotObject
tt.create_banner_ad(param) 
```

#### **2.2 接口格式**
- 遵循 Godot 代码风格，Godot API 均以 **snake-case** 格式命名；
  - 例如 JS 的 `tt.createBannerAd` 接口在 Godot 中通过 `tt.create_banner_ad` 方法进行调用。
- Godot TTSDK 目前有 **3 种接口调用格式**，分别是 **同步、异步、以及 signal**；
  - **格式一：同步接口调用**，所有同步返回的 JavaScript API 可以直接调用

```python
var system_info := tt.get_system_info_sync()
print(system_info)

var banner_ad := tt.create_banner_ad({
    ""
})

get_tree().root.add_child(banner_ad)
banner_ad.on_load.connect(...)
banner_ad.show()
banner_ad.destroy()
banner_ad.queue_free()
```

  - **格式二：异步接口调用**，Godot SDK 对异步返回的 JavaScript API 进行了二次封装（`TTAsyncTask`），开发者可以采用下面任意的格式进行调用，底层实现是相同的。
    - **以方法形式调用**：使用 Dictionary 作为入参，不支持监听回调。请注意 Dictionary 内字段命名应与 JavaScript 接口文档定义保持一致（**camel-case**）

```python
await tt.report_event({
    "event": "event-name",
    "extra": {
        "field 1": "abc"
    }
})
```

    - **以对象形式调用**：提供显式的字段定义，支持监听回调，也支持协程格式

```python
var task := await tt.login_async() # 方法名多了 _async 后缀

# 提供显式参数字段名，snake-case
task.force = true

# 协程格式调用
await task.invoke()
if task.is_success:
    var res := task.get_result_success();
else:
    print (task.get_result_fail())
```

```text
var task: TTAsyncTask = await tt.login_manual()
# 非协程格式
task.invoke()
if task.is_done:
    if task.is_success:
        _on_login_success(task.get_result_success())
    else:
        _on_login_fail(task.get_result_fail()）
else:
    task.on_success.connect(_on_login_success, CONNECT_ONE_SHOT)
    task.on_fail.connect(_on_login_fail, CONNECT_ONE_SHOT)
```

  - **格式三：事件监听类接口**，Godot SDK 对 `onXXX/offXXX` 格式的 JavaScript API 提供了 signal 封装。

```python
tt.on_show.connect(_on_show)    # 对应 JavaScript tt.onShow 接口
tt.on_show.disconnect(_on_show) # 对应 JavaScript tt.offShow 接口

func _on_show(res: TT.OnShowRes) {
    print(res)
}
```

#### **2.3 内存管理**
- 调用 JavaScript API 时涉及到 Godot 与 JS 之间的内存交换，内存管理的关键是意识到 Godot 的内存对象管理是基于引用计数（`RefCounted`）而 JavaScript 则是基于垃圾回收的，Godot 引擎会在 `JavaScriptObject` 引用结束时释放 JS 对象。
- 通常情况下，开发者无需关注接口调用内存管理的细节。
  - **特别的，**`TTBannerAd`** 这类带生命周期**的对象是基于 `Node` 实现的，开发者可以像普通节点一样管理其生命周期，这类对象**需要开发者手段管理生命周期**（在合适的实际调用 `destroy`）。

## 三、导出工具
> Godot SDK 提供工具将 Godot 项目导出为抖音小游戏格式，导出后使用抖音开发者工具运行调试与上传发布
> 参考文档：
> - [抖音开发者工具 - 概览](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/mini-app-developer-instrument)
> - [抖音开发者工具 - 下载](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/developer-instrument-update-and-download)
> - [抖音开发者工具 - 调试控制台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/game-debug/v-console)
> - [抖音开发者工具 - 真机调试](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/game-debug/real-machine-adjust)
> - [抖音开发者工具 - 版本上传](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/mini-app-developer-instrument#a0e1724d)
### 使用基础
- 激活 ttsdk 插件后，导出界面会新增 `tt-minigame` 导出平台，填写参数后点击导出项目，选择导出路径即可导出抖音小游戏项目。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/4770f8166d2f4d719aee4e0ba130fbbe~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/4811449c034343228f9f0519d246bb3c~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b660b1f9bc854269a0a4d4249a28c369~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/f2412851ab4741d49b9b2c1e23376118~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/36244fb1579a42e4af961d23ff41c06f~tplv-9nona0m7ha-image.image)

- 注意事项：
  - 导出 pack 时应该剔除 `addons/ttsdk.editor` 目录；
  - 抖音小游戏暂不支持上传`.pck`文件，因此`.pck`在导出后会被 SDK 重命名为`.bin`（或`.br`，如果开启 brotli 压缩）。但 godot 代码中仍然可以使用`.pck`对文件进行加载；
    - 另外，导出的小游戏目录中仍然保留了`.pck`文件，该文件不会计入包大小计算，仅仅是为了下次仅导出 pack 时方便选择覆盖。
  - 暂不支持将 pack 导出成 `.zip` 格式（性能不如`.pck`）；
  - 暂不支持自定义导出模板；（附：SDK 内置导出模板构建）

附件下载：[custom.py.txt](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/59d6bf63f9e94969bf555bea9276f578~tplv-9nona0m7ha-image.image)

### 导出参数说明

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| `Douyin/App ID` | String | 小游戏的 App ID |
| `Douyin/Canvas Resize Policy` | enum | 同 Web 导出的 [Canvas Resize Policy](https://docs.godotengine.org/en/stable/tutorials/platform/web/html5_shell_classref.html#canvasResizePolicy) |
| `Douyin/Subpackage On` | bool | 开启后 wasm 和 main pack 会被打进子包中 用到 subpackage 能力时必须开启 |
| `Douyin/Enable iOS Hpp` | bool | 在 iOS 上使用高性能 + 模式 |
| `Douyin/Custom Game Js` | bool | 开启后重复导出不会覆盖 game.js 文件 自定义 game.js 时可以开启 |
| `Douyin Debug/Remote Debugger On` | bool | 开启远程调试，游戏启动后自动连接 godot 调试器 |
| `Douyin Debug/Remote Debugger Url` | String | godot 调试服务地址，格式为 `ws://xx.xx.xx.xx:xxxx` |
| `Douyin Optimize/Brotli On` | bool | 开启后，对 pack 进行 brotli 压缩 |
| `Douyin Optimize/Brotli Policy` | enum | brotli 压缩策略 |
| `Douyin Experimental/Audio Context` | bool | 开启后会使用新的音频接口，对旧版本抖音的兼容性会更好 |

### 功能指引
#### 3.1 使用 remote debugger 进行调试
- 在导出界面勾选 Remote Debugger On 参数可以使用 godot 调试器对小游戏进行调试。
- 连接调试器时，请确保以下几个事项：
- 1）godot debug 服务可以通过局域网进行访问；
  - 设置 Editor Settings -> Network -> Debug -> Remote Host 为局域网可访问地址

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/f334ec6eb41f48e19d42796a7404199c~tplv-9nona0m7ha-image.image)

- 2）godot 调试服务已开启；
  - 勾选 Debug -> Keep Debug Server On

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b27c5a56a4384f0cb0499ac4647c41f4~tplv-9nona0m7ha-image.image)

#### 3.2 使用 brotli 对资源进行压缩

> 注意：brotli 对 godot pack 资源文件的压缩率取决于 pack 内资源的内容，具体情况因项目而异，请谨慎使用。

- 当出现包体过大的情况时，可以借助 SDK 提供的 brotli 压缩能力对资源进行压缩。
  - Brotli Policy：
    - Auto：根据 debug/release 自动选择
    - Fast：compression level 5
    - Size：compression level 9

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/3c1dcae09d97401089eacc8359bd8c2d~tplv-9nona0m7ha-image.image)

- 经过 brotli 压缩后的资源后缀为 `.br`，但是在 godot 内仍然可以使用 `.pck` 进行文件加载。

#### 3.3 使用分包能力加载资源包
- 当游戏的资源包较大时，可以使用分包策略将部分非首场景使用的资源打包到子包内，在运行时进行动态加载，从而达到缩短首场景启动耗时的效果。
- SDK 提供了名为 `tt-minigame-subpackage` 的导出平台，来辅助完成资源分包过程。
- 使用示例：

1）在主包打包选项中，打开 Subpackage On 开关。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/bbb2640da90c49cb991ad7d0695e9939~tplv-9nona0m7ha-image.image)

2）新增 `tt-minigame-subpackage` 平台预设并填写参数，其中：
  - Project Config File 选择已导出的小游戏项目的 `project.config.json` 文件；
  - Subpackage Name 是子包名称，后续用于子包的加载。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/ba43674b114f4800bb50751c39ddc6ea~tplv-9nona0m7ha-image.image)

3）根据需要配置导出 Resource 清单，尽量不与主包发生重叠。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/73d721a2b89949b2b14636203394e0fe~tplv-9nona0m7ha-image.image)

4）点击 Export PCK/ZIP，选择导出目录和导出文件名后点击保存。点击 Save 后会在小游戏工程中自动创建子包。
  - 可以将多个 PCK 导出进同一个子包内。
  - 注意导出的目标目录须是小游戏项目的子文件夹。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/a689b152083c46e9bde8513aa0b95745~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/5482c2d311e94a56bd45d79a6e5c83d0~tplv-9nona0m7ha-image.image)

5）在代码里加载子包资源：

```python
var packed_scene_res_path = "res://example/demos/audio/audio_effects.tscn"
if !ResourceLoader.exists(packed_scene_res_path):
        # 加载子包
    var task = await tt.load_subpackage({
        "name": "audio" # 子包名称
    })
    if !task.is_success:
        # 加载失败，打印错误信息
        printerr("failed to load subpackage", task.get_fail_result())
        return null
    # 子包内的资源文件的导出路径，使用小游戏工程根目录的相对路径
    var path = "subpackages/audio/data.pck"
    # 加载包内文件必须先调用 mount_ttpkg_file 接口
    tt.mount_ttpkg_file(path)
    # 加载 pack 资源文件
    if !ProjectSettings.load_resource_pack(path):
        printerr("failed to load resource pack");
        return null
```
