---
title: "GridAd"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/grid-game-panel/grid-ad
update_time: 2025-08-25
---

## 互推资源位
createGridGamePanel是一个原生广告组件，开发者可以通过[tt.createGridGamePanel](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/tt-create-grid-game-panel)创建宫格实例, 其层级高于普通组件。该组件默认显示在屏幕右下角，用于创建和展示游戏推荐矩阵。通过宫格(Grid)形式展示多个小游戏入口，用户点击后可跳转至对应游戏。主要功能是实现游戏间的交叉推广，构建游戏生态矩阵。

```js

  const singleGrid = tt.createGridGamePanel({
    gridCount: "one",
    size: "large",
    position: {
      top: 600,
      left: 300,
    },
    query: {
      tt00000000000000: "age=12&name=xxxx",
    },
  });
```

### 显示/隐藏

广告创建后，可以通过调用[GridGamePanel.show](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/grid-game-panel/grid-game-panel-show)显示广告，该方法返回一个Promise对象

```js
let gridGamePanel = tt.createGridGamePanel({ gridCount:"nine" })
*
*gridGamePanel.show().then(()=>{
*   console.log('组件显示成功!')
*})
```

当需要隐藏广告组件时，可以调用[GridGamePanel.hide](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/grid-game-panel/grid-game-panel-hide)

```js
let gridGamePanel = tt.createGridGamePanel({ gridCount:"nine" })
*
*gridGamePanel.hide().then(()=>{
*   console.log('组件显示成功!')
*})
```

### 监听与解绑
当组件状态发生变化，可通过监听[GridGamePanel.onStateChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/grid-game-panel/grid-game-panel-on-state-change)来监听组件是否关闭和显示, 最后通过[GridGamePanel.offStateChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/grid-game-panel/grid-game-panel-off-state-change)解绑监听函数
### 销毁
当广告已经使用完毕，需要销毁时，可以调用[GridGamePanel.destroy](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/ads/grid-game-panel/grid-game-panel-destroy)

javascript;
try {
// 单宫格配置示例
const singleGrid = tt.createGridGamePanel({
gridCount: "one",
size: "large",
position: {
top: 600,
left: 300,
},
query: {
tt00000000000000: "age=12&name=xxxx",
},
});

// 四宫格配置示例
const quadGrid = tt.createGridGamePanel({
gridCount: "four",
size: "large",
query: {
tt00000000000000: "age=12&name=xxxx",
tt00000000000001: "age=12&name=xxxx",
},
});

// 九宫格配置示例
const nineGrid = tt.createGridGamePanel({
gridCount: "nine",
query: {
tt00000000000000: "age=12&name=xxxx",
tt00000000000001: "age=12&name=xxxx",
tt00000000000002: "age=12&name=xxxx",
},
});
} catch (err) {
console.error("游戏推荐组件创建失败", err);
}

try {
// 单宫格可设置大小和位置
const oneGridGamePanel = tt.createGridGamePanel({
gridCount: "one",
size: "large",
position: {
top: 600,
left: 300,
},
query: {
tt00000000000000: "age=12&name=xxxx",
},
});
// 四宫格可设置大小 设置位置无实际作用
const fourGridGamePanel = tt.createGridGamePanel({
gridCount: "four",
size: "large",
query: {
tt00000000000000: "age=12&name=xxxx",
tt00000000000001: "age=12&name=xxxx",
},
});
// 九宫格 设置大小和位置无实际作用
const nineGridGamePanel = tt.createGridGamePanel({
gridCount: "nine",
query: {
tt00000000000000: "age=12&name=xxxx",
tt00000000000001: "age=12&name=xxxx",
tt00000000000002: "age=12&name=xxxx",
},
});
} catch (error) {
console.error("创建游戏推荐组件失败", error);
}
