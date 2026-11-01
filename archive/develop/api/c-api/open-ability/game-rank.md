---
title: "好友排行榜"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/game-rank
update_time: 2026-05-11
---

游戏中好友排行榜相关。

> 注意：
> 该模块对应 [好友排行榜](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#52090c07) 。

## TT.SetImRankData
> 6.0.0 开始支持本方法
在关键的游戏场景，设置写入用户的排行榜数据（游戏成绩信息），该数据会上传到服务端。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | **字段解释** |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void SetImRankData(
    JsonData paramJson,
    Action<bool, string> action = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| paramJson | JsonData | -- | 是 | 相关参数使用 json 格式传入。 | 6.0.0 |
| action | Action<bool, string> | null | 否 | 回调函数，返回是否成功和错误信息。 | 6.0.0 |

`paramJson`的数据格式说明如下

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| dataType | int |  | 是 | 数据解析类型，可选值有 0 或 1。 0 表示数据被解析为数值。 1 表示数据被解析为字符串。 | 6.0.0 |
| value | string |  | 是 | 展示出来的数值，dataType 为 0 时只能传正数的**字符串  **（如'103', '105'）,且取值范围为** [0, int32_MAX)**，否则会报错。 dataType 为 1 时，则可传入任意字符串（eg：'青铜'、'白银'）。 | 6.0.0 |
| extra | string |  | 否 | 补充字段。字节数要求不超过 128。 | 6.0.0 |
| priority | int | 0 | 否 | 用于判断权重 ，仅当  dataType 为 1 时需要，不传则使用默认值 0。如传入 value 为'白银'，priority 为 2，则白银的权重为 2，传入value 为 '黄金'，priority 为 3，则黄金的权重为3，高于白银，届时生成的榜单，黄金段位会排在白银前面。 | 6.0.0 |
| zoneId | string | default | 否 | 排行榜分区标识，取值可以是 'default' 或 'test' 或其他开发者自定义字符串，'default' 表示为默认的线上分区，'test' 表示测试分区。不同分区的排行榜数据存在数据隔离，如 zoneId='test' 设置的数据不会影响 zoneId='default' 的排行榜，可用于测试环境。目前每个小游戏除了 default 和 test， 最多可支持 10 个分区。 | 6.0.0 |

### 代码示例
【代码示例1】一个跑酷游戏，想要对用户的跑酷分数做排序

```csharp
public void TestImRank()
{
    var paramJson = new JsonData
    {
        ["dataType"] = 0,    // 分数为数字类型
        ["value"] = "999",    //  该用户得了 999 分
        ["priority"] = 0,        // dataType为数字类型，不需要权重，直接传0
        ["zoneId"] = "test"
    };
    TT.SetImRankData(paramJson, (isSuccess, errMsg) =>
    {
        if (isSuccess)
        {
            Debug.Log("SetImRankData success");
        }
        else
        {
            Debug.Log($"SetImRankData fail res: {errMsg}");
        }
    });
}
```

【代码示例2】一个moba游戏，想要对用户的段位进行排序

```csharp
public void TestImRank()
{
    var paramJson = new JsonData
    {
        ["dataType"] = 1,    // 成绩为枚举类型，因为段位不是一个数字
        ["value"] = "秩序白银",    // 该用户段位为白银
        ["priority"] = 2,        //dataType为 1，需要权重，该游戏排序为 青铜（1）、白银（2）、黄金（3）、王者（4），因此此处传2
        ["zoneId"] = "default"
    };
    TT.SetImRankData(paramJson, (isSuccess, errMsg) =>
    {
        if (isSuccess)
        {
            Debug.Log("SetImRankData success");
        }
        else
        {
            Debug.Log($"SetImRankData fail res: {errMsg}");
        }
    });
}
```

## TT.GetImRankList
> 6.0.0 开始支持本方法
获取排行榜列表，调用 API 后， 根据参数自动绘制游戏好友排行榜（ native UI ）。

| 前提条件 | 在拉起排行榜前，需要调用 TT.Login 接口进行用户登录，否则可能会出现榜单无法拉起或闪退的问题 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | **排序规则：** 数字类型则按照传入的 value 从大到小排序，若数字大小相同，按照写入时间从早到晚排序 枚举类型按照权重从高到低排序，若权重相同，按照写入时间从早到晚排序   **参数字段对应解释：** |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void GetImRankList(JsonData paramJson,
    Action<bool, string> action = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| paramJson | JsonData | -- | 是 | 相关参数使用 json格式传入。 | 6.0.0 |
| action | Action<bool, string> | null | 否 | 回调函数，返回是否成功和错误信息。 | 6.0.0 |

`paramJson`的数据格式说明如下

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| dataType | int |  | 是 | 数据解析类型，可选值有 0 或 1。 0 表示数据被解析为数值。 1 表示数据被解析为字符串。 | 6.0.0 |
| rankType | string |  | 是 | 排行榜类型。 day 天榜，每天更新。 week 周榜，每周更新。 month 月榜，每月更新。 all 总榜。 | 6.0.0 |
| zoneId | string | default | 否 | 排行榜分区标识，取值可以是 'default' 或 'test' 或其他开发者自定义字符串，'default' 表示为默认的线上分区，不同分区的排行榜数据存在数据隔离，如 zoneId='test' 设置的数据不会影响通过 zoneId='default' 的排行榜，可用于测试环境。目前每个小游戏除了 default 和 test， 最多可支持 10 个分区。 | 6.0.0 |
| suffix | string |  | 否 | 分数后缀补充文案。 | 6.0.0 |
| rankTitle | string |  | 否 | 排行榜标题。 | 6.0.0 |
| relationType | string | friend | 否 | 关系类型。 default 表示同时获取好友榜和总榜。 all 表示获取总榜。 friend 表示获取当前登录用户的好友榜。 | 6.0.0 |
| shareImageUrl | string |  | 否 | 排行榜分享卡片展示的封面图。 | 6.6.2 |
| shareTitle | string |  | 否 | 排行榜分享卡片展示的标题。 | 6.6.2 |

### 代码示例

```csharp
public void TestImRank()
{
    var paramJson = new JsonData
    {
        ["zoneId"] = "default",
        ["suffix"] = "分",
        ["rankTitle"] = "每周排行榜",
        ["dataType"] = 0,
        ["relationType"] = "default",
        ["rankType"] = "week",
        ["shareImageUrl"] = "https://example.com/test.png",
        ["shareTitle"] = "分享标题"
    }; 
    TT.GetImRankList(paramJson, (isSuccess, errMsg) =>
    {
        if (isSuccess)
        {
            Debug.Log("GetImRankList success");
        }
        else
        {
            Debug.Log($"GetImRankList fail with error message: {errMsg}");
        }
    });
}
```

## TT.GetImRankData
> 6.0.0 开始支持本方法
获取排序好的「好友/总榜」数据源，开发者基于数据源自行渲染返回的数据。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 该方法需要在开放数据域中使用，请访问 [开放数据域能力介绍](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/relationship-chain/open-data-base/)进行通信 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void GetImRankData(JsonData paramJson,
    TTRank.OnGetRankDataSuccessCallback onGetRankDataSuccessCallback,
    TTRank.OnGetRankDataFailCallback onGetRankDataFailCallback)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| paramJson | JsonData | -- | 是 | 相关参数使用 json格式传入 |
| onGetRankDataSuccessCallback | TTRank.OnGetRankDataSuccessCallback | -- | 是 | 获取成功回调 |
| onGetRankDataFailCallback | TTRank.OnGetRankDataFailCallback | -- | 是 | 获取失败回调 |

`paramJson`的数据格式说明如下

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| dataType | int |  | 是 | 数据解析类型，可选值有 0 或 1。 0 表示数据被解析为数值。 1 表示数据被解析为字符串。 | 6.0.0 |
| rankType | string |  | 是 | 排行榜类型。 day 天榜，每天更新。 week 周榜，每周更新。 month 月榜，每月更新。 all 总榜。 | 6.0.0 |
| pageSize | int |  | 是 | 每页长度，大于0小于40。 | 6.0.0 |
| pageNum | int |  | 是 | 页码，从1开始。 | 6.0.0 |
| zoneId | string | default | 否 | 排行榜分区标识，取值可以是 'default' 或 'test' 或其他开发者自定义字符串，'default' 表示为默认的线上分区，不同分区的排行榜数据存在数据隔离，如 zoneId='test' 设置的数据不会影响通过 zoneId='default' 的排行榜，可用于测试环境。目前每个小游戏除了 default 和 test， 最多可支持 10 个分区。 | 6.0.0 |
| relationType | string | friend | 否 | 关系类型。 all 表示获取总榜。 friend 表示获取当前登录用户的好友榜。 | 6.0.0 |

### 回调成功
`onGetRankDataSuccessCallback` 回调对象为 `RankData` 类型，数据结构说明如下

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| Items | List<RankResItem> | 获取的榜单数据 | 6.0.0 |
| SelfItem | SelfRankResItem | 请求者自己的数据 | 6.0.0 |
| PageNum | int | 页码，从1开始 | 6.0.0 |
| TotalNum | int | 总条数 | 6.0.0 |
| SelfUserInfo | UserInfo | 用户个人信息 | 6.0.0 |

`RankResItem` 类型数据结构说明如下

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| DataType | int | 数据解析类型，可选值有 0 或 1。 0 表示数据被解析为数值。 1 表示数据被解析为字符串。 | 6.0.0 |
| Value | string | 分数值或枚举名称，代表分数值时只能传正数 | 6.0.0 |
| Priority | int | 类型为枚举时有意义，返回值为正整数 | 6.0.0 |
| Extra | string | 传入的附加字段，小游戏只负责透传 | 6.0.0 |
| OpenId | string | 用户的 openid | 6.0.0 |
| SecUid | string | 加密后的 uid | 6.0.0 |
| UserImg | string | 用户头像 | 6.0.0 |
| Nickname | string | 用户昵称 | 6.0.0 |
| UTime | Int64 | unix秒级时间戳 | 6.0.0 |

`SelfRankResItem` 类型数据结构说明如下

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| Item | RankResItem | 用户自己的排行数据 | 6.0.0 |
| Rank | int | 从 1 开始的排序，返回 0 表示不在排行榜内 | 6.0.0 |
| PrivateSetting | int | 隐私设置，0：所有人可见，1：仅好友可见，2：仅自己可见 | 6.0.0 |

`UserInfo` 类型数据结构说明如下

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| OpenId | string | 用户 openid | 6.0.0 |
| SecUid | string | 加密后的 sec_uid | 6.0.0 |
| UserImg | string | 用户头像 | 6.0.0 |
| Nickname | string | 用户昵称 | 6.0.0 |

### 回调失败
`OnGetRankDataFailCallback` 回调返回错误信息。

### 代码示例

```csharp
public void TestImRank()
{
    var paramJson = new JsonData
    {
        ["relationType"] = "friend",
        ["dataType"] = 0,
        ["rankType"] = "month",
        ["pageNum"] = 1,
        ["pageSize"] = 40,
        ["zoneId"] = "default",
    };
    TT.GetImRankData(paramJson, 
        (ref TTRank.RankData data) =>
        {
            Debug.Log(data.ToString());
            Debug.Log($"data: {data}");
            Debug.Log($"data: {data.Items.Count}");
            for (var i = 0; i < data.Items.Count; i++)
            {
                Debug.Log($"item-->nickName :{data.Items[i].Nickname}, openId:{data.Items[i].OpenId}");    
            }
            Debug.Log("GetImRankData success");
        }, msg => { 
            Debug.Log("GetImRankData fail error message:" + msg); 
        });
}
```
