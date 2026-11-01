---
title: "游戏币扣除接口"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/mini-game-coin-deduction-interface
update_time: 2024-07-24
---

> 本接口应在开发者后端服务器调用
扣除游戏币。开通小游戏支付后，可以调用该接口扣除某个用户的游戏币。**接口调用异常，可以通过相同的订单号再次请求该接口，不会重复扣款**。

```http
POST https://developer.toutiao.com/api/apps/game/wallet/game_pay
```

## 参数说明

| 属性 | 类型 | 默认值 | 是否必填 | 说明 |
| --- | --- | --- | --- | --- |
| openid | string |  | 是 | 用户唯一标识 |
| appid | string |  | 是 | 小程序唯一标识 |
| offer_id | string |  | 否 | 扩展字段，目前未使用，可不填 |
| ts | number |  | 是 | UNIX 时间戳，单位秒 |
| zone_id | string |  | 是 | 游戏服务器大区 id，游戏不分大区则默认填写"1"。如果应用支持多角色，则角色 ID 接在分区 ID 后，用"_"连接 |
| pf | string |  | 是 | 平台 安卓：android |
| user_ip | string |  | 否 | 用户外网 IP |
| amt | number |  | 是 | 扣除游戏币数量，不能为 0 |
| bill_no | string |  | 是 | 扣游戏币的开发者订单号，开发者需要保证全局唯一。相同的订单号不会重复扣款。长度不超过 63，只能是数字、大小写字母_- |
| pay_item | string |  | 否 | 游戏道具名，开发者自定义称 |
| app_remark | string |  | 否 | 游戏开发者备注，会写到账户流水。开发者自定义 |
| sig | string |  | 否 | 扩展字段，目前未使用，可不填 |
| access_token | string |  | 是 | [身份验证](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token) |
| mp_sig | string |  | 是 | [支付签名](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/payment-signature-generation-algorithm/),本次请求的所有非空参数+uri+method+支付密钥，用 HMAC-SHA256 签名 |

## 返回值
Object ，包含以下属性

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 错误码 |
| errmsg | string | 错误信息 |
| bill_no | string | 订单号，有效期是 48 小时 |
| balance | number | 预扣后的余额 |
| used_gen_amt | number | 本次扣的赠送币的金额 |

### errcode 枚举说明

| 值 | 说明 |
| --- | --- |
| 0 | 请求成功 |
| -1 | 系统繁忙，此时请开发者稍候再试 |
| 90009 | mp_sig 签名错误 |
| 90010 | 用户未登录或登录态已过期 |
| 90011 | sig 签名错误 |
| 90012 | 订单已存在 |
| 90013 | 余额不足 |
| 90017 | 没有调用接口的权限，access_token 过期会导致该错误 |
| 90018 | 参数错误，根据 msg 修复后再试 |

## 代码示例

```json
{
  "openid": "fge35vh5h3f2",
  "appid": "tthdch45hd2df",
  "zone_id": "1",
  "mp_sig": "d1f0a41272f9b85618361323e1b19cd8cb0213f2",
  "access_token": "hds2rt6bhgh5wfg5nf4gdh6",
  "ts": 1507530737,
  "pf": "android",
  "amt": 10,
  "bill_no": "1234567890000"
}
```

## Bug & Tip
无
