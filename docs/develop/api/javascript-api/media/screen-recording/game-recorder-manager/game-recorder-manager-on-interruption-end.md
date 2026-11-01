---
title: "GameRecorderManager.onInterruptionEnd"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/media/screen-recording/game-recorder-manager/game-recorder-manager-on-interruption-end
update_time: 2024-11-11
---

## 语法

```js
GameRecorderManager.onInterruptionEnd(callback)
```
基础库 1.6.1 开始支持本方法，这是一个**同步**方法。
监听录屏中断结束事件。

## 示例代码
```js
const recorder = tt.getGameRecorderManager();

recorder.onStop(() => {
    console.log('录屏发生中断')
});

recorder.onInterruptionEnd(() => {
    console.log('录屏结束中断')
})

recorder.start();
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.6.1 | 监听录屏中断结束事件的回调函数 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
