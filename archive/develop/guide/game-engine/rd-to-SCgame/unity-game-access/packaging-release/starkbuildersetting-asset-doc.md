---
title: "StarkBuilderSetting.asset 配置文件说明"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/packaging-release/starkbuildersetting-asset-doc
update_time: 2025-12-26
---

位于 `Assets/Editor/StarkBuilderSetting.asset` 即为 TTSDK 的导出配置文件，其中部分配置可在抖音小游戏导出面板中可视化配置，本节将对配置文件中各项字段进行说明，开发者可直接修改其配置内容。
## 项目配置

| 字段 | 说明 |
| --- | --- |
| AppId | 小游戏的 AppId |
| version | 小游戏的版本号 |
| ~~AutoVersion~~ | 已废弃，不再使用 |
| Orientation | 屏幕方向 |
| iOSPerformance Plus | iOS 下是否开启高性能+ |
| MenuButton Style | 功能按钮颜色，见 https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/mini-game-configuration |
| ~~PublishType~~ | 已废弃，不再使用 |
| ~~Publish Desc~~ | 已废弃，不再使用 |

## 开发者工具配置

| 字段 | 说明 |
| --- | --- |
| IdePath | 开发者工具的可执行文件路径，Windows 下以 exe 结尾，Mac 下以 app 结尾。配置后，可在构建面板直接跳转至抖音开发者工具 |
| IsOld Build Format | 是否以旧有的构建方式构建包体，旧有方式构建出的包体为 zip 包，新版方式构建结果为与普通小游戏类似的工程目录 （TTSDK 6.6.3及以上支持），具体详情可参考[Unity包体格式更新](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/unity-new) |

## WebGL方案相关配置

| 字段 | 说明 |
| --- | --- |
| Wasm Resource Url | WebGL 模式下音频资源的 url |
| OutputDir | 产物生成目录 |
| UseByteAudioAPI | 对应 WebGL 构建面板上的复制音频文件，开启会自动将工程目录中的音频文件以工程目录的结构复制出来 |
| Wasm Memory Size | 对应 WebGL 构建面板上的 UnityHeap，用于设置游戏的堆内存大小 |
| IsWebGL2 | 是否以 WebGL 2.0 的方式进行构建 |
| NeedCompress | 是否开启 brotli 压缩，默认需要开启，否则会影响游戏的启动速度 |
| SymbolMode | 符号表的开启模式，有三个取值 Off/External/Embeded ，对应 PlayerSettings.WebGL.debugSymbolMode |
| Profiling | 是否开启运行的性能检查，仅在测试版可用，线上版本需关闭 |
| ClearStreamingAssets | 是否将构建产物目录中的 SteamingAssets 目录情况，并移除目录 |
| BuildOptions | 构建产物是的构建选项，对应 Unity 的 BuildOptions |
| WasmSubFramework | Wasm 构建方案的选项，取值 WebGL/MiniGame，仅在团结引擎上适用。对应构建产物是原始 WebGL 产物还是团结引擎小游戏的产物。 |
| HideAfterCallMain | true：在callmain阶段结束后立即隐藏封面视频 false：等待首帧渲染回调后隐藏【默认】 *注：仅新包体格式支持，详情见：*[*Unity包体格式更新*](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/unity-new) |
| DisableLoadingPage | 是否禁止加载页面 *注：仅新包体格式支持，详情见：*[*Unity包体格式更新*](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/unity-new) |
| UseDataCDNAsStreamingAssetsUrl | 是否将 DATA_CDN 的地址作为 Application.streamingAssetsPath 的路径 |
| OptimizeWebGLMemoryInBackground | 是否在游戏切后台之后，优化游戏所占内存，降低后台崩溃概率 |
| AssetBundleFSEnable | 是否开启 TTAssetBundle 对内存的优化 |
| AssetBundleBufferCapacity | 缓存超过此数值，将会被清理 |
| AssetBundleBufferTTL | AssetBundle 缓存超过这个时间未使用，将被清理，单位：秒 |
| PreloadFiles | 对应构建面板上文件列表，支持模糊匹配 |
| CDN | 对应构建面板上的游戏资源 CDN，构建工具会拼接 CDN 与模糊匹配的文件列表进行预下载 |
| PreloadDataListUrl | 对应构建面板上的动态资源列表接口。开发者可配置动态加载的资源列表接口 |
| iOSDevicePixelRatio | 设备像素比 |
| UrlCacheList | 缓存列表，对应构建面板缓存资源域名 |
| DontCacheFilesNames | 缓存资源域名列表中，不缓存的文件名 |

## Native方案相关配置

| 字段 | 说明 |
| --- | --- |
| IsDevBuild | 是否构建 debug 版本 |
| StripEngineCode | 是否裁剪引擎代码 |
| AppHost | 宿主类型 |
| CompressMethod | 是否压缩，以及压缩方案选择 |
| RuntimeEnv | 默认为 latest，不可修改 |
| FrameWork | 游戏方案类型，Native ，WebGL，UnityInstantGame， |
| Architecture | 架构类型，默认为 ALL，线上不支持单架构方案 |
| MiniApkVersion | 最低 Android API 版本 |
| ScriptingBackground | 脚本后端，IL2CPP/Mono |
| ~~NativeWhiteListRegex~~ | 不再维护 |
