---
title: "多线程 Worker"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/basic-function/multi-thread
update_time: 2025-09-11
---

## 步骤
### 配置Worker信息

```js
{
  "deviceOrientation": "portrait",
  "workers": "workers"
}
```

### 添加 Worker 文件

```js
touch workers/request/index.js
touch workers/request/utils.js
touch workers/response/index.js
```

### 编写 Worker 代码

```js
// worker线程中，无法访问tt全局对象
function fibonacci(n) {
  console.log("worker show")
}

worker.onMessage(function (res) {
   console.log(`worker start`);
});
```

### 在主线程中初始化线程

```go
// 创建 Worker
const worker = tt.createWorker('workers/calculator.js');
```

### 在主线程中发送信息给worker

```go
// 向 Worker 发送消息，开始计算
worker.postMessage({
  type: 'calculate',
  payload: 40
});
```

## 分包预加载与worker能力的配合

> 确保在完成一个 Worker 能力后，先关闭该 Worker，再于分包或主线程中启动其他 Worker 能力

worker能力详情请查看[worker实例](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/worker/worker)
分包预加载 详情请查看[分包加载](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/subpackages/LoadSubpackageTask)

在并行执行的任务中，小游戏会静默加载分包预加载任务

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/918043c179a544aea04a00608adaebd4~tplv-9nona0m7ha-image.image)

## 开发常见问题
1. 在某个 Worker 完成任务后，需要手动将线程关闭，调用 Worker.terminate 方法
1. 分包之间的worker线程遵循同一原则，必须关闭上一个worker线程，才能开启下一个worker
## Tips
1. Worker线程数量有且只有一个，而且需要在根目录声明并创建game.json,显式声明workers字段
1. Worker目录中，不能调用tt系列的 API
1. Workers 之间不支持发送消息
1. Worker 目录内只支持放置 JS 文件，其他类型的静态文件需要放在 Worker 目录外
1. Worker 的入口文件在调用 [tt.createWorker](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/worker/tt-create-worker) 时指定，开发者可动态指定 Worker 入口文件
1. Worker 线程是一个独立的运行环境，它无法访问主线程中的 tt 全局对象，分包加载必须在主线程中完成

{
"workers": "workers"
}

var worker = wx.createWorker('workers/request/index.js') // 文件名指定 worker 的入口文件路径，绝对路径

var utils = require('./utils')

// 在 Worker 线程执行上下文会全局暴露一个 `worker` 对象，直接调用 worker.onMessage/postMessage 即可
worker.onMessage(function (res) {
console.log(res)
})

const worker = tt.createWorker('workers/request/index.js')

worker.postMessage({
msg: 'hello worker'
})

{
"workers": {
"path": "workers",
"isSubpackage": true  // true 表示把 worker 打包为分包。默认 false。填 false 时等同于 { "workers": "workers" }
}

var task = wx.preDownloadSubpackage({
packageType: "workers",
success(res) {
console.log("load worker success", res)
var worker = wx.createWorker("workers/request/index.js")   // 创建 worker。 如果 worker 分包没下载完就调 createWorker 的话将报错
},
fail(res) {
console.log("load worker fail", res)
}
})

task.onProgressUpdate(res => {
console.log(res.progress) // 可通过 onProgressUpdate 接口监听下载进度
console.log(res.totalBytesWritten)
console.log(res.totalBytesExpectedToWrite)
})

const utils = require('./utils')

ttworker.onMessage((res) => {
console.log('Received:', res)
*// 处理逻辑... *
})

workers/request/index.js
workers/request/utils.js
workers/response/index.js

{
"workers": {
"path": "workers",
"isSubpackage": true*// 设为true表示打包为分包 *
}

├── game.js
├── game.json
├── project.config.json
└── workers
├── request
│ ├── index.js
│ └── utils.js
└── response
└── index.jsÏ

├── game.js
├── game.json
├── project.config.json
└── workers
├── request
│   ├── index.js
│   └── utils.js
└── response
└── index.js
