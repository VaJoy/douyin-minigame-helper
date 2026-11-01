---
title: "查询Link"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/link/query-link-info
update_time: 2025-07-31
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/url_link/query_info`

**版本：** 1.0.201

查询已经生成的url link的信息（过期的url_link返回"url_link不存在或已失效"）。

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `url_link` | string | 是 | 生成的url_link |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |
| `access-token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `err_no` | int | 是 | 错误码 |  | BodyParam |
| `log_id` | string | 是 | 日志id |  | BodyParam |
| `data` | Object | 否 | 详细信息  **字段** - `query`（string）：query（json形式） - `version_type`（string）：小游戏版本 - `app_id`（string）：小游戏id - `app_name`（string）：宿主名称 - `create_time`（int64）：创建时间 - `expire_time`（int64）：到期失效时间 - `path`（string）：页面路径 |  | BodyParam |
| `err_msg` | string | 是 | 错误信息 |  | BodyParam |

## 请求示例

```bash
curl --location --request POST 'https://minigame.zijieapi.com/mgplatform/api/apps/url_link/query_info' \
--header 'content-type: application/json' \
--header 'access-token: 0801121846735352506a356a6' \
--data '{
  "url_link": "https://z.douyin.com/79lNBpL"
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
        "app_id": "tt411***",
        "app_name": "douyin",
        "create_time": 1748351411,
        "expire_time": 1749522180,
        "path": "",
        "query": "{\"page\":\"abc\",\"type\":6}",
        "version_type": "current"
    },
    "err_msg": "",
    "err_no": 0,
    "log_id": "2025052721145740C32A4CF2B6E3CE2929"
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
| 200 | 28005019 | 

url_link不存在或已失效

 |  |