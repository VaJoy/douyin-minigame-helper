---
title: "tt.vibrateShort"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/shake/tt-vibrate-short
update_time: 2024-07-24
---

基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
使手机发生较短时间的振动。安卓震动时间为 30ms，ios 震动时间为 15ms。

## 示例代码
```js
tt.vibrateShort({
  success(res) {
    console.log(`${res}`);
  },
  fail(res) {
    console.log(`vibrateShort调用失败`);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："vibrateShort:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："vibrateShort:fail " + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21100 | vibrator disable |  |  |
| 20000 | internal error |  |  |

## 使用限制
某些机型在不支持短振动时会 fallback 到 [vibrateLong](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/shake/tt-vibrate-long/)，某些机型不支持时会进入 fail 回调。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/shake/tt-vibrate-short) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-vibrate-short%22%7D)
