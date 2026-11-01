---
title: "tt.getEnvInfoSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/system-information/tt-get-env-info-sync
update_time: 2024-08-29
---

基础库 2.78.0 开始支持本方法，这是一个**同步**方法。
获取小游戏环境信息。

## 示例代码
```js
const { microapp, common } = tt.getEnvInfoSync();
console.log("microapp:", microapp, "common:", common);
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | Object | object 类型，属性如下  **对象字段** - **microapp**（Object）：小游戏信息 - **common**（Object）：object 类型，属性如下： |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/system/system-information/tt-get-env-info-sync) / [本地体验路径](tt-get-env-info-sync)
