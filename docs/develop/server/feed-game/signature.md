---
title: "推荐流直出游戏能力签名计算方式"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/feed-game/signature
update_time: 2025-02-24
---

## 推荐流直出游戏能力OpenAPI签名计算流程
### **计算流程**
**开发者请务必计算数据签名，用于验证数据来源的合法性，否则存在被伪造数据攻击的危险。若无计算签名，相应数据会被抖音平台过滤掉。**
签名计算方式如下：
1. 对url的query参数按key[字典序](https://baike.baidu.com/item/%E5%AD%97%E5%85%B8%E5%BA%8F/7786229?fr=ge_ala)进行排序，排序后，将key-value按顺序连接起来。如：key1=value1&key2=value2。
1. 再直接拼接(无需连接符)上返回体的body字符串和平台分配给开发者的密钥secret（在接入过程中平台侧会生成对应secret）。**注意，字符串需要使用utf-8编码**
1. 把拼接好的字符串进行md5计算(16bytes)，并对md5计算结果进行base64编码，编码结果便是x-signature

### **代码示例**
下述为 go 代码示例：

```go
package sign

import (
    "crypto/md5"
    "encoding/base64"
    "sort"
    "strings"
)

/*
    参数示例，params对应url里的query参数
    params := map[string]string{
        "nonce":     "1234567890",
        "timestamp": "1717038098",
        "openid":    "ab-cdefghijk",
        "appid":     "tt123456789",
    }
    secret := "secret"
*/
// 请求头签名计算时bodyStr为空字符串， 响应头签名计算时bodyStr为对应响应体字符串
func getSignature(params map[string]string, bodyStr, secret string) string {
   keyList := make([]string, 0, len(params))
   for key, _ := range params {
      keyList = append(keyList, key)
   }
   sort.Slice(keyList, func(i, j int) bool {
      return keyList[i] < keyList[j]
   })
   
   kvList := make([]string, 0, 4)
   for _, key := range keyList {
      kvList = append(kvList, key+"="+params[key])
   }
   
   urlParams := strings.Join(kvList, "&")
   rawData := urlParams + bodyStr + secret 
   md5Result := md5.Sum([]byte(rawData)) 
   return base64.StdEncoding.EncodeToString(md5Result[:])
}
```

下述为 java 示例：

```java
import java.security.NoSuchAlgorithmException;
import java.nio.charset.StandardCharsets;

/*
    参数示例，params对应url里的query参数
    HashMap<String, String> params = new HashMap<>();
    params.put("nonce","1234567890");
    params.put("timestamp","1717038098");
    params.put("openid","ab-cdefghijk");
    params.put("appid","tt123456789");
    secret： "secret"
*/

public class Signature {
    public static String getSignature(Map<String, String> params, String bodyStr, String secret) {
        List<String> keyList = new ArrayList<>(params.keySet());
        Collections.sort(keyList);

        List<String> kvList = new ArrayList<>();
        for (String key : keyList) {
            kvList.add(key + "=" + params.get(key));
        }

        String urlParams = String.join("&", kvList);
        String rawData = urlParams + bodyStr + secret;

        byte[] md5Result = getMD5(rawData);
        return Base64.getEncoder().encodeToString(md5Result);
    }

    private static byte[] getMD5(String data) {
        try {
            MessageDigest md5 = MessageDigest.getInstance("MD5");
            return md5.digest(data.getBytes(StandardCharsets.UTF_8));
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Failed to get MD5 instance", e);
        }
    }
 }
```

下述为 python3 示例：

```python
import hashlib
import base64

"""
    参数示例，params对应url里的query参数
    params = {
        "nonce":     "1234567890",
        "timestamp": "1717038098",
        "openid":    "ab-cdefghijk",
        "appid":     "tt123456789",
    }
    secret = "secret"
"""

def get_signature(params, body_str, screct):
    keys = sorted(params.keys())
    kv_list = [f"{key}={params[key]}" for key in keys]
    url_params = "&".join(kv_list)
    raw_data = url_params + body_str + screct
    md5_result = hashlib.md5(raw_data.encode()).digest()
    return base64.b64encode(md5_result).decode()
```

下述为 js 代码示例：

```js
const crypto = require('crypto');

/*
    参数示例，params对应url里的query参数
    const params = {
        "nonce":     "1234567890",
        "timestamp": "1717038098",
        "openid":    "ab-cdefghijk",
        "appid":     "tt123456789",
    }
    const secret = "secret"
*/

// 请求头签名计算时bodyStr为空字符串， 响应头签名计算时bodyStr为对应响应体字符串
const getSignature = (params, bodyStr, secret) => {
    const keys = Object.keys(params).sort();
    const kvList = keys.map(key => `${key}=${params[key]}`);
    const urlParams = kvList.join('&');
    const rawData = urlParams + bodyStr + secret;
    const md5sum = crypto.createHash('md5');
    md5sum.update(rawData);
    const md5Result = md5sum.digest();
    return Buffer.from(md5Result).toString('base64');
}
```

下述为 php 代码示例：

```php
<?php
function get_signature($params, $body_str, $secret) {
    ksort($params);
    $kv_list = [];
    foreach ($params as $key => $value) {
        $kv_list[] = "$key=$value";
    }
    $url_params = implode("&", $kv_list);
    $raw_data = $url_params . $body_str . $secret;
    $md5_result = md5($raw_data, true);
    return base64_encode($md5_result);
}

// 参数示例，params对应url里的query参数
$params = [
    "nonce"     => "1234567890",
    "timestamp" => "1717038098",
    "openid"    => "ab-cdefghijk",
    "appid"     => "tt123456789",
];
$body_str = "";  // 根据实际情况设置
$secret = "secret";

// 获取签名
$signature = get_signature($params, $body_str, $secret);
echo $signature;
?>
```

### 
### **计算过程示例**
#### **请求头签名计算示例**
- 秘钥：

```bash
secret: secret
```

- 请求参数:

```bash
nonce: 1234567890
timestamp: 1717038098
openid: ab-cdefghijk
appid: tt123456789
```

- 请求头签名计算过程

```json
// 以go语言作为示例，请求头签名计算过程如下：
params := map[string]string{
    "nonce":     "1234567890",
    "timestamp": "1717038098",
    "openid":    "ab-cdefghijk",
    "appid":     "tt123456789",
}
secret := "secret"
signature := getSignature(params, "", secret)
```

- 请求头签名计算结果

```text
signature: HPJf+MAaRDcmBWLxHD3FPg==
```

#### **响应头签名计算示例**
- 响应体

```bash
{
        "err_no": 0,
        "err_msg": "",
        "data": {
                "scenes": [{
                        "scene": 1,
                        "content_ids": ["CONTENT27648287"],
                        "extra": ""
                }]
        }
}
```

- 响应头签名计算过程

```json
// 以go语言作为示例，请求头签名计算过程如下：
// 响应头签名计算中的query参数使用请求头中的参数
type Body struct {
    ErrNo  int32       `json:"err_no"`
    ErrMsg string      `json:"err_msg"`
    Data   *DataStruct `json:"data"`
}

type DataStruct struct {
    Scenes []*Scene `json:"scenes"`
}

type Scene struct {
    ContentIDs []string `json:"content_ids"`
    Extra      string   `json:"extra"`
    Scene      int64    `json:"scene"`
}

params := map[string]string{
    "nonce":     "1234567890",
    "timestamp": "1717038098",
    "openid":    "ab-cdefghijk",
    "appid":     "tt123456789",
}
secret := "secret"
body := &Body{
    ErrNo:  0,
    ErrMsg: "",
    Data: &DataStruct{
       Scenes: []*Scene{
          {
             Scene:      1,
             ContentIDs: []string{"CONTENT27648287"},
             Extra:      "",
          },
       },
    },
}
bodyStr, err := json.Marshal(body)
// bodyStr = "{\"err_no\":0,\"err_msg\":\"\",\"data\":{\"scenes\":[{\"content_ids\":[\"CONTENT27648287\"],\"extra\":\"\",\"scene\":1}]}}"
if err != nil {
    // 处理错误
    panic(err)
}
signature := getSignature(params, bodyStr, secret)
```

- 响应头签名计算结果

```bash
signature: TloY4E3Dt9+QhS6ApoLAYQ==
```
