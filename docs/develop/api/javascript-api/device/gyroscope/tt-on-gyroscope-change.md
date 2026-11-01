---
title: "tt.onGyroscopeChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/gyroscope/tt-on-gyroscope-change
update_time: 2024-08-29
---

## 语法

```js
tt.onGyroscopeChange(callback)
```
基础库 1.72.0 开始支持本方法，这是一个**同步**方法。
监听陀螺仪数据变化，数据变化及回调函数被调用的频率取决于启动陀螺仪实例时传入的参数，该方法为同步方法。

## 示例代码
```js
//设置每隔100ms刷新一次陀螺仪数据

tt.startGyroscope({ interval: 100 });

tt.onGyroscopeChange(function (params) {
  console.log("陀螺仪数据:x ", params.x);
  console.log("陀螺仪数据:y ", params.y);
  console.log("陀螺仪数据:z ", params.z);
  console.log("陀螺仪数据:t ", params.t);
  console.log("陀螺仪数据:result ", params.result);
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 1.72.0 | 陀螺仪数据变化事件的回调函数，回调频率由开发者决定。  **对象字段** - **params**（Object）：object类型，属性如下： |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/gyroscope/tt-on-gyroscope-change) / [本地体验路径](tt-on-gyroscope-change)
