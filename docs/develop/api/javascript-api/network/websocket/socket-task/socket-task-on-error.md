---
title: "SocketTask.onError"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/network/websocket/socket-task/socket-task-on-error
update_time: 2024-07-24
---

> 基础库 1.0.0 开始支持本方法。
监听 WebSocket 发生错误的事件。
## 语法
```
SocketTask.onError(callback)
```
## 参数说明
参数为回调函数：
| 参数 | 参数类型 | 说明 | 最低支持版本 |
| -------- | -------- | ---------------------- | ------------ |
| callback | function | 连接发生错误的事件回调 | 1.0.0 |
回调函数的参数为 Object 类型，属性如下：
| 参数 | 参数类型 | 说明 | 最低支持版本 |
| ------ | -------- | -------- | ------------ |
| errMsg | string | 错误信息 | 1.0.0 |
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
socketTask.onError((error) => {
console.error("WebSocket 发生错误:", error);
});
```
## Bug & Tip
- Tip：WebSocket 服务器接口地址必须是 `wss` 协议，且域名必须是后台配置的合法域名。
