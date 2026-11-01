---
title: "tt.offCompassChange"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/device/compass/tt-off-compass-change
update_time: 2024-08-29
---

## 语法

```js
tt.offCompassChange(callback)
```
基础库 1.94.0 开始支持本方法，这是一个**同步**方法。
解绑罗盘数据变化监听器。

## 示例代码
```js
const callback = (res) => {
  console.log(`罗盘方向: ${res.direction}`);
};

tt.onCompassChange(callback);
tt.offCompassChange(callback);
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 否 |  | 1.94.0 | 在罗盘数据变化时执行的函数 |

## 注意事项
不传入 callback 参数时，会移除所有监听函数

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/device/compass/tt-off-compass-change) / [本地体验路径](tt-off-compass-change)
