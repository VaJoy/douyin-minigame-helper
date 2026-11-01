---
title: "tt.stopAccelerometer"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/jerkmeter/tt-stop-accelerometer
update_time: 2024-08-19
---

基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
停止监听加速度数据。

## 示例代码
```js
tt.startAccelerometer({
  success(res) {
    // 调用开始加速度成功 startAccelerometer:ok
    console.log("调用开始加速度成功", res.errMsg);
  },
  fail(res) {
    // 调用开始加速度失败 startAccelerometer:fail
    console.log("调用开始加速度失败", res.errMsg);
  },
});

tt.stopAccelerometer({
  success(res) {
    // 调用停止加速度成功 stopAccelerometer:ok
    console.log("调用停止加速度成功", res.errMsg);
  },
  fail(res) {
    // 调用停止加速度失败 stopAccelerometer:fail
    console.log("调用停止加速度失败", res.errMsg);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："stopAccelerometer:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："stopAccelerometer:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21100 | sensor disable |  |  |
| 21000 | The current device does not support accelerometers |  |  |
| 21000 | The accelerometer is running |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/jerkmeter/tt-stop-accelerometer) / [本地体验路径](tt-stop-accelerometer)
