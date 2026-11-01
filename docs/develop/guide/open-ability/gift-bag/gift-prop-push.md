---
title: "礼包道具推送协议"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/gift-bag/gift-prop-push
update_time: 2025-12-17
---

## 简介
接入此协议，开发者可在服务器接收来自平台的礼包、道具发放的消息，并可据此实现给用户发放特定道具奖励的能力。
目前协议支持的礼包类型有：小游戏站礼包、平台托管礼包、道具推送（如小游戏站活动奖励等）。

> **注意**
> 完成消息协议接入后，请务必通过「道具推送测试」「礼包测试」等能力验证礼包发放链路的有效性，并保障好接口的稳定性。

### **前提条件**
> 开发者需要在平台上配置好推送的地址，触发奖励发放时，平台将把请求推送到开发者服务器
参考：[消息推送配置接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/message-push/msg-push-config-guide) 完成接入

## 推送消息协议
在具体的发货请求中，有效的 payload 会放在请求的 body 中，开发者可在验签成功后对 body 进行解析，并执行具体的发货业务逻辑。
### 请求
编码协议：JSON

| **字段名** | **字段类型** | **必须** | **说明** |
| --- | --- | --- | --- |
| gift_id | int64 | 否 | 发货时对应的礼包ID 如果是礼包发货则包含，如果是纯道具发货则没有 |
| play_type | int8 | 是 | 发货时对应的玩法类型枚举 枚举：3(游戏站登录礼包), 4(游戏站签到礼包), 5(平台托管礼包)，11(道具) |
| channel | int8 | 否 | 对应托管礼包发货时的渠道枚举：3(用户权益中心) |
| gift_name | string | 否 | 发货时对应的礼包名称，与 gift_id 共同存在 |
| gift_code | string | 是 | 此次发货使用的礼包码，可用于消息去重 |
| open_id | string | 是 | 领奖用户的 open_id |
| prop_list | array | 是 | 此次发货的道具列表，正常情况下，开发者需给用户账号增加这些道具资产 |
| prop_list.prop_id | string | 是 | 道具列表中当前道具的道具ID |
| prop_list.name | string | 是 | 道具列表中当前道具的道具名称 |
| prop_list.count | int64 | 是 | 道具列表中当前道具的发货数量 |
| env_type | string | 是 | 发货请求的环境标识 •development：调试环境，使用平台测试推送入口时使用 •production：正式环境，用户正式领取礼包时使用 |
| send_time | int64 | 是 | 礼包/道具推送请求触发的秒级时间戳 |
| refer_id | string | 否 | 礼包/道具推送对应的来源ID： 道具推送测试为：test_prop_push 游戏站活动任务为: 活动ID如 "7584227948077607459" |

#### 示例
道具推送测试：

```json
{
    "play_type":11,
    "gift_code": "53e4f0fdf53f4e4397d8715e14e92415",
    "open_id": "_0000-vQJEof2jifeowf1TbzSda6jg",
    "prop_list": [
        {
            "prop_id": "coin003",
            "name": "游戏金币",
            "count": 5
        },
        {
            "prop_id": "skin002",
            "name": "皮肤",
            "count": 1
        }
    ],
    "env_type": "production",
    "send_time": 1737619782,
    "refer_id": "test_prop_push"
}
```

游戏站签到礼包推送：

```json
{
    "gift_id": 7461891275051078697,
    "play_type":4,
    "gift_name":"每日签到游戏礼包",
    "gift_code": "53e4f0fdf53f4e4397d8715e14e92415",
    "open_id": "_0000-vQJEof2jifeowf1TbzSda6jg",
    "prop_list": [
        {
            "prop_id": "coin003",
            "name": "游戏金币",
            "count": 5
        },
        {
            "prop_id": "skin002",
            "name": "皮肤",
            "count": 1
        }
    ],
    "env_type": "production",
    "send_time": 1737619782
}
```

### 响应
#### **正常响应**
HTTP 状态码：200
HTTP 响应体：JSON

```json
{
    "success": true
}
```

#### **异常响应**
HTTP 状态码：200（**非200响应可能导致礼包下架， 无法发货请通过下方错误码返回**）
HTTP 响应体：JSON

```json
{
    "success": false,
    "err_code": 100001,
    "reason": "失败原因"
}
```

**err_code 错误码枚举**：

| err_code | 说明 |
| --- | --- |
| 100001 | 未注册/未登录/未创建角色，用户未满足领取条件 |
| 100002 | 触发频控，允许稍后重试 |

## 消息接入测试
完成道具配置后，可在道具列表点击「道具推送测试」来触发消息推送

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/4de4ebd8d9c1445984cecd17f6998e5a~tplv-9nona0m7ha-image.image)

请按照提示输入你用来测试的抖音UID，并选择此次推送的道具，点击确定后，你将在下方的实时日志中看到此次请求的详细内容。
这里输入的抖音UID在推送前会转成抖音宿主端对应的 open_id。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/192b27d03d404906bd0a8c73340f0781~tplv-9nona0m7ha-image.image)

{"gift_id":7461891275051078697,"play_type":4,"gift_name":"每日签到游戏礼包","gift_code":"cdk0000001","open_id":"_0000-vQJEof2jifeowf1TbzSda6jg","prop_list":[{"prop_id":"coin003","name":"游戏金币","count":5},{"prop_id":"skin002","name":"皮肤","count":1}],"env_type":"production","send_time":1737619782}
