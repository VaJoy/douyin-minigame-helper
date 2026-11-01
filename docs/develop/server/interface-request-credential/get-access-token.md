---
title: "getAccessToken"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token
update_time: 2025-07-31
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/v2/token`

**版本：** 1.0.25

access_token 是小游戏的全局唯一调用凭据，开发者调用小游戏支付时需要使用 access_token。access_token 的有效期为 2 个小时，需要定时刷新 access_token，重复获取会导致之前一次获取的 access_token 的有效期缩短为 5 分钟。

**Bug & Tip**

- Tip: token 是小游戏级别 token，不要为每个用户单独分配一个 token，会导致 token 校验失败。建议每小时更新一次即可。
- Tip: 原域名 https://developer.toutiao.com/api/apps/xxx 仍然可用，不过为了后续兼容性和可能的迁移，建议开发者更换到新的域名。
- Tip: 为了保障应用的数据安全，只能在开发者服务器使用 AppSecret；开发者服务器不应该把会话密钥下发到小游戏，也不应该对外提供这个密钥。如果小游戏存在泄露 AppSecret 或会话密钥的问题，字节小游戏平台将有可能下架该小游戏，并暂停该小游戏相关服务。

access_token 是小游戏的全局唯一调用凭据，开发者调用小游戏支付时需要使用 access_token。access_token 的有效期为 2 个小时，需要定时刷新 access_token，重复获取会导致之前一次获取的 access_token 的有效期缩短为 5 分钟。

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `secret` | string | 是 | 小游戏的 APP Secret，可以在开发者后台获取 | 98*******************92 | BodyParam |
| `appid` | string | 是 | 小游戏 ID | tt411d37a0de37d565 | BodyParam |
| `grant_type` | string | 否 | 获取 access_token 时值为 client_credential | client_credential | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `data` | Object | 是 | **字段** - `expires_at`（int64）：access_token 过期时间戳 - `expires_in`（int64）：access_token 有效时间，单位：秒 - `access_token`（string）：获取的 access_token |  | BodyParam |
| `err_no` | int64 | 是 | 错误码 | 0 | BodyParam |
| `err_tips` | string | 是 | 错误信息 | success | BodyParam |

## 请求示例

```bash
curl -X POST \
 -H "content-type: application/json" \
 -d '{"appid":"tt**********65","secret":"98*******************92","grant_type":"client_credential"}' \
 https://minigame.zijieapi.com/mgplatform/api/apps/v2/token
```

## 成功响应示例

```json
{
  "err_no": 0,
  "err_tips": "success",
  "data": {
    "access_token": "0801121***********",
    "expires_in": 7200
  }
}
```

## 异常响应示例

```json
{
  "err_no": 40017,
  "err_tips": "bad secret",
  "data": {
    "access_token": "",
    "expires_in": 0
  }
}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 0 | 请求成功 | 暂无 |
| 200 | -1 | 系统错误 |  |
| 200 | 40015 | appid 错误 |  |
| 200 | 40017 | secret 错误 |  |
| 200 | 40020 | grant_type 不是 client_credential |  |
