---
title: "加速度计"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/device/jerkmeter
update_time: 2024-10-12
---

## TT.StartAccelerometer
> 6.0.0 开始支持本方法，WebGL也支持该方法
开始监听加速度数据。
### **语法 **

```csharp
public static void StartAccelerometer(
    OnAccelerometerChanged onAccelerometerChanged,
    Action<bool, string> statusCallback = null)
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| onAccelerometerChanged | delegate void OnAccelerometerChanged(double x, double y, double z) | -- | 是 | 加速度数据回调事件监听 |
| statusCallback | Action<bool, string> | null | 否 | 接口调用状态回调，(bool success, string errMsg) => {} |

### 代码示例

```csharp
// 根据加速度速度对方块进行旋转的示例
class TestClass 
{
    private TTExampleCube _exampleCube;
    void Test() {
        TT.StartAccelerometer((x, y, z) =>
        {
            var text = $"x: {x}\ny: {y}\nz: {z}";
            Debug.Log(text);
            if (acceleration != Vector3.zero)
            {
                float dx = (float)(x - acceleration.x) * 100;
                float dy = (float)(y - acceleration.y) * 100;
                float dz = (float)(z - acceleration.z) * 100;
                _exampleCube?.Rotate(dx, dy, dz);
            }
        
            acceleration.x = (float)x;
            acceleration.y = (float)y;
            acceleration.z = (float)z;
        }, (success, errMsg) =>
        {
            if (success)
            {
                acceleration = Vector3.zero;
                if (_exampleCube == null)
                {
                    var gameObject = new GameObject();
                    _exampleCube = gameObject.AddComponent<TTExampleCube>();
                }
                else
                {
                    _exampleCube.Reset();
                    _exampleCube.Show();
                }
            }
        
            Debug.Log(errMsg);
        });
    }
}

public class TTExampleCube : MonoBehaviour
{
    private GameObject _cube;

    void Awake()
    {
        _cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
        Reset();
    }

    public void Reset()
    {
        if (_cube != null)
        {
            _cube.transform.position = new Vector3(0, 1f, 0.0f);
            _cube.transform.localScale = new Vector3(1.5f, 1.5f, 1.5f);
            _cube.transform.rotation = Quaternion.identity;
        }
    }

    public void Rotate(float xAngle = 1, float yAngle = 1, float zAngle = 1)
    {
        _cube?.transform?.Rotate(xAngle, yAngle, zAngle, Space.Self);
    }

    public void Show()
    {
        _cube?.SetActive(true);
    }
    
    public void Hide()
    {
        _cube?.SetActive(false);
    }
}
```

## TT.StopAccelerometer
> 6.0.0 开始支持本方法，WebGL也支持该方法
停止监听加速度数据。
### **语法 **

```csharp
public static void StopAccelerometer(Action<bool, string> statusCallback = null)
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| statusCallback | Action<bool, string> | null | 否 | 接口调用状态回调，(bool success, string errMsg) => {} |

### 代码示例

```csharp
private void Test(){
    TT.StopAccelerometer((success, errMsg) => { Debug.Log(errMsg); });
}
```
