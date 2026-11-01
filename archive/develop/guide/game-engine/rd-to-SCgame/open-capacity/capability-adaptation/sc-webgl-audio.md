---
title: "音频适配"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc-webgl-audio
update_time: 2024-07-24
---

> 此文档描述小游戏开发时音频适配问题。
> 更多详情见 [抖音小游戏 Unity WebGL 适配方案](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/sc_webgl_overall)

**本文档主要说明 WebGL 方案**下音频能力的限制并给出适配建议。

## 适配建议
**大多数情况下，直接使用 Unity 内的音频能力可以满足常见的游戏需求。**建议开发者注意参照当前文档和 Unity 官方文档给出的限制，避免使用不支持的音频特性。额外提供的 StarkAudio 接口作为补充，供有播放网络上音频文件需求的开发者选择接入。

## Unity 音频
### 适配情况
在 WebGL 方案中，Unity 音频能力从以下版本开始正式适配：
- Unity 2021
- 发布工具 StarkSDKUnityTools 3.1.0

这些基础音频能力经验证可用：
- AudioSource 播放、停止、暂停、恢复播放
- AudioSource 设置音量、静音
- 获取 AudioClip 总时长、获取/设置 AudioSource 当前播放进度

备注：
1. 若使用低于 3.1.0 版本 StarkSDKUnityTools 发布游戏，AudioSource.time 的设置和获取不可用，其他功能不受影响。
1. 若使用的 Unity 引擎版本不在适配范围或不兼容 3.0 以上版本的发布工具，可以考虑手动接入 StarkSDK 提供的 StarkAudio 音频接口来接管音频播放。

### 功能限制
Unity WebGL 仅支持有限的音频功能：
- 由于 Unity 在 WebGL 平台音频实现与原生平台存在较大差异，其本身仅支持有限的音频功能，这些限制也存在于小游戏 WebGL 环境中。
- 具体支持范围可参考 Unity 官方文档：https://docs.unity3d.com/Manual/webgl-audio.html

在小游戏环境中，还存在以下额外的特性或限制：
- AudioSource
  - 音频固定按默认音调、1 倍速播放。不支持调整音调和播放速率相关属性：pitch。
  - 音频组件均视为 2D Audio，在空间中的位置关系不会对音频效果产生影响。不支持空间音频相关属性：dopplerLevel、maxDistance、minDistance、rolloffMode、velocityUpdateMode。
- AudioClip
  - LoadType 仅支持 Decompress on Load、Compressed In Memory，不支持 Streaming。
  - 实际的 LoadType 会根据音频 Buffer 的大小、以最小内存占用为目标动态适配决定，无需开发者适配。
    - 具体来说，我们以 AudioClip 资源构建后压缩产生的 AAC 二进制数据是否大于 128k 为标准，将其区分为短音频和中长音频。
    - 短音频会视为 Decompress on Load，在 AudioClip 加载时解码，解码后的 32 位浮点线性 PCM 数据将一直占用内存直到该资源释放；
    - 中长音频会视为 Compressed In Memory，自动切换至调用 StarkAudio 音频接口本地播放，流式解码以优化内存占用。
    - 32 位线性 PCM 数据内存占用量（字节） = 时长（秒） x 通道数量 x (32 / 8) x 44100Hz

在设计游戏音频体验或相关玩法时，开发者应避免使用不受支持的能力。

### 优化建议
对于音频性能，还有以下优化建议：
- 双声道音频内存占用比单声道多一倍，如无必要建议使用单声道的 AudioClip。
- 建议对同时处于播放状态的 AudioSource 音效数量做出合理限制。

### 已知问题
iOS 处于静音模式且未连接耳机时，短音频和中长音频会遵循的不同的静音策略。

## StarkAudio 音频接口
> 小游戏环境中，Unity 播放长音频时会自动切换至调用 StarkAudio，**开发者通常无需手动接入****。**
StarkAudio 是 StarkSDK 提供的一套额外的 C# 音频播放接口，支持不通过 Unity 引擎直接调用宿主底层提供的 InnerAudio 能力来播放网络上的音频文件。该接口作为 Unity 音频适配之外的补充，开发者可根据需求选择使用（Optional）。

### 代码示例

```csharp
var op = new StarkAudioManager.InnerAudioContextOptions
{
    src = "http://127.0.0.1/sound/Battle.mp3", // 音频资源的 url 地址
    autoPlay = true,
    loop = false,
    needDownload = true
};
var ctx = StarkAudioManager.CreateInnerAudioContext(op);
ctx.Play();
```

### 注意事项
- StarkAudio 同时支持 Native 和 WebGL 方案。
- 仅支持 wav、mp3、m4a、aac 格式，推荐使用 44100 hz 采样率。
- 音频资源会根据 url 缓存，更新音频文件时请改变 url 或 query string，否则可能因缓存导致不生效。
- 尽量避免高频创建 InnerAudioContext，建议用对象池管理并复用 InnerAudioContext 实例，一定时间内不使用的实例及时销毁。

更多使用方式可参考 StarkAudioManager 接口注释。
