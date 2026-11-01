---
title: "选手排名上报"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/microgame-competition-upload-rank
update_time: 2025-08-07
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/competition/rank/upload`

**版本：** 1.0.248

**支持沙箱：** 是

小游戏赛事开始后，可以将游戏内赛事的排名进行上报至平台，将用于赛事活动页展示。请于接入前和平台运营对接赛事相关参数的配置

小游戏赛事相关

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `rank_status` | int | 否 | 排行状态  **可选值：** Starting=；End= |  | BodyParam |
| `ranks` | Array | 是 | 排名  **字段** - `0`（Object）： |  | BodyParam |
| `schedule_id` | string | 否 | 赛程ID |  | BodyParam |
| `app_id` | string | 是 | 小游戏ID |  | BodyParam |
| `competition_id` | string | 是 | 赛事ID |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |
| `access-token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `log_id` | string | 是 |  |  | BodyParam |
| `err_msg` | string | 是 |  |  | BodyParam |
| `err_no` | int | 是 |  |  | BodyParam |

## 请求示例

```bash
curl -X POST "https://minigame.zijieapi.com/mgplatform/api/apps/competition/rank/upload" \
-H "access-token: 08011218462b6b4b5054626e426e50685a7554643144644449413d3d" \ 
-H "content-type: application/json" \ 
-d '{
  "app_id": "tt1234567", 
  "competition_id": "101",       
  "schedule_id": "1",           
  "ranks": [
    {
      "open_id": "ba253642-0590-40bc-40ca", 
      "nickname": "抖音用户xxx",
      "player_source": 1,
      "rank": 1,
      "score": 2000
    },
    {
      "open_id": "ba253642-0590-40bc-50ca", 
      "nickname": "微信用户bbb",
      "player_source": 2,
      "rank": 2,
      "score": 1000
    }
  ],
  "rank_status": 1
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

qps < 10
