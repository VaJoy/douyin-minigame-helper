---
title: "方向监听"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/device/device-motion
update_time: 2024-10-15
---

## StartDeviceMotionListening
> 6.0.0 开始支持本方法，WebGL也支持该方法
开始监听设备方向变化。
### **语法 **

```csharp
public static void StartDeviceMotionListening(
    TTDeviceMotion.Interval interval = TTDeviceMotion.Interval.normal,
    TTDeviceMotion.MotionCallback callback = null)
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| interval | Interval | Interval.**normal** | 否 | "监听设备方向的变化回调函数的执行频率,game 适用于更新游戏的回调频率，在 20ms/次 左右,ui 适用于更新 UI 的回调频率，在 60ms/次 左右,normal 普通的回调频率，在 200ms/次 左右" |
| callback | MotionCallback | null | 否 | 监听回调函数类 |

**interval 的合法值：**

| 值 | 说明 |
| --- | --- |
| normal | 普通的回调频率：约200ms/次 |
| game | 适用于更新UI的回调频率：约60ms/次 |
| ui | 适用于更新游戏的回调频率：约20ms/次 |

**MotionCallback 包含函数：**

| 值 | 类型 | 说明 |
| --- | --- | --- |
| OnSuccess | void OnSuccessDelegate() | 监听成功 |
| OnFailed | OnFailedDelegate(int code, string msg) | 监听失败 |
| OnComplete | OnCompleteDelegate() | 监听完成 |

### 代码示例

```csharp
private void Test() {
    TT.StartDeviceMotionListening(Interval.normal,  new TTDeviceMotion.MotionCallback()
    {
        OnComplete = ()=>
        {
            Debug.Log("StartDeviceMotionListening OnComplete");          
        },
        OnSuccess = () =>
        {
            Debug.Log("StartDeviceMotionListening OnSuccess");               
        },
        OnFailed = (code, msg) =>
        {
            Debug.Log($"StartDeviceMotionListening OnFailed, errorCode:{code}, errorMsg:{msg}");                      
        }
    });
}
```

## StopDeviceMotionListening
> 6.0.0 开始支持本方法，WebGL也支持该方法
停止监听设备方向变化。
### **语法 **

```csharp
public static void StopDeviceMotionListening(
    TTDeviceMotion.MotionCallback callback = null
)
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| callback | MotionCallback | null | 否 | 监听回调函数类 |

### 代码示例

```csharp
private void Test() {
    TT.StopDeviceMotionListening();
}
```

## OnDeviceMotionChange
> 6.0.0 开始支持本方法，WebGL也支持该方法
监听设备方向变化事件，数据变化及回调的频率根据 TT.StartDeviceMotionListening 的 interval 参数决定。
### **语法 **

```csharp
public static TTDeviceMotion.OnDeviceMotionChangeEvent OnDeviceMotionChange;
```

### 代码示例

```csharp
private void AddListener()
{
    TT.OnDeviceMotionChange += OnDeviceMotionChange;
}

private void RemoveListener()
{
    TT.OnDeviceMotionChange -= OnDeviceMotionChange;
}

private void OnDeviceMotionChange(double alpha, double beta, double gamma)
{
    Debug.Log($"OnDeviceMotionChange alpha ->{alpha},beta ->{beta},gamma->{gamma}");
}
```
