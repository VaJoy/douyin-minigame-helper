---
title: "tt.getSetting"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/set/tt-get-setting
update_time: 2025-09-29
---

基础库 1.3.0 开始支持本方法，这是一个**异步**方法。
获取用户已经授权过的配置。

## 示例代码
```js
tt.getSetting({
  success(res) {
    console.log(res);
  },
  fail(res) {
    console.log(`getSetting 调用失败`);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **authSetting**（Object）：[AuthSetting](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/set/auth-setting/)，授权结果。 - **errMsg**（string）："getSetting:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getSetting:fail " + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 注意事项
与 [tt.openSetting](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/set/tt-open-setting) 的区别是 getSetting 只会获取配置，而不会打开配置页面。

## 版本说明
**结果中只会包含小游戏向用户请求过的**[权限](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/authorization/authorization/)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-capacity/user-information/set/tt-get-setting) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-get-setting%22%7D)
