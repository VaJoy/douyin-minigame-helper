---
title: "tt.uploadFile"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/network/onload/tt-upload-file
update_time: 2024-09-03
---

## 语法

```js
tt.uploadFile(url, filePath, name, header, formData, timeout, enableProfile)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
将本地文件上传到网络。客户端将发起一个 HTTPS POST 请求，其中 content-type 为 multipart/form-data。

## 示例代码
```js
let task = tt.uploadFile({
  url: "someuploadurl",
  filePath: tempFilePath,
  name: "file",
  success(res) {
    if (res.statusCode === 200) {
      console.log(`uploadFile调用成功 ${res.data}`);
    }
  },
  fail(res) {
    console.log(`uploadFile调用失败`);
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
| url | string | 是 |  | 1.0.0 | 目标地址 |
| filePath | string | 是 |  | 1.0.0 | 本地文件路径 |
| name | string | 是 |  | 1.0.0 | HTTP 请求的文件名 |
| header | Object | 是 | {"content-type": "multipart/form-data"} | 1.0.0 | 请求 Header ，不能设置 referer 和 user-agent  ### referer 说明  网络请求 header 中的 referer 不可设置。 其固定格式为：https://tmaservice.developer.toutiao.com?appid={appid}&version={appVersion}，其中 appid 为小游戏的 APPID，appVersion 为小游戏的版本号。  ### user-agent 说明  网络请求 header 中的 user-agent 不可设置。 其固定格式分为：  - IOS 系统：[系统user-agent] [宿主标识]/[宿主app版本] ToutiaoMicroApp/[基础库版本] webview/[插件版本]。 - Android 系统：[系统user-agent] [宿主标识]/[宿主app版本] ToutiaoMicroApp/[基础库版本] PluginVersion/[插件版本]。 |
| formData | Object | 是 |  | 1.0.0 | 请求额外参数 |
| timeout | number | 否 |  | 3.83.0 | 接口超时时间，单位为毫秒，不传默认取 game.json 中的 networkTimeout 配置 |
| enableProfile | boolean | 否 | true | 3.83.0 | 是否开启 profile，默认开启。开启后可在接口回调的 res.profile 中查看性能调试信息。PC 未支持该能力，请使用真机调试。 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| UploadTask | Object | [UploadTask](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/network/onload/upload-task) 实例（上传任务对象） |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **statusCode**（number）：返回 HTTP 状态码 - **data**（string）：返回数据 - **errMsg**（string）："uploadFile:ok" |
| profile | Object | 网络请求过程中一些调试信息  **对象字段** - **domainLookupStart**（number）：DNS 域名查询开始的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 requestStart 值相等 - **domainLookupEnd**（number）：DNS 域名查询完成的时间，如果使用了本地缓存（即无 DNS 查询）或持久连接，则与 requestStart 值相等 - **connectStart**（number）：HTTP（TCP） 开始建立连接的时间，如果是持久连接，则与 requestStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接开始的时间 - **connectEnd**（number）：HTTP（TCP） 完成建立连接的时间（完成握手），如果是持久连接，则与 requestStart 值相等。注意如果在传输层发生了错误且重新建立连接，则这里显示的是新建立的连接完成的时间。注意这里握手结束，包括安全连接建立完成、SOCKS 授权通过 - **sslConnectionStart**（number）：SSL 建立连接的时间，如果不是安全连接，则值为 0 - **sslConnectionEnd**（number）：SSL 建立完成的时间，如果不是安全连接，则值为 0 - **requestStart**（number）：HTTP 请求读取真实文档开始的时间（完成建立连接），包括从本地读取缓存。连接错误重连时，这里显示的也是新建立连接的时间 - **requestEnd**（number）：HTTP 请求读取真实文档结束的时间 - **rtt**（number）：当次请求连接过程中实时 rtt - **estimateNetType**（number）：评估的网络状态 unknown, offline, slow 2g, 2g, 3g, 4g, last/0, 1, 2, 3, 4, 5, 6 - **throughputKbps**（number）：当前网络的实际下载 kbps - **port**（number）：当前请求的端口 - **socketReused**（number）：是否复用连接 - **sentBytesCount**（number）：发送的字节数 - **receivedBytesCount**（number）：收到的字节数 - **responseStart**（number）：HTTP 开始接收响应的时间（获取到第一个字节），包括从本地读取缓存 - **responseEnd**（number）：HTTP 响应全部接收完成的时间（获取到最后一个字节），包括从本地读取缓存 - **peerIP**（string）：当前请求的IP - **protocol**（string）：使用协议类型 - **clientStart**（number）：完整请求开始时本地设备的时间戳（请求任务创建开始计时） - **clientEnd**（number）：完整请求结束时本地设备的时间戳（请求任务创建开始计时） - **networkStart**（number）：仅网络的开始时间戳（发起请求开始计时） - **networkEnd**（number）：仅网络的结束时间戳（发起请求开始计时） - **taskCreate**（number）：创建请求任务时间戳 |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："uploadFile:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21100 | url is not valid domain, url == %s |  |  |
| 21100 | url is invalid, url == %s |  |  |
| 21102 | no file exist, filePath == %s |  |  |
| 21101 | permission denied, open |  |  |
| 20000 | abort |  |  |
| 20000 | no uploadTaskId |  |  |
| 20000 | internal error |  |  |
| 20000 | $paramName is invalid |  |  |
| 10501 | app in background |  |  |
| 20000 | filePath is illegal |  |  |
| 21000 | file is empty |  |  |
| 21000 | url is not valid domain, url == $url |  |  |
| 20000 | url is not valid domain, url == $url |  |  |

## 使用限制
- header 不支持设置 referer 、user-agent、content-type 字段字段。
- 目前 tt.uploadFile 上传文件大小限制为 10M。
- 目前 tt.uploadFile 暂不支持多文件上传，一次只能上传一个文件。

## 前置条件
网络相关的 API 在使用前需要配置域名白名单，请前往开发者平台「开发 - 开发设置」，添加 uploadFile 合法域名

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/system/system-information/tt-upload-file) / [本地体验路径](tt-upload-file)
