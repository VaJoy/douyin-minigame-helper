---
title: "敏感数据处理"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/sensitive-data-process
update_time: 2024-07-24
---

## 校验数据合法性
当开发者通过[tt.getUserInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/info/tt-get-user-info)接口请求到敏感数据时，返回的`signature`字段是在小程序服务器端通过如下算法得到：
```text
signature = sha1(`${rawData}${session_key}`)
```
开发者可以在自己的**服务器端**执行同样的算法，来校验数据是否合法。
## 解密敏感数据

1. 对称解密使用的算法为`AES-128-CBC`，数据采用`PKCS#7`填充。
2. 对称解密的目标密文为`encryptedData`。
3. 对称解密秘钥`aeskey = Base64_Decode(session_key)`, `aeskey`长度为 16Byte。
4. 对称解密算法初始向量为`Base64_Decode(iv)`。
