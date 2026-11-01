---
title: "CI自动化"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/packaging-release/ci_openapi
update_time: 2025-12-26
---

> CI 自动化主要是通过提供开放接口供开发者接入来实现的。从配置，构建两个方面提供了 C# 接口。开发者可以利用 Unity 的 batchmode 或其他方案来进行接入。

## 配置
配置接口提供了丰富的配置选项，开发者可根据需要进行相应的配置。另外对于配置接口中的配置项与以下构建或者发布接口中参数项冲突时，以接口内的参数为准。
#### 获取配置对象

```csharp
var settings = TTSDK.Tool.StarkBuilderSettings.Instance；
```

#### WebGL构建相关
配置项均在`TTSDK.Tool.StarkBuilderSettings.Instance`下：

| 接口 | 含义 |
| --- | --- |
| wasmResourceUrl | WebGL模式下音频资源的url |
| useByteAudioAPI | *对应WebGL构建面板上的复制音频文件，开启会自动将工程目录中的音频文件以工程目录的结构复制出来* |
| wasmMemorySize | WebGL模式下预占内存值大小 |
| isWebGL2 | 是否开启WebGL2.0 |
| needCompress | 是否开启压缩 |
| buildOptions | 构建选项 |
| urlCacheList | 缓存资源域名列表 |
| dontCacheFileNames | 构建时不自动缓存的文件 |

#### 安卓构建相关

| 接口 | 含义 |
| --- | --- |
| isDevBuild | 是否开启development |
| stripEngineCode | 是否开启stripEngineCode |
| apkFileNameBase | 基础apk名称 |
| apkOutputDir | 生成apk所在目录 |
| appHost | 宿主（调试时的宿主） |
| compressMethod | 压缩方法 |
| runtimeEnv | runtimeEnv（调试时的版本环境） |
| framework | 运行框架 |
| architecture | cpu架构 |
| miniApkVersion | 最低安卓版本 |
| scriptingBackend | 脚本后端 |
| NativeWhiteListRegex | Native脚本白名单 |

#### 发布配置

| 接口 | 含义 |
| --- | --- |
| appId | 游戏的appId |
| version | 发布游戏的版本 |
| autoVersion | 是否开启自动版本号功能 |
| webglPackagePath | 生成的webgl zip包的路径（注意:是生成后的） |
| orientation | 屏幕方向 |
| menuButtonStyle | 胶囊深浅色 |
| publishType | 发布类型 |
| publishDesc | 发布描述 |

#### 开发者工具配置

| 接口 | 含义 |
| --- | --- |
| idePath | 开发者工具的可执行文件路径，Windows下以exe结尾，Mac下以app结尾 |

## 构建
构建接口在`TTSDK.Tool.API.BuildManager`下：
#### Build
> 构建游戏

```csharp
public enum Framework
{
    Native,
    Wasm,
    UnityInstantGame
}
//返回值中string即代表最终产物路径
//confirm在batchmode下建议使用false，防止因弹窗导致卡主构建流程
public static async Task<string> Build(Framework framework, bool confirm = false)
```

##
