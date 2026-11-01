---
title: "tt.startDeviceMotionListening"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/device-motion/tt-start-device-motion-listening
update_time: 2024-08-19
---

## 语法

```js
tt.startDeviceMotionListening(interval)
```
基础库 2.92.0 开始支持本方法，这是一个**异步**方法。
创建设备方向监听实例，开始监听设备方向的变化。

## 示例代码
```js
tt.startDeviceMotionListening({
  interval: "normal",
  success(res) {
    console.log("startDeviceMotionListening success");
    tt.onDeviceMotionChange((res) => {
      console.log("设备的偏航角为：", res.alpha);
      console.log("设备的俯仰角为：", res.beta);
      console.log("设备的翻滚角为：", res.gamma);
    });
  },
  fail(res) {
    console.log("startDeviceMotionListening fail");
  },
  complete(res) {
    console.log("startDeviceMotionListening complete");
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| interval | number | 是 |  | 2.92.0 | 监听设备方向的变化回调函数的执行频率，单位为ms/次  **可选值：** normal=普通的回调频率：约200ms/次；game=适用于更新UI的回调频率：约60ms/次；ui=适用于更新游戏的回调频率：约20ms/次 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："startDeviceMotionListening:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："startDeviceMotionListening:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | expect params.interval to be one of "normal", "ui", "game", but got xxx |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/tt-start-device-motion-listening) / [本地体验路径](tt-start-device-motion-listening)
