---
title: "UploadTask.offProgressUpdate"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/network/onload/upload-task-dir/uploadtask-progress
update_time: 2025-09-11
---

> 基础库 2.1.0 开始支持，低版本需做[兼容处理](../../../guide/runtime/client-lib/compatibility.html)。
> 相关文档: [网络使用说明](../../../guide/base-ability/network.html)、[局域网通信]((mDNS))
## 功能描述
移除上传进度变化事件的监听函数
### 参数
#### function listener
onProgressUpdate 传入的监听函数。不传此参数则移除所有监听函数。
### 示例代码

```text
const listener = function (res) { console.log(res) }

UploadTask.onProgressUpdate(listener)
UploadTask.offProgressUpdate(listener) // 需传入与监听时同一个的函数对象
```
