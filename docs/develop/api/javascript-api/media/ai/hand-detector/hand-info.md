---
title: "HandInfo"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/ai/hand-detector/hand-info
update_time: 2025-06-18
---

HandInfo 是描述手势动作的对象，通过[Detector.detect](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/hand-detector/detector) 方法返回。
## 实例属性

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| id | number | 手的 id |
| score | number | 识别置信度，取值范围为 0 到 1 |
| boundingBox | object | 手部矩形框描述 |
| actions | string | 手势动作 |
| rotAngle | number | 手部旋转角度 |
| rotAngleBothhand | number | 双手夹角 |
| seqAction | number | 动态手势值，没有为 0,参照动态手势说明 |
| keyPoints | Array[object] | 手部关键点 22 个，每个点的值为坐标（x,y) |

**boundingBox 属性**

| 属性名 | 类型 | 属性说明 | 备注 |
| --- | --- | --- | --- |
| x | number | 包围盒左上角 x 坐标 | 坐标原点(0, 0)位于左上角，向右为 x 轴正向 |
| y | number | 包围盒左上角 y 坐标 | 坐标原点(0, 0)位于左上角，向下为 y 轴正向 |
| width | number | 包围盒宽度 | right-left 得到 |
| height | number | 包围盒高度 | top-bottom 得到 |
| left | number | 矩形框距离屏幕左边距离 | - |
| right | number | 矩形框距离屏幕右边距离 | - |
| top | number | 矩形框距离屏幕上边距离 | - |
| bottom | number | 矩形框距离屏幕下边距离 | - |

**actions 属性**：
[取值和对应的手势说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/media/hand-detector/description)
## Bug & Tip
Tip： 坐标轴的原点（0，0）位于设备的左上角，向右为 x 轴正向，向下为 y 轴正向。
