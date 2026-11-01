---
title: "Worker.terminate"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/worker/worker-terminate
update_time: 2025-06-05
---

基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
结束当前 worker 线程。

## 示例代码
```js
worker = tt.createWorker('workers/index.js');

worker.terminate();  // 结束worker进程
```

## 使用限制
仅限在主线程 worker 对象上调用。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/worker/worker-terminate) / [本地体验路径](worker-terminate)
