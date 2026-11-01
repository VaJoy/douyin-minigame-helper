---
title: "查询Schema"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/schema/query-schema-info
update_time: 2025-07-31
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/schema/query_info`

**版本：** 1.0.201

查询已经生成的schema的信息（过期的schema返回"schema不存在或已失效"）。

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `schema` | string | 是 | 生成的schema |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |
| `access-token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `log_id` | string | 是 | 日志id |  | BodyParam |
| `data` | Object | 否 | 详细信息  **字段** - `app_id`（string）：小游戏id - `create_time`（int64）：创建时间 - `expire_time`（int64）：到期失效时间 - `path`（string）：页面路径 - `query`（string）：query（json形式） - `version_type`（string）：小游戏版本 |  | BodyParam |
| `err_msg` | string | 是 | 错误信息 |  | BodyParam |
| `err_no` | int | 是 | 错误码 |  | BodyParam |

## 请求示例

```bash
curl --location --request POST 'https://minigame.zijieapi.com/mgplatform/api/apps/schema/query_info' \
--header 'access-token: 0801121846735352506a356a6' \
--header 'content-type: application/json' \
--data '{
  "schema": "sslocal://microgame?app_id=tt411***&bdp_log=%7B%22enter_from_merge%22%3A%22share_alert%22%2C%22enter_position%22%3A%22z_link%22%2C%22entrance_form%22%3A%22share%22%2C%22launch_from%22%3A%22share_zlink%22%2C%22location%22%3A%22message%22%7D&query=%7B%22page%22%3A%22abc%22%2C%22type%22%3A6%7D&scene=024012&uniq_id=S2025060316421784319298209263721021449ae2822a0f82&version=v2&version_type=current&bdpsum=e135db4"
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
        "create_time": 1748940137,
        "expire_time": 1749522180,
        "path": "",
        "query": "{\"page\":\"abc\",\"type\":6}",
        "version_type": "current"
    },
    "err_msg": "",
    "err_no": 0,
    "log_id": "20250603191312E29F073EEA970C502539"
}
```

## 异常响应示例

```json
{
    "BaseResp": {
        "StatusCode": 0,
        "StatusMessage": ""
    },
    "data": {
        "app_id": "tt411***",
        "create_time": 1748940137,
        "expire_time": 1749522180,
        "path": "",
        "query": "{\"page\":\"abc\",\"type\":6}",
        "version_type": "current"
    },
    "err_msg": "",
    "err_no": 0,
    "log_id": "20250603191312E29F073EEA970C502539"
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
| 200 | 28005077 | 

schema不存在或已失效

 |  |