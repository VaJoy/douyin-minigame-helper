---
title: "发起请求"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/internet/tt-request
update_time: 2025-01-13
---

## TT.Request

> 6.0.0 开始支持本方法，WebGL也支持该方法

发起一个网络请求。网络相关的 API 在使用前需要配置域名白名单。
请参考 https://microapp.bytedance.com/docs/zh-CN/mini-app/develop/guide/basic-ability/network/

| 前提条件 | 网络相关的 API 在使用前需要配置域名白名单，请前往开发者平台「开发 - 开发设置」，添加 request 合法域名 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | header 不支持设置 referer、user-agent 字段。 tt.request 目前只支持 HTTPS 协议的请求 。 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static int Request(
    string url, 
    TTRequest.InnerOptions options, 
    Action<TTRequest.Response> success,
    Action<TTRequest.Response> fail)
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | -- | 是 | 请求地址 |
| options | TTRequest.InnerOptions | -- | 是 | 相关设置 |
| success | Action<TTRequest.Response> | -- | 是 | 请求'成功'的回调 |
| fail | Action<TTRequest.Response> | -- | 是 | 请求失败的回调 |

**TTRequest.InnerOptions的属性如下**

| 属姓名 | 类型 | 说明 |
| --- | --- | --- |
| Method | string | 网络请求方法，支持 GET/POST/OPTIONS/PUT/HEAD/DELETE |
| Data | string | 请求的参数。object / array / ArrayBuffer 类型 |
| Header | JsonData | 请求header |
| DataType | string | 期望返回的数据类型，支持 json、string |
| ResponseType | string | 期望响应的数据类型，支持 text 或 arraybuffer |

**header 参数说明**
**referer**
网络请求 header 中的 referer 不可设置。 其固定格式为：[https://tmaservice.developer.toutiao.com?appid={appid}&version={appVersion}](https://tmaservice.developer.toutiao.com/?appid={appid}&version={appVersion})，其中 appid为小游戏的 APPID，appVersion为小游戏的版本号。
**user-agent**
网络请求 header 中的 user-agent 不可设置。 其固定格式分为：
- IOS 系统：[系统user-agent] [宿主标识]/[宿主app版本] ToutiaoMicroApp/[基础库版本] webview/[插件版本]。
- Android 系统：[系统user-agent] [宿主标识]/[宿主app版本] ToutiaoMicroApp/[基础库版本] PluginVersion/[插件版本]。
**data 参数说明**
传给服务器的数据最终会是 String 类型，如果 data 不是 String 类型，会被转换成 String 。转换规则如下：
1. 如果数据类型是 string 或者是 arraybuffer，则直接返回该数据；
1. 如果 header['content-type'] 是 application/x-www-form-urlencoded，会将数据转换成 query string： encodeURIComponent(k)=encodeURIComponent(v)&encodeURIComponent(k)=encodeURIComponent(v)...，然后返回该数据。
1. 如果 header['content-type'] 是 application/json，则会对数据进行 JSON 序列化，然后返回该数据。
1. 如果数据类型是 object，则会对数据进行 JSON 序列化，然后返回该数据。
1. 如果是其他情况，则直接调用数据的 toString()， 然后返回该数据。
**method 的合法值**

| 属姓名 | 类型 |
| --- | --- |
| GET | GET 请求 |
| OPTIONS | OPTIONS 请求 |
| HEAD | HEAD 请求 |
| POST | POST 请求 |
| PUT | PUT 请求 |
| DELETE | DELETE 请求 |

**回调成功**
TTRequest.Response 类型，可用属性如下：

| **属姓名** | **类型** | **说明** |
| --- | --- | --- |
| statusCode | number | 返回的 HTTP 状态码 |
| header | object | 返回的 HTTP Response Header |
| data | string | 返回的数据，类型取决于 dataType 和 responseType 参数 |
| errMsg | string | "request:ok" |

**回调失败**
TTRequest.Response 类型，可用属性如下：

| **属姓名** | **类型** | **说明** |
| --- | --- | --- |
| statusCode | number | 返回的 HTTP 状态码 |
| errMsg | string | "request:fail " + 详细错误信息 |

### 返回值

| **类型** | **说明** |
| --- | --- |
| int | 任务id，-1为请求失败 |

### 代码示例

```csharp
private void Test() {
    TTRequest.InnerOptions options = new TTRequest.InnerOptions();
    options.Header["content-type"] = "application/json";
    options.Header["cookie"] = "test";
    options.Header["other"] = "test";
    PrintText("Request url:" + url);
    TT.Request("https://www.baidu.com", options, 
            response => { Debug.Log(response); },
            response => { Debug.Log(response); });
}
```
