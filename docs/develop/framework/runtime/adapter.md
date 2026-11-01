---
title: "Adapter"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/runtime/adapter
update_time: 2026-06-29
---

小游戏的运行环境不同于 Web 环境，在真机上运行时，没有 BOM、DOM API，因此也就没有 window 对象以及其上面的各种属性。所以，从 H5 迁移过来的游戏，开发者需要自己实现 window 对象的兼容(如果是利用游戏引擎开发的小游戏，导出的小游戏版本一般已经包含了一份 adapter，适配了 window 对象)。
官方也提供一份简易的适配器实现 tt-adapter，基于小游戏 JSAPI 实现了部分 H5 能力，用于抹平 H5 能力和小游戏实现上的差异。开发者可在游戏项目内引入该文件，以开发H5游戏的方式进行小游戏开发。

## 下载地址
[tt-adapter.zip](https://lf-douyin-open-2c-cdn.open-douyin.com/obj/douyin-open-2c/developer/minigame/tt-adapter.CaJ89wht.zip)

## 使用示例
1. 在`game.js`中引入文件`tt-adapter.js`
1. 上屏画布 canvas 已创建并挂载到全局变量 window 上，无需重新创建，直接引用即可。若再次调用`document.createElement('canvas')`或`tt.createCanvas()`，将创建离屏画布。

```js
const ctx = window.canvas.getContext('2d')

ctx.fillStyle = '#ffffff';
ctx.fillRect(0, 0, 100, 100);
```

1. 根据需要调用其他的支持的 H5 能力

```js
const audio = new Audio();   // 音频能力

const image = new Image();  // 图片能力

localStorage.setStorage();  // 本地存储
```

## 能力清单
需要说明的是，当前该适配器提供的模拟属性和方法仍然比较简陋，如在游戏内引入请自行保障游戏运行正常，开发者也可以自行扩展，以适配项目内使用的游戏能力。
目前 tt-adapter 对开源的 [three.js](https://threejs.org/) 和 [phaser.js](https://phaser.io/) 等游戏引擎提供了最小能力适配，demo 可参考：
- [three.js 五子棋](https://developer.open-douyin.com/ide/minicode/52bad7ad3ae52c806035c25ba67ae380)
- [phaser.js 消除小球](https://developer.open-douyin.com/ide/minicode/f07503912bd1159c09d329e3760664cd)

Web API的部分支持情况罗列如下：
> ✅ 仅表示支持该API的核心功能，不代表完全对齐实现Web标准的属性、方法或参数

| H5 | tt-adapter |
| --- | --- |
| canvas | ✅ |
| document | ✅ |
| base64 | ✅ |
| Audio | ✅ |
| AudioContext | ✅ |
| Blob | ❌ |
| FileReader | ❌ |
| Element | ✅ |
| Node | ✅ |
| Event | ✅ |
| EventTarget | ✅ |
| Image | ✅ |
| ImageBitMap | ✅ |
| localStorage | ✅ |
| location | ✅ |
| matchMedia | ✅ |
| navigator | ✅ |
| performance | ✅ |
| TextDecoder | ✅ |
| TextEncoder | ❌ |
| URL | ❌ |
| window | ✅ |
| Worker | ✅ |
| WebSocket | ✅ |
| XMLHttpRequest | ✅ |
| fetch | ❌ |
| touchEvent | ✅ |
| pointerEvent | ✅ |
| mouseEvent | ❌ |

若对此能力有任何疑问，或需进一步支持，请发起工单反馈。

GameGlobal.GameGlobal === GameGlobal;

setTimeout === GameGlobal.setTimeout; // true
requestAnimationFrame === GameGlobal.requestAnimationFrame; // true
