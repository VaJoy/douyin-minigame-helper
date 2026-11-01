---
title: "Worker"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/worker/worker
update_time: 2024-07-24
---

Worker 实例，可通过 [tt.createWorker](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/worker/tt-create-worker) 接口获取。
## 属性说明
| 属性名 | 类型 | 说明 |
| ----------------------------------------------------------------------- | -------- | ---------------------------------------------------- |
| [postMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/worker/worker-post-message/) | Function | 向主线程/Worker 线程发送消息 |
| [terminate](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/worker/worker-terminate/) | Function | 结束当前 worker 线程，仅限在主线程 worker 对象上调用 |
| [onMessage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/worker/worker-on-message/) | Function | 监听接收主线程/Worker 线程向当前线程发送的消息 |
