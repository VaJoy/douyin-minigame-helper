---
title: "TTFileSystemManager.TruncateSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/file/tt-file-system-manager/tt-filesystem-truncate-sync
update_time: 2025-03-04
---

> TTSDK 6.2.5 及以后版本支持该能力。
在文件结尾追加内容，文件不存在时会新建。

| **前提条件** | 无 |
| --- | --- |
| **业务背景** | 无 |
| **使用限制** | 无 |
| **注意事项** | •文件路径通过 Application.persistentDataPath 拼接。 •目前 Native 方案下效果与 FileStream setLength 一致，有复杂需求推荐自己实现。 |
| **相关教程** | 无 |

## 语法

```csharp
public string TruncateSync(string filePath, int length);
```

## 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| filePath | string | 无 | 是 | 要截断的文件路径 |
| length | int | 无 | 是 | 截断的长度 |

## 返回值

| 类型 | 说明 |
| --- | --- |
| string | "truncate:ok" |

## 错误码
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-truncate-sync)
## 代码示例

```csharp
var filePath = Path.Combine(Application.persistentDataPath, "test.txt");
var errMsg = TT.GetFileSystemManager().TruncateSync(filePath, (int)(rsp.stat.size/2));
if (string.IsNullOrEmpty(errMsg))
{
    Debug.Log($"truncate file {srcPathInput.text} succeed!");
}
else
{
    Debug.Log("truncate", errMsg);
}
```
