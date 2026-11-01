---
title: "Worker.onMessage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/worker/worker-on-message
update_time: 2025-06-05
---

const worker = tt.createWorker("my-worker.js");
worker.onMessage((message) => {
console.log(message);
});

Worker.onMessage(callback)

## 语法

```js
Worker.onMessage(callback)
```
基础库 1.0.0 开始支持本方法，这是一个**同步**方法。
监听接收 主线程/Worker线程 向当前线程发送的消息。

## 示例代码
```js
const worker = tt.createWorker("my-worker.js");
worker.onMessage((message) => {
  console.log(message);
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| callback | Function | 是 |  | 1.0.0 | 监听消息的回调函数 |

## 注意事项
- 主线程中通过 tt.createWorker 创建 worker 实例，并通过 worker.onMessage/postMessage 发送和接收消息
- 在 Worker 线程全局上下文暴露一个 worker 对象，可直接调用 worker.onMessage/postMessage

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/worker/worker-on-message) / [本地体验路径](worker-on-message)
