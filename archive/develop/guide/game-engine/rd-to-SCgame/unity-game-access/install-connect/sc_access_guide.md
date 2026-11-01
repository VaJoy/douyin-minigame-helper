---
title: "Unity 小游戏接入指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/sc_access_guide
update_time: 2025-06-11
---

抖音 Unity 小游戏是一种即玩游戏解决方案。该方案的特点是可以在抖音/头条等字节系 App 中无需安装，即可运行商业游戏引擎（Unity/UE）开发的游戏。该方案包含两种核心能力，一个是**免安装沙盒运行**技术，一个是**小包化技术**。目前接入游戏超过 5000+，有多款 DAU 破百万。
*效果参考：*[**演示视频**](https://bytedance.feishu.cn/file/boxcnp8zDc6jiZFcLooQn2AcAcd)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/c8e04e5a3e3848a89df0918e234f7ad1)

字节流量矩阵
## 解决方案
Unity 小游戏为您提供以下解决方案：
- 在字节系 App 中运行基于商业引擎（Unity/UE 引擎）的原生游戏（仅 Android，APK 格式）方案。
- 在字节系 App 中运行 Unity WebGL 及其他引擎导出的**wasm**（A*ndroid/iOS*）能力。[Unity 小游戏 WebGL 方案说明](https://bytedance.feishu.cn/docx/doxcn54u9PAOduj5IHYd5AOPG0g)
- 调用字节系 App 中的商业化能力，如 广告、录屏、分享等。
- 调用字节系 App 中的分发能力，基于视频、feed流、直播、微端等。

## 接入流程

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a25882e51d214caf8cdbe70509e55903)

### 【阶段一】可行性及方案评估
> 相关手册：
> - 
> - [抖音Unity小游戏转换案例](https://bytedance.feishu.cn/docx/FUpRdoGXEokdXlx50QWcRqclnEh)
初步确认游戏项目是否可改造，适合用哪种方案；**native 方案**是字节独有的能力，其他平台不曾提供。遇到问题请以本文档为准。遇到问题在[反馈群](https://bytedance.larkoffice.com/docx/IsWKdCTnGoks2zx1IiscnDfYngg)中搜索更多有效信息。

### 【阶段二】简单验证：先运行起来
> 相关手册：
> - [抖音Unity小游戏WebGL方案说明](https://bytedance.feishu.cn/docx/doxcn54u9PAOduj5IHYd5AOPG0g)
> - [抖音Unity小游戏发布](https://bytedance.feishu.cn/docs/doccnGEsOm0yquys4iAgtVi7nKh#RBNyBI)
对于没有接触过抖音Unity小游戏的开发者来说，在动手改造之前，可以通过此步骤，先确定一下当前项目是否能在抖音下正常运行，提前暴露问题。
抖音小游戏平台提供了商业化及数据分析能力，能满足大部分项目的运营需求。并且**不支持**接入其他平台的商业化sdk。
验证步骤很简单：
1. 删除其他平台的 SDK（如广告 SDK、登录 SDK、支付 SDK 等），该操作同时能有效降低包体大小。
1. 如果使用**Native方案**：安全考虑，C++代码的插件需要以源码形式放在工程内，会对插件中的 so 文件进行安全扫描；不支持任何Java代码的执行或者对jni的调用，**需删除项目中的Assets/Plugins/Android下的java代码及jar包或aar包。如对抖音有破坏性行为，会封停账号，保留追究法律责任的权利。**
1. 连上手机，使用本地调试功能即可运行在抖音中进行效果验证 [抖音Unity小游戏发布](https://bytedance.feishu.cn/docs/doccnGEsOm0yquys4iAgtVi7nKh#5KSPt0)

---

### 【阶段三】抖音平台能力接入：接入更多平台能力
> 相关手册
> [**抖音Unity C# SDK接入文档**](https://bytedance.feishu.cn/docx/doxcnTom4J47auHMnkjGYMBaNnZ)
> [**抖音Unity小游戏发布**](https://bytedance.feishu.cn/docs/doccnGEsOm0yquys4iAgtVi7nKh)
> [**抖音Unity C# SDK发版记录**](https://bytedance.feishu.cn/docs/doccnfO07C3R783siaLMS4VdaKd#4YZSwo)
#### Step1 - 账号准备
- **申请开发者账号并注册游戏**
首先您得有一个[**抖音小游戏开发者平台**](https://developer.open-douyin.com/)账号，需进行注册。
接下来您得创建一个自己的游戏，如下图所示，请在小游戏开发引擎选项中选择**「Unity 引擎」**。注意：这里创建的游戏方案一旦选择，后续无法在普通小游戏引擎和 Unity 引擎之间进行转换。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/934e76f1ea574bdfafad16258f3cb8fc)

*图2：游戏类型选择*
#### Step2 - 了解SDK能力，接入SDK
- 下载[接入Demo](https://bytedance.larkoffice.com/file/PvlNbkVZuomSuXxOq0kc8IbBnWg)，了解相关能力及接入代码
- 安装[**抖音Unity C# SDK**](https://bytedance.feishu.cn/docx/doxcnTom4J47auHMnkjGYMBaNnZ)( [**视频讲解**](https://bytedance.feishu.cn/file/boxcnJb0xp51ExtYdemvR9ygc6M)** **）
- 接入所需能力，完成所有接口的回调处理[并在Editor下测试完成](https://bytedance.feishu.cn/docx/doxcnTom4J47auHMnkjGYMBaNnZ#doxcn824qC44sCsuSkrmERqlAmd)
#### 

---

### 【阶段四】体验调优：达到可上线标准的小游戏体验
- 首场景启动优化：用户启动游戏的耗时与取消率呈正相关，启动耗时越短转化率越高。为保证用户体验，在小游戏平台上线，我们对首包大小有如下约束:
- 使用 **原生** 方案，首包包体需小于 100M
- 使用 **WebGL** 方案，首包包体需小于 100M
这是一个较为宽松的标准，目的在于让接入方能早点拿到线上数据，再考虑优化。但显然，包体越小，下载，加载的速度会越快，取消率会越低。
优秀数据参考：Native方案，包体20M，WebGL方案，包体10M

对于WebGL方案
- 优化可以参考相关优化文档[抖音小游戏 Unity WebGL 适配方案](https://bytedance.larkoffice.com/docx/J20NdqbznogTmWxL9k1c2fc7nyc)
- 提供了分包工具，可优化首包代码大小 [Wasm分包工具说明](https://bytedance.feishu.cn/docx/doxcncpOeaEXbwssnURb64TA1wd?from=from)
- 从Unity2021版本开始，可以使用ASTC纹理压缩，能够使得运行内存减少，提升一定的运行时性能。
- 对于ab加载，尽可能早使用Unload，避免内存过大导致反复崩溃。
其他加快启动速度的可选优化
- 减少MonoBehaviour脚本中Start/Awake的逻辑
- 减少初始场景的内容
- 采取分帧策略，延迟加载等

---

### 【阶段五】发布上线与运营
> 发布 -> 送审 -> 上线 -> 运营
#### 构建及发布
请参考文档：[抖音Unity小游戏发布](https://bytedance.feishu.cn/docs/doccnGEsOm0yquys4iAgtVi7nKh)
需要使用CI来构建发布请参文档中的[FAQ](https://bytedance.feishu.cn/docs/doccnGEsOm0yquys4iAgtVi7nKh#2Bsvms)部分
#### 运营
在抖音运营小游戏和在微信/其他平台有**很大不同**
- 视频是分发载体，游戏入口挂载在视频的锚点上，没有视频，就没有用户。
- 游戏数据的好坏，会影响视频在推荐系统的评分（如果性能没有优化好，使用wasm方案 iOS 会带来整体的负向效果，所以建议前期不要考虑上 iOS，先理清运营思路，优化好产品再上）。
- 用户看到视频后进入，对内容有一定期待，所以相对于图文广告，相对可容忍更多一点的首包下载时间，但更小的首包，肯定转化率更好。

在这之前请先阅读：[字节小游戏介绍&发行攻略](https://bytedance.feishu.cn/docs/doccnrf3eMsj86MboKWlwHBpYqf) ，**视频分发**场景有其独特的特性，下面介绍几个案例，可以去体验学习一下他们的游戏版本节奏和运营方式（可安卓抖音搜索体验游戏和查看官号）

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/33589ded322f41a1b7d92fd288a07ecb)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/413ba0bf655a45669f5af325b0b40bba)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ec8509abd0c84e2abc0b7d5589e01b00)

*游戏二维码*

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/97350d345b6c4098976a066897bf6fb7)

*官号二维码*

### 其他注意事项
- [抖音Unity小游戏目录说明与缓存策略](https://bytedance.feishu.cn/docx/doxcndqvjqK0FlitAnvamW2A0Pg)
- [WebGL方案优化建议](https://bytedance.larkoffice.com/docx/doxcnXixXNn6KkvH3NglKJlr3Zd)
## 
## 关于抖音普通小游戏能力
抖音Unity小游戏提供的解决方案与抖音普通小游戏不同，抖音普通小游戏提供的平台能力对于Unity C# SDK也有一定的开发工作量，我们目前同步支持了大多数抖音普通小游戏提供的平台能力，例如排行榜、loading加载背景图、插屏广告、banner广告等，现在在Unity C# SDK上你都可以找到对应的api；普通小游戏更新的平台能力在多数情况下，Unity C# SDK也会在短期内同步支持，当然，如果你想要更快的在Unity C# SDK上使用普通小游戏的某个平台能力，可以前往抖音Unity小游戏意见和反馈群中催更

## 问题反馈
[问题反馈与联系我们](https://bytedance.larkoffice.com/docx/IsWKdCTnGoks2zx1IiscnDfYngg)
## 其他参考资料
[抖音Unity小游戏FAQ](https://bytedance.feishu.cn/docx/doxcn9SfMOWLHiqeSJa9gtMFNzb)
[字节小游戏开发者常见问题FAQ](https://bytedance.feishu.cn/docs/doccnNMzHGscpzkbOF4XlzjGImb)** **
[关注【抖音创作者学院】官方账号](https://www.douyin.com/video/6761676940127538446)
