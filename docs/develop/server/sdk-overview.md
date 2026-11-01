---
title: "小游戏 OpenAPI SDK 总览"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/server/sdk-overview
update_time: 2025-07-31
---

为了帮助开发者更加便捷地使用抖音开放能力，简化在接入抖音开放平台时的操作步骤，开放平台提供了统一的服务端 OpenAPI SDK。开发者可使用OpenAPI SDK，快捷地接入抖音开放平台提供的服务端接口，提升开发效率。需要注意的是SDK中的Token参数需要用户自己注入。当前OpenAPI SDK支持三种编程语言：
- Java
- NodeJS
- Go

下面的示例代码以[《查询券模板》](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/server/merchant-coupon/coupon-meta-mgmt/query-coupon-meta)对应的接口为例
## Java接入
### 包引入
在 pom.xml 文件添加仓库和依赖，最新版本为`1.0.5`，请使用最新版本

```xml
<repository>
  <id>douyin-openapi-repo</id>
  <url>https://artifacts-cn-beijing.volces.com/repository/douyin-openapi/</url>
</repository>
```

```xml
<dependency>
  <groupId>com.douyin.openapi</groupId>
  <artifactId>sdk</artifactId>
  <version>1.0.0</version>
</dependency>
```

### 代码示例

```java

import com.aliyun.tea.TeaException;
import com.douyin.openapi.client.Client;
import com.douyin.openapi.client.models.*;
import com.douyin.openapi.credential.models.Config;

public class Main {
    public static void main(String[] args) {
    
        try {
            Config config = new Config().setClientKey("test_app_id").setClientSecret("test_app_secret");
            Client client = new Client(config);

            CouponQueryCouponMetaRequest sdkRequest = new CouponQueryCouponMetaRequest()
                    .setCouponMetaId("test_id")
                    .setBizType(new Integer(1))
                    .setAccessToken("test_access_token");
            CouponQueryCouponMetaResponse sdkResponse = client.CouponQueryCouponMeta(sdkRequest);
            System.out.println(sdkResponse);
        } catch (TeaException e) {
            System.out.println(e.getMessage());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }
}
```

## Go接入
### 包引入

```go
go get github.com/bytedance/douyin-openapi-sdk-go
```

### 代码示例

```go
import (
    "fmt"
    "testing"

    credential "github.com/bytedance/douyin-openapi-credential-go/client"
    openApiSdkClient "github.com/bytedance/douyin-openapi-sdk-go/client"
)

func TestCouponQueryCouponMeta(t *testing.T) {

    // 初始化SDK client
    opt := new(credential.Config).
       SetClientKey("test_app_id").
       SetClientSecret("test_app_secret")
    sdkClient, err := openApiSdkClient.NewClient(opt)
    if err != nil {
       t.Fatal(fmt.Sprintln("sdk init err:", err))
    }

    // 构建请求参数
    couponMetaId := "7373678331264630820"
    bizType := 1
    sdkRequest := &openApiSdkClient.CouponQueryCouponMetaRequest{
       CouponMetaId: &couponMetaId,
       BizType:      &bizType,
    }
    // token获取与注入
    // credential包提供了默认的token获取方法，但是该实现方式是基于单实例的，如果用户多实例场景使用会出现token互刷的问题。
    // 开发者如果有多实例部署的需求可以自行实现token获取的逻辑
    credentialHandler, err := credential.NewCredential(opt)
    if err != nil {
       t.Fatal(fmt.Sprintln("credential init err:", err))
    }
    token, err := credentialHandler.GetClientToken()
    if err != nil {
       t.Fatal(fmt.Sprintln("token get err:", err))
    }
    sdkRequest.AccessToken = token.AccessToken 

    // sdk调用
    sdkResponse, err := sdkClient.CouponQueryCouponMeta(sdkRequest)
    if err != nil {
       t.Fatal(fmt.Sprintln("sdk call err:", err))
    }

    t.Log(sdkResponse)

}
```

## NodeJS接入
### 包引入
运行以下命令：

```text
npm add @open-dy/open_api_sdk
npm add @open-dy/open_api_credential
```

### 代码示例

```typescript
import Client, { MessageGetUserMessageRequest } from '@open-dy/open_api_sdk';
import CredentialClient from '@open-dy/open_api_credential';
interface ClientTokenResponse {
     data?: {
        access_token?: string,
        description?: string,
        error_code?: number,
        expires_in?: number
    }
}
// 传入 clientKey 和 clientSecret 获取 token
const credentialClient = new CredentialClient({clientKey: 'xxx', clientSecret: 'xxx'});
const { accessToken } = await credentialClient.getClientToken();
 // 传入 clientKey 和 clientSecret 
const client = new Client({ clientKey: 'xxx', clientSecret: 'xxx' });
 // 拼接请求入参
const params = new MessageGetUserMessageRequest({accessToken:accessToken, startTime:xxx, endTime: xxx, type: xxx, username: xxx, pageNum: xxx, pageSize: xxx });
// 调用方法发起请求
const messageRes = await client.messageGetUserMessage(params);
console.log('messageRes', messageRes);
```

## 接口列表
