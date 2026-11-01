---
title: "消息推送客服"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/message-push-customer-service
update_time: 2025-04-16
---

> 为了更好的给您提供服务，小6客服和消息推送客服全面升级为【抖音客服平台】，请尽快完成迁移升级，小6客服和消息推送客服将在2025年6月30日 关闭服务
**填写服务配置**
开发者使用账号登录抖音开放平台后，按提示填写相关信息，具体如下：
- URL：开发者用来接收消息的接口 URL。开发者所填写的 URL 默认以 `https://` 开头，端口为 `443`。
- Token：开发者可以任意填写，用作生成签名，长度 3 ～ 32 个字符。
- 选择消息数据格式：JSON 格式（默认）或 XML 格式。
**验证消息来自抖音小游戏**
开发者提交信息后，抖音小游戏服务器将发送 GET 请求到填写的服务器地址 URL 上，所携带的参数如下表所示：

| 参数 | 描述 |
| --- | --- |
| signature | 加密签名，signature 结合了开发者填写的 token 参数和请求中的 timestamp 参数、nonce 参数 |
| timestamp | 时间戳 |
| nonce | 随机数 |
| msg | 消息信息 |
| echostr | 随机字符串 |

开发者通过校验 signature 来判断请求是否来自于抖音小游戏服务器。signature 生成方式为：
1. 将开发者填写的 token、timestamp、nonce、msg 四个参数进行字典序排序，并拼接(不用任何符号，直接拼接)成一个字符串。
1. 将上一步得到的字符串进行 sha1 加密。
开发者将获得加密后的字符串与 signature 对比，如果相同，则可以认为请求来自于抖音小游戏服务器，请原样返回 echostr 参数的内容（内容前后不加单引号或双引号，直接返回文本字符串），抖音小游戏服务器收到回复之后进行对比，相同则保存客服配置信息并开启消息推送客服。
**接收消息**
开启消息推送之后，用户发送的所有消息，抖音小游戏服务器将会通过 POST 请求发送到开发者配置的 URL，格式为 JSON 或者 XML，开发者将收到的消息自行验证解密。转发用户消息到开发者服务器时，如果两秒内没收到响应，将认为失败，然后 sleep 几秒再重试，总共重试三次。每条消息都包含一个 CreateTime 字段，当收到多条消息时，可以根据 FromUserName 和 CreateTime 两个字段进行重排序。
开发者服务器收到请求必须作出相应的回复，以便抖音小游戏服务器判断消息发送情况，回复方式建议：
1. 直接回复 success 或者长度为 0 的空串。
1. 其他。
第一种情况，抖音小游戏服务器才会认为消息发送成功，第二种情况认为失败并也不会重试。
**文本消息**
用户在客服聊天中发送文本消息时将产生如下的数据包：
**XML 格式**

```xml
 <xml>
   <ToUserName><![CDATA[appid]]></ToUserName>
   <FromUserName><![CDATA[openid]]></FromUserName>
   <CreateTime>1577364225</CreateTime>
   <MsgType><![CDATA[text]]></MsgType>
   <Content><![CDATA[text content]]></Content>
</xml>
```

**JSON 格式**

```json
{
  "ToUserName": "appid",
  "FromUserName": "openid",
  "CreateTime": 1577364225,
  "MsgType": "text",
  "Content": "text content"
}
```

**参数解释**

| 参数 | 说明 |
| --- | --- |
| ToUserName | 小游戏的 ID |
| FromUserName | 发送消息用户的 openid |
| CreateTime | 消息创建时间 |
| MsgType | 消息类型(text) |
| Content | 文本消息内容 |

**图片消息**
用户在客服聊天中发送图片消息时将产生如下的数据包： **XML 格式**

```xml
 <xml>
   <ToUserName><![CDATA[appid]]></ToUserName>
   <FromUserName><![CDATA[openid]]></FromUserName>
   <CreateTime>1577364225</CreateTime>
   <MsgType><![CDATA[image]]></MsgType>
   <PicUrl><![CDATA[this is image url link]]></PicUrl>
</xml>
```

**JSON 格式**

```json
{
  "ToUserName": "appid",
  "FromUserName": "openid",
  "CreateTime": 1577364225,
  "MsgType": "image",
  "PicUrl": "this is image url link"
}
```

**参数说明**

| 参数 | 说明 |
| --- | --- |
| ToUserName | 小游戏的 ID |
| FromUserName | 发送消息用户的 openid |
| CreateTime | 消息创建时间 |
| MsgType | 消息类型(image) |
| PicUrl | 图片链接 |

**发送客服消息接口**
## 使用限制
无
## 接口说明
收到用户发来的消息之后，开发者可以通过调用抖音小游戏平台提供的接口回复客服消息给用户，当用户不在线时，会以消息通知的形式发送到用户
## 基本信息

| 名称 | 描述 |
| --- | --- |
| HTTP URL | `https://developer.toutiao.com/api/apps/message/custom/send?access_token={accesstoken}` |
| HTTP Method | POST |

## 请求头

| 名称 | 字段类型 | 是否必填 | 示例 | 描述 |
| --- | --- | --- | --- | --- |
| content-type | String | 是 |  | 固定值"application/json" |

## 请求参数

| 参数名 | 类型 | 必传 | 描述 |
| --- | --- | --- | --- |
| access_token | 字符串 | 是 | 获取方式见 [getAccessToken](https://developer.open-douyin.com/docs/resource/zh-CN/interaction/develop/server/interface-request-credential/get-access-token/)，获取到的值以参数形式拼接到 url 后面 |
| open_id | 字符串 | 是 | 用户的 openid |
| msg_type | 字符串 | 是 | 消息类型，文本消息为 text，图片消息为 image |
| content | 字符串 | msg_type 为 text 时必传 | 文字消息 |
| pic_url | 字符串 | msg_type 为 image 时必传 | 图片链接 |

## 请求示例

```bash
curl --location 'https://developer.toutiao.com/api/apps/message/custom/send?access_token={accesstoken}' \
--header 'Content-Type: application/json' \
--data '{
    "access_token": "xxx",
    "open_id": "xxx",
    "msg_type": "text",
    "content": "123"
}' 
```

## 响应参数

| 参数名 | 类型 | 描述 |
| --- | --- | --- |
| errno | 整型 | 错误码 |
| msg | 字符串 | 描述信息 |

## 响应示例
### 正常示例

```text
{
  "error": 0
}
```

### 异常示例

```text
{
  "error": -3,
  "msg": "bad access token"
}
```

## 错误码

| HTTP 状态码 | 错误码 | 错误码描述 | 排查建议 |
| --- | --- | --- | --- |
| 200 | 0 | 请求成功 |  |
| 200 | -1 | 内部错误 | 稍后重试，还是不行反馈到抖音小游戏平台 |
| 200 | -2 | 消息限制 | 根据提示操作 |
| 200 | -3 | 参数错误 | 根据提示操作 |

### Bug & Tip
- 请求 body 的`Content-Type`限定为`application/json`
