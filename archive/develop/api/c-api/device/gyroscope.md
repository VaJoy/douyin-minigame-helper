---
title: "陀螺仪"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/device/gyroscope
update_time: 2025-06-11
---

## TT.StartGyroscope
> 6.0.0 开始支持本方法，WebGL也支持该方法
开始监听陀螺仪。
### **语法 **

```csharp
public static void StartGyroscope(double interval = 50, Action<bool, string> statusCallback = null)
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| interval | double | 50 | 否 | 获取陀螺仪数据的间隔时间，单位为毫秒（ms），默认大小为50 |
| statusCallback | Action<bool, string> | null | 否 | 接口调用状态回调，(bool success, string errMsg) => {} |

### 代码示例

```csharp
void Test() {
    TT.StartGyroscope(50,
        (success, errMsg) => { Debug.Log($"success = {success}, errMsg = {errMsg}"); });
}
```

## TT.StopGyroscope
> 6.0.0 开始支持本方法，WebGL也支持该方法
停止监听陀螺仪。
### **语法 **

```csharp
public void StopGyroscope(Action<bool, string> statusCallback = null)
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| statusCallback | Action<bool, string> | null | 否 | 接口调用状态回调，(bool success, string errMsg) => {} |

### 代码示例

```csharp
void Test() {
    TT.StopGyroscope(
        (success, errMsg) => { Debug.Log($"success = {success}, errMsg = {errMsg}"); }
        );
}
```

## TT.OnGyroscopeChange
> 6.0.0 开始支持本方法，WebGL也支持该方法
陀螺仪回调。
### **语法 **

```csharp
public delegate void OnGyroscopeChanged(
    double x, 
    double y, 
    double z,
    double t, 
    double roll, 
    double pitch, 
    double yaw, 
    double result);
public OnGyroscopeChanged OnGyroscopeChangedHandler;
```

### 返回值

| 属性名 | **类型** | **说明** |
| --- | --- | --- |
| x | double | x 轴的角速度。 |
| y | double | y 轴的角速度。 |
| z | double | z 轴的角速度。 |
| t | double | 从设备启动到现在经过的时间戳，单位是 ms。 |
| roll | double | 姿态角值，围绕 Z 轴旋转，也叫翻滚角。 |
| pitch | double | 姿态角值，围绕 X 轴旋转，也叫做俯仰角。 |
| yaw | double | 姿态角值，围绕 Y 轴旋转，也叫偏航角。 |
| result | double | 数据是否有效的标志，当值为-1 时表示当前值无效。 |

### 代码示例

```csharp
private void Test() {
    TT.OnGyroscopeChange += GyroscopeChanged;
}

private void GyroscopeChanged(double x, double y, double z, double t, double roll, double pitch, double yaw, double result)
{
     Debug.Log(
            $"x = {x}, y = {y}, z = {z}, t = {t}, roll = {roll}, pitch = {pitch}, yaw = {yaw}, result = {result}");
};
```
