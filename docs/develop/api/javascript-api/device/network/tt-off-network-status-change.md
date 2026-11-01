---
title: "tt.offNetworkStatusChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/network/tt-off-network-status-change
update_time: 2024-07-24
---

## 语法

```js
tt.offNetworkStatusChange(callback)
```
基础库 1.91.0 开始支持本方法，这是一个**同步**方法。
移除网络状态变化事件的监听函数。

## 示例代码
```js
function handleNetworkStatusChange(res) {
  console.log(res.networkType);
  console.log(res.isConnected);
}
tt.onNetworkStatusChange(handleNetworkStatusChange);
tt.offNetworkStatusChange(handleNetworkStatusChange);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 1.91.0 | 网络状态变化的事件回调 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |

## 注意事项
不传入callback参数时，会移除所有监听函数。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/network/tt-off-network-status-change) / [本地体验路径](tt-off-network-status-change)
