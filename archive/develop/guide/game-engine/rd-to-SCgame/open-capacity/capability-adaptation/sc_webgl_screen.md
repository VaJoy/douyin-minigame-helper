---
title: "屏幕适配"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_screen
update_time: 2024-07-24
---

> 此文档描述小游戏制作时的屏幕适配问题
> 更多详情见[Unity WebGL 抖音小游戏适配方案](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/sc_webgl_overall)

## 游戏界面
小游戏的屏幕适配与unity游戏适配常见手机屏幕没有区别。常见的适配方式都可以在小游戏中使用。区别的是一些屏幕信息的获取。 如安全区域的获取需调用 `StarkSDK.API.GetSystemInfoSync`得到其中的安全区域。
要注意小游戏右上角默认有退出按钮和胶囊按钮，游戏界面设计时需要避开。
在Unity Editor下通过mock可以显示出胶囊按钮的位置。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/a73772071c1c457bb0a25178971d03f9)

#### 安全区域的获取接口

```csharp
public struct SafeArea
{
    /// <summary>
    /// 安全区域左上角横坐标
    /// </summary>
    public int left;
    
    /// <summary>
    /// 安全区域右下角横坐标
    /// </summary>
    public int right;
    
    /// <summary>
    /// 安全区域左上角纵坐标
    /// </summary>
    public int top;
    
    /// <summary>
    /// 安全区域右下角纵坐标
    /// </summary>
    public int bottom;

    /// <summary>
    /// 安全区域的宽度，单位逻辑像素
    /// </summary>
    public int width;
    
    /// <summary>
    /// 安全区域的高度，单位逻辑像素
    /// </summary>
    public int height;
}

/// <summary>
/// 系统信息
/// </summary>S
public class StarkSystemInfo
{
    ...
    
    /// <summary>
    /// 在竖屏正方向下的安全区域
    /// </summary>
    public SafeArea safeArea;    
}

var systemInfo = StarkSDK.API.GetSystemInfo();
Debug.Log(systemInfo.safeArea);
```
