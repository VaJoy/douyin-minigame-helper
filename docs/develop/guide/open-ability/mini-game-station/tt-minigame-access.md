---
title: "小游戏tt.navigateToMiniProgram接入"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/open-ability/mini-game-station/tt-minigame-access
update_time: 2025-09-08
---

**此接口仅适用于抖音小游戏站之间跳转。**

| 业务背景 | 无 |
| --- | --- |
| 版本限制 | ●  普通小游戏： Android - 抖系宿主（抖音、抖极）33.4.0版本起，**支持跳转到抖音小游戏站小程序**；<33.4.0版本请升级抖音版本。 iOS - 不限版本，无需配置。 ●  unity小游戏： Android、iOS - 抖系宿主（抖音、抖极）33.4.0版本起支持调用该能力。 TTSDK - 请更新到版本6.2.6。 |
| 注意事项 | 该 API 必须要由用户点击触发，也就是只能在 tt.onTouchEnd 的回调里面同步调用该 API。 |
| 支持沙盒 | 否 |
| 相关教程 | 无 |

## 普通小游戏
### 语法

```js
tt.navigateToMiniProgram(options)
```

### 参数说明
options 为 object 类型，属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 | 最低支持版本 |
| --- | --- | --- | --- | --- | --- |
| path | string |  | 否 | 要跳转的小程序页面路径（不传则默认打开首页），允许携带 query 参数，格式详见示例；  **请注意：** 1.页面路径path：可通过“开发者后台-运营能力-小游戏站-运营管理”生成对应的首页链接 | 1.15.0 |
| extraData | object |  | 否 | 需要传递给目标小程序的数据，目标小程序可在 [App.onLaunch](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/framework/logic-layer/start-app/#app)，[App.onShow](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/framework/logic-layer/start-app/#app)，[tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/foundation/lifecycle/tt-get-launch-options-sync/) 中获取到这份数据。如果跳转的是小游戏，可以在 tt.onShow，tt.getLaunchOptionsSync 中获取到这份数据 | 1.15.0 |
| envVersion | enum | current | 否 | 要打开的小程序版本。合法的值有 current--线上版；latest--测试版。仅在当前小程序为开发版或测试版时此参数有效。如果当前小程序是正式版，则打开的小程序必定是正式版 | 1.15.0 |
| appId | string |  | 是 | 要跳转的小程序APPID：ttc9e5bf5856eff54001 | 1.15.0 |
| success | function |  | 否 | 接口调用成功的回调函数 | 1.15.0 |
| fail | function |  | 否 | 接口调用失败的回调函数 | 1.15.0 |
| complete | function |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） | 1.15.0 |

### 回调成功
object 类型，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| errMsg | string | "navigateToMiniProgram:ok" | 1.15.0 |

### 回调失败
object 类型，属性如下：

| 属性名 | 类型 | 说明 | 最低支持版本 |
| --- | --- | --- | --- |
| errMsg | string | "navigateToMiniProgram:fail" + 详细错误信息 | 1.15.0 |

### 错误码

| errorCode | errMsg | 说明 |
| --- | --- | --- |
| 21100 | navigateToMiniProgram:fail unSupport on game | 若跳转至非小游戏站appid，则会进行此错误码报错，小游戏站appid无需加白，可直接设置跳转 |
| 21102 | navigateToMiniProgram:fail appId %s is not in navigateToMiniProgramAppIdList | 未在game.json的navigateToMiniProgramAppIdList属性中配置对应跳转的小程序/小游戏id |
| 10502 | navigateToMiniProgram:fail cancel | 用户取消 |
| 10403 | navigateToMiniProgram:fail onBusinessError | 平台内部错误，有需要请[创建工单](https://developer.open-douyin.com/work-order-page?tab=workOrderRecord)咨询 |
| 10401 | navigateToMiniProgram:fail appConfig is null | unity小游戏需使用抖音33.4.0及以上版本 |

### 代码示例

```js
tt.navigateToMiniProgram({
    appId: 'ttc9e5bf5856eff54001',    // 小游戏站appid
    path: 'xxx',
    success: (res) => {
    },
    fail: (res) => {
    },
  });
```

## Unity小游戏
> TTSDK 6.2.6及以上版本支持该能力
### 语法

```csharp
public static void NavigateToMiniProgram(NavigateToMiniProgramParam param)
```

### 参数说明
param 为 NavigateToMiniProgramParam 类型，属性参数如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| AppId | string |  | 是 | 要跳转的小程序APPID：ttc9e5bf5856eff54001 |
| Path | string |  | 否 | 要跳转的小程序页面路径（不传则默认打开首页），允许携带 query 参数，格式详见示例； **请注意：** 1.页面路径path：可通过“开发者后台-运营能力-小游戏站-运营管理”生成对应的首页链接 |
| ExtraData | Dictionary<string, string> |  | 否 | 需要传递给目标小程序的数据，目标小程序可在 [App.onLaunch](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/framework/logic-layer/start-app/#app)，[App.onShow](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/framework/logic-layer/start-app/#app)，[tt.getLaunchOptionsSync](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/foundation/lifecycle/tt-get-launch-options-sync/) 中获取到这份数据。如果跳转的是小游戏，可以在 tt.onShow，tt.getLaunchOptionsSync 中获取到这份数据 |
| EnvVersion | enum EnvVersionEnum | EnvVersionEnum.Current | 否 | 要打开的小程序版本。EnvVersionEnum.Current--线上版；EnvVersionEnum.Latest--测试版。仅在当前小程序为开发版或测试版时此参数有效。如果当前小程序是正式版，则打开的小程序必定是正式版 |
| Success | NavigateToMiniProgramSuccessCallback |  | 否 | 接口调用成功的回调函数 |
| Fail | Action<ErrorInfo> |  | 否 | 接口调用失败的回调函数 |
| Complete | Action |  | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

### 回调成功
NavigateToMiniProgramSuccessResult 类型包含属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "navigateToMiniProgram:ok" |

### 错误码
同普通小游戏
### 代码示例

```js
TT.NavigateToMiniProgram(new NavigateToMiniProgramParam()
{
    AppId = appId,
    Path = path,
    ExtraData = extraData,
    EnvVersion = envVersion,
    Success = (res) =>
    {
        Debug.Log($"NavigateToMiniProgram Success: ${res.ErrMsg}");
    },
    Fail = (errInfo) =>
    {
        Debug.Log($"NavigateToMiniProgram Fail, ErrMsg : ${errInfo.ErrMsg},ErrCode: ${errInfo.ErrorCode},ErrType: ${errInfo.ErrorType}");
    },
    Complete = () =>
    {
        Debug.Log("NavigateToMiniProgram Complete");
    }
});
```
