---
title: "TTFileSystemManager.AppendFile"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/file/tt-file-system-manager/tt-file-system-append
update_time: 2025-03-04
---

> TTSDK 6.2.5 及以后版本支持该能力。
在文件结尾追加内容，文件不存在时会新建。

| **前提条件** | 无 |
| --- | --- |
| **业务背景** | 无 |
| **使用限制** | 无 |
| **注意事项** | •文件路径通过 Application.persistentDataPath 拼接。 •目前 Native 方案下效果与 File.AppendAllText 一致，有复杂需求推荐自己实现。 |
| **相关教程** | 无 |

## 语法

```csharp
TTFileSystemManager.AppendFile(AppendFileParam param)

TTFileSystemManager.AppendFile(AppendFileStringParam param)
```

## 参数说明
param 为 AppendFileParam 类型，属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| FilePath | string | 无 | 是 | 要追加写入的文件路径 |
| Data | byte[] | 无 | 是 | 要追加写入的二进制数据 |

有一重载方法， 为追加字符串。主要区别是 param 类型不同，为 AppendFileStringParam，属性如下

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| FilePath | string | 无 | 是 | 要追加写入的文件路径 |
| Data | string | 无 | 是 | 要追加写入的数据要追加写入的二进制数据 |
| Encoding | string | utf8 | 否 | 指定写入文件的字符编码 |

## 回调成功
TTBaseResponse 类型，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "appendFile:ok" |

### 回调失败
TTBaseResponse 类型，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "appendFile:fail " + 详细错误信息 |

## 错误码
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-append)
## 代码示例

```csharp
var path = Path.Combine(Application.persistentDataPath, srcPathInput.text);
var binData = Encoding.UTF8.GetBytes("test");
TT.GetFileSystemManager().AppendFile(new AppendFileParam
{
    FilePath = path,
    Data = binData,
    success = (_) =>
    {
        Debug.Log(
            $"append file to {srcPathInput.text} succeed, data length: {binData.Length}");
    },
    fail = (rsp) =>
    {
        Debug.Log($"append file fail, errCode: {rsp.errCode}, errMsg: {rsp.errMsg}");
    }
});

TT.GetFileSystemManager().AppendFile(new AppendFileStringParam()
{
    FilePath = path,
    Data = "test",
    Encoding = "utf8",
    success = (_) =>
    {
        Debug.Log($"append to {srcPathInput.text} succeed");
    },
    fail = (rsp) =>
    {
        Debug.Log($"Append binary to file fail, errCode: {rsp.errCode}, errMsg: {rsp.errMsg}");
    }
});
```
