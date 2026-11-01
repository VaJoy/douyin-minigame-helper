---
title: "直播福袋礼包接入指引"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/gift-bag/game-gift-lottery-guide
update_time: 2025-06-04
---

## 礼包下发路径概览

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/d9bb72c152b549efa783ca1aba851be4~tplv-9nona0m7ha-image.image)

## 礼包配置
> 配置入口：控制台-运营-运营能力-道具&礼包营销-礼包列表-新建礼包-直播福袋礼包
按照页面提示完成礼包信息配置和礼包道具库存配置即可，对配置字段有疑问可查看 Q&A
## 兑奖流程开发

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/ef58a318a57a4004a66edd57a1b5a905~tplv-9nona0m7ha-image.image)

游戏内需要主动获取 tt.onShow 中的 query 字段，携带的 json 信息中包含了 game_cdkey 字段：

```json
{
*    "game_cdkey": "cdkey88888"
*}
```

获取到 cdkey 后可通过 兑奖 [OpenAPI](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/receive-reward) 构造兑奖请求并完成核销下发礼包道具。

## 兑奖流程测试
**第一步：加入对应小游戏的调试成员**
开发-开发设置-测试管理-添加设备，使用抖音扫码：

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/652cb73798494f0b97d11a2fb40f4f96~tplv-9nona0m7ha-image.image)

**第二步：进入礼包详情页进行礼包测试**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/4df7630ca05b47bf93a08d19f1d51577~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/424fc481d5d44df3aafaf6d6a292083a~tplv-9nona0m7ha-image.image)

用抖音扫码即可打开当前游戏的测试版本，并且tt.onShow的query中会携带cdkey信息。开发者可以自己调试兑奖流程。

> **注意**
> 测试 cdkey 只能使用一次，多次测试请输入不同的 cdkey

## Q&A
Q: 礼包生效期和领取有效期的区别是什么？
A: 礼包生效期控制主播可见福袋礼包生效并下发的时间，而领取有效期指的是用户在直播间中奖后进入游戏兑奖的有效期，超出领取有效期将无法完成兑奖。

Q: 领取路径是什么意思？
A: 用户在直播间中奖后，提示给用户如何在游戏内查找手动兑奖入口的路径，如「我的-礼包-兑换」。

Q: 不是已经有了 tt.onShow 监听用户进入游戏携带的 cdkey 吗？为什么还需要领取路径进行手动兑奖？
A：福袋礼包支持多种兑奖方式，从直播间中奖页直接跳转小游戏、从中奖消息站内信链接跳转小游戏都会自动携带 cdkey；也支持用户在中奖页手动复制 cdkey 进入游戏兑奖，此时 tt.onShow 中不会有 cdkey 信息，因此游戏内需要有手动兑奖入口。

Q: 除了调用兑奖的 OpenAPI 外，我还可以对 cdkey 进行别的校验吗？
A: cdkey 目前是由平台根据库存数量自动生成的随机字符串，除了使用兑奖接口OpenAPI进行兑奖外，不需要再进行额外的校验。
