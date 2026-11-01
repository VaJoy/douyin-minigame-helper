---
title: "高性能模式"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/performance-optimization/high-performance-mode
update_time: 2025-01-21
---

## 简介
为了提升 iOS 上[普通小游戏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/minigame/introduction)的运行时性能，我们推出了 iOS 高性能模式，游戏经过简单适配即可大幅提升性能。
**Unity 小游戏已经默认全量开启高性能模式**。
## 性能数据
从内测阶段的数据来看，接入高性能模式后，小游戏的 80 分位 FPS 有平均 69.01% 的提升（32.53 -> 54.98）。从原理上来说，高性能模式大幅提升了 JS 代码的运行效率，因此 CPU 压力较大的游戏，在接入高性能模式后会有较为明显的性能提升。
## 接入改造指南
### 1 内存限制
高性能模式利用了 iOS 系统的 WKWebView 能力，但是由于 WKWebView 本身对内存占用较高，高性能模式下对内存的限制会更加严格。**建议开发者在上线高性能模式前，针对内存进行优化**。具体来说，平台侧建议游戏在运行过程中**平均内存占用不超过 800MB，最高内存占用不超过 1.1 GB**，超过该限制可能会导致出现游戏异常退出、白屏等问题，进而造成用户投诉。
需要注意的是，高性能模式下小游戏运行在非抖音进程，因此在进行内存优化时，**需要针对小游戏进程进行内存优化**。小游戏的进程名一般为 WebContent，在使用性能测试工具时，请找到对应的 WebContent 进程进行测试。
**一般系统可能存在多个 WebContent 进程，因此需要找到当前小游戏对应的 WebContent 进程再进行测试**。在测试时可以先关闭后台其他应用，然后通过观察 CPU 占用、FPS 等数据来观察 WebContent 进程是否为游戏进程（游戏进程一般 CPU 占用不为 0）。
**录屏**接口对内存占用有一定影响，同时在低版本 iOS 系统上（< iOS 15.4）对 FPS 也有一定的影响，因此**建议开发者首先确认录屏功能的必要性后再接入录屏接口**，并且只在有需要时进行录屏。目线上有部分游戏在游戏过程中一直处于录制状态，建议对这种行为进行更改，确认当前内存占用、FPS 符合预期再进行录屏。平台也将会持续优化录屏性能，提供更优的体验。
### 2 运行环境要求
**抖音客户端版本要求**：抖音客户端版本需 >= 31.6.0。
**客户端基础库版本要求**：客户端基础库版本需 >= 3.43.0。
**系统版本要求**：iOS 版本需 >= 14.5，截止 2024 年 10 月，符合该要求的用户机型占比约为 96.7%。
不符合这三项要求的设备将运行在普通模式下，另外开发者上线前**请务必保证游戏在高性能模式和普通模式均可以正常运行**。
### 3 如何打开高性能模式
在 [game.json](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/mini-game-configuration) 中，配置 enableIOSHighPerformanceMode 为 true 即可打开高性能模式。目前局域网预览尚不支持高性能模式，请在预览时不要勾选「开启局域网快速预览」选项。

```json
{
    "deviceOrientation": "portrait",
    "enableIOSHighPerformanceMode": true
}
```

**如何确认是否已经打开高性能模式：**
1. 高性能模式下可通过访问 GameGlobal.isIOSHighPerformanceMode 判断是否为高性能模式，高性能模式下该变量为 true，普通模式下为 undefined。
1. 通过 vConsole 的颜色进行判断，普通模式下 vConsole 为绿色，高性能模式下 vConsole 为蓝色。 （Unity 小游戏vConsole在高性能模式下依然为绿色）

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/e1030dd0e7c14894a2343db7bbf27a75)

### 4 游戏适配
一般来说，小游戏可以直接运行在高性能模式下，但由于二者的运行环境存在一些差异，部分逻辑可能需要做针对性适配。当需要适配时可以通过以下方式判断当前环境是否为高性能模式：

```js
if (GameGlobal.isIOSHighPerformanceMode) {
    // 针对高性能的适配
}
```

#### 4.1 打开严格模式
在高性能模式下，开发者代码必须打开严格模式才能正常运行。一般游戏引擎产生的代码会自动编译为严格模式，开发者需要检查自己的业务代码是否也符合[严格模式](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)的标准。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/5b482adc75994511af9789e32beb4d8a)

#### 4.2 API 支持
目前高性能模式下部分 API 尚未完全支持，请参考下列表格进行适配。

| API 名称 | 支持情况 | 调用后行为 |
| --- | --- | --- |
| request/pause/resumeMicrophone | 不支持 | 抛出异常 |
| createCamera | 不支持 | 抛出异常 |
| createFaceDetector | 不支持 | 抛出异常 |
| createHandDetector | 不支持 | 抛出异常 |
| video.paintTo | 高性能模式下的 video 只支持 paintTo 到 2d context 的 canvas，不支持 paintTo 到 WebGL context 的 canvas 上 | paintTo 到 WebGL context 的 canvas 上无效 |
| video.play | 高性能模式下的 video.play 和 video.paintTo 一样不支持 WebGL context 上播放视频，有这类诉求可以使用引擎或者 webgl 的纹理绘制能力进行视频绘制 |  |

需要注意的是，getGameRecorderManager（录屏能力）接口会对性能会产生一定影响。在低版本机型上（< iOS 15.4），录屏时 FPS 会出现劣化，且开启录屏会使内存压力增大，建议开发者在线下进行充分的测试，确认没有性能问题后再开启录屏接口，或者根据系统版本确认是否开启该接口，否则可能导致线上出现性能/稳定性问题。平台也将会持续优化录屏性能，提供更优的体验。
#### 4.3 性能问题适配
在大部分情况下，高性能模式的性能都应优于普通模式。然而由于 iOS 系统存在部分问题，在低版本系统上可能会有性能下降的情况，需要针对这些情况进行适配。目前已知的问题如下：
##### 4.3.1 iOS 14.x 性能问题
在 iOS 14.x 系统下，部分游戏会出现单帧耗时低，但帧率依然很低的情况。此时可以尝试在获取 WebGL Context 时，将 antialias 参数设置为 true 进行解决：

```js
const canvas = tt.createCanvas();
canvas.getContext('webgl', {
    antialias: true,
});
```

##### 4.3.2 iOS 15.3 及以下版本性能问题
在 iOS 14 之后，多个 drawcall 间会共享同一份 vertexBuffer 和 indexBuffer，由于 iOS 本身的实现原因，会导致一些性能问题。截止 2024 年 10 月，受此影响的机型（iOS 14 - iOS 15.3）占比约为 6.7%。
目前主流的游戏引擎均有针对这一问题的修复，可以参考 [cocos](https://forum.cocos.org/t/topic/97808/11) 等游戏引擎的修复进行手动适配。此外 cocos 在 3.8.3 的版本上也针对抖音小游戏修复了这一问题，使用 cocos 3.8.3 及以上版本的用户不再需要手动修复。
cocos 在 3.8.3 上针对抖音小游戏高性能模式的修复可以参考[这里](https://github.com/cocos/cocos-engine/pull/16769/files)。
#### 4.4 高性能模式下暂不支持真机调试
IDE 中的「真机调试」能力暂不支持高性能模式，使用该能力时请不要在 [game.json](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/mini-game-configuration) 中配置为高性能模式，并且调试中的性能数据无法作为运行时性能的参考。
