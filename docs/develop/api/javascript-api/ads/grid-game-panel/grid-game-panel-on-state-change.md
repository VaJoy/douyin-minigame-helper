---
title: "GridGamePanel.onStateChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/grid-game-panel/grid-game-panel-on-state-change
update_time: 2024-08-19
---

## 语法

```js
GridGamePanel.onStateChange(callback)
```
基础库 2.82.0 开始支持本方法，这是一个**同步**方法。
绑定游戏推荐组件实例状态变化事件的监听器。

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
  gridGamePanel.onStateChange((res) => {
    console.log("游戏推荐组件状态变化", res);
  });
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 2.82.0 | 状态变化事件的监听器  **对象字段** - **GridGamePanelStateChangeResponse**（Object）：object类型，属性如下 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 999981 | In the gray scale experiment, the user will not display |  |  |
| 21101 | GridGamePanel with the same gridCount can show most one |  |  |
| 21102 | Fetch game list error |  |  |
| 10301 | feature is not supported in app |  |  |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |
| 21000 | current game panel doesn't exist |  |  |
| 21000 | @'operation' is illegal param |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/grid-game-panel-state-change) / [本地体验路径](grid-game-panel-state-change)
