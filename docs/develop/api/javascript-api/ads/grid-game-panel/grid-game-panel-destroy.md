---
title: "GridGamePanel.destroy"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/grid-game-panel/grid-game-panel-destroy
update_time: 2024-08-19
---

基础库 2.82.0 开始支持本方法，这是一个**同步**方法。
销毁游戏推荐组件实例。

## 示例代码
```js
let gridGamePanel = null;
try {
  gridGamePanel = tt.createGridGamePanel({
    gridCount: "nine",
    query: {
      tt00000000000000: "age=12&name=xxxx",
    },
  });
} catch (error) {
  console.error("创建游戏推荐组件失败", error);
}

if (gridGamePanel) {
  gridGamePanel.destroy();
  console.log("游戏推荐组件销毁");
}
```

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 21000 | current game panel doesn't exist |  |  |
| 10401 | Internal error |  |  |
| 10301 | feature is not supported in app |  |  |
| 10302 | In the gray scale experiment, the user will not display |  |  |

## 注意事项
游戏推荐组件实例销毁时，会移除实例上所有事件的监听器

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/tt-create-grid-game-panel) / [本地体验路径](tt-create-grid-game-panel)
