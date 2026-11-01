---
title: "回复文字格式的客服消息"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/douyin-microgame-im/reply-user-text
update_time: 2025-07-31
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/reply/reply_user_text`

**版本：** 1.0.192

开发者回复文字格式的客服消息

开发者回复消息至C端用户

**鉴权：** `access-token`（string）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `msg_type` | string | 是 | 消息类型，text-文字类型 | text | BodyParam |
| `sender_name` | string | 否 |  | 绑定的客服人员用户名，对应开平网站的用户名，非必填（不填会导致B端客服平台的发送人为 Error） | BodyParam |
| `content` | string | 是 | 文字消息 | 这是一条文字消息 | BodyParam |
| `conversation_id` | string | 是 | 会话ID | 5123024011322180 | BodyParam |
| `create_time` | int64 | 是 | 消息创建时间 | 1743664062 | BodyParam |
| `micro_game_id` | string | 是 | 小游戏ID | tt411d37a0de37d565 | BodyParam |
| `msg_id` | string | 是 | 消息ID，用作幂等处理 | 512302104011322180 | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |
| `access-token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `data` | Object | 否 | **字段** - `im_msg_id`（string）：IM 返回的消息ID，唯一标识这条消息 - `filter_reason`（int）：本条消息过滤原因 1：命中敏感词； 2：非小游戏； 3：msg_id 触发幂等； 4：已超过最晚回复时间，距离用户上一次发送消息已超过 48 h 5：回复次数过多，用户发送消息后至多只能回复 5 条； 6：sender_name 不存在，请检查是否为绑定的客服人员用户名 |  | BodyParam |
| `err_msg` | string | 是 |  |  | BodyParam |
| `err_no` | int | 是 |  |  | BodyParam |
| `log_id` | string | 是 | 链路日志ID |  | BodyParam |

## 请求示例

```bash
curl --location 'http://minigame.zijieapi.com/mgplatform/api/apps/reply/reply_user_text' \
--header 'Content-Type: application/json' \
--header 'access-token: 0801121847445a664742744e5643524d38462f41314d4c736c513d3d' \
--data '{
    "micro_game_id": "tt411d37a0de37d565",
    "conversation_id": "7483846274349842751",
    "msg_id": "5123031140113221826",
    "create_time": 2872345199,
    "msg_type": "link",
    "content": "测试demo\n<a rel=\"noopener noreferrer\" target=\"_blank\" href=\"https://www.baidu.com/\">https://www.baidu.com/</a>"
}'
```

## 成功响应示例

```json
{
    "BaseResp": {
        "StatusCode": 0,
        "StatusMessage": ""
    },
    "data": {
        "im_msg_id": "7488981014917154850"
    },
    "err_msg": "",
    "err_no": 0,
    "log_id": "2025040315151807A9D402BD7DAE61EE0A"
}
```

## 异常响应示例

```json
{
    "BaseResp": {
        "StatusCode": 0,
        "StatusMessage": ""
    },
    "data": {
        "filter_reason": 3,
        "im_msg_id": ""
    },
    "err_msg": "",
    "err_no": 0,
    "log_id": "2025040314545445D52C13C71AB841C33F"
}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 28001005 | 系统内部错误，请重试 | 请求重试，若依然无解请向平台提交反馈 |
| 200 | 28001003 | access_token无效 | 重新请求生成access_token |
| 200 | 28001008 | access_token过期,请刷新或重新授权 | 重新请求生成access_token |
