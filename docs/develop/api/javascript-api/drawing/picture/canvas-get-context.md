---
title: "Canvas.getContext"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/drawing/picture/canvas-get-context
update_time: 2024-09-26
---

## 语法

```js
Canvas.getContext(contextType)
```
基础库 1.31.0 开始支持本方法，这是一个**同步**方法。
获取画布对象的绘图上下文。​

## 示例代码
```js
// 获取2d上下文，绘制一个黑色的矩形
const canvas = tt.createCanvas();
let CanvasRenderingContext2D = canvas.getContext("2d");
CanvasRenderingContext2D.fillStyle = "black";
CanvasRenderingContext2D.fillRect(0, 0, canvas.width, canvas.height);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| contextType | number | 是 |  | 1.31.0 | 上下文类型  **可选值：** 2d=2d 绘图上下文​；webgl=webgl 绘图上下文 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| Context | Object | Canvas 上下文对象  **当参数为 2d 时，返回值 CanvasRenderingContext2D 实现了** [HTML Canvas 2D Context](https://www.w3.org/TR/2dcontext/) **定义的大部分属性、方法，暂不支持的特性如下：**​  \|  \| \| --- \| \| 暂时不支持的特性​ \| \| CanvasRenderingContext2D.clip​ \| \| CanvasRenderingContext2D.lineDashOffset​ \| \| CanvasRenderingContext2D.isPointInPath​ \| \| CanvasRenderingContext2D.isPointInStroke​ \|  **当参数为 webgl 时，返回值 WebGLRenderingContext 实现了** [WebGL 1.0](https://www.khronos.org/registry/webgl/specs/latest/1.0/) **定义的所有属性、方法、常量。** |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/drawing/picture/canvas-get-context) / [本地体验路径](canvas-get-context)
