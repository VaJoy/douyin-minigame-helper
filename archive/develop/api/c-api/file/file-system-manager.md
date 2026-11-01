---
title: "文件管理器"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/file/file-system-manager
update_time: 2025-09-25
---

## TTFileSystemManager
> Native版本 6.0.0 开始支持，WebGL支持
文件管理器，TT.GetFileSystemManager 的返回值。

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| Access | Function | 判断文件/目录是否存在 |
| AccessSync | Function | 同步判断文件/目录是否存在 |
| GetSavedFileList | Function | 获取已保存的本地缓存文件列表 |
| CopyFile | Function | 复制文件 |
| CopyFileSync | Function | 同步复制文件 |
| Mkdir | Function | 创建目录 |
| MkdirSync | Function | 同步创建目录 |
| ReadFile | Function | 读取本地文件内容 |
| ReadFileSync | Function | 同步读取本地文件内容 |
| Rename | Function | 重命名文件，可以把文件从 oldPath 移动到 newPath |
| RenameSync | Function | 同步重命名文件，可以把文件从 oldPath 移动到 newPath |
| Rmdir | Function | 删除目录 |
| RmdirSync | Function | 同步删除目录 |
| Stat | Function | 获取文件 Stats 对象 |
| StatSync | Function | 同步获取文件 Stats 对象 |
| Unlink | Function | 删除文件 |
| UnlinkSync | Function | 同步删除文件 |
| WriteFile | Function | 写文件 |
| WriteFileSync | Function | 同步写文件 |
| GetLocalCachedPathForUrl | Function | 根据 url 链接获取本地缓存文件路径（仅 WebGL 平台可用） |
| IsUrlCached | Function | 判断该 url 是否有本地缓存文件（仅 WebGL 平台可用） |

## TTFileSystemManager.Access
> Native版本 6.0.0 开始支持，WebGL支持
判断文件/目录是否存在。

> 目前 Native 方案下效果与 File.Exists || Directory.Exists 一致，路径参数不应包含 scfile 协议头，请使用 Application.persistentDataPath 等原生接口。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | Access 可以用于 用户目录(scfile://user) 临时目录(scfile://temp) 以及 包内目录(访问包内目录不需要加额外协议头) |
| 相关教程 | 无 |

### **语法**

```csharp
public void Access(AccessParam options)
```

### 参数说明
options 为 AccessParam 类型，属性如下：

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| path | string | -- | 是 | 要判断是否存在的文件/目录路径 |
| success | Action<TTBaseResponse> | null | 否 | 接口调用成功的回调函数 |
| fail | Action<TTBaseResponse> | null | 否 | 接口调用失败的回调函数 |

### 回调成功
TTBaseResponse 类型，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "access:ok" |

### 回调失败
TTBaseResponse 类型，属性如下：

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "access:fail " + 详细错误信息 |

### 错误码

| errNo | errMsg | 说明 |
| --- | --- | --- |
| 20000 | access:fail path is invalid | path 参数错误 |
| 20001 | access:fail param should be xxx, but got xxx | 参数校验错误 |
| 21101 | access:fail permission denied, access {path_value} | 访问路径不可读 |
| 21102 | access:fail no such file or directory, access {path_value} | 访问文件不存在 |

### 代码示例
【代码示例 1 】判断临时目录路径是否存在。

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    var path = "scfile://temp/some-path"; // 判断的地址
    try {
        fileSystemManager.Access(new AccessParam
        {
            path = path,
            success = (rsp) =>
            {
                Debug.log(`${path} 地址存在`);
            },
            fail = (rsp) =>
            {
                Debug.log(`${path} 地址不存在或其他错误`, rsp.errMsg);
            },
        });
    }
}
```

【代码示例 2 】判断用户目录下路径是否存在。

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    var path = "scfile://user/some-path"; // 判断的地址
    try {
        fileSystemManager.Access(new AccessParam
        {
            path = path,
            success = (rsp) =>
            {
                Debug.log(`${path} 地址存在`);
            },
            fail = (rsp) =>
            {
                Debug.log(`${path} 地址不存在或其他错误`, res.errMsg);
            },
        });
    }
}
```

【代码示例 3 】判断包内路径是否存在。

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    // 包内路径不需要 `scfile://` 协议
    var path = "app.js";  // 判断的地址
    try {
        fileSystemManager.Access(new AccessParam
        {
            path = path,
            success = (rsp) =>
            {
                Debug.log(`${path} 地址存在`);
            },
            fail = (rsp) =>
            {
                Debug.log(`${path} 地址不存在或其他错误`, res.errMsg);
            },
        });
    }
}
```

## TTFileSystemManager.AccessSync
判断文件/目录是否存在。

> 目前 Native 方案下效果与 File.Exists || Directory.Exists 一致，路径不能使用 scfile 协议头，请使用 Application.persistentDataPath 等原生接口。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 小游戏支持 200M 的本地文件空间存储。  小游戏的本地空间储存逻辑上为以 appid 为维度，不区分预览版，正式版。 |
| 相关教程 | 无 |

### **语法**

```csharp
public bool FileSystemManager.AccessSync(string path)
```

### **参数说明 **
无。
### 返回值

| **类型** | **说明** |
| --- | --- |
| bool | 文件/目录是否存在 |

### 代码示例
【代码示例 1 】判断临时目录路径是否存在。

```csharp
private void Test() {
    var path = "scfile://temp/some-path"; // 判断的地址
    bool exist = TT.GetFileSystemManager().AccessSync(path);
    if (exist)
    {
        Debug.log(`${path} 地址存在`);
    }
    else
    {
        Debug.log(`${path} 地址不存在或其他错误`);
    }
}
```

【代码示例 2 】判断用户目录下路径是否存在。

```csharp
private void Test() {
    var path = "scfile://user/some-path"; // 判断的地址
    bool exist = TT.GetFileSystemManager().AccessSync(path);
    if (exist)
    {
        Debug.log(`${path} 地址存在`);
    }
    else
    {
        Debug.log(`${path} 地址不存在或其他错误`);
    }
}
```

【代码示例 3 】判断包内路径是否存在。

```csharp
private void Test() {
    // 包内路径不需要 `scfile://` 协议
    var path = "app.js"; // 判断的地址
    bool exist = TT.GetFileSystemManager().AccessSync(path);
    if (exist)
    {
        Debug.log(`${path} 地址存在`);
    }
    else
    {
        Debug.log(`${path} 地址不存在或其他错误`);
    }
}
```

## FileSystemManager.Stat
读取文件描述信息（同步）。

> 目前 Native 方案下效果与 IO.FileInfo(path) 一致，路径不能使用 scfile 协议头，请使用 Application.persistentDataPath 等原生接口。

### **语法**

```csharp
public void Stat(StatParam options)
```

### 参数说明
options 为 StatParam 类型，属性如下：

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| path | string | -- | 是 | 文件/目录路径 |
| success | function | null | 否 | 接口调用成功的回调函数 |
| fail | function | null | 否 | 接口调用失败的回调函数 |

### 回调成功
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| stats | TTStatInfo | *文件信息* |
| errMsg | string | "FileSystemManager.Stat:ok" |

### 回调失败
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| errNo | number | 错误码 |
| errMsg | string | "FileSystemManager.Stat:fail " + 详细错误信息 |

### 错误码

| **errNo** | **errMsg** | **说明** |
| --- | --- | --- |
| 20000 | stat:fail {param_name} is invalid | path 参数错误 |
| 20001 | stat:fail param should be xxx, but got xxx | 参数校验错误 |
| 21101 | stat:fail permission denied, stat {path_value} | 文件路径不可读 |
| 21102 | stat:fail no such file or directory, stat {path_value} | 文件不存在 |

### 代码示例

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    
    var filePath = "scfile://user/example.txt";
    
    fileSystemManager.Stat(new StatParam
      path = filePath,
      success(rsp) {
          var info = rsp.stat;
          Debug.Log($"{filePath} mode: {info.mode}, size: {info.size}, " +
             $"lastAccessedTime: {info.lastAccessedTime}, lastModifiedTime: {info.lastModifiedTime}, " +
             $"isFile: {info.IsFile()}, isDirectory: {info.IsDirectory()}");
      },
      fail(rsp) {
          Debug.Log("Stat fail: ", rsp.errMsg);
      }
    });
}
```

## FileSystemManager.StatSync
读取文件描述信息（同步）。

> 目前 Native 方案下效果与 IO.FileInfo(path) 一致，路径不能使用 scfile 协议头，请使用  Application.persistentDataPath 等原生接口。

### **语法**

```csharp
TTStatInfo StatSync(string path, bool throwException = false)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| path | string | -- | 是 | 文件/目录路径 |
| throwException | bool | false | 否 | 是否抛出错误信息，如果抛出错误信息，当文件不存在时则会抛出异常，错误信息从异常中获取。 |

### 返回值

| 类型 | 说明 |
| --- | --- |
| TTStatInfo | 返回文件信息，如果访问失败则返回null |

### 代码示例

```csharp
private void Test() {
    var filePath = "scfile://user/example.txt";
    
    try
    {
        var info = TT.GetFileSystemManager().StatSync(path, true);
        if (info != null)
        {
            Debug.Log($"{path} mode: {info.mode}, size: {info.size}, " +
                     $"lastAccessedTime: {info.lastAccessedTime}, lastModifiedTime: {info.lastModifiedTime}, " +
                     $"isFile: {info.IsFile()}, isDirectory: {info.IsDirectory()}");
        }
        else
        {
            Debug.LogError($"StatSync info is null");
        }
    }
    catch (Exception ex)
    {
        Debug.LogError($"StatSync failed, error: {ex}");
    }
}
```

## FileSystemManager.WriteFile
写文件，只能写入用户目录 (scfile://user)。

> 目前 Native 方案下效果与 File.WriteAllText 一致，路径不能使用 scfile 协议头，请使用  Application.persistentDataPath 等原生接口。

| **功能描述** | **接口类型** | **是否对外** | **字节专有** |
| --- | --- | --- | --- |
| 写文件，只能写入用户目录 (scfile://user) ，文件不存在时会新建文件 | 异步 | 是 | 否 |

### **语法**

```csharp
public void WriteFile(WriteFileParam options)
```

### 参数说明
options 为 WriteFileStringParam / WriteFileParam 类型，属性如下：

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| filePath | string | -- | 是 | 要写入的文件路径, 必须以 `scfile://user` 开头 |
| data | string / byte[] | -- | 是 | 要写入的文本或二进制数据 |
| encoding | string | utf8 | 否 | 指定写入文件的字符编码 |
| success | function | null | 否 | 接口调用成功的回调函数 |
| fail | function | null | 否 | 接口调用失败的回调函数 |

| **值** | **说明** |
| --- | --- |
| ascii | https://en.wikipedia.org/wiki/ASCII https://developer.mozilla.org/zh-CN/docs/Glossary/ASCII |
| base64 | [RFC 4648, Section 5](https://tools.ietf.org/html/rfc4648#section-5) |
| binary/latin1 | ISO-8859-1 https://en.wikipedia.org/wiki/ISO-8859-1 |
| hex | 十六进制 |
| ucs2/ucs-2/utf16le/utf-16le | 以小端序写入 |
| utf-8/utf8 | [RFC 3629, Section 4](https://www.rfc-editor.org/rfc/rfc3629.html#section-4) |

### 回调成功
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| errMsg | string | "writeFile:ok" |

### 回调失败
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| errNo | number | 错误码 |
| errMsg | string | "FileSystemManager.writeFile:fail" + 详细错误信息 |

### 错误码

| **errNo** | **errMsg** | **说明** |
| --- | --- | --- |
| 20000 | writeFile:fail {param_name} is invalid | filePath 参数错误 |
| 20000 | writeFile:fail data is invalid | data 传入参数类型不正确 |
| 20001 | writeFile:fail param should be xxx, but got xxx | 参数校验错误 |
| 21101 | writeFile:fail permission denied, writeFile {filePath_value} | 文件路径不可写 |
| 21103 | writeFile:fail user dir saved file size limit exceeded | 超出目录大小限制 |
| 21105 | saveFile:fail permission denied, saveFile {tempFilePath_value} | 源路径不是文件类型 |

### 代码示例

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    
    var filePath = "scfile://user/example.txt";
    
    //字符串
    fileSystemManager.WriteFile(new WriteFileStringParam{
      filePath = filePath,
      data = "example content",
      encoding = "utf8",
      success(_res) {
        Debug.Log("调用成功");
        var data = fileSystemManager.ReadFileSync(filePath);
        Debug.Log("写入的内容为:", data);
      },
      fail(res) {
        Debug.Log("调用失败", res.errMsg);
      }
    });
    
    //二进制数组
    var buffer = new byte[12];
    fileSystemManager.WriteFile(new WriteFileParam{
      filePath = filePath,
      data = buffer,
      success(_res) {
        Debug.Log("调用成功");
        var data = fileSystemManager.ReadFileSync(filePath);
        Debug.Log("写入的内容为:", data);
      },
      fail(rsp) {
        Debug.Log("调用失败", rsp.errMsg);
      }
    });
}
```

## FileSystemManager.WriteFileSync
同步写文件，只能写入用户目录 (scfile://user) 。

> 目前 Native 方案下效果与 File.WriteAllText 一致，路径不能使用 scfile 协议头，请使用 Application.persistentDataPath 等原生接口。

| **功能描述** | **接口类型** | **是否对外** | **字节专有** |
| --- | --- | --- | --- |
| 写文件，只能写入用户目录 (scfile://user)，文件不存在时会新建文件 | 异步 | 是 | 否 |

### **语法**

```csharp
public string WriteFileSync(string filePath, string data, string encoding = "utf8")
public string WriteFileSync(string filePath, byte[] data)
```

### 参数说明
options 为 object 类型，属性如下：

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| filePath | string | -- | 是 | 要写入的文件路径, 必须以` scfile://user `开头 |
| data | string / byte[] | -- | 是 | 要写入的文本或二进制数据 |
| encoding | string | utf8 | 否 | 指定写入文件的字符编码 |

### 返回值

| **类型** | **说明** |
| --- | --- |
| string | 返回值为空表示写入成功，否则返回失败信息 |

### 代码示例

```csharp
private void Test() {
    //字符串
    var fileSystemManager = TT.GetFileSystemManager();
    
    var filePath = "scfile://user/example.txt";
    var buffer = new byte[size * dimension];
    var errMsg = fileSystemManager.WriteFileSync(
      filePath,
      data: "example content",
      encoding: "utf8"
    );
    
    if (string.IsNullOrEmpty(errMsg))
    {
        Debug.Log("调用成功");
        var data = fileSystemManager.ReadFileSync(filePath);
        Debug.Log("写入的内容为:", data);
    }
    else
    {
        Debug.Log("WriteFileSync", errMsg);
    }
}
```

```csharp
private void Test() {
    // 二进制数组
    var fileSystemManager = TT.GetFileSystemManager();
    
    var filePath = "scfile://user/example.txt";
    var buffer = new byte[size * dimension];
    var errMsg = fileSystemManager.WriteFileSync(
      filePath,
      data: buffer
    );
    
    if (string.IsNullOrEmpty(errMsg))
    {
        Debug.Log("调用成功");
        var data = fileSystemManager.ReadFileSync(filePath);
        Debug.Log("写入的内容为:", data);
    }
    else
    {
        Debug.Log("WriteFileSync", errMsg);
    }
}
```

## FileSystemManager.ReadFile
读取本地文件内容。

> 目前 Native 方案下效果与 File.ReadAllText / ReadAllBytes 一致，路径不能使用 scfile 协议头，请使用 Application.persistentDataPath 等原生接口。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | readFile 可以用于 用户目录 (scfile://user)、临时目录(scfile://temp) 以及 包内目录(访问包内目录不需要加额外协议头) |
| 相关教程 | 无 |

### **语法**

```csharp
public void ReadFile(ReadFileParam options)
```

### 参数说明
options 为 ReadFileStringParam / ReadFileParam 类型，属性如下：

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| filePath | string | -- | 是 | 要写入的文件路径, 必须以 `scfile://user` 开头 |
| data | string / byte[] | -- | 是 | 要写入的文本或二进制数据 |
| encoding | string | utf8 | 否 | 指定写入文件的字符编码 |
| success | function | null | 否 | 接口调用成功的回调函数 |
| fail | function | null | 否 | 接口调用失败的回调函数 |

| **encoding 的合法值** | **说明** |
| --- | --- |
| ascii |  |
| base64 |  |
| binary |  |
| hex |  |
| ucs2/ucs-2/utf16le/utf-16le | 以小端序读取 |
| utf-8/utf8 |  |
| latin1 |  |

### 回调成功
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| stringData | string | 如果返回的是字符串，则数据在这个字段 |
| binData | byte[] | 如果返回二进制（encoding = binary），则数据在这个字段 |
| errMsg | string | "FileSystemManager.readFile:ok" |

### 回调失败
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| errNo | number | 错误码 |
| errMsg | string | "FileSystemManager.readFile:fail " + 详细错误信息 |

### 错误码

| **errNo** | **errMsg** | **说明** |
| --- | --- | --- |
| 20000 | writeFile:fail {param_name} is invalid | filePath 参数错误 |
| 20000 | writeFile:fail data is invalid | data 传入参数类型不正确 |
| 20001 | writeFile:fail param should be xxx, but got xxx | 参数校验错误 |
| 21101 | writeFile:fail permission denied, writeFile {filePath_value} | 文件路径不可写 |
| 21103 | writeFile:fail user dir saved file size limit exceeded | 超出目录大小限制 |
| 21105 | saveFile:fail permission denied, saveFile {tempFilePath_value} | 源路径不是文件类型 |

### 代码示例

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    
    var filePath = "scfile://user/example.txt";
    
    fileSystemManager.ReadFile(new ReadFileParam
      filePath = filePath,
      encoding = "utf8", // 二进制时使用 binary
      success(rsp) {
          if (rsp.binData != null)
           {
              Debug.Log($"读取成功，文件长度：{rsp.binData.Length}");
           }
           else if (!string.IsNullOrEmpty(rsp.stringData))
           {
               Debug.Log($"读取成功， content: {rsp.stringData}");
           }
           else
           {
              Debug.Log("读取成功，但文件内容为空");
           }
      },
      fail(rsp) {
          Debug.Log("调用失败", rsp.errMsg);
      }
    });
}
```

## FileSystemManager.ReadFileSync
同步读取本地文件内容。

> 目前 Native 方案下效果与 File.ReadAllText / ReadAllBytes 一致，路径不能使用 scfile 协议头，请使用   Application.persistentDataPath 等原生接口。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | readFileSync 可以用于 用户目录 (scfile://user)、临时目录(scfile://temp) 以及 包内目录(访问包内目录不需要加额外协议头) |
| 相关教程 | 无 |

### **语法**

```csharp
public string ReadFileSync(string filePath, string encoding)
public byte[] ReadFileSync(string filePath)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| filePath | string |  | 是 | 要写入的文件路径, 必须以 `scfile://user` 开头 |
| encoding | string | utf8 | 否 | 指定写入文件的字符编码 |

| **encoding 的合法值** | **说明** |
| --- | --- |
| ascii |  |
| base64 |  |
| binary |  |
| hex |  |
| ucs2/ucs-2/utf16le/utf-16le | 以小端序读取 |
| utf-8/utf8 |  |
| latin1 |  |

### 返回值

| 类型 | 说明 |
| --- | --- |
| string/byte[] | 文件内容, 根据 encoding 设置不同返回 string 或 byte[] 类型 |

### 代码示例

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    
    var filePath = "scfile://user/example.txt";
    
    var data = fileSystemManager.ReadFileSync(
      filePath,
      encoding = "utf8"
    ）；
    Debug.Log($"读取成功， 内容: {rsp.stringData}");
    
    var byteData = fileSystemManager.ReadFileSync(
      filePath,
      encoding = "binary"
    ）；
    Debug.Log($"读取成功， 长度: {byteData.Length}");
}
```

## FileSystemManager.CopyFile
复制文件。

> 目前 Native 方案下效果与 File.Copy 一致，路径不能使用 scfile 协议头，请使用 Application.persistentDataPath 等原生接口。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | srcPath 值和 destPath 必须对等。如果 srcPath 是文件路径，destPath 就要是文件路径。目前不支持目录拷贝。 当拷贝源路径为文件时，目标也是要是个文件路径，例如，源：scfile://user/test1.zip，那么目标可以是 scfile://user/test2.zip， 这里 test2.zip 为开发者定义的拷贝后目标文件名字。 |
| 相关教程 | 无 |

### **语法**

```csharp
public void CopyFile(CopyFileParam options)
```

### 参数说明
options 为 CopyFileParam 类型，属性如下：

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| srcPath | string | -- | 是 | 源文件路径，只可以是普通文件，不能是目录 |
| destPath | string | -- | 是 | 目标文件路径, 必须以 scfile://user 开头 |
| success | function | null | 否 | 接口调用成功的回调函数 |
| fail | function | null | 否 | 接口调用失败的回调函数 |

### 回调成功
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| errMsg | string | "FileSystemManager.copyFile:ok" |

### 回调失败
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| errNo | number | 错误码 |
| errMsg | string | "FileSystemManager.copyFile:fail " + 详细错误信息 |

### 错误码

| **errNo** | **errMsg** | **说明** |
| --- | --- | --- |
| 20000 | copyFile:fail srcPath is invalid | srcPath 参数错误 |
| 20000 | copyFile:fail destPath is invalid | destPath 参数错误 |
| 20001 | copyFile:fail param should be xxx, but got xxx | 参数校验错误 |
| 21101 | copyFile:fail permission denied, copyFile {srcPath_value} -> {destPath_value} | 无操作权限(源路径不可读/目标路径不可写) |
| 21102 | copyFile:fail operation not permitted, copyFile {srcPath_value} | path 类型不对 (directory/file) |
| 21103 | copyFile:fail no such file or directory, copyFile {srcPath_value} -> {destPath_value} | 文件不存在 |
| 21104 | copyFile:fail user dir saved file size limit exceeded | 超出 User 目录存储上限 |

### 代码示例

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    
    var srcPath = "scfile://user/example1.txt";
    
    var destPath = "scfile://user/example2.txt";
    
    fileSystemManager.CopyFile(new CopyFileParam 
    {
        srcPath = srcPath,
        destPath = destPath,
        success = (rsp) => {
            Debug.Log($"copy file from {srcPath} to {destPath} succeed!");
         fail = (rsp) => {
            Debug.Log($"copy file failed . errCode:  {rsp.errCode}  errMsg: {rsp.errMsg}");
         }
    });
}
```

## FileSystemManager.CopyFileSync
同步复制文件。

> 目前 Native 方案下效果与 File.Copy 一致，路径不能使用 scfile 协议头，请使用 Application.persistentDataPath 等原生接口。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | srcPath 值和 destPath 必须对等。如果 srcPath 是文件路径，destPath 就要是文件路径。目前不支持目录拷贝。 当拷贝源路径为文件时，目标也是要是个文件路径，例如，源：scfile://user/test1.zip，那么目标可以是 scfile://user/test2.zip， 这里 test2.zip 为开发者定义的拷贝后目标文件名字。 |
| 相关教程 | 无 |

### **语法**

```csharp
public string CopyFileSync(string srcPath, string destPath)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| srcPath | string | -- | 是 | 源文件路径，只可以是普通文件，不能是目录 |
| destPath | string | -- | 是 | 目标文件路径, 必须以 scfile://user 开头 |

### 返回值

| **类型** | **说明** |
| --- | --- |
| string | 为空则表示复制成功，否则为失败，并带上失败信息 |

### 错误码

| **errNo** | **errMsg** | **说明** |
| --- | --- | --- |
| 20000 | copyFile:fail srcPath is invalid | srcPath 参数错误 |
| 20000 | copyFile:fail destPath is invalid | destPath 参数错误 |
| 20001 | copyFile:fail param should be xxx, but got xxx | 参数校验错误 |
| 21101 | copyFile:fail permission denied, copyFile {srcPath_value} -> {destPath_value} | 无操作权限(源路径不可读/目标路径不可写) |
| 21102 | copyFile:fail operation not permitted, copyFile {srcPath_value} | path 类型不对 (directory/file) |
| 21103 | copyFile:fail no such file or directory, copyFile {srcPath_value} -> {destPath_value} | 文件不存在 |
| 21104 | copyFile:fail user dir saved file size limit exceeded | 超出 User 目录存储上限 |

### 代码示例

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    
    var srcPath = "scfile://user/example1.txt";
    
    var destPath = "scfile://user/example2.txt";
    
    var errMsg = fileSystemManager.CopyFileSync(
        srcPath,
        destPath
    );
    if (string.IsNullOrEmpty(errMsg))
    {
        Debug.Log($"copy file from {srcPath} to {destPath} succeed!");
    }
    else
    {
        Debug.Log($"CopyFileSync:  {errMsg}");
    }
}
```

## FileSystemManager.RenameFile
重命名文件，可以把文件从 oldPath 移动到 newPath 。

> 目前 Native 方案下效果与 File.Move 一致，路径不能使用 scfile 协议头，请使用 Application.persistentDataPath 等原生接口。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 因为开发者只有在 scfile://user 目录下才有写的权限, 因此 rename 只能在用户目录下进行。 |
| 相关教程 | 无 |

### **语法**

```csharp
void RenameFile(RenameFileParam options)
```

### 参数说明
options 为 RenameFileParam 类型，属性如下：

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| srcPath | string | -- | 是 | 源文件路径，只可以是普通文件，不能是目录 |
| destPath | string | -- | 是 | 目标文件路径, 必须以 scfile://user 开头 |
| success | function | null | 否 | 接口调用成功的回调函数 |
| fail | function | null | 否 | 接口调用失败的回调函数 |

### 回调成功
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| errMsg | string | "FileSystemManager.rename:ok" |

### 回调失败
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| errNo | number | 错误码 |
| errMsg | string | "FileSystemManager.rename:fail" + 详细错误信息 |

### 错误码

| **errNo** | **errMsg** | **说明** |
| --- | --- | --- |
| 20000 | rename:fail oldPath is invalid | oldPath 参数错误 |
| 20000 | rename:fail newPath is invalid | newPath 参数错误 |
| 20001 | rename:fail param should be xxx, but got xxx | 参数校验错误 |
| 21101 | rename:fail permission denied, copyFile {srcPath_value} -> {destPath_value} | 无操作权限(源路径不可读/目标路径不可写) |
| 21102 | rename:fail operation not permitted, copyFile {srcPath_value} | path 类型不对(directory/file) |
| 21103 | rename:fail no such file or directory, rename {srcPath_value} -> {destPath_value} | 文件不存在 |
| 21104 | rename:fail user dir saved file size limit exceeded | 超出 User 目录存储上限 |

### 代码示例

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    
    var srcPath = "scfile://user/example1.txt";
    
    var destPath = "scfile://user/example2.txt";
    
    fileSystemManager.RenameFile(new RenameFileParam 
    {
        srcPath = srcPath,
        destPath = destPath,
        success = (rsp) => {
            Debug.Log($"rename file from {srcPath} to {destPath} succeed!");
         fail = (rsp) => {
            Debug.Log($"rename file failed, errCode: {rsp.errCode} errMsg: {rsp.errMsg}");
         }
    });
}
```

## FileSystemManager.RenameFileSync
同步重命名文件，可以把文件从 oldPath 移动到 newPath。

> 目前 Native 方案下效果与 File.Copy 一致，路径不能使用 scfile 协议头，请使用 Application.persistentDataPath 等原生接口。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 因为开发者只有在 scfile://user 目录下才有写权限, 因此 rename 只能在用户目录下进行。 |
| 相关教程 | 无 |

### **语法**

```csharp
public string RenameFileSync(string srcPath, string destPath)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| srcPath | string | -- | 是 | 源文件路径，只可以是普通文件，不能是目录 |
| destPath | string | -- | 是 | 目标文件路径, 必须以 scfile://user 开头 |

### 返回值

| **类型** | **说明** |
| --- | --- |
| string | 为空则表示重命名成功，否则为失败，并带上失败信息 |

### 代码示例

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    
    var srcPath = "scfile://user/example1.txt";
    
    var destPath = "scfile://user/example2.txt";
    
    var errMsg = fileSystemManager.RenameFileSync(
        srcPath,
        destPath
    );
    if (string.IsNullOrEmpty(errMsg))
    {
        Debug.Log($"Rename file from {srcPath} to {destPath} succeed!");
    }
    else
    {
        Debug.Log($"RenameFileSync failed:  {errMsg}");
    }
}
```

## FileSystemManager.UnLink
删除文件，只能在 scfile://user 开头的用户目录下操作。

> 目前 Native 方案下效果与 File.Delete 一致，路径不能使用 scfile 协议头，请使用 Application.persistentDataPath 等原生接口。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 开发者只能删除 用户目录(scfile://user) 下的文件 |
| 相关教程 | 无 |

### **语法**

```csharp
public void Unlink(UnlinkParam options)
```

### 参数说明
options 为 UnlinkParam 类型，属性如下：

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| filePath | string | -- | 是 | 要删除的文件路径, 必须以 scfile://user 开头 |
| success | function | null | 否 | 接口调用成功的回调函数 |
| fail | function | null | 否 | 接口调用失败的回调函数 |

### 回调成功
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| errMsg | string | "FileSystemManager.unlink:ok" |

### 回调失败
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| errNo | number | 错误码 |
| errMsg | string | "FileSystemManager.unlink:fail" + 详细错误信息 |

### 错误码

| **errNo** | **errMsg** | **说明** |
| --- | --- | --- |
| 20000 | unlink:fail filePath is invalid | filePath 参数错误 |
| 20001 | unlink:fail param should be xxx, but got xxx | 参数校验错误 |
| 21101 | unlink:fail permission denied, unlink {filePath_value} | 文件路径不可写 |
| 21102 | unlink:fail no such file or directory, unlink {filePath_value} | 文件不存在 |
| 21103 | unlink:fail operation not permitted, unlink {filePath_value} | 非文件路径 |

### 代码示例

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    
    var filePath = "scfile://user/example1.txt";
    
    fileSystemManager.Unlink(new UnlinkParam
    {
        filePath = filePath,
        success = (rsp) => {
            Debug.Log("删除成功");
         fail = (rsp) => {
            Debug.Log($"删除失败 errCode: {rsp.errCode}, errMsg: {rsp.errMsg}");
         }
    });
}
```

## FileSystemManager.UnlinkSync
同步删除文件，只能在 scfile://user 开头的用户目录下操作。

> 目前 Native 方案下效果与 File.Delete 一致，路径不能使用 scfile 协议头，请使用 Application.persistentDataPath 等原生接口。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 因为开发者只有在 scfile://user 目录下才有写的权限, 因此 UnlinkSync 只能在用户目录下进行。 |
| 相关教程 | 无 |

### **语法**

```csharp
string UnlinkSync(string filePath)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| filePath | string | -- | 是 | 要删除的文件路径，必须以 scfile://user 开头。 |

### 返回值

| **类型** | **说明** |
| --- | --- |
| string | 为空则表示删除成功，否则为失败，并带上失败信息 |

### 代码示例

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    
    var filePath = "scfile://user/example1.txt";
    
    var errMsg = fileSystemManager.UnlinkSync(
        filePath
    );
    if (string.IsNullOrEmpty(errMsg))
    {
        Debug.Log($"Unlink file from {filePath} succeed!");
    }
    else
    {
        Debug.Log($"Unlink file failed:  {errMsg}");
    }
}
```

## FileSystemManager.Mkdir
在 **用户目录** 下创建目录。

> 目前 Native 方案下效果与 Directory.CreateDirectory 一致，路径不能使用 scfile 协议头，请使用 Application.persistentDataPath 等原生接口。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | dirPath 必须以 scfile://user 开头 |
| 相关教程 | 无 |

### **语法**

```csharp
public void Mkdir(MkdirParam options)
```

### 参数说明
options 为 MkdirParam 类型，属性如下：

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| dirPath | string | -- | 是 | 要创建的文件路径, 必须以 scfile://user 开头 |
| recursive | bool | false | 否 | 是否在递归创建该目录的上级目录后再创建该目录。如果对应的上级目录已经存在，则不创建该上级目录。如 dirPath 为 a/b/c/d 且 recursive 为 true，将创建 a 目录，再在 a 目录下创建 b 目录，以此类推直至创建 a/b/c 目录下的 d 目录。 |
| success | function | null | 否 | 接口调用成功的回调函数 |
| fail | function | null | 否 | 接口调用失败的回调函数 |

### 回调成功
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| errMsg | string | "FileSystemManager.mkdir:ok" |

### 回调失败
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| errNo | number | 错误码 |
| errMsg | string | "FileSystemManager.mkdir:fail" + 详细错误信息 |

### 错误码

| **errNo** | **errMsg** | **说明** |
| --- | --- | --- |
| 20000 | mkdir:fail dirPath is invalid | dirPath 参数错误 |
| 20001 | mkdir:fail param should be xxx, but got xxx | 参数校验错误 |
| 21101 | mkdir:fail permission denied, mkdir {dirPath_value} | 无操作权限(dirPath 路径不可写) |
| 21102 | mkdir:fail file already exists, mkdir {dirPath_value} | dirPath 目录已经存在 |
| 21103 | mkdir:fail no such file or directory, mkdir {dirPath_value} | dirPath 父级目录不存在 |

### 代码示例

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    
    var dirPath = "scfile://user/example-dir";
    
    fileSystemManager.Mkdir(new MkdirParam 
    {
        dirPath = dirPath,
        recursive = false,
        success = (rsp) => {
            Debug.Log("创建成功");
         fail = (rsp) => {
            Debug.Log($"创建失败 errCode: {rsp.errCode}, errMsg: {rsp.errMsg}");
         }
    });
}
```

## FileSystemManager.MkdirSync
同步在 **用户目录** 下创建目录。

> 目前 Native 方案下效果与 Directory.CreateDirectory 一致，路径不能使用 scfile 协议头，请使用 Application.persistentDataPath 等原生接口。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 因为开发者只有在 scfile://user 目录下才有写的权限, 因此 MkdirSync 只能在用户目录下进行。 |
| 相关教程 | 无 |

### **语法**

```csharp
public string MkdirSync(string dirPath, bool recursive = false)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| filePath | string | -- | 是 | 要创建的目录路径，必须以 scfile://user 开头。 |
| recursive | bool | false | 否 | 是否在递归创建该目录的上级目录后再创建该目录。如果对应的上级目录已经存在，则不创建该上级目录。如 dirPath 为 a/b/c/d 且 recursive 为 true，将创建 a 目录，再在 a 目录下创建 b 目录，以此类推直至创建 a/b/c 目录下的 d 目录。 |

### 返回值

| **类型** | **说明** |
| --- | --- |
| string | 为空则表示创建成功，否则为失败，并带上失败信息 |

### 代码示例

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    
    var dirPath = "scfile://user/example-dir";
    
    var errMsg = fileSystemManager.MkdirSync(
        dirPath,
        false
    );
    if (string.IsNullOrEmpty(errMsg))
    {
        Debug.Log($"MkdirSync from {dirPath} succeed!");
    }
    else
    {
        Debug.Log($"MkdirSync failed: {errMsg}");
    }
}
```

## FileSystemManager.Rmdir
删除目录，只能是 scfile://user 下的目录。

> 目前 Native 方案下效果与 Directory.Delete 一致，路径不能使用 scfile 协议头，请使用 Application.persistentDataPath 等原生接口。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 开发者只能删除 scfile://user 下的目录。 |
| 相关教程 | 无 |

### **语法**

```csharp
public void Rmdir(RmdirParam options)
```

### 参数说明
options 为 RmdirParam 类型，属性如下：

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| dirPath | string | -- | 是 | 要删除的目录路径, 必须以 scfile://user 开头 |
| recursive | bool | false | 否 | 是否递归删除目录下的文件，false 的情况下只能删除空目录 |
| success | function | null | 否 | 接口调用成功的回调函数 |
| fail | function | null | 否 | 接口调用失败的回调函数 |

### 回调成功
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| errMsg | string | "FileSystemManager.rmdir:ok" |

### 回调失败
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| errNo | number | 错误码 |
| errMsg | string | "FileSystemManager.rmdir:fail" + 详细错误信息 |

### 错误码

| **errNo** | **errMsg** | **说明** |
| --- | --- | --- |
| 20000 | rmdir:fail dirPath is invalid | dirPath 参数错误 |
| 20001 | rmdir:fail param should be xxx, but got xxx | 参数校验错误 |
| 21101 | rmdir:fail permission denied, rmdir {dirPath_value} | dirPath 路径不可写 |
| 21102 | rmdir:fail no such file or directory, rmdir {dirPath_value} | dirPath 路径不存在 |
| 21103 | rmdir:fail directory not empty | 目录不为空，且 recursive 为 false |
| 21105 | rmdir:fail operation not permitted, rmdir {dirPath_value} | 类型不正确(不是目录) |

### 代码示例

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    
    var dirPath = "scfile://user/example-dir";
    
    fileSystemManager.Rmdir(new RmdirParam 
    {
        dirPath = dirPath,
        recursive = false,
        success = (rsp) => {
            Debug.Log("创建成功");
         fail = (rsp) => {
            Debug.Log($"创建失败 errCode: {rsp.errCode}, errMsg: {rsp.errMsg}");
         }
    });
}
```

## FileSystemManager.RmdirSync
删除目录，开发者只能删除 用户目录 (scfile://user) 下的目录。

> 目前 Native 方案下效果与 File.Delete 一致，路径不能使用 scfile 协议头，请使用 Application.persistentDataPath 等原生接口。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 因为开发者只有在 scfile://user 目录下才有写的权限, 因此 rmdir 只能在用户目录下进行。 |
| 相关教程 | 无 |

### **语法**

```csharp
public string RmdirSync(string dirPath, bool recursive = false)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| dirPath | string | -- | 是 | 要删除的目录路径，必须以 scfile://user 开头。 |
| recursive | bool | false | 否 | 是否递归删除目录下的文件，false 的情况下只能删除空目录 |

### 返回值

| **类型** | **说明** |
| --- | --- |
| string | 为空则表示删除成功，否则为失败，并带上失败信息 |

### 代码示例

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    
    var dirPath = "scfile://user/example-dir";
    
    var errMsg = fileSystemManager.RmdirSync(
        dirPath，
        true
    );
    if (string.IsNullOrEmpty(errMsg))
    {
        Debug.Log($"RmdirSync from {filePath} succeed!");
    }
    else
    {
        Debug.Log($"RmdirSync failed:  {errMsg}");
    }
}
```

## FileSystemManager.GetSavedFileList
判断该 url 是否有本地缓存文件（仅 WebGL 平台可用）。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 开发者只能删除 scfile://user 下的目录。 |
| 相关教程 | 无 |

### **语法**

```csharp
public void GetSavedFileList(GetSavedFileListParam param)
```

### 参数说明
options 为 GetSavedFileListParam 类型，属性如下：

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| success | function | -- | 否 | 接口调用成功的回调函数 |
| fail | function | -- | 否 | 接口调用失败的回调函数 |

### 回调成功
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| fileList | TTFileInfo[] | 文件数组，每一项是一个 `FileItem` |

**TTFileInfo** 的属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| filePath | string | 文件路径 |
| size | number | 本地文件大小，以字节为单位 |
| createTime | number | 文件保存时的时间戳，从 `1970/01/01 08:00:00` 到当前时间的秒数 |

### 回调失败
object 类型，属性如下：

| **属性名** | **类型** | **说明** |
| --- | --- | --- |
| fileList | TTFileInfo[] | 文件数组，每一项是一个 `FileItem` |
| errMsg | string | "FileSystemManager.rmdir:fail" + 详细错误信息 |
| errNo | number | 错误码 |

### 代码示例

```csharp
private void Test() {
    TT.GetFileSystemManager().GetSavedFileList(new GetSavedFileListParam()
    {
        success = (rsp) =>
        {
            PrintLog($"total file count: {rsp.fileList.Length}");
            double totalSize = 0;
            var fileCount = 0;
            var folderCount = 0;
            foreach (var info in rsp.fileList)
            {
                PrintLog($"path: {info.filePath}, mode: {info.mode}, size: {info.size}, " +
                         $"isFile: {info.IsFile()}, isDirectory: {info.IsDirectory()}, " +
                         $"createTime: {info.createTime}");
                if (info.IsFile())
                {
                    fileCount += 1;
                    totalSize += info.size;
                }
                else
                {
                    folderCount += 1;
                }
            }
    
            var unit = "B";
            if (totalSize > 1024 * 1024)
            {
                totalSize = totalSize / 1024.0 / 1024.0;
                unit = "MB";
            }
            else if (totalSize > 1024)
            {
                totalSize = totalSize / 1024.0;
                unit = "KB";
            }
    
            PrintLog($"总文件数量: {fileCount}, 文件夹数量: {folderCount}, 总文件大小: {totalSize:F2} {unit}");
            TTUIManager.ShowToast(
                $"调用成功，总文件数量: {fileCount}, 文件夹数量: {folderCount}, 总文件大小: {totalSize:F2} {unit}");
        },
        fail = (rsp) =>
        {
            PrintLogError($"GetSavedFileList fail: {rsp.errMsg}");
            TTUIManager.ShowToast($"调用失败: {rsp.errMsg}");
        }
    });
}
```

## FileSystemManager.GetLocalCachedPathForUrl
根据 url 链接获取本地缓存文件路径（仅 WebGL 平台可用）。
> **Native方案下，由于我们目前暂时还没有针对文件下载 url 进行处理，所以不会对下载的url文件进行文件缓存，该接口目前暂不能在Native方案下使用。**
### **语法**

```csharp
public string GetLocalCachedPathForUrl(string url)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| url | string | -- | 是 | *输入文件下载链接url*。 |

### 返回值

| **类型** | **说明** |
| --- | --- |
| string | 返回本地缓存文件路径，以scfile://user开头的路径，可以直接用这个路径访问该文件。 |

### 代码示例

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    var url = "https://img1.baidu.com/it/u=1927402677,3664842615&fm=253&fmt=auto&app=120&f=JPEG?w=750&h=500";
    var cachePath = TT.GetFileSystemManager().GetLocalCachedPathForUrl(url);
    if (TT.GetFileSystemManager().AccessSync(cachePath))
    {
        var errMsg = TT.GetFileSystemManager().UnlinkSync(cachePath);
        if (string.IsNullOrEmpty(errMsg))
        {
            Debug.Log($"{cachePath}删除成功");
        }
        else
        {
            Debug.Log($"{cachePath}删除失败: {errMsg}");
        }
    }
    else
    {
        Debug.Log("缓存文件不存在");
    }
}
```

## FileSystemManager.IsUrlCached
判断该 url 是否有本地缓存文件（仅 WebGL 平台可用）。
> **Native 方案下，由于我们目前暂时还没有针对文件下载 url 进行处理，所以不会对下载的 url 文件进行文件缓存，该接口目前暂不能在Native方案下使用。**
### **语法**

```csharp
public bool IsUrlCached(string url)
```

### 参数说明

| **属性名 ** | **类型 ** | **默认值 ** | **必填** | **说明 ** |
| --- | --- | --- | --- | --- |
| url | string | -- | 是 | 输入文件下载链接url。 |

### 返回值

| **类型** | **说明** |
| --- | --- |
| string | 返回本地缓存文件路径，以scfile://user开头的路径，可以直接用这个路径访问该文件。 |

### 代码示例

```csharp
private void Test() {
    var fileSystemManager = TT.GetFileSystemManager();
    var url = "https://img1.baidu.com/it/u=1927402677,3664842615&fm=253&fmt=auto&app=120&f=JPEG?w=750&h=500";
    var exist = TT.GetFileSystemManager().IsUrlCached(url);
    if (exist)
    {
        Debug.Log("缓存文件存在");
    }
    else
    {
        Debug.Log("缓存文件不存在");
    }
}
```

## 类 TTStatInfo
> Native版本 6.0.0 开始支持，WebGL支持
描述文件状态的对象。
### 属性

| **属性名** | 数据**类型** | **描述** |
| --- | --- | --- |
| mode | string | 文件的类型和存取的权限，对应 `POSIX` `stat.st_mode` |
| size | number | 文件大小，单位：`B`，对应 `POSIX` `stat.st_size` |
| lastAccessedTime | number | 文件最近一次被存取或被执行的时间，UNIX 时间戳，对应 `POSIX` `stat.st_atime` |
| lastModifiedTime | number | 文件最后一次被修改的时间，UNIX 时间戳，对应 `POSIX` `stat.st_mtime` |

### 方法

| 名称 | 参数 | 返回值 | 描述 |
| --- | --- | --- | --- |
| [isDirectory](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/stats/stats-is-directory) | 无 | boolean | 判断当前文件是否为一个目录 |
| [isFile](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/stats/stats-is-file) | 无 | boolean | 判断当前文件是否为一个普通文件 |

### 代码示例

```csharp
private void Test() {
    var filePath = "scfile://user/example.txt";
    
    try
    {
        var info = TT.GetFileSystemManager().StatSync(path, true);
        if (info != null)
        {
            Debug.Log($"{path} mode: {info.mode}, size: {info.size}, " +
                     $"lastAccessedTime: {info.lastAccessedTime}, lastModifiedTime: {info.lastModifiedTime}, " +
                     $"isFile: {info.IsFile()}, isDirectory: {info.IsDirectory()}");
        }
        else
        {
            Debug.LogError($"StatSync info is null");
        }
    }
    catch (Exception ex)
    {
        Debug.LogError($"StatSync failed, error: {ex}");
    }
}
```

## TTBaseResponse
文件异步 API 回调。
### 属性

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | 错误信息 |
| errCode | int | 错误码 |
