---
title: "tt.getSharedCanvas"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/open-data/tt-get-shared-canvas
update_time: 2025-10-10
---

基础库 1.11.0 开始支持本方法，这是一个**同步**方法。
开放数据域下调用，获取主域和开放数据域共享的 canvas。

## 示例代码
```js
const canvas = tt.getSharedCanvas();
canvas.getContext("2d");
canvas.width = 400;
canvas.height = 200;
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| Canvas | Object | object类型，属性如下：  **对象字段** - **width**（number）：画布的宽度 - **height**（number）：画布的高度 - **getContext**（Function）：获取画布对象的绘图上下文。详情请参考 [Canvas.getContext](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/picture/canvas-get-context) - **toTempFilePath**（Function）：将当前 Canvas 保存为一个临时文件，并生成相应的临时文件路径。详情请参考 [Canvas.toTempFilePath](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/picture/canvas-to-temp-file-path) - **toTempFilePathSync**（Function）：toTempFilePath 方法的同步版本，参数与 toTempFilePath 的参数 相同，返回值为 string 类型的临时文件路径。 - **toDataURL**（Function）：把画布上的绘制内容以一个 string 的格式返回 - **dispose**（Function）：主动释放 canvas 的资源，释放后绑定的 context 将无法使用 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-capacity/relationship-chain/open-data/tt-get-shared-canvas) / [本地体验路径](tt-get-shared-canvas)
