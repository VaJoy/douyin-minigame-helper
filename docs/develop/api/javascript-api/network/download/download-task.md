---
title: "DownloadTask"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/network/download/download-task
update_time: 2025-09-11
---

> 基础库版本 1.0.0 开始支持
通过 [tt.downloadFile](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/download/tt-download-file) 得到的网络请求任务
## 方法
### DownloadTask.abort()
中断下载任务
### DownloadTask.onProgressUpdate(callback)
监听下载任务，`onProgressUpdate`注册的监听方法会收到一个`object`类型参数，该参数的属性值有：

| 名称 | 数据类型 | 描述 |
| --- | --- | --- |
| progress | number | 下载进度 |
| totalBytesWritten | number | 已经下载的数据长度，单位 byte |
| totalBytesExpectedToWrite | number | 预期需要下载的数据总长度，单位 byte |

### DownloadTask.onHeadersReceived(callback)
监听 HTTP Response Header 事件。会比请求完成事件更早。
回调的 Object：

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| header | Object | 开发者服务器返回的 HTTP Response Header |

### DownloadTask.offHeadersReceived(callback)
移除 HTTP Response Header 事件的监听函数。
onHeadersReceived 传入的监听函数。不传此参数则移除所有监听函数。
