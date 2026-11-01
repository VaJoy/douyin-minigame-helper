---
title: "tt.createGridGamePanel"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/tt-create-grid-game-panel
update_time: 2024-08-19
---

## 语法

```js
tt.createGridGamePanel(params)
```
基础库 2.82.0 开始支持本方法，这是一个**同步**方法。
创建游戏推荐组件实例。

## 示例代码
```js
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
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| params | Object | 是 |  | 2.82.0 | object类型，属性如下：  **对象字段** - **position**（Object）：控制游戏推荐组件的展示位置，不传入时默认展示在屏幕右下角。 仅 gridCount = one 时有效 - **query**（Object）：从组件内打开游戏时附带的query信息，请阅读下文确认具体格式 - **gridCount**（number）：表示游戏推荐组件的格子数量 - **size**（number）：表示组件大小，仅 gridCount = one \| four 时有效。 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| GridGamePanel | Object | [GridGamePanel](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/grid-game-panel/grid-game-panel/grid-game-panel)实例 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10302 | In the gray scale experiment, the user will not display |  |  |
| 10401 | operation is illegal |  |  |
| 21101 | GridGamePanel with the same gridCount can show most one |  |  |
| 10301 | feature is not supported in app |  |  |
| 21102 | Fetch game list error |  |  |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |

## 使用限制
目前仅支持抖音、抖音极速版。

## 注意事项
本接口是同步接口，传入参数不合法时会直接抛出参数错误的异常，请做好处理。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
