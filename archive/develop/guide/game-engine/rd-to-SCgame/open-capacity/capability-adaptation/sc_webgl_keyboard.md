---
title: "键盘输入法适配"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/capability-adaptation/sc_webgl_keyboard
update_time: 2025-10-14
---

> 此文档描述小游戏开发时输入法适配问题。
> 更多详情见 [Unity WebGL 抖音小游戏适配方案](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/open-capacity/sc_webgl_overall)

## 自动适配
在 Unity 小游戏环境的 WebGL 方案中，**支持 Unity 2022 及以上版本 Input Field 组件自动适配键盘输入法**，无需手动调用。低版本或其他组件暂不支持。

## 低版本兼容
WebGL 方案中 Unity 2021 及以下版本无法正常唤起输入法。我们提供了 TTKeyboard 模块以及`OnKeyboardInput`、`OnKeyboardConfirm`与`OnKeyboardComplete`等事件，开发者可以通过`ShowKeyboard`、`HideKeyboard`等方法来显示键盘输入法。

### **使用示例**

```csharp
using TTSDK;
using UnityEngine;
using UnityEngine.UI;

public class TTKeyboardTest : MonoBehaviour
{
    public InputField input1;

    private void Start()
    {
        SetInputTexts();
        RegisterKeyboardEvents();
    }

    private void SetInputTexts()
    {
        input1.text = "done";
        InitClickableInputField(input1, false);
    }

    private void InitClickableInputField(InputField inputField, bool multiple)
    {
        var comp = inputField.GetComponent<TTClickableInputField>();
        if (comp == null)
        {
            comp = inputField.gameObject.AddComponent<TTClickableInputField>();
        }

        comp.multiple = multiple;
        comp.confirmType = inputField.text;
    }

    private void OnDestroy()
    {
        UnregisterKeyboardEvents();
    }

    private void RegisterKeyboardEvents()
    {
        TT.OnKeyboardInput += OnKeyboardInput;
        TT.OnKeyboardConfirm += OnKeyboardConfirm;
        TT.OnKeyboardComplete += OnKeyboardComplete;

        input1.onValueChanged.AddListener(OnUnityKeyboardValueChanged);
        input1.onEndEdit.AddListener(OnUnityKeyboardOnEndEdit);
    }

    private void UnregisterKeyboardEvents()
    {
        TT.OnKeyboardInput -= OnKeyboardInput;
        TT.OnKeyboardConfirm -= OnKeyboardConfirm;
        TT.OnKeyboardComplete -= OnKeyboardComplete;

        input1.onValueChanged.RemoveListener(OnUnityKeyboardValueChanged);
        input1.onEndEdit.RemoveListener(OnUnityKeyboardOnEndEdit);
    }

    private void OnHideKeyboardButtonClicked()
    {
        TT.HideKeyboard(() => { Debug.Log("hide keyboard success"); },
            errMsg => { Debug.LogError($"hide keyboard failed: {errMsg}"); });
    }

    private void OnKeyboardInput(string value)
    {
        Debug.Log($"[StarkKeyboard] OnKeyboardInput: {value}");
        if (input1.isFocused)
        {
            input1.text = value;
        }
    }

    private void OnKeyboardConfirm(string value)
    {
        Debug.Log($"[StarkKeyboard] OnKeyboardConfirm: {value}");
    }

    private void OnKeyboardComplete(string value)
    {
        Debug.Log($"[StarkKeyboard] OnKeyboardComplete: {value}");
    }
    
    private void OnUnityKeyboardValueChanged(string value)
    {
        Debug.Log($"[Unity InputField] OnValueChanged: {value}");
    }
    
    private void OnUnityKeyboardOnEndEdit(string value)
    {
        Debug.Log($"[Unity InputField] OnEndEdit: {value}");
    }
}
```
