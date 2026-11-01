---
title: "FadingNode"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/audio/AudioContext/fading-node
update_time: 2024-07-24
---

FadingNode 可以用于实现音频数据淡入淡出。可以通过[AudioContext.createFading](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/audio-context-create-fading) 创建。
![图片名称](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/other/9d901223e2828a56e641e4275c99c042_58397009-90ae-4c1d-a8aa-a3856a2b6849.png)
## 属性
继承其父类 AudioNode 的属性。
| 属性名 | 类型 | 读写特性 | 说明 | 最低支持版本 |
| ----------------- | ------ | -------- | ---------------------------------------------------------- | ------------ |
| contentDuration | number | 只读 | 淡入淡出效果的总长，淡入效果起点到淡出效果结束点之间的长度 | 1.34.0 |
| fadingInDuration | number | 只读 | 淡入效果的时长 | 1.34.0 |
| fadingOutDuration | number | 只读 | 淡出效果的时长 | 1.34.0 |
| fadingInCurve | number | 只读 | 淡入效果的曲线 | 1.34.0 |
| fadingOutCurve | number | 只读 | 淡出效果的曲线 | 1.34.0 |
## 方法
继承其父类 AudioNode 的方法。
### FadingNode.setFadingDurations(number total,number fadingIn,number fadingOut)
设置淡入淡出效果的时间参数，目前有三种取值，见 **曲线取值** 表格。
#### 参数
| 属性名 | 类型 | 说明 |
| --------- | ------ | ------------------------------- |
| total | number | 淡入淡出效果的总跨度时长 |
| fadingIn | number | 设置淡入效果的范围时长，单位 ms |
| fadingOut | number | 设置淡出效果的范围时长，单位 ms |
因为需要知道总长才能知道整体的形状，所以其关系图如下（可以参考说明部分图片）：
**fadingIn+未受影响的音频时长+fadingOut = total**
### FadingNode.setFadingCurves(number inCurve,number outCurve)
设置淡入淡出效果的曲线参数。
#### 参数
| 属性名 | 类型 | 说明 |
| -------- | ------ | --------------------------------------------------------------------------------------------------------------- |
| inCurve | number | 淡入效果的曲线，取值详见[曲线取值](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/fading-node/#曲线取值) |
| outCurve | number | 淡出效果的曲线，取值详见[曲线取值](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/audio/AudioContext/fading-node/#曲线取值) |
#### 曲线取值
| 取值 | 对应函数 | 描述 |
| ---- | -------- | --------------- |
| 0 | log | 曲线为 log 函数 |
| 1 | linear | 曲线为线性函数 |
| 2 | exp | 曲线为 exp 函数 |
## Bug&Tip
- Tip:  该 API 目前在小游戏中暂无效果，已经废弃，请开发者避免使用。
