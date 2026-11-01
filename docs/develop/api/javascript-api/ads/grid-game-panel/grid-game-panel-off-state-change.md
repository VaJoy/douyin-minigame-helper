---
title: "GridGamePanel.offStateChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/grid-game-panel/grid-game-panel-off-state-change
update_time: 2024-08-19
---

## 语法

```js
GridGamePanel.offStateChange(callback)
```
基础库 2.82.0 开始支持本方法，这是一个**同步**方法。
解绑游戏推荐组件实例状态变化事件的监听器。

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
  const listener = (res) => {
    console.log("游戏推荐组件状态变化", res);
  };
  gridGamePanel.onStateChange(listener);
  gridGamePanel.offStateChange(listener);
  console.log("游戏推荐组件 offStateChange");
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 2.82.0 | 通过 [GridGamePanel.onStateChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/grid-game-panel/grid-game-panel/grid-game-panel-on-state-change) 绑定的监听器 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/grid-game-panel-state-change) / [本地体验路径](grid-game-panel-state-change)
