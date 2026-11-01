---
title: "生成Schema"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/schema/generate-schema
update_time: 2025-07-31
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/schema/generate`

**版本：** 1.0.201

该接口用于生成能够直接在端内跳转小游戏的 schema。

schema支持两种类型：

1. 长期有效 schema，可通过no_expire指定，生成后可永久使用。
2. 短期有效 schema，需传入到期时间的 Unix 时间戳，最长距离当前时间 180 天。

Schema相关api

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `version_type` | string | 否 | 小游戏版本 |  | BodyParam |
| `expire_time` | int64 | 否 | 失效时间 |  | BodyParam |
| `no_expire` | boolean | 否 | 生成的scheme码类型，false:短期有效，true:长期有效 |  | BodyParam |
| `query` | string | 否 | query（json形式） |  | BodyParam |
| `access-token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | HeaderParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `data` | Object | 否 | 详细信息  **字段** - `schema`（string）：生成的schema |  | BodyParam |
| `err_msg` | string | 是 | 错误信息 |  | BodyParam |
| `err_no` | int | 是 | 错误码 |  | BodyParam |
| `log_id` | string | 是 | 日志id |  | BodyParam |

## 请求示例

```bash
curl --location --request POST 'https://minigame.zijieapi.com/mgplatform/api/apps/schema/generate' \
--header 'content-type: application/json' \
--header 'access-token: 0801121846735352506a356a6' \
--data '{
  "query": "{\"page\":\"abc\",\"type\":6}",
  "expire_time": 1749522180,
  "no_expire": false,
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
        "schema": "sslocal://microgame?app_id=tt411***&bdp_log=%7B%22enter_from_merge%22%3A%22share_alert%22%2C%22enter_position%22%3A%22z_link%22%2C%22entrance_form%22%3A%22share%22%2C%22launch_from%22%3A%22share_zlink%22%2C%22location%22%3A%22message%22%7D&query=%7B%22page%22%3A%22abc%22%2C%22type%22%3A6%7D&scene=024012&uniq_id=S2025060316421784319298209263721021449ae2822a0f82&version=v2&version_type=current&bdpsum=e135db4"
    },
    "err_msg": "",
    "err_no": 0,
    "log_id": "20250603174333527BA738A6040A9AC3E1"
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
| 200 | 28005078 | 

到期时间不在范围内

 |  |
| 200 | 28005075 | 

生成Schema频率过快

 |  |
| 200 | 28005076 | 

生成Schema数量超过上限

 |  |

## 使用限制

该接口设有频次限制，如有特殊需求请 oncall。

- 短期有效：每个小游戏，100qps，每日上限不超过50万条。
- 长期有效：每个小游戏，100qps，配置上限不超过10万条。

注意事项：生成的schema为明文，如果放入二维码中对外开放，用户扫码后可以看到原文，请注意信息安全。