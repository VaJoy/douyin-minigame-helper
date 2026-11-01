---
title: "上报赛事报名用户"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/microgame-competition-upload-player
update_time: 2025-08-07
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/competition/player/upload`

**版本：** 1.0.248

**支持沙箱：** 是

小游戏赛事开始前，用户在游戏内赛事报名后调用此接口上报至平台，将用于赛事活动页展示。请于接入前和平台运营对接赛事相关参数的配置

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `competition_id` | string | 是 | 赛事ID，用于唯一标识一个赛事 |  | BodyParam |
| `open_id` | string | 是 | 用户OpenID |  | BodyParam |
| `player_status` | int | 是 | 参赛状态  **可选值：** SignUpSuccess=报名成功；SignUpCancel=取消报名；Promoted=已晋级；Eliminated=已淘汰 |  | BodyParam |
| `schedule_id` | string | 否 | 赛程ID |  | BodyParam |
| `sign_up_time` | int64 | 否 | 报名时间 |  | BodyParam |
| `app_id` | string | 是 | 小游戏ID |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |
| `access-token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `err_msg` | string | 是 |  |  | BodyParam |
| `err_no` | int | 是 |  |  | BodyParam |
| `log_id` | string | 是 |  |  | BodyParam |

## 请求示例

```bash
curl -X POST "https://minigame.zijieapi.com/mgplatform/api/apps/competition/player/upload" \
-H "access-token: 08011218462b6b4b5054626e426e50685a7554643144644449413d3d" \ 
-H "content-type: application/json" \
-d '{
  "open_id": "ba253642-0590-40bc-40ca", 
  "app_id": "tt1234567", 
  "competition_id": "101",  
  "schedule_id": "1",     
  "player_status": 1,   
  "sign_up_time": 1753773212   
}'
```

## 成功响应示例

```json
{"err_no":0,"err_msg":"","log_id":"20250727iYqFshkJBI"}
```

## 异常响应示例

```json
{"err_no":28001005,"err_msg":"系统错误","log_id":"20250727iYqFshkJBI"}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 28001005 | 系统内部错误，请重试 | 请求重试，若依然无解请向平台提交反馈 |
| 200 | 28001003 | access_token无效 | 重新请求生成access_token |
| 200 | 28001008 | access_token过期,请刷新或重新授权 | 重新请求生成access_token |
| 200 | 28001007 | 参数错误 | 请检查入参是否正确 |

## 使用限制

qps < 10000
