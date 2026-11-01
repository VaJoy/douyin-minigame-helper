---
title: "Canvas.toTempFilePath"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/drawing/picture/canvas-to-temp-file-path
update_time: 2024-09-26
---

## 语法

```js
Canvas.toTempFilePath(x, y, width, height, destWidth, destHeight, fileType, quality)
```
基础库 1.31.0 开始支持本方法，这是一个**异步**方法。
将当前 Canvas 保存为一个临时文件，并生成相应的临时文件路径。​

## 示例代码
```js
const canvas = tt.createCanvas();
canvas.getContext("2d");

// oTempFilePath 方法
canvas.toTempFilePath({
  x: 20,
  y: 20,
  width: 200,
  height: 150,
  destWidth: 400,
  destHeight: 300,
  success: (res) => {
    console.log(res.tempFilePath);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| x | number | 否 | 0 | 1.31.0 | 截取 canvas 的左上角横坐标​ |
| y | number | 否 | 0 | 1.31.0 | 截取 canvas 的左上角纵坐标​ |
| width | number | 否 |  | 1.31.0 | 截取 canvas 的宽度​。**默认取 canvas 的宽度** |
| height | number | 否 |  | 1.31.0 | 截取 canvas 的高度​。**默认取 canvas 的高度** |
| destWidth | number | 否 |  | 1.31.0 | 目标文件的宽度，会将截取的部分拉伸或压缩至该数值​。**默认取 canvas 的宽度** |
| destHeight | number | 否 |  | 1.31.0 | 目标文件的高度，会将截取的部分拉伸或压缩至该数值​。**默认取 canvas 的高度** |
| fileType | number | 否 | png | 1.31.0 | 目标文件的类型  **可选值：** jpg=jpg 文件；png=png 文件 |
| quality | number | 否 | 1.0 | 1.31.0 | jpg 图片的质量，仅当 fileType 为 jpg 时有效。取值范围为 0.0（最低）- 1.0（最高），不含 0。不在范围内时当作 1.0​ |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 状态信息 |
| toTempFilePath | string | canvas 生成的临时文件路径 |

## 回调：失败回调
调用失败时的回调函数

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | @The base64Data cannot be null |  |  |
| 21101 | @tmpFilePath is nil, destAbsPath: %@ |  |  |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |
| 21101 | save temp file fail |  |  |
| 21102 | decode image fail |  |  |
| 21103 | base64 data error |  |  |
| 10401 | cause: $cause, errMsg: $extraMsg |  |  |
| 10403 | internal error |  |  |

## 注意事项
不要在 tt.createCanvas 后立即调用该方法，在 Canvas 创建后的初始状态下调用该方法可能会导致异常。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/drawing/picture/canvas-to-temp-file-path) / [本地体验路径](canvas-to-temp-file-path)
