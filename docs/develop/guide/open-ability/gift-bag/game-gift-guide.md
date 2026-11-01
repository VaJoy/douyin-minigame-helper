---
title: "游戏礼包能力接入指引概览"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/gift-bag/game-gift-guide
update_time: 2025-08-13
---

## 礼包类型概览
抖音开放平台提供组件化的道具礼包营销能力，厂商可根据不同经营目标，选择经营场景配置道具和礼包列表，促进游戏转化提升用户留存。
当前支持的礼包类型如下：

| 场景分类 | 核心价值 | 数据效果案例 |
| --- | --- | --- |
| 直播场景-礼包福袋 | 福袋抽奖玩法，用户完成直播间任务即可参与礼包抽奖，提升直播间进小游戏转化 | 接入直播福袋能力的小游戏，相比未有福袋能力时：  直播间启动CTR**+30%** 老用户启动游戏收入**+50%** 游戏广告渗透/au显著提升**+56.19%** |
| 游戏站场景-登录/签到礼包 | 每日游戏登录礼包 / 每日游戏站签到礼包，提升社区复访，增强用户-社区的粘性 | 游戏次日留存**+25%、**7日留存**+28%** |
| 付费场景-限时付费礼包 | 平台根据厂商配置的多档位礼包，在端内对用户进行精准触达和推荐，提升付费转化 | / |

## 礼包核心概念
不同的礼包类型在具体配置和技术接入上存在区别，但共享了一套统一的后台管理流程和库存管理等能力，我们先对这部分通用的能力进行说明。
> 道具礼包配置入口：控制台-运营-运营能力-道具&礼包营销
### 游戏道具 & 礼包内容
游戏道具是一种游戏内部虚拟资源，开发者配置礼包时可以指定「一个礼包能够兑换成什么游戏道具，数量分别是几个」，因此在配置礼包之前需要先完成道具的创建。

**道具创建**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b33696778e624c01af6191d2e3140632~tplv-9nona0m7ha-image.image)

> 按照页面提示进行创建即可，需审核通过后可用于礼包配置

**礼包配置关联道具**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/475f588f7711403b86589853873a8e5f~tplv-9nona0m7ha-image.image)

> 选择道具以及指定数量作为礼包奖励

> **注意**
> 一个游戏道具本身不允许设置为固定数量，如道具名称：金币x99；正确的方式应该是在配置礼包时指定金币道具，并设置数量x99

### 礼包码 & 礼包库存管理
礼包码，别名有 gift_code, cdk, cdkey 等，在常见的游戏礼包兑奖系统中是作为玩家的兑奖凭证使用，这里也不例外。在平台中礼包码具有以下约束：
- 礼包码唯一性：在同一个小游戏ID命名空间中保证唯一，不会重复；
- 礼包码数量=库存数量：玩家获得一个礼包码会对应后台礼包库存数量-1；
- 一人一码：玩家获得礼包码后，只能由本人兑奖，可通过[兑奖OpenAPI](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/receive-reward)完成确认。

> **礼包类型差异说明**
> 礼包福袋和限时付费礼包需要通过兑奖OpenAPI确认**礼包码的有效性**以及**是否本人兑奖**；
> 游戏站登录/签到礼包则不需要，其有效性已通过[消息推送协议](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/gift-bag/game-gift-station-guide#a21a833e)确认，可以直接兑换。

开发者在平台上配置了礼包的库存数量限额后，平台会自动生成对应数量的礼包码以供后续消耗，当前支持两种类型库存限制：

**无库存限制**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/66a02e5f815d4354b80b429411cd3a03~tplv-9nona0m7ha-image.image)

> 只要玩家满足领取条件，礼包允许无限下发，需关注礼包的实时消耗情况

**有库存限制**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b902d6e49f7640719fff5465869e2bfc~tplv-9nona0m7ha-image.image)

> 有限量的库存消耗完时，礼包会自动下架，需即时补充库存

## 接入指引
### 直播福袋礼包

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/a4f70141fa764769aaf41054507ad273~tplv-9nona0m7ha-image.image)

参照[直播福袋礼包接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/gift-bag/game-gift-lottery-guide)文档完成礼包接入
### 限时付费礼包

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/3f94b44fd5dd478897bf74cd51e46c72~tplv-9nona0m7ha-image.image)

参照[限时付费礼包接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/gift-bag/game-gift-paid-guide)文档完成礼包接入
### 游戏站登录/签到礼包

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/2aff7220554d4de188c40dca0df0cd35~tplv-9nona0m7ha-image.image)

参照[游戏站礼包接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/gift-bag/game-gift-station-guide)文档完成礼包接入

**第一步：新建道具**，需要填名称、图标以及道具ID