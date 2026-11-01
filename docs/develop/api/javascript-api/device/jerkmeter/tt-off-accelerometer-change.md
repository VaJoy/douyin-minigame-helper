---
title: "tt.offAccelerometerChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/jerkmeter/tt-off-accelerometer-change
update_time: 2024-08-12
---

## 语法

```js
tt.offAccelerometerChange(callback)
```
基础库 1.94.0 开始支持本方法，这是一个**同步**方法。
解绑加速度数据监听器。

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

const callback = (res) => {
  console.log(`x轴数据：${res.x}`);
  console.log(`y轴数据：${res.y}`);
  console.log(`z轴数据：${res.z}`);
};

tt.onAccelerometerChange(callback);
tt.offAccelerometerChange(callback);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 1.94.0 | 加速度数据的事件回调 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |

## 注意事项
不传入callback参数时，会移除所有监听函数

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
