---
title: "tt.startGyroscope"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/gyroscope/tt-start-gyroscope
update_time: 2024-08-29
---

## 语法

```js
tt.startGyroscope(interval)
```
基础库 1.73.0 开始支持本方法，这是一个**异步**方法。
创建陀螺仪实例，准备获取陀螺仪数据

## 示例代码
```js
//设置每隔100ms刷新一次陀螺仪数据
tt.startGyroscope({
  interval: 100,
  fail(res) {
    console.warn(res); //失败时候进入这里
  },
});

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
| interval | number | 是 | 50 | 1.73.0 | 获取陀螺仪数据的间隔时间，单位为毫秒（ms），默认大小为 50。 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："startGyroscope:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："startGyroscope:fail" + 详细错误信息 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/gyroscope/tt-start-gyroscope) / [本地体验路径](tt-start-gyroscope)
