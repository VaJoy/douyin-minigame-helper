---
title: "SocketTask.close"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/network/websocket/socket-task/socket-task-close
update_time: 2024-07-24
---

> 基础库 1.0.0 开始支持本方法。
关闭 WebSocket 连接的方法。
## 语法
```
SocketTask.close(options)
```
## 参数说明
options 为 Object 类型，属性如下：
| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| -------- | -------- | --------- | ---- | -------------------------------------------- | ------------ |
| code | number | 1000/1001 | 否 | 关闭连接状态码 | 1.0.0 |
| reason | string | -- | 否 | 连接被关闭的原因 | 1.0.0 |
| success | function | -- | 否 | 接口调用成功的回调函数 | 1.0.0 |
| fail | function | -- | 否 | 接口调用失败的回调函数 | 1.0.0 |
| complete | function | -- | 否 | 接口调用结束的回调函数（成功、失败都会执行） | 1.0.0 |
code 值说明：
| code 值 | 说明 |
| ------- | -------------------------------- |
| 1000 | 正常关闭 |
| 1001 | 由于处于后台等异常原因导致的关闭 |
## 回调成功
Object 类型，属性如下：
| 参数 | 参数类型 | 说明 | 最低支持版本 |
| ------ | -------- | -------- | ------------ |
| errMsg | string | 回调信息 | 1.0.0 |
## 回调失败
Object 类型，属性如下：
| 参数 | 参数类型 | 说明 | 最低支持版本 |
| ------ | -------- | -------- | ------------ |
| errMsg | string | 回调信息 | 1.0.0 |
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
socketTask.onClose(() => {
console.log("WebSocket 已断开");
});
setTimeout(() => {
socketTask.close({
code: 1001,
reason: "close",
success: (res) => {
// 关闭成功的回调
console.log("close success", res);
},
fail: (res) => {
// 关闭失败的回调
console.log("close fail", res);
},
});
}, 1000);
```
## Bug & Tip
- Tip：WebSocket 服务器接口地址必须是 `wss` 协议，且域名必须是后台配置的合法域名。
