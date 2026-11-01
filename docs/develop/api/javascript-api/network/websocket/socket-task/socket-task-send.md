---
title: "SocketTask.send"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/network/websocket/socket-task/socket-task-send
update_time: 2024-07-24
---

通过 WebSocket 连接发送数据。
## 语法
```
SocketTask.send(options)
```
## 参数说明
`options` 是 object 类型，属性如下：
| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| -------- | ------------------ | ------ | ---- | ------------------------------------------------ |
| data | string/ArrayBuffer | | 是 | 需要发送的内容 |
| success | Function | | 否 | 接口调用成功的回调函数 |
| fail | Function | | 否 | 接口调用失败的回调函数 |
| complete | Function | | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |
## 回调成功
object 类型，属性如下：
| 属性 | 类型 | 说明 | 最低支持版本 |
| ------ | ------ | -------------------- | ------------ |
| errMsg | string | "SocketTask.send:ok" | 1.0.0 |
## 回调失败
object 类型，属性如下：
| 属性 | 类型 | 说明 | 最低支持版本 |
| ------ | ------ | --------------------------------- | ------------ |
| errMsg | string | "SocketTask.send:fail" + 错误信息 | 1.0.0 |
## 代码示例
```js
const socketHandler = tt.connectSocket({
url: "wss://somepath",
success: (res) => {
console.log("connectSocket success", res.socketTaskId);
},
fail: (err) => {
console.log("connectSocket fail", err);
},
});
socketHandler.onOpen(function () {
socketHandler.send({
data: "hello world",
success: (res) => {
console.log("Socket发送数据成功", res);
},
fail: (err) => {
console.log("Socket发送数据失败", err);
},
});
});
```
## Bug&Tip
- Tip : 开发者在使用 send 发送数据时，注意只支持 string 和 ArrayBuffer。不要使用 TyepArray，例如 Uint8Array 类型。
