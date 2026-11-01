---
title: "tt.createCanvas"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/drawing/picture/tt-create-canvas
update_time: 2024-09-26
---

基础库 1.31.0 开始支持本方法，这是一个**同步**方法。
创建一个画布对象。首次调用创建的是显示在屏幕上的画布，之后调用创建的都是离屏画布。

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| Canvas | Object | object类型，属性如下：  **对象字段** - **dispose**（Function）：主动释放 canvas 的资源，释放后绑定的 context 将无法使用 - **toTempFilePath**（Function）：[Canvas.toTempFilePath](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/picture/canvas-to-temp-file-path)。将当前 Canvas 保存为一个临时文件，并生成相应的临时文件路径，​配置开启[开放数据域](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/relationship-chain/open-data-base)后，主域所有 canvas 不能调用该接口 - **toTempFilePathSync**（Function）：toTempFilePath 方法的同步版本，参数与 toTempFilePath 的参数 相同，返回值为 string 类型的临时文件路径，配置开启[开放数据域](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/relationship-chain/open-data-base)后，主域所有 canvas 不能调用该接口 - **width**（number）：画布的宽度 - **height**（number）：画布的高度 - **getContext**（Function）：[Canvas.getContext](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/picture/canvas-get-context)。获取画布对象的绘图上下文​ - **toDataURL**（Function）：把画布上的绘制内容以一个 string 的格式返回，配置开启[开放数据域](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/relationship-chain/open-data-base)后，主域所有 canvas 不能调用该接口 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 注意事项
如果上屏 Canvas 出现绘制模糊，则需要对上屏 Canvas 进行缩放。举例如下：假如tt.getSystemInfo中返回的screenWidth为360，screenHeight为 640，pixelRatio为 2，你需要主动设置canvas.width = screenWidth * pixelRatio; canvas.height = screenHeight * pixelRatio;才能获得清晰的渲染效果。但这样设置会对渲染速度和内存占用有一些影响。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/drawing/picture/tt-create-canvas) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-create-canvas%22%7D) / [在线试玩](https://developer.open-douyin.com/docs/playground?project_id=tma-demo&version=1.0.0.10&entry=tt-create-canvas&codes_select=js&type=mini-game&sdk_version=1.0.0.205)
