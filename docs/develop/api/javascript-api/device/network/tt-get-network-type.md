---
title: "tt.getNetworkType"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/network/tt-get-network-type
update_time: 2024-07-24
---

基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
获取设备当前所处的网络类型。

## 示例代码
```js
tt.getNetworkType({
  success(res) {
    console.log(`${res.networkType}`);
  },
  fail(res) {
    console.log(`getNetworkType调用失败`);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **networkType**（string）：网络类型 - **errMsg**（string）："getNetworkType:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getNetworkType:fail " + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 注意事项
networkType 在设备某些无法确定网络类型情况下会返回 "unknown"

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/network/tt-get-network-type) / [本地体验路径](tt-get-network-type)
