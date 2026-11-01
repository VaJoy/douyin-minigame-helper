---
title: "开放数据域基础能力"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/open-data-base
update_time: 2024-08-07
---

## 开放数据域
为了让开发者安全使用平台的关系数据，我们提供了一个名为开放数据域的环境。这是一个封闭、独立的 JavaScript 作用域。模块的功能结构如下图：

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1664283444530)

通过在 game.json 中添加配置项 openDataContext 指定开放数据域的代码目录，来开启该项功能，以便使用对应的关系链数据接口，同时，在使用这一功能时，也会有一些限制。
对应的代码目录应该如下：

```text
├── src
|   └── myOpenDataContext
|       ├── index.js
|       └── ...
├── game.js
├── game.json
└── ...
```

index.js 作为开放数据域的入口文件是必需的，平台构建工具会将开放数据目录下的文件自动打包为一个独立文件，其代码运行在开放数据域。而 game.js 其代码运行在主域。
具体参考下图：

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1664281820987)

注意，主域和开放数据域中的代码不能相互 require。
## 主域和开放数据域的通信
开放数据域不能向主域发送消息。
主域可以向开放数据域发送消息。调用 tt.getOpenDataContext() 方法可以获取开放数据域实例，调用实例上的 OpenDataContext.postMessage() 方法可以向开放数据域发送消息。

```js
// game.js
const openDataContext = tt.getOpenDataContext();
openDataContext.postMessage({
  text: "This is a test.",
});
```

在开放数据域中通过 tt.onMessage() 方法可以监听从主域发来的消息。

```js
// src/myOpenDataContext/index.js
tt.onMessage((data) => {
  console.log(data);
  /* {
    text: 'This is a test.',
  } */
});
```

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1664283322294)

## 如何使用关系链数据
通过关系链 API 获取到的用户数据，在绘制排行榜等业务场景下如果想要展示，需要将排行榜绘制到 sharedCanvas 上，再在主域将 sharedCanvas 渲染上屏。可参考以下示例代码：
1. **sharedCanvas** 是主域和开放数据域都可以访问的一个离屏画布。在开放数据域调用** **[tt.getSharedCanvas()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data/tt-get-shared-canvas)** **将返回 **sharedCanvas**。根据业务逻辑获取关系链数据，然后绘制到 **sharedCanvas** 上。

```js
// src/myOpenDataContext/index.js
const sharedCanvas = tt.getSharedCanvas();
const context = sharedCanvas.getContext("2d");

function drawRankList(data) {
  data.forEach((item, index) => {
    // ...
    context.fillStyle = "red";
    context.fillRect(0, 0, 100, 100);
  });
}

tt.getCloudStorageByRelation({
  success: (res) => {
    const data = res.data;
    drawRankList(data);
  },
});
```

1. 在主域中可以通过开放数据域实例访问 sharedCanvas，通过 drawImage() 方法可以将 sharedCanvas 绘制到上屏画布。

```js
// game.js
const openDataContext = tt.getOpenDataContext();
const sharedCanvas = openDataContext.canvas;

const canvas = tt.createCanvas();
const context = canvas.getContext("2d");
context.drawImage(sharedCanvas, 0, 0);
```

sharedCanvas 的宽高只能在主域设置，不能在开放数据域中设置。本质上其也是一个离屏 Canvas，而重设 Canvas 的宽高会清空 Canvas 上的内容。所以可以通过 postMessage 通知开放数据域去重绘 sharedCanvas 。

```js
// game.js
sharedCanvas.width = 400;
sharedCanvas.height = 200;

openDataContext.postMessage({
  command: "render",
});
```

```js
// src/myOpenDataContext/index.js
tt.onMessage((data) => {
  if (data.command === "render") {
    // ... 重绘 sharedCanvas
  }
});
```

## 运行时限制
### 主域
1. sharedCanvas 只能被绘制到上屏 canvas 上。
1. 上屏 canvas 不能调用 toDataURL，其 context 不能调用 getImageData、readPixels。
1. sharedCanvas 不能调用 toDataURL 和 getContext。
1. 不能将上屏 canvas 和 sharedCanvas 以任意形式绘制到其他 canvas 上，包括 drawImage、createPattern、texImage2D、texSubImage2D。
1. sharedCanvas 的宽高只能在主域设置。
1. 配置开启开放数据域后，主域所有 canvas 不能调用 toDataURL、toTempFilePath、toTempFilePathSync
### 开放数据域
1. 不能设置 sharedCanvas 的宽高。
1. 开放数据域的 Image 只能使用本地或者是通过 `tt.xx` 系列 API 拿到的平台本身的用户头像图片，不能使用开发者自己服务器上的图片。对于非本地或非用户头像图片，可以先从主域 tt.downloadFile() 下载图片文件，再通过 openDataContext.postMessage() 把文件路径传给开放数据域去使用。
1. 配置开启开放数据域后，主域所有 canvas 不能调用 toDataURL、toTempFilePath、toTempFilePathSync
### 开放数据域 API
只能调用有限的 API，如下所示：
#### 帧率
- [requestAnimationFrame()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/frame-rate/request-animation-frame)
- [cancelAnimationFrame()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/frame-rate/cancel-animation-frame)
#### Timer
- [setTimeout()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/timer/set-timeout/)
- [clearTimeout()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/timer/clear-timeout)
- [setInterval()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/timer/set-interval)
- [clearInterval()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/timer/clear-interval)
#### 触摸事件
[所有触摸事件 API](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/click-event/touch)
#### 画布
- [tt.createCanvas()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/picture/tt-create-canvas)
- [tt.getSharedCanvas()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data/tt-get-shared-canvas)
#### 图片
[tt.createImage()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/drawing/picture/tt-create-image)
#### 开放数据
- [tt.getUserCloudStorage()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data/tt-get-user-cloud-storage)
- [tt.setUserCloudStorage()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data/tt-set-user-cloud-storage)
- [tt.removeUserCloudStorage()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data/tt-remove-user-cloud-storage)
- [tt.getCloudStorageByRelation()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data/tt-get-cloud-storage-by-relation)
- [tt.setUserGroup()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/relationship-chain/ranking/tt-set-user-group)
#### 游戏排行榜
- [tt.getImRankData()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/game-rank/getImRankData)
- [tt.setImRankDataInOpenContext()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/game-rank/set-im-rank-data-in-open-context)
#### 监听主域消息
[tt.onMessage()](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data-area/tt-on-message)
