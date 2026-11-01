---
title: "tt.getLocation"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/location/tt-get-location
update_time: 2024-08-19
---

## 语法

```js
tt.getLocation(type)
```
基础库 1.0.0 开始支持本方法，这是一个**异步**方法。
获取设备当前的地理位置。

## 示例代码
```js
tt.getLocation({
  success(res) {
    console.log(`经度${res.longitude}，维度${res.latitude}`);
  },
  fail(res) {
    console.log(`getLocation调用失败`);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| type | string | 否 | "wgs84" | 1.0.0 | 指定坐标系类型，可以是 "wgs84" 或 "gcj02" |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getLocation:ok" - **altitude**（number）：高度，单位 m - **accuracy**（number）：位置的精确度，反应与真实位置之间的接近程度，可以理解成10即与真实位置相差10m，越小越精确 - **verticalAccuracy**（number）：垂直精度，单位 m（Android 需要系统 8.0 及以上机型并且开启 GPS，否则返回 0） - **horizontalAccuracy**（number）：水平精度，单位 m - **speed**（number）：速度，单位 m/s - **city**（string）：定位到的城市信息（因整体性能考虑，不开放返回 iOS 端的城市数据，可基于经纬度自行测算） - **latitude**（string）：纬度，范围为-90 ~ 90，正数表示北，负数表示南 - **longitude**（string）：经度，范围为-180 ~180，正数表示东，负数表示西 |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："getLocation:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21301 | locate fail, $errMsg |  |  |
| 10403 | internal error |  |  |
| 10401 | Internal error: locationManagerPlugin is nil |  |  |
| 10501 | app in background |  |  |
| 10200 | system auth deny |  |  |
| 21201 | Unable to access your location |  |  |
| 20000 | /s |  |  |
| 21301 | locate fail, invalid lat lng |  |  |
| 21301 | locate fail, user permission denied |  |  |

## 注意事项
- 该 API 有一定性能消耗，请注意不要频繁调用以防设备过热和耗电过快。小游戏框架也会做相应的节流处理。
- 如果要将返回值使用在 [openLocation](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/location/tt-open-location/) 中，必须指定坐标系为 "gcj02"

## 用户授权说明
该 API 需要用户授权方可调用，详细信息可参考[用户授权](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/other/user-authorization)。位置精度和调用耗时会因设备而异。

## 授权要求
无需开发者授权；需要用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/location/tt-get-location) / [本地体验路径](tt-get-location)
