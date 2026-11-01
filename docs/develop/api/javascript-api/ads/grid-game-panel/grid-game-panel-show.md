---
title: "GridGamePanel.show"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/grid-game-panel/grid-game-panel-show
update_time: 2024-08-19
---

基础库 2.82.0 开始支持本方法，这是一个**同步**方法。
展示游戏推荐组件。

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
  gridGamePanel
    .show()
    .then(() => {
      console.error("展示游戏推荐组件成功");
    })
    .catch((err) => {
      console.error("展示游戏推荐组件失败", err);
    });
}
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | Promise | Promise对象 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21101 | GridGamePanel with the same gridCount can show most one |  |  |
| 21102 | Fetch game list error |  |  |
| 10301 | feature is not supported in app |  |  |
| 10401 | Internal error |  |  |
| 10302 | In the gray scale experiment, the user will not display |  |  |
| 21000 | invalid param |  |  |
| 21000 | previous request not finish |  |  |
| 10103 | unavailable network |  |  |

## 使用限制
目前仅支持抖音、抖音极速版

## 注意事项
- 修改游戏推荐组件实例的属性如 size、position、query 后，需要下一次调用 GridGamePanel.show 时才会生效；
- 同一个游戏推荐组件重复调用 show 接口且当前实例已经处于展示状态时，调用并不会失败，也不会有错误消息返回。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/tt-create-grid-game-panel) / [本地体验路径](tt-create-grid-game-panel)
