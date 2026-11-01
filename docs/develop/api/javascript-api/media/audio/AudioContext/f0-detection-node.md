---
title: "F0DetectionNode"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/f0-detection-node
update_time: 2024-07-24
---

F0DetectionNode 是一个提供输入源的音高检测数据的节点。约 20ms 检测一次。音高数据最多保存 2 秒，每次调用获取的是最近 2s 的数据。可以通过[AudioContext.createF0Detection](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-f0-detection) 创建。
## 属性
继承其父类 AudioNode 的属性。
| 属性名 | 类型 | 读写特性 | 说明 | 最低支持版本 |
| ------ | ------ | -------- | ----------------------------------------------------------- | ------------ |
| min | number | 只读 | 当前音高检测下限值，目前实际值固定为 0 | 1.34.0 |
| max | number | 只读 | 当前音高检测上限值。目前实际值为 AudioContext.sampleRate/30 | 1.34.0 |
## 方法
继承其父类 AudioNode 的方法。
### F0DetectionNode.getF0DetectionData()
获取当前的音高检测数据。返回结果为 JSON 对象。
#### 语法
```
F0DetectionNode.getF0DetectionData()
```
#### 参数
无
#### 返回值
| 参数名 | 参数类型 | 说明 |
| ------ | ------------- | ---------------------------------------- |
| size | number | 返回的 time 和 data 数据的数组长度 |
| time | Array[number] | 时间数据，每条数据的时间间隔为 20ms 左右 |
| data | Array[number] | 对应的音高数据 |
