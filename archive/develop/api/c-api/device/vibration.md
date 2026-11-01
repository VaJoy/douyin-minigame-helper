---
title: "震动"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/device/vibration
update_time: 2025-07-25
---

## TT.VibrateShort
使手机发生较短时间的振动。Android震动时间为 30ms，iOS 震动时间为 15ms。
### 语法

```csharp
public static void VibrateShort(VibrateShortParam param)
```

### 参数说明
VibrateShortParam包含属性如下：

| 属性名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| Success | VibrateShortSuccessCallback | 是 | 接口调用成功的回调函数 |
| Fail | Action<ErrorInfo> | 否 | 接口调用失败的回调函数 |
| Complete | Action | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

### 回调成功
Success 包含 VibrateShortSuccessCallback，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| ErrMsg | string | "vibrateShort:ok" |

### 回调失败
ErrorInfo属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| ErrorCode | int | 错误码 |
| ErrMsg | string | 错误信息 |

[错误码信息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/shake/tt-vibrate-short)
### 代码示例

```csharp
public void TestNewVibrateShort()
{
    TT.VibrateShort(new VibrateShortParam()
    {
        Success = (res) => 
        {
            Debug.Log("TT.VibrateShort Success");
        },
        Fail = (errInfo) =>
        {
            Debug.Log($"TT.VibrateShort Fail, {errInfo.ToString()}");
        },
        Complete = () =>
        {
            Debug.Log("TT.VibrateShort Complete");
        }
    });
}
```

## TT.VibrateLong
使手机发生较长时间的振动（400 ms)。
### 语法

```csharp
public static void VibrateLong(VibrateLongParam param)
```

### 参数说明
VibrateLongParam包含属性如下：

| 属性名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| Success | VibrateLongSuccessCallback | 是 | 接口调用成功的回调函数 |
| Fail | Action<ErrorInfo> | 否 | 接口调用失败的回调函数 |
| Complete | Action | 否 | 接口调用结束的回调函数（调用成功、失败都会执行） |

### 回调成功
Success 包含 VibrateLongSuccessCallback，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| ErrMsg | string | "vibrateLong:ok" |

### 回调失败
ErrorInfo属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| ErrorCode | int | 错误码 |
| ErrMsg | string | 错误信息 |

[错误码信息](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/device/shake/tt-vibrate-long)
### 代码示例

```csharp
public void TestNewVibrateLong()
{
    TT.VibrateLong(new VibrateLongParam()
    {
        Success = (res) => 
        {
            Debug.Log("TT.VibrateLong Success");
        },
        Fail = (errInfo) =>
        {
            Debug.Log($"TT.VibrateLong Fail, {errInfo.ToString()}");
        },
        Complete = () =>
        {
            Debug.Log("TT.VibrateLong Complete");
        }
    });
}
```

## TT.Vibrate

> **说明**
> 推荐长震动使用TT.VibrateLong，短震动使用TT.VibrateShort。

> 6.0.0 开始支持本方法，WebGL也支持该方法
以配置震动周期的手机震动接口，单位 ms 。

> 注意：WebGL 平台下，只有两种震动：长和短。
> pattern 数组参数只能传入一个数值，传入数值小于 1000 则为短震动，否则为长震动。
> 不支持取消和重复。即repeat参数无效。
>     当收不到长震动时，可以检查是否在 IOS 开启静音模式了。静音模式下，长震动会被禁。

### **语法 **

```csharp
public static void Vibrate(long[] pattern, int repeat = -1)
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| pattern | long[] | -- | 是 | 震动周期 like long[] pattern = {0, 100, 1000, 3000}; 传入null则取消震动 |
| repeat | int | -1 | 否 | 重复次数，为-1则不重复 |

### 代码示例

```csharp
private void TestVibrate()
{
    long[] pattern = { 0, 100, 1000, 300 };
    TT.Vibrate(pattern);
}

private void TestVibrateShort()
{
    long[] pattern = { 400 };
    TT.Vibrate(pattern);
}
```
