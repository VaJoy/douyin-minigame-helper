---
title: "推荐流直出游戏能力SPI接入文档"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/feed-game/open-api
update_time: 2025-10-29
---

## 一、开发者需要提供的API
### SPI接入：查询用户就绪场景列表
开发者需要提供一个接口供抖音开放平台查询指定用户的就绪场景列表，以便激活推荐流直出游戏能力（备注：为方便阅读，在本文中推荐流直出游戏能力将被统一**简称为直玩能力/直玩游戏**）的分发。
#### 接口说明

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/bd5467da82c547baa1bd10540179cc58)

直玩能力接入协议交互图

如上图所示，接入直玩能力的开发者需要提供一个用于抖音开放平台查询指定用户存在待促活事件的场景列表的接口，当用户符合出直玩游戏条件时，抖音开放平台会调用开发者的接口来拉取场景列表，根据一定策略排序选取最优场景，将结合厂家信息的游戏分发到推荐流中。
#### 基本信息

| 名称 | 描述 |
| --- | --- |
| HTTP URL | 需要开发者提供，需要支持公网访问 |
| HTTP Method | GET |
| 接口用途 | 查询指定用户存在待促活事件的场景列表 |
| 接口协议 | 接口使用**https**协议（注意，此处不支持仅http协议） |

#### 接口要求
- 合法性校验：以”双向签名+签名校验“的形式来确保请求的合法性，开发者接收到请求时需要按规则校验请求的签名的正确性，确保请求来自于平台；开发者响应请求时需要按规则计算签名并传递签名参数，平台接收到响应时会校验签名的正确性。注意，签名信息无效的响应会被丢弃，导致无法在推荐流中刷出对应直玩游戏。
- 性能要求：从开发者提供的接口拉取数据时，如果拉取请求响应超过300ms或者返回【非2xx】状态码，此时平台认为本次数据拉取失败，会直接放弃此处直玩出卡动作，直到下次符合出卡条件时刻触发时再尝试拉取数据。

| 性能项目 | 具体要求 | 备注 |
| --- | --- | --- |
| 接口耗时 | < 300ms | 查询耗时太长会导致不出直玩游戏，开发者需要做好接口的性能优化和测试工作 |
| SLA | 999+ | SLA指服务等级协议，详细定义可见[SLA定义](https://baike.baidu.com/item/%E6%9C%8D%E5%8A%A1%E7%AD%89%E7%BA%A7%E5%8D%8F%E8%AE%AE/20861172?fr=ge_ala) |
| qps上限 | 峰值qps >= n | 需要开发者确认自己服务可承载的查询qps并在平台接入流程中填写配置，平台会根据开发者提供的数值进行限流保护 |

- 有效性要求：开发者必须保证返回的场景在游戏内一定是就绪状态（如：若该用户游戏内无离线收益，则不可返回表示离线收益就绪的状态），如果因为”货不对板“引起客诉，平台会封禁游戏的直玩能力
#### 请求参数
> 请求由抖音开放平台发送，此处参数提供开发者查看使用
- 请求示例

```bash
# 参数示例：{nonce}
curl --location --globoff 'https://{domain}/{path}?nonce={nonce}&timestamp={timestamp}&openid={openid}&appid={appid}' \
--header 'content-type: application/json' \
--header 'x-signature: GmDFaaUJQ58AAatTmS+kzA=='
```

- 请求头

| 参数形式 | 名称 | 类型 | 是否必填 | 描述 | 示例值 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| Header | x-signature | string | 是 | 请求签名，开发者需要验证签名的正确性，确保请求来自抖音开放平台，而不是其它非法来源方 |  | 计算方式见[推荐流直出游戏能力签名计算方式](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/feed-game/signature)，对应的body参数为空的字符串"" |

- 具体参数

| 参数形式 | 名称 | 类型 | 是否必填 | 描述 | 备注 |
| --- | --- | --- | --- | --- | --- |
| Query | nonce | string | 是 | 签名用的随机字符串，10位，由字母和数字组成 |  |
|  | timestamp | int64 | 是 | 发送消息的秒级时间戳 |  |
|  | openid | string | 是 | 用户openid |  |
|  | appid | string | 是 | 小游戏的appid，可供开发者校验使用 |  |

#### 响应参数
- 响应示例

```bash
// 以下json表示当前用户在游戏内有离线收益可领取
// 注意header需要带上x-signature
{
        "err_no": 0,
        "err_msg": "",
        "data": {
                "scenes": [{
                        "scene": 1,
                        "content_ids": ["CONTENT27648287"],
                        "extra": ""
                }]
        }
}
```

- 响应头：

| 参数形式 | 名称 | 类型 | 是否必填 | 描述 | 示例值 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| Header | content-type | string | 是 | 固定值，为application/json | application/json |  |
|  | x-signature | string | 是 | 返回值签名，开发者返回数据前，需要计算签名，防止伪造和篡改，供抖音平台进行校验，无效的签名会被丢弃，导致游戏不出直玩信息 |  | 计算方式[推荐流直出游戏能力签名计算方式](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/feed-game/signature) |

- 响应体：application/json

| 参数形式 | 名称 | 类型 | 是否必填 | 描述 | 示例值 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| Body | err_no | int32 | 是 | 请求错误码 | 0 | 0代表正常，非0代表错误 |
|  | err_msg | string | 是 | err_no非0时对应的错误信息文案提示，成功时为空字符串 | "" | 错误码规范见下述错误码规范章节 |
|  | data | object | 是 | 响应体的业务数据字段 |  | 关于data里各字段详见下述data结构章节 |

- data结构：

| 字段名 | 类型 | 是否必填 | 描述 | 示例 |
| --- | --- | --- | --- | --- |
| scenes | array | 是 | 就绪状态的场景对象列表，场景值定义见下述scene结构章节 |  |

- scenes的元素结构

| 字段名 | 类型 | 是否必填 | 描述 | 示例 |
| --- | --- | --- | --- | --- |
| scene | int64 | 是 | 就绪的场景值： 1： 离线收益场景 2： 体力恢复场景 3： 重要事件掉落 |  |
| content_ids | array | 是 | 就绪场景对应自定义文案ID列表，由开发者向平台申请生成，具体见下述文案使用方式章节 |  |
| extra | string | 否 | 开发者可为每个场景携带额外的信息，类型是字符串，要求字符串长度 < 100 |  |

#### 签名计算过程
详见[推荐流直出游戏能力签名计算方式](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/feed-game/signature)。
#### 文案使用方式
针对同一场景的不同内容，开发者可以在平台上自定义不同的文案描述，并生成对应的content_id。
示例如下：

| 场景 | 描述 | 场景内容示例 | 审核通过的文案示例 | content_id示例 |
| --- | --- | --- | --- | --- |
| 离线收益场景 | 离线收益场景在推荐页的展示文案 | 游戏内玩家胡萝卜离线收益可领取 | 你的胡萝卜已满，快来领取 | CONTENT123 |
|  |  | 游戏内玩家四叶草离线收益可领取 | 你的四叶草已满，快来领取 | CONTENT456 |
| 体力恢复场景 | 体力恢复场景在推荐页的展示文案 | 游戏内玩家体力恢复完成 | 你的体力已恢复，可以继续游戏了 | CONTENT789 |
| 重要事件掉落场景 | 重要事件掉落场景在推荐页的展示文案 | 游戏内试炼塔挑战就绪 | 你的试炼塔挑战已就绪，快来处理 | CONTENT012 |

以离线收益场景就绪为例，开发者对content_id使用如下：

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/eb9ddf2bfb054309ab2141dc0ad20297)

文案申请和使用流程示意图

#### 错误码规范

> 说明：为了减少开发者的接入工作量，平台规定开发者在返回数据流程中若遇到内部错误等情况统一返回200状态码与空值（即scenes为空数组），但若是平台传参错误或者开发校验签名失败则需要返回对应下述错误码。

| http状态码 | 错误码(err_no) | 错误信息（err_msg） | 描述 |
| --- | --- | --- | --- |
| 200 | 0 | "" | 成功 |
| 200 | 28001007 | "invalid param" | 参数错误 |
| 200 | 28006009 | "check signature failed" | 校验签名失败 |
| 非200 | / | / | 失败 |
