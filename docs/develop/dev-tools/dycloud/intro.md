---
title: "抖音云"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/dev-tools/dycloud/intro
update_time: 2024-07-24
---

## 一、抖音云介绍
[抖音云托管](https://cloud.douyin.com/?from=doc-minigame)是服务于抖音开放生态的云托管服务，为应用（小程序、小游戏、小玩法）开发者提供后端服务的开发、部署、运行、监控、运维的一站式开发体验。

抖音云托管致力于帮助开发者，打造出稳定性高，安全性强的后端服务。同时，云托管可以帮助你降低开发门槛，提供一站式开发体验。与抖音生态结合，支持 免登录、云调用、抖音回调（内网专线） 等众多优势特性。

前往[抖音云控制台](https://cloud.douyin.com/?from=doc-minigame)上手体验，查看[抖音云文档](https://developer.open-douyin.com/docs/resource/zh-CN/developer/tools/cloud/introduction/summary)。
## 二、使用场景
### 场景1：一行代码实现将 游戏进度 进行云端存档，杜绝用户投诉
问题：游戏进度存档在客户端本地，在用户切换账号后，客户端缓存清空导致游戏进度丢失，引发用户投诉。
解决方案：通过抖音云提供的小游戏SDK进行云端存档，详情可查看：[小游戏如何使用云数据库存储用户游戏进度](https://developer.open-douyin.com/docs/resource/zh-CN/developer/tools/cloud/scene/deploy/mini-game-how-to-use-cloud)

```js
db.collection("game-progress").add({"score": 100})}
```

### 场景2：一体机式的后端服务开发体验，弹性免运维，轻松应对游戏爆量
问题：随着小游戏持续运营，小游戏服务端无法自动应对游戏暴涨流量，影响用户体验，甚至引发用户投诉。
解决方案：服务部署在抖音云上，平台基于并发数，实现秒级伸缩容，轻松应对流量波动。

### 场景3：小游戏前端请求小游戏服务端免登录，小游戏服务端请求开放能力免鉴权，提升研发效率
问题：小游戏前端请求小游戏服务端，需要构建用户的登录态，实现请求身份的识别；小游戏服务端请求开放能力，需要维护access_token鉴权凭证。
解决方案：小游戏服务端托管在抖音云上，基于小游戏SDK，即可享受“免登录”和“免鉴权”特性。
1. 免鉴权：小游戏服务端托管在抖音云上，可直接调用开放能力OpenAPI接口，不需要传递和维护access_token
1. 免登录：基于小游戏SDK，小游戏前端网络请求自动带上用户openId，小游戏服务端天然感知请求用户的身份信息，不再需要开发和维护tt.login/code2Session相关流程。
## 三、常见问题

| 问题 | 回复 |
| --- | --- |
| 小游戏会上架到其他端（微信/vivo/oppo/快手），抖音云支持吗？ | 服务调用，云数据库、云存储（对象存储）只提供抖音端的SDK，抖音端SDK可免登录调用服务，自动携带openid信息。  如希望多端一套代码，可以在客户端统一使用[自定义域名](https://developer.open-douyin.com/docs/resource/zh-CN/developer/tools/cloud/guide/server-manage/custom-domain)请求云托管服务，在服务里通过服务端的SDK请求云数据库、云存储。  [云存储（对象存储） 服务端SDK](https://developer.open-douyin.com/docs/resource/zh-CN/developer/tools/cloud/sdk/tos-server-sdk) [云数据库 服务端SDK](https://developer.open-douyin.com/docs/resource/zh-CN/developer/tools/cloud/sdk/cloud-database-server-sdk/sdk-index) |
| 可以单独小游戏端接入云端存档吗？ | 支持。可识别小游戏宿主环境，针对抖音端进行云端存档 |
