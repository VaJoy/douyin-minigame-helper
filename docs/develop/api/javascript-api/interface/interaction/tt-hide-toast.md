---
title: "tt.hideToast"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/interface/interaction/tt-hide-toast
update_time: 2024-07-24
---

基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
隐藏灰色背景的消息提示框。

## 示例代码
```js
tt.hideToast({
  success(res) {
    console.log(`${res}`);
  },
  fail(res) {
    console.log(`hideToast调用失败`);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："hideToast:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："hideToast:fail " + 详细错误信息 |

## 注意事项
loading 的实现基于 toast，所以 hideToast 也会将 loading 隐藏。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/interface/interaction/tt-hide-toast) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-hide-toast%22%7D) / [在线试玩](https://developer.open-douyin.com/docs/playground?project_id=tma-demo&version=1.0.0.10&entry=tt-hide-toast&codes_select=js&type=mini-game&sdk_version=1.0.0.205)
