---
title: "图片检测"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/content-safety/image-detection
update_time: 2025-07-23
---

**接口地址：** `POST https://developer.toutiao.com/api/v2/tags/image`

**版本：** 1.0.18

检测图片是否包含违法违规内容

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `targets` | Array | 是 | 检测任务列表  **字段** - `0`（string）： |  | BodyParam |
| `tasks` | Array | 是 | 检测目标  **字段** - `0`（Object）： |  | BodyParam |
| `X-Token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | HeaderParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `error_id` | string | 否 | 错误时返回 |  | BodyParam |
| `exception` | string | 否 | 错误时返回 |  | BodyParam |
| `log_id` | string | 否 | 请求 id |  | BodyParam |
| `message` | string | 否 | 错误时返回 |  | BodyParam |
| `code` | int64 | 否 | 错误时返回 |  | BodyParam |
| `data` | Array | 否 | 检测结果列表  **字段** - `0`（Object）： |  | BodyParam |

## 请求示例

```bash
curl --location 'https://developer.toutiao.com/api/v2/tags/image/' \
--header 'X-Token: 08011218463941377738715a44544d3842774d704a59756531673d3d' \
--header 'Content-Type: application/json' \
--data '{
  "targets": ["ad", "porn"],
  "tasks": [
    {
      "image": "https://ts1.cn.mm.bing.net/th/id/R-C.748160bf925a7acb3ba1c9514bbc60db?rik=AYY%2bJ9WcXYIMgw&riu=http%3a%2f%2fseopic.699pic.com%2fphoto%2f50017%2f0822.jpg_wh1200.jpg&ehk=CMVcdZMU6xxsjVjafO70cFcmJvD62suFC1ytk8UuAUk%3d&risl=&pid=ImgRaw&r=0"
    }
  ]
}
'
```

## 成功响应示例

```json
{
  "log_id": "2019010320551501001001621510071",
  "data": [
    {
      "code": 0,
      "task_id": "d18197c4-0f56-11e9-99a5-0242ac110004",
      "data_id": null,
      "cached": false,
      "predicts": [
        {
          "prob": 1,
          "model_name": "image_ocr",
          "target": "ad"
        },
        {
          "prob": 0,
          "model_name": "image_qrcode",
          "target": "ad"
        }
      ],
      "msg": "ok"
    },
    {
      "code": 0,
      "task_id": "d1aedc02-0f56-11e9-99a5-0242ac110004",
      "data_id": null,
      "cached": false,
      "predicts": [
        {
          "prob": 0.0005013857153244317,
          "model_name": "image_porn",
          "target": "porn"
        },
        {
          "prob": 0.022131478413939476,
          "model_name": "image_vulgar",
          "target": "porn"
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

AccessToken 失效或者为空

 |  |
| 200 | 400 | 

Tasks 或者 Target 不能为空

 |  |