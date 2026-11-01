---
title: "Unity资源按需加载概述"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/startup/sc_webgl_load_overview
update_time: 2024-12-11
---

> 此文档描述小游戏开发时资源按需加载概述
> 更多详情见[Unity WebGL 字节小游戏适配方案](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/sc_webgl_overall)

## 一. 引言
资源按需下载是游戏中很重要的一项技术，避免了游戏过大的包体大小，主流的手机游戏几乎都重度使用了该项技术。
大概做法是，将首场景及一些必须的内容放到首包内，在运行中根据玩家的需求动态下载所需素材。

> 对于小游戏而言，存在即点即玩的需求，应尽快缩短用户从点击到游玩体验之间的时间，对于资源加载而言，必须做到最大限度地缩减首包的体积，能延迟加载的都进行延迟加载处理。

对于代码而言，也要尽量做到分包，首包仅放置首场景中会使用到的代码，目的也是为了避免在一开始就堆积过于集中的下载任务，WASM代码分包可以详细参考[Wasm分包工具说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/code-upload/sc_webgl_split)。
## 二. 各方案比较
Unity中现在较为主流的资源管理系统有Addressables、Asset Bundle、[Unity InstantGame](https://unity.cn/instantgame)。
### 2.1 Asset Bundle
Asset Bundle是Unity提供的底层的资源加载方式，AssetBundle是一个存档文件包含了非代码资源，如模型、纹理、音频、场景等，还可包括如ScriptableObject等的序列化数据。工作流程为，先将资产标记为AssetBundle文件，生成AssetBundle文件，在运行时加载AssetBundle文件。
需要注意的是在加载AssetBundle文件时，会一次性将整个AssetBundle读入内存，因此对资源**合理地分组**非常重要。AssetBundle只会加载本Bundle文件，对于依赖项需要**手动**将其加载进内存，由于资源分组是手动进行的，可能会存在被多依赖的资产被重复打包进AssetBundle，从而造成**资源冗余**，因此在打包前需要对资源做依赖分析，尽可能消除冗余，上述几个较为消耗人力的功能将会被封装进Addressables。
对于AssetBundle的接口可以参考官方文档
> https://docs.unity3d.com/2021.3/Documentation/Manual/AssetBundles-Workflow.html
### 2.2 Addressables
Addressables是Unity针对AssetBundle配置过于繁琐做出的一种解决方案。Addressables使用了一种基于标签的打包方式，可以根据资源的标签进行打包，不需要手动配置依赖关系。同时Addressables内置了远程加载和动态更新等相对更高级的接口，使用起来更加简便和方便。
对于Addressable而言，提供了更为直观的UI配置界面，是现在主流的资源加载方案。

### 2.3 Unity InstantGame
Unity InstantGame是Unity提供的一套针对小游戏即点即玩需求而打造的框架。关于InstantGame的配置可以参考官方文档
https://unity.cn/instantgame/doc/2019/2019.4.29f1c110
对于InstantGame而言，默认且只能使用UOS CDN作为部署streaming资源的云服务器。为了对接现有方案，InstantGame支持重打包，将AB/AA包工程转化InstantGame对应的资源加载方式。
InstantGame针对小游戏情况，相较于AB/AA包方式可以减少开发及维护时间，减少人力，但是想要达到最佳配置，仍然需要配置。

### 四种方案比较如下

|  | **Asset Bundle** | **Addressables** | **InstantGame** |
| --- | --- | --- | --- |
| 原理 | Unity底层资源加载方式 | 对Asset Bundle做了一层封装 | 对Addressable的封装 |
| 学习成本 | **大**，需要手动组织Bundle，手动设置依赖关系等，后期维护成本较大 | **适中**，自动关联依赖，自动分组等。 | **较少** |
| 支持CDN | 任意 | 任意 | 只支持UOS CDN |
| 配置复杂程度 | 较为复杂 | 中等 | 较少 |
| 代码修改量 | 较多 | 多 | 少 |
| 是否支持资源LOD | 否 | 否 | 是 |

## 三. 方案选择建议
不同的游戏对于运行时，加载时，开发时的要求不尽相同，因此不同的游戏也应选择不同的方案，同于同一种方案也应选择不同的侧重点。
- 对于极小游戏，或者急需上线的游戏，可以使用InstantGame，该方案集成了整套工具链，包括cdn，小游戏服务器部署。
- 对于相对较为大型的游戏，不推荐使用Addressables，原因是Addressables中的catalog会随着资源变多而膨胀，其中对JSON文件的解析需要花费较多时间。
- 对于AssetBundle而言，理想情况下会比Addressables等更快，但是会导致较多的开发时间。建议根据项目情况自行评估开发时间以及最终性能之间的取舍关系。
