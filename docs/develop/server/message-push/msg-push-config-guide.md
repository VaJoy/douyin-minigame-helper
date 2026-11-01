---
title: "消息推送配置接入指引"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/message-push/msg-push-config-guide
update_time: 2025-05-26
---

### 整体流程

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/082ff71e3c64419c8634f71a7e8cf2f3~tplv-9nona0m7ha-image.image)

### **填写消息推送配置**
进入小游戏详情页，开发-开发设置-消息推送配置

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/911946ed5fcb4f2f8e205677ec0f014c~tplv-9nona0m7ha-image.image)

启用消息推送，并按提示填写相关信息，具体如下：
- URL：开发者用来接收消息的接口 URL。开发者所填写的 URL 默认以 `https://` 开头，端口为 `443`。
- Token：开发者可以任意填写，用作生成签名，长度 3 ～ 32 个字符。
- 选择消息数据格式：JSON 格式（默认）或 XML 格式。

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/e3d182b2a83a454589cd6ed00b294702~tplv-9nona0m7ha-image.image)

开发者提交信息后，**需按如下操作验证消息来自抖音小游戏**，通过后才可成功保存
### **验证消息来自抖音小游戏**
抖音小游戏服务器将发送 HTTP POST 请求到填写的服务器地址 URL 上，**开发者请务必校验数据签名，验证数据来源的合法性，否则存在被伪造数据攻击的危险，需自行担责**
- **请求参数：**

| Method | POST |  |  |
| --- | --- | --- | --- |
| 参数形式 | 参数名 | 类型 | 说明 |
| Header | x-nonce-str | string | 签名用的随机字符串 |
|  | x-timestamp | string | 发送消息的毫秒级时间戳 |
|  | x-signature | string | 请求签名，业务方接收后需要计算和校验签名，防伪造和篡改 |
|  | x-appid | string | appid |
|  | x-msg-type | string | **消息类型** verify_request：验证请求 gift_delivery：游戏站礼包推送  douyin_microgame_im：抖音客服消息推送 注意：务必判断 x-msg-type 做好不同事件的分发，执行不同事件的处理逻辑 eg：if x-msg-type == "xxx" { do } |
| body | ~ | string | **具体消息的 json 序列化字符串** |

- **Header 示例：**
> 注意：实际接收到的 val 是数组类型(只有一个元素)，使用框架方法如 golang 的 Header.Get("x-msg-type")，会默认取第一个值得到 "verify_request"

```json
{
    "x-appid": ["tt12321"],
    "x-msg-type": ["verify_request"],
    "x-nonce-str": ["313932313532383034"],
    "x-timestamp": ["1737635474798"],
    "x-signature": ["AoOtx/dFR5MFrCTqUmtmDg=="]
}
```

- **开发者验证签名流程**：
通过校验 Header 里的 x-signature 来判断请求是否来自于抖音小游戏服务器，x-signature 生成方式为：
1. 将 Header 里的的 x-appid、x-msg-type、x-nonce-str、x-timestamp 四个参数进行字典序排序，并用 & 符号拼接成一个字符串。
1. 再**直接**拼接上 body 和 token（无需任何连接符号）。
1. 把拼接好的字符串进行 md5 计算(16bytes)，并对 md5 计算结果进行 base64 编码，编码结果便是 signature。
1. 将 signature 与 Header 里的 x-signature 对比，如果相同，则可以认为请求来自于抖音小游戏服务器。
- **开发者对请求的响应：响应 HTTP 200 状态码，平台才会认为是成功的 ack，可成功保存配置**
### **代码示例（golang）**

```go
import (
    "context"
    "crypto/md5"
    "encoding/base64"
    "encoding/json"
    "fmt"
    "sort"
    "strings"
)

/**
比如：
   header := map[string]string{
                "x-nonce-str": "313932313532383034",
                "x-timestamp": "1737635474798",
                "x-appid":    "tt12321",
                "x-msg-type":  "verify_request",
        }
   bodyStr := "verify_body"
   token := "verify_token"

拼接好之后的 rawData为：x-appid=tt12321&x-msg-type=verify_request&x-nonce-str=123456&x-timestamp=456789verify_bodyverify_token

生成的 signatureStr 为：AoOtx/dFR5MFrCTqUmtmDg==
*/

// 生成数据签名
func generateSignature(ctx context.Context, headerMap map[string]string, bodyStr string, token string) string {
    // 1、对 headerMap 中的 key 按字典序从小到大排序（注意实际编码时，只对如上指定的 4个 key 进行排序）
    keyList := make([]string, 0, 5)
    for key := range headerMap {
       keyList = append(keyList, key)
    }
    sort.Slice(keyList, func(i, j int) bool {
       return keyList[i] < keyList[j]
    })
    // 2、将 key-value 按顺序拼接成字符串，格式为 key1=value1&key2=value2&...
    kvList := make([]string, 0, 5)
    for _, key := range keyList {
       kvList = append(kvList, key+"="+headerMap[key])
    }
    urlParams := strings.Join(kvList, "&")

    // 3、直接拼接(无需连接符)：urlParams + bodyStr + token
    rawData := urlParams + bodyStr + token
    md5Result := md5.Sum([]byte(rawData))
    signatureStr := base64.StdEncoding.EncodeToString(md5Result[:])

    return signatureStr
}

// 接收消息的函数（平台上设置的 Url）
func HandleMessage(ctx context.Context, c *app.RequestContext) {
    msgType := c.Request.Header.Get("x-msg-type")
    // 0、从请求头读取 Header
    headerMap := map[string]string{
       "x-appid":     c.Request.Header.Get("x-appid"),
       "x-msg-type":  msgType,
       "x-nonce-str": c.Request.Header.Get("x-nonce-str"),
       "x-timestamp": c.Request.Header.Get("x-timestamp"),
    }
    // 读取 body
    bodyStr := c.Request.Body()
    // 平台上设置的 Token
    token := "xxxxxxxx"
    // 1、生成签名
    signature := generateSignature(ctx, headerMap, string(bodyStr), token)

    // 2、验证签名
    logs.CtxInfo(ctx, "generate signature: %v", signature)
    logs.CtxInfo(ctx, "request signature: %v", c.Request.Header.Get("x-signature"))
    if signature != c.Request.Header.Get("x-signature") {
       service.SendLarkMessage(ctx, "验签失败")
       c.JSON(500, utils.H{
          "message": "signature not equal",
       })
       return
    }
    // 3、接收的是验证消息，则直接返回，无需处理后续逻辑
    if msgType == "verify_request" {
       c.JSON(200, utils.H{})
       return
    }
    
    // 接收的是游戏站礼包推送消息，处理请求 .....
    //（务必判断此 msgType 做好事件分离，后续抖音可能还会推送其他 msgType 到同样的服务器地址上）
    if msgType == "gift_delivery" {
      
       xxxxxxx // 具体执行逻辑
      
       c.JSON(200, utils.H{})
       return
    }

    // 接收的是抖音客服推送消息，处理请求 .....
    //（务必判断此 msgType 做好事件分离，后续抖音可能还会推送其他 msgType 到同样的服务器地址上）
    if msgType == "douyin_microgame_im" {
      
       xxxxxxx // 具体执行逻辑
      
       c.JSON(200, utils.H{})
       return
    }
    
    // 其他 msgType，不做处理
```

### 消息推送调试（可选）
> 调试台地址：[URL验证](https://developer.open-douyin.com/docs/openapi-explorer?id=webhook-url)、[消息请求构造](https://developer.open-douyin.com/docs/openapi-explorer?id=webhook-debug)
为了便于开发者调试，我们在不同阶段，分别提供了相关的调试工具供开发者使用，点击推送调试按钮即可进入

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/14eb2b56b2f44cc2a0f9df0671704b64~tplv-9nona0m7ha-image.image)

- [URL验证](https://developer.open-douyin.com/docs/openapi-explorer?id=webhook-url)（填写消息推送配置阶段）：支持开发者自定义填写 URL 和 Token，抖音小游戏会发送一条调试验证事件供开发者调试。
- [消息请求构造](https://developer.open-douyin.com/docs/openapi-explorer?id=webhook-debug)（接收消息事件推送阶段）：支持开发者自定义填写请求体 ，抖音小游戏会拉取你配置的消息推送配置，**实际推送一条真实的事件**供开发者调试。
> 注意：发送请求等同于真实操作，请谨慎操作
### 自查手册
报错：发起验证请求失败，请确保服务器地址的可用性
解决方案：
1. 可使用调试台的 URL 验证功能进行排查，确保验签逻辑正确
1. 检查开发者服务器是否开启了安全组，导致抖音小游戏服务器无法正常访问

import (
"context"
"crypto/md5"
"encoding/base64"
"encoding/json"
"fmt"
"sort"
"strings"
)

/**
比如：
header := map[string]string{
"x-nonce-str": "313932313532383034",
"x-timestamp": "1737635474798",
"x-appid":    "tt12321",
"x-msg-type":  "verify_request",
}
bodyStr := "verify_body"
token := "verify_token"

拼接好之后的 rawData为：x-appid=tt12321&x-msg-type=verify_request&x-nonce-str=123456&x-timestamp=456789verify_bodyverify_token

生成的 signatureStr 为：AoOtx/dFR5MFrCTqUmtmDg==
*/

// 生成数据签名
func generateSignature(ctx context.Context, headerMap map[string]string, bodyStr string, token string) string {
// 1、对 headerMap 中的 key 按字典序从小到大排序（注意实际编码时，只对如上指定的 4个 key 进行排序）
keyList := make([]string, 0, 5)
for key := range headerMap {
keyList = append(keyList, key)
}
sort.Slice(keyList, func(i, j int) bool {
return keyList[i] < keyList[j]
})
// 2、将 key-value 按顺序拼接成字符串，格式为 key1=value1&key2=value2&...
kvList := make([]string, 0, 5)
for _, key := range keyList {
kvList = append(kvList, key+"="+headerMap[key])
}
urlParams := strings.Join(kvList, "&")

// 3、直接拼接(无需连接符)：urlParams + bodyStr + token
rawData := urlParams + bodyStr + token
md5Result := md5.Sum([]byte(rawData))
signatureStr := base64.StdEncoding.EncodeToString(md5Result[:])

return signatureStr
}

// 接收消息的函数（平台上设置的 Url）
func HandleMessage(ctx context.Context, c *app.RequestContext) {
msgType := c.Request.Header.Get("x-msg-type")
// 0、从请求头读取 Header
headerMap := map[string]string{
"x-appid":     c.Request.Header.Get("x-appid"),
"x-msg-type":  msgType,
"x-nonce-str": c.Request.Header.Get("x-nonce-str"),
"x-timestamp": c.Request.Header.Get("x-timestamp"),
}
// 读取 body
bodyStr := c.Request.Body()
// 平台上设置的 Token
token := "xxxxxxxx"
// 1、生成签名
signature := generateSignature(ctx, headerMap, string(bodyStr), token)

// 2、验证签名
logs.CtxInfo(ctx, "generate signature: %v", signature)
logs.CtxInfo(ctx, "request signature: %v", c.Request.Header.Get("x-signature"))
if signature != c.Request.Header.Get("x-signature") {
service.SendLarkMessage(ctx, "验签失败")
c.JSON(500, utils.H{
"message": "signature not equal",
})
return
}
// 3、接收的是验证消息，则直接返回，无需处理后续逻辑
if msgType == "verify_request" {
c.JSON(200, utils.H{})
return
}

// 4、接收的是抖音客服推送消息，处理请求 .....
//（务必判断此 msgType，因为后续抖音可能还会推送其他 msgType 到同样的服务器地址上）
if msgType == "douyin_microgame_im" {

xxxxxxx // 具体执行逻辑

c.JSON(200, utils.H{})
return
}

// 其他 msgType，不做处理
