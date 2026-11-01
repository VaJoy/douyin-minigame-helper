---
title: "使用预下载功能"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/startup/use-predownload-feature
update_time: 2025-10-09
---

## 简介
通过[启动加载时序](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization/startup-performance/startup-performance-guide)我们知道，在小游戏加载过程中“加载性能”的阶段，存在**网络空闲**的情况，我们可以在此阶段提前下载游戏内资源。
预下载功能的原理是提前通过网络下载资源并缓存到本地，下次使用时从本地缓存中读取文件，以此提高资源加载速度。
目前仅支持Unity小游戏，需在抖音33.6.0及以上版本验证

---

## 配置方式
### 打包配置
主要配置入口在预加载选项中。(TTSDK版本>=6.3.1)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/2821ba03383b4dc3aa52290cc6dd8d6c~tplv-9nona0m7ha-image.image)

- 文件列表：使用`;`间隔，支持模糊匹配(资源文件名中包含文件列表中字符串，即可将资源文件匹配进资源列表中)，在构建时会将文件列表生成到 game.js 的 managerConfig 配置中
- 游戏资源CDN: 部署资源的CDN前缀，构建时会生成到 game.js 的 managerConfig 配置中，在运行时，会拼接游戏资源CDN与文件列表中的文件路径进行预下载。拼接规则:{DATA_CDN}/StreamingAssets/{FilePath}
在Unity转换导出插件填写文件列表，生成时工具会自动从**webgl/StreamingAssets目录**找资源并填充到game.js。 运行时将根据列表内容在网络空闲期下载。
若在构建面板有配置内容，且匹配到了资源，那么会在game.js 中存在以下类似配置的内容：

```go
const managerConfig = {
    DATA_CDN: '',
    preloadDataList: [
        // 'DATA_CDN/StreamingAssets/WebGL/textures_005b9e6b32e22099edc38cba5b3d11de',
        // '/WebGL/bundles_e1af572c458eda6944e73db25cae88d5'
        
    ],
 };
GameGlobal.managerConfig = managerConfig;
```

### 手动配置
可以直接修改打包产物中 game.js 文件进行修改。格式如上。
### 运行时配置
#### 引擎初始化完成后
通过C#接口 `TT.SetPreloadList` 修改。（TTSDK版本>=6.5.6）

```csharp
private IEnumerator GetPreloadList()
{
    using (UnityWebRequest www = UnityWebRequest.Get("https://api.example.com/preloadlist"))
    {
        yield return www.SendWebRequest();
        if (www.result != UnityWebRequest.Result.Success)
        {
            Debug.Log(www.error);
        }
        else
        {
            string json = www.downloadHandler.text;
            PreloadListData preloadListData = JsonUtility.FromJson<PreloadListData>(json);

            // 获取URL列表
            TT.SetPreloadList(preloadListData.list);
        }
    }
}

[System.Serializable]
public class PreloadListData
{
    public List<string> list;
}
```

---

## 预下载时机
Unity小游戏会在 引擎初始化完成前（对应wasm 代码编译以及 callmain 阶段）开始进行预下载。

---

## 并发数
在引擎初始化完成前，默认**并发 10 个**预下载。已发起但未完成的下载任务，以及列表中尚未发起的任务，会在引擎初始化完成后继续进行，但**并发数改为 1 个**。可通过 Csharp 接口`TT.PreloadConcurrent` 修改引擎初始化后的预下载并发数。（TTSDK版本>=6.5.6）
- 默认值：引擎初始化完成前 10 个；引擎初始化完成后 1 个
- 最大值：10 个
## 如何验证
### Unity小游戏
可以通过测试版本的vconsole日志观察：接入预下载后，日志中会包含`JSFW_PreloadManager：`相关的日志描述，其中会包含请求成功或者失败等字样，开发者可根据日志进行调试。
> Unity小游戏还可以在抖音开发者工具中进行验证，需抖音开发者工具版本>=4.3.8, 可在模拟器预览时，观察日志描述。获取接入情况。

---

## 注意事项
1. 预下载**最大数量为30个**。超出会取前30个作为预下载列表
1. 添加到预下载列表中的文件，在预下载完成后**会保留60s**，随后删除引用。如果您没有持有数据的引用，会被回收导致下载浪费。
1. 会按照列表顺序发起预下载，请将优先需要的资源放到列表前面。
1. 抖音开发者工具4.3.6版本在 game.json 新增了预下载的代码提示，可以升级获得更好支持。

{
"preloadDataList": ArrayObject
}

// game.json
{
"preloadDataList": [
"https://developer3.bytedance.com/abc.png",
...
]
}

// game.json
{
"preloadDataListUrl": "动态更新的url" // optional, 如果配置了preloadDataListUrl则preloadDataList不生效
}

// game.json
{
"preloadDataListUrl": "https://api.example.com/preloadlist" // 如果配置了preloadDataListUrl则preloadDataList不生效
}

"preloadDataList":[
"https://developer3.bytedance.com/abc.png",
...
]
