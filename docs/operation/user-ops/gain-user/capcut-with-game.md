---
title: "录屏添加剪映视频模板能力"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/user-ops/gain-user/capcut-with-game
update_time: 2024-07-24
---

为更好帮助开发者利用录屏分享视频推广小游戏，字节小游戏面向开发者推出“录屏添加剪映视频模板”的能力（仅支持抖音）。

开发者可通过在后台绑定剪映号并持续更新创作剪映模板，实现以录屏分享为分发核心的流量变现渠道。同时，用户直接在游戏内生成的录屏内容嵌套剪映模版进行发布，发布优质录屏视频也更容易获取流量。

开发者完成配置后，将审核通过的模板 id 传入对应的检验接口，即可将剪映模板自动嵌套在用户的分享视频内。

**示例对比**

|  |  |
| --- | --- |
| 无剪映模板：直接发布默认录屏视频 | 成功配置剪映模板：把录屏嵌套剪映模板内，更丰富视频内容 |
|      |      |

### 一、开通规则

|  |  |
| --- | --- |
| 开通规则 | |
| 前置条件 | 小游戏当前上架状态为「已发布」，且上线抖音；  小游戏主体信用分不低于 70 分；  通过平台设置页完成剪映号绑定。 |
| 绑定规则 | 一个游戏仅支持绑定一个剪映账号，  且暂不支持解绑和换绑。 |
| 绑定须知 | 绑定同一剪映号的小游戏将共享剪映视频模版 |
| 剪映专用包 | 为避免在小游戏中出现模板调用不成功的情况，  请下载剪映模板制作专用版 apk 进行模板创作和提交。  [剪映模版制作专用版](https://bytedance.larkoffice.com/docx/AxfPd4DgeoNhEZxuc4dcjykWnpb) |

### 二、接入指南

#### 申请能力

1.登录开发者后台，选择已发布上线游戏，点击【运营能力】的【剪映视频模板】后点击【申请开通】

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1661918540135)

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/剪映模版开通截图-3258246644460580.5.jpg)

2.编辑填写相关申请内容绑定剪映账号，提交申请等待审核通过即可（审核时效：1-2 个工作日）

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1662015159191)

#### 创作模板

剪映模板能力申请通过后，在剪映 app 中登录开发者后台所绑定的剪映账号，即可进行编辑创作模板。

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651587186985)

创作完成在发布导出界面，选择【导出】→【发布到其他平台】→【字节小游戏】 （如无法看到“发布到其他平台”按钮请上滑界面）。

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651587186881)

#### 管理模板

1.平台会对开发者成功发布的模板进行审核，只有审核通过的模板才可使用（审核时效：1-2 个工作日）；

2.开发者可在后台【剪映视频模板】界面对审核通过的模板进行管理；

3.该界面可查看该剪映账号下所关联的小游戏。

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1662015633041)

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1662015683452)

**注意：审核通过的模板是默认关闭的，如需玩家使用该模板，请注意操作开启**

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1651587187410)
