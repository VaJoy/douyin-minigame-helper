---
title: "tt.offDeviceMotionChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/device-motion/tt-off-device-motion-change
update_time: 2024-08-19
---

## 语法

```js
tt.offDeviceMotionChange(callback)
```
基础库 2.92.0 开始支持本方法，这是一个**同步**方法。
移除设备方向变化事件的监听函数，但不会停止获取设备方向数据。

## 示例代码
```js
//设置两个监听函数
function handler1(res) {
  console.log("设备的偏航角为：", res.alpha);
  console.log("设备的俯仰角为：", res.beta);
  console.log("设备的翻滚角为：", res.gamma);
}
function handler2(res) {
  console.log("设备的偏航角为：", res.alpha);
  console.log("设备的俯仰角为：", res.beta);
  console.log("设备的翻滚角为：", res.gamma);
}

//开始获取数据
tt.startDeviceMotionListening({
  interval: "normal",
  success(res) {
    //开始监听
    tt.onDeviceMotionChange(handler1);
    tt.onDeviceMotionChange(handler2);
  },
});

//一秒之后移除监听函数
setTimeout(() => {
  //移除所有监听函数
  tt.offGyroscopeChange();
  //or
  //移除某个监听函数
  tt.offGyroscopeChange(handler1);
}, 1000);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 2.92.0 | 需要移除的监听函数。若不传此参数，则移除所有监听函数。 |

## 注意事项
若需要停止设备方向数据的获取，可以使用 [tt.stopDeviceMotionListening](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/device-motion/tt-stop-device-motion-listening) 方法。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/tt-off-device-motion-change) / [本地体验路径](tt-off-device-motion-change)
