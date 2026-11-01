---
title: "Cocos/Laya/Egret引擎适配"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/cocos-laya-egret
update_time: 2025-06-09
---

## 概述
抖音小游戏是一个不同于浏览器的 JavaScript 运行环境，没有 BOM 和 DOM API。然而几乎所有基于 HTML5 的游戏引擎都是依赖浏览器提供的 BOM 和 DOM API ，所以如果要在小游戏中使用游戏引擎进行开发，需要关注引擎本身是否对抖音小游戏进行适配。

## 引擎适配
目前 Cocos，Laya，Egret 已完成了引擎对抖音小游戏的适配，可以使用引擎直接导出抖音小游戏产物，具体的开发和发布流程介绍可以参考引擎的官方文档：
- Cocos：https://docs.cocos.com/creator/3.8/manual/zh/editor/publish/publish-bytedance-mini-game.html
- Laya: https://layaair.com/3.2/doc/released/miniGame/byteDance/readme.html
- Egret: [https://www.egret.uk/egretengine2d/发布项目publish/发布到小游戏平台/字节跳动小游戏开发指南/字节跳动开发快速指南/](https://www.egret.uk/egretengine2d/%E5%8F%91%E5%B8%83%E9%A1%B9%E7%9B%AEpublish/%E5%8F%91%E5%B8%83%E5%88%B0%E5%B0%8F%E6%B8%B8%E6%88%8F%E5%B9%B3%E5%8F%B0/%E5%AD%97%E8%8A%82%E8%B7%B3%E5%8A%A8%E5%B0%8F%E6%B8%B8%E6%88%8F%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/%E5%AD%97%E8%8A%82%E8%B7%B3%E5%8A%A8%E5%BC%80%E5%8F%91%E5%BF%AB%E9%80%9F%E6%8C%87%E5%8D%97)

## 适配原理
基于 HTML5 的游戏引擎会依赖浏览器提供的能力实现游戏画面的绘制，游戏音频的播放等功能，而就如概述所说，抖音小游戏的运行环境不同于浏览器，一方面并不提供 BOM 和 DOM API，另一方面额外提供了 FileSystem 这类浏览器不具备的 API。
为了让基于 HTML5 的游戏引擎开发的游戏能够运行在抖音小游戏的环境下，需要在引擎层面进行 BOM 和 DOM API  的抹平，并利用抖音小游戏提供的 FileSystem 进行文件读写等操作，我们称之为 Adapter，可能不同的引擎的 Adapter 实现方案不同，但原理大致相同。

以 HTML5 createElement 为例，创建画布和图片需要使用 DOM API，依赖 document：

```js
var canvas = document.createElement('canvas');
var img = ducument.createElement('img');
```

为了抹平这里的差异，引擎会构造一个 document，使用抖音小游戏提供的 API 来实现对应的功能，比如 tt.createCanvas 和 tt.createImage 等。

```js
// document
var document = {
    // ...
    createElement: function createElement(tagName) {
        if (tagName === 'canvas') {
          return new _Canvas["default"]();
        } else if (tagName === 'audio') {
          return new _Audio["default"]();
        } else if (tagName === 'img') {
          return new _Image["default"]();
        } else if (tagName === 'video') {
          return new _HTMLVideoElement["default"]();
        }
        return new _HTMLElement["default"](tagName);
    },
    // ...
}

// canvas
function Canvas() {
  var canvas = tt.createCanvas();
  canvas.type = 'canvas';
  // ...
  return canvas;
}
```

除 createElement 外，引擎会抹平差异的差异还有很多：
- touch 事件
- 缓存
- 音频
- 图片
- socket
- request
- ......

后续新增的基础能力平台也会和引擎协作使开发者低成本的接入，不过平台提供的[开放能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/overview)（比如广告，支付）还是需要开发者主动通过 tt api 的方式接入。
