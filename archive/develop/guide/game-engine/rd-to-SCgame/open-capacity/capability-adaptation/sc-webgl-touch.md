---
title: "多点触控适配"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc-webgl-touch
update_time: 2025-12-04
---

> 此文档描述小游戏开发时多点触控适配问题。
> 更多详情见[抖音小游戏 Unity WebGL 适配方案](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/sc_webgl_overall)。

**本文档说明 WebGL 方案**下对多点触控的适配。供有多点触控需求、并且在 iOS 环境下实际遇到了按键粘连或触控/点击事件丢失问题的游戏参考接入。

## 开发参考
### 重载触控
根据项目使用的 UI 方案参考对应的小节进行接入。
#### UGUI
> 如果项目使用 Unity 自带的 UGUI 作为 UI 解决方案，需要重载 EventSystem，参考本小节步骤接入。
1. 在 Unity 场景内找到 EventSystem，挂载 TTInputOverrideBypass 组件。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/39b53bd6d50f45228ab28597a04061d5~tplv-9nona0m7ha-image.image)

1. 构建发布测试。

#### FairyGUI
> 如果项目使用 FairyGUI 作为 UI 解决方案，需要重载 EventSystem 和 Input，参考本小节步骤接入。
1. 在 Unity 场景内找到 EventSystem，挂载 TTInputOverrideBypass 组件。
  - 如果没有 EventSystem，请先手动创建一个 Empty Object，添加 EventSystem 组件。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/39b53bd6d50f45228ab28597a04061d5~tplv-9nona0m7ha-image.image)

1. 在 Project Settings - Player 中，切换到 WebGL 页签。
  - 找到 Scripting Define Symbols，点加号添加 `STARK_UNITY_INPUT_OVERRIDE` ，并点击 Apply 保存。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/b3ac9856fe884f49bf174150644c570a)

1. 首次触控操作前，手动启用 FairyGUI 的触屏能力。

```js
FairyGUI.Stage.touchScreen = true; // 在首次触控操作前调用，否则 Began 事件会丢失。
```

1. 构建发布测试。

#### 其他说明
对 Event System 的重载启用（且 StarkInputOverrideBypass 上勾选 `DebugTraceEnabled` 时）会输出日志：

```text
StarkInputOverrideBypass enabled.
```

对全局 Input 的重载启用时，会输出日志：

```text
Global Input overridden by StarkSDK.
```

影响范围：

| **使用方式** | **是否受重载影响** | 参考接入方式 |
| --- | --- | --- |
| UGUI | 是 | UGUI |
| `IPointerDownHandler` | 是 | UGUI |
| FairyGUI | `STARK_UNITY_INPUT_OVERRIDE` 存在时影响 | FairyGUI |
| `using UnityEngine;` `Input.GetTouch()` | `STARK_UNITY_INPUT_OVERRIDE` 存在时影响 | FairyGUI |
| `UnityEngine.Input.GetTouch()` | 否 | / |

使用其他 UI 方案时，可根据其监听点击事件的方式，尝试按 UGUI 或 FairyGUI 的步骤配置。如果触控粘连的问题仍存在，可参考“手动监听”小节。

### 手动监听
> 如果上述接入方式无法满足需求，可以考虑手动监听。
> 通过直接监听原始 Touch 事件、获取每个点的 Touch Phase 来定制操控逻辑。
#### 接口参考
这套 API 仅在 WebGL 环境中有效，可以手动监听触控事件。支持的触控事件有 `TouchStart`、`TouchMove`、`TouchEnd`、`TouchCancel`。

```csharp
public abstract class TTInput
{
    /// <summary>
    /// 触控事件回调
    /// </summary>
    public delegate void TouchEventCallback(TTTouchEvent touchEvent);
    
    /// <summary>
    /// 监听开始触摸事件
    /// </summary>
    /// <param name="callback"></param>
    [TTVersion(MinTTContainerAndroidVersion = "9999.9999", WebGLMethod = "startTouchEventsListening")]
    public abstract void OnTouchStart(TouchEventCallback callback);
    
    /// <summary>
    /// 监听触点移动事件
    /// </summary>
    /// <param name="callback"></param>
    [TTVersion(MinTTContainerAndroidVersion = "9999.9999", WebGLMethod = "startTouchEventsListening")]
    public abstract void OnTouchMove(TouchEventCallback callback);
    
    /// <summary>
    /// 监听触摸结束事件
    /// </summary>
    /// <param name="callback"></param>
    [TTVersion(MinTTContainerAndroidVersion = "9999.9999", WebGLMethod = "startTouchEventsListening")]
    public abstract void OnTouchEnd(TouchEventCallback callback);
    
    /// <summary>
    /// 监听触点失效事件
    /// </summary>
    /// <param name="callback"></param>
    [TTVersion(MinTTContainerAndroidVersion = "9999.9999", WebGLMethod = "startTouchEventsListening")]
    public abstract void OnTouchCancel(TouchEventCallback callback);
    
    /// <summary>
    /// 取消监听开始触摸事件
    /// </summary>
    /// <param name="callback"></param>
    [TTVersion(MinTTContainerAndroidVersion = "9999.9999", WebGLMethod = "stopTouchEventsListening")]
    public abstract void OffTouchStart(TouchEventCallback callback = null);
    
    /// <summary>
    /// 取消监听触点移动事件
    /// </summary>
    /// <param name="callback"></param>
    [TTVersion(MinTTContainerAndroidVersion = "9999.9999", WebGLMethod = "stopTouchEventsListening")]
    public abstract void OffTouchMove(TouchEventCallback callback = null);
    
    /// <summary>
    /// 取消监听触摸结束事件
    /// </summary>
    /// <param name="callback"></param>
    [TTVersion(MinTTContainerAndroidVersion = "9999.9999", WebGLMethod = "stopTouchEventsListening")]
    public abstract void OffTouchEnd(TouchEventCallback callback = null);
    
    /// <summary>
    /// 取消监听触点失效事件
    /// </summary>
    /// <param name="callback"></param>
    [TTVersion(MinTTContainerAndroidVersion = "9999.9999", WebGLMethod = "stopTouchEventsListening")]
    public abstract void OffTouchCancel(TouchEventCallback callback = null);
    
}
```

#### 使用示例

```csharp
// 监听 TouchStart 事件
TT.OnTouchStart(evt => {
    Debug.Log($"OnTouchStart {evt}" ); 
});
```

## 实现原理
### 事件监听
- TT上的触控事件监听接口由 JS 基础库单独提供，无事件粘连问题。

### UGUI
- TTInputOverrideBypass 组件启用时，会重载 Event System 中 Input Module 的 Touch 相关行为。
- 该重载不影响 `UnityEngine.Input`。

### FairyGUI
- 定义了 `STARK_UNITY_INPUT_OVERRIDE` 符号的状态下，全局命名空间中会存在一个与 `UnityEngine.Input` 等价且同名的 `Input` 实现。
- 该 `Input` 实现与 StarkInputOverrideBypass 组件配合使用，能够重载 `Input.touches`, `Input.GetTouch()` 等属性和方法。编译时，业务代码中对 `Input` 而非显式指定 `UnityEngine.Input` 的引用，会定向至该 `Input` 实现。
- 该重载仅影响对 `Input` 的直接引用，不影响 `UnityEngine.Input`。
