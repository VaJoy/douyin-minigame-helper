---
title: "tt.getSystemInfo"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/system-information/tt-get-system-info
update_time: 2024-07-24
---

基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
获取系统信息。

## 示例代码
```js
tt.getSystemInfo({
  success(res) {
    console.log(res);
  },
  fail(res) {
    console.log(`getSystemInfo 调用失败`);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **system**（string）：操作系统版本。示例："11.4", "8.0.0" - **platform**（string）：操作系统类型。可选值："ios"、"android"、"openHarmony"。 - **brand**（string）：手机品牌。示例："Apple", "Xiaomi" - **model**（string）：手机型号 - **version**（string）：宿主 App 版本号（宿主指今日头条、抖音等）。示例："6.7.8" - **appName**（string）：宿主 APP 名称。示例："Toutiao" - **SDKVersion**（string）：客户端基础库版本。示例："1.0.0" - **screenWidth**（number）：屏幕宽度 - **screenHeight**（number）：屏幕高度 - **windowWidth**（number）：可使用窗口宽度 - **windowHeight**（number）：可使用窗口高度 - **safeArea**（Object）：在竖屏正方向下的安全区域。安全区域指的是一个可视窗口范围，处于安全区域的内容不受圆角（corners）、齐刘海（sensor housing）、小黑条（Home Indicator）影响。 - **pixelRatio**（number）：设备像素比 - **deviceScore**（Object）：机型性能评分。分数越高说明设备越好，其中(0, 7.30)为低端机，[7.30, 8.51)为中端机，[8.51, +∞)为高端机。如果获取不到对应分数，返回-1。 - **errMsg**（string）："getSystemInfo:ok" - **deviceOrientation**（string）：设备方向 |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getSystemInfo:fail " + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |

## 注意事项
通过 getSystemInfoSync 和 getSystemInfo 获取到的所有宽高单位均为设备的逻辑分辨率，设备的物理分辨率为逻辑分辨率*设备像素比。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/system/system-information/tt-get-system-info) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-get-system-info%22%7D)
