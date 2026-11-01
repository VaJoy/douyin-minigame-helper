---
title: "公会群解绑"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/social-interaction/guild-group-ability/unbind-group
update_time: 2025-11-27
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/share/unbind_union_group`

**版本：** 1.0.41

开发者可以主动在工会长长期未上线，但是绑定关系一直存在的时候主动调用此接口解绑公会群

工会长解绑公会群

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `union_id` | string | 是 | 游戏自维护的工会ID |  | BodyParam |
| `mp_id` | string | 是 | 小游戏ID |  | BodyParam |
| `access-token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | HeaderParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `err_no` | int | 是 | 错误码，0表示成功 |  | BodyParam |
| `log_id` | string | 是 | 日志id，排查定位问题使用 |  | BodyParam |
| `err_msg` | string | 是 | err_no非0时对应的错误信息文案提示，成功时为空字符串 |  | BodyParam |

## 请求示例

```bash
curl --location --request POST 'https://minigame.zijieapi.com/mgplatform/api/apps/share/unbind_union_group' \
--header 'content-type: application/json' \
--header 'access-token: 08011218462b6b4b5054626e426e50685a7554643144644449413d3d' \
--data '{"union_id":"732328938203892083", "mp_id":"tt411d37a0de37d565"}'
```

## 成功响应示例

```json
{"err_msg":"","log_id":"20250102232455329302AGDBDEDE","err_no":0}
```

## 异常响应示例

```json
{"err_msg":"access_token无效","log_id":"20250103232455329302AGDBDEDE","err_no":28001003}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 28001005 | 系统内部错误，请重试 | 请求重试，若依然无解请向平台提交反馈 |
| 200 | 28001003 | access_token无效 | 重新请求生成access_token |
| 200 | 28001008 | access_token过期,请刷新或重新授权 | 重新请求生成access_token |
| 200 | 28001006 | 网络调用错误，请重试 | 重试即可 |
| 200 | 28001007 | 参数错误 | 请仔细检查相关参数 |
| 200 | 28006046 | 工会未绑定或已解绑 | 当前工会不存在绑定关系 |

## 前置条件

公会群与小游戏存在绑定关系，厂商调用时需校验 AccessToken 是否正确
