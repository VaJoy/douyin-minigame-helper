---
title: "SocketTask.onClose"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/network/websocket/socket-task/socket-task-on-close
update_time: 2025-11-14
---

> 基础库 1.0.0 开始支持本方法。
监听 WebSocket 与服务器连接断开的事件。
## 语法

```text
SocketTask.onClose(callback)
```

## 参数说明
参数为回调函数：

| 参数 | 参数类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| callback | Function | 连接成功的事件回调 | 1.0.0 |

回调函数的参数为 object 类型，属性如下：

| 参数 | 参数类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| protocolType | string | 使用的网络传输层协议 | 1.0.0 |
| socketType | string | websocket 类型 | 1.0.0 |
| errMsg | string | 错误信息 | 1.0.0 |
| reason | string | 关闭原因 | 1.81.0 |
| code | number | 关闭的状态码 | 1.81.0 |

## 返回值
无
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

socketTask.onClose((res) => {
  // WebSocket连接已经断开
  console.log("WebSocket 已断开", res);
});

setTimeout(() => {
  socketTask.close();
}, 1000);
```

## Bug & Tip
- Tip：WebSocket 服务器接口地址必须是 `wss` 协议，且域名必须是后台配置的合法域名。
- Bug: IDE 目前没有返回 `protocolType` 和 `socketType` 字段。
