---
title: "使用 Addressable 进行资源按需加载"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/startup/sc_webgl_aa
update_time: 2025-06-17
---

对于小游戏情况而言，需做到即点即玩，即尽可能缩短玩家进入首场景之前的等待时间，因此分包是必须要做的一个环节，本文将介绍Addressable资源管理系统。
## 一. Addressable概述
Addressable是由Unity官方在2019版本，正式发布的一种资源管理系统，Addressable是Unity官方对AssetBundle的一种封装，目的是为了填补一些AssetBundle缺失的功能，封装一些资源加载的固有功能，从而降低资源加载的使用门槛和后期维护所消耗的精力。
相较于AssetBundle而言，Addressable封装了以下几个功能
- **可视化UI界面**，关于资源的分组及其他情况更加直观
- **自动依赖管理**，相较于AssetBundle手动保证某资源的依赖需提前加载进内存，Addressable在开发时无需关注资源依赖情况，当作所有依赖都已经被加载进内存处理，在运行时会自动检测其依赖并自动加载，从而保证每次资源加载都能成功。
- **封装网络请求接口**，相较于AssetBundle需要手动实现远程bundle的网络请求，Addressable在开发时无需关注资源在本地或者在cdn，统一调用`LoadAssetAsync`等异步接口处理处理，在运行时会自动下载远程或加载本地。
- **资源分析工具**，相较于AssetBundle需要手动检测多依赖下的资源重复打包问题，Addressable提供了资源检测工具自动分析重复情况。同时还提供Event Viewer来检测资源加载情况，供优化使用。
如今而言，Addressable是现在游戏作为分包的首选方案。

## 二. Addressables的加载流程

Addressable一般在构建之后会出现几个文件
- catalog.json:资源表，存放了addressable的所有资源
- setting.json：运行时addressable参数
- {bundle_name}.bundle：bundle包文件
对于所有Asset都是由`ResourceManager`来管理的
对于每一个资源都分别继承了`IResourceLocation`和`IResourceProvider`
- `IResourceLocation`：包含了该资源的所有信息，包括依赖信息，location哈希等。
- `IResourceProvider`：包含资源的加载和卸载方式，主要是为了统一本地和远程的区别。
**在刚进入游戏时，Addressable会做以下操作：**
- 加载`Setting.json`，并根据哈希值判断`catalog.json`是否有更新
- 加载最新`catalog.json`文件，并替换本地catalog缓存
- 解析`catalog.json`文件，读取其中所有的`IResourceLocation`信息，并保存到`ResourceManager`中
**一次运行时资源加载会做以下操作：**
- 通过`IResourceLocation`获取该资源的依赖信息及文件hash信息
- 通过`IResourceProvider`获取该资源所属bundle包的加载方式
- 如果所属bundle在本地，则直接加载
- 如果所属bundle包在云端，则启用网络请求下载，下载完成后再加载
- 将加载的资源赋值给`AsyncOperationHandle.Result`并 设置`AsyncOperationHandle.Statue`并执行`Completed`事件

## 三. Addressables简单例子
AssetReferences 支持拖放和对象选择器分配，这可以使它们更方便地在 Editor Inspector 中使用。

```csharp
public class LoadAssetScript : MonoBehaviour
{
    public AssetReference somePrefab;
    private void Start()
    {
        somePrefab.InstantiateAsync().Completed += (obj) =>
        {
           // 加载完成回调
            if (obj.Status == AsyncOperationStatus.Succeeded)
            {
               Debug.Log("successful");
            }
        };
    }
}
//协程写法
public class LoadAssetScript : MonoBehaviour
{
    public AssetReference somePrefab;
    private IEnumerator spawnSomathing()
    {
        var hanle = somePrefab.InstantiateAsync();
        while(!handle.IsDone) {yield return null;}
         // 加载完成回调
        var gameObject = hanle.Result;
    }
}
```

简单的异步加载接口`Addressables.LoadAssetAsync`例子

```csharp
  void Start()
    { 
        StartCoroutine(Load());
       
        Addressables.LoadAssetAsync<GameObject>("Assets/Image.prefab").Completed += (handle) => { 
            if(handle.Status == AsyncOperationStatus.Succeeded){
                Instantiate(handle.Result);
            }
        };

    }
    //协程写法
    IEnumerator Load()
    {
        var handle = Addressables.LoadAssetAsync<GameObject>("Assets/Image.prefab");
        if (!handle.IsDone)
        {
            yield return handle;
        }
        if (handle.Status == AsyncOperationStatus.Succeeded)
        {
            Instantiate(handle.Result);

        }
    }
```

## 四. 资源卸载
可以使用`Addressables.Release`方法对某一个资源进行卸载，此时该资源不会立刻从内存退出
- 调用后引用记数会减1，当资源的引用记数为0时，此时该资源仍然不会从内存退出
- 等到该资源所属bundle的所有资源的引用计数全为0时，该bundle及包含的所有资源从内存退出

```csharp
 //这是一个Addressable handle卸载的简单例子
 Addressables.LoadAssetAsync<GameObject>("Assets/Image.prefab").Completed += (handle) => { 
            if(handle.Status == AsyncOperationStatus.Succeeded){
                Instantiate(handle.Result);
            }
            Addressables.Release(handle);
        };
```

## 五. Addressable配置简介
### 5.1 Group
Addressable在打包时是以Group为单位的，一个Group会打包成一个Bundle，同时在资源加载时，当需要加载某一个资源，会一次性将该资源所属的整个bundle包读取进内存，对于某一个资源的依赖资源，也会读取依赖资源所属的bundle包，因此，**做好合理的资源分组非常重要**
### 5.2 Profiles
Profiles中记录了构建和加载的路径，包括本地和远程。在运行时调用`Addressables.LoadAssetAsync`会自动请求此处设置的地址
### 5.3 Analyzer
Analyzer会通过一个模拟构建，扫描所有Addressable的group，从而分析其中的资源冗余及共享依赖问题，关于具体实现可以参考[Unity手游实战：从0开始SLG——资源管理系统-Addressable中文手册（五）分析器（完）](https://zhuanlan.zhihu.com/p/98663321)
### 5.4 Event Viewer
该项可以监视Addressables资源的内存管理情况，供性能优化及调试时使用。详细信息可以参考https://zhuanlan.zhihu.com/p/502115922
