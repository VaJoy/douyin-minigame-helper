---
title: "初始化"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/init/init
update_time: 2024-10-12
---

> 注意：
> 该模块回调部分与旧版文档对应 [旧版Unity SDK文档 【初始化回调】](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/sc_stark_sdk#3238cab3)

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

## TT.InitSDK
> 6.0.0 开始支持本方法
Unity SDK 初始化函数。
### **语法 **

```csharp
public static int InitSDK(OnTTContainerInitCallback callback = null)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| callback | OnTTContainerInitCallback | null | 否 | 初始化完成的回调 |

### 错误码

| 错误码 | 说明 |
| --- | --- |
| 0 | 无错误 |
| 1 | TT Unity SDK 版本不支持 |
| 2 | Unity Engine 版本不被支持 |

### 代码示例

```csharp
void TestTTInitSDK()
{
    TT.InitSDK((code, env) =>
    {
        Debug.Log("Unity message init sdk callback");
        Debug.Log("Unity message code: " + code);
        Debug.Log("Unity message HostEnum: " + env.m_HostEnum);
    });

}
```

## TT.InContainerEnv
> 6.0.0 开始支持本方法
是否在 TT Container 真机环境下。
### 语法

```csharp
public static bool InContainerEnv;
```

### 代码示例

```csharp
void TestTTInContainerEnv()
{
    Debug.Log("是否在TT Container真机环境下：" + TT.InContainerEnv);
}
```

## OnTTContainerInitCallback
callback 变量为 OnTTContainerInitCallback 类型。

```csharp
public delegate void OnTTContainerInitCallback(int code, ContainerEnv env);
```

## ContainerEnv
OnTTContainerInitCallback 中的 env 为 ContainerEnv 类型，它包含一些变量和方法，说明如下：
### 变量说明

| 属性名 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| GameAppId | string | null | 游戏AppId |
| m_HostEnum | HostEnum | HostEnum.None | 运行的宿主 |
| m_LaunchFromEnum | LaunchFromEnum | LaunchFromEnum.UnKnown | 启动入口 |

### 方法语法

```csharp
public ContainerRuntime GetContainerRuntime();
public VersionType GetVersionType();
public string GetLaunchFromStr();
public IReadOnlyDictionary<string, string> GetQueryFromScheme();
public string GetLocation();
public string GetLaunchFrom();
public LaunchOption GetLaunchOptionsSync();
```

### 方法说明

| 属性名 | 返回值 | 说明 |
| --- | --- | --- |
| GetContainerRuntime | ContainerRuntime | 当前UC运行在哪个环境下 |
| GetVersionType | VersionType | 当前APK的版本类型 |
| GetLaunchFromStr | string | LaunchFromScene的字符串值 |
| GetQueryFromScheme | IReadOnlyDictionary<string, string> | 获取query字段，即小程序的启动参数，可能为空，使用时需判空 |
| GetLocation | string | 启动场景（该字段目前只有在「侧边栏」启动场景才会返回，返回的属性值为：homepage） |
| GetLaunchFrom | string | 启动场景（该字段目前只有在「侧边栏」启动场景才会返回，返回的属性值为：homepage） |
| GetLaunchOptionsSync | LaunchOption | 获取小程序启动时的参数，里面的参数可能为空，使用时需判空; 可以在TTSDK.init()之后调用，确保得到非空值 |

## HostEnum

```csharp
public enum HostEnum
{
    None = 0,
    Toutiao = 1,        // 头条
    Douyin = 2,         // 抖音
    ToutiaoLite = 3,    // 头条极速
    DouyinLite = 4,     // 抖音极速
    HuoShan = 5,        // 火山
    HuoShanLite = 6,    // 火山极速
    XiGua = 7,          // 西瓜视频
    Helo = 8,           // helo
    Tiktok = 9,         // Tiktok
    PiPiXia = 10,       // 皮皮虾
    MoMoYu = 11,        // 摸摸鱼
    DongCheDi = 12,     // 懂车帝
    Fanqie = 13         // 番茄小说
};
```

## LaunchFromEnum

```csharp
public enum LaunchFromEnum
{
    UnKnown = 0,
    Search = 1,         //搜索
    DeskTop = 2,        //桌面快捷方式
    MP_List = 3,        //列表项，包括历史，收藏，小程序盒子里的搜索等
    Scan = 4,           //扫码
    Share = 5,          //分享
    Video_Archor = 6,   //视频锚点
    Feed = 7,
    MiniApk = 8,        // 穿山甲miniapk拉起
};
```

## ContainerRuntime

```csharp
public enum ContainerRuntime
{
    Unity = 0,          // 当前UC运行在标准的Unity中
    Launcher = 1,       // 当前UC运行在Launcher Android 工程中
    Standard = 2        // UC运行在各大宿主，标准的UC环境中
}
```

## VersionType

```csharp
public enum VersionType
{
    None = 0,               // 默认值，如安装apk或者在editor模式下使用此值
    Perview = 1,            // 扫Preview二维码
    Test = 2,               // 扫Test二维码
    Release = 3,            // 正式环境
}
```

## LaunchOption
变量说明。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| Path | string | 冷启动页面的路径 |
| Query | Dictionary<string, string> | 冷启动页面的参数 |
| Scene | string | 启动场景值 |
| SubScene | string | 冷启动子场景值 |
| IsSticky | bool | 遗留字段 |
| ShareTicket | string | 群分享Ticket |
| GroupId | string | 视频锚点的groupId |
| Extra | Dictionary<string, string> | 抖音直播间特殊字段 |
| RefererInfo | Dictionary<string, string> | 小程序跳小程序的来源信息。从另一个小程序进入小程序时返回。否则返回 {}。 |
