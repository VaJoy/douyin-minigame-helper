---
title: "公会群能力指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/union-group-guide
update_time: 2025-04-07
---

## 能力简介：
抖音「公会群」旨在打造一个便捷化的交流互动平台，便于公会成员之间进行沟通交流，以及高效组织各类游戏相关活动 。公会长可在抖音平台自行创建公会、联盟、帮派等的专属群组，并将其与游戏内的公会进行绑定操作。绑定完成后，公会成员即可在游戏内一键加群至相应群中。
- *「公会群」互动案例：*

| 公会活动组织 | 攻略经验分享 | 游戏日常交流 | 游戏组队开黑 | 游戏资讯分享 |
| --- | --- | --- | --- | --- |

## 数据效果：
- LT ：加群前 VS 加群后，人均游戏时长 **+ 15.5%。**
- 留存：加群玩家 VS 小游戏玩家大盘，次日留存**高 33%，**7 日留存**高 27%。**
- 群活跃：公会群 VS 活跃群大盘，日均发言率**高 16.2%，**日均进群率**高 28.6%。**

## 能力示意图：
**分为公会长和公会成员的流程，部分页面实现逻辑（包括 UI）由小游戏承接、剩余部分由平台承接，请详细看图区分。**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b4c12d3fa70a4ec7be6027566e684fce~tplv-9nona0m7ha-image.image)

## 前置准备：
检查基础库版本：基础库版本 >= 3.51.0.0。

## 接入流程：
### 名词说明：

| 名词 | 说明 |
| --- | --- |
| 公会 | 游戏内自行维护的群体，可以是帮派，群组等，通过 unionId 唯一标识 |
| 公会长 | 游戏内自行维护的公会的管理人员，一般给予公会长绑定和公开群的权限 |
| unionId | 游戏与平台交互的主要字段，由游戏侧生成和存储，平台会记录 unionId 与 公开群的绑定信息，并提供查询/绑定/解绑 等能力 |

### 整体链路：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/163659035cb94bfe8d193dc686e8bfd6~tplv-9nona0m7ha-image.image)

### 场景细拆：

| 场景 | 步骤说明 | 示例截图 |
| --- | --- | --- |
| 前置判断 | 通过 [tt.canIuse](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/foundation/tt-can-i-use/)("getUnionGroupInfo") 判断当前环境和应用版本是否支持公会群能力： 不支持则不应展示公会群相关的信息 支持则继续 |  |
| 展示公会群信息 | 游戏内自行判断用户是否为公会成员； 通过 tt.getUnionGroupInfo 获取当前公会是否有绑定过公开群 如果未绑定则给特定用户，比如公会长展示绑定按钮 如果已绑定则展示加入公开群按钮（一个公会只支持绑定一个公开群，请勿提供绑定入口重复绑定） |  |
| 绑定公会和公开群（公会长） | 公会长点击触发 tt.bindUnionGroup 接口，接口成功回调可获取绑定结果； success bindResult = true：绑定成功更新游戏公会群信息，展示解绑（公会长）/进群入口（公会成员）； success bindResult = false：用户未进行绑定操作，游戏按需进行提示或者引导重新； fail 回调：绑定失败，请参考错误码排查； |  |
| 解除绑定公会和公开群（公会长） JSAPI 解绑必须和绑定是同一人 OpenAPI 支持游戏服务端解除绑定 | 公会长点击触发 tt.unbindUnionGroup 接口： success 回调：解绑成功； fail 回调：根据错误码排查；  公会长无法进行解绑时，游戏也能通过 OpenAPI 进行解绑操作； |  |
| 加入群聊（公会成员） | 公会成员点击触发 tt.joinUnionGroup 接口： success 回调：接口调用成功，但是否进群由玩家自行选择，游戏无法感知加群结果； fail 回调：接口调用失败，根据错误码排查； （成功加入后，也需要保留“加入群”按钮，公会成员一点就进入群聊互动） |  |
