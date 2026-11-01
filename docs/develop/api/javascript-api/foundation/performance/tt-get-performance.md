---
title: "tt.getPerformance"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/performance/tt-get-performance
update_time: 2024-07-24
---

基础库 1.15.0 开始支持本方法，这是一个**同步**方法。
获取性能管理器。

## 示例代码
```js
// 获取性能管理器
let performance = tt.getPerformance();
// 获取当前时间的时间戳
let now = performance.now();
```

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| Performance | Object | 性能管理对象  **对象字段** - **now**（Function）：获取当前时间的时间戳(单位：微秒) |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/performance/tt-get-performance) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-get-performance%22%7D)
