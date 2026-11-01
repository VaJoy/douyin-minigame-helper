---
title: "游戏分享能力"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/game-share/share-module
update_time: 2026-05-11
---

开发者可以在小游戏中分享内容到抖音等平台。

> 注意：
> 该模块对应 [分享](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#7631fac2)

## TT.ShareAppMessage
> 6.0.0 开始支持本方法
通用分享能力。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 参数 shareJson 是一个 json 对象 生成的分享链接有效期为 45 天，过期后链接失效 报错返回 "get shareInfo return null" 时为获取分享信息失败，可能为获取分享信息时网络请求超时，或者是当前 appID 的分享状态异常，比如被封禁导致，可以检查站内信或通过运营群进行反馈（接入指南 -[联系我们](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/guide/contactus/feedbacks)） 6.6.2+ 成功回调数据格式变更 |
| 相关教程 | 无 |

### **语法 **

```text
public static void ShareAppMessage(JsonData shareJson,
    TTShare.OnShareSuccessCallback successCallback = null,
    TTShare.OnShareFailedCallback failedCallback = null,
    TTShare.OnShareCancelledCallback cancelledCallback = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 支持版本 |
| --- | --- | --- | --- | --- | --- |
| shareJson | JsonData | -- | 是 | 内容填充参考 [ShareParam](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/retweet/share-param) | 6.0.0+ |
| successCallback | OnShareSuccessCallback | null | 否 | 分享成功回调 | 6.0.0+ |
| failedCallback | OnShareFailedCallback | null | 否 | 分享失败回调 | 6.0.0+ |
| cancelledCallback | OnShareCancelledCallback | null | 否 | 取消分享回调 | 6.0.0+ |

### 回调成功
`OnShareSuccessCallback` 回调对象为 `Dictionary<String, Object>` 类型，数据结构说明如下

| 属性名 | 类型 | 说明 | 支持版本 |
| --- | --- | --- | --- |
| state | string | 分享状态，"success" | 6.0.0~6.6.1 |
| share_type | string | 标识分享场景，目前为空值 | 6.0.0~6.6.1 |
| data | Array | 仅当入参 shareJson["channel"] = "invite"时返回，包含邀请对象的用户名和用户头像。详情可以查看 [tt.shareAppMessage_小游戏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/retweet/tt-share-app-message) | 6.0.0~6.6.1 |
| result | JsonData | 分享成功后的核心数据。其内部结构见下表。 | 6.6.2+ |

`result` 的数据结构说明如下

| 属性名 | 类型 | 说明 | 支持版本 |
| --- | --- | --- | --- |
| errMsg | string | 分享结果信息 | 6.6.2+ |
| state | string | 分享状态，"success" | 6.6.2+ |
| share_type | string | 标识分享场景，目前为空值 | 6.6.2+ |
| data | Array | 仅当入参 shareJson["channel"] = "invite"时返回，包含邀请对象的用户名和用户头像。详情可以查看 [tt.shareAppMessage_小游戏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/open-capacity/retweet/tt-share-app-message) | 6.6.2+ |
| info | ShareMessageResult | 自定义分享内容的审核结果，数据结构说明见下文 TT.OnShareMessageResult | 6.6.3+ |
| encryptedData | string | 分享到抖音私信或者群聊的加密信息，解密方法参考 [解密敏感数据](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/sensitive-data-process#%E8%A7%A3%E5%AF%86%E6%95%8F%E6%84%9F%E6%95%B0%E6%8D%AE) | 6.6.5+ |
| iv | string | 加密算法参数 | 6.6.5+ |

`ShareMessageResult` 的数据结构说明如下

| 属性名 | 类型 | 说明 | 支持版本 |
| --- | --- | --- | --- |
| position | string | 分享点位 top「更多面板-分享按钮」 quick_share「更多面板-好友头像」 quick_share_more「更多面板-好友头像最右处的更多按钮」 rank「排行榜」 | 6.6.2+ |
| info | Dictionary<string, ShareRecord> | 分享审核结果 key='image' \| 'title' value=ShareRecord | 6.6.2+ |

`ShareRecord` 的数据结构说明

| 属性名 | 类型 | 说明 | 支持版本 |
| --- | --- | --- | --- |
| expect | string | 预期来源，'official'表示平台素材，'custom'表示自定义素材, 'default'表示兜底素材 | 6.6.2+ |
| actual | string | 实际来源，'official'表示平台素材，'custom'表示自定义素材, 'default'表示兜底素材 | 6.6.2+ |
| code | int | 错误码 | 6.6.2+ |

### 回调失败

| 属性名 | 类型 | 说明 | 支持版本 |
| --- | --- | --- | --- |
| errMsg | string | "shareAppMessage:fail" + 错误信息 | 1.0.0+ |

### 代码示例
【示例一】视频分享

```text
public void TestVideoShare()
{
    // 通用分享
    JsonData shareJson = new JsonData();
    shareJson["channel"] = "video";
    shareJson["title"] = "Some Title";
    shareJson["extra"] = new JsonData();
    shareJson["extra"]["videoPath"] = "/xxx/xxx.mp4";//录屏分享的话，路径是 OnRecordComplete 拿到的路径
    JsonData videoTopics = new JsonData();
    videoTopics.SetJsonType(JsonType.Array);
    videoTopics.Add("Some Topic1");
    videoTopics.Add("Some Topic2");
    shareJson["extra"]["videoTopics"] = videoTopics;
    shareJson["extra"]["hashtag_list"] = videoTopics;
    
    Debug.Log($"ShareAppMessageBtnClicked jsonData: {shareJson.ToJson()}");
    TT.ShareAppMessage(shareJson, (data) =>
        {
            Debug.Log($"ShareAppMessage success: {data["result"].ToJson()}");
        },
        (errMsg) =>
        {
            Debug.Log($"ShareAppMessage failed: {errMsg}");
        },
        () =>
        {
            Debug.Log($"ShareAppMessage cancel");
        });
}
// 成功 data 数据格式示例
data = {
    "result": {
        "data": {}, // 内容填充参考 tt.shareAppMessage_小游戏
    }
}
```

【示例二】使用审核通过的分享素材

```text
public void TestShare()
{
    JsonData shareJson = new JsonData();
    shareJson["title"] = "Some Title";
    shareJson["templateId"] = "YOUR_APPROVED_TEMPLATE_ID";    // 替换成通过审核的分享ID
    
    TT.ShareAppMessage(shareJson, (data) =>
        {
            Debug.Log($"ShareAppMessage success: {data["result"].ToJson()}");
        },
        (errMsg) =>
        {
            Debug.Log($"ShareAppMessage failed: {errMsg}");
        },
        () =>
        {
            Debug.Log($"ShareAppMessage cancel");
        });
}
// 成功 data 数据格式示例
data = {
    "result": {
        "data": {}, // 内容填充参考 tt.shareAppMessage_小游戏
    }
}
```

【示例三】分享自定义图片

```text
public void TestImageShare()
{
    // 6.6.2+ 支持自定义图片分享
    JsonData shareJson = new JsonData();
    shareJson["title"] = "Some Title";
    shareJson["cardImageUrl"] = "https://example.com/test.png";
    shareJson["extra"] = new JsonData();
    JsonData topics = new JsonData();
    topics.SetJsonType(JsonType.Array);
    topics.Add("Some Topic1");
    topics.Add("Some Topic2");
    shareJson["extra"]["hashtag_list"] = topics;
    
    TT.ShareAppMessage(shareJson, (data) =>
        {
            Debug.Log($"ShareAppMessage success: {data["result"].ToJson()}");
        },
        (errMsg) =>
        {
            Debug.Log($"ShareAppMessage failed: {errMsg}");
        },
        () =>
        {
            Debug.Log($"ShareAppMessage cancel");
        });
}
// 成功 data 数据格式示例
data = {
    "result": {
        "data": {}, // 内容填充参考 tt.shareAppMessage_小游戏
        "info": ShareMessageResult // ShareMessageResult 见 TT.OnShareMessageResult 参数说明
    }
}
```

## TT.OnShareAppMessage
> 6.0.0 开始支持本方法
监听用户点击右上角菜单中“转发”、“拍抖音”按钮时触发事件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 该方法可以监听用户通过右上角菜单中触发的分享操作，在不同宿主端具体的操作会有所差别，在抖音中包括分享和拍抖音，在头条包括分享和发头条，以此类推。 该方法的实际调用链路为： 开发者注册此事件 用户点击小游戏菜单中的分享或者拍抖音等按钮 自动调用开发者通过** TT.OnShareAppMessage** 定义的函数，并传入带有 channel 参数的对象，执行得到该函数的返回对象 接着调用** TT.ShareAppMessage** ，将上一步返回的对象传入其中，拉起分享 当开发者发现虽然已成功配置分享内容，但是调试时内容无法生效时，有可能是分享内容触发了内容安全检测失败，导致分享失败。发生这种情况时，开发者可以尝试对分享内容进行内容安全检测，具体操作手段见[内容安全检测](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/server/content-security/content-security-detect/) |
| 相关教程 | 无 |

### **语法 **

```text
public static void OnShareAppMessage(TTShare.OnshareAppMessageCallback callback = null)
```

### **参数说明 **
`OnshareAppMessageCallback` 回调对象的类型为 `ShareOption`，`ShareOption`的数据结构说明如下

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 支持版本 |
| --- | --- | --- | --- | --- | --- |
| webViewUrl | string | -- | 是 | 分享内容 url | 6.0.0+ |
| channel | string | -- | 是 | 分享渠道 | 6.0.0+ |

### 返回说明
`OnshareAppMessageCallback` 需要开发者组装`ShareParam`对象并返回，`ShareParam`的数据结构说明如下

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 支持版本 |
| --- | --- | --- | --- | --- | --- |
| shareJson | JsonData | -- | 是 | 分享内容 | 6.0.0+ |
| successCallback | OnShareSuccessCallback | -- | 是 | 分享成功返回，返回结构和 `TT.ShareAppMessage`保持一致 | 6.0.0+ |
| failedCallback | OnShareFailedCallback | -- | 是 | 分享失败返回 | 6.0.0+ |
| cancelledCallback | OnShareCancelledCallback | -- | 是 | 分享取消返回 | 6.0.0+ |

### 代码示例

```text
public void TestShare()
{
    // 通用分享
    TT.OnShareAppMessage((res) =>
    {
        var channel = res.channel;
        JsonData json = new JsonData();
        if (channel == "video")
        {
            json["title"] = "分享标题";
            json["channel"] = "video";
            JsonData topic = new JsonData();
            topic.Add("test1 videoTopics");
            topic.Add("test2 videoTopics");
            JsonData extra = new JsonData();
            extra["videoTopics"] = topic;
            json["extra"] = extra;
        } 
        else
        {
            // 6.6.2+ 支持传入自定义图片
            json["title"] = "Some Title";
            json["cardImageUrl"] = "https://example.com/test.png";
            // ≤ 6.6.2 传入通过审核的分享ID
            json["templateId"] = "YOUR_APPROVED_TEMPLATE_ID";
        }
        
        return new TTShare.ShareParam(
                json,
                (data) => { Debug.Log("分享成功"); },
                (msg) => { Debug.Log("分享失败" + msg); },
                () => { Debug.Log("取消分享"); }
            );
    });
}
```

## TT.OffShareAppMessage
> 6.0.0 开始支持本方法
取消监听用户点击右上角菜单中“转发”、“拍抖音”按钮时触发事件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```text
public static void OffShareAppMessage(TTShare.OnshareAppMessageCallback callback = null)
```

### 代码示例

```text
public void TestShare()
{
    // 注销 OnShareAppMessage 回调
    TT.OffShareAppMessage((res) => null);
}
```

## TT.ShareMessageToFriend
> 6.0.0 开始支持本方法
给指定好友分享游戏信息。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 目前仅支持 抖音、抖音极速版 App |
| 注意事项 | **注意游戏场景，不要过度频繁引导分享：**定向分享需要与游戏场景强相关，建议结合游戏内的好友系统、互动系统，会起到事半功倍的效果 配合“邀请有奖”或“礼物赠送”等功能模式，可以更大程度激发用户的分享意愿（具体实现：通过定向分享能力，入参中传入分享者的 openid（query 字段），并结合 TT.GetLaunchOptionsSync 或 TT.OnShow 获取启动参数中的 query 来判断是否通过分享链接启动的，并给分享人发放对应的奖励） |
| 相关教程 | 无 |

### **语法 **

```text
public static void ShareMessageToFriend(JsonData options,
    TTShare.OnShareSuccessCallback successCallback = null,
    TTShare.OnShareFailedCallback failedCallback = null,
    TTShare.OnShareCancelledCallback cancelledCallback = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 支持版本 |
| --- | --- | --- | --- | --- | --- |
| options | JsonData | -- | 是 | 内容填充参考 [tt.shareMessageToFriend__抖音开放平台](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-share-message-to-friend/#%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E) | 6.0.0+ |
| successCallback | OnShareSuccessCallback | null | 否 | 分享成功回调 | 6.0.0+ |
| failedCallback | OnShareFailedCallback | null | 否 | 分享失败回调 | 6.0.0+ |
| cancelledCallback | void | null | 否 | 取消分享回调 | 6.0.0+ |

### 回调成功
`OnShareSuccessCallback` 回调对象为为一个 `Dictionary<String, Object>` ，其内容即为分享成功返回的数据，可以直接使用。

| 属性名 | 类型 | 说明 | 支持版本 |
| --- | --- | --- | --- |
| state | string | 调用成功状态，'success' | 6.0.0+ |
| errMsg | string | 调用成功信息 | 6.0.0+ |

### 回调失败

| 属性名 | 类型 | 说明 | 支持版本 |
| --- | --- | --- | --- |
| errMsg | string | 错误信息描述 | 6.0.0+ |

### 代码示例

```text
public void TestShare()
{
    var jsonData = new JsonData
    {
        ["openId"] = openIdField.text ?? "",
        ["templateId"] = templateIdField.text ?? "",
        ["query"] = queryField.text ?? ""
    };
    Debug.Log($"ShareMessageToFriendBtnClicked jsonData: {jsonData.ToJson()}");
    
    TT.ShareMessageToFriend(jsonData,
        (data) =>
        {
            Debug.Log($"ShareMessageToFriend success: {data.ToJson()}");
        },
        (errMsg) =>
        {
            Debug.Log($"ShareMessageToFriend failed: {errMsg}");
        },
        () =>
        {
            Debug.Log($"ShareMessageToFriend cancel");
        }); 
}
```

## TT.ShowShareMenu
> 6.0.0 开始支持本方法
显示当前小游戏页面的转发按钮。转发按钮位于小游戏页面右上角的“更多”中。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无论调用本 API 前当前页面是否显示转发按钮，调用本 API 均会执行成功回调 |
| 相关教程 | 无 |

### **语法 **

```text
public static void ShowShareMenu(
    TTShare.OnShowShareMenuSuccessCallback successCallback = null,
    TTShare.OnShowShareMenuFailCallback failCallback = null,
    TTShare.OnShowShareMenuCompleteCallback completeCallback = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 支持版本 |
| --- | --- | --- | --- | --- | --- |
| successCallback | OnShowShareMenuSuccessCallback | null | 否 | 成功回调 | 6.0.0+ |
| failedCallback | OnShowShareMenuFailCallback | null | 否 | 失败回调 | 6.0.0+ |
| completeCallback | OnShowShareMenuCompleteCallback | null | 否 | 完成回调 | 6.0.0+ |

### 回调失败
回调传参为 string 类型，说明如下：

| 属性名 | 类型 | 说明 | 支持版本 |
| --- | --- | --- | --- |
| errMsg | string | 错误信息描述 | 6.0.0+ |

### 代码示例

```text
public void TestShare()
{
    TT.ShowShareMenu();
}
```

## TT.HideShareMenu
> 6.0.0 开始支持本方法
隐藏转发按钮。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无论调用本 API 前当前页面是否显示转发按钮，调用本 API 均会执行成功回调 |
| 相关教程 | 无 |

### **语法 **

```text
public static void HideShareMenu(
    TTShare.OnHideShareMenuSuccessCallback successCallback = null,
    TTShare.OnHideShareMenuFailCallback failedCallback = null,
    TTShare.OnHideShareMenuCompleteCallback completeCallback = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 支持版本 |
| --- | --- | --- | --- | --- | --- |
| successCallback | OnHideShareMenuSuccessCallback | null | 否 | 成功回调 | 6.0.0+ |
| failedCallback | OnHideShareMenuFailCallback | null | 否 | 失败回调 | 6.0.0+ |
| completeCallback | OnHideShareMenuCompleteCallback | null | 否 | 完成回调 | 6.0.0+ |

### 回调失败
回调传参为 string 类型，属性如下：

| 属性名 | 类型 | 说明 | 支持版本 |
| --- | --- | --- | --- |
| errMsg | string | 错误信息描述 | 6.0.0+ |

### 代码示例

```text
public void TestShare()
{
    TT.HideShareMenu();
}
```

## TT.OnShareMessageResult
> 6.6.2 开始支持本方法
监听平台触发分享的图片、标题素材的分享的结果

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 触发分享时传入自定义标题或图片 |
| 注意事项 | 该方法可以监听由平台触发的分享(排行榜邀请分享、右上角分享)的结果，在不同宿主端具体的操作会有所差别。 该方法的实际调用链路为： 开发者注册此事件 用户点击小游戏菜单中的分享等按钮 分享行为携带了自定义标题和图片，触发 **TT.OnShareMessageResult** 返回自定义内容的审核结果 用户分享行为按照来源返回结果 |
| 相关教程 | 无 |

### **语法 **

```text
public static void OnShareMessageResult(TTShare.OnShareMessageResultCallback callback = null)
```

### **参数说明 **
回调 `OnShareMessageResultCallback` 说明如下

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 支持版本 |
| --- | --- | --- | --- | --- | --- |
| shareResult | ShareMessageResult | -- | 是 | 分享审核结果 | 6.6.2+ |

`ShareMessageResult` 的数据结构说明如下

| 属性名 | 类型 | 说明 | 支持版本 |
| --- | --- | --- | --- |
| position | string | 分享点位 top「更多面板-分享按钮」 quick_share「更多面板-好友头像」 quick_share_more「更多面板-好友头像最右处的更多按钮」 rank「排行榜」 | 6.6.2+ |
| info | Dictionary <string, ShareRecord> | 分享审核结果 key='image' \| 'title' value=ShareRecord | 6.6.2+ |
| encryptedData | string | 加密后的聊天进入信息 解密方法参考 [解密敏感数据](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/sensitive-data-process#%E8%A7%A3%E5%AF%86%E6%95%8F%E6%84%9F%E6%95%B0%E6%8D%AE) | 6.6.5+ |
| iv | string | 加密算法参数 | 6.6.5+ |

`ShareRecord` 的数据结构说明如下

| 属性名 | 类型 | 说明 | 支持版本 |
| --- | --- | --- | --- |
| expect | string | 预期来源，'official'表示平台素材，'custom'表示自定义素材, 'default'表示兜底素材 | 6.6.2+ |
| actual | string | 实际来源，'official'表示平台素材，'custom'表示自定义素材, 'default'表示兜底素材 | 6.6.2+ |
| code | int | 错误码 | 6.6.2+ |

### 错误码

| errNo | 说明 |
| --- | --- |
| 201001 | 图片尺寸不符合要求 |
| 201002 | 图片文件过大 |
| 201003 | 图片审核超时 |
| 201004 | 图片审核不通过 |
| 201005 | 图片下载超时 |
| 201006 | 图片下载失败 |
| 201007 | 图片格式不合法 |
| 201008 | 图片上传失败 |
| 201009 | 禁止自定义图片 |
| 202001 | 标题长度不合法 |
| 202002 | 标题包含非法字符 |
| 202003 | 标题审核超时 |
| 202004 | 标题审核不通过 |
| 203001 | 模板ID无效 |
| 203002 | 模板不存在 |
| 203003 | 模板已过期 |

### 代码示例

```text
public void TestOnShareMessageResult()
{
    TT.OnShareMessageResult((result) =>
    {
        Debug.Log($"OnShareMessageResult call, {result}");
    });
}
// result log 示例
{
    "position":"quick_share",
    "info":{
        "title": {
            "expected":"custom",
            "actual":"custom",
            "code":0,
        },
        "image":{
            "expected":"custom",
            "actual":"default",
            "code":201004,
        }
    },
    "encryptedData":"",
    "iv":""
}
```

## TT.OffShareMessageResult
> 6.6.2 开始支持本方法
取消 TT.OnShareMessageResult 的监听。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### 语法

```text
public static void OffShareMessageResult(TTShare.OnShareMessageResultCallback callback = null)
```

### 代码示例

```text
public void TestOffShareMessageResult()
{
    // 注销 OnShareMessageResult 回调
    TT.OffShareMessageResult((res) => null);
}
```

## TT.GetChatEnterInfo
> 6.6.5 开始支持本方法
获取聊天信息。

| 前提条件 | 该接口需要在登录后使用 |
| --- | --- |
| 业务背景 | 用户通过点击分享卡片进入游戏，在游戏内获取聊天进入信息 |
| 使用限制 | 无 |
| 注意事项 | 聊天信息属于敏感数据，请在服务端执行解密，解密方法参考 [解密敏感数据](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/sensitive-data-process#%E8%A7%A3%E5%AF%86%E6%95%8F%E6%84%9F%E6%95%B0%E6%8D%AE) |
| 相关教程 | 无 |

### 语法

```text
public static void GetChatEnterInfo(TTBaseParam param)
```

### **参数说明 **
`TTBaseParam` 的数据结构说明如下

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 支持版本 |
| --- | --- | --- | --- | --- | --- |
| success | Action<JsonData> | null | 否 | 成功回调 | 6.6.5+ |
| fail | Action<ErrorInfo> | null | 否 | 失败回调 | 6.6.5+ |
| complete | Action | null | 否 | 完成回调 | 6.6.5+ |

### 回调成功

| 属性名 | 类型 | 说明 | 支持版本 |
| --- | --- | --- | --- |
| encryptedData | string | 加密后的聊天进入信息 解密方法参考 [解密敏感数据](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/sensitive-data-process#%E8%A7%A3%E5%AF%86%E6%95%8F%E6%84%9F%E6%95%B0%E6%8D%AE) | 6.6.5+ |
| iv | string | 加密算法参数 | 6.6.5+ |

### 回调失败
回调传参为 `ErrorInfo` 类型，属性如下：

| 属性名 | 类型 | 说明 | 支持版本 |
| --- | --- | --- | --- |
| ErrorCode | int | 错误码 | 6.6.5+ |
| ErrMsg | string | 错误信息 | 6.6.5+ |

### 错误码

| errNo | errMsg | 说明 |
| --- | --- | --- |
| -1 | jssdk.getChatEnterInfo is not available | 接口不可用 |
| 10301 | The feature is not supported in app | 宿主不支持 |
| 10401 | Internal error | 网络失败（加密网络失败，不对外说明） |
| 20000 | The feature is not available in current scene | 在非分享卡片进入的场景不可用 |
| 20001 | The share card is too outdated. | 兼容老卡片没有发送者id |

### 代码示例

```text
public void GetChatEnterInfoBtnClicked()
{   
    TT.GetChatEnterInfo(new()
    {
        success = (res) =>
        {
            string encryptionData = res.ContainsKey("encryptedData") ? res["encryptedData"].ToString() : "";
            string iv = res.ContainsKey("iv") ? res["iv"].ToString() : "";
            Debug.Log($"GetChatEnterInfo success, encryptedData: {encryptionData}, iv: {iv}");

            // 后续可将 encryptionData 和 iv 发送到服务器进行解密
        },
        fail = (errInfo) =>
        {
            Debug.Log($"GetChatEnterInfo fail, errorInfo: {errInfo}");
        },
        complete = () =>
        {
            Debug.Log($"GetChatEnterInfo complete");
        }
    });
}
```

public void TestShare()
{
// 注销 OnShareAppMessage 回调
TT.OffShareAppMessage((res) => null);
}

public static void ShowShareMenu(
TTShare.OnShowShareMenuSuccessCallback successCallback = null,
TTShare.OnShowShareMenuFailCallback failCallback = null,
TTShare.OnShowShareMenuCompleteCallback completeCallback = null)

public void TestImageShare()
{
// 6.6.2 支持图片分享，【此能力需平台运营准入】
JsonData shareJson = new JsonData();
shareJson["title"] = "Some Title";
shareJson["cardImageUrl"] = "https://example.com/test.png";
shareJson["extra"] = new JsonData();
shareJson["extra"]["hashtag_list"] = videoTopics;

TT.ShareAppMessage(shareJson, (data) =>
{
Debug.Log($"ShareAppMessage success: {data["result"].ToJson()}");
},
(errMsg) =>
{
Debug.Log($"ShareAppMessage failed: {errMsg}");
},
() =>
{
Debug.Log($"ShareAppMessage cancel");
});
}

// 成功 data 数据格式示例
data = {
"result": {
"data": {}, // 内容填充参考 [tt.shareAppMessage_小游戏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-share-app-message#%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E)
"info": 'ShareMessageResult'// ShareMessageResult 见 TT.OnShareMessageResult 参数说明
}

public void GetChatEnterInfoBtnClicked()
{
TT.GetChatEnterInfo(new()
{
success = (res) =>
{
Debug.Log($"GetChatEnterInfo success, res: {res.ToJson()}");

_encryptionData = res["encryptedData"].ToString() ?? "";
_iv = res["iv"].ToString() ?? "";
},
fail = (errInfo) =>
{
Debug.Log($"GetChatEnterInfo fail, errorInfo: {errInfo}");
},
complete = () =>
{
Debug.Log($"GetChatEnterInfo complete");
}
});
}

public void TestVideoShare()
{
// 通用分享
JsonData shareJson = new JsonData();
shareJson["channel"] = "video";
shareJson["title"] = "Some Title";
shareJson["extra"] = new JsonData();
shareJson["extra"]["videoPath"] = "/xxx/xxx.mp4";//录屏分享的话，路径是 OnRecordComplete 拿到的路径
JsonData videoTopics = new JsonData();
videoTopics.SetJsonType(JsonType.Array);
videoTopics.Add("Some Topic1");
videoTopics.Add("Some Topic2");
shareJson["extra"]["videoTopics"] = videoTopics;
shareJson["extra"]["hashtag_list"] = videoTopics;

Debug.Log($"ShareAppMessageBtnClicked jsonData: {shareJson.ToJson()}");
TT.ShareAppMessage(shareJson, (data) =>
{
Debug.Log($"ShareAppMessage success: {data["result"].ToJson()}");
},
(errMsg) =>
{
Debug.Log($"ShareAppMessage failed: {errMsg}");
},
() =>
{
Debug.Log($"ShareAppMessage cancel");
});
}

// 成功 data 数据格式示例
data = {
"result": {
"data": {}, // 内容填充参考 [tt.shareAppMessage_小游戏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-share-app-message#%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E)
}

public static void HideShareMenu(
TTShare.OnHideShareMenuSuccessCallback successCallback = null,
TTShare.OnHideShareMenuFailCallback failedCallback = null,
TTShare.OnHideShareMenuCompleteCallback completeCallback = null)

public static void OffShareAppMessage(TTShare.OnshareAppMessageCallback callback = null)

public void TestShare()
{
// 通用分享
TT.OnShareAppMessage((res) =>
{
var channel = res.channel;
if (channel == "video")
{
JsonData json = new JsonData();
json["title"] = "分享标题";
json["channel"] = "video";
JsonData topic = new JsonData();
topic.Add("test1 videoTopics");
topic.Add("test2 videoTopics");
JsonData extra = new JsonData();
extra["videoTopics"] = topic;
json["extra"] = extra;

returnnew TTShare.ShareParam(
json,
(data) => { Debug.Log("分享成功"); },
(msg) => { Debug.Log("分享失败" + msg); },
() => { Debug.Log("取消分享"); }
);
}
});
}

public static void ShareMessageToFriend(JsonData options,
TTShare.OnShareSuccessCallback successCallback = null,
TTShare.OnShareFailedCallback failedCallback = null,
TTShare.OnShareCancelledCallback cancelledCallback = null)

public void TestOnShareMessageResult()
{
TT.OnShareMessageResult((result) =>
{
Debug.Log($"OnShareMessageResult call, {result}");
});
}

// result log 示例
{
"position":"quick_share",
"info":{
"title": {
"expected":"custom",
"actual":"custom",
"code":0,
},
"image":{
"expected":"custom",
"actual":"default",
"code":200000,
}

public static void OnShareMessageResult(TTShare.OnShareMessageResultCallback callback = null)

public void TestShare()
{
TT.ShowShareMenu();
}

public static void ShareAppMessage(JsonData shareJson,
TTShare.OnShareSuccessCallback successCallback = null,
TTShare.OnShareFailedCallback failedCallback = null,
TTShare.OnShareCancelledCallback cancelledCallback = null)

public void TestShare()
{
var jsonData = new JsonData
{
["openId"] = openIdField.text ?? "",
["templateId"] = templateIdField.text ?? "",
["query"] = queryField.text ?? ""
};
Debug.Log($"ShareMessageToFriendBtnClicked jsonData: {jsonData.ToJson()}");

TT.ShareMessageToFriend(jsonData,
(data) =>
{
Debug.Log($"ShareMessageToFriend success: {data.ToJson()}");
},
(errMsg) =>
{
Debug.Log($"ShareMessageToFriend failed: {errMsg}");
},
() =>
{
Debug.Log($"ShareMessageToFriend cancel");
});
}

publicvoidTestOnShareMessageResult()
{
// 注销 OnShareAppMessage 回调
TT.OffShareMessageResult((res) =>null);
}

public void TestVideoShare()
{
// 通用分享
JsonData shareJson = new JsonData();
shareJson["channel"] = "video";
shareJson["title"] = "Some Title";
shareJson["extra"] = new JsonData();
shareJson["extra"]["videoPath"] = "/xxx/xxx.mp4";//录屏分享的话，路径是 OnRecordComplete 拿到的路径
JsonData videoTopics = new JsonData();
videoTopics.SetJsonType(JsonType.Array);
videoTopics.Add("Some Topic1");
videoTopics.Add("Some Topic2");
shareJson["extra"]["videoTopics"] = videoTopics;
shareJson["extra"]["hashtag_list"] = videoTopics;

Debug.Log($"ShareAppMessageBtnClicked jsonData: {jsonData.ToJson()}");
TT.ShareAppMessage(jsonData, (data) =>
{
Debug.Log($"ShareAppMessage success: {data["result"].ToJson()}");
},
(errMsg) =>
{
Debug.Log($"ShareAppMessage failed: {errMsg}");
},
() =>
{
Debug.Log($"ShareAppMessage cancel");
});
}

// 成功 data 数据格式示例
data = {
"result": {
"data": {}, // 内容填充参考 [tt.shareAppMessage_小游戏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-share-app-message#%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E)
}

public void TestShare()
{
TT.HideShareMenu();
}

publicstaticvoidOffShareMessageResult(TTShare.OnShareMessageResultCallback callback = null)

publicstaticvoidGetChatEnterInfo(TTBaseParam param)

public void TestShare()
{
JsonData shareJson = new JsonData();
shareJson["title"] = "Some Title";
shareJson["templateId"] = "";    // 替换成通过审核的分享ID

TT.ShareAppMessage(shareJson, (data) =>
{
Debug.Log($"ShareAppMessage success: {data["result"].ToJson()}");
},
(errMsg) =>
{
Debug.Log($"ShareAppMessage failed: {errMsg}");
},
() =>
{
Debug.Log($"ShareAppMessage cancel");
});
}

// 成功 data 数据格式示例
data = {
"result": {
"data": {}, // 内容填充参考 [tt.shareAppMessage_小游戏](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/retweet/tt-share-app-message#%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E)
}

public static void OnShareAppMessage(TTShare.OnshareAppMessageCallback callback = null)

注意：
该模块对应 [分享](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#7631fac2)
