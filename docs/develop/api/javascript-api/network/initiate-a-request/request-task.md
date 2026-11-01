---
title: "RequestTask"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/network/initiate-a-request/request-task
update_time: 2025-09-11
---

网络请求任务对象
## 方法
### RequestTask.abort()
中断请求任务

### RequestTask.onHeadersReceived(callback)
监听 HTTP Response Header 事件，会比请求完成事件更早，PC 暂不支持。
回调的 Object：

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| header | Object | 开发者服务器返回的 HTTP Response Header |
| statusCode | Number | 开发者服务器返回的 HTTP 状态码 |
| cookies | Array<string> | 开发者服务器返回的 cookies，格式为字符串数组 |

### RequestTask.onHeadersReceived(callback)
移除 HTTP Response Header 事件的监听函数。
callback 为 onHeadersReceived 传入的监听函数，不传此参数则移除所有监听函数。
##
