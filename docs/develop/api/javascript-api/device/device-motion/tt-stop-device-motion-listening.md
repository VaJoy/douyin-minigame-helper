---
title: "tt.stopDeviceMotionListening"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/device-motion/tt-stop-device-motion-listening
update_time: 2024-08-19
---

基础库 2.92.0 开始支持本方法，这是一个**异步**方法。
销毁设备方向监听实例，停止监听设备方向的变化。

## 示例代码
```js
tt.startDeviceMotionListening({
  interval: "normal",
});

tt.stopDeviceMotionListening({
  success(res) {
    console.log("stopDeviceMotionListening success");
  },
  fail(res) {
    console.log("stopDeviceMotionListening fail");
  },
  complete(res) {
    console.log("stopDeviceMotionListening complete");
  },
});
//or
tt.stopDeviceMotionListening();
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："stopDeviceMotionListening:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："stopDeviceMotionListening:fail" + 详细错误信息 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/tt-stop-device-motion-listening) / [本地体验路径](tt-stop-device-motion-listening)
