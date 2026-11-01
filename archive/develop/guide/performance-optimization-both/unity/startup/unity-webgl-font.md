---
title: "Unity WebGL 抖音系统字体"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/performance-optimization-both/unity/startup/unity-webgl-font
update_time: 2026-01-29
---

游戏基本会使用中文，中文字体体积少则2～3M。
抖音小游戏平台，提供统一的中文字体，节省启动下载的资源量，该字体为所有unity游戏公用，开发者无需在包体内引入字体文件，即可使用中文。
常用汉字已经过测试，如发现有中文无法支持，请联系抖音平台进行支持。
另外也有可能存在字体无法获取的情况，需开发者做好兜底工作。

---

## 版本要求
仅用于Unity WebGL产物，不支持Android Native Unity产物，IDE环境暂不支持该API。
- 小游戏基础库 >= 3.30.0.0
- Android抖音客户端版本 >= 30.3.0
- iOS抖音客户端版本 >= 30.3.0

---

## 代码示例

```csharp
public Text text;
TT.GetSystemFont(font =>
{
    if (font != null)
    {
        text.font = font;
    } else {
        // system font 加载失败
    }
});
```

---

## 相关日志
- 如果加载字体失败，可以观察下列日志信息，提供给抖音平台侧排查。
  - `[system-font]:get system-font failed,code:******`
  - `load font data failed ******`
- 团结引擎需升级至1.8.1及以上版本，以支持此接口。
