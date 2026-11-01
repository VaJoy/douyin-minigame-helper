---
title: "tt.setDeviceOrientation"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/orientation/tt-set-device-orientation
update_time: 2025-04-18
---

## 语法

```js
tt.setDeviceOrientation(value)
```
基础库 3.66.0 开始支持本方法，这是一个**异步**方法。
切换横竖屏，接口调用成功后会触发 tt.onDeviceOrientationChange 事件。

## 示例代码
```js
tt.setDeviceOrientation({
  value: 'landscape',
  success() {
    console.log('转屏成功')
  },
  fail() {
    console.log('转屏失败')
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| value | number | 是 |  | 3.66.0 | 表示切换为横屏还是竖屏，string 类型  **可选值：** landscape=

横屏

；portrait=

竖屏

 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | setDeviceOrientation: ok |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "setDeviceOrientation:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10401 | internal error |  |  |
| 21100 | setDeviceOrientation: can't set device orientation in live |  |  |
| 21101 | setDeviceOrientation: can't set device orientation in x screen |  |  |
| 21102 | setDeviceOrientation: can't set device orientation in direct play |  |  |
| 21103 | setDeviceOrientation: can't set device orientation in current device model |  |  |

## 使用限制
以下场景下无法使用该能力：

- 直播场景
- x 分屏场景
- 直玩场景
- pad 场景
- 折叠屏场景

## 注意事项
1. 该接口为异步接口，success 回调后才是转屏完成的准确时机。
2. 转屏完成后宽高会发生变更，需要通过 [tt.getSystemInfoSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/system-information/tt-get-system-info-sync) 获取转屏后的宽高重新渲染游戏画面，避免转屏后画面拉伸异常。

## 前置条件
从基础库版本 3.66.0 开始支持，使用该能力前请做好 [canIUse](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/tt-can-i-use) 判断。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/tt-set-device-orientation) / [本地体验路径](tt-set-device-orientation)