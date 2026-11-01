---
title: "GridGamePanel"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/ads/grid-game-panel/grid-game-panel
update_time: 2025-02-18
---

通过 [tt.createGridGamePanel](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/grid-game-panel/tt-create-grid-game-panel) 获取的实例，通过它可以对 游戏推荐组件 进行展示、隐藏、销毁、注册监听等操作。
## 属性
### 可设置属性

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| size | string | large | 否 | 合理值：large \| medium \| small，表示组件大小，large：100%，medium：90%，small：80%。 **仅 gridCount = one \| four 时有效。** | 2.82.0 |
| position | object |  | 否 | 控制游戏推荐组件的展示位置，不传入时默认展示在**屏幕右下角**。 **仅 gridCount = one 时有效。** | 2.82.0 |
| query | object |  | 否 | 从组件内打开游戏时附带的query信息，请阅读下文确认具体格式。 | 2.82.0 |

Tip: 实例属性修改后需要下一次`GridGamePanel.show`时才会生效。
#### **position**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| left | number |  | 是 | 组件左上角横坐标 |
| top | number |  | 是 | 组件左上角纵坐标 |

#### **query**

| 属性 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| appid1 | string |  | 否 | query字符串，必须是 key1=val1&key2=val2 的格式。打开游戏后，可通过 [tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-get-launch-options-sync) 获取启动参数中的 query。 appid1 是游戏的AppId的具体值，用于给指定游戏设置query。 |
| appid2 | string |  | 否 | 同上 |
| ... |  |  |  |  |

合法的 query 格式如下：

```json
{
  "appid1": "age=1",
  "appid2": "age=2&name=xxx",
  "appid3": "age=3&location=xxx"
}
```

### 只读属性

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| gridCount | string | 合理值：one \| four \| nine，表示游戏推荐组件的格子数量。 | 2.82.0 |

## 方法

| 方法名 | 说明 | 最低支持版本 |
| --- | --- | --- |
| [show](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/grid-game-panel/grid-game-panel/grid-game-panel-show) | 展示游戏推荐组件 | 2.82.0 |
| [hide](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/grid-game-panel/grid-game-panel/grid-game-panel-hide) | 隐藏游戏推荐组件 | 2.82.0 |
| [onStateChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/grid-game-panel/grid-game-panel/grid-game-panel-on-state-change) | 绑定游戏推荐组件状态变化事件的监听器 | 2.82.0 |
| [offStateChange](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/grid-game-panel/grid-game-panel/grid-game-panel-off-state-change) | 解绑游戏推荐组件状态变化事件的监听器 | 2.82.0 |
| [destroy](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/grid-game-panel/grid-game-panel/grid-game-panel-destroy) | 销毁游戏推荐组件实例 | 2.82.0 |
