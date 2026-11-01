---
title: "广告金账户余额查询"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/advertising-monetization-data/ad-balance
update_time: 2026-04-03
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/ad/balance/query`

**版本：** 1.0.296

查询小游戏广告金账户余额信息，可用于广告金管理、转充决策和账户核对。

广告金余额接口

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `Base` | Object | 否 | **字段** - `Client`（string）： - `Extra`（Object）： - `LogID`（string）： - `TrafficEnv`（Object）： - `Addr`（string）： - `Caller`（string）： |  | BodyParam |
| `Common` | Object | 是 | **字段** - `mp_id`（string）：小游戏 AppID - `Base`（Object）： - `access-token`（string）：OpenAPI 调用凭证 |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `BaseResp` | Object | 是 | **字段** - `Extra`（Object）： - `StatusCode`（int）： - `StatusMessage`（string）： |  | BodyParam |
| `items` | Object | 否 | **字段** - `available_balance`（double）：广告金可转充余额（元） - `expiring_balance`（double）：即将过期余额（元） - `mp_id`（string）：游戏 ID |  | BodyParam |
| `trace` | Object | 否 | **字段** - `cache_hit`（boolean）：是否命中缓存 - `downstream_cost_ms`（int64）：下游耗时（ms） - `downstream_service`（string）：下游服务名 - `log_id`（string）：请求日志 ID |  | BodyParam |

## 请求示例

```bash
curl --location 'https://minigame.zijieapi.com/mgplatform/api/apps/ad/income/query' \
--header 'access-token: 080112184749375a6a41694d4c7a685a4a657961734f42696c773d3d' \
--header 'Content-Type: application/json' \
--data '{
    "Common": {
        "access-token": "08011218474a454c517252594d56446a787a37564775695747673d3d",
        "mp_id": "tta682d03f39b2471b07",
        "Base": {
            "LogID": "202408212023569E4E311CD0F1CC3BF7B7",
            "Caller": "",
            "Addr": "",
            "Client": "",
            "TrafficEnv": {
                "Open": false,
                "Env": ""
            },
            "Extra": {
                "": ""
            }
        }
    },
    "Base": {
        "LogID": "202408212023569E4E311CD0F1CC3BF7B7",
        "Caller": "",
        "Addr": "",
        "Client": "",
        "TrafficEnv": {
            "Open": false,
            "Env": ""
        },
        "Extra": {
            "": "",
            "env": "prod"
        }
    }
}'
```

## 成功响应示例

```json
{
    "Items": {
        "MpID": "tta682d03f39b2471b07",
        "AvailableBalance": 19920.72,
        "ExpiringBalance": 0
    },
    "Trace": {
        "LogID": "202602042035214B0B1C4B25F082E94B63"
    },
    "BaseResp": {
        "StatusMessage": "success",
        "StatusCode": 0
    }
}
```

## 异常响应示例

```json
{
    "BaseResp": {
        "StatusMessage": "date range too long (max 90 days)",
        "StatusCode": 28001451
    }
}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 28001429 | qps超限 |  |
| 200 | 28001005 | 系统内部错误，请重试 | 请求重试，若依然无解请向平台提交反馈 |
| 200 | 28001003 | access_token无效 | 重新请求生成access_token |
| 200 | 28001008 | access_token过期,请刷新或重新授权 | 重新请求生成access_token |
| 200 | 28001016 | 当前应用已被封禁或下线 | clientKey被封禁或者下线 |
| 200 | 28001006 | 网络调用错误，请重试 | 重试即可 |
| 200 | 28001014 | 应用未授权任何能力 | 确认应用是否授权能力 |
| 200 | 28001018 | 应用未获得该能力 | 开通相关能力 |
| 200 | 28003017 | quota已用完 | 联系平台处理 |
| 200 | 28001019 | 应用该能力已被封禁 | 该能力被封禁，联系平台处理 |
| 200 | 28001007 | 参数不合法 | 根据错误信息检查请求参数是否填写正常 |
