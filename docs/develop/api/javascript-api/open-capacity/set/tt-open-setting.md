---
title: "tt.openSetting"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/set/tt-open-setting
update_time: 2025-11-24
---

基础库 1.3.0 开始支持本方法，这是一个**异步**方法。
打开设置页面，返回用户设置过的授权结果。

## 示例代码
```js
tt.openSetting({
  success(res) {
    console.log(res);
  },
  fail(res) {
    console.log(`openSetting 调用失败`);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **authSetting**（Object）：[AuthSetting](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/set/auth-setting)，授权结果 - **errMsg**（string）："openSetting:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："openSetting:fail " + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10401 | internal error |  |  |
| 20000 | internal error |  |  |

## 注意事项
- 设置页面只包含用户请求过的[权限](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/set/auth-setting)。
- 与 [tt.getSetting](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/set/tt-get-setting) 的区别是，openSetting 会打开设置页面，而 getSetting 只会返回用户授权的设置信息

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-capacity/user-information/set/tt-open-setting) / [本地体验路径](tt-open-setting)
