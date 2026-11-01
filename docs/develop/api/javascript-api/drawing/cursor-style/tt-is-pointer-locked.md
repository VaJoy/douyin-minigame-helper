---
title: "tt.isPointerLocked"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/drawing/cursor-style/tt-is-pointer-locked
update_time: 2025-01-03
---

基础库 3.54.0 开始支持本方法，这是一个**同步**方法。
检查鼠标指针是否被锁定，仅适用于 PC 平台

## 示例代码
```js
const isLocked = tt.isPointerLocked();
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| isLocked | boolean | 光标是否被锁定 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
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
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/cursor) / [本地体验路径](tt-cursor)
