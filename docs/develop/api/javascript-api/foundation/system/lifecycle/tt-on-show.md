---
title: "tt.onShow"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/lifecycle/tt-on-show
update_time: 2024-07-24
---

## 语法

```js
tt.onShow(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
监听小游戏回到前台的事件。

## 示例代码
```js
tt.onShow((res) => {
  console.log("启动参数：", res.query);
  console.log("来源信息：", res.refererInfo);
  console.log("场景值：", res.scene);
  console.log("启动场景字段：", res.launch_from, ", ", res.location);
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.0.0 | 小游戏回到前台的事件回调  **对象字段** - **GameShowParams**（Object）：回调参数 |

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
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/system/lifecycle/tt-on-show) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-on-show%22%7D)
