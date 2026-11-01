---
title: "tt.canIUse"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/tt-can-i-use
update_time: 2024-07-24
---

## 语法

```js
tt.canIUse(schema)
```
基础库 1.35.0 开始支持本方法，这是一个**同步**方法。
判断小游戏的 API、回调、参数、组件等是否在当前版本可用。

## 示例代码
```js
// 判断tt.request(option)函数是否可用
tt.canIUse("request");
// 判断tt.request(option)函数的回调成功的返回值中是否有data参数
tt.canIUse("request.success.data");
// 判断tt.request(option)传入参数对象中是否有url参数
tt.canIUse("request.object.url");
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| schema | string | 是 |  | 1.35.0 | 用来测试的能力，模式为 ${API}.${method}.${param}.${option} 或者 ${component}.${attribute}.${option}  - ${API}：API名字 - ${method}：调用方式，有效值为 return、success、object、callback - ${param}：参数或者返回值 - ${option}：参数的有效值或者返回值的属性或者组件属性的有效值 - ${component}：组件名字 - ${attribute}：组件属性 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| canUse | boolean | 在当前版本是否可用 |

## 使用限制
- 不支持 fail 和 complete 回调函数的判断
- 纯 number 类型的属性不做支持

## 注意事项
- 回调函数的名称以文档为准

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/tt-can-i-use) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-can-i-use%22%7D)
