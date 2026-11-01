---
title: "tt.onCompassChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/compass/tt-on-compass-change
update_time: 2024-08-29
---

## 语法

```js
tt.onCompassChange(callback)
```
基础库 1.2.0 开始支持本方法，这是一个**同步**方法。
监听罗盘数据变化事件，罗盘数据会在用户手机发生“朝向变化/加速前进&后退/摇一摇”等手势时触发变化。频率：5 次/秒，接口调用后会自动开始监听，可使用 [tt.stopCompass](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/compass/tt-stop-compass) 停止监听。

## 示例代码
```js
tt.onCompassChange((res) => {
  console.log(`罗盘方向: ${res.direction}`);
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.2.0 | 在罗盘数据变化时执行的回调函数  **对象字段** - **args_0**（Object）：object类型，属性如下： |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/compass/tt-on-compass-change) / [本地体验路径](tt-on-compass-change)
