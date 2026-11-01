---
title: "tt.startAccelerometer"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/jerkmeter/tt-start-accelerometer
update_time: 2024-08-19
---

基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
开始监听加速度数据。具体加速度数据通过注册 tt.onAccelerometerChange 的回调方法来获取。

## 示例代码
开始监听加速度数据
```js
tt.startAccelerometer({
  success(res) {
    console.log("调用成功", res.errMsg);
  },
  fail(res) {
    console.log("调用失败", res.errMsg);
  }
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "startAccelerometer:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "startAccelerometer:fail" + 详细错误信息 |

## 回调：完成回调
调用完成时的回调函数

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21100 | sensor disable |  | 1.0.0 |
| 21000 | The current device does not support accelerometers |  | 1.0.0 |
| 21000 | The accelerometer is running |  | 1.0.0 |
| 20001 | invalid param |  | 1.0.0 |
| 20000 | internal error |  | 1.0.0 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/tt-start-accelerometer) / [本地体验路径](tt-start-accelerometer)
