---
title: "C# SDK 发版记录"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/update-record/sc_changelog
update_time: 2026-10-15
---

## TTSDK
### [6.9.5]-2026.10.15
Feature] 团结引擎试玩广告适配
[Optimize] 优化报错提示
[Feature] 新增多包融合工具
### [6.9.4]-2026.9.17
[Feature] 增加了一些打包提示
[Feature] 支持更高版本的 Unity 和团结引擎
[Feature] 优化了一些 GC 问题
[BugFix] 修复新包体格式音频资源 url 失效的问题
[BugFix] 修复 GLX 播放广告后音频消失的问题
### [6.9.3]-2026.9.7
[Feature] 支持 EmscriptenGLX 及新的构建工具
[Feature]【小游戏】厂商开放能力 · 分享得好礼
[BugFix] 修复 TTAssetBundle 潜在的内存泄漏问题
### [6.9.1]-2026.8.25
[Feature] 全端经营能力增加拉端 API
[BugFix] 特定情况下分包缺失字段的问题
### [6.9.0]-2026.8.11
[Feature] 新增小游戏音频播放路由控制
### [6.8.0]-2026.7.27
[Feature] wasm新分包方案上线。
### [6.7.9]-2026.7.13
[Feature] 隐私接口新增授权
[Feature] 新包体格式适配鸿蒙平台
[Bugfix] 修复不勾选压缩首包资源时 IDE 无法进入的问题
### [6.7.7]-2026.6.12
[Feature] 游戏维度玩家多场景通行能力
[Feature] 支持团结引擎新的buildTarget
[Feature] 新增wasm分包相关字段
### [6.7.6]-2026.5.30
[Feature] 试玩广告能力增加接口
### [6.7.4]-2026.4.21
[Feature] 支持小游戏分享至日常体裁
[Optimize] 优化cdn模式打包流程
[Bugfix] 修复metal下摇杆问题
### [6.7.3]-2026.4.7
[Feature] iOS 端支持 EmscriptenGLX
[Feature] 支持全端经营能力
[BugFix] Custom Template兼容starksdk
### [6.7.2]-2026.3.23
[Feature] 首包资源支持开发者配置 CDN 的方式进行加载
### [6.7.1]-2026.3.11
[BugFix] 修复 WebGL 新包体，非抖音宿主金币功能异常
### **[6.7.0]-2026.3.9**
[Feature] 平台实时语音能力优化
### [6.6.9]-2026.2.10
[BugFix] 修复 IDE 环境网络请求异常问题
[BugFix] 修复特定场景内存泄漏
[BugFix] 修复特定游戏加载失败
### [6.6.8]-2026.1.26
[Bugfix] 修复 Metal 模式下 GC 异常的问题
[Bugfix] 异常上报信息修复
### [6.6.7]-2026.1.12
[Bugfix] 修复Android在监听OnShareAppMessage时拉起两个分享弹窗
[Bugfix] JS加载失败
[Bugfix] 混合引擎链路，使用远程StreamingAsset资源加载TTAB失败的bug
### [6.6.5]-2025.12.29
[BugFix] 预下载配置支持aa路径&&修复构建结果appid填充不正确的问题
[Optimize] 增加对Eventsystem.current的判空逻辑
### [6.6.4]-2025.12.17
[Feature] 新增调用IM能力
### [6.6.3]-2025.12.14
[Feature] 混合引擎构建选项入口完全放开
[Feature] 支持游戏自定义动态分享图片
### [6.6.1]-2025.12.1
[Feature] 文件系统Write接口增加position字段
[Feature] OnShow事件增加showFrom字段
### [6.6.0]-2025.11.17
[Bugfix] 修复6.5.9TTSDK版本报错问题
[Bugfix] 修复混合引擎cp自定义代码无法执行的问题
### [6.5.9]-2025.11.3
[Feature] 激励分享拓展小游戏题材
[Feature] 新增团结引擎 Metal 能力适配
[Feature] PC 抖小逻辑兼容
### [6.5.8]-2025.10.24
[Bugfix] 修复文字渲染异常问题
### [6.5.7] - 2025.10.17
[Feature] 增加云抖小 GetPhoneNumberAuthState、GrantPhoneNumber、ShowCloudGame 接口
[Bugfix] 修复未设置 Unity Profiler IP 时提示报错的问题
[Bugfix] 修复模板拷贝不正确的问题
### [6.5.6] - 2025.9.28
[Feature] 增加 PreloadConcurrent、SetPreloadList 接口
### [6.5.5] - 2025.9.19
[Bugfix] 修复团结引擎下使用 douyin_profile 构建时会出错的问题
### [6.5.4] - 2025.9.5
[Feature] 新增错误监听 onError 接口
[Feature] 新增 OnMemoryWarning 接口
[Feature] 新增获取设备当前的地理位置接口
[Feature] 新增 TriggerGC 接口
[Feature] 新增二维码扫码接口
### [6.5.3] - 2025.9.1
[Feature] 新增录音相关接口
[Feature] 新增罗盘相关接口
[Feature] 新增缓存文件清理接口
[Feature] 新增即看即玩接口
### [6.5.2] - 2025.8.25
[Feature] 交互弹窗类接口接入
[Feature] 新增混合引擎功能
[Optimize] GetSystemInfo 不依赖 TT.InitSDK 接口
[Optimize] 不再支持开发者配置 apk 的基础名称
### [6.4.5] - 2025.8.8
[Feature] 非抖音宿主增加客服能力
### [6.4.4] - 2025.8.1
[Feature] 增加图片操作接口：ChooseImage、PreviewImage、GetImageInfo
### [6.4.3] - 2025.7.25
[Feature] 支持群铭牌设置查询接口
[Bugfix] 修复团结引擎 build profile 面板 config 配置为空时读取错误的问题
### [6.4.2] - 2025.7.18
[Bugfix] 修复保存数据时日志错误打印的问题
[Bugfix] 修复未正确统计已使用磁盘空间大小的问题
### [6.4.1] - 2025.7.11
[Feature] 增加群铭牌接入能力
### [6.3.9] - 2025.6.26
[Feature] 增加跳转反馈页能力
[Feature] 新增接口-保存图片到相册
[Feature] 团结引擎在 buildTarget 上增加子平台的超链接
### [6.3.8] - 2025.6.19
[Bugfix] 修复 IDE 中音频 OnStop 回调触发 OnEnd 事件的问题
[Feature] 增加文件流式读写能力
### [6.3.7] - 2025.6.12
[Bugfix] 修复[团结引擎]development 版本打包时的报错问题
### [6.3.6] - 2025.5.29
[Feature] 增加UnityVideoPlayer的适配
### [6.3.4] - 2025.5.19
[Feature] 增加OnWindowResize接口
### [6.3.3] - 2025.5.12
[Feature] 增加StoreFeedData、GetFeedData接口
### [6.3.2] - 2025.04.24
[Feature] 增加振动接口
[Bugfix] 修复 UDPSocket 对象销毁时报错的问题
[Bugfix] 修复 StarkAudioManager 回调未触发的问题
[Bugfix] 修复 Unity 2022 及以上版本调用 TTKeyboard 报错的问题
### [6.3.1] - 2025.04.08
[Feature] 增加转屏接口
### [6.3.0] - 2025.03.27
[Feature] 构建工具提供预下载配置能力
[Feature] 在团结引擎 1.5.0 及以上版本支持 MiniGame 导出、完善了对团结 MiniGame 产物的适配
### [6.2.7] - 2025.03.13
[Feature] 新增设置渲染精度接口
[Bugfix] 修复多点触控 EditorMockEnabled 调试开关不生效的问题
### [6.2.6] - 2025.03.05
[Bugfix] 修复 LogManager 无法在 Application.logMessageReceived 方法中调用的问题
### [6.2.5]- 2025.02.20
[Feature] 添加设置帧率能力
[Feature] 直播扩展组件能力补充
[Feature] 补齐 WebGL 新文件系统 AppendFile/AppendFileSync/ReadDir/ReadDirSync/Truncate/TruncateSync API
### [6.2.4]- 2025.02.14
[Feature] Feed直玩添加从Feed流进入游戏、游戏退回到Feed流的监听
[Bugfix] 修复 TT.GetSetting 始终返回空的问题
### [6.2.2]-2025.01.06
[Optimization] 广告接口功能优化
[Bugfix] 修复 PC 键鼠接口 CanIUse 功能
[Bugfix] 修复系统字体能力容错处理的问题
### [6.2.1]-2025.01.03
[Feature] 新增 PC 端小游戏键盘/鼠标/滚轮/光标样式相关接口
[Optimization] 广告接口功能优化
### [6.2.0]-2024.12.30
[Feature] 新增反馈日志、实时日志功能以及相关 API 接口
[Bugfix] 修复插屏和激励广告WebGL 方案 canIUse 接口始终返回 false 问题
[Bugfix] 修复购买礼包接口支持注册一次回调多次的问题
[Feature] Unity Tools 合并至 TTSDK，原 StarkUnityTools 废弃
### [6.1.3]-2024.12.17
[Feature] 新增设备网络相关能力 API
[Bugfix] 修复 Native 方案分享能力传入 query 时必然出现分享失败问题
### [6.1.2]-2024.12.09
[Bugfix] [重要] 修复文件系统接口 Access/WriteFile/CopyFile/RenameFile/Unlink/Mkdir/Rmdir 回调函数未释放问题
[Bugfix] 修复 TTAssetBundle 低版本降级能力构建时可能被代码裁剪的问题
### [6.1.1]-2024.11.25
[Feature] 新增公会群接口
[Feature] 新增支付礼包接口
### [6.0.9]-2024.11.11
[Bugfix] 修复使用 TTInputOverrideBypass 引起的 SDK 未初始化问题
[Bugfix] 修复在 IDE 模拟器中重启游戏报错的问题
### [6.0.8]-2024.11.05
[New] 新增游戏版本更新管理器能力
### [6.0.5]-2024.10.22
[Bugfix] 修复激励视频广告在 WebGL 下创建后立即播放的问题
### [6.0.3]-2024.10.21
[Bugfix] 修复 Native 方案激励视频广告播放的回调问题
### [6.0.2]-2024.10.16
[Bugfix] 修复Native方案直玩订阅能力不可用问题
### [6.0.1]-2024.10.15
[Bugfix] TTAssetBundle 优化能力兼容 Addressables 1.19 版本（参考文档：[使用 TTAssetBundle 优化内存](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc-webgl-tt-ab)）
### [6.0.0]-2024.10.11
[New] 升级了 API 的调用方式，由原来的 `StarkSDK.API` 升级为 `TT` 的调用形式（参考文档：[旧版 StarkSdk API 迁移 TTSDK API 说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/starksdk-migration-guide)）
[Feature] 提供了 TTSDK API 升级工具（参考文档：[TTSDK API 升级工具](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/ttsdk-api-upgrade-guide)）

## 旧版本 StarkSDK
### [5.52.12]-2024.09.25
[Bugfix] 修复侧边栏能力因缺少 complete 回调参数导致 successCallback 未触发的异常
[Bugfix] 屏蔽词检测接口特殊字符处理异常
[Bugfix] 登录接口补充实名制字段参数
### [5.52.10]-2024.08.06
[Feature]新增 TTAssetBundle 优化能力，需依赖 StarkSDK Unity Tools 3.31.2 及以上版本
### [5.52.4]-2024.06.25
[Feature]新增系统字体获取接口
### [5.52.0]-2024.06.06
[Feature]添加侧边栏福利能力支持
### [5.51.0]-2024.05.14
[Feature]适配 Unity 2022 版本
[Feature]适配团结引擎 1.0 版本
[Feature]新增启动场景数据上报接口（参考文档：[启动场景上报分析](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/startup-performance/startup-scene-analysis)）
[Feature]新增 UDP 网络通信接口（参考文档：[网络通信适配 - UDP 网络通信](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_network#1dbceceb)）
### [5.50.8]-2024.04.02
[Feature]新增 WebGL 多点触控适配（参考文档：[多点触控适配](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc-webgl-touch)）
### [5.50.6]-2024.03.26
[Bugfix]修复抖音云获取服务端数据为空的问题
### **[5.50.3]-2024.02.27**
[Feature]新增showShareMenu/hideShareMenu接口，控制菜单面板分享按钮显示
[Feature]WebGL方案新增NavigateToVideoView，接口对齐Native方案
[Feature]新增重启小游戏接口
[Feature]新增小游戏收藏引导接口
[Feature]新增获取授权信息以及打开授权面板能力
[Feature]新增调起实名认证接口
[Feature]新增复访引导弹窗接口
[Feature]新增IM客服接口
[Bugfix]修复抖音火山版获取hostEnum返回错误问题
[Bugfix]修复激励广告返回超时异常
### [5.49.2]-2023.11.30
[Bugfix]排行榜 getImRankData 数据解析问题以及小游戏返回数据兼容性问题
### [5.49.1]-2023.11.22
[Feature]新增金币游戏能力支持 API
[Feature]新增排行榜多分区支持
### [5.48.0]-2023.10.24
[Feature]新增右上角胶囊按钮位置 API
### [5.47.0]-2023.9.20
[Feature]首次启动参数增加LaunchFrom和Location获取
### [5.46.1]-2023.9.7
[Feature]新增订阅消息能力
[Feature]新增调起侧边栏能力
### [5.45.1]-2023.8.16
[Feature]新增抖音云能力
[Feature]新增敏感词检测并替换服务
### [5.44.0]-2023.7.18
[Feature]新增屏幕方向旋转能力
### [5.43.0]-2023.6.27
[Feature]新增广告上报sendtoTAQ能力
[Feature]新增屏幕亮度相关能力支持
[Feature]iOS WebGL添加桌面快捷方式能力支持
[Bugfix]WebGL获取游戏版本号问题
### [5.42.1]-2023.5.22
[Feature]新增群聊能力
[Feature]新增 onShow/onHide 方法来获取启动参数修改信息
### [5.41.3]-2023.5.10
[Feature]新增Android WebGL方案支付接口
[Bugfix]修复部分注释显示问题
### [5.41.2]-2023.4.25
[Feature]新增互推组件能力
[Feature]新增激励广告再次获取能力
[Feature]新增剪切板API
[Feature]新增GetLocalCachedPathForUrl / IsUrlCached接口
[Feature]新增Stat/StatSync/GetSavedFileList等filelist路径获取相关接口
### [5.40.8]-2023.3.23
[Feature] StarkSDK WebGL方案iOS系统增加OpenAwemeCustomerService接口用于iOS支付
### [5.40.5]-2023.3.20
[Feature] StarkSDK C#增加 StarkSDKSpace.StarkFileSystemManager 接口，支持新文件存储系统。（参考文档：[使用新文件系统说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_new_file_system)）
### [5.39.4]-2023.2.15
[Feature] StarkSDK C#增加小游戏 getRoomInfo 接口
[Feature] WebGL 支持插屏广告以及 banner 广告
### [5.38.4] - 2022.12.12
[Feature] StarkSDK C# 增加排行榜接口
[Feature] StarkSDK C# 增加激励广告 OnShow 回调
[Feature] StarkSDK C# 支持 WebGL 陀螺仪
### [5.36.2] - 2022.10.18
[Optimize] RTC接口调整
### [5.34.1] - 2022.8.18
[Feature] StarkSDK C# 增加 native 音频播放接口
[Feature] native音频播放接口：支持相对路径url播放
[Bugfix] 修复 RTC 默认 appid 实现，补充注释
[Optimize] 调整getLaunchOptionSync 的接口位置
[Bugfix] 修复 WebGL shareParam 透传问题
### [5.33.5] - 2022.7.25
[Optimize] 取消支付以及屏蔽多次点击逻辑
[Bugfix] UNBridge.jslib 兼容UTF8ToString
[Feature] 增加CreateInvitePanel接口
### [5.32.4] - 2022.7.8
[Feature] 添加tt.authorize接口
[Bugfix] jsonData double类型转换兼容 Int/Long, 防止getSystemInfoSync接口报错
[Feature] 添加敏感词检测
[Feature] 添加 RTC 语音能力（白名单）
### [5.28.0] - 2022.5.16
[Feature] 添加tt.request / innerRequest接口
[Feature] 增加getSystemInfo接口
[Bugfix] 修复WebGL shareVideo无回调的问题
### [5.24.0] - 2022.4.20
[Feature] Android WebGL支持快捷方式、手机震动接口
### [5.20.6] - 2022.4.6
[Optimize] Unbridge 迁移进 StarkSDKSpace中，避免和CP自己的类产生冲突
[Optimize] 启动参数内容对齐普通小游戏
[Feature] 录屏增加关键帧插帧接口
[Bugfix] 支付失败输出正确的 errCode
[Bugfix] 修正分享接口 query 的正确传输
### [5.18.0] - 2022.2.25
[Feature] 加入 OnShareAppMessage & OffShareAppMessage 接口
[Optimize] 去掉退出回调接口
[Bugfix] 修复WebGL下Save接口保存文件可能未保存成功的问题
[Bugfix] WebGL UNBridge 接口增加 Preserve 属性，防止代码被 stripped
[Feature] WebGL增加CanIUse接口
[Feature] WebGL 支持陀螺仪，增加陀螺仪接口
### [5.15.1] - 2022.1.13
[Feature] 增加GetSystemInfo接口（tt.getSystemInfoSync）
[Feature] StarkSDK增加退出接口
[Bugfix] 修复WebGL平台日志格式化bug
### [5.14.1] - 2022.1.5
[Feature] 增加跳转到抖音视频接口（与分享视频返回 Vid 配合使用）
[Feature] 增加接入小游戏支付接口
[Bugfix] 屏蔽互跳接口
### [5.9.0] - 2021.12.3
[Feature] 增加客服页接口
### [5.6.0] - 2021.10.28
[Feature] 增加对 WebGL 平台视频广告接口的支持
[Feature]实名认证加入回调
[Bugfix]录屏SDK更新
### [4.22.0] - 2021.07.26
[Optimize]移除无用的lib
[Optimize]非 SC 下也可以运行，此时广告接口返回失败
[Bugfix]修复缺失dll注释的问题
[Bugfix]修复banner广告创建时可能超出屏幕的问题
### [4.20.0] - 2021.07.26
[Bugfix]修复在 OnAwake 生命周期中调用 CanIUse 导致的 SC 版本号读取异常问题
[Bugfix]录屏SDK版本升级
### [4.17.4] - 2021.07.14
[Optimize]在创建广告时广告大小的限制区分了横竖屏
[Optimize]增加了广告位置和大小的限制，约束不能超出屏幕范围
### [4.17.0] - 2021.06.22
[Optimize]抖音lite，头条lite下支持miniapk安装
[Optimize]修复录屏相关 bug，增加录屏时间过短的状态和超时回调
[Optimize]env中增加懂车帝，摸摸鱼
### [4.6.147] - 2021.03.12
[Optimize]确保 enable_pangle 开启下，广告拉起逻辑正常
[Bugfix]修正了enable_miniapk开启下，安装引导包与安装快捷方式的路径选择逻辑
### [4.4.136] - 2021.03.12
[Bugfix]修复比较 SC 版本号错误导致不能录屏分享的问题
### [3.20.128] - 2021.03.02
[Feature]互跳重新拉起获取上次互跳信息时添加参数appid
[Feature]互跳支持添加额外自定义参数
[Feature]互跳视频播放添加关闭视频的回调
[Feature]互跳完善埋点信息，添加游玩时间和宿主id
[Optimize]视频播放接口不对外暴露
[Optimize]启动参数去除 showfrom字段
[Optimize]修复 Banner 广告 resize 不成功以及 Banner 接口描述对齐开发者文档
[Optimize]修复UC测试Demo的自动录屏问题
[Optimize]互跳，跳转到另一个游戏时左上角显示返回按钮，点击会返回上个游戏
[Optimize]互跳添加宿主运行环境的判断
[Optimize]拉取互跳信息时过滤自身游戏
[Optimize]清除引导包的配置
[Optimize]完成互跳参数传递
[Optimize]互跳添加宿主判断
[Bugfix] 修复 ReportAnalyze 接口未进行参数判空导致的错误，参数 param 现默认为空且可省略
[Bugfix]视频播放仅在抖音和头条下有效，抖音lite会崩溃，因为缺少必要的依赖库
[Bugfix]修复互跳时长统计问题的bug
### [3.17.123] - 2021.02.03
[Optimize]每次打开视频播放界面，自动播放不同的视频。如果视频播放失败，自动重试，最多3次，播放3次都失败自动播放下一个视频
###### [Bugfix]修复某些机型上视频播放失败的问题
### [3.17.121] - 2021.02.01
[Optimize]添加日志上报CS
### [3.17.117] - 2021.01.29
[Optimize]去掉激励视频的Preload()功能和IsVideoAdReady()接口
###### [Bugfix]修复视频播放某些机型不全屏显示的问题
### [3.17.104] - 2021.01.29
[Feature]加入支付模块初始化接口，减少第一次使用支付接口时的等待时间
[Optimize]优化视频播放，增加支持空url视频链接
[Optimize]去掉error基本log
###### [Bugfix]修复屏幕旋转导致视频播放分辨率被拉伸的问题，Android 8.0 以下系统不支持视频播放
[Bugfix]修复视频播放结束后，不会自动播放下一个视频的问题
### [3.15.100] - 2021.01.25
[Feature]开放游戏直跳功能
### [3.15.96] - 2021.01.18
[Feature]游戏互跳功能，在一个游戏中跳转到另一个游戏
[Feature]游戏内播放抖音视频的功能
[Feature]判断是否绑定抖音号
[Feature]获取scheme中query
[Feature]胶囊按钮的关闭回调
[Optimize]优化StarkSDK与引导包的通讯方式
[Bugfix]Mock录屏时间改为真实的录屏时间，之前Mock时间恒为10s
### [3.12.85] - 2020.12.15
添加SCConfigCenter服务器数据，后台配置成功后无需再调用StarkSDKSpace.StarkSDK.MiniApk.InitMiniApk接口
预先兼容引导包插件化后的广告播放
引导包和穿山甲广告开关分离
引导包包名支持用户Init接口传入以及内置的包名规则，内置的包名规则com.bytedance.{appid}.miniapk
### [3.10.78] - 2020.12.09
StarkSDK兼容穿山甲插件广告
StarkMiniApk初始化内置到StarkSDK中
### [3.10.77] - 2020.12.08
StarkMock添加平台限制
### [3.10.69/70] - 2020.12.01
StarkSDK通知引导包退出改为在StarkSDK内部完成
### [3.10.67] - 2020.12.01
[Bugfix]引导包安装新安装后，若已存在安装记录则不再重复统计
### [3.10.65] - 2020.12.01
修改版本匹配规则考虑大小写
添加上报
### [3.9.61] - 2020.11.26
补充log
### [3.8.55] - 2020.11.20
Uri接口新从5.0.0开始
修改AD代码文件，修复乱码问题
### [3.8.54] - 2020.11.19
Uri接口新老版本兼容
### [3.8.53] - 2020.11.17
修复引导包日志上报问题
### [3.8.52] - 2020.11.16
将引导包合并到StarkSDK中，屏蔽引导包的使用接口
### [3.6.52] - 2020.11.16
优化视频分享错误提示，当视频时长低于 3 秒时弹出分享视频失败提示
### [3.6.50] - 2020.11.11
修复 log 无法 Track 的问题
### [3.6.49] - 2020.11.06
添加UCConfigCenter内部接口
添加插屏广告15s后才能播放的限制
### [3.6.47] - 2020.11.04
修复在UnityContainer环境下依旧可以打开Mock的bug
### [3.6.46] - 2020.10.30
增加支付模块
### [3.5.45] - 2020.10.29
修改MiniApk命令行构建脚本
### [3.4.44] - 2020.10.28
Banner广告的Mock方案
插屏广告的Mock方案
统计游戏内存占用、内存分配、PSS内存、Native内存、Dalvik内存、CPU占用
### [3.4.43] - 2020.10.27
修改MiniApk命令行构建脚本
### [3.4.43] - 2020.10.27
修复MiniApkApi可用性判断问题
### [3.4.42] - 2020.10.25
更新录屏SDK代码
### [3.4.41] - 2020.10.25
修改GameRecorderMock，不让其继承MonoBehavior
### [3.4.40] - 2020.10.23
完成登录功能
### [3.4.39] - 2020.10.21
优化CanIUse接口，不在运行时使用反射判断接口是否可用，直接判断uc版本号
修复录屏手动初始化的问题，仅在第一次录屏时才初始化
### [3.4.24] - 2020.10.20
StarkSDK 代码混淆
### [3.4.23] - 2020.10.16
添加胶囊按钮的Mock
添加设置当前宿主环境的Mock
### [3.4.22] - 2020.10.12
录屏模块在开始录屏时才初始化
录屏模块增加设置视频分辨率接口
### [3.3.X] - 2020.10.12
新增获取UC运行环境的接口
新增获取VersionType的接口
修改判断是否为UC环境的方式
新增Mock分模块开关
整理场景值
### [3.3.20] - 2020.09.28
增加link.xml文件（解决Unity il2cpp代码strip问题）
### [3.3.19] - 2020.09.28
StarkMock增加静音功能，默认打开，即关闭所有Mock界面
使用StarkSDKSpace.MockSetting.MuteStarkMock属性可以打开Mock界面
### [3.3.17] - 2020.09.27
增加收藏模块：StarkFavorite
关注抖音号失败增加Toast弹窗提示
如果API不受支持，弹Toast提示
### [3.3.15] - 2020.09.25
添加StarkMock功能，在编辑器下可以直接调用各种Stark的功能
添加穿山甲入口类型[MiniApk]
### [3.3.13] - 2020.09.25
修复ByteRec内的宏包含序列化成员变量导致无法编译通过问题
### [3.3.12] - 2020.09.24
ByteRec目录不编译进dll，增加宏限制，在Editor下运行不会抛出异常
### [3.3.10] - 2020.09.23
增加是否已关注抖音号接口：StarkAPI.IsFollowDouyin
### [3.2.8] - 2020.09.23
录屏增加声音录制
### [3.1.5] - 2020.09.15
修复连续点击视频分享，弹出多次分享器的问题
### [3.1.2] - 2020.09.14
增加是否已创建快捷方式接口：IStarkAPI.IsShortCutExists
增加判断接口是否在当前宿主可用的CanUse接口
增加通用分享接口，支持传递原始json数据
视频分享支持传递默认标题、话题（仅在抖音里有效）
增加震动接口
### [1.2] - 2020.08.27
修改StarkAdManagerImpl.StartLoadVideoAd内部实现，使用UNBridge callback
广告增加Loading弹窗
增加对 StarkSDK Android 版本号处理，在 C#侧读取该版本号
