---
title: "设置帧率"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/drawing/set-frame-rate
update_time: 2025-02-20
---

## 
| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

## TT.SetPreferredFramesPerSecond
> TTSDK 6.2.5 及以上版本支持该能力
### 语法

```csharp
TT.SetPreferredFramesPerSecond(fps)
```

### 参数说明
**fps：**

| 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- |
| int | 60 | 是 | 默认渲染帧率为 60 帧每秒，有效范围 1-60 |

### 返回值
无
### 错误码

| errNo | errMsg | 说明 |
| --- | --- | --- |
| 20000 | internal error | 小游戏框架内部错误，有需要请[创建工单](https://developer.open-douyin.com/work-order-page?tab=workOrderRecord)咨询 |

### 代码示例

```csharp
// 修改渲染帧率为30帧每秒
TT.SetPreferredFramesPerSecond(30);
```

### 备注
- WebGL 和 Native 方案均可使用该方法设置帧率，区别是 WebGL 是通过平台来实现，Native 方案则是调用 Unity 的 `Application.targetFrameRate`来设置帧率。
- WebGL 方案下仍可以使用 `Application.targetFrameRate` 来设置帧率，但需要注意垂直同步`QualitySettings.vSyncCount`的设置，但更推荐使用`TT.SetPreferredFramesPerSecond`设置。
- WebGL 方案，通过`Application.targetFrameRate` 设置的帧率，不能被 60 整除或超过 1000 的值会造成帧率不稳定或与预期帧率不一致。使用 `TT.SetPreferredFramesPerSecond` 不会。
