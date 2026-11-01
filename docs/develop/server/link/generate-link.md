---
title: "生成Link"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/link/generate-link
update_time: 2025-07-31
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/url_link/generate`

**版本：** 1.0.201

该接口用于生成能够直接跳转到端内小游戏的 url link。

URL Link相关api

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `app_name` | string | 是 | 宿主名称 |  | BodyParam |
| `expire_time` | int64 | 否 | 失效时间 |  | BodyParam |
| `query` | string | 否 | query（json形式） |  | BodyParam |
| `version_type` | string | 否 | 小游戏版本 |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |
| `access-token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `data` | Object | 否 | 详细信息  **字段** - `url_link`（string）：生成的link |  | BodyParam |
| `err_msg` | string | 是 | 错误信息 |  | BodyParam |
| `err_no` | int | 是 | 错误码 |  | BodyParam |
| `log_id` | string | 是 | 日志id |  | BodyParam |

## 请求示例

```bash
curl --location --request POST 'https://minigame.zijieapi.com/mgplatform/api/apps/url_link/generate' \
--header 'content-type: application/json' \
--header 'access-token: 0801121846735352506a356a6' \
--data '{
  "app_name": "douyin",
  "query": "{\"page\":\"abc\",\"type\":6}",
  "expire_time": 1749520800,
  "version_type": "current"
}'
```

## 成功响应示例

```json
{
    "BaseResp": {
        "StatusCode": 0,
        "StatusMessage": ""
    },
    "data": {
        "url_link": "https://l.douyin.com/7i9NPQN"
    },
    "err_msg": "",
    "err_no": 0,
    "log_id": "202505272110409E7071F616BEEB9A05F1"
}
```

## 异常响应示例

```json
{
    "BaseResp": {
        "Extra": {
            "oerror_inner_error": "",
            "oerror_origin_code": "28001003",
            "oerror_penetrate_data": "",
            "oerror_stability": "0"
        },
        "StatusCode": 28001003,
        "StatusMessage": "access_token无效"
    },
    "err_msg": "access_token无效",
    "err_no": 28001003,
    "log_id": "20250527222206F0E90F0A9FA3D9C5D558"
}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 0 | 

成功

 |  |
| 200 | 28001005 | 

系统错误

 |  |
| 200 | 28001007 | 

参数不合法

 |  |
| 200 | 28001003 | 

access_token无效

 |  |
| 200 | 28001019 | 

权限被封禁

 |  |
| 200 | 28005017 | 

schema编码异常

 |  |
| 200 | 28005014 | 

到期时间不在范围内

 |  |
| 200 | 28005016 | 

生成URL_Link频率过快

 |  |
| 200 | 28005018 | 

生成URL_Link数量超过上限

 |  |

## 使用限制

该接口设定有频次控制，每个小游戏，100qps，50w次/自然日。如有特殊需求联系oncall。