---
title: "游戏币赠送接口"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/mini-game-coin-gift-interface
update_time: 2025-06-03
---

> 本接口应在后端服务器调用
给用户赠送游戏币。开通小游戏支付后，可以通过该接口赠送游戏币给某个用户。**接口调用异常，可以通过相同的订单号再次请求该接口，不会重复奖励**。

```http
POST https://developer.toutiao.com/api/apps/game/wallet/add_coin
```

## 参数说明

| 属性 | 类型 | 默认值 | 是否必填 | 说明 |
| --- | --- | --- | --- | --- |
| openid | string |  | 是 | 用户唯一标识 |
| appid | string |  | 是 | 小程序唯一标识 |
| offer_id | string |  | 否 | 扩展字段，目前未使用，可不填 |
| ts | number |  | 是 | UNIX 时间戳，单位秒 |
| zone_id | string |  | 是 | 游戏服务器大区 id，开发者自定义。游戏不分大区则默认填写"1"。如果应用支持多角色，则角色 ID 接在分区 ID 后，用"_"连接 |
| pf | string |  | 是 | 平台 目前仅为android："android" |
| user_ip | string |  | 否 | 用户外网 IP |
| bill_no | string |  | 是 | 游戏开发者自定义订单号，开发者需要保证全局唯一。相同的订单号不会重复加币。长度不超过 63，只能是数字、大小写字母_- |
| present_counts | number |  | 是 | 赠送游戏币的个数，不能为 0 |
| sig | string |  | 否 | 扩展字段，目前未使用，可不填 |
| access_token | string |  | 是 | [身份验证](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token) |
| mp_sig | string |  | 是 | [支付签名](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/payment-signature-generation-algorithm/),本次请求的所有非空参数+uri+method+支付密钥，用 HMAC-SHA256 签名 |

### 返回值
Object ，包含以下属性

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 错误码 |
| errmsg | string | 错误信息 |
| balance | number | 赠送后的余额 |
| bill_no | string | 赠送游戏币的订单号 |

#### errcode 值类型

| 值 | 说明 |
| --- | --- |
| 0 | 请求成功 |
| -1 | 系统繁忙，此时请开发者稍候再试 |
| 90009 | mp_sig 签名错误 |
| 90010 | 用户未登录或登录态已过期 |
| 90011 | sig 签名错误 |
| 90012 | 订单已存在 |
| 90017 | 没有调用接口的权限 |
| 90018 | 参数错误, 通过 errmsg 进行检查 |

### 代码示例

```json
{
  "openid": "jjiemnnuyiopqmpvmmiji",
  "appid": "tt899008766",
  "ts": 1507530737,
  "zone_id": "1",
  "pf": "android",
  "present_counts": 123,
  "bill_no": "89jjnjkkmmku939",
  "mp_sig": "39271a12d8d56b0395981a0990a9e75ae239c54f419cb6235399fe70acf8ccfb",
  "access_token": "hds2rt6bhgh5wfg5nf4gdh6"
}
```
