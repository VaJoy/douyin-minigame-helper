---
title: "获取系统信息"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/system/get-system-info
update_time: 2025-05-26
---

> 注意事项：
> 该接口类似 [tt.getSystemInfoSync 接口](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/system/system-information/tt-get-system-info-sync) 返回值 。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

## TT.GetSystemInfo
> 6.0.0 开始支持本方法
获取系统信息。
### **语法 **

```csharp
public static TTSystemInfo GetSystemInfo();
```

### 代码示例

```csharp
void PrintSystemInfo()
{
    if (CanIUse.GetSystemInfo)
    {
        var systemInfo = TT.GetSystemInfo();
        Debug.Log(JsonUtility.ToJson(systemInfo));
    }
    else
    {
        Debug.Log("接口不兼容");
    }
}
```

## TTSystemInfo
### 属性说明

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| hostName | string | 当前宿主名，如 Douyin |
| hostVersion | string | 当前宿主版本号，如 19.2.0 |
| ttVersion | string | TTContainer 底层框架版本号 |
| brand | string | 手机设备制造商，如 Apple、samsung |
| model | string | 手机品牌，如 iPhone 12、SM-G9880 |
| platform | string | 操作系统，如 ios、android |
| system | string | 系统版本，如 iOS 15.1.1、Android 11 |
| language | string | 系统语言，如 zh_CN |
| sdkVersion | string | 客户端基础库版本 |
| pixelRatio | double | 设备像素比 |
| screenHeight | int | 屏幕高度，单位逻辑像素 |
| screenWidth | int | 屏幕宽度，单位逻辑像素 |
| statusBarHeight | int | 状态栏的高度 |
| safeArea | SafeArea | 在竖屏正方向下的安全区域 |
| deviceScore | DeviceScore | 表示机型性能评分分数越高说明设备越好，其中(0, 7.30)为低端机，[7.30, 8.51)为中端机，[8.51, +∞)为高端机。如果获取不到对应分数，返回-1。 |
| deviceOrientation | TTDeviceOrientation | 屏幕方向 |

## SafeArea
在竖屏正方向下的安全区域。
### 属性说明

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| left | int | 安全区域左上角横坐标 |
| right | int | 安全区域右下角横坐标 |
| top | int | 安全区域左上角纵坐标 |
| bottom | int | 安全区域右下角纵坐标 |
| width | int | 安全区域的宽度，单位逻辑像素 |
| height | int | 安全区域的高度，单位逻辑像素 |

## DeviceScore
表示机型性能评分
### 属性说明

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| cpu | double | cpu的评分 |
| gpu | double | gpu的评分 |
| memory | double | 内存的评分 |
| overall | double | 全面评分 |

## TTDeviceOrientation
屏幕方向。
该类型是枚举类型。
### 说明

| 枚举名称 | 说明 |
| --- | --- |
| Portrait | 竖屏 |
| Landscape | 横屏 |
