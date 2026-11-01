---
title: "removeUserStorage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/data-caching/remove-user-storage
update_time: 2025-07-31
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/remove_user_storage`

**版本：** 1.0.24

删除存储到字节跳动的云存储服务的 key-value 数据。当开发者不需要该用户信息时，需要删除，以免占用过大的存储空间。

## Bug&Tip

- Tip: 该接口为服务端接口，接口的实际效果与前端 tt.removeUserCloudStorage 一致。

删除存储到字节跳动的云存储服务的 key-value 数据。当开发者不需要该用户信息时，需要删除，以免占用过大的存储空间。

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `access_token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | QueryParam |
| `sig_method` | string | 是 | 用户登录态签名的编码方法 |  | QueryParam |
| `signature` | string | 是 | 用户登录态签名 |  | QueryParam |
| `openid` | string | 是 | 登录用户唯一标识 |  | QueryParam |
| `key` | Array | 是 | (body 中) 要删除的用户数据的 key list  **字段** - `0`（string）： |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `error` | int | 是 | 错误号, 正确返回时为 0 |  | BodyParam |
| `message` | string | 否 | 错误信息（同 errmsg） |  | BodyParam |
| `errcode` | int | 否 | 详细错误号 |  | BodyParam |
| `errmsg` | string | 否 | 错误信息 |  | BodyParam |

## 请求示例

```bash
curl -X POST \
 -H "content-type: application/json" \
 -d '{"key":["test"]}' \
 https://minigame.zijieapi.com/mgplatform/api/apps/remove_user_storage?access_token=080112184***************6f7a57513d3d&openid=vziik******R9&sig_method=hmac_sha256&signature=44b5092fa1c9adba03803239934d4958b8a1840adf0cee8d5e95c1cf5d495e0e
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
