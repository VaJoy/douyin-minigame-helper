---
title: "tt.setPreferredFramesPerSecond"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/drawing/frame-rate/tt-set-preferred-frames-per-second
update_time: 2024-07-24
---

## 语法

```js
tt.setPreferredFramesPerSecond(fps)
```
基础库 1.15.0 开始支持本方法，这是一个**同步**方法。
修改渲染帧率。修改后，requestAnimationFrame 的回调频率会发生改变。

## 示例代码
```js
// 修改渲染帧率为30帧每秒
tt.setPreferredFramesPerSecond(30);
requestAnimationFrame(() => {
  console.log("理论上每秒绘制30次，在每次重绘前执行requestAnimationFrame回调");
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| fps | number | 是 | 60 | 1.15.0 | 默认渲染帧率为 60 帧每秒，有效范围 1-60 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/drawing/frame-rate/tt-set-preferred-frames-per-second) / [本地体验路径](sslocal://microgame?app_id=ttc203b4be5d39867a&query=%7B%22query%22%3A%22tt-set-preferred-frames-per-second%22%7D)
