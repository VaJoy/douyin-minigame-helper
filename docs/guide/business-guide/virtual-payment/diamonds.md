---
title: "钻石兑换功能"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/virtual-payment/diamonds
update_time: 2025-11-11
---

## 一、钻石兑换介绍
“钻石”是抖音平台向用户提供的，用于在抖音平台上进行相关消费的虚拟道具。小游戏接入钻石兑换后，用户可以使用“钻石”兑换游戏中的服务及道具。
- 当前iOS和安卓均已支持接入钻石兑换能力。
- 自2024年8月1日起，钻石能力签约状态，将作为安卓端内购收益政策减免条件之一，详情可查看：（[小游戏内购收入结算规则](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/revenue/sharingclause/pay)）（[小游戏减免版内购收益政策说明](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/revenue/sharingclause/pay-instructions)）

## 二、用户兑换体验
### 2.1 兑换场景交互
#### iOS端：

| **场景1：若用户钻石余额充足，可直接全额兑换** | **场景2：若用户钻石余额不足，钻石充值和兑换一步完成** |  |
| --- | --- | --- |

#### 安卓端：

| **场景1：若用户钻石余额充足，可直接全额兑换** | **场景2：若用户钻石余额不足，钻石充值和兑换一步完成** |
| --- | --- |

### 2.2 订单查询界面

| **钻石充值查询** 查询路径：我->我的钱包->账单 | **钻石兑换查询** 查询路径：我->我的钱包->点击钻石->右上角钻石明细 |
| --- | --- |

## 三、钻石兑换开通流程
### 3.1 整体流程

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/1fa9e655d5674e7a838015aff0140721)

### 3.2 【钻石兑换合作】协议签署流程
> 开发者需使用超级管理员账号，在【小游戏控制台**->**商业化**->**虚拟支付】页面，进行协议签署，同一主体只需签署一次协议。

| **签约入口** | **协议展示** |
| --- | --- |

### 3.3 钻石兑换能力接入
**第一步： IM客服能力接入**
1. 接入虚拟支付相关能力前，需先完成[IM客服能力](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/user-service/douyinIM/)接入，确保及时处理用户反馈，保证用户体验
1. 在抖音开放平台为小游戏绑定抖音IM客服（运营-功能-客服管理-抖音IM客服）

**第二步：钻石兑换功能技术接入**
整体技术调用流程参考下图，请注意：**用户的钻石用于购买游戏币，开发者扣除游戏币后发货**。

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/ca8994c6fb294f31a895595952ba134a)

当游戏内设计的游戏币名称也是钻石时（后续称：游戏钻石），请重点区分游戏钻石和抖音钻石的概念：用户消耗抖音钻石，获得了游戏钻石（游戏币）， 开发者扣除游戏钻石（游戏币）后发货。

| **游戏钻石（游戏币）** | **游戏内道具标价单位** | **抖音钻石** |
| --- | --- | --- |
| 游戏内的一级货币，可能为钻石，也可能为其它（如点券、仙玉等）。 | 游戏内设计了游戏钻石（游戏币）与人民币之间的汇率。 一般会用人民币向玩家展示该项游戏道具价值。在接入钻石兑换能力时，需按下文第三步调整游戏内道具标价单位为抖音钻石**。** | 抖音平台向用户提供的，用于在抖音平台上进行相关消费的虚拟道具，也是本文介绍的玩家使用钻石兑换能力对应的钻石概念。 |

**相关接口：**
1. iOS使用[tt.openAwemeCustomerService](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-open-aweme-service)方法创建钻石兑换订单，安卓使用[tt.requestGamePayment](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-request-game-payment)方法创建钻石兑换订单
1. 使用[服务端回调接口](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/payment-server-callback)方法查询订单状态回调

**第三步：调整游戏内道具标价单位**
由于iOS渠道相关服务商自身运营策略，在用户付费时将收取渠道服务费，可能导致用户充值钻石购买游戏道具时价格与游戏页面价格有所差异。** 请确保游戏内虚拟道具标价，调整为“抖音钻石”标价，避免用户产生误解**。
> 现金：抖音钻石转换汇率= 1: 10，例如道具定价为6元，调整后为60抖音钻石
> 注：为确保游戏顺利接入钻石兑换功能并上线，请务必在上线前调整道具标价单位为“抖音钻石”，否则可能会面临版本审核被驳回的风险。

| **原界面** | **调整后的界面** |
| --- | --- |

**抖音钻石素材及使用规范**
[抖音钻石素材（点击进入文档下载）](https://bytedance.larkoffice.com/file/ZPyibY7KYozfE1xOVNJcuf8pnjg)

![screenshot](https://p9-arcosite.byteimg.com/obj/tos-cn-i-goo7wpa0wc/3da738bfd5c741fda71078ee99eee3a6)

## 四、未成年人退款规则
> 钻石兑换支持未成年人退款，退款路径主要有两种形式
**1：用户通过抖音钱包对原始充值订单发起退款**
- 该退款流程无需开发者审批，由平台相关团队核实信息无误，确认为未成年人充值后，原路退回100%充值金额。

| **原始充值订单退款路径** |  |  |
| --- | --- | --- |

**2：用户通过客服或是在游戏内发起退款申请**
- 用户可选择对钻石充值订单或支付订单发起退款申请，其中钻石充值订单，原路退回原充值账户，钻石支付订单会退款到用户指定账户。
- 与当前平台未成年退款流程一致，需要开发者审批。相关流程：[未成年人退款功能使用指南_小游戏_抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/pay/refund)

| **客服或是游戏内退款路径** |  |  |  |
| --- | --- | --- | --- |

## 五、数据查看

| **入口：小游戏控制台->商业化->虚拟支付** |  |
| --- | --- |
|  | **支付数据** 通过【支付指标明细】->【支付渠道】选择“抖音钻石兑换”，即可查看钻石订单 |
|  | **退款数据** 通过【支付指标明细】->【支付渠道】可查看退款详细 |

## 六、结算申请
钻石结算与常规内购结算流程一致，均需要开发者及时确认结算单、开具发票、邮寄或上传结算材料、等待平台打款。
*但钻石结算单开票信息与虚拟支付结算单开票信息不一致，请开发者注意区分开票。
**详情结算操作可参考：**[小游戏结算使用指南](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/revenue/introduction/douyin-games-guide)

## 七、平台打款
结算周期受第三方服务效率、系统对账及结算周期、银行转账时长、网络环境、系统环境等因素影响，如开发者不提供发票、提供不合格发票或不及时提供发票，平台有权不支付或相应延迟支付。
“支付中”状态的款项当周都会完成处理，具体到账时间取决于银行系统交换时间。
## 八、Q&A
1. **所有小游戏都需要接入钻石兑换能力吗？**
答：申请开通钻石能力并签署相应接入协议为小游戏享受减免版内购收益政策的条件之一，为避免影响游戏享用减免版内购收益政策，建议及时开通并签署协议。
注意：已接入[tt.openAwemeCustomerService](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-open-aweme-service)接口的小游戏直接签署钻石能力协议即可，无需单独接入钻石能力，历史未接入[tt.openAwemeCustomerService](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-open-aweme-service)接口的小游戏需按照上述流程及时接入钻石兑换能力。
1. **30%的渠道服务费怎么算？**
答：当用户通过iOS渠道充值钻石时，会基于服务商的运营策略收取相应的渠道服务费。
1. **钻石兑换功能，服务端如何通过支付回调区分是现金支付还是钻石支付？**
答：
tt.openAwemeCustomerService  普通小游戏支付发起接口
TT.OpenAwemeCustomerService  unity小游戏支付发起接口
通过以上接口发起支付请求， 服务端通过支付回调里的 currency字段 区分是现金支付还是钻石支付
人民币 currency == CNY，钻石 currency == DIAMOND