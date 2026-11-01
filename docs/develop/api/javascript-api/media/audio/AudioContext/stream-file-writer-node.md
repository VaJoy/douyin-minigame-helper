---
title: "StreamFileWriterNode"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/stream-file-writer-node
update_time: 2024-07-24
---

StreamFileWriterNode 对象能将一个或多个输入节点写入到文件。可以通过[AudioContext.createStreamFileWriter](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-stream-file-writer/) 创建。
## 属性
继承其父类 AudioNode 的属性。
## 方法
继承其父类 AudioNode 的方法。
### StreamFileWriterNode.start(string path)
开始将输入节点写入到文件。
#### 参数

| 属性名 | 类型 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- |
| path | string |  | 指定输出文件路径，需指定为 mp4，m4a，wav 中的一种 | 1.34.0 |

#### 返回值
无
### StreamFileWriterNode.stop()
在需要停止文件写入时手动调用，完成文件写入。
#### 参数
无
#### 返回值
无
## Bug & Tip

- Tip: 注意，每次调用 StreamFileWriterNode.start 都会结束当前节点的文件写入，不要使用相同的 path 进行文件写入，否则可能导致写入的音频文件播放时出现提前结束的问题。
