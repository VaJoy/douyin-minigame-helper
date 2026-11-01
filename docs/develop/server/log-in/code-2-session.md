---
title: "code2Session"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/log-in/code-2-session
update_time: 2025-07-31
---

**接口地址：** `GET https://minigame.zijieapi.com/mgplatform/api/apps/jscode2session`

**版本：** 1.0.28

通过[tt.login](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/log-in/tt-login/)接口获取到登录凭证后，开发者可以通过服务器发送请求的方式获取 session_key 和 openid。​

## 匿名 openid 数据迁移

![](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/other/17db99c83c9d85eb645629178a388be3_image.png)

## Bug & Tip

- Tip：原域名 https://developer.toutiao.com/api/apps/jscode2session 仍然可用，不过为了后续兼容性和可能的迁移，建议开发者更换到新的域名。
- Tip: 为了保障应用的数据安全，只能在开发者服务器使用 AppSecret；开发者服务器不应该把会话密钥下发到小游戏，也不应该对外提供这个密钥。如果小游戏存在泄露 AppSecret 或会话密钥的问题，字节小游戏平台将有可能下架该小游戏，并暂停该小游戏相关服务。
- Tip：登录凭证 code，anonymous_code 只能使用一次，非匿名需要 code，非匿名下的 anonymous_code 用于数据同步；匿名需要 anonymous_code。

通过tt.login接口获取到登录凭证后，开发者可以通过服务器发送请求的方式获取 session_key 和 openid。
Tip：登录凭证 code，anonymous_code 只能使用一次，非匿名需要 code，非匿名下的 anonymous_code 用于数据同步；匿名需要 anonymous_code。

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `anonymous_code` | string | 否 | tt.login 接口返回的匿名登录凭证（code 和 anonymous_code 至少要有一个） |  | QueryParam |
| `appid` | string | 是 | 小游戏 ID |  | QueryParam |
| `code` | string | 否 | tt.login 接口返回的登录凭证（code 和 anonymous_code 至少要有一个） |  | QueryParam |
| `secret` | string | 是 | 小游戏的 APP Secret，可以在「开发者后台->开发管理->开发设置」获取 |  | QueryParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `anonymous_openid` | string | 否 | 匿名用户在当前小游戏的 ID，如果请求时有 anonymous_code 参数才会返回 |  | BodyParam |
| `message` | string | 否 | 错误信息（同 errmsg） |  | BodyParam |
| `unionid` | string | 否 | 用户在小游戏平台的唯一标识符，请求时有 code 参数才会返回。如果开发者拥有多个小游戏，可通过 unionid 来区分用户的唯一性。 |  | BodyParam |
| `error` | int64 | 是 | 错误号 返回非 0 |  | BodyParam |
| `session_key` | string | 否 | 会话密钥，如果请求时有 code 参数才会返回 |  | BodyParam |
| `openid` | string | 否 | 用户在当前小游戏的 ID，如果请求时有 code 参数才会返回 |  | BodyParam |
| `errcode` | int64 | 否 | 详细错误号 |  | BodyParam |
| `errmsg` | string | 否 | 错误信息 |  | BodyParam |

## 请求示例

```bash
curl -X GET \
 -H "content-type: application/json" \
https://minigame.zijieapi.com/mgplatform/api/apps/jscode2session?appid=tt**********5&secret=988**************92&code=1********3
```

## 成功响应示例

```json
{
  "error": 0,
  "session_key": "ffaaed37bb05d096***",
  "openid": "36d4bd3c8****",
  "anonymous_openid": "",
  "unionid": "f7510d9ab***********"
}
```

## 异常响应示例

```json
{
  "errcode": 40018,
  "errmsg": "bad code",
  "error": 3,
  "message": "bad code"
}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 0 | 请求成功 |  |
| 200 | -1 | 系统错误 |  |
| 200 | 40014 | 未传必要参数，请检查 |  |
| 200 | 40015 | appid 错误 |  |
| 200 | 40017 | secret 错误 |  |
| 200 | 40018 | code 错误 |  |
| 200 | 40019 | anonymous code 错误 |  |
