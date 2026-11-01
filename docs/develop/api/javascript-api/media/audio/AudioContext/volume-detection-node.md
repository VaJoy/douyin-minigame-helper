---
title: "VolumeDetectionNode"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/volume-detection-node
update_time: 2024-07-24
---

VolumeDetectionNode 是提供输入源的音量检测数据的节点。约 20ms 检测一次。音高数据最多保存 2 秒，每次调用获取的是最近 2s 的数据。可以通过[AudioContext.createVolumeDetection](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-volume-detection) 创建。
## 属性
继承其父类 AudioNode 的属性。
## 方法
继承其父类 AudioNode 的方法。
### VolumeDetectionNode.getVolumeDetectionData()
获取当前的音量检测数据。返回结果为 JSON 对象。
#### 语法
```
VolumeDetectionNode.getVolumeDetectionData()
```
#### 参数
无
#### 返回值
| 参数名 | 参数类型 | 说明 |
| ------ | ------------- | ---------------------------------------- |
| size | number | 返回的 time 和 data 数据的数组长度 |
| time | Array[number] | 时间数据，每条数据的时间间隔为 20ms 左右 |
| data | Array[number] | 对应的音高数据 |
