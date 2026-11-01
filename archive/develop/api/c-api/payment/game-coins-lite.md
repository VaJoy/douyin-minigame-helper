---
title: "游戏金币（仅抖音 lite）"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/payment/game-coins-lite
update_time: 2024-10-12
---

[激励能力接入指引](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/operation1/ability/incentive/guidelines)
## TT.RequestGoldOrder

> 注意：
> 该模块对应 [旧版Unity SDK文档中的 【金币游戏支持】 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#5c85d32b)

> 6.0.0 开始支持本方法，WebGL也支持该方法
金币发放 or 扣除。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 仅在当前小游戏生效，离开小游戏后设置失效。 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void RequestGoldOrder(
    JsonData paramJson,
    Action<JsonData> successCallback, 
    Action completeCallback,
    Action<int, string> errorCallback)
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| paramJson | JsonData | -- | 是 | 金币参数使用json的形式传入，例如：{"type":1,"bizId":"xxxxx","goldNum":1,"customId":"xxxx"} |
| successCallback | Action<JsonData> | -- | 是 | 接口调用成功的回调函数 |
| completeCallback | Action | -- | 是 | 接口调用完成的回调函数 |
| failCallback | Action<string> | -- | 是 | 接口调用失败的回调函数 |

paramJson 为 JsonData 包含下列键值对：

| 键 | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| type | string | -- | 是 | 订单类型,1-发放金币，2-消耗金币 |
| bizId | string | -- | 是 | 点位ID，在开发者后台中金币配置中获取, string |
| goldNum | int | -- | 是 | 金币数量, int |
| customId | string | -- | 是 | 开发者自定义的订单号, string |

### 代码示例

```csharp
private void Test() {
    var bizId = "xxxx";
    var goldNum = 100;
    var customId = DateTime.UtcNow.ToUniversalTime().Millisecond+"-"+Random.Range(0,11);
    var paramJson = new JsonData
    {
        ["type"] = dropdownEnumsList[dropdownSelectIndex],
        ["bizId"] = bizId,
        ["goldNum"] = goldNum,
        ["customId"] = customId
    };
    Debug.Log($"RequestGoldOrder param :{paramJson.ToJson()}");
    TT.RequestGoldOrder(paramJson,
        orderId =>
        {
            var printText = $"requestGoldOrder success, {orderId}";
            Debug.Log(printText);
        }, () =>
        {
            var printText = $"requestGoldOrder complete";
            Debug.Log(printText);
        },
        (errorCode, errorMsg) =>
        {
            var printText = $"requestGoldOrder error, errorCode :{errorCode}, errorMsg:{errorMsg}";
            Debug.Log(printText);
        });
}
```
