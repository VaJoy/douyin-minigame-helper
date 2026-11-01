---
title: "抖音客服平台-客服能力消息推送接入指引"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/message-push/douyin-microgame-im-guide
update_time: 2025-06-16
---

## 技术接入流程
### **参考流程图：**

![screenshot](https://p9-douyin-open.byteimg.com/tos-cn-i-9nona0m7ha/14215a1f084e4418b75e51a6aeccff10~tplv-9nona0m7ha-image.image)

### 详细路径：
### 步骤一：消息推送能力接入
参考：[消息推送配置接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/message-push/msg-push-config-guide) 进行接入
### 步骤二：接收消息
在具体的推送请求中，有效的 payload 会放在请求的 body 中，开发者可在验签成功后对 body 进行解析，并执行具体的推送业务逻辑。
#### 请求
编码协议：JSON

| **字段** | **必须** | **说明** |
| --- | --- | --- |
| app_id | 是 | 小游戏ID |
| conversation_id | 是 | 会话ID，当前用户所处的会话 |
| msg_id | 是 | 消息ID（可用作幂等保证） |
| create_time | 是 | 用户消息的创建时间，秒级时间戳 |
| msg_type | 是 | 当前消息的类型：text、image、video、score |
| open_id | 是 | 用户的 open_id |
| content | 否 | 文本消息内容（msg_type = "text" 时返回） |
| pic_url | 否 | 图片 url（msg_type = "image" 时返回） |
| video_url | 否 | 视频 url（msg_type = "video" 时返回） |
| score_content | 否 | 评分消息内容（msg_type = "score" 时返回） |

示例：

```json
// 文本消息
{
*  "app_id": "tt123",
*  "conversation_id": 7494205308479291111,
*  "msg_id": 7494460928000411111,
*  "create_time": 1744940173524,
*  "msg_type": "text",
  "open_id": "_000Iuoq1hxt4Kva16Y6szdms7qujIqiwvOx",
*  "pic_url": null,
*  "content": "{\"text\":\"1\",\"action\":{}}" // 只需要关注 text 字段
*}

// 图片消息
{
*  "app_id": "tt123",
*  "conversation_id": 7494205308479291111,
*  "msg_id": 7494460928000411111,
*  "create_time": 1747386717944,
*  "msg_type": "image",
  "open_id": "_000Iuoq1hxt4Kva16Y6szdms7qujIqiwvOx",
*  "pic_url": "https://lf6-developer-sign.bytemastatic.com/tos-cn-i-noahc9e5u2/96e3e119894443bc8b02828f7c505825?lk3s=86e038d0&x-expires=2062745687&x-signature=H3V6EZy%2FNuwt9uIXx4bqWrtwfRQ%3D",
  "content": null
*}

// 视频消息
{
  "app_id": "tt123",
  "conversation_id": 7494205308479291111,
  "msg_id": 7494460928000411111,
  "create_time": 1747386717944,
  "msg_type": "video",
  "pic_url": null,
  "video_url": "https://v26-default.douyinvod.com/1bd9e41c63ae552385e4cb96e64a7cb9/684f909c/video/tos/cn/tos-cn-v-5f73e7/ocUnGerP1IOaQQB2hAQALC2fQxrwOANwEBfADv/?a=371173&ch=0&cr=0&dr=2&er=0&lr=test&cd=0%7C0%7C0%7C0&br=606&bt=606&ds=3&ft=GwL5G6EEBBkq8ZmossSL-_vjVQWw&mime_type=video_mp4&qs=13&rc=M3c2OnQ5cjRyNDQzNGdnM0BpM3c2OnQ5cjRyNDQzNGdnM0BqM2BwMmRzMjRhLS1kXmFzYSNqM2BwMmRzMjRhLS1kXmFzcw%3D%3D&btag=c0000e00008000&dy_q=1750041225&l=02175004122535300000000000000000000ffff0ad2b6a8ff283e",
  "content": null,
  "score_content": null,
  "open_id": "_000Iuoq1hxt4Kva16Y6szdms7qujIqiwvOx",
}

// 评分消息
{
  "app_id": "tt123",
  "conversation_id": 7494205308479291111,
  "msg_id": 7494460928000411111,
  "create_time": 1747386717944,
  "msg_type": "score",
  "pic_url": null,
  "video_url": null,
  "content": null,
  // score：评分；label：评分标签；coment：评论；state：1-已解决；2-未解决
  "score_content": "{\"payload\":{\"score\":5,\"labels\":[{\"id\":1,\"text\":\"处理流畅及时\"},{\"id\":2,\"text\":\"服务态度良好\"},{\"id\":3,\"text\":\"准确理解问题\"}],\"comment\":\"非常\",\"state\":1}}",
  "open_id": "_000Iuoq1hxt4Kva16Y6szdms7qujIqiwvOx"
}
```

#### 响应
**正常响应**
  HTTP 状态码：200
  HTTP 响应体：JSON

```json
{
    "success": true
}
```

**异常响应**
  HTTP 状态码：200
  HTTP 响应体：JSON

```json
{
    "success": false,
    "err_code": 100002,
    "reason": "失败原因"
}
```

**err_code 错误码枚举**：

| err_code | 说明 |
| --- | --- |
| 100002 | 触发频控，允许稍后重试 |

### 步骤三：回复消息
用户发送信息后，可在48小时内，至多回复5条信息
curl 示例如下：
- 回复文本消息：

```sql
curl --location 'http://minigame.zijieapi.com/mgplatform/api/apps/reply/reply_user_text' \
--header 'Content-Type: application/json' \
--header 'access-token: 0801121847445a664742744e5643524d38462f41314d4c736c513d3d' \
--data '{
    "micro_game_id": "tt411d37a0de37d565",
    "conversation_id": "7483846274349842751",
    "msg_id": "5123031140113221826",
    "create_time": 2872345199,
    "msg_type": "link",
    "content": "测试demo\n<a rel=\"noopener noreferrer\" target=\"_blank\" href=\"https://www.baidu.com/\">https://www.baidu.com/</a>"
}'
```

- 回复图片消息：

```sql
curl --location 'http://minigame.zijieapi.com/mgplatform/api/apps/reply/reply_user_image?micro_game_id=tt411d37a0de37d565&conversation_id=7483846274349842751&msg_id=51230312401132218143&create_time=1744106803&sender_name=userName' \
--header 'Content-Type: multipart/form-data' \
--header 'access-token: 0801121847445a6576303563624e384971796a58636c505a4e413d3d' \
--data-binary '@/Users/bytedance/Pictures/蓝色头像.png'
```

具体细节可参考 [回复文本消息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/douyin-microgame-im/reply-user-text)、[回复图片消息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/douyin-microgame-im/reply-user-image)

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
