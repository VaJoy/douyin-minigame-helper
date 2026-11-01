---
title: "tt.offGyroscopeChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/gyroscope/tt-off-gyroscope-change
update_time: 2024-08-29
---

## 语法

```js
tt.offGyroscopeChange(callback)
```
基础库 1.72.0 开始支持本方法，这是一个**同步**方法。
移除陀螺仪监听，但不会停止获取陀螺仪数据。

## 示例代码
```js
//设置每隔 100ms 刷新一次陀螺仪数据

tt.startGyroscope({ interval: 100 });

function handler(param) {
  console.log("陀螺仪数据:x ", param.x);
  console.log("陀螺仪数据:y ", param.y);
  console.log("陀螺仪数据:z ", param.z);
  console.log("陀螺仪数据:t ", param.t);
  console.log("陀螺仪数据:result ", param.result);
}

tt.onGyroscopeChange(handler);

setTimeout(() => {
  // 一秒之后卸载监听函数
  tt.offGyroscopeChange();
}, 1000);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 1.72.0 | 取消监听的回调函数，不传时取消所有监听事件 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/gyroscope/tt-off-gyroscope-change) / [本地体验路径](tt-off-gyroscope-change)
