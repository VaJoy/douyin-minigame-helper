---
title: "TTFileSystemManager.ReadDirSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/file/tt-file-system-manager/tt-filesystem-read-dir
update_time: 2025-03-04
---

> TTSDK 6.2.5 及以后版本支持该能力。
同步读取目录内文件列表。

| **前提条件** | 无 |
| --- | --- |
| **业务背景** | 无 |
| **使用限制** | 无 |
| **注意事项** | •文件路径通过 Application.persistentDataPath 拼接。 • Native 方案下效果与 Directory.GetFiles 一致。 |
| **相关教程** | 无 |

## 语法

```csharp
public string[] ReadDirSync(string dirPath)
```

## 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| dirPath | string | 无 | 是 | 要读取的目录路径 |

## 返回值

| 类型 | 说明 |
| --- | --- |
| string[] | 指定目录下的文件名数组 |

### 回调失败
TTReadDirResponse 类型，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "readDir:fail " + 详细错误信息 |

## 错误码
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-readdir-sync)
## 代码示例

```csharp
var dirPath = Application.persistentDataPath;
var fileList = TT.GetFileSystemManager().ReadDirSync(dirPath);
if (fileList != null)
{
    Debug.Log($"ReadDirSync file {dirPath} succeed!, {string.Join(",",fileList.ToList())}");
}
else
{
    Debug.Log($"ReadDirSync file is empty or has error");
}
```
