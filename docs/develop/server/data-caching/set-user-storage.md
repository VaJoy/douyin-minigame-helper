---
title: "setUserStorage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/data-caching/set-user-storage
update_time: 2025-07-31
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/set_user_storage`

**版本：** 1.0.24

以 key-value 形式存储用户数据到小程序平台的云存储服务。若开发者无内部存储服务则可接入，免费且无需申请。一般情况下只存储用户的基本信息，禁止写入大量不相干信息。

## Bug&Tip

- Tip：当 key 是开发者所配置的排行榜 key 时，value 的内容应该满足[KVData](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data/kv-data/)所指出的形式，必须是 string 类型，不要传 json struct。
- Tip: 该方法为服务端方法，实际方法效果与前端接口 tt.setUserCloudStorage 一致。通过该接口设置数据后，可以在前端通过 tt.getUserCloudStorage 或 tt.getCloudStorageByRelation 获取。

以 key-value 形式存储用户数据到小程序平台的云存储服务。若开发者无内部存储服务则可接入，免费且无需申请。一般情况下只存储用户的基本信息，禁止写入大量不相干信息。

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `sig_method` | string | 是 | 用户登录态签名的编码方法 |  | QueryParam |
| `signature` | string | 是 | 用户登录态签名 |  | QueryParam |
| `access_token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | QueryParam |
| `openid` | string | 是 | 登录用户唯一标识 |  | QueryParam |
| `kv_list` | Array | 是 | (body 中) 要设置的用户数据  **字段** - `0`（Object）： |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `errmsg` | string | 否 | 错误信息 |  | BodyParam |
| `error` | int | 是 | 错误号, 正确返回时为 0 |  | BodyParam |
| `message` | string | 否 | 错误信息（同 errmsg） |  | BodyParam |
| `errcode` | int | 否 | 详细错误号 |  | BodyParam |

## 请求示例

```bash
curl -X POST \
 -H "content-type: application/json" \
 -d '{"kv_list":[{"key":"test","value":"{\"ttgame\":{\"score\":1}}"}]}' \
https://minigame.zijieapi.com/mgplatform/api/apps/set_user_storage?access_token=080112***********513d3d&openid=v********oFR9&sig_method=hmac_sha256&signature=44b5092fa1c9adba03803239934d4958b8a1840adf0cee8d5e95c1cf5d495e0e
```

## 成功响应示例

```json
{
  "error": 0
}
```

## 异常响应示例

```json
{
  "errcode": 40002,
  "errmsg": "nil access_token",
  "error": 1,
  "message": "nil access_token"
}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 0 | 请求成功 |  |
| 200 | -1 | 系统错误 |  |
| 200 | 40009 | key 长度大于 128 个字节 |  |
| 200 | 40010 | key 和 value 的长度和大于 1024 个字节 |  |
| 200 | 40011 | 排行榜 key 对应的 value 值格式不对，具体见 warning |  |
| 200 | 60001 | 单用户存储 kv 超过 128 对 |  |
