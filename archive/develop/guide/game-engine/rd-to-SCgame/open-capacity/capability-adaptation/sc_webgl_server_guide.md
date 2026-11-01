---
title: "后端服务指引"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_server_guide
update_time: 2024-07-24
---

> 此文档描述小游戏开发时后端服务的问题
> 更多详情见[Unity WebGL 抖音小游戏适配方案](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/sc_webgl_overall)

字节小游戏对后端服务无任何限制，可以根据自身需求选择，比如：
1. 自建后端：支持 WebSocket、HTTP 通信（Natvie方案下可使用TCP/UDP）
1. 云开发：云开发可以降低运维、研发成本，详见[抖音云开发](https://developer.open-douyin.com/docs/resource/zh-CN/developer/tools/cloud/introduction/summary)
也可以两种模式混合开发
## 自建服务端开发
参考抖音开放平台[服务端开发](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/server-api-introduction)
## 抖音云开发
[抖音云托管](https://cloud.douyin.com/)是服务于抖音开放生态的云托管服务，为应用（小程序、小游戏、小玩法）开发者提供后端服务的开发、部署、运行、监控、运维的一站式开发体验。
抖音云托管致力于帮助开发者，打造出稳定性高，安全性强的后端服务。
### 快速部署
参考开放平台[快速部署](https://developer.open-douyin.com/docs/resource/zh-CN/developer/tools/cloud/quick-start/quick-start-deploy)
### 客户端使用
StarkSDK抖音云相关接口介绍：[SC小游戏抖音云接口文档](https://bytedance.feishu.cn/docx/JICFduZpgolEkzxZbEucBqzRnxd)
已部署服务器：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/c11fb12921ce498aa73257b60f237bfe)

提供接口：api/getinfo（测试接口，会透传客户端上报字段）

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/046193e257f54ee293c242c29a824524)

客户端接口调用：

```csharp
/// <summary>
/// 抖音云接口测试 
/// </summary>
private void TestDyCloudGetRequest()
{
    StarkDouyinCloud.Options options = new StarkDouyinCloud.Options();
    options.Header = new JsonData();
    options.Header["my_header"] = "test_header";
    options.Method = "GET";
    StarkSDK.API.GetStarkDouyinCloudManager().CallContainer(DY_CLOUD_EVN_ID, DY_CLOUD_SERVICE_ID,
        "/api/getinfo?test_text=abcd",
        options,
        response =>
        {
            Debug.Log($"CallContainer: /api/getinfo response.StatusCode:{response.StatusCode},response.Data:{response.Data}");
        },
        response =>
        {
            Debug.Log($"CallContainer: /api/getinfo response.StatusCode:{response.StatusCode},response.ErrMsg:{response.ErrMsg}");
        });
}
```

对象存储数据库：

```csharp
StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDBCollection(DY_CLOUD_EVN_ID, DY_CLOYD_DB_NAME)
    .Doc(DyCloudTestDocId).Get(
        response =>
        {
            Debug.Log(
                $"TestDbDocGet Doc get response.StatusCode:{response.StatusCode}, response.ErrMsg:{response.ErrMsg}, response.Data:{response.Data.ToJson()}");
        },
        response =>
        {
            Debug.Log(
                $"TestDbDocGet failed response.StatusCode:{response.StatusCode},response.ErrMsg:{response.ErrMsg}");
        });
```
