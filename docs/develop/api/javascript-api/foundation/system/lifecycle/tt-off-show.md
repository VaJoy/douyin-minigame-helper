---
title: "tt.offShow"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/lifecycle/tt-off-show
update_time: 2024-07-24
---

## 语法

```js
tt.offShow(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
取消监听小游戏回到前台的事件。

## 示例代码
【代码示例 1】：取消所有的监听函数。
```js
tt.offHide();
```
【代码示例 2】：取消传入的监听函数。
```js
function onShowCallback(res) {
  console.log("启动参数如下：", res.query);
  console.log("来源信息如下：", res.refererInfo);
}
// 添加小游戏回到前台的监听函数
tt.onShow(onShowCallback);
// 取消小游戏回到前台的监听函数
tt.offShow(onShowCallback);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 1.0.0 | 小游戏回到前台的事件回调  - callback 参数非必填，不传时表示取消所有的回到前台的监听函数。 - callback 传入对应的回调函数，表示取消当前传入的回到前台的监听函数。 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/system/lifecycle/tt-off-show) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-off-show%22%7D)
