---
title: "账号"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/account
update_time: 2026-03-25
---

## TT.Login

> 注意：
> 该模块对应 [旧版Unity SDK文档中的 【登录】 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#d68fd7bc)

> 6.0.0 开始支持本方法，WebGL支持该方法
登录-获取临时登录凭证。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | force 为 true 时（默认值为 true），如果用户未在端登录（例如未在头条 APP 登录），则会调起端的登录窗口，如果用户点击取消则会调用 fail 回调 只有端登录的用户 success 才有 code，否则只有 anonymousCode code 可以换取 openid，openid 是用户的唯一标识 anonymousCode 可以换取 anonymous_openid，同一台手机的 anonymous_openid 是相同的 |
| 相关教程 | 无 |

### **语法 **

```csharp
public void Login(OnLoginSuccessCallback successCallback,
    OnLoginFailedCallback failedCallback,
    bool forceLogin = true)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| successCallback | delegate void OnLoginSuccessCallback(string code, string anonymousCode, bool isLogin) | -- | 是 | 登录成功的回调 |
| failedCallback | delegate void OnLoginFailedCallback(string errMsg) | -- | 是 | 登录失败的回调 |
| forceLogin | Bool | true | 否 | 未登录时, 是否强制调起登录框 |

### 代码示例

```csharp
private void Test() {
    var force = true;
    TT.Login((code, anonymousCode, isLogin) =>
        {
            Debug.Log($"TestLogin: force:{force},code:{code},anonymousCode:{anonymousCode},isLogin:{isLogin}");
            Code = code;
            AnonymousCode = anonymousCode;
        },
        (msg) => { Debug.Log($"TestLogin: force:{force},{msg}"); }, force);
 }
```

## TT.CheckSession
> 6.0.0 开始支持本方法，WebGL支持该方法
检查用户当前的 session 状态是否有效。
只有成功调用 login 才会生成 session，checkSession 才会进入 success 回调，当用户退出登录会清除 session。
session_key 会随着 login 接口的调用被刷新。可以通过 checkSession 方法验证当前 session 是否有效，从而避免频繁登录。
目前实际测试若使用匿名登录（forceLogin = false），则 checkSession 会一直返回 fail。
只有登录了宿主（forceLogin = true），checkSession 才会返回 success ，下次不用 login checkSession 也可以返回 true。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 只有成功调用 [tt.login](https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/api/open-interface/log-in/tt-login/) 才会生成 session，tt.checkSession 也会因此进入 success 回调，当用户退出登录会清除 session |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void CheckSession(TTAccount.OnCheckSessionSuccessCallback successCallback,
   TTAccount.OnCheckSessionFailedCallback failedCallback)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| successCallback | delegate void OnCheckSessionSuccessCallback() | -- | 是 | 验证有效的回调 |
| failedCallback | delegate void OnCheckSessionFailedCallback(string errMsg) | -- | 是 | 验证无效或者验证失败的回调 |

### 代码示例

```csharp
private void Test() {
    TT.CheckSession(() => { Debug.Log($"TestCheckSession success session"); },
        (errMsg) => { Debug.Log($"TestCheckSession fail: {errMsg}"); });
}
```

## TT.GetUserInfo
> 6.0.0 开始支持本方法，WebGL支持该方法
获取已登录用户的基本信息或特殊信息。
若匿名登录后 userinfo 里面字段全部为默认值。
登录了宿主后可以获取账号数据，下次不用 login GetUserInfo 也可以返回正确数据。
### **语法 **

```csharp
public static void GetUserInfo(TTAccount.OnGetUserInfoSuccessCallback successCallback,
   TTAccount.OnGetUserInfoFailedCallback failedCallback)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| successCallback | delegate void OnGetUserInfoSuccessCallback(ref TTUserInfo scUserInfo) | -- | 是 | 获取用户信息成功的回调 |
| failedCallback | delegate void OnGetUserInfoFailedCallback(string errMsg) | -- | 是 | 获取用户信息失败的回调 |

**TTUserInfo **为登录后获取登录的用户信息**，**** **属性如下：

| **属性名 ** | **类型 ** | **说明 ** |
| --- | --- | --- |
| avatarUrl | string | 用户头像 |
| nickName | string | 用户名 |
| gender | int | 用户性别，0: 未知(默认值)；1:男性；2:女性 |
| city | string | 城市 |
| province | string | 省份 |
| country | string | 用户国家 |
| language | string | 用户语言，目前为空 |
| signature | string | 加密签名 |
| encryptedData | string | 加密数据 |
| iv | string | 秘钥IV |
| cloudId | string | 抖音云CloudId |

### 代码示例

```csharp
private void Test() {
    TT.GetUserInfo(
        (ref TTUserInfo scUserInfo) => { Debug.Log($"TestGetUserInfo info: {scUserInfo.ToString()}"); },
        (errMsg) => { Debug.Log($"TestGetUserInfo fail: {errMsg}"); });
}
```

## TT.GetUserInfoAuth
> 6.0.0 开始支持本方法，WebGL支持该方法
判断用户是否已经授权给当前游戏读取个人信息。
该 API 会调用宿主的代码，如果调用宿主代码成功则会调用 onGetUserInfoAuth ，并返回是否已经授权。
如果调用宿主代码失败则会调用 onGetUserInfoAuthFail 。
### **语法 **

```csharp
public static void GetUserInfoAuth(TTAccount.OnGetUserInfoAuthSuccess onGetUserInfoAuth,
   TTAccount.OnGetUserInfoAuthFail onGetUserInfoAuthFail)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| successCallback | delegate void OnGetUserInfoAuthSuccess(bool auth); | -- | 是 | 调用宿主代码成功，并返回是否已经授权读取用户信息 |
| failedCallback | delegate void OnGetUserInfoAuthFail(string errMsg) | -- | 是 | 调用宿主代码时发生错误 |

**OnGetUserInfoAuthSuccess **参数如下：

| **属性名 ** | **类型 ** | **说明 ** |
| --- | --- | --- |
| auth | bool | 是否授权 |

### 代码示例

```csharp
private void Test() {
    TT.GetUserInfoAuth(
        (auth) => { Debug.Log($"TestGetUserInfoAuth info auth: {auth}"); },
        (errMsg) => { Debug.Log($"TestGetUserInfoAuth fail: {errMsg}"); });
}
```

## TT.OpenSettingsPanel
> 6.0.0 开始支持本方法，WebGL支持该方法
主动打开获取用户信息的授权界面，在 Setting 界面关闭后返回最新的授权状态，该方法没有超时时间。
该 API 会调用宿主的代码，如果调用宿主代码成功则会调用 onGetUserInfoAuth ，并返回最新的授权状态。
如果调用宿主代码失败则会调用 onGetUserInfoAuthFail 。
### **语法 **

```csharp
public static void OpenSettingsPanel(TTAccount.OnGetUserInfoAuthSuccess onGetUserInfoAuth,
    TTAccount.OnGetUserInfoAuthFail onGetUserInfoAuthFail)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| successCallback | delegate void OnGetUserInfoAuthSuccess(bool auth); | -- | 是 | 调用宿主代码成功，并返回是否已经授权读取用户信息 |
| failedCallback | delegate void OnGetUserInfoAuthFail(string errMsg) | -- | 是 | 调用宿主代码时发生错误 |

### 代码示例

```csharp
private void Test() {
    TT.OpenSettingsPanel(
        (auth) => { Debug.Log($"TestOpenSettingPanel info new auth: {auth}"); },
        (errMsg) => { Debug.Log($"TestOpenSettingPanel fail: {errMsg}"); });
}
```

## TT.GetSetting
[小游戏对应接口描述](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/set/tt-get-setting)

> 注意：
> 该模块对应 [旧版Unity SDK文档中的 【获取授权信息】 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#55170a57)

> 6.0.0 开始支持本方法，WebGL支持该方法
获取用户已经授权过的配置。
结果中只会包含向用户请求过的权限。
与 OpenSetting 的区别是 GetSetting 只会获取配置，而不会打开配置页面。
### **语法 **

```csharp
public static void GetSetting(TTAccount.OnGetSettingSuccess onGetSettingSuccess,
    TTAccount.OnGetSettingFail onGetSettingFail)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| successCallback | delegate void OnGetSettingSuccess(AuthSetting authSetting) | -- | 是 | 接口调用成功的回调函数 |
| failedCallback | delegate void OnGetSettingFail(string errMsg) | -- | 是 | 接口调用失败的回调函数 |

**AuthSetting** 为用户权限授权结果类，属性如下：

| **属性名 ** | **类型 ** | **说明 ** |
| --- | --- | --- |
| UserInfo | bool | 是否授权用户信息  对应接口：tt.getUserInfo |
| UserLocation | bool | 是否授权地理位置  对应接口：tt.getLocation |
| Record | bool | 是否授权录音功能  对应接口：tt.getRecorderManager.start |
| Album | bool | 是否授权保存到相册  对应接口：tt.saveImageToPhotosAlbum tt.saveVideoToPhotosAlbum |
| Camera | bool | 是否授权摄像头 对应接口：tt.scanCode tt.chooseImage tt.chooseVideo |
| ScreenRecord | bool | 是否授权录屏，默认为开。在 onError 里面报错到没有录屏权限时，可以尝试主动调用  对应接口：tt.getGameRecorderManager |
| Calendar | bool | 是否授权添加日历事件  对应接口：tt.addPhoneCalendar |

### 代码示例

```csharp
private void Test() {
    TT.GetSetting(
        (auth) => { Debug.Log($"TestGetSetting info new auth: {auth}"); },
        (errMsg) => { Debug.Log($"TestGetSetting fail: {errMsg}"); });
}
```

## TT.OpenSetting
[小游戏对应接口描述](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/set/tt-open-setting)

> 注意：
> 该模块对应 [旧版Unity SDK文档中的 【打开授权页面】 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#261acddd)

> 6.0.0 开始支持本方法，WebGL支持该方法
获取用户已经授权过的配置。
结果中只会包含向用户请求过的权限。
与 OpenSetting 的区别是 GetSetting 只会获取配置，而不会打开配置页面。
### **语法 **

```csharp
public abstract void OpenSetting(OnOpenSettingSuccess onOpenSettingSuccess,
    OnOpenSettingFail onOpenSettingFail);
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| successCallback | delegate void OnOpenSettingSuccess(AuthSetting authSetting) | -- | 是 | 接口调用成功的回调函数 |
| failedCallback | delegate void OnOpenSettingFail(string errMsg) | -- | 是 | 接口调用失败的回调函数 |

### 代码示例

```csharp
private void Test() {
    TT.OpenSetting(
        (auth) => { Debug.Log($"TestOpenSetting info new auth: {auth}"); },
        (errMsg) => { Debug.Log($"TestOpenSetting fail: {errMsg}"); });
}
```

## TT.SetRealNameAuthenticationCallback
> 6.0.0 开始支持本方法，WebGL支持该方法
用户在实名认证弹窗完成实名认证后回调。
需要在初始化时设置，回调时机为：游戏中弹出实名认证，用户完成了实名认证时触发。
### **语法 **

```csharp
public static void SetRealNameAuthenticationCallback(
    TTAccount.OnRealNameAuthentication onRealNameAuth)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| onRealNameAuth | delegate void OnRealNameAuthentication() | -- | 是 | 用户实名认证成功的回调 |

### 代码示例

```csharp
private void Test() {
    TT.SetRealNameAuthenticationCallback(
        () => { Debug.Log($"用户完成了实名认证"); });
}
```

## TT.AuthenticateRealName
[小游戏对应接口描述](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/user-information/info/authenticate-real-name)

> 注意：
> 该模块对应 [旧版Unity SDK文档中的 【实名认证】 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#b6cfe935)

> 6.0.0 开始支持本方法，WebGL支持该方法
拉起实名认证窗口。
注意：调用该接口前请确保用户已登录。

| 前提条件 | 调用该接口前请确保用户已登录。 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 当前用户是否已经实名认证可以通过 [tt.getUserInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/info/tt-get-user-info) 查询 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void AuthenticateRealName(
    TTAccount.OnAuthenticateRealNameSuccessCallback successCallback,
    TTAccount.OnAuthenticateRealNameFailedCallback failedCallback)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| successCallback | delegate void OnAuthenticateRealNameSuccessCallback(string errMsg) | -- | 是 | 实名认证窗口拉起成功回调 |
| failedCallback | delegate void OnAuthenticateRealNameFailedCallback(string errMsg) | -- | 是 | 实名认证窗口拉起失败回调 |

### 代码示例

```csharp
private void Test() {
    TT.AuthenticateRealName(
        (errMsg) => { Debug.Log($"TestAuthenticateRealName success: {errMsg}"); },
        (errMsg) => { Debug.Log($"TestAuthenticateRealName fail: {errMsg}"); });
}
```

## TT.ShowDouyinOpenAuth
[小游戏对应接口描述](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/user-information/authorization/tt-show-douyin-open-auth)

> 注意：
> 该模块对应 [旧版Unity SDK文档中的 【抖音专用开放能力授权】 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#2a663800)

> 6.0.0 开始支持本方法，WebGL支持该方法
提供小游戏获取抖音权限的能力，展示出抖音权限授权弹窗。
在使用接口前，需要小游戏拥有者登录抖音开发平台申请开通小游戏需要的权限。

| 前提条件 | 在使用在接口前，需要小游戏拥有者登录抖音开放平台申请开通小游戏需要的权限。 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 该接口只支持抖音，所以请在抖音 APP 中调用； |
| 注意事项 | 每次申请授权都是该小游戏的抖音权限全量授权，请在传入 scopes 时，把需要的授权的 scopes 都传入。由于不支持增量授权，即使用户已经授权过部分抖音权限，也还是需要全量传入所有需要的权限； 每次申请授权的抖音权限必须是在抖音开放平台已经**申请并且审批开通**的权限，否则会导致本次授权操作失败； 此处授权是抖音相关的授权，如果想要申请小游戏授权，请查看 [tt.authorize](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/open-capacity/user-information/authorization/tt-authorize)。这两处授权的 scopes 范围不同； 在请求服务端接口时，**应用唯一标识** 在小游戏场景下，对应的是小游戏 appId；**应用唯一标识对应的密钥**对应的是小游戏的 APP Secret。 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void ShowDouyinOpenAuth(Dictionary<string, DouyinPermissionScopeStatus> scopes,
    TTAccount.OnShowDouyinOpenAuthSuccessCallback successCallback,
    TTAccount.OnShowDouyinOpenAuthFailedCallback failedCallback)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| scopes | Dictionary<string, DouyinPermissionScopeStatus> | -- | 是 | 需要获取权限的信息，其中 key 值是申请权限的 scope，value 值必须是 0，1，2（此处申请的权限在抖音开放平台必须是**已开通**状态） |
| successCallback | delegate void OnShowDouyinOpenAuthSuccessCallback(string errMsg, string ticket, string[] grantPermissions) | -- | 是 | 展示抖音权限授权弹窗成功回调 |
| failedCallback | delegate void OnShowDouyinOpenAuthFailedCallback(int errNo, string errMsg) | -- | 是 | 展示抖音权限授权弹窗失败回调 |

**DouyinPermissionScopeStatus **枚举如下：

| **枚举名** | **枚举值** | **说明 ** |
| --- | --- | --- |
| **Required** | 0 | 必选项（用户无法取消） |
| **OptionalSelected** | 1 | 非必选，默认选中 |
| **OptionalUnselected** | 2 | 非必选，默认不选中 |

**OnShowDouyinOpenAuthSuccessCallback **参数如下：

| **属性名 ** | **类型 ** | **说明 ** |
| --- | --- | --- |
| errMsg | string | 回调信息 |
| ticket | string | 请求授权返回的票据，此处对标开放平台的 authCode |
| grantPermissions | string[] | 用户授权的权限 |

**OnShowDouyinOpenAuthFailedCallback **参数如下：

| **属性名 ** | **类型 ** | **说明 ** |
| --- | --- | --- |
| errNo | string | 错误码 |
| errMsg | string | 错误信息 |

### 代码示例

```csharp
private void Test() {
    TT.ShowDouyinOpenAuth(new Dictionary<string, DouyinPermissionScopeStatus>()
        {
            {"im", DouyinPermissionScopeStatus.Required},
            {"im.media", DouyinPermissionScopeStatus.OptionalUnselected}, // todo: input
        },
        (errMsg, ticket, grantPermissions) =>
        {
            Debug.Log($"TestShowDouyinOpenAuth success. errMsg: {errMsg}, ticket: {ticket}, grantPermissions: {grantPermissions}");
        },
        (errNo, errMsg) =>
        {
            Debug.Log($"TestShowDouyinOpenAuth fail: {errNo} {errMsg}");
        });
}
```
