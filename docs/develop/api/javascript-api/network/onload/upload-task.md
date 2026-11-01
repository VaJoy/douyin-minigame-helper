---
title: "UploadTask"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/network/onload/upload-task
update_time: 2025-09-11
---

> 基础库 1.0.0 开始支持
通过 [tt.uploadFile](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/onload/tt-upload-file) 得到的网络请求任务对象。
## 方法
### UploadTask.abort()
中断上传任务
### UploadTask.onProgressUpdate(callback)
监听上传任务状态变化，`onProgressUpdate`注册的监听方法会收到一个`object`类型参数，该参数的属性值有：

| 名称 | 数据类型 | 描述 |
| --- | --- | --- |
| progress | number | 上传进度 |
| totalBytesSent | number | 已经上传的数据长度，单位`byte` |
| totalBytesExpectedToSend | number | 预期需要上传的数据总长度，单位`byte` |

### UploadTask.onHeadersReceived(callback)
监听 HTTP Response Header 事件。会比请求完成事件更早。
回调的 Object：

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| header | Object | 开发者服务器返回的 HTTP Response Header |

### UploadTask.offHeadersReceived(callback)
移除 HTTP Response Header 事件的监听函数。
callback 为 onHeadersReceived 传入的监听函数，不传此参数则移除所有监听函数。
