---
title: "游戏礼包"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/receive-reward
update_time: 2025-07-31
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/gift/receive_reward`

**版本：** 1.0.96

用户在获取到礼包兑换码进入游戏后，发起核销兑换码的动作，开发者需要使用本接口校验礼包兑换码的有效性。校验通过后才可以发放对应礼包。

兑换福袋

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `env_type` | string | 否 | 环境类型 |  | BodyParam |
| `gift_code` | string | 是 | cdk |  | BodyParam |
| `open_id` | string | 是 | 兑奖用户的OpenID |  | BodyParam |
| `uuid` | string | 是 | 开发者厂商侧传入，幂等 |  | BodyParam |
| `access-token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | HeaderParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `err_no` | int | 是 |  |  | BodyParam |
| `gift_info` | Object | 否 | **字段** - `play_type`（int）：任务信息 玩法类型 - `name`（string）：礼包基础信息 - `gift_effective_end_time`（int64）： - `user_receive_guide`（Array）： - `gift_effective_start_time`（int64）： - `prop_list`（Array）：关联道具列表 - `gift_id`（string）：回显展示字段 - `icon_url`（string）： |  | BodyParam |
| `err_msg` | string | 是 |  |  | BodyParam |

## 请求示例

```bash
curl --location 'https://minigame.zijieapi.com/mgplatform/api/gift/receive_reward' \
--header 'content-type: application/json' \
--header 'access-token: 0801121846735352506a356a6' \
--data '{
    "uuid": "a017cd52-ca34-4a21-bab1-0844160d06e5",
    "open_id": "ba253642-0590-40bc-40ca",
    "gift_code": "mg1722924937_11229022",
}'
```

## 成功响应示例

```json
{
    "gift_info": {
        "play_type": 1,
        "user_receive_guide": [
            "玩小游戏10秒后获得白金礼包"
        ],
        "name": "白金强化碎片包",
        "icon_url": "https://img.byte25cdn.org/image/198082103523233",
        "gift_effective_start_time": 1722873600,
        "gift_effective_end_time": 1723737600,
        "gift_id": "222622358400",
        "prop_list": [
            {
                "prop_id": "10111",
                "name": "白金强化碎片",
                "icon": "https://img.byte25cdn.org/image/1980821035232290",
                "count": 10
            }
        ]
    },
    "err_msg": "",
    "log_id": "202008121419360101980821035705926A",
    "err_no": 0
}
```

## 异常响应示例

```json
{
  "err_msg": "重复核销",
  "log_id": "202008121419360101980821035705926A",
  "err_no": 29005065
}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 28001005 | 系统内部错误，请重试 | 请求重试，若依然无解请向平台提交反馈 |
| 200 | 28001003 | access_token无效 | 重新请求生成access_token |
| 200 | 28001008 | access_token过期,请刷新或重新授权 | 重新请求生成access_token |
| 200 | 28001006 | 网络调用错误，请重试 | 重试即可 |
| 200 | 28001007 | 参数错误 | 请仔细检查相关参数 |
| 200 | 28006040 | 礼包码重复核销 | 该券已经提交过核销记录，无需再提交 |
| 200 | 28006041 | 礼包码与open_id的绑定关系有误 | 礼包码与open_id的绑定关系有误，请再次确认 |

## 前置条件

无
