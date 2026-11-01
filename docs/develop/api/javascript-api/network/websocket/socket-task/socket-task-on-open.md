---
title: "SocketTask.onOpen"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/network/websocket/socket-task/socket-task-on-open
update_time: 2024-07-24
---

> 基础库 1.0.0 开始支持本方法。
监听 WebSocket 连接服务器成功的事件。
表示 WebSocket 的状态变成 open，可以发送数据给服务器。
## 语法
```
SocketTask.onOpen(callback)
```
## 参数说明
参数为回调函数：
| 参数 | 参数类型 | 说明 | 最低支持版本 |
| -------- | -------- | ------------------ | ------------ |
| callback | function | 连接成功的事件回调 | 1.0.0 |
回调函数的参数为 Object 类型，属性如下：
| 参数 | 参数类型 | 说明 | 最低支持版本 |
| ------------ | --------------------- | -------------------------------- | ------------ |
| header | object | 连接服务器返回的 Response Header | 1.0.0 |
| protocolType | string | 使用的网络传输层协议 | 1.0.0 |
| socketType | "ttnet" / "tradition" | websocket 类型 | 1.0.0 |
## 代码示例
```js
const socketTask = tt.connectSocket({
url: "wss://someurl",
success: (res) => {
console.log("创建成功", res);
},
fail: (res) => {
console.log("创建失败", res);
},
});
socketTask.onOpen((res) => {
// 表示连接准备好，可以发送数据了。
console.log("WebSocket 已连接", res);
});
```
## Bug & Tip
- Tip：WebSocket 服务器接口地址必须是 `wss` 协议，且域名必须是后台配置的合法域名。
