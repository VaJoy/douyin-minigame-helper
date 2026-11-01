---
title: "键盘处理器"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/ui/keyboard-processor
update_time: 2024-10-29
---

键盘模块，仅 webgl 支持。

> 注意：
> 该模块对应 [键盘处理](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#76989268)

## TT.OnKeyboardInput
> 6.0.0 开始支持本方法，仅 webgl 支持
监听键盘输入事件。

| 前提条件 | Unity WebGL 小游戏 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static TTKeyboard.OnKeyboardInputEvent OnKeyboardInput
```

### **参数说明 **
无。
### 代码示例

```csharp
public void TestKeyboard()
{
    TT.OnKeyboardInput -= OnKeyboardInput;
    TT.OnKeyboardInput += OnKeyboardInput;
}

private void OnKeyboardInput(string value)
{
    Debug.Log($"OnKeyboardInput: {value}");
}
```

## TT.OnKeyboardConfirm
> 6.0.0 开始支持本方法，仅 webgl 支持
监听用户点击键盘确定按钮时的事件。

| 前提条件 | Unity WebGL 小游戏 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static TTKeyboard.OnKeyboardConfirmEvent OnKeyboardConfirm
```

### **参数说明 **
无。
### 代码示例

```csharp
public void TestKeyboard()
{
    TT.OnKeyboardConfirm -= OnKeyboardConfirm;
    TT.OnKeyboardConfirm += OnKeyboardConfirm;
}

private void OnKeyboardConfirm(string value)
{
    Debug.Log($"OnKeyboardConfirm: {value}");
}
```

## TT.OnKeyboardComplete
> 6.0.0 开始支持本方法，仅 webgl 支持
监听键盘收起事件。

| 前提条件 | Unity WebGL 小游戏 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static TTKeyboard.OnKeyboardCompleteEvent OnKeyboardComplete
```

### **参数说明 **
无。
### 代码示例

```csharp
public void TestKeyboard()
{
    TT.OnKeyboardComplete -= OnKeyboardComplete;
    TT.OnKeyboardComplete += OnKeyboardComplete;
}

private void OnKeyboardComplete(string value)
{
    Debug.Log($"OnKeyboardComplete: {value}");
}
```

## TT.ShowKeyboard
> 6.0.0 开始支持本方法，仅 webgl 支持
展示键盘。

| 前提条件 | Unity WebGL 小游戏 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void ShowKeyboard(TTKeyboard.ShowKeyboardOptions options = null,
        Action onSuccess = null, Action<string> onError = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| options | TTKeyboard.ShowKeyboardOptions | null | 否 | 显示键盘的参数 |
| onSuccess | Action | null | 否 | 成功回调 |
| onError | Action<string> | null | 否 | 失败回调 |

### 代码示例

```csharp
public void TestKeyboard()
{
    TT.ShowKeyboard(new TTKeyboard.ShowKeyboardOptions(){
        maxLength = maxInputLength,
        multiple = multiple,
        defaultValue = _inputField.text,
        confirmType = confirmType
    }, () => { 
        Debug.Log("show keyboard succeed"); 
    }, errMsg => { 
        Debug.LogError($"show keyboard failed, error: {errMsg}"); 
    });
}
```

## TT.HideKeyboard
> 6.0.0 开始支持本方法，仅 webgl 支持
收起键盘。

| 前提条件 | Unity WebGL 小游戏 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void HideKeyboard(Action onSuccess = null, 
    Action<string> onError = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| onSuccess | Action | null | 否 | 成功回调 |
| onError | Action<string> | null | 否 | 失败回调 |

### 代码示例

```csharp
public void TestKeyboard()
{
    TT.HideKeyboard(() => { 
        Debug.Log("hide keyboard success");
    }, errMsg => { 
        Debug.LogError($"hide keyboard failed: {errMsg}"); 
    });
}
```

## TT.UpdateKeyboard
> 6.0.0 开始支持本方法，仅 webgl 支持
更新键盘，只有当键盘处于拉起状态时才会产生效果。

| 前提条件 | Unity WebGL 小游戏 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void UpdateKeyboard(string value, 
    Action onSuccess = null,
    Action<string> onError = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| value | string | -- | 是 | 键盘输入框的当前值 |
| onSuccess | Action | null | 否 | 成功回调 |
| onError | Action<string> | null | 否 | 失败回调 |

### 代码示例

```csharp
public void TestKeyboard()
{
    TT.UpdateKeyboard("xxxx",() => { 
        Debug.Log("hide keyboard success"); 
    }, errMsg => { 
        Debug.LogError($"hide keyboard failed: {errMsg}"); 
    });
}
```
