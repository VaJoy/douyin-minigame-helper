---
title: "TTUpdateManager"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/basics/unity-tt-updatemanager/tt-update-manager
update_time: 2025-11-14
---

Unity 小游戏版本更新对象，TT.GetUpdateManager() 的返回值。
### 属性说明

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| OnCheckForUpdate | function | 版本信息请求完成的回调 |
| OnUpdateReady | function | 新版本下载成功的回调 |
| OnUpdateFailed | function | 新版本下载失败的回调 |
| ApplyUpdate | function | 应用新版本 |

## TTUpdateManager.OnCheckForUpdate
> TTSDK 6.0.8开始支持本方法
当向小游戏后台请求完新版本信息，会进行回调。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### 语法

```csharp
TT.GetUpdateManager().OnCheckForUpdate(OnCheckForUpdateCallback callback)
```

### 参数说明
**callback**

| 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- |
| delegate |  | 是 | 请求完新版本信息后，回调的函数 |

callback 是一个 delegate ，接受 `OnCheckForUpdateResult` 类型参数，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| HasUpdate | bool | 是否有新的版本 |

### 返回值
无
### 代码示例

```csharp
TT.GetUpdateManager().OnCheckForUpdate(data =>
{
    Debug.Log($"OnCheckForUpdate,hasUpdate-->{data.HasUpdate}");
});
```

## TTUpdateManager.OnUpdateReady
> TTSDK 6.0.8开始支持本方法
当新版本下载完成，会进行回调。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### 语法

```csharp
TT.GetUpdateManager().OnUpdateReady(OnUpdateReadyCallback callback)
```

### 参数说明
**callback**

| 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- |
| delegate |  | 是 | 当新版本下载完成后进行回调的函数 |

### 返回值
无
### 代码示例

```csharp
TT.GetUpdateManager().OnUpdateReady(() =>
{
    Debug.Log($"OnUpdateReady");
});
```

## TTUpdateManager.OnUpdateFailed
> TTSDK 6.0.8开始支持本方法
当新版本下载失败，会进行回调。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### 语法

```csharp
TT.GetUpdateManager().OnUpdateFailed(OnUpdateFailedCallback callback)
```

### 参数说明
**callback**

| 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- |
| delegate |  | 是 | 请求完新版本信息后，回调的函数 |

callback 是一个 delegate ，接受 `OnUpdateFailedResult` 类型参数，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| Err | string | 版本更新失败原因 |

### 返回值
无
### 代码示例

```csharp
TT.GetUpdateManager().OnUpdateFailed(data =>
{
    
    Debug.Log($"OnUpdateFailed-->{data.Err}");
});
```

## TTUpdateManager.ApplyUpdate
> TTSDK 6.0.8开始支持本方法
当新版本下载完成，调用该方法会强制当前小游戏应用上新版本并重启。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### 语法

```csharp
TT.GetUpdateManager().ApplyUpdate(ApplyUpdateParams applyUpdateParams)
```

### 参数说明
applyUpdateParams 为 `ApplyUpdateParams` 类型，属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| Success | delegate |  | 是 | 接口调用成功的回调函数，(不会必定回调) |
| Fail | delegate |  | 是 | 接口调用失败的回调函数 |
| Complete | delegate |  | 是 | 接口调用结束的回调函数（调用成功、失败都会执行） |

#### 回调成功
Success 是一个 delegate ，接受 `ApplyUpdateSuccessResult` 类型参数，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| ErrMsg | string |  |

#### 回调失败
Fail 是一个 delegate ，接受 `ApplyUpdateFailResult` 类型参数，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| ErrMsg | string |  |

### 返回值
无
### 代码示例

```csharp
var param = new ApplyUpdateParams
{
    Success = result =>
    {
        Debug.Log("ApplyUpdate success");
    },
    Fail = result =>
    {
        Debug.Log($"ApplyUpdate fail-->{result.ErrMsg}");
    },
    Complete = () =>
    {
        Debug.Log("ApplyUpdate complete");
    }
};
TT.GetUpdateManager().ApplyUpdate(param);
```
