---
title: "小游戏资源缓存"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/packaging-release/changelog-and-resource/sc_webgl_resource_cache
update_time: 2025-03-05
---

## 概述
为提升小游戏加载速度、减少重复下载资源的网络流量消耗，平台提供了自动资源缓存能力。当 Unity 小游戏从配置为缓存资源域名的 URL 加载资源时，获取到的资源会被保存到本地，下次请求时直接从缓存读取。

基于不同的加载方式，Unity 小游戏资源可分为**首包资源**和**远程资源**两类。
- **首包资源**包含 wasm 代码文件、StreamingAssets 文件夹等内容。通常在首次进入游戏时下载，常驻在小游戏缓存中。
- **远程资源**则以开发者自行托管在 CDN 上的 AssetBundle 文件为主。通常在游戏内按需下载，根据配置保存到缓存。
本文档主要描述**远程资源**在小游戏中的缓存机制。

## 使用说明
要使用资源缓存能力，可在 StarkSDK Unity 调试工具（菜单栏 - ByteGame - StarkSDKTools - Build Tool）面板配置：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/c899ebcfbcbe4aa7a7956ec31aabab70)

缓存资源域名：
- 请求被配置的域名下资源时会经过缓存。
- 支持填写顶级域名与子域名（例 `dailygn.com`、`cdn.dailygn.com`）和域名下的子目录（例 `cdn.bytedance.com/dailygn`）。
- 支持配置多个，一行一个。

不缓存的文件：
- 被配置的文件会及时更新，即使在缓存资源域名下也不会被缓存。
- 支持填写完整文件名（例如 `settings.json`）或文件扩展名（如 `json`）。
- 支持配置多个，一行一个。

Tips：
- 项目中的资源配置文件（例如：addressables 的 `settings.json` 和 `catalog.json`）的文件名通常是固定的。如果希望游戏资源能够及时更新，应避免这些文件使用缓存，尽量将其配置在“不缓存的文件”中。
- 不同插件版本中配置项名称略有差异，“缓存资源域名”与“缓存资源域名列表”是同一配置项、“不缓存的文件”与“不自动缓存的文件”是同一配置项。

## 缓存规则

> **说明**
> 开发者通常无需关心具体的缓存逻辑，以不存在缓存为前提开发业务代码，配置后自动实现缓存机制。

### 触发场景
在 Unity 中使用 UnityWebRequest、UnityWebRequestAssetBundle、WWW、Addressables 等常见网络接口/封装发起 HTTP GET 请求时，都会根据配置检查是否命中缓存策略。
“缓存资源域名”下的请求如果命中本地缓存，将直接使用缓存的文件。未命中本地缓存时，会发起真正的网络请求，成功下载到的文件会按规则重命名，保存在 Android/iOS 本地存储空间中。

主要缓存策略如下：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/51d91e7cd5e0472f910e8a4e2618bdfa)

### 缓存淘汰
在用户长期没有打开小游戏时，平台会清理小游戏的本地缓存文件，暂不支持开发者主动干预。

## 缓存调试
在小游戏预览/测试版环境中会默认开启缓存调试日志，每一次读写缓存操作都会有对应的日志输出，并带有本次操作的上下文信息供开发者参考，具体格式如下：

```text
INFO/JSFW_Cache: use cache file { url: "https://your-cdn-domain.net/xxx/xx.bundle", path: "scfile://user/__sc_http_cache_files__/xxxxxxxx", cost: "11ms" }
```

- INFO 代表日志的等级，可能为 DEBUG、INFO、WARN、ERROR。
- JSFW_Cache 代表日志来自 JS 框架层的 Cache 模块。
- use cache file 代表日志的文本内容。
- { ... } 大括号中是日志附带的上下文信息。

### 日志信息
缓存日志文本内容：

| **日志名称** | **日志文本** | **说明 ** |
| --- | --- | --- |
| 缓存命中 | use cache file | 请求一个 URL 时，本地缓存文件存在，直接使用缓存的内容。 |
| 读缓存失败 | read cache fail | 请求一个 URL 时，本地缓存文件存在，但无法从缓存读入，需要重新下载。 |
| 开始写入缓存 | not cached, saving... | 请求一个 URL 完成时，如果其需要被缓存，开始写入缓存。 |
| 写入缓存成功 | cache saved | 已成功将请求结果写入到本地缓存文件。 |
| 写缓存失败 | save cache fail | 写入文件缓存失败，日志中会体现具体错误原因。 |
| 长度校验失败 | Content-Length mismatch | 请求一个 URL 完成时，其实际文件大小与响应头中 Content-Length 不匹配，将不作缓存写入操作。（仅校验未压缩的响应） |

缓存日志中可能带有的上下文信息：

| **属性名 ** | **类型 ** | **必传** | **说明 ** |
| --- | --- | --- | --- |
| url | string | 是 | 要缓存资源的 URL |
| path | string | 否 | 缓存文件对应小游戏文件系统路径 |
| cost | string | 否 | 本次读写缓存操作耗时（毫秒） |

## API 接口
### C#
检查资源是否已被缓存

```csharp
TT.GetFileSystemManager().IsUrlCached(string url);
```

获取缓存资源的本地路径

```csharp
TT.GetFileSystemManager().GetLocalCachedPathForUrl(string url);
```

手动删除对应的缓存文件

```csharp
TT.GetFileSystemManager().UnlinkSync(string path);
```

### JavaScript
开关缓存调试日志

```js
window.StarkSDK.SetDebugLogEnabled("Cache", false)
```

## 常见问题
1. 平台提供的缓存能力与 Unity 自身 Addressables 或 WWW 的 Cache 有什么区别？是否可以同时使用？
  - 平台提供的缓存能力会将文件缓存到小游戏文件沙盒；而 Unity 自带 Cache 能力为原生平台设计，在 WebGL 上使用了内存文件系统 + IndexedDB 同步持久化的方式实现，所有缓存都会常驻在内存中，会浪费大量内存并引起崩溃。
  - 建议不要在 WebGL 游戏中使用任何 Unity 自带的资源 Cache 能力。

1. 是否支持手动操作缓存文件？
  - 可参考上述 C# 接口通过 URL 获取本地缓存文件路径、检查缓存状态、删除缓存文件、手动读入缓存文件等。

1. 是否可以直接从缓存文件中加载 AssetBundle 资源？
  - 需使用 SDK 提供的接口，可参考 https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc-webgl-tt-ab

1. 抖音开发者工具中运行游戏时缓存没生效？
  - 请使用真机测试，抖音开发者工具下默认不缓存游戏资源文件。
