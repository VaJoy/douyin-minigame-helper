---
title: "游戏站礼包接入指引"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/gift-bag/game-gift-station-guide
update_time: 2025-12-24
---

## 礼包下发路径概览

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/ec0440211fec4c9f909200db3378df46~tplv-9nona0m7ha-image.image)

## 技术接入流程

### 步骤一：接入道具推送协议
参考：[道具推送协议](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/gift-bag/gift-prop-push)完成接入

### 步骤二：礼包下发弹窗-告知用户

| **推送测试** | **示例图** |
| --- | --- |
| •请配合平台，将游戏礼包&道具统一下发到游戏内账号邮箱中，用户可自行进行领取，展示规则如下： ◦icon、名称对齐平台配置礼包名称、道具名称 ◦过期时间需披露 |  |

### 步骤三：配置道具 & 礼包
> 配置入口：控制台-运营-运营能力-道具&礼包营销-礼包列表-新建礼包-登录/签到礼包

建议配置高价值礼包提升用户转化效果，每日签到小游戏站与每日登录游戏各配置 1 个。
完成礼包上架后需实际去小游戏站内测试领取，包括是否页面提示领取成功、游戏内下发是否正常等。

{
"success":true
}

{
"gift_id":7461891275051078697,
"play_type":4,
"gift_name":"每日签到游戏礼包",
"gift_code":"cdk0000001",
"open_id":"_0000-vQJEof2jifeowf1TbzSda6jg",
"prop_list":[
{
"prop_id":"coin003",
"name":"游戏金币",
"count":5
},
{
"prop_id":"skin002",
"name":"皮肤",
"count":1
}
],
"env_type":"production",
"send_time":1737619782
}

{
"success":false,
"err_code":100001,
"reason":"失败原因"
}
