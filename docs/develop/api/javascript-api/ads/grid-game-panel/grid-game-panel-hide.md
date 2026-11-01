---
title: "GridGamePanel.hide"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/grid-game-panel/grid-game-panel-hide
update_time: 2024-08-19
---

基础库 2.82.0 开始支持本方法，这是一个**异步**方法。
隐藏游戏推荐组件。

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
      console.log("展示游戏推荐组件成功");
    })
    .catch((err) => {
      console.error("展示游戏推荐组件失败", err);
    });
  setTimeout(() => {
    gridGamePanel.hide();
    console.log("隐藏游戏推荐组件");
  }, 5000);
}
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："GridGamePanel.hide:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："GridGamePanel.hide:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 10401 | Internal error |  |  |
| 21000 | current game panel doesn't exist |  |  |
| 10301 | feature is not supported in app |  |  |
| 10302 | In the gray scale experiment, the user will not display |  |  |

## 注意事项
同一个游戏推荐组件重复调用 hide 接口且当前实例已经处于隐藏状态时，调用并不会失败，也不会有错误消息返回

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/tt-create-grid-game-panel) / [本地体验路径](tt-create-grid-game-panel)
