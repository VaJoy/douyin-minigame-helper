---
title: "服务端回调接口"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/payment/payment-server-callback
update_time: 2025-05-27
---

## 介绍
开发者通过 服务端回调接口 可以获得订单交易信息 并 确认订单状态。 对应支付流程中 6. 部分。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1664196090694)

## 完成前置配置
### 回调地址填写
开发者需要在开发者平台的 商业化->虚拟支付->支付设置 中填写 服务器地址 和 服务器回调 Token。字节平台服务端会对开发者填写的服务器地址进行可访问性验证，验证通过后设置才生效。
> 服务器回调 Token 用于 字节平台服务端 和 开发者的服务器 之间身份验证使用，由开发者自定义并保存。如果后续忘记该字段，开发者可以通过开发者平台进行查询。

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1664196090263)

### 接口可访问性验证
对于开发者填写的回调地址，平台会向其发送 **GET 请求 进行验证，请求中包含 echostr 字符串，开发者在校验**该请求是由平台发出后，需**回传**由平台发送的 **echostr** 字符串完成验证。
接口可访问性校验通过之后，游戏侧完成支付时 才会将 支付订单信息 发送到填写的回调地址，此时回调请求是 **POST 类型**的。
#### 具体步骤
开发者需要在服务端侧通过以下逻辑校验请求是否来源于字节平台服务端，并返回 echostr 字段。
1. token 即服务器回调Token，由开发者自己保存，也可以通过开发者平台查询到
1. timestamp、nonce、msg、echostr 是验证请求的 body 里面的参数
1. 开发者将 token，timestamp，nonce，msg 四个参数进行拼接，然后按照字符串自然大小进行排序，使用 SHA1 算法得到 **signature**，
1. 开发者将上一步 **计算得到的 **signature 和 **验证请求的body中的** signature 对比，如果一致，说明请求来自于开发者的服务端。
1. 最后返回 echostr 完成验证。
示例代码如下：
##### golang 示例

```js
// 收到GET请求
sortedString := make([]string, 0, 4)
sortedString = append(sortedString, token)
sortedString = append(sortedString, timestamp)
sortedString = append(sortedString, nonce)
sortedString = append(sortedString, msg)
// 需要对这些参数按字符串自然大小进行排序
sort.Strings(sortedString)
// 使用SHA1算法
h := sha1.New()
h.Write([]byte(strings.Join(sortedString, "")))

bs := h.Sum(nil)
_signature := fmt.Sprintf("%x", bs)

// signature 一致表示请求来源于 字节小程序服务端
if _signature == Signature {
    return echostr
}
return nil
```

##### nodejs 示例（Koa）

```js
// 收到GET请求
function handler(ctx) {
    const { signature, timestamp, msg: '', nonce, echostr } = ctx.query;
    //需要对这些参数按字符串自然大小进行排序
    const strArr = [token, timestamp, nonce, msg].sort();
    const str = strArr.join('');
    //使用SHA1算法生成signature
    const _signature = require('crypto').createHash('sha1').update(str).digest('hex');

    // signature 一致表示请求来源于 字节小程序服务端
    if (_signature === signature) {
        ctx.body = echostr;
        return;
    }

    ctx.body = '';
}
```

##### java 示例

```js
// 收到GET请求
// 创建list
List<String> sortedString = new ArrayList<>();
sortedString.add(token);
sortedString.add(timestamp);
sortedString.add(nonce);
sortedString.add(msg);
//按字符串自然大小排序
Collections.sort(sortedString);
//拼接字符串
String joinStr = String.join("", sortedString);
//用sha1算法进行加密
MessageDigest md = MessageDigest.getInstance("SHA1");;
//获取密文  （完成摘要计算）
byte[] b = md.digest(joinStr.getBytes());
//将密文转换成十六进制字符串（小写）
String s = DatatypeConverter.printHexBinary(b).toLowerCase();
if (s.equals(signature)) {
   //signature 一致表示请求来源于 字节小程序服务端
    return echostr;
}else {
    return null;
}
```

### Tips
- 开发者自定义的订单号和额外参数字段仅在基础库 1.55.0+ 版本支持，低版本的客户端发生支付行为后，服务端回调接口并不会携带对应的 cp_orderno 和 cp_extra，低于 1.55.0+ 的支付行为要保留原先的对账逻辑。
- 开发者填写的回调地址需要支持 GET 和 POST 两种方式，两种逻辑不一致：
  - 1.字节服务端在验证接口可访问性时使用 GET 方法。
  - 2.当有正式支付订单时字节服务端调用 POST 方法传递开发者服务端订单信息。
## 正式订单回调接口示例
当完成接口可访问性验证 并且 订单**成功支付 **之后(支付失败不会收到回调)，服务端会通过 **POST 方式 **回调开发者提供的 HTTP 接口。
**开发者需要校验确认回调请求是否对应自身游戏。**

> **说明**
> 开发者服务端收到回调且处理成功后，请返回 http 状态码200 ，作为成功响应。 若返回 http 状态码非200，平台会认为通知失败进行重试，重试频率为 10s/30s/1m/2m/3m/4m/5m/6m/7m/8m/9m/10m/20m/30m/1h/2h - 总共4小时45m。

回调信息
- 小游戏 appid
- 开发者自定义的订单号
- 开发者传的额外参数
- 官方交易单号 （路径：小游戏后台 - 商业化 - 虚拟支付 - 支付指标明细）
- 订单金额（单位分）
- 订单使用的币种（CNY-人民币/DIAMOND-钻石）
- 订单游戏币数量

![screenshot](https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/img1664196090538)

#### golang 示例

```go
type OrderSuccessPayInfo struct {
    Appid          string    `json:"appid"`            // 小游戏appid
    CpOrderNo      string    `json:"cp_orderno"`       // 开发者自定义订单号
    CpExtra        string    `json:"cp_extra"`         // 开发者传的额外参数
    OrderNoChannel string    `json:"order_no_channel"` // 小游戏后台交易单号
    Amount         int64     `json:"amount_cent"`      // 订单金额，单位人民币分
    BuyQuantity    int64     `json:"amount_coin"`      // 购买游戏币数量
    Currency       string    `json:"currency"`         // 支付币种，CNY 人民币，DIAMOND 钻石
}

type OrderInfo struct {
   Timestamp    string `json:"timestamp"`    // 时间戳
   Nonce        string `json:"nonce"`        // 随机数
   Msg          string `json:"msg"`          // 包体
   Signature    string `json:"signature"`    // 根据token生成的签名
}

func TestPaySuccessCallback(c *gin.Context) {
   logs.CtxInfo(c, "TestPaySuccessCallback: request = [%+v]", c.Request)
   var oi OrderInfo
   err := c.BindJSON(&oi)
   if err != nil {
      logs.CtxError(c, "TestPaySuccessCallback: request = [%+v], err = [%v]", c.Request, err)
      retJSON(c, map[string]string{"status" : "unsuccess"})
      return
   }
   logs.CtxInfo(c, "TestPaySuccessCallback: request = [%+v], oi = [%+v]", c.Request, oi)

   var ospi OrderSuccessPayInfo
   err = json.Unmarshal([]byte(oi.Msg), &ospi)
   if err != nil {
      logs.CtxError(c, "TestPaySuccessCallback: m = [%+v], err = [%v]", oi, err)
      retJSON(c, map[string]string{"status" : "fail"})
   }
   logs.CtxInfo(c, "TestPaySuccessCallback: oi = [%+v], ospi = [%+v]", oi, ospi)
   retJSON(c, map[string]string{"status" : "success"})
}
```

### 校验请求方法
根据 token，timestamp，nonce，msg ，使用 SHA1 算法生成 signature，与平台的服务端返回的 signature 对比。
#### golang 示例

```js
sortedString := make([]string, 4)
sortedString = append(sortedString, token)
sortedString = append(sortedString, timestamp)
sortedString = append(sortedString, nonce)
sortedString = append(sortedString, string(msg))
sort.Strings(sortedString)

h := sha1.New()
h.Write([]byte(strings.Join(sortedString, "")))

_signature := h.Sum(nil)
```

#### nodejs 示例（Koa）

```js
// http handler POST content-type: application/json
function handler(ctx) {
   const { signature, timestamp, msg: '', nonce, echostr } = ctx.request;
   const strArr = [token, timestamp, nonce, msg].sort();
   const str = strArr.join('');
   const _signature = require('crypto').createHash('sha1').update(str).digest('hex');

   // signature 一致表示请求来源于 字节小游戏开发者的服务端
   if (_signature !== signature) {
      ctx.body = '';
      return;
   }

   // ...... 处理量msg业务逻辑

   ctx.body = echostr;
}
```

### Tips
- 如遇扣款成功但却不回调或回调信息不全等问题，请在 tt.requestGamePayment / tt.openAwemeCustomerService 接口确认是否 customId 和 extraInfo 字段是否填写，强烈建议必填这两个字段，请参考[tt.requestGamePayment](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-request-game-payment) / [tt.openAwemeCustomerService](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/payment/tt-open-aweme-service)。
