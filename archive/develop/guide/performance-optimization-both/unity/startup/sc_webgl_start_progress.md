---
title: "WebGL启动流程与时序"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/startup/sc_webgl_start_progress
update_time: 2024-07-24
---

> 此文档描述小游戏启动的流程和时序
> 更多详情见[Unity WebGL 字节小游戏适配方案](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/sc_webgl_overall)

## **启动加载时序**
Unity WebGL拉起流程如下图所示：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/d97b93f1897e49298692bebeaa96c8b7)

## 拉起Unity游戏**流程**
### 流程图

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a729bc89a65043b4ba9e5791f118006f)

### 关键步骤
1. 检查基础库是否需要更新
1. 在开放平台加载页面下载游戏首包，包含游戏wasm代码、资源以及胶水代码
1. 进入Unity加载页面，检查资源是否完整
1. 如果采用wasm分包，会检查是否包含wasm子包
1. 对wasm代码进行解压、编译、实例化
1. 完成上述准备后，等待wasm main函数被调用，进入Unity运行阶段

## **QA:**
1. Q：有哪些文件需要放CDN服务器？
> A：Adressable/AssetsBundle生成的文件
1. Q：资源(data)或资源包是否需每次下载？
> A: 资源(data)文件为首包内容，首包下载后，则不会再次下载。其它资源文件，主要是外部CDN资源文件，需要手动配置需要缓存的资源域名，会对需要缓存的下载资源进行缓存，有缓存的情况下则不会再次下载。
