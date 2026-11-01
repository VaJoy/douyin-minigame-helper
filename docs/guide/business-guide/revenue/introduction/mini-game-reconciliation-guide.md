---
title: "小游戏对账使用指南"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/revenue/introduction/mini-game-reconciliation-guide
update_time: 2026-08-24
---

## **一、收入结算流程概览**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/54d118759d424e539008ff0d0a6fd2ad~tplv-9nona0m7ha-image.image)

> ①收入结算账单为小游戏现金收益部分，广告金与任务金收益不在收入结算账单中体现；
> ②如遇到账单数据异常、提现失败等问题，请联系平台客服处理。
> ③担保支付渠道的收入余额无需开发者开具发票，等待收入自动进入商户号余额后，点击银行卡提现即可。
## **二、收入结算基本规则拆解**
### 1. 收入来源

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/ffced7115c93478695c09c3ea2a5d741~tplv-9nona0m7ha-image.image)

> 解读：
> - 平台小游戏收入类型分为三类：
>   - 内购收入小游戏，具备内购功能，即开通虚拟支付功能的小游戏，也叫做IAP小游戏；
>   - 广告收入小游戏，仅依靠广告收入变现的小游戏，也叫做IAA小游戏；
>   - 混合收入小游戏，是指同时具备内购收入和广告收入2种收入类型的小游戏，所以叫做IAAP（混合变现）小游戏；
> - 玩家来源视角下，分为投广场景引流来的玩家和非投广场景引流来的玩家
>   - 投广场景是指开发者通过广告投放渠道【微端和直投】引流来的玩家；
>   - 非投广场景是除了投广场景以外的场景，包含发行人计划（含一口价）、自然流量等；
### 2.收入结算规则

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/8c2f11ec37644b628c207fe46ca26efc~tplv-9nona0m7ha-image.image)

> 解读：
> - 收入政策，分为两大类，[广告（IAA）小游戏收益政策](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/revenue/sharingclause/mini-game)和[内购小游戏（IAP\IAPP）收益政策](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/revenue/sharingclause/pay)
>   - 当前不提供广告收入的流水对账功能，广告小游戏以广告结算单数据为准。能力可能迭代，请以实际页面与公告为准。
> 内购小游戏收入结算的收益政策，分为两类：
> - 一般内购收益政策，开发者可获得内购消费总额60%的现金收益。
> - 减免版内购收益政策：当小游戏满足[减免版内购收益政策条件](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/revenue/sharingclause/pay-instructions)时，可享受更高的收益比例；其次，减免版内购小游戏收入需要区分①投广场景和②非投广场景
>   - 投广场景：开发者可获得通过[巨量引擎广告投放](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/advertiser/miniapk/guidelines)所产生的安卓内购消费总额90%的现金收益和ios内购消费总额99%的现金收益。
>   - 非投广场景：开发者可获得用户在安卓与ios双端的内购消费总额80%的现金收益。
>     - 非投广场景包含发行人计划（含一口价）推广产生的内购消费总额流水和自然流量等场景；
## 三、结算单收入对账
### **1.对账流程概览**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/51d4dc3c32d44a0a9bef6bca971a656e~tplv-9nona0m7ha-image.image)

### **2.结算单对账实操**
[对账金额核算工具——抖音小游戏（请下载副本使用）](https://bytedance.larkoffice.com/file/CHKVbSoXHoPhdAxSrHUcS6Vvnhg)
> 大多开发者是以半月或者整月的周期维度去核对账单所获得收入，接下来我们用举例的半月案例去讲解内购减免版小游戏结算单如何对账 （如果以天级单位计算，可自行查询选择周期为某天）

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/4e9b6bde08364e51a931732461b5414a~tplv-9nona0m7ha-image.image)

> 解读：
> **可提现金额：**指当周期内，开发者最终可得到的提现收入金额；
> **开发者收益的总收入**：指当周期内，根据收入收益政策计算得到的理论上不包含各种扣款项的开发者收益的总收入；
> **总扣款金额：**指当周期内，发生的买量扣款、充值退款、特殊调减（金币成本扣除、达人活动成本扣除），或实际发生扣款的其他场景（费用产生场景不清楚的，可咨询平台客服）
- 首先计算**开发者收益的总收入**

1. **安卓设备下充值的总内购金额: **
点击对应小游戏的【商业化-虚拟支付-支付数据】。筛选条件中选择对应周期，按照右图1红框位置，记录【分成前内购收入】2,211,963（包含安卓设备下所有的普通支付、钻石支付、担保支付充值流水）

1. **安卓设备下投广内购金额:**
在【操作系统】选【安卓】的情况下，【归因渠道来源】选择【广告】，按照右图2记录对应的【分成前内购收入】为1,627,766

1. （2,211,963）-投广内购金额（1,627,766）=获得安卓设备下的非投广内购金额（584197）

**注：平台现有PC端（windows），该内购收入按照安卓端内购消费总额规则结算。**
- **PC端（windows）的收入如何计算**
1.PC端（windows）设备下充值的总内购金额:
点击对应小游戏的【商业化-虚拟支付-支付数据】。筛选条件中选择对应周期，按照右图3红框位置，记录【分成前内购收入】（包含windows设备下所有的普通支付、钻石支付、担保支付充值流水）

2.PC端（windows）设备下投广内购金额:
在【操作系统】选【windows】的情况下，【归因渠道来源】选择【广告】，按照右图4记录对应的【分成前内购收入】

3.使用windows设备下充值的总分成前内购收入-投广内购金额=获得windows设备下的非投广内购金额

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/1cd4c289b15d49a4af9832fb057a999a~tplv-9nona0m7ha-image.image)

（图1）

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/ecdaf9663e4741418eb4bac09b8d6255~tplv-9nona0m7ha-image.image)

（图2）

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/344666d0a21a4ab4a19f5772b22f97b6~tplv-9nona0m7ha-image.image)

（图3）

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/8f81d2f6c57d423584dd38713126d83f~tplv-9nona0m7ha-image.image)

（图4）

**注：上图中的分成后内购收入因收到半月减免分成条件和实时分成后退款金额影响仅作参考，具体结算金额需要以结算单上面的金额为准**
- 第二步**查询【IOS】设备上玩家充值内购的总消耗流水**，具体操作如下：

1. **IOS设备下充值的总内购金额**：
筛选条件中选择对应周期，按照右图1红框位置,记录【分成前内购收入】982,964（包含IOS设备下所有的普通支付、钻石支付、担保支付充值流水）
1. **IOS设备下投广内购金额：**
【操作系统】选项选【IOS】情况下，【归因渠道来源】选择【广告】，按照右图2记录对应的【分成前内购收入】消耗流水为453,854
1. 使用IOS设备下充值的分成前内购收入（982,964）-投广内购金额（453,854）=获得IOS设备下的非投广内购金额（529110）

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/139e29206e3a4c9b85e70af46e27859c~tplv-9nona0m7ha-image.image)

（图1）

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/746a09339b134378b6cb82a4cb6fa410~tplv-9nona0m7ha-image.image)

（图2）

- 第三步根据以上获得的流水和对应不同流水的平台收益比例，算出**开发者收益的总收入：**

- 根据右图减免版收益比例政策
- 安卓的投广收益比例为90%，所以使用记录的【安卓投广】（1,627,766）*0.9
- 加上安卓的非投广收益比例为80%，所以使用记录的【安卓非投广】（584197）*0.8
- 再加上IOS投广的收益比例是99%，使用【IOS广告】（453,854）*0.99
- 最后加上IOS非投广收益比例80%，使用【IOS非投广】（529110）*0.8
- 以上相加得到的总金额**2804950.46，这个就是开发者收益的总收入**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/cc7f7667da644f6ab62470be8f70da4d~tplv-9nona0m7ha-image.image)

我们得到了**开发者收益的理论总收入**，还需要计算**总扣款金额**，获取方式如下：
- 第一步查询**当周期退款金额**
1. 点击【商业化-虚拟支付-支付数据】，根据下图1【时间】选择需要核对的时间周期，【APP】、【操作系统】、【归因渠道来源】选择[全部]，向下滑动鼠标，可以查看到下图2【支付明细】点击【导出】
> 如果支付笔数多，导出所需时间会比较长，可以把日期选择得短一些，分开进行导出。
下图3，导出后打开表格，统计**J列**金额，最后汇总该小游戏A的退款流水为350.4元，记录下来。
> **J列 退款金额（元）：**如玩家充值1元后发生退款，按照收益政策，开发者获得了0.9元，完成退款时将扣减开发者0.9元；如开发者获得0.6元，完成退款时就扣除0.6元

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/43803128c566412f9378fae39d7d6171~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/a2a85ae7c7354765b1acf32146d98602~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/b3ee028583234bba8df058141d045131~tplv-9nona0m7ha-image.image)

**（二）一般内购收益政策场景操作步骤**：

> 一般内购开发者收益比例统一为60%，计算操作步骤如下：
> 1. 首先导出**开发者收益的总收入 **操作路径：根据右图1导出对账周期内的内购消耗流水*收益比60%
> 1. 然后在导出**总扣款金额**此查看方式与减免版内购收益政策的查看方式相同。
> 1. 由此可计算出一般内购的可提现金额=**开发者收益的总收入**-**总扣款金额**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/6a20cdc3fe184be7be22190949e0a5e4~tplv-9nona0m7ha-image.image)

以上为示例计算过程，用于说明口径与步骤。实际比例、收益口径与汇总金额以开发者后台页面与结算单披露为准。
## 四、结算常见问题
详情可见：[小游戏结算使用指南-常见问题](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/revenue/introduction/douyin-games-guide#ab8c451f)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/73523da545724544b9fd1625c8f74f05~tplv-9nona0m7ha-image.image)

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/79d33ae7f6ac4248bb08454b0a33cf26~tplv-9nona0m7ha-image.image)

> 右图1为虚拟支付—>支付数据
> 右图2为发行人计划—>任务转化收入
> 两个界面统计口径均不同，请勿直接对比

> 
![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/8c9568c59e5c4daeb43e1976dafd0584~tplv-9nona0m7ha-image.image)

> 
![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/d9f8e5bef20844be92d97c4931e22d29~tplv-9nona0m7ha-image.image)