---
title: "tt.downloadFile"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/network/download/tt-download-file
update_time: 2025-04-01
---

tt.downloadFile(options)

let task = tt.downloadFile({
url: "somefileurl",
success(res) {
if (res.statusCode === 200) {
console.log(`${res.tempFilePath}`);
}
},
fail(res) {
console.log(`downloadFile调用失败`);
},
});

task.onProgressUpdate((res) => {
this.setData({
progress: res.progress,
});

if (someReason) {
task.abort();
}

## 语法

```js
tt.downloadFile(url, header, timeout, enableProfile)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
客户端直接发起一个 HTTPS GET 请求，下载网络文件到本地临时目录。​

## 示例代码
```js
let task = tt.downloadFile({
  url: "somefileurl",
  success(res) {
    if (res.statusCode === 200) {
      console.log(`${res.tempFilePath}`);
    }
  },
  fail(res) {
    console.log(`downloadFile调用失败`);
  },
});

task.onProgressUpdate((res) => {
  this.setData({
    progress: res.progress,
  });
});

if (someReason) {
  task.abort();
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| url | string | 是 |  | 1.0.0 | 文件地址 |
| header | Object | 否 |  | 1.0.0 | 请求 Header  ## referer  请求 header 中的 referer 不可设置。  其固定格式为：[https://tmaservice.developer.toutiao.com?appid={appid}&version={appVersion}](https://tmaservice.developer.toutiao.com/?appid={appid}&version={appVersion})，其中 appid为小游戏的 APPID，appVersion为小游戏的版本号。  ## user-agent  请求 header 中的 user-agent 不可设置。  其固定格式分为：  - IOS 系统：[系统user-agent] [宿主标识]/[宿主app版本] ToutiaoMicroApp/[基础库版本] webview/[插件版本]。 - Android 系统：[系统user-agent] [宿主标识]/[宿主app版本] ToutiaoMicroApp/[基础库版本] PluginVersion/[插件版本]。 |
| timeout | number | 否 |  | 3.83.0 | 接口超时时间，单位为毫秒，不传默认取 game.json 中的 networkTimeout 配置 |
| enableProfile | boolean | 否 | true | 3.83.0 | 是否开启 profile，默认开启。开启后可在接口回调的 res.profile 中查看性能调试信息。PC 未支持该能力，请使用真机调试。 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| DownloadTask | Object | [DownloadTask](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/download/download-task) |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | 回调参数  **对象字段** - **tempFilePath**（string）：文件本地路径，下载的文件会存放在[临时目录](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/tt-get-file-system-manager#_%E7%9B%AE%E5%BD%95%E8%AF%B4%E6%98%8E)中 - **statusCode**（number）：返回 HTTP 状态码 |
| profile | Object | 网络请求过程中一些调试信息  **对象字段** - **domainLookupStart**（number）：DNS 域名查询开始的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 requestStart 值相等 - **domainLookupEnd**（number）：DNS 域名查询完成的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 requestStart 值相等 - **connectStart**（number）：HTTP（TCP） 开始建立连接的时间，如果是持久连接，则与 requestStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接开始的时间 - **connectEnd**（number）：HTTP（TCP） 完成建立连接的时间（完成握手），如果是持久连接，则与 requestStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接完成的时间。注意这里握手结束，包括安全连接建立完成、SOCKS 授权通过 - **sslConnectionStart**（number）：SSL 建立连接的时间，如果不是安全连接，则值为 0 - **sslConnectionEnd**（number）：SSL 建立完成的时间，如果不是安全连接，则值为 0 - **requestStart**（number）：HTTP 请求读取真实文档开始的时间（完成建立连接），包括从本地读取缓存。连接错误重连时，这里显示的也是新建立连接的时间 - **requestEnd**（number）：HTTP 请求读取真实文档结束的时间 - **rtt**（number）：当次请求连接过程中实时 rtt - **estimateNetType**（number）：评估的网络状态 unknown, offline, slow 2g, 2g, 3g, 4g, last/0, 1, 2, 3, 4, 5, 6 - **throughputKbps**（number）：当前网络的实际下载 kbps - **port**（number）：当前请求的端口 - **socketReused**（number）：是否复用连接 - **sentBytesCount**（number）：发送的字节数 - **receivedBytesCount**（number）：收到的字节数 - **responseStart**（number）：HTTP 开始接收响应的时间（获取到第一个字节），包括从本地读取缓存 - **responseEnd**（number）：HTTP 响应全部接收完成的时间（获取到最后一个字节），包括从本地读取缓存 - **peerIP**（string）：当前请求的IP - **protocol**（string）：使用协议类型 - **clientStart**（number）：完整请求开始时本地设备的时间戳（请求任务创建开始计时） - **clientEnd**（number）：完整请求结束时本地设备的时间戳（请求任务创建开始计时） - **networkStart**（number）：仅网络的开始时间戳（发起请求开始计时） - **networkEnd**（number）：仅网络的结束时间戳（发起请求开始计时） - **taskCreate**（number）：创建请求任务时间戳 |

## 回调：失败回调
调用失败时的回调函数

## 使用限制
- header 不支持设置 referer、user-agent 字段。
- 目前 tt.downloadFile 暂不支持多文件下载，一次只能下载一个文件。​

## 注意事项
- ​iOS系统从 2.21.0（包含）版本开始， 单次下载允许的最大文件为 50MB 提升到 200M，安卓侧依然是50MB。​
- 请在服务端响应的 header 中指定合理的 Content-Type 字段，以保证客户端正确处理文件类型。​

## 前置条件
网络相关的 API 在使用前需要配置域名白名单，[详细说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/basic-function/network)。​

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/system/system-information/tt-download-file) / [本地体验路径](tt-download-file)
