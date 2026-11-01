---
title: "SocketTask"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/network/websocket/socket-task/socket-task
update_time: 2024-07-24
---

WebSocket 任务，通过 [tt.connectSocket](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/websocket/tt-connect-socket) 接口创建返回。
## 属性说明
| 属性名 | 类型 | 说明 |
| -------------------- | -------- | ------------------------------------- |
| SocketTask.send | function | 通过 WebSocket 连接发送数据 |
| SocketTask.close | function | 关闭 WebSocket 连接 |
| SocketTask.onOpen | function | 监听 WebSocket 连接打开事件 |
| SocketTask.onClose | function | 监听 WebSocket 连接关闭事件 |
| SocketTask.onError | function | 监听 WebSocket 错误事件 |
| SocketTask.onMessage | function | 监听 WebSocket 接受到服务器的消息事件 |
