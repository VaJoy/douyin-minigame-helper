---
title: "查询用户群标签"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/game-group-tag/get-user-group-tag
update_time: 2025-07-31
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/group_tag/get_user_group_tag`

**版本：** 1.0.239

查询用户群标签（已删除的不会返回）

查询用户铭牌

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `mp_id` | string | 是 | 小游戏 appid |  | BodyParam |
| `open_id` | string | 是 |  |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |
| `access-token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `err_no` | int | 是 |  |  | BodyParam |
| `log_id` | string | 是 |  |  | BodyParam |
| `user_group_tag_list` | Array | 是 | **字段** - `0`（Object）： |  | BodyParam |
| `err_msg` | string | 是 |  |  | BodyParam |

## 请求示例

```bash
curl --location 'https://minigame.zijieapi.com/mgplatform/api/apps/group_tag/get_user_group_tag' \
--header 'access-token: 080112184745766e56626b6f72324f63445433655271704353413d3d' \
--header 'Content-Type: application/json' \
--data '{
    "mp_id": "tt411d37a0de37d565",
    "open_id": "GOV.64fFjLb7xaEY"
}'
```

## 成功响应示例

```json
{
    "BaseResp": {
        "StatusCode": 0,
        "StatusMessage": ""
    },
    "err_msg": "",
    "err_no": 0,
    "log_id": "20250723113624C502D1DD796BBE1A7E9D",
    "user_group_tag_list": [
        {
            "status": 1,
            "tag_id": "547998720770",
            "template_id": "546358272258"
        }
    ]
}
```

## 异常响应示例

```json
{
    "BaseResp": {
        "Extra": {
            "oerror_inner_error": "",
            "oerror_origin_code": "28001005",
            "oerror_penetrate_data": "",
            "oerror_stability": "1"
        },
        "StatusCode": 28001005,
        "StatusMessage": "系统内部错误，请重试"
    },
    "err_msg": "系统内部错误，请重试",
    "err_no": 28001005,
    "log_id": "202507231137291060BA897F80A124ED35",
    "user_group_tag_list": []
}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 28001003 | access_token无效 | 重新请求生成access_token |
| 200 | 28001004 | open_id invalid | 检查入参 |
| 200 | 28006062 | mp_id 非法 | 检查入参 |
| 200 | 28006066 | status 非法 | 检查入参 |
| 200 | 28001005 | 系统内部错误，请重试 |  |
