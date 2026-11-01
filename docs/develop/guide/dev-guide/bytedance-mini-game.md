---
title: "开发指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/dev-guide/bytedance-mini-game
update_time: 2025-06-09
---

抖音小游戏是一种开放能力，允许开发者基于给定 API 编写游戏代码，生成可在接入小游戏功能的各产品 App 上运行的程序。
## 快速上手
### 安装开发工具
前往[开发者工具下载页面](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/developer-instrument-update-and-download)，根据自己的操作系统下载对应的安装包进行安装。
### 小游戏文件结构

```js
.
├── game.js               =>  小游戏入口文件
├── game.json             =>  小游戏配置文件
└── project.config.json   =>  工程配置文件
```

以上三个文件为小游戏的三个必要文件，开发者如有其它资源可以在根目录下自由建立 `js`, `audio`, `images` 等目录，规范自己的开发文件。
### 配置
小游戏包含两个配置文件：小游戏配置文件`game.json`和工程配置文件`project.config.json`。
#### 小游戏配置文件`game.json`
`game.json` 示例如下，详细说明可见[小游戏配置](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/mini-game-configuration)。

```json
{
  "deviceOrientation": "portrait"
}
```

#### 工程配置文件`project.config.json`
`project.config.json` 示例：

```json
{
  "description": "项目描述",
  "setting": {
    "es6": true // 声明使用的 js 语法版本
  }
}
```

## 平台能力
### tt API
本平台只能使用 JavaScript 来编写小游戏。小游戏的运行环境是一个绑定了一些方法的 JavaScript VM。不同于浏览器，这个运行环境没有 `BOM` 和 `DOM` API，只有 `tt`系列 API。接下来我们将介绍如何用 `tt` API 来完成创建画布、绘制图形、显示图片以及响应用户交互等基础功能。
### 创建 Canvas

```js
var canvas = tt.createCanvas();
```

通过调用 tt.createCanvas() 接口，可以创建一个 Canvas 对象。用户第一次调用时， 获取到的是一个上屏 Canvas，该 Canvas 已经显示在了屏幕上，且与屏幕等宽等高。小游戏运行期间，有且仅有一个上屏 Canvas。
### 绘制

```js
var context = canvas.getContext("2d");
context.fillStyle = "#ff00ff";
context.fillRect(0, 0, 100, 100);
```

### 触摸事件
平台提供了一系列监听触摸事件的 API：
- [tt.onTouchStart()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/click-event/tt-on-touch-start)
- [tt.onTouchMove()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/click-event/tt-on-touch-move)
- [tt.onTouchEnd()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/click-event/tt-on-touch-end)
- [tt.onTouchCancel()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/click-event/tt-on-touch-cancel)
### 动画能力
开发者可以利用定时器相关 API 实现动画效果，如下：
- [setTimeout](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/timer/set-timeout)
- [setInterval](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/timer/set-interval)
- [requestAnimationFrame](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/frame-rate/request-animation-frame)
- [clearTimeout](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/timer/clear-timeout)
- [clearInterval](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/timer/clear-interval)
- [cancelAnimationFrame](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/frame-rate/cancel-animation-frame)
### 全局对象
小游戏的运行环境不同于 Web 环境，在真机上运行时，没有`BOM` API，因此也就没有 window 对象以及其上面的各种属性。所以，从 H5 迁移过来的游戏，开发者需要自己实现 window 对象的兼容(如果是利用游戏引擎开发的小游戏，导出的小游戏版本一般已经包含了一份 adapter，适配了 window 对象)。同时，在小游戏的运行环境中，提供了全局对象 GameGlobal，所有全局定义的变量都是 GameGlobal 的属性。如：

```js
setTimeout === GameGlobal.setTimeout; // true
requestAnimationFrame === GameGlobal.requestAnimationFrame; // true
```

同时，GameGlobal 是一个全局对象，也是一个循环引用的对象。

```js
GameGlobal.GameGlobal === GameGlobal;
```

## 无网兼容
平台支持缓存小游戏后在无网条件下再打开，建议游戏逻辑也根据网络条件做好兼容，保障玩家在无网/弱网条件下的游戏体验。
## 关系链数据使用
请参考文档[开放数据域的基础能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data-base)。
## 开放能力
平台允许开发者利用产品宿主提供的如登录、分享及即将支持的支付、广告等开放能力，用以完善产品逻辑和体验。具体可参考开发 > 指南 > 开放能力一栏。
## 代码包限制
在 **IDE 1.1.0** 及以上版本，小游戏包体积限制分为两种情况，普通非分包小游戏和分包小游戏。
### 普通小游戏包
未配置分包的场景下，每个小游戏允许上传的代码包总大小上限为 **20MB**。
### 分包后小游戏包
对于配置了分包的小游戏，默认限制为：
- **小游戏整体包（小游戏包整个目录）大小不超过 20MB；**
- **单个主包不超过 4MB；**
- **单个分包大小不超过 20MB。**
**开放数据域**
开放数据域文件类似子包概念，该文件 / 目录的大小不超过 4MB。
### 说明
分包的应用场景在于减少小游戏加载耗时，以及提供额外的扩展包大小。普通小游戏包的压缩后大小依赖于开发者的资源，不可控。
IDE 的包大小计算不会包含：unix dot 隐藏文件及目录、node_modules 文件、js.map 文件。超过大小上限的小游戏包，预览上传将受限，请开发者注意小游戏包体积。
**文件类型**
小游戏限制了可以上传的文件类型。只能上传以下列表中的文件：

|  | 类型 |
| --- | --- |
| 文件后缀类型 | .png, .jpg, .jpeg, .gif, .svg, .json, .cer, .mp3, .aac, .m4a, .mp4, .wav, .flac, .ape, .ogg, .wma, .midi, .ogv, .webm, .mkv, .ttc, .ttf, .woff, .otf, .obj, .dae, .fbx, .mtl, .stl, .3ds, .pvr, .plist, .fnt, .gz, .ccz, .bmp, .atlas, .swf, .ani, .part, .proto, .bin, .sk, .mipmaps, .txt, .zip, .tt, .map, .silk, .dbbin, .dbmv, .etc, .lmat, .lm, .ls, .lh, .lani, .lav, .lsani, .ltc, .xml, .pkm, .scene, .csv, .prefab, .mesh, .astc, .wasm, .br, .heic, .ico, .cur, .wasm.br, .dat, .dds, .glb, .gltf, .ktx, .lmani, .lml, .skel |
