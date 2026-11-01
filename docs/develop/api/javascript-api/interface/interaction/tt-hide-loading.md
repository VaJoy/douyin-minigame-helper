---
title: "tt.hideLoading"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/interaction/tt-hide-loading
update_time: 2024-07-24
---

基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
隐藏 loading 提示框。

## 示例代码
```js
tt.hideLoading({
  success(res) {
    console.log(`${res}`);
  },
  fail(res) {
    console.log(`hideLoading调用失败`);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："hideLoading:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："hideLoading:fail " + 详细错误信息 |

## 注意事项
loading 的实现基于 toast，所以hideLoading也会将 toast 隐藏。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/interface/interaction/tt-hide-loading) / [本地体验路径](tt-hide-loading) / [在线试玩](https://developer.open-douyin.com/docs/playground?project_id=tma-demo&version=1.0.0.10&entry=tt-hide-loading&codes_select=js&type=mini-game&sdk_version=1.0.0.205)
