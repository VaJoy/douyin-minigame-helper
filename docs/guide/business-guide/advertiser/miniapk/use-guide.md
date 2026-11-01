---
title: "小游戏信息流投放金使用指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/advertiser/miniapk/use-guide
update_time: 2026-04-17
---

## 一、流程概览
- **流程简述**：
  - 查看投放金账户余额->完成巨量账户授权 -> 转充投放金 ->查看转充记录
- **注意事项**：
  - 投放金的使用应遵守投放金使用规则，详见《[小游戏投放金合作协议](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/agreement-and-norms/game-ad-agreement)》

## 二、投放金转充流程
### **第一步：查看投放金账户余额**
#### 1.查看投放金账户余额
> 1. 有信息流推广的小游戏才配赠投放金，**无投放行为则无法看到信息流账户模块**。
> 1. 该账户为**游戏维度的账户，每个小游戏独立计算投放金。**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/0d78eb22cc4249d8a510b260d17dea56~tplv-9nona0m7ha-image.image)

#### 2.查看赠送记录
平台每个自然月结算一次投放金，结算后自动发放到投放金账户中。可在【抖音小游戏平台-能力-广告投放-投放金账户-赠送记录】模块查看投放金的结算记录明细。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/ee320bba88854836b0047e40ba0d0c51~tplv-9nona0m7ha-image.image)

### **第二步：巨量账户授权**
投放金可转充至同主体和同集团非同主体的巨量引擎投放账户中使用，主体指小游戏开发者平台认证主体和巨量引擎投放账户主体。授权账户的个数不受限。
#### 1.同主体授权
适用场景：巨量引擎投放账户主体 = 小游戏开发者平台认证主体
1. 在【抖音小游戏平台-能力-广告投放-投放金账户】模块点击账户授权按钮，在弹窗的账户类型选择同主体授权。阅读并勾选《[小游戏投放金合作协议](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/agreement-and-norms/game-ad-agreement)》后点击提交账户授权申请按钮

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/03bc458a384a4bde883c2f183d0d9804~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/8fd12c5287bc43a4aeab6d14e285e496~tplv-9nona0m7ha-image.image)

1. 在巨量引擎投放平台的同主体账户可自动完成授权。授权通过后，若后续在巨量平台新增同主体投放账户，可自动拉取新增的账户，无需再次授权。

注意事项：需要同时**满足以下两个条件**才可完成主体授权
- 巨量引擎的投放账户主体需与小游戏开发者认证主体一致
- 该主体下的巨量引擎投放账户存在历史投放消耗（任意一个账号历史消耗数据＞0）

#### 2.同集团非同主体授权
适用场景：巨量引擎投放账户主体A ≠ 小游戏开发者平台认证主体 B，但在A&B主体在巨量平台属于**关联主体，**认定关系详见https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/advertiser/policy
1. 在【抖音小游戏平台-能力-广告投放-投放金账户】模块点击账户授权按钮，在弹窗的账户类型选择同集团非主体授权。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/03bc458a384a4bde883c2f183d0d9804~tplv-9nona0m7ha-image.image)

1. 在账户ID输入框中，输入需要转充的巨量引擎投放平台账户ID。阅读并勾选《[小游戏投放金合作协议](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/agreement-and-norms/game-ad-agreement)》后点击提交账户授权申请按钮。
注意事项：需要同时**满足以下三个条件**才可发起授权申请
  - 巨量引擎的投放账户主体需与小游戏开发者认证主体属于同集团。说明：关联关系的认定需向巨量引擎平台报备，实际是否认定为关联主体以巨量引擎平台提供的查询结果为准。
  - 巨量引擎的投放账户存在投放消耗（当前申请账号历史消耗数据＞0）
  - 巨量引擎的投放账户属于游戏行业账户

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/f5abc031cce94361b11c0d8537f0ad0e~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/346146bc0586435c918950e5d6956631)

1. 账户确认授权。 在小游戏平台发起授权申请后，在【巨量引擎平台】https://ad.oceanengine.com/pages/login/index.html，查看授权申请并操作确认。授权申请在当日24点前有效，若未及时同意授权则申请失效需要重新发起申请。
- 登录【巨量引擎平台】账户，点击“消息中心”按钮查看站内信。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4c1b323a8140410ca06308c9bab28730)

- 点击站内信查看详情，如确认授权，可在有效期内点击“确认授权”按钮完成授权。
  - 若未及时操作授权，当日24点申请自动失效。需联系小游戏开发者在抖音小游戏平台再次发起授权申请。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/4da95d16cfe649f4896a20cbda8a6979)

1. 授权完成后，在【抖音小游戏平台-能力-广告投放-投放金账户】查看账户列表以及授权状态。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/e113017792ab4936bc2140850714c69d~tplv-9nona0m7ha-image.image)

**授权状态说明：**
- 申请已通过：代表授权流程已完成，可向该账户转充投放金
- 申请中：代表已经发起申请，需要登录巨量平台确认授权后才能转为申请通过状态。详见上述第3步
- 申请已过期：代表授权申请已过期，巨量平台对应账户中未确认授权，当日24点失效。可再次发起申请。

### **第三步：转充投放金**
完成授权后，若投放金账户中有余额，可向授权状态为申请已通过的账户转充投放金。

1. 在【抖音小游戏平台-能力-广告投放-投放金账户】模块点击转充至巨量账户按钮，在弹窗中输入需要转充的金额和账户。转充账户必须为已授权的巨告投放账户，支持搜索账户名称或账户ID。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/9848fe330d96478f88c335cd3492d73c~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/37f4ee567fa04acaacdc4f40d4e4a8ba~tplv-9nona0m7ha-image.image)

1. **确认账户信息和金额无误后**，点击充值按钮完成转充。转充后可在【抖音小游戏平台-能力-广告投放-投放金账户-转充记录】模块查看向巨量账户的转充记录。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/6dd341fcd808422b8400f49db3450734~tplv-9nona0m7ha-image.image)

1. 转充完成后，也可在**【巨量引擎投放平台-财务】**模块的“资金钱包-竞价余额-赠款”查看投放金余额，或在“财务流水”页面查看明细。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/ed5c0abdf0394561be9121b029bdb418~tplv-9nona0m7ha-image.image)