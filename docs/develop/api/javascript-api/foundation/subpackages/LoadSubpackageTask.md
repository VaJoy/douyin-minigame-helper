---
title: "LoadSubpackageTask"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/subpackages/LoadSubpackageTask
update_time: 2024-07-24
---

> 基础库 1.88.0 开始支持本方法，低版本需做[兼容处理](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/basic-library/compatibility-description/)。
通过 [tt.loadSubpackage](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/subpackages/tt-loadsubpackage) 得到的加载分包任务实例，用于获取分包加载状态。
## 方法
### LoadSubpackageTask.onProgressUpdate(callback)
监听分包加载进度变化事件
#### 参数说明
参数为回调函数：

| 参数 | 参数类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| callback | function | 分包加载进度变化事件的回调函数 | 1.88.0 |

回调函数的参数为 Object 类型，属性如下：

| 参数 | 参数类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| progress | number | 分包下载进度百分比 | 1.88.0 |
| totalBytesWritten | number | 已经下载的数据长度，单位 Bytes | 1.88.0 |
| totalBytesExpectedToWrite | number | 预期需要下载的数据总长度，单位 Bytes | 1.88.0 |

## Bug & Tip
无
