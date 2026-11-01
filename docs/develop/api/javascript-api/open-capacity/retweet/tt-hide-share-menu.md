---
title: "tt.hideShareMenu"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/retweet/tt-hide-share-menu
update_time: 2024-07-24
---

基础库 1.5.0 开始支持本方法，这是一个**异步**方法。
隐藏转发按钮。

## 示例代码
```js
tt.hideShareMenu({
  success(res) {
    console.log("已成功隐藏转发按钮");
  },
  fail(err) {
    console.log("hideShareMenu 调用失败", err.errMsg);
  },
  complete(res) {
    console.log(`hideShareMenu 调用完成`);
  },
});
```

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："hideShareMenu:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："hideShareMenu:fail " + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |
| 20000 | unsupport menu |  |  |

## 注意事项
无论调用本 API 前当前页面是否显示转发按钮，调用本 API 均会执行成功回调。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/retweet/tt-hide-share-menu) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-hide-share-menu%22%7D)
