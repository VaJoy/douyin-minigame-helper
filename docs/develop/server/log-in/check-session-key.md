---
title: "checkSessionKey"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/log-in/check-session-key
update_time: 2025-07-31
---

**接口地址：** `GET https://minigame.zijieapi.com/mgplatform/api/apps/check_session_key`

**版本：** 1.0.38

校验服务器所保存的登录态 session_key 是否合法

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `signature` | string | 是 | 用户登录态签名 |  | QueryParam |
| `access_token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | QueryParam |
| `openid` | string | 是 | 用户唯一标识符 |  | QueryParam |
| `sig_method` | string | 是 | 用户登录态签名的哈希方法，目前只支持 hmac_sha256 |  | QueryParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `log_id` | string | 是 | 请求日志ID |  | BodyParam |
| `err_msg` | string | 是 | 错误信息 |  | BodyParam |
| `err_no` | int | 是 | 错误码 |  | BodyParam |

## 请求示例

```bash
curl --location --request GET 'https://minigame.zijieapi.com/mgplatform/api/apps/check_session_key?openid=_000nHq5DzNNx9nNWOEE_AJBEXS-b01ol-E5&signature=2e62381e164b0142bbf9cdb11417f15cc74efbd89e800654f90f673bd14e7176&sig_method=hmac_sha256&access_token=080112184745453548436d332b764a35493643713663735074673d3d' \
--header 'content-type: application/json' \
```

## 成功响应示例

```json
{"err_no":0,"err_msg":"","log_id":"20250528154636C3DD5EA834B0BF27F544"}
```

## 异常响应示例

```json
{"err_msg":"access_token无效","err_no":28001003,"log_id":"20250528154636C3DD5EA834B0BF27F544"}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 28001003 | access_token无效 | 重新获取有效的access_token |
| 200 | 28001004 | open_id 无效 | 检查传入的登录用户的openID有效 |
| 200 | 28001038 | 参数错误 | 检查请求参数是否正确，如sig_method |
| 200 | 28001039 | 签名不正确 | 检查生成的签名是否正确 |
