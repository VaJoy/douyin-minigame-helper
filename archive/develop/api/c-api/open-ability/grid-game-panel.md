---
title: "游戏互推组件"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/grid-game-panel
update_time: 2024-12-30
---

游戏互推组件能力。

> 注意：
> 该模块对应  [游戏互推组件](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#1d5f9542) 。

## TT.CreateGridGamePanel
> 6.0.0 开始支持本方法
创建游戏推荐组件实例。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 目前仅支持抖音、抖音极速版 |
| 注意事项 | 本接口是同步接口，传入参数不合法时会直接抛出参数错误的异常，请做好处理 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static TTGridGamePanelManager.TTGridGamePanel CreateGridGamePanel(
    TTGridGamePanelManager.GridGamePanelCount gridCount, 
    JsonData query,
    TTGridGamePanelManager.GridGamePanelSize size, 
    JsonData position)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| gridCount | TTGridGamePanelManager.GridGamePanelCount | -- | 是 | 表示游戏推荐组件的格子数量 |
| query | JsonData | -- | 是 | 从组件内打开游戏时附带的 query 信息 |
| size | TTGridGamePanelManager.GridGamePanelSize | -- | 是 | 表示组件大小，large：100%，medium：90%，small：80%。仅 gridCount = one \| four 时有效 |
| position | JsonData | -- | 是 | 控制游戏推荐组件的展示位置，不传入时默认展示在屏幕右下角。 仅 gridCount = one 时有效 |

#### 返回说明

| 类型 | 默认值 | 说明 |
| --- | --- | --- |
| TTGridGamePanel | null | 表示游戏推荐组件实例 |

### 代码示例

```csharp
public void TestGridGame()
{
    
    var query = new JsonData
    {
        ["testKey"] = "testValue"
    };
    
    var position = new JsonData
    {
        ["top"] = 100,
        ["left"] = 100
    };

    TTGridGamePanelManager.TTGridGamePanel _gridGamePanel = TT.CreateGridGamePanel(
        TTGridGamePanelManager.GridGamePanelCount.One,
        query,
        TTGridGamePanelManager.GridGamePanelSize.Medium,
        position);
    
    _gridGamePanel?.Show();
    
    _gridGamePanel?.Hide();
    
    _gridGamePanel?.Destroy();

}
```

## TTGridGamePanel
游戏互推组件能力。

### TTGridGamePanel.Show
> 6.0.0 开始支持本方法
显示游戏推荐组件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 目前仅支持抖音、抖音极速版 |
| 注意事项 | 本接口是同步接口，传入参数不合法时会直接抛出参数错误的异常，请做好处理 |
| 相关教程 | 无 |

#### **语法 **

```csharp
public void Show();
```

#### 代码示例

```csharp
public void TestGridGame()
{
    
    var query = new JsonData
    {
        ["testKey"] = "testValue"
    };
    
    var position = new JsonData
    {
        ["top"] = 100,
        ["left"] = 100
    };

    TTGridGamePanelManager.TTGridGamePanel _gridGamePanel = TT.CreateGridGamePanel(
        TTGridGamePanelManager.GridGamePanelCount.One,
        query,
        TTGridGamePanelManager.GridGamePanelSize.Medium,
        position);
    });
    
    _gridGamePanel?.Show();
}
```

### TTGridGamePanel.Hide
> 6.0.0 开始支持本方法
隐藏游戏推荐组件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 目前仅支持抖音、抖音极速版 |
| 注意事项 | 本接口是同步接口，传入参数不合法时会直接抛出参数错误的异常，请做好处理 |
| 相关教程 | 无 |

#### **语法 **

```csharp
public void Hide();
```

#### 代码示例

```csharp
public void TestGridGame()
{
    
    var query = new JsonData
    {
        ["testKey"] = "testValue"
    };
    
    var position = new JsonData
    {
        ["top"] = 100,
        ["left"] = 100
    };

    TTGridGamePanelManager.TTGridGamePanel _gridGamePanel = TT.CreateGridGamePanel(
        TTGridGamePanelManager.GridGamePanelCount.One,
        query,
        TTGridGamePanelManager.GridGamePanelSize.Medium,
        position);
    });
    
    _gridGamePanel?.Hide();
}
```

### TTGridGamePanel.Destroy
> 6.0.0 开始支持本方法
销毁游戏推荐组件。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 目前仅支持抖音、抖音极速版 |
| 注意事项 | 本接口是同步接口，传入参数不合法时会直接抛出参数错误的异常，请做好处理 |
| 相关教程 | 无 |

#### **语法 **

```csharp
public abstract void Destroy();
```

#### 代码示例

```csharp
public void TestGridGame()
{
    
    var query = new JsonData
    {
        ["testKey"] = "testValue"
    };
    
    var position = new JsonData
    {
        ["top"] = 100,
        ["left"] = 100
    };

    TTGridGamePanelManager.TTGridGamePanel _gridGamePanel = TT.CreateGridGamePanel(
        TTGridGamePanelManager.GridGamePanelCount.One,
        query,
        TTGridGamePanelManager.GridGamePanelSize.Medium,
        position);
    });
    
    _gridGamePanel?.Destroy();

}
```
