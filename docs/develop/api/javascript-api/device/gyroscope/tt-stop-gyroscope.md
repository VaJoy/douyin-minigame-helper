---
title: "tt.stopGyroscope"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/gyroscope/tt-stop-gyroscope
update_time: 2024-08-29
---

基础库 1.72.0 开始支持本方法，这是一个**异步**方法。
停止获取陀螺仪数据，调用该方法后会销毁陀螺仪实例，并会自动调用 tt.offGyroscopeChange 移除陀螺仪监听。

## 示例代码
```js
//设置每隔100ms刷新一次陀螺仪数据
tt.startGyroscope({ interval: 100 });
//停止获取陀螺仪数据
tt.stopGyroscope();
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："stopGyroscope:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："stopGyroscope:fail" + 详细错误信息 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/gyroscope/tt-stop-gyroscope) / [本地体验路径](tt-stop-gyroscope)
