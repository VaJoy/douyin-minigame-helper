---
title: "tt.offWheel"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/wheel/tt-off-wheel
update_time: 2025-01-03
---

## 语法

```js
tt.offWheel(handler)
```
基础库 3.54.0 开始支持本方法，这是一个**同步**方法。
取消监听鼠标滚轮事件

## 示例代码
```js
// 解除所有 Wheel 监听
tt.offWheel();

// 解除特定 Wheel 监听
const callback = () => console.log('Wheel');
tt.onWheel(callback);
tt.offWheel(callback);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| handler | Function | 否 |  | 3.54.0 | 可选传入，传入特定监听的回调函数可以解除特定 wheel 事件监听，不传则解除所有 wheel 事件监听 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 999999 | invalid param |  |  |
| 999988 | The feature is not available in current operating system |  |  |

## 使用限制
只支持 PC 端使用该能力

## 相关课程
[PC 端小游戏接入指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/tutorial)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/wheel) / [本地体验路径](tt-wheel)
