---
title: "GameRecorderManager.onStart"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/screen-recording/game-recorder-manager/game-recorder-manager-on-start
update_time: 2024-11-11
---

## 语法

```js
GameRecorderManager.onStart(callback)
```
基础库 1.4.1 开始支持本方法，这是一个**同步**方法。
监听录屏开始事件。

## 示例代码
```js
const recorder = tt.getGameRecorderManager();

recorder.onStart((res) => {
  // do something;
});

recorder.start();
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.4.1 | 监听事件的回调函数 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/game-recorder-manager-on-start) / [本地体验路径](game-recorder-manager-on-start)
