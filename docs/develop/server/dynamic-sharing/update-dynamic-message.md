---
title: "更新动态消息"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/dynamic-sharing/update-dynamic-message
update_time: 2025-07-31
---

**接口地址：** `POST https://minigame.zijieapi.com/mgplatform/api/apps/share/update_dynamic_message`

**版本：** 1.0.60

修改被分享的动态消息，详见[动态消息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/social-interaction/share-team-access-guide)。

**鉴权：** `access-token`（string；

服务端 API 调用标识，<a href="https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token/" target="_blank" rel="nofollow" class="syl-link">获取方法</a>

）

## 请求参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `query` | string | 否 | 状态 1 时有效，点击「进入」启动小游戏时传递的查询字符串（query），必须是 key1=val1&key2=val2 的格式。从这条转发消息进入后，可通过 [tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/lifecycle/tt-get-launch-options-sync) 或[tt.onShow](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/foundation/system/lifecycle/tt-on-show)获取启动参数中的 query 用来实现信息透传。 |  | BodyParam |
| `target_state` | int | 是 | 消息状态。状态0表示组队中；状态1表示已开始。 |  | BodyParam |
| `template_info` | Array | 否 | 消息模板的初始参数。  **字段** - `0`（Object）： |  | BodyParam |
| `version_type` | string | 否 | 状态 1 时必填，指定通过此消息启动的小游戏版本，默认为 current (线上版)，可设为 latest (开发版) 用于测试。 |  | BodyParam |
| `activity_id` | string | 是 | 消息唯一ID，从[createActivityID](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/social-interaction/team-share-ability/create-activity-id)中获取。 |  | BodyParam |
| `content-type` | string | 是 | 固定值"application/json" |  | HeaderParam |
| `access-token` | string | 是 | 调用[https://minigame.zijieapi.com/mgplatform/api/apps/v2/token](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token)生成的token | 08011218462b6b4b5054626e426e50685a7554643144644449413d3d | HeaderParam |

## 返回参数
| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `err_msg` | string | 是 | err_no非0时对应的错误信息文案提示，成功时为空字符串 |  | BodyParam |
| `err_no` | int | 是 | 错误码，0表示成功 |  | BodyParam |
| `log_id` | string | 是 | 日志id，排查定位问题使用 |  | BodyParam |

## 请求示例

```bash
curl --location 'https://minigame.zijieapi.com/mgplatform/api/apps/share/update_dynamic_message' \
--header 'access-token: 08011218462b4b54307662766c3150454833752b353739513d3d' \
--header 'Content-Type: application/json' \
--data '{
    "access_token": "08011218462b4b54307662766c3150454833752b353739513d3d",
    "activity_id": "562176002",
    "target_state": 0,
    "query": "?room_id=48796951",
    "version_type": "",
    "template_info": [
        {
            "name": "memberCount",
            "value": "2"
        },
        {
            "name": "roomLimit",
            "value": "3"
        }
    ]
}
'
```

## 成功响应示例

```json
{"err_no":0,"err_msg":"","log_id":"202407301711006405CAE372F768C1F110"}
```

## 异常响应示例

```json
{"err_msg":"TargetState 为 0 时，必须传入合法的 member_count 和 room_limit","err_no":28001038,"log_id":"2024073116513060B8B22555BD305E72B4"}
```

## 错误码
| HTTP 状态码 | 错误码 | 描述 | 处理建议 |
| --- | --- | --- | --- |
| 200 | 28001005 | 系统内部错误，请重试 | 请求重试，若依然无解请向平台提交反馈 |
| 200 | 28001038 | 参数不合法 | 根据错误信息检查请求参数是否填写正常 |
| 200 | 28001003 | access_token无效 | 重新请求生成access_token |
| 200 | 28001008 | access_token过期,请刷新或重新授权 | 重新请求生成access_token |
| 200 | 28001016 | 当前应用已被封禁或下线 | clientKey被封禁或者下线 |
| 200 | 28001006 | 网络调用错误，请重试 | 重试即可 |
| 200 | 28001014 | 应用未授权任何能力 | 确认应用是否授权能力 |
| 200 | 28001018 | 应用未获得该能力 | 开通相关能力 |
| 200 | 28003017 | quota已用完 | 联系平台处理 |
| 200 | 28001019 | 应用该能力已被封禁 | 该能力被封禁，联系平台处理 |