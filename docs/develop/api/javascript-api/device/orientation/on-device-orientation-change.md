---
title: "tt.onDeviceOrientationChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/orientation/on-device-orientation-change
update_time: 2025-04-18
---

## 语法

```js
tt.onDeviceOrientationChange(callback)
```
基础库 3.66.0 开始支持本方法，这是一个**同步**方法。
监听屏幕转向切换事件

## 示例代码
```js
tt.onDeviceOrientationChange(() => {
  const systemInfo = tt.getSystemInfoSync();
  console.log(systemInfo.deviceOrientation);
});


tt.setDeviceOrientation({
  value: 'landscape',
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 3.66.0 | 屏幕转向切换事件的监听函数  **对象字段** - **res**（Object）：转屏事件回调参数，类型是 Object |

## 使用限制
以下场景下无法使用该能力：

- 直播场景
- x 分屏场景
- 直玩场景
- pad 场景
- 折叠屏场景

## 前置条件
从基础库版本 3.66.0 开始支持，使用该能力前请做好 [canIUse](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/tt-can-i-use) 判断。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/tt-set-device-orientation) / [本地体验路径](tt-set-device-orientation)
