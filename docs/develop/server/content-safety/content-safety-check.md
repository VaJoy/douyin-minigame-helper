---
title: "内容安全检测"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/content-safety/content-safety-check
update_time: 2025-07-23
---

**接口地址：** `POST https://developer.toutiao.com/api/v2/tags/text/antidirt`

**版本：** 1.0.18

检测一段文本是否包含违法违规内容

**鉴权：** `X-Token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `tasks` | Array | 是 | 检测任务列表  **字段** - `0`（Object）： |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |
| `X-Token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `message` | string | 否 | 错误时返回 |  | BodyParam |
| `code` | int64 | 否 | 错误时返回 |  | BodyParam |
| `data` | Array | 否 | 检测结果列表  **字段** - `0`（Object）： |  | BodyParam |
| `error_id` | string | 否 | 错误时返回 |  | BodyParam |
| `exception` | string | 否 | 错误时返回 |  | BodyParam |
| `log_id` | string | 否 | 请求 id |  | BodyParam |

## 请求示例

```bash
curl --location 'https://developer.toutiao.com/api/v2/tags/text/antidirt' \
--header 'X-Token: 080112184639455479586b76302f77664e6942474c2f302b37673d3d' \
--header 'Content-Type: application/json' \
--data '{
  "tasks": [
    {
      "content": "要检测的文本"
    }
  ]
}
'
```

## 成功响应示例

```json
{
  "log_id": "2018112821375501001506902813132",
  "data": [
    {
      "code": 0,
      "task_id": "d0229abe-f312-11e8-966d-0242ac110009",
      "data_id": null,
      "cached": false,
      "predicts": [
        {
          "prob": 1,
          "model_name": "antidirt",
          "target": "default"
        }
      ],
      "msg": "ok"
    }
  ]
}
```

## 异常响应示例

```json
{
  "error_id": "dd60b2bef95f40d7a4ace0bf5130d2e7",
  "code": 401,
  "message": "Authentication credentials were not provided.",
  "exception": "Authentication credentials were not provided."
}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 0 | 

成功

 |  |
| 200 | 401 | 

AccessToken 失效/为空

 |  |
| 200 | 400 | 

tasks 数组为空

 |  |