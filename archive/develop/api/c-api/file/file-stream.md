---
title: "文件流式读写"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/file/file-stream
update_time: 2025-07-01
---

> TTSDK 6.3.9 及以后版本支持该能力。iOS 抖音v3470 版本后开始支持，Android 无版本限制。
增加文件流的相关能力。

| **前提条件** | 无 |
| --- | --- |
| **业务背景** | 无 |
| **使用限制** | 无 |
| **注意事项** | •文件路径通过 Application.persistentDataPath 拼接。 •目前 Native 方案下实现为System.IO.FileStream，有复杂需求推荐自己实现。 |
| **相关教程** | 无 |

## TTFileSystemManager.Open
异步打开一个文件流，回调中获取文件的标识符，文件系统可以根据此标识符对文件流进行操作。
### 语法

```csharp
void TTFileSystemManager.Open(OpenParam param);
```

### 参数说明
param 为 OpenParam 类型，有效属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| filePath | string | 无 | 是 | 文件路径。 |
| flag | string | 无 | 是 | 文件系统标志。 |
| success | Action<TTOpenResponse> | 无 | 否 | 接口调用成功回调。 |
| fail | Action<TTOpenResponse> | 无 | 否 | 接口调用失败回调。 |

#### flag 的合法值
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/filesystemmanager-open#%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E)
#### 回调成功
TTOpenResponse 类型，有效属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| fd | string | 文件系统标志，用于操作文件流。 |

#### 回调失败
TTOpenResponse 类型，有效属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errCode | int | 错误码。 |
| errMsg | string | 详细错误信息。 |

##### 错误码
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/filesystemmanager-open#%E9%94%99%E8%AF%AF%E7%A0%81)
### 代码示例

```csharp
TT.GetFileSystemManager().Open(new(){
    filePath = Path.Combine(Application.persistentDataPath, "test.txt"),
    flag = "a+",
    success = (res) => {PrintLog($"Open Success, fd:{res.fd}");},
    fail = (res) => PrintLog($"Open Fail, errCode: {res.errCode}, errMsg: {res.errMsg}")
});
```

## TTFileSystemManager.OpenSync
同步打开一个文件流，返回文件的标识符，文件系统可以根据此标识符对文件流进行操作。
### 语法

```csharp
string TTFileSystemManager.OpenSync(OpenSyncParam param);
```

### 参数说明
param 为 OpenSyncParam 类型，有效属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| filePath | string | 无 | 是 | 文件路径。 |
| flag | string | 无 | 是 | 文件系统标志。 |

#### flag 的合法值
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/filesystem-opensync#%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E)
#### 返回值

| **类型** | **说明** |
| --- | --- |
| string | 文件的标识符。 |

### 代码示例

```csharp
var fd = TT.GetFileSystemManager().OpenSync(new() {
    filePath = Path.Combine(Application.persistentDataPath, "test.txt"),
    flag = "a+"
});
```

## TTFileSystemManager.Close
异步关闭一个文件流。
### 语法

```csharp
void TTFileSystemManager.Close(CloseParam param);
```

### 参数说明
param 为 CloseParam 类型，有效属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| fd | string | 无 | 是 | 文件标识符，通过Open/OpenSync获取。 |
| success | Action<TTOpenResponse> | 无 | 否 | 接口调用成功回调。 |
| fail | Action<TTOpenResponse> | 无 | 否 | 接口调用失败回调。 |

#### 回调成功
TTBaseResponse 类型，有效属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errCode | int | 0。 |
| errMsg | string | 空字符串。 |

#### 回调失败
TTBaseResponse 类型，有效属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errCode | int | 错误码。 |
| errMsg | string | 详细错误信息。 |

##### 错误码
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/filesystem-close#%E9%94%99%E8%AF%AF%E7%A0%81)
### 代码示例

```csharp
string fd;

TT.GetFileSystemManager().Open(new(){
    filePath = Path.Combine(Application.persistentDataPath, "test.txt"),
    flag = "a+",
    success = (res) => {fd = res.fd;}
});

TT.GetFileSystemManager().Close(new(){
    fd = fd,
    success = (_) => {
        PrintLog($"Close Success, fd:{fd}");
    },
    fail = (res) => PrintLog($"Close Fail, errCode: {res.errCode}, errMsg: {res.errMsg}")
});
```

## TTFileSystemManager.CloseSync
同步关闭一个文件流。
### 语法

```csharp
void TTFileSystemManager.CloseSync(CloseSyncParam param);
```

### 参数说明
param 为 CloseSyncParam 类型，有效属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| fd | string | 无 | 是 | 文件标识符，通过Open/OpenSync获取。 |

#### 返回值
无。
### 代码示例

```csharp
var fd = TT.GetFileSystemManager().OpenSync(new() {
    filePath = Path.Combine(Application.persistentDataPath, "test.txt"),
    flag = "a+"
});

TT.GetFileSystemManager().CloseSync(new()
{
    fd = fd
});
```

## TTFileSystemManager.Write
异步写文件。
### 语法

```csharp
void TTFileSystemManager.Write(WriteBinParam param);

void TTFileSystemManager.Write(WriteStringParam param);
```

### 参数说明
param 为 WriteBinParam 类型时，有效属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| fd | string | 无 | 是 | 文件标识符，通过Open/OpenSync获取。 |
| data | byte[] | 无 | 是 | 要写入的二进制数据。 |
| offset | int | 0 | 否 | data中要被写入的位置。 |
| length | int | data.Length - offset | 否 | 指定要写入的字节数。 |
| success | Action<TTWriteResponse> | 无 | 否 | 接口调用成功回调。 |
| fail | Action<TTWriteResponse> | 无 | 否 | 接口调用失败回调。 |

param 为 WriteStringParam 类型时，有效属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| fd | string | 无 | 是 | 文件标识符，通过Open/OpenSync获取。 |
| data | string | 无 | 是 | 要写入的字符串数据。 |
| encoding | string | 无 | 是 | 编码格式，如"utf-8"。 |
| success | Action<TTWriteResponse> | 无 | 否 | 接口调用成功回调。 |
| fail | Action<TTWriteResponse> | 无 | 否 | 接口调用失败回调。 |

#### 回调成功
TTWriteResponse 类型，有效属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| bytesWritten | int | 写入的字节数。 |

#### 回调失败
TTWriteResponse 类型，有效属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errCode | int | 错误码。 |
| errMsg | string | 详细错误信息。 |

##### 错误码
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/filesystem-write#%E9%94%99%E8%AF%AF%E7%A0%81)
### 代码示例

```csharp
string fd;
string content = "hello world!";
var binContent = Encoding.UTF8.GetBytes(content);

TT.GetFileSystemManager().Open(new(){
    filePath = Path.Combine(Application.persistentDataPath, "test.txt"),
    flag = "a+",
    success = (res) => {fd = res.fd;}
});

TT.GetFileSystemManager().Write(new WriteBinParam(){
    data = binContent,
    fd = fd,
    success = (res) => PrintLog($"Write Success, bytesWritten:{res.bytesWritten}"),
    fail = (res) => PrintLog($"Write Fail, errCode: {res.errCode}, errMsg: {res.errMsg}")
});

TT.GetFileSystemManager().Write(new WriteStringParam(){
    data = content,
    fd = fd,
    encoding = "utf-8",
    success = (res) => PrintLog($"Write Success, bytesWritten:{res.bytesWritten}"),
    fail = (res) => PrintLog($"Write Fail, errCode: {res.errCode}, errMsg: {res.errMsg}")
});
```

## TTFileSystemManager.WriteSync
同步写文件。
### 语法

```csharp
WriteResult TTFileSystemManager.WriteSync(WriteBinSyncParam param);

WriteResult TTFileSystemManager.WriteSync(WriteStringSyncParam param);
```

### 参数说明
param 为 WriteBinSyncParam 类型时，有效属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| fd | string | 无 | 是 | 文件标识符，通过Open/OpenSync获取。 |
| data | byte[] | 无 | 是 | 要写入的二进制数据。 |
| offset | int | 0 | 否 | data中要被写入的位置。 |
| length | int | data.Length - offset | 否 | 指定要写入的字节数。 |

param 为 WriteStringSyncParam 类型时，有效属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| fd | string | 无 | 是 | 文件标识符，通过Open/OpenSync获取。 |
| data | string | 无 | 是 | 要写入的字符串数据。 |
| encoding | string | 无 | 是 | 编码格式，如"utf-8"。 |

#### 返回值
WriteResult 类型，有效属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| bytesWritten | int | 写入的字节数。 |

### 代码示例

```csharp
string fd;
string content = "hello world!";
var binContent = Encoding.UTF8.GetBytes(content);

TT.GetFileSystemManager().Open(new(){
    filePath = Path.Combine(Application.persistentDataPath, "test.txt"),
    flag = "a+",
    success = (res) => {fd = res.fd;}
});

TT.GetFileSystemManager().WriteSync(new WriteBinSyncParam(){
    data = binContent,
    fd = fd,
});

TT.GetFileSystemManager().WriteSync(new WriteStringSyncParam(){
    data = content,
    fd = fd,
    encoding = "utf-8"
});
```

## TTFileSystemManager.Read
异步读文件。
### 语法

```csharp
void TTFileSystemManager.Read(ReadParam param);
```

### 参数说明
param 为 ReadParam 类型，有效属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| fd | string | 无 | 是 | 文件标识符，通过Open/OpenSync获取。 |
| arrayBuffer | byte[] | 无 | 是 | 存放数据的缓冲区。 |
| offset | int | 0 | 否 | 缓冲区中的写入偏移量。 |
| length | int | arrayBuffer.Length - offset | 否 | 要从文件中写入的字节数。 |
| success | Action<TTReadResponse> | 无 | 否 | 接口调用成功回调。 |
| fail | Action<TTReadResponse> | 无 | 否 | 接口调用失败回调。 |

#### 回调成功
TTReadResponse 类型，有效属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| bytesRead | int | 写入的字节数。 |
| arrayBuffer | byte[] | 读取的缓冲区对象。 |

#### 回调失败
TTReadResponse 类型，有效属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errCode | int | 错误码。 |
| errMsg | string | 详细错误信息。 |

##### 错误码
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/filesystem-read#%E9%94%99%E8%AF%AF%E7%A0%81)
### 代码示例

```csharp
string fd;

TT.GetFileSystemManager().Open(new(){
    filePath = Path.Combine(Application.persistentDataPath, "test.txt"),
    flag = "r",
    success = (res) => {fd = res.fd;}
});

TT.GetFileSystemManager().Read(new ReadParam()
{
    fd = fd,
    arrayBuffer = new byte[24],
    success = (res) => PrintLog($"Read Success, bytesRead: {res.bytesRead}, contentLength: {res.arrayBuffer.Length}"),
    fail = (res) => PrintLog($"Read Fail, errCode: {res.errCode}, errMsg: {res.errMsg}")
});
```

## TTFileSystemManager.ReadSync
同步读文件。
### 语法

```csharp
ReadResult TTFileSystemManager.ReadSync(ReadSyncParam param);
```

### 参数说明
param 为 ReadSyncParam 类型，有效属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| fd | string | 无 | 是 | 文件标识符，通过Open/OpenSync获取。 |
| arrayBuffer | byte[] | 无 | 是 | 存放数据的缓冲区。 |
| offset | int | 0 | 否 | 缓冲区中的写入偏移量。 |
| length | int | data.Length - offset | 否 | 要从文件中写入的字节数。 |

#### 返回值
ReadResult 类型，有效属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| bytesRead | int | 写入的字节数。 |
| arrayBuffer | byte[] | 读取的缓冲区对象。 |

### 代码示例

```csharp
string fd;

TT.GetFileSystemManager().Open(new(){
    filePath = Path.Combine(Application.persistentDataPath, "test.txt"),
    flag = "r",
    success = (res) => {fd = res.fd;}
});

var result = TT.GetFileSystemManager().ReadSync(new ReadSyncParam()
{
    fd = fd,
    arrayBuffer = new byte[24]
});
```

## TTFileSystemManager.ReadCompressedFile
异步读取压缩文件。
### 语法

```csharp
void TTFileSystemManager.ReadCompressedFile(ReadCompressedFileParam param);
```

### 参数说明
param 为 ReadCompressedFileParam 类型，有效属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| filePath | string | 无 | 是 | 文件路径。 |
| compressionAlgorithm | string | 无 | 是 | 压缩算法，目前仅支持"br"。 |
| success | Action<TTReadCompressedFileResponse> | 无 | 否 | 接口调用成功回调。 |
| fail | Action<TTReadCompressedFileResponse> | 无 | 否 | 接口调用失败回调。 |

#### 回调成功
TTReadCompressedFileResponse 类型，有效属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| arrayBuffer | byte[] | 文件内容。 |

#### 回调失败
TTReadResponse 类型，有效属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errCode | int | 错误码。 |
| errMsg | string | 详细错误信息。 |

##### 错误码
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/filesystem-read-compressed-file#%E9%94%99%E8%AF%AF%E7%A0%81)
### 代码示例

```csharp
TT.GetFileSystemManager().ReadCompressedFile(new(){
    filePath = Path.Combine(Application.persistentDataPath, "test.br"),
    compressionAlgorithm = "br",
    success = (res) => PrintLog($"ReadCompressedFile Success, bytesRead: {res.arrayBuffer.Length}"),
    fail = (res) => PrintLog($"ReadCompressedFile Fail, errCode: {res.errCode}, errMsg: {res.errMsg}")
});
```

## TTFileSystemManager.ReadCompressedFileSync
同步读取压缩文件。
### 语法

```csharp
byte[] TTFileSystemManager.ReadCompressedFileSync(ReadCompressedFileSyncParam param);
```

### 参数说明
param 为 ReadCompressedFileSyncParam 类型，有效属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| filePath | string | 无 | 是 | 文件路径。 |
| arrayBuffer | byte[] | 无 | 是 | 存放数据的缓冲区。 |

#### 返回值

| **类型** | **说明** |
| --- | --- |
| byte[] | 文件内容。 |

### 代码示例

```csharp
var result = TT.GetFileSystemManager().ReadCompressedFileSync(new(){
    filePath = Path.Combine(Application.persistentDataPath, "test.br"),
    compressionAlgorithm = "br"
});
PrintLog($"ReadCompressedFile Success, bytesRead: {result.Length}");
```

## TTFileSystemManager.Fstat
异步获取文件信息。
### 语法

```csharp
void TTFileSystemManager.Fstat(FstatParam param);
```

### 参数说明
param 为 FstatParam 类型，有效属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| fd | string | 无 | 是 | 文件标识符，通过Open/OpenSync获取。 |
| success | Action<FstatResponse> | 无 | 否 | 接口调用成功回调。 |
| fail | Action<FstatResponse> | 无 | 否 | 接口调用失败回调。 |

#### 回调成功
FstatResponse 类型，有效属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| stats | [TTStatInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/file/file-system-manager#a62ad910) | 文件信息 |

#### 回调失败
FstatResponse 类型，有效属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errCode | int | 0。 |
| errMsg | string | 空字符串。 |

##### 错误码
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/filesystemmanager-fstat#%E9%94%99%E8%AF%AF%E7%A0%81)
### 代码示例

```csharp
string fd;

TT.GetFileSystemManager().Open(new(){
    filePath = Path.Combine(Application.persistentDataPath, "test.txt"),
    flag = "r",
    success = (res) => {fd = res.fd;}
});

TT.GetFileSystemManager().Fstat(new(){
    fd = fd,
    success = (res) => PrintLog($"Fstat Success, mode: {res.stats.mode}, size: {res.stats.size}, lastAccessedTime: {res.stats.lastAccessedTime}, lastModifiedTime: {res.stats.lastModifiedTime}"),
    fail = (res) => PrintLog($"Fstat Fail, errCode: {res.errCode}, errMsg: {res.errMsg}")
});
```

## TTFileSystemManager.FstatSync
同步获取文件信息。
### 语法

```csharp
TTStatInfo TTFileSystemManager.FstatSync(FstatSyncParam param);
```

### 参数说明
param 为 FstatSyncParam 类型，有效属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| fd | string | 无 | 是 | 文件标识符，通过Open/OpenSync获取。 |

#### 返回值

| **类型** | **说明** |
| --- | --- |
| [TTStatInfo](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/file/file-system-manager#a62ad910) | 文件信息。 |

### 代码示例

```csharp
string fd;

TT.GetFileSystemManager().Open(new(){
    filePath = Path.Combine(Application.persistentDataPath, "test.txt"),
    flag = "r",
    success = (res) => {fd = res.fd;}
});

var result = TT.GetFileSystemManager().FstatSync(new(){
    fd = fd
});
PrintLog($"Fstat Success, mode: {result.mode}, size: {result.size}, lastAccessedTime: {result.lastAccessedTime}, lastModifiedTime: {result.lastModifiedTime}");
            
```

## TTFileSystemManager.Ftruncate
异步截断文件。
### 语法

```csharp
void TTFileSystemManager.Ftruncate(FtruncateParam param);
```

### 参数说明
param 为 FtruncateParam 类型，有效属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| fd | string | 无 | 是 | 文件标识符，通过Open/OpenSync获取。 |
| length | int | 0 | 否 | 文件截断的长度。 |
| success | Action<TTBaseResponse> | 无 | 否 | 接口调用成功回调。 |
| fail | Action<TTBaseResponse> | 无 | 否 | 接口调用失败回调。 |

#### 回调成功
TTBaseResponse 类型，有效属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errCode | int | 0。 |
| errMsg | string | 空字符串。 |

#### 回调失败
TTBaseResponse 类型，有效属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errCode | int | 错误码。 |
| errMsg | string | 详细错误信息。 |

##### 错误码
[参照小游戏文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/file-system-manager/filesystemmanager-ftruncate#%E9%94%99%E8%AF%AF%E7%A0%81)
### 代码示例

```csharp
string fd;

TT.GetFileSystemManager().Open(new(){
    filePath = Path.Combine(Application.persistentDataPath, "test.txt"),
    flag = "r",
    success = (res) => {fd = res.fd;}
});

TT.GetFileSystemManager().Ftruncate(new(){
    fd = fd,
    length = 24,
    success = (_) => PrintLog($"Ftruncate Success"),
    fail = (res) => PrintLog($"Ftruncate Fail, errCode: {res.errCode}, errMsg: {res.errMsg}")
});
            
```

## TTFileSystemManager.FtruncateSync
同步截断文件。
### 语法

```csharp
void TTFileSystemManager.FtruncateSync(FtruncateSyncParam param);
```

### 参数说明
param 为 FtruncateSyncParam 类型，有效属性如下：

| **属性名** | **类型** | **默认值** | **必填** | **说明** |
| --- | --- | --- | --- | --- |
| fd | string | 无 | 是 | 文件标识符，通过Open/OpenSync获取。 |
| length | int | 0 | 否 | 文件截断的长度。 |

#### 返回值
无。
### 代码示例

```csharp
string fd;

TT.GetFileSystemManager().Open(new(){
    filePath = Path.Combine(Application.persistentDataPath, "test.txt"),
    flag = "r",
    success = (res) => {fd = res.fd;}
});

TT.GetFileSystemManager().FtruncateSync(new(){
    fd = fd,
    length = 24,
});
            
```
