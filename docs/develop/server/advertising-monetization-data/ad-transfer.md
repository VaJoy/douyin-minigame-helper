---
title: "广告金转充流水查询"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/advertising-monetization-data/ad-transfer
update_time: 2026-04-03
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/ad/transfer/query`

**版本：** 1.0.296

广告金转充流水接口

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `end_date` | string | 是 | 结束日期 yyyy-MM-dd |  | BodyParam |
| `start_date` | string | 是 | 开始日期 yyyy-MM-dd |  | BodyParam |
| `Base` | Object | 否 | **字段** - `Caller`（string）： - `Client`（string）： - `Extra`（Object）： - `LogID`（string）： - `TrafficEnv`（Object）： - `Addr`（string）： |  | BodyParam |
| `Common` | Object | 是 | **字段** - `access-token`（string）：OpenAPI 调用凭证 - `mp_id`（string）：小游戏 AppID - `Base`（Object）： |  | BodyParam |
| `Page` | Object | 否 | **字段** - `page_no`（int）：页码，必填，从 1 开始 - `page_size`（int）：每页条数，必填，最大 500 |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `items` | Array | 否 | **字段** - `0`（Object）： |  | BodyParam |
| `trace` | Object | 否 | **字段** - `downstream_service`（string）：下游服务名 - `log_id`（string）：请求日志 ID - `cache_hit`（boolean）：是否命中缓存 - `downstream_cost_ms`（int64）：下游耗时（ms） |  | BodyParam |
| `BaseResp` | Object | 是 | **字段** - `StatusCode`（int）： - `StatusMessage`（string）： - `Extra`（Object）： |  | BodyParam |
| `Page` | Object | 否 | **字段** - `total`（int）：总条数 |  | BodyParam |

## 请求示例

```bash
curl --location 'https://minigame.zijieapi.com/mgplatform/api/apps/ad/transfer/query' \
--header 'access-token: 080112184749375a6a41694d4c7a685a4a657961734f42696c773d3d' \
--header 'Content-Type: application/json' \
--data '{
    "Common": {
        "AccessToken": "080112184749375a6a41694d4c7a685a4a657961734f42696c773d3d",
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
    "start_date": "2025-01-01",
    "end_date": "2025-02-01",
    "Page": {
        "page_no": 1,
        "page_size": 20
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
            "TransferDate": "2025-06-06 16:41:32",
            "AccountID": "1798402546593865",
            "AccountName": "星图全域联投-星图内广ppe账户_星品追投",
            "AccountOwner": "北京xxxxx有限公司",
            "TransferAmount": 1
        },
        {
            "TransferDate": "2025-05-21 16:39:14",
            "AccountID": "1777562970844163",
            "AccountName": "星图全域联投-星图内广ppe账户",
            "AccountOwner": "北京xxxxx有限公司",
            "TransferAmount": 100
        }
    ],
    "Page": {
        "Total": 2
    },
    "Trace": {
        "LogID": "2026020117023206C23E47C65DA261631E"
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
| 200 | 28001451 | 查询范围超限 |  |
| 200 | 28001429 | qps超限 |  |
