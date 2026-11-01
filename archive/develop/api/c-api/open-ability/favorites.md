---
title: "收藏"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/open-ability/favorites
update_time: 2025-04-17
---

## TT.ShowFavoriteGuide
[小游戏对应接口描述](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/collect/favorite/tt-show-favorite-guide)

> 注意：
> 该模块对应 [旧版Unity SDK文档中的 【显示收藏引导】 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#5d1f52c5)

> 6.0.0 开始支持本方法，WebGL也支持该方法
收藏引导。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 展现策略仅在线上版、审核版有效，测试版、预览版不受限制。 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static void ShowFavoriteGuide(
    TTFavorite.Style style = TTFavorite.Style.BottomBar,
    string content = "")
```

### 参数说明

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| style | Style | Style.BottomBar | 否 | 弹窗类型，默认为底部弹窗。 |
| content | string | "" | 否 | 弹窗文案，仅style为 Tip 时可修改，最多显示 12 个字符。 |

Style 包含 3 种类型：

| 类型 | 说明 |
| --- | --- |
| TopBar | 顶部弹窗 |
| BottomBar | 底部弹窗 |
| Tip | 顶部气泡 |

### 代码示例

```csharp
private void Test() {
    TT.ShowFavoriteGuide(TTFavorite.Style.TopBar);
    TT.ShowFavoriteGuide(TTFavorite.Style.Tip, "测试文案测试文案测试文案测试文案测试文案测试文案");
}
```

## TT.ShowRevisitGuide
[小游戏对应接口描述](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/open-capacity/collect/favorite/tt-show-revisit-guide)

> 注意：
> 该模块对应 [旧版Unity SDK文档中的 【复访能力】 ](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#d4555049)

> 6.0.0 开始支持本方法，WebGL也支持该方法
调起引导用户复访的提示弹窗，目前仅抖音宿主支持。
为了更好的玩家体验，建议在按钮的点击回调中使用。
### **语法 **

```csharp
public static void ShowRevisitGuide(Action<bool> callback)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| callback | Action<bool> | -- | 是 | 调起复访提示回调，true表示成功，false表示失败 |

### 代码示例

```csharp
private void Test() {
    TT.ShowRevisitGuide((res) => Debug.Log($"ShowRevisitGuide result: {res}"));
}
```

public static bool IsCollected()

private void Test() {
bool isCollected = TT.IsCollected();
Debug.("IsGameFavorite: " + isCollected);
}

public static void Collect(Action<bool> callback)

private void Test() {
TT.CancelCollection(
success => { Debug.Log("CancelCollection - success: " + success); }
);
}

private void Test() {
TT.Collect(
success => { Debug.Log("Collect - success: " + success); }
);
}

public static void CancelCollection(Action<bool> callback)
