---
title: "AudioParam"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/audio-param
update_time: 2024-07-24
---

AudioParam 表示音频相关的参数， 通常是一个 AudioNode (如 GainNode.gain) 的参数。一个 AudioParam 可以被设置为一个具体的值或者变量 ，可以被设置在特定的模式下特定的时间发生。
**当前只支持一种类型的 AudioParam： a-rate 参数。**
## 属性
| 属性名 | 类型 | 读写特性 | 说明 |
| -------------- | ------------ | -------- | ------------------------------------------------------------------- |
| context | AudioContext | 只读 | 代表当前 AudioParam 指向的 AudioContext |
| automationRate | string | 只读 | 代表 a-rate 和 k-rate 参数的 AudioNode 类型，目前只支持 a-rate |
| defaultValue | number | 只读 | 代表被具体的 AudioNode 创建的 AudioParam 的属性的初始的音量 |
| minValue | number | 只读 | 代表参数有效范围的最大可能值 |
| maxValue | number | 只读 | 代表参数有效范围的最小可能值 |
| value | number | 可读写 | 代表音频参数目前的实际值；初始化设定为 AudioParam.defaultValue 的值 |
## 代码示例
```js
const gainNode = ctx.createGain();
gainNode.gain.value = 0;
// 这里的 value 的赋值就是设置 gainNode.gain 属性指向的AudioParam对象的value值
// 所有类型为AudioParam对象的节点属性都需通过“属性名.value”的方式访问控制
```
## Bug&Tip
- Tip: 所有类型为 AudioParam 对象的节点属性都需通过“属性名.value”的方式访问控制。
