---
title: "钻石小额直付"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/business-guide/virtual-payment/diamond-pay
update_time: 2025-04-02
---

## 一、什么是钻石小额直付？
用户开通钻石小额直付后，当同时满足条件①钻石余额大于待支付订单金额 ②待支付订单金额小于免确认额度 时，可一步完成支付流程，省略二次确认环节，实现快捷支付，并且支持用户随时调整额度和关闭/打开该功能。

| **动态效果** | **分步骤效果** |  |  |
| --- | --- | --- | --- |

## 二、用户的开通和设置流程是怎样的？
### 1.开通流程
当用户通过收银台完成一次小额钻石支付后，将弹出「钻石小额直付」开通页面，若用户点击“确认开通”，则该功能完成开通，在用户下一次发起钻石支付订单时生效，若用户点击“x”，则该次未开通，用户可于游戏内右上角点击「三个点--支付设置」自行开通，也可等待下一次触发开通页面时开通。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/cdfeacf3d00443f89c8ee10ea6a24e13~tplv-9nona0m7ha-image.image)

### 2.调整额度流程
「钻石小额直付」在待支付订单金额小于免确认额度时生效，若用户想要调整免确认额度，可随时于支付设置页面上调或下调额度。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/c3bfd91dd1604701961b393fa2c69c8c~tplv-9nona0m7ha-image.image)

### 3.关闭流程
若用户希望关闭「钻石小额直付」功能，可随时于直付设置页面针对单游戏关闭，或完全关闭该功能。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/d41ed0e2091244f1aaa836bb72df185b~tplv-9nona0m7ha-image.image)

## 三、游戏的接入和关闭流程是怎样的？
**接入**：若游戏已接入「钻石支付」能力，则默认开通「钻石小额直付」功能，无需单独开发；
> 钻石支付接入指引：https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/diamonds
**关闭**：若您诉求关闭该功能，可与您对接的运营或直客销售联系沟通关闭。

## 四、常见问题FAQ
1. **为什么有用户体验不到「钻石小额直付」功能？**
**答：**该功能跟版抖音客户端33.9.0版本，若用户客户端低于该版本则有可能体验不到，可引导用户自行升级抖音版本。
1. **「钻石小额直付」功能适用于现金免密场景吗？**
**答：**不适用。该功能生效场景仅为使用「钻石」用于支付时，若用户选择现金支付，则「钻石小额直付」的设置不生效于该场景。
1. **如果用户使用「钻石小额直付」后想要退款怎么办？**
**答**：可引导用户至「游戏内--右上角三个点--反馈与举报--充值问题」反馈，平台客服将视具体情况判断是否支持退款并跟进退款流程。