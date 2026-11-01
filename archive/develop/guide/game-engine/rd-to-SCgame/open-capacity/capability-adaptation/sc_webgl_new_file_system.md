---
title: "使用新文件系统说明"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_new_file_system
update_time: 2025-06-17
---

> 迁移仅涉及IOS，不涉及Android（Android仅需替换接口，新文件系统接口已适配C#标准接口）
> 更多文档参考 [接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide)

## 新文件系统的背景
原有实现中，C#标准的文件接口，如`File.ReadAllText`、`File.WriteAllText`、`FileStream`等，是将数据写入到内存文件系统，然后再在合适的时机自动同步内存数据到IndexedDB中存储。由于采用了IndexedDB文件存储系统，使得运行时内存有一定的增加，如果文件数量过多，可能会发生闪退。另外，IndexedDB文件存储系统兼容性不够好，在部分iOS系统上会无法正常使用，从而导致无法正常进入游戏的情况。所以我们提供 `StarkFileSystemManager`接口作为替换，开发者可以通过调用`StarkSDKSpace.StarkSDK.API.GetStarkFileSystemManager()`方法来使用新的文件存储系统。
### 重点说明：
- 对于 iOS WebGL 方案，`StarkFileSystemManager`接口提供的新文件存储系统只在**新版本iOS抖音(版本号>=24.4)上有效**，旧版本iOS抖音上仍然则使用默认的IndexedDB存储。
- 对于Android WebGL 方案，新旧版本抖音都支持新的文件存储系统的使用。
- `UnityEngine.PlayerPrefs`接口保存数据是保存在IndexedDB中的，为了使用新的文件系统存储，我们也提供了在全局名字空间的`PlayerPrefs`接口，或者使用`StarkSDKSpace.StarkSDK.API.PlayerPrefs`接口。这里提供的两个`PlayerPrefs`接口实现有一定的区别，全局名字空间的`PlayerPrefs`接口，不会自动迁移IndexedDB中的数据到本地存储，而`StarkSDK.API.PlayerPrefs`接口会自动迁移IndexedDB中的数据到本地。
- 对于已上线的游戏，游戏存档保存在IndexedDB中，当采用新的文件存储系统后，会将IndexedDB中的数据迁移到本地存储，之后将无法从IndexedDB中读取。具体数据迁移方法见下一节。
- **当使用了新版本文件存储系统后，之后不允许再使用C#标准的文件接口，不然数据将无法持久化存储，因为不会访问IndexedDB存储系统。**
> 在新的抖音版本中，不会再对IndexedDB做操作，能够大幅降低内容占用。当前属于过渡阶段，长期会禁用File.xxx。
> 当前在 测试环境 如果发生了File的读写（file.xxx 或者 UnityEngine.PlayerPrefs）会弹出 “**请替换新文件存储接口**“的提示。线上环境 不会有提示。
由于已上线的游戏，用户本地已经有了存档文件。所以需要迁移。新游戏直接使用StarkSDK提供的接口，就不会有此问题。
## 已有存档文件迁移方法：
1. 应尽可能早的调用`StarkSDKSpace.StarkFileSystemManager.MigratingData`方法，该方法会尝试迁移IndexedDB中的数据到本地，**并标记迁移完成**。如果不主动调用，那么在后续使用新文件存储系统接口时，会在对象实例化时自动调用一次，这样能保证正确读取到旧的数据。当数据迁移完成后，之后将无法使用C#标准文件存储接口（File.xxx等）访问原有数据，需要调用`StarkFileSystemManager`接口来访问。
1. 需将项目中的File.xxx 和FileStream 改为 `StarkSDK.API.GetStarkFileSystemManager()`。`UnityEngine.PlayerPrefs`替换为 `StarkSDK.API.PlayerPrefs`，或者使用全局名字空间的`PlayerPrefs`（但如果有旧的存储，要确保主动调用了数据迁移接口）。
1. 当项目中主动调用了`StarkFileSystemManager`接口，那么我们认为项目已经准备好了使用新文件系统，之后不会再去访问老的IndexedDB系统。
1. StarkSDK所提供的原有的 `StarkSDK.API.Save` 和 `StarkSDK.API.Load` 接口，在数据迁移完成前，仍然使用的IndexedDB存储，当迁移完成后，内部实现会自动切换为新的文件存储系统，开发者无需修改。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/34827bee966e4bcba9621254e9137bed)

## 下载资源缓存

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4a5ffee614be4119bd71e42ef485d377)

如果有下载的资源需要自动缓存的，在“**缓存资源域名列表**”中填写相应的域名信息，不支持通配符。比如下载资源url是https://cdn.bytedance.com/resource.data，这个文件需要被缓存下载，那么可以在“**缓存资源域名列表**”中填写域名cdn.bytedance.com，这样当下载这个资源时底层会自动缓存下来。
如果你需要知道当前url文件在本地是否有缓存，你可以调用这个接口，传入url信息`StarkSDKSpace.StarkSDK.API.GetStarkFileSystemManager().IsUrlCached(string url)`，如果返回true，那么则表示本地有缓存。
如果你想手动读取或删除本地资源缓存文件，你可以先获取资源文件缓存路径，然后再对该文件进行操作。调用这个接口，传入下载的url，获取缓存文件路径：`StarkSDKSpace.StarkSDK.API.GetStarkFileSystemManager().GetLocalCachedPathForUrl`
如果你有不想缓存的资源文件，比如像aa资源的catalog.json文件，那么你可以在"**不自动缓存的文件**"列表中填写文件信息，匹配规则是文件名后缀匹配，你可以填写.json，也可以填写catalog.json，不支持通匹符。
## 数据对比
在老文件系统上写入约400MB的文件后，打开游戏后占用内存约1G，在迁移后则基本不会再占用内存，游戏内存将至630MB左右
**迁移前：**

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/025af9a972524cd08e33143c1108b848)

**迁移后：**

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/bb56f58ff1c64774a21560808f000fc7)
