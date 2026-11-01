---
title: "tt.checkFollowState"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/follow/follow-tt/tt-check-follow-state
update_time: 2024-07-24
---

基础库 1.30.0 开始支持本方法，这是一个**异步**方法。
查看用户是否已关注小游戏绑定的头条号（注意这个头条号是小游戏开发者在开发者平台绑定的官方头条号）

## 示例代码
```js
tt.checkFollowState({
  success(res) {
    console.log(res.result); // true:已关注 /  false:未关注
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **result**（boolean）：是否已关注头条号 - **errMsg**（string）："checkFollowState:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："checkFollowState:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 21000 | internal error |  |  |

## 前置条件
使用该功能前开发者需要绑定想要查看的头条号，参考[绑定头条号](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/-retention/binding-toutiao-account/)指南

1. 前往“头条号-功能实验室-小程序”
2. 点击“新建绑定”，输入小游戏的 Appid ，提交绑定
3. 前往“小游戏开发者后台-设置-基础设置-绑定设置”，同意绑定并等待审核通过

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/open-capacity/follow/follow-tt/tt-check-follow-state)
