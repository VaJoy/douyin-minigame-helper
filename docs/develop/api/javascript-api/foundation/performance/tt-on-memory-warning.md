---
title: "tt.onMemoryWarning"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/performance/tt-on-memory-warning
update_time: 2024-07-24
---

## 语法

```js
tt.onMemoryWarning(callback)
```
基础库 1.28.0 开始支持本方法，这是一个**同步**方法。
注册监听内存不足警告函数。当手机内存占用过高时，触发注册函数。

## 示例代码
```js
tt.onMemoryWarning(function () {
  console.log("onMemoryWarning");
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.28.0 | 内存不足回调函数  **对象字段** - **level**（number）：仅 Android 有该字段，对应系统内存告警等级宏定义 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 使用限制
- 该事件不会杀掉小程序, 建议开发者可以在接收到报警后释放相关不必要的资源。
- Android 下有告警等级划分。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/performance/tt-on-memory-warning) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-on-memory-warning%22%7D)
