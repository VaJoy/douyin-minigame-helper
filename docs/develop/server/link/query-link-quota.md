---
title: "查询Link配额"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/link/query-link-quota
update_time: 2025-07-31
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/url_link/query_quota`

**版本：** 1.0.201

查询当前小游戏生成url link的配额。

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `access-token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | HeaderParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `data` | Object | 否 | 详细信息  **字段** - `url_link_used`（int）：url_link 已生成次数 - `url_link_limit`（int）：url_link 生成次数上限 |  | BodyParam |
| `err_msg` | string | 是 | 错误信息 |  | BodyParam |
| `err_no` | int | 是 | 错误码 |  | BodyParam |
| `log_id` | string | 是 | 日志id |  | BodyParam |

## 请求示例

```bash
curl --location --request POST 'https://minigame.zijieapi.com/mgplatform/api/apps/url_link/query_quota' \
--header 'content-type: application/json' \
--header 'access-token: 0801121846735352506a356a6' \
--data '{}'
```

## 成功响应示例

```json
{
    "BaseResp": {
        "StatusCode": 0,
        "StatusMessage": ""
    },
    "data": {
        "url_link_limit": 500000,
        "url_link_used": 4
    },
    "err_msg": "",
    "err_no": 0,
    "log_id": "202505272220238FD68647F4AF04CD25CE"
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
| 200 | 28001003 | 

access_token无效

 |  |
| 200 | 28001019 | 

权限被封禁

 |  |