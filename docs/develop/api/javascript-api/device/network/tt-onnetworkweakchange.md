---
title: "tt.onNetworkWeakChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/network/tt-onnetworkweakchange
update_time: 2024-12-25
---

## 语法

```js
tt.onNetworkWeakChange(callback)
```
基础库 3.44.0 开始支持本方法，这是一个**同步**方法。
监听弱网状态变化事件

## 示例代码
```js
tt.onNetworkWeakChange(function (res) {
  console.log(res.weakNet)
  console.log(res.networkType)
})
// 取消监听
tt.offNetworkWeakChange()
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 3.44.0 | 弱网状态变化事件的监听函数  **对象字段** - **args_0**（Object）：回调参数 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
