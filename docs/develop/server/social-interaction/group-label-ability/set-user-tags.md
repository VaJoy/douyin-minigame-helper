---
title: "设置用户群标签"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/social-interaction/group-label-ability/set-user-tags
update_time: 2025-11-27
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/group_tag/set_user_group_tag`

**版本：** 1.0.239

设置用户群标签

设置用户铭牌

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `status` | int | 是 | 用户铭牌标签状态: 1-已佩戴 3-已删除 |  | BodyParam |
| `tag_id` | string | 是 | 铭牌id |  | BodyParam |
| `mp_id` | string | 是 | 小游戏 appid |  | BodyParam |
| `open_id` | string | 是 |  |  | BodyParam |
| `access-token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | HeaderParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `err_msg` | string | 是 |  |  | BodyParam |
| `err_no` | int | 是 |  |  | BodyParam |
| `is_sandbox_request` | boolean | 是 |  |  | BodyParam |
| `log_id` | string | 是 |  |  | BodyParam |

## 请求示例

```bash
curl --location 'https://minigame.zijieapi.com/mgplatform/api/apps/group_tag/set_user_group_tag' \
--header 'access-token: 080112184746516d61724a654242634f644b51447862474153413d3d' \
--header 'Content-Type: application/json' \
--data '{
    "mp_id": "tt411d37a0de37d565",
    "open_id": "GOV.64fFjLb7xaEY",
    "tag_id": "547998720514",
    "status": 1
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
    "is_sandbox_request": false,
    "log_id": "202507231122476FA277E45138900629A7"
}
```

## 异常响应示例

```json
{
    "BaseResp": {
        "Extra": {
            "oerror_inner_error": "",
            "oerror_origin_code": "28006067",
            "oerror_penetrate_data": "",
            "oerror_stability": "0"
        },
        "StatusCode": 28006067,
        "StatusMessage": "标签不存在"
    },
    "err_msg": "标签不存在",
    "err_no": 28006067,
    "is_sandbox_request": false,
    "log_id": "20250723112303CBA55B70228C634AC6DB"
}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 28001004 | open_id invalid | 检查入参 |
| 200 | 28006062 | mp_id 非法 | 检查入参 |
| 200 | 28006065 | tag_id 非法 | 检查入参 |
| 200 | 28006066 | status 非法 | 检查入参 |
| 200 | 28006063 | 当前标签已过期 | 前往「运营能力」-「游戏群标签能力」进行有效期调整 |
| 200 | 28006064 | 当前标签状态不支持设置用户标签 | 待上架、已上架状态的标签才允许调用 |
| 200 | 28006067 | 标签不存在 | 检查入参 |
| 200 | 28001005 | 系统内部错误，请重试 |  |
| 200 | 28001003 | access_token无效 | 重新请求生成access_token |
