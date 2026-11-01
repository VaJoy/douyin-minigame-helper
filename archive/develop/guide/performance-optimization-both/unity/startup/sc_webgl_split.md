---
title: "Wasm分包工具说明"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/startup/sc_webgl_split
update_time: 2026-08-26
---

> 文档说明：本文档描述 Unity WebGL方案下，对代码进行分包优化的工具使用方法。
> *了解更多：*[接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_access_guide)，[Webgl方案说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/overview-and-compatibility/sc_webgl_compatibility)** **

## 背景介绍
  Unity编译出来的WebGL产物中，代码包文件是一个wasm文件。通常情况下，小游戏的 wasm大小在30M左右，经过Brotli压缩后为6M左右。Unity WebGL小游戏在启动时，需要先将代码包下载下来，再对wasm代码进行编译，通常会占用较高的内存以及较长的编译时间。
  使用wasm分包工具，将原来的wasm代码包拆分为两个，一个用于启动加载，另一个可以延迟加载。使得小游戏可以先加载较小的首包进入主场景，再异步加载剩下的分包。
好处：
1. 首包变小，下载时间变短，编译时间变短，优化启动时间
1. 对于iOS来说，减少内存使用，以支持更多 iOS 低端机上运行
1. 减少编译时间，降低了游戏前期的发烫情况

## 工具介绍
开发者可以在测试阶段，通过真机运行预览，并尽量覆盖游戏内的场景，特别是启动后最先进入的场景和关卡（比如新手教学，游戏最初的关卡内容）来收集信息。
在开发者进行一次分包并发布到线上后，即可自动开启线上收集能力。线上收集能力可以收集用户在线上版本游玩时产生的新增函数，有助于开发者更全面地收集Wasm函数。真机收集和线上收集函数可以同步进行。
工具上会显示收集到的函数个数，这时候就可以点击分包，将收集到的函数加入首包。可同时包含真机和线上收集到的新增函数个数。
收集的场景覆盖率越高，命中子包的时机就可以相应延后，使得首包可以满足大部分新玩家前几分钟的游戏进程。
## 工具入口
在抖音开发者工具（版本>=4.3.2）的上方工具栏：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/8cd6eea870334c36a66703e65f999e9a)

## 使用流程
### 初始界面
当首次进行wasm分包时，或者选择的WebGL包文件中的wasm代码发生变化，则会打开工具界面如下：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/4688f58ee1554e6f8f62dfc01f57d5da~tplv-9nona0m7ha-image.image)

打开该界面，表示当前AppId所选择的wasm文件没有分包记录，需要进行首次分包。
**输入项：**
- **WebGL包**：通过构建工具构建出来的WebGL产物，为一个名称为**webgl_package-xxx.zip**的压缩包文件。
- **版本描述**：针对此次分包版本的描述
- **增量分包**：基于之前结果再次进行分包的能力，详情请见下方的`增量分包说明`部分
### 主要流程
1. **启动代码分包**
在初始界面上有一个【启用代码分包】按钮，点击该按钮，会将WebGL构建产物上传到服务器端，服务器端会对Wasm文件进行预处理：
> **请注意，这个【**启用代码分包**】并不是做wasm分包，只是为wasm分包前函数收集做准备，你需要收集一些函数后，再点击后续步骤中的【收集完成，开始分包】，才是最终的wasm分包。**

   1. **上传分包以及预处理：**
此步耗时将需要数分钟，一般为3-5分钟，如果超过10分钟处于此状态，请重启开发者工具。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/7e478e62fdf74a53bbd3127c6a675cf3~tplv-9nona0m7ha-image.image)

   1. **预处理完成**
服务端预处理完成代码之后，将跳转到以下界面。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/ea6cec83d56c4caeaf3078a28c09aab3~tplv-9nona0m7ha-image.image)

界面将包含以下信息：
- **【WebGL包】**：此次分包所选中的文件，也可在此时切换其他WebGL包，来开启一个新的分包。
- **【函数收集信息】：**
  - **新增函数个数**：表示当前正在运行过程中，所收集到函数个数。这个数值会在游戏运行过程中变化，当这个数值长时间未发生变化并大于0时，可以认为函数收集完成，可以点击【收集完成，开始分包】进行Wasm分包**。**
  - **当前首包函数个数**：已经分好的Wasm首包中的函数个数。
  - **总函数个数**：原始Wasm文件中的函数总个数。
- **【加载预览，开始收集函数】**：点击此按钮将在页面上显示一个预览二维码，可通过真机扫描预览，进行函数收集。
  - 在【详情页】打开局域网预览，可加快出码速度。但是需要确保扫码的手机同 IDE 处于同一局域网。
  
![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b111d0b684b241c59f961eeb0ec51a7c~tplv-9nona0m7ha-image.image)

1. **预览收集**
点击**【加载预览，开始收集函数】,**将会自动执行预览操作，预览成功后显示二维码
   1. **显示预览二维码**
此时可使用手机扫码预览运行游戏，在运行期间将会观察到新增函数个数增加。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/6aeea1569dad48ceb4c7c5dc1f5fe90b~tplv-9nona0m7ha-image.image)

   1. **扫码收集**
  使用Android/iOS手机扫码预览进行函数收集，请尽可能的覆盖新手教学以及最初的关卡内容，防止玩家进入游戏，在启动游戏过程中便触发了子包函数加载，而产生负向的效果。
  尽量在真机上覆盖更多的场景，尽量将子包的加载延后，将很大程度提升游戏体验。
  
  **收集到函数，新增函数数值有变化**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/bdb1bb0e956b4bfc9711f58318ef061c~tplv-9nona0m7ha-image.image)

- **【上传函数名】：**这是 4.5.2版本 新增的功能，可以让开发者上传一个包含需要进入主包的函数签名的文本文件，签名信息对应打包产物的symbols.json。注意不要有标点符号，用换行符分隔函数名即可。格式如下：

```csharp
UNBridge_setCallBackTimeout_m1415E8F925390D730A5583CE905DA4A1225531B1
UNBridge_UnListen_mFDC00670C329376C37789F8E85D1CFD9604BFCE7
UNBridge_Start_mD970BD8AE4D3C118210E54039C0742C700D38C38
UNBridge_SendEvent_m0ECCC961DC9D66D982C5CD936A202BEC158E9FC8
UNBridge_RegisterEvent_m845716EF218F609B5DEF6EB187E141CB1D57BF92
UNBridge_OnDestroy_mABD94EF89DFC28543B4F073F60005B6C5FF8E077
UNBridge_MixCall_m2B4047732B2396FC1FF17A80C3BDC27D5F468FD0
UNBridge_HandleMsgFromiOSNative_mC462D7C0E14100521AFBF0EDC444FDB7CF5C3766
UNBridge_HandleMsgFromNative_mFF2C2B4C18FC12AFF8801F9E46B466F83194C134
UNBridgeHandler_PrintJsonData_m87B5A7D0135EBEDA95DC308F98447BCEE6F9D272
UNBridgeHandler_ParseJsonData_m39ECBDB42DF86869B71F361CC29CDADFE7655922
UNBridgeHandler_OnCall_m267178588152C4D1AE6A90E146FE6CEEFFBAEE04
```

上传后，会返回匹配结果，同时**【新增函数个数】**也会同步更新。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/bb02536ebbd34477a0db28c0c7fef74e~tplv-9nona0m7ha-image.image)

- 【**收集完成，开始分包**】：当认为Wasm函数收集完成，即可以点击该按钮向服务器端请求Wasm分包。

1. **分包**
  点击【**收集完成，开始分包**】，服务器将对代码进行处理，将wasm代码分为首包和子包。
  对于4.4.6及以上的 IDE 版本，分包可选择 release 或 debug 版本（4.4.6之前固定为 release）。debug 包体略大，但可以还原 wasm 错误堆栈，详细说明可参考[此文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/how-to-debug)。
  
![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/264d550b3cfe4f38bf20d42bcb408b2e~tplv-9nona0m7ha-image.image)

  分包过程中将经历以下状态：
   1. **分包中**
此过程耗时较长，一般为7-8分钟，（**有可能需要等待超过10分钟**），如果长时间处于此状态，请重启开发者工具

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/ed19281540bc4ce6bf28617f8af1f638~tplv-9nona0m7ha-image.image)

   1. **分包完成**：
当前首包函数个数将变化，同时出现下载分包文件按钮，点击【下载分包文件】按钮，将会获得完整的可用于发布的文件。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/5dd558c647e34ff08b03a3f5cb606c74~tplv-9nona0m7ha-image.image)

   1. **下载后得到的文件**
此文件名称将类似于webgl-split-xxxx.zip。此文件**可用于最终测试版本的发布**。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/9269e81838624f78bbe087f12c9ad10e~tplv-9nona0m7ha-image.image)

另外开发者可以通过再次点击**【加载分包预览，开始收集函数】，**继续收集函数，此操作可重复进行，直到新增函数不再增加，即可认为分包已经完成，点击开始分包之后，再下载分包文件用于后续的发布即可。

### 线上收集
1. 开启能力（需抖音开发者工具4.4.1版本及以上）
开发者进行一次分包并发布到线上后，即可自动开启线上收集能力。当对应WebGL包收集到线上用户在游戏运行过程中产生的新增函数，再次使用线上运行代码包对应的原始webgl包，打开wasm分包界面进行预览时，可看到新增函数个数有数量上的变化：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/a3b178b8ab5e4efdb1d15355fb5f3ba1~tplv-9nona0m7ha-image.image)

1. 分包
如果认为函数收集完成，可以点击【收集完成，开始分包】进行Wasm分包。后续步骤和真机收集的流程一致。

### 其他功能
- **【获取首包函数以及新增函数】：**当收集到新增函数或者首包函数大于0时，点击此按钮将会向服务端获取函数信息，获取完成后，函数信息将在开发者工具的编辑区显示。仅支持获取最新一次分包的首包函数以及新增函数。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/a17f9b18a5b148e783aaeef9677e48d3~tplv-9nona0m7ha-image.image)

- **【终止分包】：**此次分包不想再进行下去，或者有卡死现象，可点击此按钮回到初始状态，使用相同代码再次开启分包历史收集信息依然会保留。

## 增量分包说明
增量分包功能，可以在前一次收集到的Wasm函数基础上进行Wasm分包。用户可以在此版本上基于之前的分包结果，只需运行新增游戏内容即可。（增量分包仅支持在准备分包状态下进行选择。）

点击增量分包下拉列表可以显示分包历史列表，列表中会显示收集到的函数数量，md5，版本号，分包时间信息。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/7cc3520a9e5e4c9786728173a4aa0529~tplv-9nona0m7ha-image.image)

**点击某个历史记录**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/e88894d73baf4a109b299e3eb2cdd676~tplv-9nona0m7ha-image.image)

**启用代码分包后**
无需进行收集，就会在新增函数信息上立即显示新增函数个数。预览游戏后，运行此前未运行的游戏内容即可，继续收集函数，直到新增函数数量不再增加，即可认为收集完成，其主要流程和前面的分包流程都将保持一致。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/eb26e0b61f8c484aaee5dadab9d6394a~tplv-9nona0m7ha-image.image)

## 注意事项
1. wasm分包可能无法将所有需要用到的函数收集全
1. 尽可能不要在游戏启动时，便触发了子包加载，会导致启动耗时增加，因此尽量覆盖新手场景，游戏启动阶段的内容。
当有一个函数未收集到，用到时都将会触发子包编译。如果是刚进入游戏时就触发了子包编译，子包编译时间可能会较长。原因是刚进入游戏时会存在JIT，使得wasm编译较慢。
1. 建议多次重复运行游戏，使用Android/iOS同时测试，并使用多个设备收集。
1. 当开启线上收集能力后，以往的历史分包记录保留最多10条。基于新版本的分包历史记录暂未限制记录上限。

## 分包工具命令行版本
### 简介
除了上面的IDE，我们还提供了命令行版本（tt-wasmsplit-ci），适用于自动化发版场景。通常情况下建议开发者优先用IDE分包，如遇特殊情况再考虑用CLI（Command-line interface)版本。
两者的功能一致，包括
1. 开启分包（支持增量分包）；
1. 获取函数收集信息；
1. 进行分包，并获取分包后游戏包；
1. 终止分包。
该工具以 npm 包形式提供，下载及使用方式请参考[readme](https://www.npmjs.com/package/@open-dy/tt-wasmsplit-ci)。

### 最佳实践
接下来我们以Unity为例，演示一下命令行分包的具体步骤。
1. 先在Unity工程中按照正常流程打出小游戏包，产物为a.zip。
1. 开启分包，生成 prepare 包。（prepare 包内会给所有函数做插桩，方便后续将收集到的函数上报至服务器）

```csharp
tt-wasmsplit-ci init -p <path/to/a.zip> -i <appId> -m <version description>
```

1. 在Unity**原始工程目录中**找到project.config.json文件，修改其中的unity -> build -> webgl 字段为上一步得到的prepare包的绝对路径

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/c135c13f66a8453ba14a9a3108cdd9f9~tplv-9nona0m7ha-image.image)

1. 生成预览码。注意传入的路径为unity的原始工程目录，该目录下要有上述project.config.json文件。

```csharp
tmg preview <path/to/unity原始工程>
```

这一步会生成二维码。
1. 用prepare包在真机上扫码预览，收集要进入主包的函数。
1. 觉得收集得足够全了，告知服务端做分包。注意 -p 的参数为第一步中打出的原始包a.zip，不是prepare包。

```csharp
tt-wasmsplit-ci dosplit -p <path/to/a.zip> -i <appId> -m <version description>
```

此步骤耗时较久，一般在5min左右。
1. 分包完成，产物会下载到本地。
1. 如果不想用分包方案，想回归一次性下发整个包体，那么调用以下命令，

```csharp
tt-wasmsplit-ci disable -p <package> -i <appId>
```

## 常见问题
1. 分包后，进入游戏出现卡顿现象。
   1. 主要原因是在加载子包时，是同步加载方式，在表现上会有卡顿，因此建议尽量多收集函数，可保证大部分场景不会出现卡顿。
1. 分包后的zip文件相比原始zip包的体积更大
   1. 这是符合预期的，在上传后，服务端会对包体进行处理，客户端加载时会加载一个较小的首包。
1. iOS扫码预览时，游戏无法进入
   1. 建议先使用Android手机进行收集，当收集足够多的函数之后，分包之后再进行预览，此时再使用iOS收集，将很大程度降低iOS无法进入的概率。
1. 同一 AppID 同时在不同 IDE 上进行分包操作，会造成状态混乱问题。相同 AppID 请避免同时在 多个 IDE 上进行分包操作。

我们于2026.7推出全新的wasm分包方案，相比于旧分包方案 iOS端游戏帧率提升10%+。无需重新收集函数，更新TTSDK（6.8.0+）及抖音开发者工具（4.5.5+）后重新分包即可（分包流程不变，仍可参考本文）。如有兴趣接入请飞书扫码填写问卷。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/89dd4ce800d74b02b005359c83c0dd9a~tplv-9nona0m7ha-image.image)
