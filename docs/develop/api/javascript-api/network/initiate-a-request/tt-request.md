---
title: "tt.request"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/network/initiate-a-request/tt-request
update_time: 2024-07-24
---

## 语法

```js
tt.request(url, header, method, data, dataType, responseType, timeout, enableProfile, redirect, enableCache)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
发起一个网络请求。

## 示例代码

【代码示例 1】：post 请求返回 dataType 为 json 类型的数据，并且可能会中断请求。

```js
let task = tt.request({
  url: "someurl",
  data: {
    user_name: "hello",
  },
  header: {
    "content-type": "application/json",
  },
  method: "POST",
  dataType: "JSON", // 指定返回数据的类型为 json
  responseType: "text",
  success(res) {
    console.log("调用成功", res.data)
  },
  fail(res) {
    console.log("调用失败", res.errMsg)
  },
})

// 某些条件下中断请求
if (someReason) {
  task.abort()
}
```

【代码示例 2】：post 请求返回 dataType 为 string 类型的数据。

```js
tt.request({
  url: "someurl",
  data: {
    user_name: "hello",
  },
  header: {
    "content-type": "application/json",
  },
  method: "POST",
  dataType: "string", // 指定返回数据的类型为 string
  responseType: "text",
  success(res) {
    console.log("调用成功", res.data)
  },
  fail(res) {
    console.log("调用失败", res.errMsg)
  },
})
```

【代码示例 3】：post 请求返回 responseType 为 arraybuffer 类型的数据。

```js
tt.request({
  url: "someurl",
  data: {
    user_name: "hello",
  },
  header: {
    "content-type": "application/json",
  },
  method: "POST",
  dataType: "string", // 在 responseType 为arraybuffer的情况下，不起作用
  responseType: "arraybuffer", // 指定返回数据的类型为 arraybuffer
  success(res) {
    // 此处返回的res.data类型为 arraybuffer
    console.log("调用成功", res.data)
  },
  fail(res) {
    console.log("调用失败", res.errMsg)
  },
})
```

【代码示例 4】：post 请求 header['content-type'] 为 application/x-www-form-urlencoded。

```js
tt.request({
  url: "someurl",
  data: {
    user_name: "hello",
  },
  header: {
    "content-type": "application/x-www-form-urlencoded", // 此处指定content-type类型
  },
  method: "POST",
  dataType: "json",
  responseType: "text",
  success(res) {
    console.log("调用成功", res.data)
  },
  fail(res) {
    console.log("调用失败", res.errMsg)
  },
})
```

【代码示例 5】：post 请求携带 cookie。

```js
const id = ""
tt.request({
  url: "someurl",
  data: {
    user_name: "hello",
  },
  header: {
    "content-type": "application/json",
    cookie: "TOUTIAOID" + id, // 此处添加cookie
  },
  method: "POST",
  dataType: "json",
  responseType: "text",
  success(res) {
    console.log("调用成功", res.data)
  },
  fail(res) {
    console.log("调用失败", res.errMsg)
  },
})
```

【代码示例 6】：put 请求。

```js
tt.request({
  url: "someurl",
  data: {
    user_name: "hello",
  },
  header: {
    "content-type": "application/json",
  },
  method: "PUT", // 此处修改请求方法
  dataType: "json",
  responseType: "text",
  success(res) {
    console.log("调用成功", res.data)
  },
  fail(res) {
    console.log("调用失败", res.errMsg)
  },
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| url | string | 是 |  | 1.0.0 | 请求地址 |
| header | Object | 否 | {"content-type": "application/json"} | 1.0.0 | 请求 Header  #### **referer**  网络请求 header 中的 referer 不可设置。 其固定格式为：https://tmaservice.developer.toutiao.com?appid={appid}&version={appVersion}，其中 appid为小游戏的 APPID，appVersion为小游戏的版本号。  #### **user-agent**  网络请求 header 中的 user-agent 不可设置。 其固定格式分为：  - IOS 系统：[系统user-agent] [宿主标识]/[宿主app版本] ToutiaoMicroApp/[基础库版本] webview/[插件版本]。 - Android 系统：[系统user-agent] [宿主标识]/[宿主app版本] ToutiaoMicroApp/[基础库版本] PluginVersion/[插件版本]。 |
| method | number | 否 | GET | 1.0.0 | 网络请求方法  **可选值：** GET=

GET 请求

；OPTIONS=

OPTIONS 请求

；HEAD=

HEAD 请求

；POST=

POST 请求

；PUT=

PUT 请求

；DELETE=

DELETE 请求

 |
| data | Object | 是 |  | 1.0.0 | 请求的参数。object / array / ArrayBuffer 类型  传给服务器的数据最终会是 String 类型，如果 data 不是 String 类型，会被转换成 String 。转换规则如下：  1. 如果数据类型是 string 或者是 arraybuffer，则直接返回该数据； 2. 如果 header['content-type'] 是 application/x-www-form-urlencoded，会将数据转换成 query string： encodeURIComponent(k)=encodeURIComponent(v)&encodeURIComponent(k)=encodeURIComponent(v)...，然后返回该数据。 3. 如果 header['content-type'] 是 application/json，则会对数据进行 JSON 序列化，然后返回该数据。 4. 如果数据类型是 object，则会对数据进行 JSON 序列化，然后返回该数据。 5. 如果是其他情况，则直接调用数据的 toString()， 然后返回该数据。 |
| dataType | string | 否 | json | 1.0.0 | 期望返回的数据类型，支持 json、string |
| responseType | string | 否 | text | 1.0.0 | 期望响应的数据类型，支持 text 或 arraybuffer |
| timeout | number | 否 |  | 3.83.0 | 接口超时时间，单位为毫秒，不传默认取 game.json 中的 networkTimeout 配置 |
| enableProfile | boolean | 否 | true | 3.83.0 | 是否开启 profile，默认开启。开启后可在接口回调的 res.profile 中查看性能调试信息。IDE 未支持该能力，请使用真机调试。 |
| redirect | number | 否 | follow | 3.83.0 | 重定向拦截策略  **可选值：** follow=

不拦截重定向，即客户端自动处理重定向

；manual=

拦截重定向。开启后，当 http 状态码为 3xx 时客户端不再自动重定向，而是触发 onHeadersReceived 回调，并结束本次 request 请求。

 |
| enableCache | boolean | 否 | false | 3.83.0 | 开启 HTTP 缓存 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| RequestTask | Object | [RequestTask](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/initiate-a-request/request-task)(网络请求任务对象)，调用 tt.request 后返回的请求对象。 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| input | Object | 参数为 Object 类型，属性如下：  **对象字段** - **statusCode**（number）：返回的 HTTP 状态码 - **header**（Object）：返回的 HTTP Response Header - **data**（string）：返回的数据，类型取决于 dataType 和 responseType 参数 - **errMsg**（string）："request:ok" |
| profile | Object | 网络请求过程中一些调试信息  **对象字段** - **domainLookupStart**（number）：DNS 域名查询开始的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 requestStart 值相等 - **domainLookupEnd**（number）：DNS 域名查询完成的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 requestStart 值相等 - **connectStart**（number）：HTTP（TCP） 开始建立连接的时间，如果是持久连接，则与 requestStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接开始的时间 - **connectEnd**（number）：HTTP（TCP） 完成建立连接的时间（完成握手），如果是持久连接，则与 requestStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接完成的时间。注意这里握手结束，包括安全连接建立完成、SOCKS 授权通过 - **sslConnectionStart**（number）：SSL 建立连接的时间，如果不是安全连接，则值为 0 - **sslConnectionEnd**（number）：SSL 建立完成的时间，如果不是安全连接，则值为 0 - **requestStart**（number）：HTTP 请求读取真实文档开始的时间（完成建立连接），包括从本地读取缓存。连接错误重连时，这里显示的也是新建立连接的时间 - **requestEnd**（number）：HTTP 请求读取真实文档结束的时间 - **rtt**（number）：当次请求连接过程中实时 rtt - **estimateNetType**（number）：评估的网络状态 unknown, offline, slow 2g, 2g, 3g, 4g, last/0, 1, 2, 3, 4, 5, 6 - **throughputKbps**（number）：当前网络的实际下载 kbps - **port**（number）：当前请求的端口 |
| socketReused | boolean | 是否复用连接 |
| sentBytesCount | number | 发送的字节数 |
| receivedBytesCount | number | 收到的字节数 |
| responseStart | number | HTTP 开始接收响应的时间（获取到第一个字节），包括从本地读取缓存 |
| responseEnd | number | HTTP 响应全部接收完成的时间（获取到最后一个字节），包括从本地读取缓存 |
| peerIP | string | 当前请求的IP |
| protocol | string | 使用协议类型 |
| clientStart | number | 完整请求开始时本地设备的时间戳（请求任务创建开始计时） |
| clientEnd | number | 完整请求结束时本地设备的时间戳（请求任务创建开始计时） |
| networkStart | number | 仅网络的开始时间戳（发起请求开始计时） |
| networkEnd | number | 仅网络的结束时间戳（发起请求开始计时） |
| taskCreate | number | 创建请求任务时间戳 |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| input | Object | 参数为 Object 类型，属性如下：  **对象字段** - **errMsg**（string）："request:fail " + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 10401 | internal error |  |  |
| 10402 | internal error |  |  |
| 21100 | url not in domain list, url == %s |  |  |
| 21100 | url is invalid, url == %s |  |  |
| 21102 | invoke permission denied |  |  |
| 20000 | no requestTaskId |  |  |
| 20000 | abort |  |  |
| 20000 | params $paramName type is not $paramType type |  |  |
| 21000 | url is not valid domain, url == $url |  |  |
| 20000 | internal error |  |  |
| 10501 | app in background |  |  |
| 21101 | abort |  |  |
| 20000 | url is not valid domain, url == $url |  |  |

## 使用限制
- header 不支持设置 referer、user-agent 字段。
- tt.request 目前只支持 HTTPS 协议的请求 。

## 前置条件
网络相关的 API 在使用前需要配置域名白名单，请前往开发者平台「开发 - 开发设置」，添加 request 合法域名

## 相关课程
[网络请求](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/framework/basic-function/network)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/network/initiate-a-request/tt-request) / [本地体验路径](tt-request)