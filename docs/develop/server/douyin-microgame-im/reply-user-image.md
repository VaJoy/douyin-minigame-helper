---
title: "回复图片格式的客服消息"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/douyin-microgame-im/reply-user-image
update_time: 2025-05-29
---

## 接口说明
开发者回复图片格式的客服消息，用户发送信息后，可在48小时内，至多回复5条信息
## 基本信息

| 名称 | 描述 |
| --- | --- |
| HTTP URL | https://minigame.zijieapi.com/mgplatform/api/apps/reply/reply_user_image |
| HTTP Method | POST |
| Scope | open.ttgame.mgplatform |

## 请求参数
### 请求头

| Key | 字段类型 | 是否必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| access-token | String | 必填 | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/api-preview?layoutMode=preview-doc-mode)生成的token |
| Content-Type | String | 必填 | multipart/form-data | form-data 格式 |

### Body

| Key | 字段类型 | 是否必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| conversation_id | String | 必填 | 5123024011322180 | 会话ID |
| create_time | Int64 | 必填 | 1743664062 | 消息创建时间 |
| FileContent | Binary | 必填 | - | 图片内容，二进制流格式 |
| micro_game_id | String | 必填 | tt411d37a0de37d565 | 小游戏ID |
| msg_id | String | 必填 | 512302104011322180 | 消息ID，用作幂等使用 |
| msg_type | String | 必填 | image | 消息类型，image-图片类型 |
| sender_name | String | 选填 | - | 绑定的客服人员用户名，对应开平网站的用户名，非必填（不填会导致B端客服平台的发送人为 Error） |

## 请求示例

```bash
curl --location 'http://minigame.zijieapi.com/mgplatform/api/apps/reply/reply_user_image?micro_game_id=tt411d37a0de37d565&conversation_id=7483846274349842751&msg_id=51230312401132218143&create_time=1744106803&sender_name=zxt_test' \
--header 'Content-Type: multipart/form-data' \
--header 'access-token: 0801121847445a6576303563624e384971796a58636c505a4e413d3d' \
--data-binary '@/Users/bytedance/Desktop/174.jpg'
```

## 响应参数
### Body

| Key |  | 字段类型 | 是否必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- | --- |
| err_msg |  | String | 必填 | - | - |
| err_no |  | Int32 | 必填 | - | - |
| log_id |  | String | 必填 | - | 链路日志ID |
| data |  | Struct |  | - | - |
|  | filter_reason | Int32 |  | 1 | 本条消息过滤原因     1：命中敏感词；     2：非小游戏；     3：msg_id 触发幂等；     4：已超过最晚回复时间，距离用户上一次发送消息已超过 48 h     5：回复次数过多，用户发送消息后至多只能回复 5 条；     6：sender_name 不存在，请检查是否为绑定的客服人员用户名 |
|  | im_msg_id | String |  | 7488928630123497499 | IM 返回的消息ID，唯一标识这条消息 |

## 响应示例
正常响应示例

```json
{
    "BaseResp": {
        "StatusCode": 0,
        "StatusMessage": ""
     },
     "data": {
         "im_msg_id": "2131241245"
      },
      "err_msg": "",
      "err_no": 0,
      "log_id": "20250410110755425027FA13AC7A1A60B4"
 }
```

异常响应示例

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

| HTTP 状态码 | 错误码 | 错误码描述 | 排查建议 |
| --- | --- | --- | --- |
| 200 | 28001005 | 系统内部错误，请重试 | 请求重试，若依然无解请向平台提交反馈 |
| 200 | 28001003 | access_token无效 | 重新请求生成access_token |
| 200 | 28001008 | access_token过期,请刷新或重新授权 | access_token过期,请刷新或重新授权 |

curl --location 'http://minigame.zijieapi.com/mgplatform/api/apps/reply/reply_user_image?micro_game_id=tt411d37a0de37d565&conversation_id=7483846274349842751&msg_id=51230312401132218143&create_time=1744106803&sender_name=zxt_test' \--header 'Content-Type: multipart/form-data' \--header 'access-token: 0801121847445a6576303563624e384971796a58636c505a4e413d3d' \
--data-binary '@/Users/bytedance/Desktop/174.jpg'
