---
title: "tt.checkScene"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/sidebar-capacity/tt-check-scene
update_time: 2024-08-19
---

## 语法

```js
tt.checkScene(scene)
```
基础库 2.92.0 开始支持本方法，这是一个**异步**方法。
确认当前宿主版本是否支持跳转某个小游戏入口场景，目前仅支持「侧边栏」场景。

## 示例代码
```js
tt.checkScene({
    scene: "sidebar",
    success: (res) => {
        console.log("check scene success: ", res.isExist);
        //成功回调逻辑
    },
    fail: (res) => {
        console.log("check scene fail:", res);
        //失败回调逻辑
    }
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| scene | number | 是 |  | 2.92.0 | 需要确认的入口场景  **可选值：** sidebar=【侧边栏】场景 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **isExist**（boolean）：入口场景是否存在 - **errMsg**（string）："checkScene:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："checkScene:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | expect params.scene to be one of "sidebar", but got xxx |  |  |
| 20001 | expect params.scene to be one of "sidebar", but got "xxx" |  |  |
| 20001 | expect params.scene to be one of "sidebar", but got undefined |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[本地体验路径](tt-check-scene)
