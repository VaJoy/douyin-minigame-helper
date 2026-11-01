---
title: "tt.restartMiniProgramSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/lifecycle/tt-restart-mini-program-sync
update_time: 2024-08-29
---

基础库 2.68.0 开始支持本方法，这是一个**同步**方法。
重启小游戏。

## 示例代码
```js
try {
  tt.restartMiniProgramSync();
} catch (error) {
  console.log(`restartMiniProgramSync调用失败`, error);
}
```

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/system/lifecycle/tt-restart-mini-program-sync) / [本地体验路径](tt-restart-mini-program-sync)
