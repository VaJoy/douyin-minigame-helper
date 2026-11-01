---
title: "tt.offHide"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/lifecycle/tt-off-hide
update_time: 2024-07-24
---

## 语法

```js
tt.offHide(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
取消监听小游戏隐藏到后台事件。锁屏、按 HOME 键退到桌面等操作会触发此事件。

## 示例代码
```js
function onHideCallback() {
  console.log("监听到小游戏进入后台");
}

// 添加小游戏进入后台的监听函数
tt.onHide(onHideCallback);
// 取消小游戏回到前台的监听函数
tt.offHide(onHideCallback);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 1.0.0 | 取消监听事件的回调函数。 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
