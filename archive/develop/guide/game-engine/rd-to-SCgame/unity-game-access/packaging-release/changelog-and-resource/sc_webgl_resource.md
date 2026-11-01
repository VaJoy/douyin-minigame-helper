---
title: "小游戏资源部署与缓存"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/packaging-release/changelog-and-resource/sc_webgl_resource
update_time: 2024-12-30
---

> 本文介绍小游戏资源部署与缓存相关内容
> 更多内容请见：[Unity WebGL 字节小游戏适配方案](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/sc_webgl_overall)

## **资源介绍**
在转换完成后，会在导出路径下生成如下目录
**不使用wasm分包时：**

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/0e0435e78a4c4349a57fd2089cfa7855)

**使用wasm分包时：**

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ab37dbd51a08451f8156fc6bbec6f00e)

- scwebgl-bundles.js - 配置文件
- StreamingAssets
- webgl.data - 首包资源
- webgl.framework.js - 胶水代码
- webgl.wasm - wasm代码包（不分包时）
- split_main.wasm - wasm主包（分包时）
- split_sub.wasm - wasm子包（分包时）

## **其他资源部署**
目前 Unity 小游戏首包上限为**100MB**，如果首包资源大小超过该值，需要游戏做相应的资源优化，将不需要在首屏渲染的资源通过各种方案部署到CDN。可参考 [资源按需加载概述](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/performance-optimization/start-up/resource-upload/sc_webgl_load_overview) 。
#### **Assets**
如果有用到纹理压缩和音频API，导出插件自动生成。将此目录部署到服务器即可
#### **StreamingAssets**
AssetBundle和Addressables资源目录。 如果是用的AA，构建时默认打包到StreamingAssets目录下。但如果是用的AB，或者自定义了bundle的生成目录，需要将bundle移动到StreamingAssets目录

#### **资源服务器注意事项**
1. 使用 brotli 或 gzip 压缩：
  - 如果 AssetBundle 使用未压缩格式打包，应尽量开启 brotli 或 gzip 压缩
  - 如果 AssetBundle 使用 LZ4 格式压缩打包，则不建议开启 brotli 或 gzip 压缩，避免二次解压开销
  - 直接部署在 CDN 上的 json, xml, csv, txt 等文本格式配置文件，应尽量开启 brotli 或 gzip 压缩
1. 为确保不同网络条件的下载成功率，单个请求文件建议控制在 2-5 MB 以内（理论最大值为 100MB，超时默认为 60s）
1. 跨域问题在平台内部已经做了处理：[跨域问题](https://juejin.cn/post/6844903882083024910)
1. 网络安全域名、SSL 等问题请参考文档：[网络通信适配](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_network)

## **资源更新说明**

> **注意**
> 对于开发者自行部署在 CDN 上的 AssetBundle 资源，需要留意 CDN 缓存机制造成的更新延迟问题。

相同路径的文件在源站修改后，一段时间后才会同步到所有边缘节点（从数小时到数天不等）。如果不同版本资源使用相同的 CDN 路径，就会导致游戏版本更新后用户仍下载到旧的资源文件。可以使用这些方法解决：
- 每次发新版本更换 CDN 资源路径，例如 `version1/xxx`，`version2/xxx`
- 项目中的资源配置文件（例如 addressables 的 `settings.json` 和 `catalog.json`、YooAsset 的 `Version.txt`）的文件名通常是固定的，应避免这些文件使用缓存。
  - 对这些文件，可以在源站或 CDN 加上不允许缓存的 HTTP 响应头，例如 `no-cache`，请自行查询对应 CDN 服务商文档进行设置。
  - 此外，通过 HTTP 请求的资源会自动缓存到本地。为避免缓存，可以将这些文件的文件名或扩展名配置在“不自动缓存的文件”中。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/61cf4812a8a34c63908426a040f4d746)

## **资源缓存**
请阅读 [小游戏资源缓存](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/changelog-and-resource/sc_webgl_resource_cache)

## 游戏版本更新说明
请阅读 [小游戏版本更新](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/changelog-and-resource/sc_webgl_version_update)
