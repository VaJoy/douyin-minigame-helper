---
title: "tt.openAwemeUserProfile"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/follow/follow-aweme/tt-open-aweme-user-profile
update_time: 2024-08-19
---

## 使用效果
> 无论用户是否已经转关，调用后在游戏内都会弹出关注面板，点击用户头像可以跳转至 抖音号主页。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1652855583188)

基础库 1.84.0 开始支持本方法，这是一个**异步**方法。
跳转个人抖音号主页，用户可以选择关注/取消关注抖音号。

## 示例代码
```js
tt.openAwemeUserProfile({
    success: (res) => {
        console.log('是否关注抖音号', res.hasFollowed)
    },
    fail: (res) => {
        console.log('调用失败', res)
    }
})
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **hasFollowed**（boolean）：是否关注抖音号 - **errMsg**（string）："openAwemeUserProfile:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："openAwemeUserProfile:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10301 | feature is not supported in app |  |  |
| 21102 | aweme uid is null |  |  |
| 21100 | not login |  |  |
| 21101 | activity is null |  |  |
| 21103 | /s |  |  |
| 20000 | internal error |  |  |
| 10101 | platform auth deny |  |  |
| 21000 | /s |  |  |

## 使用限制
暂时只支持在**抖音**及**抖音极速版** App 上使用。

## 前置条件
使用该功能前开发者需要绑定想要查看的抖音号，参考[游戏内关注抖音号能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/-retention/follow-douyin/)接入指南

1. 前往小游戏开发者后台，进入“设置-基础设置”模块，在“抖音号绑定”一栏点击“去绑定”
2. 进入“抖音号绑定”页面，使用需绑定的抖音号，打开手机使用抖音 APP 扫一扫。 （绑定成功暂不支持更换，请谨慎选择需绑定的抖音号）

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
