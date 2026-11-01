---
title: "requestAnimationFrame"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/drawing/frame-rate/request-animation-frame
update_time: 2024-08-21
---

## 语法

```js
requestAnimationFrame(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
该方法需要传入一个回调函数作为参数，该回调函数会在下一次重绘之前执行。

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.0.0 | 浏览器会在下一次重绘之前执行该函数 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| requestId | number | 调用 requestAnimationFrame 方法添加到计划中的动画帧请求 id |

## 注意事项
- 若想在下次重绘之前继续更新下一帧动画，那么回调函数自身必须再次调用 requestAnimationFrame。
- 作为全局属性在全局直接调用即可

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/api/drawing/frame-rate/request-animation-frame) / [本地体验路径](request-animation-frame) / [在线试玩](https://developer.open-douyin.com/docs/playground?project_id=tma-demo&version=1.0.0.10&entry=request-animation-frame&codes_select=js&type=mini-game&sdk_version=1.0.0.205)
