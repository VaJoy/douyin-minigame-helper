---
title: "tt.checkFollowAwemeState"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/follow/follow-aweme/tt-check-follow-state
update_time: 2024-07-24
---

基础库 2.70.0 开始支持本方法，这是一个**异步**方法。
提供从小游戏查看抖音号是否关注的能力。

## 示例代码
```js
tt.checkFollowAwemeState({
  success(res) {
    console.log("调用成功", res);
  },
  fail(res) {
    console.log("调用失败", res);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **hasFollowed**（boolean）：是否关注抖音号 - **errMsg**（string）："checkFollowAwemeState:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："checkFollowAwemeState:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10301 | feature is not supported in app |  |  |
| 21100 | not login |  |  |
| 21101 | aweme uid is null |  |  |
| 21102 | /s |  |  |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |
| 10101 | platform auth deny |  |  |
| 10601 | not login |  |  |
| 21000 | /s |  |  |

## 使用限制
目前该接口只支持抖音，所以请在**抖音**或**抖音Lite** APP中调用

## 前置条件
该功能为抖音专有 API，使用该功能前开发者需要绑定想要查看的抖音号，参考[游戏内关注抖音号能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/-retention/follow-douyin/)接入指南

1. 前往小游戏开发者后台，进入“设置-基础设置”模块，在“抖音号绑定”一栏点击“去绑定”
2. 进入“抖音号绑定”页面，使用需绑定的抖音号，打开手机使用抖音 APP 扫一扫。 （绑定成功暂不支持更换，请谨慎选择需绑定的抖音号）

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-capacity/follow/follow-aweme/tt-check-follow-aweme-state) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-check-follow-state%22%7D)
