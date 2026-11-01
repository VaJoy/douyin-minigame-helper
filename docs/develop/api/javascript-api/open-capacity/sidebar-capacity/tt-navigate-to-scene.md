---
title: "tt.navigateToScene"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/sidebar-capacity/tt-navigate-to-scene
update_time: 2024-08-19
---

## 语法

```js
tt.navigateToScene(scene)
```
基础库 2.92.0 开始支持本方法，这是一个**异步**方法。
调用该API可以跳转到某个小游戏入口场景，目前仅支持跳转「侧边栏」场景。

## 示例代码
```js
tt.navigateToScene({
    scene: "sidebar",
    success: (res) => {
        console.log("navigate to scene success");
        // 跳转成功回调逻辑
    },
    fail: (res) => {
        console.log("navigate to scene fail: ", res);
        // 跳转失败回调逻辑
    },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| scene | number | 是 |  | 2.92.0 | 需要确认的入口场景  **可选值：** sidebar=

【侧边栏】场景

 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："navigateToScene:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："navigateToScene:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | expect params.scene to be one of "sidebar", but got xxx |  |  |
| 20001 | expect params.scene to be one of "sidebar", but got "xxx" |  |  |
| 20001 | expect params.scene to be one of "sidebar", but got undefined |  |  |
| 21101 | scene xxx is inaccessible |  |  |

## 使用限制
仅支持抖音宿主。可以通过 [tt.checkScene](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/sidebar-capacity/tt-check-scene) 判断是否当前宿主是否支持

## 注意事项
- 抖音开发者工具在4.1.5及以上版本支持通过模拟器模拟该API，详见[开发者工具更新及下载](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/developer-instrument/developer-instrument-update-and-download)。
- 通过侧边栏入口进入小游戏时，[tt.onShow](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/system/lifecycle/tt-on-show/) 会在监听回调中新增两个返回字段 launch_from = 'homepage' 和 location = 'sidebar_card' ，可用于判断用户是否从该入口场景进入小游戏

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-capacity/sidebar-capacity/tt-navigate-to-scene) / [本地体验路径](tt-navigate-to-scene)