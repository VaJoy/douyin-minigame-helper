---
title: "tt.getScreenBrightness"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/screen-intensity/tt-get-screen-brightness
update_time: 2024-08-29
---

基础库 1.79.0 开始支持本方法，这是一个**异步**方法。
获取屏幕亮度。

## 示例代码
```js
tt.getScreenBrightness({
  success: (res) => {
    console.log("getScreenBrightness success", res);
  },
  fail: (res) => {
    console.log("getScreenBrightness fail", res);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **value**（number）：屏幕亮度值，范围 0 ～ 1。（0 最暗，1 最亮） - **errMsg**（string）："getScreenBrightness:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getScreenBrightness:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10401 | Failed to get screen brightness. |  |  |
| 20000 | internal error |  |  |

## 注意事项
在没有设置小游戏屏幕亮度的情况下，默认获取系统屏幕亮度

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/screen-intensity/tt-get-screen-brightness) / [本地体验路径](tt-get-screen-brightness)
