---
title: "获取位置"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/location/get-location
update_time: 2025-09-02
---

## TT.GetLocation
> 6.5.4开始支持本方法
获取设备当前的地理位置。

| 前提条件 | 该 API 需要用户授权方可调用，详细信息可参考[用户授权](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/other/user-authorization)。位置精度和调用耗时会因设备而异。 |
| --- | --- |

### 语法

```csharp
public static void GetLocation(TTGetLocationParam param)
```

### 参数说明
TTGetLocationParam包含以下参数

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| type | string | "wgs84" | 否 | 指定坐标系类型，可以是 "wgs84" 或 "gcj02" |
| success | Action<GeneralCallbackResult> | null | 否 | 成功回调 |
| fail | Action<ErrorInfo> | null | 否 | 失败回调 |
| complete | Action<GeneralCallbackResult> | null | 否 | 完成回调 |

### 回调成功
TTGetLocationSuccessCallbackResult包含以下参数：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "getLocation:ok" |
| altitude | double | 高度，单位 m |
| accuracy | double | 位置的精确度，反应与真实位置之间的接近程度，可以理解成10即与真实位置相差10m，越小越精确 |
| verticalAccuracy | double | 垂直精度，单位 m（Android 需要系统 8.0 及以上机型并且开启 GPS，否则返回 0） |
| horizontalAccuracy | double | 水平精度，单位 m |
| speed | double | 速度，单位 m/s |
| city | string | 定位到的城市信息（因整体性能考虑，不开放返回 iOS 端的城市数据，可基于经纬度自行测算） |
| latitude | string | 纬度，范围为-90 ~ 90，正数表示北，负数表示南 |
| longitude | string | 经度，范围为-180 ~180，正数表示东，负数表示西 |

### 回调失败
ErrorInfo包含以下参数：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| ErrorCode | int | 错误码 |
| ErrMsg | string | 错误信息。"startCompass:fail" + 详细错误信息 |

### 错误码
参考
### 代码示例

```csharp
private void Test() {
    TT.GetLocation(new TTGetLocationParam()
    {
        success = result =>
        {
            Debug.Log($"GetLocation success, result -->{result.ToJson()}");
        },
        fail = result =>
        {
            Debug.Log($"GetLocation fail, errCode -->{result.ErrorCode}, errMsg -->{result.ErrMsg}");
        },
        complete = result =>
        {
            Debug.LogAppended("GetLocation complete");
        },
    });
}
```
