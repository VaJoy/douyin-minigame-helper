---
title: "tt.onAccelerometerChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/jerkmeter/tt-on-accelerometer-change
update_time: 2024-08-19
---

## 语法

```js
tt.onAccelerometerChange(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
监听加速度数据。回调的频率为 5 次 / 秒，暂不支持设置。接口调用后会开始监听，可通过 [tt.onStopAccelerometer](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/jerkmeter/tt-stop-accelerometer/) 停止监听。

## 示例代码
```js
tt.onAccelerometerChange((res) => {
    console.log(`x轴数据：${res.x}`);
    console.log(`y轴数据：${res.y}`);
    console.log(`z轴数据：${res.z}`);
});


tt.startAccelerometer({
    success(res) {
        // 调用开始加速度成功 startAccelerometer:ok
        console.log('调用开始加速度成功', res.errMsg);
    },
    fail(res) {
        // 调用开始加速度失败 startAccelerometer:fail
        console.log('调用开始加速度失败', res.errMsg);
    },
});

tt.stopAccelerometer({
    success(res) {
        // 调用停止加速度成功 stopAccelerometer:ok
        console.log('调用停止加速度成功', res.errMsg);
    },
    fail(res) {
        // 调用停止加速度失败 stopAccelerometer:fail
        console.log('调用停止加速度失败', res.errMsg);
    },
});
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.0.0 | 加速度数据的事件回调  **对象字段** - **args_0**（Object）：参数为 Object 类型，属性如下： |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21000 | The current device does not support accelerometers |  |  |
| 21000 | The accelerometer is running |  |  |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |

## 注意事项
如果在调用该方法之前没有调用 [tt.onStartAccelerometer](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/jerkmeter/tt-start-accelerometer/)， 该方法会默认调用一次 [tt.onStartAccelerometer](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/jerkmeter/tt-start-accelerometer/) 方法。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/jerkmeter/tt-on-accelerometer-change) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-on-accelerometer-change%22%7D)
