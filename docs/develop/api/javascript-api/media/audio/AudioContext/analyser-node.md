---
title: "AnalyserNode"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/analyser-node
update_time: 2024-07-24
---

AnalyserNode 表示一个可以提供实时频域和时域分析信息的节点。可以通过
[AudioContext.createAnalyser](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-analyser)
创建。
## 属性
> 继承其父类 AudioNode 的属性
| 属性名 | 类型 | 读写特性 | 默认值 | 说明 | 最低支持版本 |
| ----------------- | ------ | -------- | --------- | --------------------------------- | ------------ |
| fftSize | number | 可读写 | 2048 | 用于频域分析的 FFT 初始尺寸 | 1.34.0 |
| maxDecibels | number | 可读写 | -30 | 用于 FFT 分析的初始最大功率（dB） | 1.34.0 |
| minDecibels | number | 可读写 | -100 | 用于 FFT 分析的初始最小功率（dB） | 1.34.0 |
| frequencyBinCount | number | 只读 | fftSize/2 | 值为 fftSize 的一半 | 1.34.0 |
## 方法
> 继承其父类 AudioNode 的方法
### AnalyserNode.getByteTimeDomainData(Uint8Array dataArray)
将当前波形，或者时域数据拷贝进 Uint8Array 数组（无符号字节数组）。
#### 参数说明
| 属性 | 类型 | 必填 | 说明 | 最低支持版本 |
| --------- | ---------- | ---- | ---------- | ------------ |
| dataArray | Uint8Array | 是 | 拷贝的目标 | 1.34.0 |
#### 语法
```
AnalyserNode.getByteTimeDomainData(dataArray)
```
#### 返回值
无
### AnalyserNode.getByteFrequencyData(Uint8Array dataArray)
将当前频域数据拷贝进 Uint8Array 数组（无符号字节数组）。
#### 参数说明
| 属性 | 类型 | 必填 | 说明 | 最低支持版本 |
| --------- | ---------- | ---- | ---------- | ------------ |
| dataArray | Uint8Array | 是 | 拷贝的目标 | 1.34.0 |
#### 语法
```
AnalyserNode.getByteFrequencyData(dataArray)
```
#### 返回值
无
### AnalyserNode.getFloatTimeDomainData(Float32Array dataArray)
将当前波形，或者时域数据拷贝进 Float32Array 数组。
#### 参数说明
| 属性 | 类型 | 必填 | 说明 | 最低支持版本 |
| --------- | ------------ | ---- | ---------- | ------------ |
| dataArray | Float32Array | 是 | 拷贝的目标 | 1.34.0 |
#### 语法
```
AnalyserNode.getFloatTimeDomainData(dataArray)
```
#### 返回值
无
### AnalyserNode.getFloatFrequencyData(dataArray)
将当前频域数据拷贝进 Float32Array 数组。
#### 参数说明
| 属性 | 类型 | 必填 | 说明 | 最低支持版本 |
| --------- | ------------ | ---- | ---------- | ------------ |
| dataArray | Float32Array | 是 | 拷贝的目标 | 1.34.0 |
#### 语法
```
AnalyserNode.getFloatFrequencyData(dataArray)
```
#### 返回值
无
## Bug&Tip
暂无。
