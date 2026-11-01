---
title: "获取游戏币余额"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/acquire-mini-game-coin-balance
update_time: 2025-06-09
---

> 本接口应在后端服务器调用
获取游戏币余额，开通小游戏支付后，可通过该接口查询用户的游戏币余额。

```text
POST https://developer.toutiao.com/api/apps/game/wallet/get_balance
```

## 参数说明

| 属性 | 类型 | 默认值 | 是否必填 | 说明 |
| --- | --- | --- | --- | --- |
| openid | string |  | 是 | 用户唯一标识 |
| appid | string |  | 是 | 小程序唯一标识 |
| offer_id | string |  | 否 | 扩展字段，目前未使用，可不填 |
| ts | number |  | 是 | UNIX 时间戳，单位秒 |
| zone_id | string |  | 是 | 游戏服务区 id，开发者自定义。游戏不分大区则默认填写"1"。如果应用支持多角色，则角色 ID 接在分区 ID 后，用"_"连接 |
| pf | string |  | 是 | 目前仅支持 "android" 和 "ios" |
| user_ip | string |  | 否 | 用户外网 ip |
| sig | string |  | 否 | 扩展字段，目前未使用，可不填 |
| access_token | string |  | 是 | [身份验证](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/interface-request-credential/get-access-token) |
| mp_sig | string |  | 是 | [支付签名](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/payment-signature-generation-algorithm/) , 本次请求的所有非空参数+uri+method+支付密钥，用 HMAC-SHA256 签名 |

## 返回值
Object ，包含以下属性

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| errcode | number | 错误码 |
| errmsg | string | 错误描述 |
| balance | number | 游戏币余额，含赠送 |
| gen_balance | number | 赠送游戏币的余额 |
| save_amt | number | 历史累计充值游戏币数量 |
| save_sum | number | 历史获得总游戏币数量 |
| cost_sum | number | 历史总消费游戏币数量 |
| present_sum | number | 历史累计收到赠送游戏币数量 |

### errcode 值类型

| 值 | 说明 |
| --- | --- |
| 0 | 请求成功 |
| -1 | 系统繁忙，稍候再试 |
| 90009 | mp_sig 支付签名校验失败 |
| 90017 | access_token 校验失败，没有接口访问权限 |
| 90018 | 参数错误，按返回的 msg 修复后再试 |

## 代码示例

```json
{
  "openid": "fge35vh5h3f2",
  "appid": "tthdch45hd2df",
  "zone_id": "1",
  "mp_sig": "d1f0a41272f9b85618361323e1b19cd8cb0213f2",
  "access_token": "hds2rt6bhgh5wfg5nf4gdh6",
  "ts": 1507530737,
  "pf": "android"
}
```

## Bug & Tip
- Tip: 查询是需要注意，查询参数要和充值时参数保持一致，包括 zone_id， openid。
