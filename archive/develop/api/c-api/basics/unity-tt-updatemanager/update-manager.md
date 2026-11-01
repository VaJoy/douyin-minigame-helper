---
title: "TT.GetUpdateManager"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/basics/unity-tt-updatemanager/update-manager
update_time: 2024-11-05
---

> TTSDK 6.0.8开始支持本方法，这是一个同步方法。
获取全局唯一的版本更新管理器，用于管理小游戏更新。小游戏发布新版本后不是立即生效，在个别情况会比较慢。如果想做到立即更新，可以接入该主动更新的能力。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 在有新版本的情况下，小游戏运行中任意时候单独使用 applyUpdate 即可立即重启游戏。但建议在 onUpdateReady 中给用户提示确认后进行重启。 |
| 相关教程 | 无 |

## 语法

```csharp
TT.GetUpdateManager()
```

## 参数说明
无
## 返回值
全局唯一的TTUpdateManger对象。
