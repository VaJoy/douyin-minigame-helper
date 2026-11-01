---
title: "获取小游戏启动参数"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/system/game-launch-params
update_time: 2024-10-12
---

该模块包含了获取小程序启动时的参数的接口。

> 注意：
> 该接口对应 [旧版Unity SDK文档中的【启动参数】](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#e939bf70)

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 里面的参数可能为空，使用时需判空 |
| 注意事项 | 可以在TT.InitSDK之后调用，确保得到非空值 |
| 相关教程 | 无 |

## TT.GetLaunchOptionsSync
> 6.0.0 开始支持本方法
获取小程序启动时的参数。
### **语法 **

```csharp
public static LaunchOption GetLaunchOptionsSync();
```

### **返回值说明 **

| 类型 | 说明 |
| --- | --- |
| LaunchOption | 小程序启动时的参数 |

### 代码示例

```csharp
void Read_LaunchOption()
{
    Debug.Log("LaunchOption: ");
    if (TT.s_ContainerEnv != null)
    {
        TTSDK.LaunchOption launchOption = TT.GetLaunchOptionsSync();
        Debug.Log("path :" + launchOption.Path);
        Debug.Log("scene :" + launchOption.Scene);
        Debug.Log("subScene :" + launchOption.SubScene);
        Debug.Log("group_id :" + launchOption.GroupId);
        Debug.Log("shareTicket :" + launchOption.ShareTicket);
        Debug.Log("is_sticky :" + launchOption.IsSticky);
        Debug.Log("query :");
        if (launchOption.Query != null)
        {
            foreach (KeyValuePair<string, string> kv in launchOption.Query)
                if (kv.Value != null)
                    Debug.Log(kv.Key + ": " + kv.Value);
                else
                    Debug.Log(kv.Key + ": " + "null ");
        }

        Debug.Log("refererInfo :");
        if (launchOption.RefererInfo != null)
        {
            foreach (KeyValuePair<string, string> kv in launchOption.RefererInfo)
                if (kv.Value != null)
                    Debug.Log(kv.Key + ": " + kv.Value);
                else
                    Debug.Log(kv.Key + ": " + "null ");
        }

        Debug.Log("extra :");
        if (launchOption.Extra != null)
        {
            foreach (KeyValuePair<string, string> kv in launchOption.Extra)
                if (kv.Value != null)
                    Debug.Log(kv.Key + ": " + kv.Value);
                else
                    Debug.Log(kv.Key + ": " + "null ");
        }
    }
}
```

##
