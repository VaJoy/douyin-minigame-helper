---
title: "游戏生命周期"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/system/game-lifecycle
update_time: 2025-04-15
---

> 注意：
> 该模块对应 [生命周期](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#197e4955)

## TT.GetAppLifeCycle
> 6.0.0 开始支持本方法
获取游戏生命周期实例。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static TTAppLifeCycle GetAppLifeCycle()

// 获取游戏生命周期实例，返回的 TTAppLifeCycle 可以监听如下周期：

// 监听游戏到前台，统一所有平台，携带参数的格式为字典，可以根据指定key获取指定数据
public event OnShowEventWithDict OnShow;
// 监听游戏切到后台，统一所有平台
public event OnAppHideEvent OnHide;
```

### 代码示例

```csharp
public void TestAppLifeCycle()
{
    TT.GetAppLifeCycle().OnShow += OnAppShow;
    
    TT.GetAppLifeCycle().OnHide += OnAppHide;
}

private void OnAppShow(Dictionary<string, object> param)
{
    Debug.Log("OnAppShow");
}

private void OnAppHide()
{
    Debug.Log("OnAppHide");
}
```

## TT.SetOnBeforeExitAppListener
> 6.0.0 开始支持本方法
监听游戏退出。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void SetOnBeforeExitAppListener(Func<bool> onBeforeExitApp)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| onBeforeExitApp | Func<bool> | -- | 是 | 返回值为true，则表示由开发者自行处理退出逻辑，可以调用 TT.ExitMiniProgram 来手动退出游戏。返回值为false，则默认退出游戏 |

### 代码示例

```csharp
public void TestAppLifeCycle()
{
   TT.SetOnBeforeExitAppListener(OnBeforeExit);
}

private bool OnBeforeExit()
{
    Debug.Log("OnBeforeExit");
    TT.ExitMiniProgram(true);
    return true;
}
```
