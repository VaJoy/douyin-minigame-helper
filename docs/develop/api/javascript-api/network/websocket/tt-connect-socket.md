---
title: "tt.connectSocket"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/network/websocket/tt-connect-socket
update_time: 2025-04-02
---

let socketTask = tt.connectSocket({
url: "wss://somepath",
protocols: ["p1"],
});

socketTask.onOpen(() => {
console.log("WebSocket 已连接");
});

socketTask.onClose(() => {
console.log("WebSocket 已断开");
});

socketTask.onError((error) => {
console.error("WebSocket 发生错误:", error);
});

socketTask.onMessage((message) => {
console.log("socket message:", message);

let data = message.data;

if (Object.prototype.toString.call(data) === "[object ArrayBuffer]") {
data = Codec.read(data);
}
});

tt.connectSocket(options)

## 语法

```js
tt.connectSocket(url, header, protocols, timeout)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
创建一个 WebSocket 连接实例，并通过返回的[SocketTask](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/websocket/socket-task/socket-task)操作该连接。

## 示例代码
```js
let socketTask = tt.connectSocket({
  url: "wss://somepath",
  protocols: ["p1"],
});

socketTask.onOpen(() => {
  console.log("WebSocket 已连接");
});

socketTask.onClose(() => {
  console.log("WebSocket 已断开");
});

socketTask.onError((error) => {
  console.error("WebSocket 发生错误:", error);
});

socketTask.onMessage((message) => {
  console.log("socket message:", message);

  let data = message.data;

  if (Object.prototype.toString.call(data) === "[object ArrayBuffer]") {
    data = Codec.read(data);
  }
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| url | string | 否 |  | 1.0.0 | Socket 连接地址 |
| header | Object | 否 |  | 1.0.0 | HTTP Header |
| protocols | Array<string> | 否 |  | 1.0.0 | 子协议数组 |
| timeout | number | 否 |  | 3.83.0 | 接口超时时间，单位为毫秒，不传默认取 game.json 中的 networkTimeout 配置 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| SocketTask | string | [SocketTask](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/websocket/socket-task/socket-task)（Socket 任务对象） |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 回调信息 |
| socketTaskId | number | 当前创建的 socketTask 序号 |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |

## 注意事项
- header 不支持设置 referer 字段。
- 在当前小程序页面已经有一个WebSocket 连接的情况下，如果再创建一个WebSocket 连接，会重新创建一个 WebSocket 连接，但是之前创建的WebSocket 连接并不会自动关闭。
- 在使用 send 方法时，参数必须是 object 类型，而具体发送的数据必须在 object 的 data 字段。
- WebSocket 服务器接口地址必须是 wss 协议，且域名必须是后台配置的合法域名。
- 在创建 WebSocket 时，如果参数中 protocols 是非空，请确保 WebSocket 服务器能解析并且返回相应的 protocol，否则会创建 WebSocket 失败。

## 前置条件
网络相关的 API 在使用前需要配置域名白名单，请前往开发者平台「开发 - 开发设置」，添加 socket 合法域名

## 相关课程
[网络请求](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/basic-function/network)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/system/system-information/tt-connect-socket) / [本地体验路径](tt-connect-socket)
