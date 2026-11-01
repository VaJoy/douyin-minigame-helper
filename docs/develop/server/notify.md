---
title: "订阅消息"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/notify
update_time: 2025-07-31
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/subscribe_notification/developer/v1/notify`

**版本：** 1.0.59

用户产生了订阅模板消息的行为后，可以通过这个接口发送模板消息给用户，功能参考[订阅消息能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/subscribe-message/introduce)。

## Bug & Tip

- 请求 body 的Content-Type限定为application/json。
- 对单个用户推送消息，频率限制为 1 次/秒。
- 订阅消息分为一次性订阅和长期订阅（内测中），详情参考[订阅消息能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/subscribe-message/introduce)。

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `data` | Object | 否 | **字段** - `_key`（string）： - `_val`（string）： | {"名次": 1, "奖励": "500钻石", "领取时间": "202x-0x-xx"}} | BodyParam |
| `access_token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | BodyParam |
| `open_id` | string | 否 |  | vziikC*******FR9 | BodyParam |
| `page` | string | 否 |  |  | BodyParam |
| `tpl_id` | string | 否 | 平台返回已分配的模板 ID | MSG*********5237304 | BodyParam |
| `app_id` | string | 否 |  | tt411d37a0de37d565 | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `err_no` | int64 | 否 |  | 0 | BodyParam |
| `err_tips` | string | 否 |  |  | BodyParam |

## 请求示例

```bash
curl -X POST \
 -H "content-type: application/json" \
 -d '{"access_token":"080112********6b6c537666514d413d3d","app_id":"tt4*********65","tpl_id":"MSG*********5237304","open_id":"vziikC*******FR9","page":"","data":{"名次": 1, "奖励": "500钻石", "领取时间": "202x-0x-xx"}}' \
 https://minigame.zijieapi.com/mgplatform/api/apps/subscribe_notification/developer/v1/notify
```

## 成功响应示例

```json
{
  "err_no": 0,
  "err_tips": ""
}
```

## 异常响应示例

```json
{
  "err_no": 1001,
  "err_tips": "app_id / open_id不合法"
}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 0 | 成功 |  |
| 200 | 1000 | 参数格式有误 |  |
| 200 | 1001 | 参数内容有误 |  |
| 200 | 1008 | 通知内容违规 |  |
| 200 | 1009 | 推送消息能力被封禁 |  |
| 200 | 1010 | 发送消息过于频繁 |  |
| 200 | 2000 | 服务内部错误 |  |
| 200 | 28006003 | 

限流（qps上限为1000）

 |  |
| 200 | 28014043 | 

用户未订阅该模板

 |  |