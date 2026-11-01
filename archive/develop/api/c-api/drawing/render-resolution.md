---
title: "渲染精度"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/drawing/render-resolution
update_time: 2025-03-10
---

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 仅支持 WebGL 方案。 |
| 注意事项 | 不支持 Unity 自带的 Screen.SetResolution() 等分辨率设置方式。 |
| 相关教程 | 无 |

## TT.SetPreferredDevicePixelRatio
> TTSDK 6.2.7 及以上版本支持该能力
设置 Unity 引擎小游戏的设备像素比（DevicePixelRatio），影响游戏的实际渲染分辨率。
### 语法

```csharp
public static void SetPreferredDevicePixelRatio(float devicePixelRatio);
```

### 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| devicePixelRatio | float | -- | 是 | 设备像素比。 |

### 返回值
无
### 代码示例

```csharp
var defaultPixelRatio = TT.GetSystemInfo().pixelRatio;
TT.SetPreferredDevicePixelRatio(defaultPixelRatio * 0.5f); // 设置渲染精度为默认的 0.5 倍
```

## 备注
1. 该接口通过改变 Unity 引擎感知到的 `Module.devicePixelRatio` 来设置渲染分辨率，不会影响 `window.devicePixelRatio`。
1. 通常情况下，小游戏 `实际渲染分辨率 = 逻辑分辨率 * devicePixelRatio`，默认渲染分辨率与屏幕物理分辨率一致。
  - 主流 iOS 设备的默认 devicePixelRatio 通常为 2.0 - 3.0。
  - 主流 Android 设备的默认 devicePixelRatio 可能为 2.0 - 4.0。
1. 适当降低渲染精度能够减少渲染开销、提升游戏帧率、减少设备发热：
  - 可通过 [TT.GetSystemInfo()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/system/get-system-info) 接口获取设备的 devicePixelRatio 默认值，以默认值为基础调整渲染精度（见上方代码示例）。
  - 发布工具中的配置项「iOS Device Pixel Ratio」也可以用来设置 iOS 平台下游戏默认 devicePixelRatio。
