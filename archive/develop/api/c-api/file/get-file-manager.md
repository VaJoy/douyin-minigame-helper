---
title: "获取文件管理器"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/file/get-file-manager
update_time: 2024-10-12
---

## TT.GetFileSystemManager
> 6.0.0 开始支持本方法，WebGL也支持该方法
获取全局唯一的文件管理器。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 小游戏支持 200M 的本地文件空间存储。  小游戏的本地空间储存逻辑上为以 appid 为纬度，不区分预览版，正式版。 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static TTFileSystemManager GetFileSystemManager();
```

### 返回值

| 类型 | 说明 |
| --- | --- |
| object | 文件管理器， TTFileSystemManager类型 |

### 代码示例
【代码实例 1 】：

```csharp
public void TestFileSystem()
{
    var fileSystemManager = TT.GetFileSystemManager();
}
```

【代码实例 2 】：
访问 包目录不需要填写前缀，例如读取包内 app.js 文件。

```csharp
public void TestFileSystem()
{
    var fileSystemManager = TT.GetFileSystemManager();
    fileSystemManager.ReadFile(new ReadFileParam
    {
        filePath = "app.js",
        encoding = "utf8",
        success = (rsp) =>
        {
            // app.js 文件内容
            Debug.Log(rsp.stringData)
        },
        fail = (rsp) =>
        {
            Debug.LogError($"读取失败 {rsp.errMsg}");
        },
    });
}
```
