---
title: "resetSessionKey"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/log-in/reset-session-key
update_time: 2025-07-31
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/reset_session_key`

**版本：** 1.0.38

重置服务器所保存的登录态 session_key 并返回新值

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `openid` | string | 是 | 用户唯一标识符 |  | BodyParam |
| `sig_method` | string | 是 | 用户登录态key的签名方法，目前只支持 hmac_sha256 |  | BodyParam |
| `access_token` | string | 是 | 调用https://developer.toutiao.com/api/apps/v2/token生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | BodyParam |
| `signature` | string | 是 | 用户登录态key的签名 |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `session_key` | string | 是 | 重置后的用户登录态key |  | BodyParam |
| `err_msg` | string | 是 | 错误信息 |  | BodyParam |
| `err_no` | int | 是 | 错误码 |  | BodyParam |
| `log_id` | string | 是 | 请求日志ID |  | BodyParam |
| `openid` | string | 是 | 用户唯一标识符 |  | BodyParam |

## 请求示例

```bash
curl --location --request POST 'https://minigame.zijieapi.com/mgplatform/api/apps/reset_session_key' \
--header 'content-type: application/json' \
--data '{"openid":"_000nHq5DzNNC9QsWOEE_AJBEXS-b01ol-F3","signature":"2e62381e164b0142bbf9cdb11417f15cc74efbd89e800654f90f673bd14e7176","sig_method":"hmac_sha256","access_token":"08011218474545706841787465683273643369666d6a703377513d3d"}'
```

## 成功响应示例

```json
{
    "err_msg": "",
    "err_no": 0,
    "log_id": "20250520145051C7448147A7B8F68A9D52",
    "openid": "_000nHq5DzNNC9QsWOEE_AJBEXS-b01ol-F3",
    "session_key": "dkLWEVhjZBJ0zh3zaPKBOg=="
}
```

## 异常响应示例

```json
{
    "err_msg": "access_token无效",
    "err_no": 28001003,
    "log_id": "20250520145051C7448147A7B8F68A9D52",
    "openid": "",
    "session_key": ""
}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 28001003 | access_token无效 | 获取最新的有效的access_token |
| 200 | 28001004 | openID无效 | 检查openID是否正确 |
| 200 | 28001038 | 参数错误 | 检查sig_method是否正确 |
| 200 | 28001039 | 签名不正确 | 检查signature的计算过程是否正确 |
| 200 | 28005139 | 请求过于频繁，请稍后再试 | 等待一段时间后重试 |
| 200 | 28001005 | 系统内部错误，请重试 | 重试请求或提oncall排查 |

## 使用限制

单个appid下每分钟不能超过6w次
