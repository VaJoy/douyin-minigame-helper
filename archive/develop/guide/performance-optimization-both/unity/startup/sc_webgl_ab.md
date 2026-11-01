---
title: "使用 AssetBundle 进行资源按需加载"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/startup/sc_webgl_ab
update_time: 2024-07-24
---

## 一. AssetBundle概述
AssetBundle是Unity内置的一种资源加载的方式，由于较为底层，因此对于开发而言会付出额外的精力及学习成本，同样由于过程完全可控，因此可以实现更加细粒度的控制，具体取舍视实际项目本身决定。
关于AssetBundle的使用可以参考
> https://docs.unity3d.com/2021.3/Documentation/Manual/AssetBundlesIntro.html
对于AssetBundle中的原理实现，以及会影响性能及内存的几个详细的解释可以参考
> https://blog.uwa4d.com/archives/USparkle_Addressable3.html
同时对于AssetBundle中比较头疼的冗余检测可以参考
> https://blog.51cto.com/u_15338442/3563063
可以参考一个AssetBundle的冗余检测的实现
[GitHub - akof1314/AssetBundleReporter: Unity AssetBundle Reporter](https://github.com/akof1314/AssetBundleReporter)
## 二. AssetBundle的简单例子
### 2.1 打包
例子如下

```csharp
public static void Build()
{
    string dst = Application.streamingAssetsPath + "/AssetBundles";
    if (!Directory.Exists(dst)){
         Directory.CreateDirectory(dst);
    }
    BuildPipeline.BuildAssetBundles(dst, 
                                    BuildAssetBundleOptions.AppendHashToAssetBundleName 
                                    | BuildAssetBundleOptions.ChunkBasedCompression 
                                    | UnityEditor.BuildAssetBundleOptions.DisableWriteTypeTree 
                                    | BuildAssetBundleOptions.None,
                                     BuildTarget.WebGL);}
```

### 2.2 加载
对于本地加载AssetBundle包，由于不支持本地读取文件，因此AssetBundle.LoadFromFile等都将失效，所有加载都需要通过网络，UnityWebRequest可以参考
https://docs.unity3d.com/cn/2021.1/Manual/UnityWebRequest-DownloadingAssetBundle.html
主要包括
- UnityWebRequestAssetBundle.GetAssetBundle

```csharp
    public IEnumerator Load_AB()
    {
        UnityWebRequest request = UnityWebRequestAssetBundle.GetAssetBundle(uriPath);
        yield return request.SendWebRequest();
        if (request.isHttpError)
        {
            Debug.LogError(GetType() + "/ERROR/" + request.error);
        }
        else
        {
            AssetBundle ab = (request.downloadHandler as DownloadHandlerAssetBundle).assetBundle;
            // ab.LoadAsset
            ab.Unload(false);
        }
        request.Dispose();
    }
```

- UnityWebRequest

```csharp
    public IEnumerator LoadAB()
    {
        UnityWebRequest www = new UnityWebRequest(uriPath);
        DownloadHandlerAssetBundle handler = new DownloadHandlerAssetBundle(www.uri.ToString(), 0);
        www.downloadHandler = handler;
        yield return www.SendWebRequest();
        if (www.isHttpError)
        {
            Debug.LogError(GetType() + "/ERROR/" + www.error);
        }
        else
        {
            AssetBundle ab = handler.assetBundle;
            // ab.LoadAsset
            ab.Unload(false);
        }
        www.Dispose();
    }
```

## 三. 跨域问题
对于Addressables.LoadAssetAsync()或者AssetBundle.LoadAssetAsync()而言，最终都会经过网络请求获取到最终资源，由于是在WebGL浏览器环境中，如果使用原生的AA/AB包的接口无法避免会遇到跨域问题，存在一些方法可以解决这些问题，比如在修改网页配置允许跨域，或者通过代码实现一些替代方案等。
我们的解决方案是，我们在JS层重写了网络请求相关的部分，用户在不修改任何C#层的代码的前提下，可以正常支持跨域请求。
大致方案为，我们修改了WebGL.Framework.js文件，接管了XMLHttpRequest，UnityWebGL将数据缓存在IndexedDB中， 而我们绕过了浏览器环境，在原生环境（IOS原生/Android原生）中实现网络请求。

## 四. 网络请求与资源缓存
Unity_WebGL因为是运行在一个类浏览器环境中，受到浏览器的限制，借助XMLHttpRequest进行网络请求，同时将数据缓存在IndexedDB中，且不支持IO，有诸多限制，因此我们重写了网络请求部分。
重写后的工作流大致如下：

🎈几个重要的点
- 由于Unity_WebGL中关于文件加载部分，无论是本地文件还是远程资源，均是通过浏览器网络获取，最终缓存在IndexedDB中。出于性能、灵活性、拓展性的考虑，我们在Android层/iOS层重写了这部分，现在文件均是存在磁盘中，且文件加载均是读取磁盘文件。
- 对于资源加载而言，iOS和Android均统一使用重写后的文件IO和网络模块，并不会再使用Unity_WebGL提供的功能。
