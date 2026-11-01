---
title: "TTFileSystemManager.AppendFileSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/file/tt-file-system-manager/tt-filesystem-append-sync
update_time: 2025-03-04
---

> TTSDK 6.2.5 及以后版本支持该能力。
在文件结尾追加内容，文件不存在时会新建。

| **前提条件** | 无 |
| --- | --- |
| **业务背景** | 无 |
| **使用限制** | 无 |
| **注意事项** | 文件路径通过 Application.persistentDataPath 拼接。 目前 Native 方案下效果与 File.AppendAllText 一致，有复杂需求推荐自己实现。 |
| **相关教程** | 无 |

## 语法

```csharp
public string AppendFileSync(string filePath, byte[] data);

public string AppendFileSync(string filePath, string data, string encoding = "utf8")
```

## 参数说明

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| filePath | string | 无 | 是 | 要追加写入的文件路径 |
| data | byte[] | 无 | 是 | 要追加写入的二进制数据 |

有一重载方法， 为追加字符串

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| filePath | string | 无 | 是 | 要追加写入的文件路径 |
| data | string | 无 | 是 | 要追加写入的数据要追加写入的二进制数据 |
| encoding | string | utf8 | 否 | 指定写入文件的字符编码 |

## 返回值

| **类型** | **说明** |
| --- | --- |
| string | 为空则表示写入成功，否则为失败，并带上失败信息 |

## 错误码
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-append)
## 代码示例

```csharp
var text = "test";
var binData = Encoding.UTF8.GetBytes(text);
var path = Path.Combine(Application.persistentDataPath, srcPathInput.text);
var errMsg = "";

errMsg = TT.GetFileSystemManager().AppendFileSync(path, binData);

errMsg = TT.GetFileSystemManager()
        .AppendFileSync(path, text, "utf8");
*
*if (string.IsNullOrEmpty(errMsg))
{
    Debug.Log($"append file to {srcPathInput.text} succeed, data length: {binData.Length}");
}
else
{
    Debug.Log("AppendFileSync", errMsg);
}
```
