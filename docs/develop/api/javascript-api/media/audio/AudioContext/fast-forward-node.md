---
title: "FastForwardNode"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/fast-forward-node
update_time: 2024-07-24
---

FastForwardNode 可以快速将上游节点的输出写入到文件。可以通过[AudioContext.createFastForward](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-fast-forward) 创建。
## 属性
继承其父类 AudioNode 的属性。
## 方法
继承其父类 AudioNode 的方法。
### FastForwardNode.start(string path,number samples)
开始快速写入。
#### 参数
| 属性名 | 类型 | 必填 | 说明 | 最低支持版本 |
| ------- | ------ | ---- | --------------------------------------------------------------------------------------------------- | ------------ |
| path | number | 是 | 指定输出文件路径（string），文件后缀需指定为 mp4，m4a，wav 中的一种 | 1.34.0 |
| samples | number | 是 | 需要手动指定希望快速输出多少音频样本 samples，如果希望输出 30 秒，则 samples = ctx.sampleRate * 30 | 1.34.0 |
## Bug & Tip
- Tip：要使用相同的 path 进行文件写入，否则可能导致录制音频播放时出现提前结束的问题。
- Tip：需要手动指定希望快速输出多少音频样本 samples，如果希望输出 30 秒，则 samples = ctx.sampleRate * 30。
- Tip：注意，不要在快速输出完成之前再次调用 start，确保在 onended 调用之后再对 FastForwardNode 进行操作。
- Tip：⚠️ 特别注意，节点不应同时连接（直接或间接）到 ctx.destination 和 FastForwardNode，否则会导致音频播放不正确：在进行快速输出后，音源节点的播放进度会向前推进。
- Tip： ⚠️ 特别注意，在进行快速输出前（调用 FastForwardNode.start），尽量先停止当前所有音频输出，否则可能在一些低端机器上导致当前播放的声音出现卡顿，且快速输出处理时间变长。
如果输入节点没有输出，不会写入文件。
- Tip：⚠️ 特别注意，所有直接或间接连接到 FastForwardNode 的所有音源节点必须保证输出文件来自本地，如果音频文件来自网络，可以使用 tt.downloadFile 方法将音频文件预加载，在加载成功后再调用 FastForwardNode 的 start 方法。
部分音频节点不支持快速输出：包括：
- **AnalyserNode**（可以连接到 FastForwardNode，但不会在快速输出时进行音频分析）。
- **F0DetectionNode**（可以连接到 FastForwardNode，但不会在快速输出时进行音高检测）。
- **StreamSourceNode**（不支持流式音源，如麦克风，流媒体，请录制出本地文件再进行操作）。
- **StreamFileWriterNode**（FastForwardNode 自带文件写入功能）。
- **VolumeDetectionNode**（可以连接到 FastForwardNode，但不会在快速输出时进行音量检测）。
