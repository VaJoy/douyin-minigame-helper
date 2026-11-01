---
title: "生成活动ID"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/dynamic-sharing/create-activity-id
update_time: 2025-07-31
---

**接口地址：** `GET https://minigame.zijieapi.com/mgplatform/api/apps/share/create_activity_id`

**版本：** 1.0.74

创建被分享动态消息的消息ID。详见[动态消息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/social-interaction/share-team-access-guide)。

**鉴权：** `access-token`（string；

服务端 API 调用标识，<a href="https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token/" target="_blank" rel="nofollow" class="syl-link">获取方法</a>

）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |
| `access-token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `data` | Object | 否 | 详细信息  **字段** - `activity_id`（string）：消息唯一ID - `expire_time`（int64）：消息过期时间 |  | BodyParam |
| `err_msg` | string | 是 | err_no非0时对应的错误信息文案提示，成功时为空字符串 |  | BodyParam |
| `err_no` | int | 是 | 错误码，0表示成功 |  | BodyParam |
| `log_id` | string | 是 | 日志id，排查定位问题使用 |  | BodyParam |

## 请求示例

```bash
curl --location 'https://minigame.zijieapi.com/mgplatform/api/apps/share/create_activity_id' \
--header 'access-token: 08011218462b632f7a6e653648614531757958753676696763513d3d'
```

## 成功响应示例

```json
{
    "data": {
        "activity_id": "2635901698",
        "expire_time": 1722501946
    },
    "err_msg": "",
    "err_no": 0,
    "log_id": "202407311645463A2EC4B3497B00DE644C"
}
```

## 异常响应示例

```json
{
    "err_msg": "AccessToken 无效",
    "err_no": 28001038,
    "log_id": "2024073116464127E1F986775F3B8461AD"
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
| 200 | 28001038 | 参数不合法 | 根据错误信息检查请求参数是否填写正常 |