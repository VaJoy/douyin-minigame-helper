---
title: "流量主广告数据查询"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/advertising-monetization-data/traffic-master-advertising-data
update_time: 2026-04-03
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/ad/income/query`

**版本：** 1.0.296

查询小游戏广告变现数据，支持按日期范围及广告位、宿主应用、操作系统、归因渠道等维度筛选，用于经营分析和效果评估

流量主广告收入接口

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `end_date` | string | 是 | 结束日期 yyyy-MM-dd，必传 |  | BodyParam |
| `Common` | Object | 是 | **字段** - `mp_id`（string）：小游戏 AppID - `Base`（Object）： - `access-token`（string）：OpenAPI 调用凭证 |  | BodyParam |
| `ad_type` | string | 否 | 广告位类型，如果不传递广告位类型名称，将默认返回全部类型广告位的数据： 广告位类型名称 枚举值： banner：Banner interstitial：插屏 video： 激励视频 |  | BodyParam |
| `os` | string | 否 | 操作系统，如果不传操作系统，将默认返回全部操作系统的数据 枚举值： ios：ios android：安卓 open_harmony：鸿蒙 |  | BodyParam |
| `Page` | Object | 是 | **字段** - `page_no`（int）：页码，必填，从 1 开始 - `page_size`（int）：每页条数，必填，最大 500 |  | BodyParam |
| `Base` | Object | 否 | **字段** - `TrafficEnv`（Object）： - `Addr`（string）： - `Caller`（string）： - `Client`（string）： - `Extra`（Object）： - `LogID`（string）： |  | BodyParam |
| `host_app` | string | 否 | 宿主 APP，如果不传递宿主 APP，将默认返回全部宿主的数据 枚举值： toutiao：今日头条 toutiao_lite：头条极速版 douyin：抖音 douyin_lite：抖音极速版 xigua：西瓜视频 fanqie：番茄小说 pipixia：皮皮虾 hongguo：红果 novel：番茄畅听 fanqie_music：番茄音乐 qishui：汽水音乐 |  | BodyParam |
| `channel` | string | 否 | 归因渠道来源，如果不传归因渠道来源，将默认返回全部归因渠道来源的数据 枚举值： AD：广告 Star：星图-口价 Pop：发行人 Nature：自然 |  | BodyParam |
| `start_date` | string | 是 | 开始日期 yyyy-MM-dd，必传 |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `items` | Array | 否 | **字段** - `0`（Object）： |  | BodyParam |
| `trace` | Object | 否 | **字段** - `downstream_cost_ms`（int64）：下游耗时（ms） - `downstream_service`（string）：下游服务名 - `log_id`（string）：请求日志 ID - `cache_hit`（boolean）：是否命中缓存 |  | BodyParam |
| `BaseResp` | Object | 是 | **字段** - `StatusMessage`（string）： - `Extra`（Object）： - `StatusCode`（int）： |  | BodyParam |
| `Page` | Object | 否 | **字段** - `total`（int）：总条数 |  | BodyParam |

## 请求示例

```bash
curl --location 'http://minigame.zijieapi.com/mgplatform/api/apps/ad/income/query' \
--header 'access-token: xxx' \
--header 'Content-Type: application/json' \
--data '{
    "Common":{
        "access-token":"xxx",
        "mp_id":"xxx"
    },
    "start_date": "2025-02-01",
    "end_date": "2025-03-02",
    "page_no": 1,
    "page_size": 20,
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
  "items": [
    {
      "date": "2026-01-01",
      "host_app": "douyin",
      "os": "android",
      "channel": "organic",
      "ad_type": "reward_video",
      "request_pv": 100000,
      "show_pv": 80000,
      "click_pv": 5000,
      "click_rate": 0.0625,
      "ecpm": 35.6,
      "income_before_share": 2850.12,
      "income_after_share": 1995.08
    }
  ],
  "page": {
    "total": 1
  },
  "trace": {
    "log_id": "abc-123",
    "cache_hit": true
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
| 200 | 28001451 | 查询范围超限 |  |
