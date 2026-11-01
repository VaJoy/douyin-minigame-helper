---
title: "genStableAccessToken"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/gen-stable-access-token
update_time: 2025-07-31
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/stable_token`

**版本：** 1.0.38

区别于 getAccessToken OpenAPI在每次调用时会生成新的access_token，并将上次获取的token有效期设置为5分钟（需要开发者构建服务实现定时刷新逻辑），getStableAccessToken OpenAPI用于获取在有效期内稳定不变的access_token，支持开发者任意服务需要时直接调用获取而不用实现单独的定时刷新逻辑集中管理。有两种模式：

- 普通模式：在 access_token 有效期内重复调用该接口不会更新 access_token，会直接返回当前值
- 强制刷新模式：调用时会让当前有效期内的 access_token 立即失效，重新生成新的 access_token

开发者自己需妥善保护稳定版的 access_token 避免泄露，若发现有泄露需及时使用强制刷新模式生成新的 access_token。

生成在有效期内稳定不变的接口调用凭据

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `appid` | string | 是 | 小游戏开发者账号唯一凭证即AppID，可在开发者平台获取 |  | BodyParam |
| `force_refresh` | boolean | 否 | 是否强制刷新，默认使用 false |  | BodyParam |
| `grant_type` | string | 是 | 授权类型，传固定值 client_credential |  | BodyParam |
| `secret` | string | 是 | 小游戏开发者账号唯一凭证的密钥即AppSecret，可在开发者平台获取 |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `log_id` | string | 是 | 请求日志ID |  | BodyParam |
| `data` | Object | 是 | **字段** - `expires_in`（int64）：凭证有效的剩余时间，单位：秒 - `access_token`（string）：获取到的凭证 |  | BodyParam |
| `err_msg` | string | 是 | 错误信息 |  | BodyParam |
| `err_no` | int | 是 | 错误码 |  | BodyParam |

## 请求示例

```bash
curl --location --request POST 'https://minigame.zijieapi.com/mgplatform/api/apps/stable_token' \
--header 'content-type: application/json' \
--data '{"appid":"ttf5d6836abcdeffbc02","secret":"eab8re3fdsaur3nf8789x0feeye","grant_type":"client_credential","force_refresh":false}'
```

## 成功响应示例

```json
{
    "data": {
        "access_token": "080112184745453432574e56596b44504a385579365368416b413d3d",
        "expires_in": 7200
    },
    "err_msg": "",
    "err_no": 0,
    "log_id": "20250520193036E7194E7CB37873E5C680"
}
```

## 异常响应示例

```json
{
    "data": {},
    "err_msg": "请求过于频繁，请稍后再试",
    "err_no": 28005139,
    "log_id": "20250520193036E7194E7CB37873E5C680"
}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 28005139 | 

请求过于频繁，请稍后再试

 | 

等待一段时间后再请求

 |
| 200 | 28001038 | 

参数错误

 | 

仔细检查appid、secret、grant_type等参数是否合法

 |
| 200 | 28001005 | 

系统内部错误

 | 

重试请求或联系oncall排查

 |

## 使用限制

普通模式，单个appid限制每分钟最多请求1w次，每天50w次；强制刷新模式，单个 appid 限制每天最多调用20次。