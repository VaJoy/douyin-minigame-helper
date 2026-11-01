---
title: "限时付费礼包接入指引"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/gift-bag/game-gift-paid-guide
update_time: 2025-06-09
---

## 礼包下发路径概览

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/814de2b68c9d4e63b1169e1d5f1bb80b~tplv-9nona0m7ha-image.image)

## 礼包配置
> 配置入口：控制台-运营-运营能力-道具&礼包营销-礼包列表-新建礼包-付费礼包
礼包编辑说明：
- **玩法生效期：**玩法上架生效时间，审核通过后，若超过起始生效期，玩法将自动上架；生效时长建议3个月以上；
- **礼包名称：**对用户展示的礼包名称，命名需具备唯一性；
- **原价：**游戏内无折扣最原始的道具价格，可自由定价；
- **现价：**用户实际购买价格，可自由定价，现价必须 ≤ 原价；
- **礼包库存：**用户实际可购买的礼包库存，库存为0平台将不再向用户推荐该付费礼包，单次配置上限50,000。

礼包库存及用户购买限制：
- 基础频控：满足命中逻辑的用户，1天最多接收1个付费礼包推荐；
- 单用户购买限制：单用户可能会被推荐同一礼包。礼包推荐优先级：已购买＜已推荐＜未推荐。

### 版本要求
适配宿主：抖音、抖音极速版**32.4.0及以上版本**，其他宿主开放时间待定。
适配游戏：普通小游戏 & Unity小游戏（暂仅支持竖屏）。

### 购买场景交互

#### iOS 端

| 第一步 | 第二步 | 第三步 (场景1：钻石余额充足） | 第四步 (场景2：钻石余额不足） | 第五步 | 礼包未购买，倒计时已结束 | 礼包库存售完 |
| --- | --- | --- | --- | --- | --- | --- |
| 用户被触发后，悬浮球出场将对用户展示，悬浮球倒计时15分钟后关闭 | 点击礼包入口，拉起礼包详情页 | 礼包详情页点击购买，拉起收银台 | 礼包详情页点击购买，钻石不足提示充值并支付 | 完成购买，游戏内入口消失 厂商需做礼包道具展示承接，如图中的“恭喜获得”展示获得道具 |  |  |

#### Android端

| 第一步 | 第二步 | 第三步 (场景1：钻石余额充足） | 第四步 (场景2：钻石余额不足） | 第五步 | 礼包未购买，倒计时已结束 | 礼包库存售完 |
| --- | --- | --- | --- | --- | --- | --- |

#### 体验录屏

抖音32.7.0之前版本体验

视频链接：[https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/46ddc6abf5324125bb87b19a7c84cd12~tplv-9nona0m7ha-image.image](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/46ddc6abf5324125bb87b19a7c84cd12~tplv-9nona0m7ha-image.image)

抖音32.7.0及以上版本体验

视频链接：[https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/a2d55a595a7344c0b9d3280f7767f6d9~tplv-9nona0m7ha-image.image](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/a2d55a595a7344c0b9d3280f7767f6d9~tplv-9nona0m7ha-image.image)

## 技术接入
普通小游戏和 Unity 小游戏的 API 存在差异，这里分别说明：
### 普通小游戏
#### 流程
1. 调用 tt.onBuyGift 监听付费礼包的「点击购买」事件
1. 在 tt.onBuyGift 的事件回调中调用支付接口 tt.requestGamePayment 和 tt.openAwemeCustomerService 发起支付

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/2f298127807b4c4cab56a70ae82fcde6~tplv-9nona0m7ha-image.image)

#### 注意事项
1. 只有调用了 tt.onBuyGift，才会按平台策略推送付费礼包入口，否则不展示。
1. 发起支付请完整透传 tt.onBuyGift 的参数，以保证支付的价格和用户从礼包详情页看到的一致。
1. 推送付费礼包要求用户已在宿主上登录。
#### tt.onBuyGift(callback)
监听到用户打开推送的付费礼包并点击购买时触发事件回调。
**入参说明**
callback

| **类型** | **默认值** | **必填** | **说明** | **最低支持版本（只填3位版本号）** |
| --- | --- | --- | --- | --- |
| Function | 无 | 是 | 回调函数，用户发生了平台推送的付费礼包的购买行为（点击购买按钮）时触发 | 3.51.0 |

**返回值**
无
**callback 回调参数**
回调返回参数如下：

| **属性名** | **类型** | **说明** | **最低支持版本** |
| --- | --- | --- | --- |
| giftId | string | 礼包 id | 3.51.0 |
| name | string | 礼包名称 | 3.51.0 |
| orderAmount | number | 礼包价格，单位是分 | 3.51.0 |

#### 支付流程的适配
> iOS接口使用：tt.OpenAwemeCustomerService
> 安卓接口使用：tt.requestGamePayment
修改参数如下

| **属性名** | **类型** | **必填** | **差异化说明** | **最低支持版本** |
| --- | --- | --- | --- | --- |
| goodsId | string | 是 | 礼包 id | 3.51.0 |
| goodType | number | 是 | 本参数传3，同时 buyQuantity 字段不传 | 3.47.0 |
| orderAmount | number | 是 | 代表礼包现金价格，单位为【分】，支持回传10、20、30， 如礼包价格为0.1元，则回传10 | 3.47.0 |
| goodName | string | 否 | 礼包名称，长度限制小于等于10个字符，非必填 | 3.47.0 |

#### **代码示例**
使用前先对 tt.onBuyGift 做兼容性判断

```js
if (!tt.canIUse('onBuyGift')) {
   return; // 不支持则不调用 tt.onBuyGift
}
```

##### **iOS**

```js
if (!tt.canIUse('onBuyGift')) {
   return; // 不支持则不调用 tt.onBuyGift
}

tt.login({force: true, success() {
    
    tt.onBuyGift((param) => {
        const {giftId, name, orderAmount} = param;
        tt.openAwemeCustomerService({
          zoneId: "1",
          customId: "QWERTYUIDFxxxxx",  // 开发者自定义唯一订单号。如不填，支付结果回调将不包含此字段，将导致游戏开发者无法发放游戏道具, 基础库版本低于1.55.0没有此字段
          goodsId: giftId,      
          goodType: 3,      
          orderAmount,      
          goodName: name,
          extraInfo: `{
            userId: "12xxx6",   // 用户自定义额外信息,支付结果回调信息包含此字段， 基础库版本低于1.55.0没有此字段
            version: "v0.0.0",
            price: "30",
          }`,  //extraInfo要转成字符串
          success(res) {
            console.log("调用函数成功");
            const { pay_time, gift } = res;
            const {                 
                gift_id, // 礼包类型id                
                gift_code, // 用户在获取到礼包兑换码进入游戏后，发起核销兑换码的动作，开发者需要使用本接口校验礼包兑换码的有效性。校验通过后才可以发放对应礼包                
                status, // init：待使用，finish：已核销，cancel 已取消            
                } = gift;            
            // 开发者做礼包逻辑处理
            
          },
          fail(res) {
            console.log("调用函数失败");
          },
          complete(res) {
            console.log("调用完成");
          },
        });
    });

}});
```

##### **安卓端**

```js
if (!tt.canIUse('onBuyGift')) {
   return; // 不支持则不调用 tt.onBuyGift
}

tt.login({force: true, success() {
    tt.onBuyGift((param) => {
        const {giftId, name, orderAmount} = param;
        // 道具直购
       tt.requestGamePayment({
          goodType: 3,      
          orderAmount，      
          goodsId: giftId,      
          goodName: name,
          currencyType: "CNY",
          zoneId: "1",
          customId: "QWERTYUIDFxxxxx", 
          extraInfo: '123', 
          mode: "game", // 支付类型
          env: 0, // 支付环境
          platform: "android",
          extraInfo: '{
            userId: "12xxx6",   // 用户自定义额外信息,支付结果回调信息包含此字段， 基础库版本低于1.55.0没有此字段
            version: "v0.0.0",
            price: "30",
          }',//extraInfo要转成字符串
          success(res) {
            console.log("调用函数成功");
            const { pay_time, gift } = res;
            const {                 
                gift_id, // 礼包类型id                
                gift_code, // 用户在获取到礼包兑换码进入游戏后，发起核销兑换码的动作，开发者需要使用本接口校验礼包兑换码的有效性。校验通过后才可以发放对应礼包                
                status, // init：待使用，finish：已核销，cancel 已取消            
                } = gift;            
            // 开发者做礼包逻辑处理
            
          },
          fail(res) {
            console.log("调用函数失败");
          },
          complete(res) {
            console.log("调用完成");
          },
        });
    });
}});
```

##### 新增错误码
下单 jsapi **新增以下错误码**：

| 错误码 | 说明 | 解决方案 | 示例 |
| --- | --- | --- | --- |
| 21002 | 小游戏或平台原因无法下单 | 根据错误提示修复 | “礼包库存不足” |

> 如果要精确判断礼包不足场景，可以使用 `if(errMsg.includes("库存不足") && (Number(errCode) === 21002))`
##### 支付回调

```json
// 支付回调 msg 中新增以下信息，含义同上
{
    "appid": "ttbxxxxxxx",
    "cp_orderno": "QWERTYUIDFxxxxx",
    "cp_extra": "自定义字段",
    "amount_cent": 300,
    "amount_coin": 0,
    "order_no_channel": "TP2024xxxxxxxx589143224",
    "currency": "CNY",
    "gift": {        
        "gift_id": "2278243952424",         
        "gift_code": "PG2378349002",         
        "status": "init"    
    }
}
```

### Unity 小游戏
> 注意事项、支付流程同普通小游戏，以下仅注明和小游戏区别部分（代码部分）
#### 流程
1. 调用 TT.OnBuyGift 监听付费礼包的「点击购买」事件
1. 在 TT.OnBuyGift 的事件回调中调用支付接口 TT.RequestGamePayment 或 TT.OpenAwemeCustomerService 发起支付

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/6460a5fb56a6464ca605784973dfc4cb~tplv-9nona0m7ha-image.image)

#### TT.OnBuyGift(BuyGiftCallback callback)
监听到用户打开推送的付费礼包并点击购买时触发事件回调。
**入参说明**
callback

| **类型** | **默认值** | **必填** | **说明** | **TTSDK支持版本** |
| --- | --- | --- | --- | --- |
| delegate | 无 | 是 | 回调函数，用户发生了平台推送的付费礼包的购买行为（点击购买按钮）时触发 | 6.1.1 |

**返回值**
无
**callback 回调参数**
回调返回参数类型为 BuyGiftResult ，包含属性如下：

| **属性名** | **类型** | **说明** | **TTSDK支持版本** |
| --- | --- | --- | --- |
| GiftId | string | 礼包 id | 6.1.1 |
| Name | string | 礼包名称 | 6.1.1 |
| OrderAmount | number | 礼包价格，单位是分 | 6.1.1 |

#### 代码示例
使用前先对 TT.OnBuyGift 做兼容性判断

```js
if (!CanIUse.OnBuyGift) {
   return; // 不支持则不调用 
}
```

##### **iOS**

```csharp
// 本例中省略登录过程
TT.OnBuyGift(result =>
{
    var param = new OpenAwemeCustomerServiceParam
    {
        GoodType = 3,        
        GoodsId = result.GiftId,        
        GoodName = result.Name,
        OrderAmount = result.OrderAmount,
        CustomId = (TimeUtils.GetCurrentTimeMs() / 1000).ToString(),
        ZoneId = "1",
        ExtraInfo = "sc diamond pay test extra",
        Success = successResult =>
        {
            PrintText($"OpenAwemeCustomerService Success , errMsg -->{successResult.ErrMsg}, " +
                      $"GiftId--> {successResult.Gift?.GiftId} ",                       
                      $"GiftCode --> {successResult.Gift?.GiftCode}",                       
                      $"Status --> {successResult.Gift?.Status}" );
        },
        Fail = failResult =>
        {
            PrintText($"OpenAwemeCustomerService Fail , errMsg -->{failResult.ErrMsg}, " +
                      $"errCode--> {failResult.ErrorCode} , errorType --> {failResult.ErrorType}");
        },
        Complete = () =>
        {
            PrintText("OpenAwemeCustomerService Complete");
        }
    };
    TT.OpenAwemeCustomerService(param);
});
```

##### **安卓端**

```csharp
// 本例中省略登录过程
TT.OnBuyGift(result =>
{
    var param = new RequestGamePaymentParam{
        GoodType = 3,        
        GoodsId = result.GiftId,        
        GoodName = result.Name,
        OrderAmount = result.OrderAmount,
        Mode = "game",
        Env = 0,
        CurrencyType = "CNY", // 固定值: CNY。币种    
        Platform = "android",
        CustomId = (TimeUtils.GetCurrentTimeMs() / 1000).ToString(),
        Success = successResult =>
        {
            PrintText($"Pay Success , errMsg -->{successResult.ErrMsg}, " +
                      $"GiftId--> {successResult.Gift?.GiftId} ",                       
                      $"GiftCode --> {successResult.Gift?.GiftCode}",                       
                      $"Status --> {successResult.Gift?.Status}" );
        },
        Fail = failResult =>
        {
            PrintText($"Pay Fail , errMsg -->{failResult.ErrMsg}, " +
                      $"errCode--> {failResult.ErrorCode} , errorType --> {failResult.ErrorType}");
        },
        Complete = () =>
        {
            PrintText("RequestGamePayment Complete");
        }
    };
    TT.RequestGamePayment(param);
});
```

### 礼包核销 OpenAPI
用于小游戏完成道具礼包领取后，开发者核销用户的礼包码，即用户核销券后，将券状态同步到开放平台。
使用[兑奖OpenAPI](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/receive-reward)完成。

### 礼包下发测试
控制台-运营-运营能力-立即创建限时付费礼包-创建成功后-查看礼包详情
【礼包测试】按钮-填写UID-点击确定-冷启动抖音进入小游戏。
配置一次只能生效15分钟。
## 数据披露
前往小游戏开发者后台--运营--运营能力--道具&礼包营销能力，选择数据Tab页下，选择付费礼包tab即可查看付费礼包售卖数据情况。

| 付费礼包-无数据 | 付费礼包-有数据 |
| --- | --- |

【每日数据汇总】展示本日所有礼包汇总数据，做去重处理
礼包点击支付人数：当日在该小游戏内多个付费礼包详情页，点击购买按钮的用户数
礼包成功支付人数：当日在该小游戏内成功购买多个付费礼包的用户数（累计去重）
销售礼包总金额：当日在该小游戏内购买多个付费礼包的付费总金额

【单个礼包ID数据】礼包汇总数据，单日不做去重；可筛选时间段，筛选时间＞1日展示的是多日去重数据。
礼包支付价格：礼包现价，即用户购买价格
礼包点击人数：选择时间范围内，该礼包详情页的点击支付按钮用户数
礼包成功人数：选择时间范围内，成功购买该礼包的用户数
销售礼包总金额：选择时间范围内，该付费礼包的成功售卖总金额

## 设计物料参考
游戏需要根据本游戏整体风格及定位，设计并提供以下图片素材

| **内容** | **设计规范** | **素材图片说明** |
| --- | --- | --- |
| 1. 礼包详情页背景图 | 如图所示，仅需上传素材图片（底层），由平台识别取色配置背景颜色（顶层）  背景图设计要求： 1、图片大小不超5M 2、仅支持长度1:1图片 3、最多可上传1张图 4、支持jpg、jpeg、png格式(建议jpg格式) |  |
| 2.礼包配图 | 1、图片大小不超1M 2、仅支持长度1:1图片 3、最多可上传1张图 4、支持 jpg、jpeg、png 格式(建议jpg格式) |  |
| 3.道具配图 | 1、图片大小不超1M 2、仅支持长度1:1图片 3、最多可上传1张图 4、支持 jpg、jpeg、png 格式(建议png格式) |  |

## Q & A

Q：游戏内基于原有设计，已经存在丰富的付费礼包推荐给用户了，为什么还要接入这个能力？
A：游戏仅拥有解读用户单游戏行为的能力，平台具备解读用户在平台上多场景行为的能力。平台基于对用户多维度的解读，可以有效发掘用户的付费潜力。而针对在游戏内已经高活跃高付费的核心用户，平台不会过多干预骚扰用户的正常游戏进程。

Q：付费礼包是否需要新增礼包？同一价位需要提供多少种礼包？
A：建议新增，新增礼包要求如下：
- 返利比≥ 游戏内同价位礼包；
- 内容需求通用性高，能满足多层次用户需要的，如一级代币、抽奖券、核心养成道具；
- 新增礼包档位支持自由定价，推荐配置档位：30钻、60钻、180钻、400钻、780钻、1280钻、3280钻、6480钻、9980钻、29980钻；
- 如果要用游戏内现有礼包，以下几种情况都可接受：
  - 游戏内限时特惠礼包，可在本能力合作中重复售卖；
  - 游戏前版本礼包（目前版本不再售卖），可在本能力合作中重复售卖；
  - 代币折扣充值礼包
- 研发同一价位需要提供多少种礼包？
  - 同一价位，1≤ 礼包种类 ≤3 为宜；超过3个礼包类型将不利于用户聚焦。

Q：混服玩家投诉“数值公平性”问题怎么办？
A：建议通过礼包名称包装来淡化，强调是“抖音平台官方福利”，而不是“游戏官方福利”，体现平台让利，而非游戏让利。

Q：用户如果停留在服务器登录界面，点击了游戏内礼包入口，是否可完成后续支付？
A：用户将无法正常完成支付，因为用户还未进入服务器，无法获取用户角色ID，支付后进而无法发货。
为防止这类情况，平台判定用户单次游戏体验时长≥3分钟，当日累计游戏时长≥10分钟才会调用起礼包入口。但如用户长久停留在登录界面，发现且点击礼包入口后发起支付，平台将无法识别，需要厂商完成拦截。

Q：用户如果刚好在付费礼包生效期结束前点击入口，发起支付时礼包生效期结束，用户是否还能正常支付？
A：无法正常支付，并且平台将有提示告知。

Q：tt.canIUse('onBuyGift')返回 false怎么解决？
sdk版本需要在3.51.0及以上才支持onBuyGift，查看sdk版本的方法：打印tt.getSystemInfoSync().SDKVersion，即可查看。
