---
title: "退出重启"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/system/quit-restart
update_time: 2024-10-12
---

## TT.ExitMiniProgram
> 6.0.0 开始支持本方法，WebGL也支持该方法

退出程序。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 调用该方法的预期表现会将小游戏切后台，并不会完全退出小游戏。 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void ExitMiniProgram(bool showDialog = false, Action<bool> callback = null)
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| showDialog | bool | false | 否 | 是否显示退出提示对话框，true为在退出前显示二次提示对话框架，false则不显示对话框而直接退出程序 |
| callback | Action<bool> | null | 否 | 接口调用成功状态回调，true表示成功，false表示失败 |

### 代码示例

```csharp
private void Test() {
    TT.ExitMiniProgram(true, 
        flag => {
            Debug.Log("退出" + flag);
        });
}
```

## TT.RestartMiniProgramSync

> 注意：
> 该模块对应 [旧版Unity SDK文档中的 【重启游戏】 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#82dd05d1)

> 6.0.0 开始支持本方法，WebGL也支持该方法
重启小游戏。
### **语法 **

```csharp
public static bool RestartMiniProgramSync()
```

### 参数说明
无参数。
## 返回值

| **类型** | **说明** |
| --- | --- |
| bool | 是否重启成功 |

### 代码示例

```csharp
private void Test() {
    if (!TT.RestartMiniProgramSync())
    {
        Debug.LogError("重启程序失败");
    }
}
```
