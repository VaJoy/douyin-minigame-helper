---
title: "网络"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/device/network
update_time: 2024-12-23
---

## TT.GetNetworkType
> TTSDK 6.1.3 版本支持本方法。
获取设备当前所处的网络类型。
### 语法

```csharp
public static void GetNetWorkType(GetNetworkTypeParam param)
```

### 参数说明
GetNetworkTypeParam 类型主要包含以下参数信息：

| **属性名** | **类型** | **必填** | **说明** | **最低支持版本** |
| --- | --- | --- | --- | --- |
| Success | delegate void GetNetworkTypeSuccessCallback(GetNetworkSuccessResult result) | 否 | 接口调用成功的回调函数 | 6.1.3 |
| Fail | Action<ErrorInfo> | 否 | 接口调用失败的回调函数 | 6.1.3 |
| Complete | Action | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） | 6.1.3 |

**回调成功**
GetNetworkSuccessResult 类型，属性如下：

| **属性名** | **类型** | **说明** | **最低支持版本** |
| --- | --- | --- | --- |
| NetworkType | enum | 网络类型 | 6.1.3 |
| ErrMsg | string | "getNetworkType:ok" | 6.1.3 |

**NetworkType 的合法值：**

| **值** | **说明** | **最低支持版本** |
| --- | --- | --- |
| NetworkWifi | Wifi网络 | 6.1.3 |
| Network2G | 2G网络 | 6.1.3 |
| Network3G | 3G网络 | 6.1.3 |
| Network4G | 4G网络 | 6.1.3 |
| None | 无网络 | 6.1.3 |
| Unknown | *不常见的网路类型* | 6.1.3 |

### 代码示例

```csharp
var param = new GetNetworkTypeParam
{
    Success = result =>
    {
        PrintText($"GetNetworkType success, result -->{result.NetworkType}");
    },
    Fail = result =>
    {
        PrintText($"GetNetworkType fail, errCode -->{result.ErrorCode}, errMsg -->{result.ErrMsg}, errorType -->{result.ErrorType}");
    },
    Complete = () =>
    {
        PrintTextAppended("GetNetworkType complete");
    }
};
TT.GetNetWorkType(param);
```

## TT.OnNetworkStatusChange
> TTSDK 6.1.3 版本支持本方法。
添加网络状态变化事件的监听函数。
### 语法

```csharp
public static void OnNetworkStatusChange(OnNetworkStatusChangeCallback callback)
```

### 参数说明
**callback**

| **类型** | **必填** | **说明** | **最低支持版本** |
| --- | --- | --- | --- |
| OnNetworkStatusChangeResult | 否 | 网络状态变化的事件回调 | 6.1.3 |

OnNetworkStatusChangeResult 属性如下：

| **属性名** | **类型** | **说明** | **最低支持版本** |
| --- | --- | --- | --- |
| NetworkType | enum | 网络类型（同GetNetworkType中参数说明） | 6.1.3 |
| IsConnected | bool | 是否有网络连接 | 6.1.3 |

### 代码示例

```csharp
private void NetworkStatusChange(OnNetworkStatusChangeResult result)
{
    Debug.Log($"OnNetworkStatusChange, networkType ->{result.NetworkType}, isConnected -->{result.IsConnected}");
}
TT.OnNetworkStatusChange(NetworkStatusChange);
```

## TT.OffNetworkStatusChange
> TTSDK 6.1.3 版本支持本方法。
监听弱网状态变化事件。
### 语法

```csharp
public static void OffNetworkStatusChange(OnNetworkStatusChangeCallback callback = null)
```

### 参数说明
**callback**
不传 callback 参数时，会移除所有监听函数

| **类型** | **必填** | **说明** | **最低支持版本** |
| --- | --- | --- | --- |
| OnNetworkStatusChangeResult | 否 | 网络状态变化的事件回调 | 6.1.3 |

### 代码示例

```csharp
TT.OffNetworkStatusChange();
```

## TT.OnNetworkWeakChange
> TTSDK 6.1.3 版本支持本方法。
添加弱网状态变化事件的监听函数。
### 语法

```csharp
public static void OnNetworkWeakChange(OnNetworkWeakChangeCallback callback)
```

### 参数说明
**callback**

| **类型** | **必填** | **说明** | **最低支持版本** |
| --- | --- | --- | --- |
| OnNetworkWeakChangeResult | 否 | 弱网状态变化的事件回调 | 6.1.3 |

OnNetworkWeakChangeResult 属性如下：

| **属性名** | **类型** | **说明** | **最低支持版本** |
| --- | --- | --- | --- |
| NetworkType | enum | 网络类型（同GetNetworkType中参数说明） | 6.1.3 |
| WeakNet | bool | 是否弱网 | 6.1.3 |

### 代码示例

```csharp
private void NetworkWeakChange(OnNetworkWeakChangeResult result)
{
    Debug.Log($"OnNetworkWeakChange, networkType ->{result.NetworkType}, WeakNet -->{result.WeakNet}");
}
TT.OnNetworkWeakChange(NetworkWeakChange);
```

## TT.OffNetworkWeakChange
> TTSDK 6.1.3 版本支持本方法。
移除弱网状态变化事件的监听函数。
### 语法

```csharp
public static void OffNetworkWeakChange(OnNetworkWeakChangeCallback callback = null)
```

### 参数说明
**callback**
不传 callback 参数时，会移除所有监听函数

| **类型** | **必填** | **说明** | **最低支持版本** |
| --- | --- | --- | --- |
| OnNetworkWeakChangeResult | 否 | 弱网状态变化的事件回调 | 6.1.3 |

### 代码示例

```csharp
TT.OffNetworkWeakChange();
```
