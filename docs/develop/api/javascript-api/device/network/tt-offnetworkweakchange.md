---
title: "tt.offNetworkWeakChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/network/tt-offnetworkweakchange
update_time: 2024-12-25
---

## 语法

```js
tt.offNetworkWeakChange(callback)
```
基础库 3.44.0 开始支持本方法，这是一个**同步**方法。
移除弱网状态变化事件的监听函数

## 示例代码
```js
const listener = function (res) { console.log(res) }

tt.onNetworkWeakChange(listener)
tt.offNetworkWeakChange(listener) // 需传入与监听时同一个的函数对象
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 3.44.0 | onNetworkWeakChange 传入的监听函数。不传此参数则移除所有监听函数。 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
