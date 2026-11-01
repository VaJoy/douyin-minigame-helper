---
title: "广告金赠送金额查询"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/advertising-monetization-data/ad-gift
update_time: 2026-04-03
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/ad/gift/query`

**版本：** 1.0.296

广告金赠送金额接口

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `Common` | Object | 是 | **字段** - `mp_id`（string）：小游戏 AppID - `Base`（Object）： - `access-token`（string）：OpenAPI 调用凭证 |  | BodyParam |
| `Page` | Object | 是 | **字段** - `page_no`（int）：页码，必填，从 1 开始 - `page_size`（int）：每页条数，必填，最大 500 |  | BodyParam |
| `end_date` | string | 是 | 结束日期 yyyy-MM-dd |  | BodyParam |
| `income_type` | string | 否 | 收入类型，如果不传递收入类型，将默认返回全部类型的数据 枚举： IAA：IAA收入广告金 IAP：IAP收入广告金 IAALimitTime：IAA收入广告金限时激励 |  | BodyParam |
| `start_date` | string | 是 | 开始日期 yyyy-MM-dd |  | BodyParam |
| `Base` | Object | 否 | **字段** - `Addr`（string）： - `Caller`（string）： - `Client`（string）： - `Extra`（Object）： - `LogID`（string）： - `TrafficEnv`（Object）： |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `BaseResp` | Object | 是 | **字段** - `StatusCode`（int）： - `StatusMessage`（string）： - `Extra`（Object）： |  | BodyParam |
| `Page` | Object | 否 | **字段** - `total`（int）：总条数 |  | BodyParam |
| `items` | Array | 否 | **字段** - `0`（Object）： |  | BodyParam |
| `trace` | Object | 否 | **字段** - `downstream_service`（string）：下游服务名 - `log_id`（string）：请求日志 ID - `cache_hit`（boolean）：是否命中缓存 - `downstream_cost_ms`（int64）：下游耗时（ms） |  | BodyParam |

## 请求示例

```bash
curl --location 'https://minigame.zijieapi.com/mgplatform/api/apps/ad/gift/query' \
--header 'access-token: 080112184749375a6a41694d4c7a685a4a657961734f42696c773d3d' \
--header 'Content-Type: application/json' \
--data '{
    "Common": {
        "access-token": "",
        "mp_id": "tt411d37a0de37d565",
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
    "start_date": "2025-12-01",
    "end_date": "2026-08-01",
    "income_type": "",
    "Page": {
        "page_no": 1,
        "page_size": 100
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
    "Items": [
        {
            "SettleDate": "2025年7月1日至31日",
            "IncomeType": "IAA收入广告金限时激励",
            "GiftAmount": 300000,
            "ExpireDate": "2026-01-17 17:18:01"
        },
        {
            "SettleDate": "2025年01月16日",
            "IncomeType": "IAP收入广告金",
            "GiftAmount": 1.21,
            "ExpireDate": "2025-10-18 00:00:00"
        }
    ],
    "Page": {
        "Total": 2
    },
    "Trace": {
        "LogID": "2026020117031606C23E47C65DA26194F5"
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
| 200 | 28001429 | qps超限 |  |
| 200 | 28001451 | 查询范围超限 |  |
