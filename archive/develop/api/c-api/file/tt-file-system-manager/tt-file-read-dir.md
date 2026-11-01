---
title: "TTFileSystemManage.ReadDir"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/file/tt-file-system-manager/tt-file-read-dir
update_time: 2025-03-04
---

> TTSDK 6.2.5 及以后版本支持该能力。
读取目录内文件列表。

| **前提条件** | 无 |
| --- | --- |
| **业务背景** | 无 |
| **使用限制** | 无 |
| **注意事项** | 文件路径通过 Application.persistentDataPath 拼接。  Native 方案下效果与 Directory.GetFiles 一致。 |
| **相关教程** | 无 |

## 语法

```csharp
public void ReadDir(ReadDirParam param)
```

## 参数说明
param 为 ReadDirParam 类型，属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| DirPath | string | 无 | 是 | 要读取的目录路径 |

## 回调成功
TTReadDirResponse 类型，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "readDir:ok" |
| files | string[] | 指定目录下的文件名数组 |

### 回调失败
TTReadDirResponse 类型，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "readDir:fail " + 详细错误信息 |

## 错误码
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-readdir)
## 代码示例

```csharp
var dirPath = Application.persistentDataPath;
TT.GetFileSystemManager().ReadDir(new ReadDirParam
{
    DirPath = dirPath,
    success = (rsp) =>
    {
        Debug.Log($"ReadDir file {dirPath} succeed!, {string.Join(",",rsp.files.ToList())}");
    },
    fail = (rsp) =>
    {
        Debug.Log($"ReadDir file {dirPath} error!, {rsp.errMsg}");
    }
});
```
