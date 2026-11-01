---
title: "使用 TTAssetBundle 优化内存"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/startup/sc-webgl-tt-ab
update_time: 2025-09-01
---

## 内存问题
在 Unity WebGL 小游戏环境中处理 AssetBundle 加载时，我们无法利用 App 游戏中常用的 `AssetBundle.LoadFromFile()` 等依赖本地文件系统的加载方式，而是需要使用 `UnityWebRequest` 等通过网络的加载接口。
通过 `UnityWebRequest` 加载 AssetBundle 时，下载或从本地缓存中读入的 AssetBundle 文件会完整拷贝到 Unity Heap 内存，在 Unload 之前额外占用 Unity Heap。而由于 Unity Heap 一旦超额分配便无法从 JS Heap 中释放，将其控制在更小范围内有利于控制整体进程内存，降低崩溃率。

## 解决方案
TTAssetBundle 接口通过打通 Unity 内存文件系统和小游戏本地缓存文件系统接口，在加载 AssetBundle 时内部使用 LoadFromFile() 仅打开文件流，在 LoadAsset 时通过文件描述符按需读取 AssetBundle 的包内资源，可以节省与 AssetBundle 文件大小相当的内存。

## 使用说明
### 版本要求
开发工具：
- TTSDK（原 StarkSDK） 5.52.10 及以上
  - TTSDK 低于 6.2.0 时，依赖 StarkSDK Unity Tools 3.31.2 及以上
- Unity 2021.3 及以上
宿主：
- 抖音/抖音极速版 29.2.0 及以上，暂不支持头条、番茄。
- 不支持的版本/宿主上，会 fallback 为类似原本 `UnityWebRequest` 加载实现，仍可正常加载到资源。

### 构建配置
要通过 TTAssetBundle 加载的资源，其域名都必须配置在“缓存资源域名”中，配置方式可参考 [小游戏资源缓存](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/changelog-and-resource/sc_webgl_resource_cache#2b05236f)。这一配置是为了 AssetBundle 资源文件能够被正确存入小游戏文件缓存中，供相关接口后续按需读取。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/db366fea809741ae964eafed090cf939)

### 加载 AssetBundle
加载 AssetBundle 代码示例：

```js
using TTSDK;

UnityWebRequest request = TTAssetBundle.GetAssetBundle(url);
yield return request.SendWebRequest();
if (request.result != UnityWebRequest.Result.Success)
{
    Debug.Error(request.error);
}
else
{
    AssetBundle ab = (request.downloadHandler as DownloadHandlerTTAssetBundle)?.assetBundle;
    ab.TTUnload(true); // 使用 TTAssetBundle 加载的资源，必须调用 TTUnload() 方法才可彻底卸载。
}
```

### 使用 Addressables
如果项目使用 Addressables 管理资源，可以通过替换 Provider 以使用 TTAssetBundle。
1. 引入适配的 Provider：
  - 在 TTSDK 目录下找到 `TTAssetBundleProviders.cs.txt` 文件（通常在 `Assets/Plugins/ByteGame/com.bytedance.ttsdk/WebGL/AssetBundle` 目录下）。
  - 将其拷贝到工程中，并更名为 `TTAssetBundleProviders.cs`（移除扩展名 txt）。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/dd023d9547b047e695c494cd131ceb6a)

1. 设置 `Addressable Asset Group` 的 Providers：
  - `Asset Provider` 设为 `Assets from TTBundles Provider`
  - `AssetBundle Provider` 设为 `TTAssetBundle Provider`
  - `Use AssetBundle Cache` 设为 `False`
  - `Asset Bundle CRC` 设置为 `Disabled`（建议）

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/258eed319d074b62952f223cfe19526a)

1. 重新导出 Addressables 资源、打包小游戏。

## 注意事项
1. **评估 Unity Heap 内存占用**
  - TTAssetBundle 主要能够节省 Unity Heap 内存的使用，而 Unity Heap 内存通常是预先分配的。建议开发者完成接入后，在构建工具面板中重新设置（适当降低） Unity Heap 预留内存大小，以取得更好的整体进程内存收益、降低崩溃率。推荐对内存有严格要求的中重度游戏接入使用。
  - 若要评估 Unity Heap 内存，可以在构建工具界面勾选 Profiling 选项在游戏内显示内存面板。面板上 Total Memory 即为 Unity Heap 的实际占用，建议以可支持长时间游玩（例如 30 分钟）而不触发增长的最小值作为预留大小的基准。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d546a5144a724cce8678777c60e2f7cd)

1. **TTAssetBundle 的卸载规则**
  - 加载过程中的 AssetBundle 文件会在 JavaScript 内存中保留一份完整的文件缓存以保证载入性能。
  - 内存文件缓存中的文件超过 5s 未被读取或缓存占用超出 128MB 上限时，将按 LRU 清理最久未被读取的 Bundle。被清理的 AssetBundle 下次读取时将重新从磁盘读入，建议开发者及时调用 `TTUnload()` 卸载不使用的 AssetBundle。自动清理的阈值支持在 `StarkBuilderSettings` 中配置。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ae32099e1eb64e12aab1afacf4c93593)

1. **环境不支持时自动降级**
  - Android Native 方案、不支持的低版本宿主上 WebGL 方案中也可以使用该接口，但内部会 fallback 为使用 `AssetBundle.LoadFromMemory()` 实现加载，没有任何内存和加载效率上的收益。
  - 开发者可以根据需要自行判断是否在不支持的环境中替换加载接口。

## **常见问题**
1. **运行时报错**`TypeError: Cannot read properties of undefined (reading 'has')`
  - 检查 `Assets/Editor/StarkBuilderSettings.asset` 中的配置，`Asset Bundle FS Enabled` 配置项需要为勾选状态。

1. **运行时 **`fs`** 相关接口读文件报错**
  - 检查资源所在域名是否已正确配置在“缓存资源域名”列表中。

1. **引入 **`TTAssetBundleProviders.cs`** 后编译报错**`TTAssetBundleProviders.cs(11,38): error CS0234: The type or namespace name 'AsyncOperations' does not exist in the namespace 'UnityEngine.ResourceManagement' (are you missing an assembly reference?)`
  - 检查项目 asmdef 配置，在 `Assembly Definition References` 中添加依赖 `Unity.ResourceManager`。

1. `UnityWebRequest`**加载完成了，但是**`(request.downloadHandler as DownloadHandlerTTAssetBundle)?.assetBundle`**为空**
  - `AssetBundle.LoadFromFile()`接口不支持重复加载同一个资源文件，需要开发者在调用`TTAssetBundle.GetAssetBundle(url)`前先检查是否已经加载。
