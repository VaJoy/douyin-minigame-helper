---
title: "抖音云"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/douyin-cloud-module/dycloud
update_time: 2024-12-31
---

抖音云功能相关接口。
## TT.CreateCloud
> 6.0.0 开始支持本方法
创建抖音云实例。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public static DouyinCloud CreateCloud()
```

### 返回说明

| 类型 | 说明 |
| --- | --- |
| DouyinCloud | 返回抖音云实例 DouyinCloud，该实例为单例，通过该实例去访问抖音云 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    DouyinCloud cloud = TT.CreateCloud();
}
```

## DouyinCloud.CallContainer
> 6.0.0 开始支持本方法
请求抖音云服务端。

| 前提条件 | 已正确获取抖音云实例 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public void CallContainer(string eveId, 
    string serviceId, 
    string path, 
    Options options,
    Action<Response> success, 
    Action<ErrorResponse> fail)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| eveId | string | -- | 是 | 抖音云平台环境 id，在抖音云平台查看 |
| serviceId | string | -- | 是 | 抖音云平台服务 id |
| path | string | -- | 是 | 请求 path |
| options | Options | -- | 是 | 请求参数 |
| success | Action<Response> | -- | 是 | 成功回调 |
| fail | Action<ErrorResponse> | -- | 是 | 失败回调 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    DouyinCloud.Options options = new DouyinCloud.Options();
    options.Header = new JsonData();
    options.Header["hello"] = "asdasd";
    options.Method = "GET";

    DouyinCloud cloud = TT.CreateCloud();
    cloud.CallContainer("xxxxxx", "xxxxx",
        "xxxxxxx",
        options,
        response =>
        {
            Debug.Log($"CallContainer: /api/getinfo response.StatusCode:{response.StatusCode},response.Data:{response.Data}");
        },
        errResponse =>
        {
            Debug.Log($"CallContainer: /api/getinfo response.StatusCode:{response.StatusCode},response.ErrMsg:{response.ErrMsg}");
        });
}
```

## DouyinCloud.GetTempFileUrl
> 6.0.0 开始支持本方法
获取抖音云文件访问地址。

| 前提条件 | 已正确获取抖音云实例 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public void GetTempFileUrl(string eveId, 
    List<String> cloudPaths, 
    int maxAge,
    Action<FileResponse> success, 
    Action<ErrorResponse> fail);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| eveId | string | -- | 是 | 抖音云平台环境 id，在抖音云平台查看 |
| cloudPaths | List<String> | -- | 是 | 云文件 path |
| maxAge | int | -- | 是 | 最长有效期 |
| success | Action<FileResponse> | -- | 是 | 成功回调 |
| fail | Action<ErrorResponse> | -- | 是 | 失败回调 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    string cloudPath = "dy_cloud_test/dy_cloud_test/dy_cloud_test.txt";
    List<string> paths = new List<string>();
    paths.Add(cloudPath);
    TT.CreateCloud().GetTempFileUrl("xxxxx", paths, 86400,
        response1 =>
        {
            Debug.Log($"GetTempFileUrl: response:{response1}");
        },
        response2 =>
        {
            Debug.Log($"GetTempFileUrl: failed response.StatusCode:{response2.StatusCode},response.ErrMsg:{response.ErrMsg}");
        });
}
```

## DouyinCloud.DeleteFile
> 6.0.0 开始支持本方法
删除抖音云文件。

| 前提条件 | 已正确获取抖音云实例 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public void DeleteFile(string eveId, 
    List<string> cloudPaths, 
    Action<FileResponse> success,
    Action<ErrorResponse> fail);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| eveId | string | -- | 是 | 抖音云平台环境 id，在抖音云平台查看 |
| cloudPaths | string | -- | 是 | 云文件 path |
| success | Action<FileResponse> | -- | 是 | 成功回调 |
| fail | Action<ErrorResponse> | -- | 是 | 失败回调 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    string cloudPath = "dy_cloud_test/dy_cloud_test/dy_cloud_test.txt";
    List<string> paths = new List<string>();
    paths.Add(cloudPath);
    TT.CreateCloud().DeleteFile("xxxxx", paths,
        response1 =>
        {
            Debug.Log($"DeleteFile: response:{response1}");
        },
        response2 =>
        {
            Debug.Log($"DeleteFile: failed response.StatusCode:{response2.StatusCode},response.ErrMsg:{response2.ErrMsg}");
        });
}
```

## DouyinCloud.UploadFile
> 6.0.0 开始支持本方法
上传抖音云文件。

| 前提条件 | 已正确获取抖音云实例 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public void UploadFile(string eveId, 
    string cloudPath, 
    string filePath,
    Action<DownloadUploadProgressData> progress, 
    Action<UploadResponse> success, 
    Action<ErrorResponse> fail);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| eveId | string | -- | 是 | 抖音云平台环境 id，在抖音云平台查看 |
| cloudPath | string | -- | 是 | 云文件 path |
| filePath | string | -- | 是 | 文件绝对路径 |
| progress | Action<DownloadUploadProgressData> | -- | 是 | 上传进度回调 |
| success | Action<UploadResponse> | -- | 是 | 成功回调 |
| fail | Action<ErrorResponse> | -- | 是 | 失败回调 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    string filepath = Path.Combine(Application.persistentDataPath, "dy_test.txt");
    Debug.Log($"write {filepath}");
    TT.GetFileSystemManager().WriteFileSync(filepath, "test message test message test message test message test message test message test message test message");
    
    string cloudPath = "dy_cloud_test/dy_cloud_test/dy_cloud_test.txt";
    
    Debug.Log("TestUploadFileInner");
    Debug.Log($"filepath :{filepath}");
    Debug.Log($"cloudPath :{cloudPath}");
    
    TT.CreateCloud().UploadFile("xxxx", cloudPath, filepath,
        progress => { 
            Debug.Log($"TestUploadFile Progress : {progress.Progress}"); 
        },
        response1 => { 
            Debug.Log($"uploadFile success"); 
        },
        response2 =>{
            AppendText($"uploadFile:failed StatusCode:{response2.StatusCode}, ErrMsg :{response2.ErrMsg}");
        });
}
```

## DouyinCloud.DownloadFile
> 6.0.0 开始支持本方法
下载抖音云文件。

| 前提条件 | 已正确获取抖音云实例 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public void DownloadFile(string eveId, 
    string cloudPath, 
    string filePath,
    Action<DownloadUploadProgressData> progress, 
    Action<DownloadResponse> success,
    Action<ErrorResponse> fail);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| eveId | string | -- | 是 | 抖音云平台环境 id，在抖音云平台查看 |
| cloudPath | string | -- | 是 | 云文件 path |
| filePath | string | -- | 是 | 文件绝对路径 |
| progress | Action<DownloadUploadProgressData> | -- | 是 | 下载进度回调 |
| success | Action<UploadResponse> | -- | 是 | 成功回调 |
| fail | Action<ErrorResponse> | -- | 是 | 失败回调 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    string filepath = Path.Combine(Application.persistentDataPath, "dy_test_download.txt");
    string cloudPath = "dy_cloud_test/dy_cloud_test/dy_cloud_test.txt";
    
    Debug.Log("TestDownloadFile2");
    Debug.Log($"filepath :{filepath}");
    Debug.Log($"cloudPath :{cloudPath}");
    
    TT.CreateCloud().DownloadFile("xxxx", cloudPath, filepath,
        progress => { 
            Debug.Log($"DownloadFile Progress : {progress.Progress}"); 
        },
        response1 => { 
            Debug.Log($"DownloadFile success"); 
        },
        response2 =>{
            AppendText($"DownloadFile:failed StatusCode:{response2.StatusCode}, ErrMsg :{response2.ErrMsg}");
        });
}
```

## DouyinCloud.CloudDb
> 6.0.0 开始支持本方法
获取抖音云数据库对象。

| 前提条件 | 已正确获取抖音云实例 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
public CloudDB CloudDb();
```

### 返回说明

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
|  | CloudDB | 抖音云操作数据库实例 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    CloudDB cloudDB = TT.CreateCloud().CloudDb();
}
```

## CloudDB.GenDBCollection
> 6.0.0 开始支持本方法
创建 DBCollection 对象。

| 前提条件 | 已正确获取抖音云数据库对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
CloudDBCollection GenDBCollection(string evnId, string name);

// 返回 CloudDBCollection 实例，可以对该实例进行相关操作
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| eveId | string | -- | 是 | 抖音云平台环境 id，在抖音云平台查看 |
| name | string | -- | 是 | 抖音云 DB 名字 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    CloudDBCollection cloudDBCollection = TT.CreateCloud().CloudDb().GenDBCollection("xxxxx", "xxxx");
}
```

## CloudDBCollection.Doc
> 6.0.0 开始支持本方法
基于 docid 获取单个文档。

| 前提条件 | 已正确获取抖音云 DBCollection 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
CloudDBDocument Doc(string id);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | -- | 是 | docid，抖音云平台对应 docid |

### 返回说明

| 类型 | 说明 |
| --- | --- |
| CloudDBDocument | 返回 CloudDBDocument 实例，可以对该实例进行相关操作 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    TT.CreateCloud().CloudDb().GenDBCollection("xxxx", "xxx").Doc("xxxx");
}
```

## CloudDBDocument.Get
> 6.0.0 开始支持本方法
获取抖音云数据单个文档数据。

| 前提条件 | 已正确获取抖音云 CloudDBDocument 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
void Get(Action<DouyinCloud.DBResponse> success, Action<DouyinCloud.DBResponse> fail);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | Action<DouyinCloud.DBResponse> | -- | 是 | 成功回调 |
| fail | Action<DouyinCloud.DBResponse> | -- | 是 | 失败回调 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    TT.CreateCloud().CloudDb().GenDBCollection("xxxx", "xxx").Doc("xxxx").Get(
        response1 =>{
            Debug.Log($"TestDbDocGet Doc get StatusCode:{response1.StatusCode}, ErrMsg:{response1.ErrMsg}, Data:{response1.Data.ToJson()}");
        },
        response2 =>{
            Debug.Log($"TestDbDocGet failed StatusCode:{response2.StatusCode},ErrMsg:{response2.ErrMsg}");
        });
}
```

## CloudDBDocument.Update
> 6.0.0 开始支持本方法
更新单个云文档数据。

| 前提条件 | 已正确获取抖音云 CloudDBDocument 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
void Update(JsonData dataJson, 
    Action<DouyinCloud.DBResponse> success,
    Action<DouyinCloud.DBResponse> fail);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| dataJson | JsonData | -- | 是 | 更新数据 |
| success | Action<DouyinCloud.DBResponse> | -- | 是 | 成功回调 |
| fail | Action<DouyinCloud.DBResponse> | -- | 是 | 失败回调 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    JsonData data = GetTestDocJson(0);
    data["_id"] = "_idxxxx";
    TT.CreateCloud().CloudDb().GenDBCollection("xxxx", "xxx").Doc("xxxx").Update(
        data,
        response1 =>
        {
            Debug.Log($"TestDbDocGet Doc get StatusCode:{response1.StatusCode}, ErrMsg:{response1.ErrMsg}, Data:{response1.Data.ToJson()}");
        },
        response2 =>
        {
            Debug.Log($"TestDbDocGet failed StatusCode:{response2.StatusCode},ErrMsg:{response2.ErrMsg}");
        });
}
```

## CloudDBDocument.Set
> 6.0.0 开始支持本方法
设置单个云文档数据，仅会更新已有字段。

| 前提条件 | 已正确获取抖音云 CloudDBDocument 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
void Set(JsonData dataJson, 
    Action<DouyinCloud.DBResponse> success,
    Action<DouyinCloud.DBResponse> fail);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| dataJson | JsonData | -- | 是 | 更新数据 |
| success | Action<DouyinCloud.DBResponse> | -- | 是 | 成功回调 |
| fail | Action<DouyinCloud.DBResponse> | -- | 是 | 失败回调 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    JsonData setData = GetTestDocJson(1);
    setData["set_new_field"] = "hello value by TestDbDocSetJson";
    TT.CreateCloud().CloudDb().GenDBCollection("xxxx", "xxxx").Doc("xxxx").Set(
        setData,
        response1 =>{
            Debug.Log($"TestDbDocSet  RawCloudDb StatusCode:{response1.StatusCode} ErrMsg:{response1.ErrMsg} ,Data:{response1.Data.ToJson()}");
        },
        response =>{
            Debug.Log($"TestDbDocSet failed StatusCode:{response2.StatusCode} ErrMsg:{response2.ErrMsg}");
        });
}
```

## CloudDBDocument.Remove
> 6.0.0 开始支持本方法
删除单个云文档数据。

| 前提条件 | 已正确获取抖音云 CloudDBDocument 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
void Remove(Action<DouyinCloud.DBResponse> success, 
    Action<DouyinCloud.DBResponse> fail);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | Action<DouyinCloud.DBResponse> | -- | 是 | 成功回调 |
| fail | Action<DouyinCloud.DBResponse> | -- | 是 | 失败回调 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    TT.CreateCloud().CloudDb().GenDBCollection("xxxx", "xxxx").Doc("xxxx")
    .Remove(
        response1 =>
        {
            Debug.Log($"Doc Remove id 为空 不符合预期 Data:{response1.Data.ToJson()}");
        },
        response2 =>
        {
            if (response2.StatusCode == DouyinCloudDBError.DOC_ID_PARAM_ERROR.GetCode())
            {
                Debug.Log($"Doc Remove id 为空 符合预期 ");
            }
            else
            {
                Debug.Log($"Doc Remove id 为空 不符合预期 StatusCode:{response2.StatusCode},ErrMsg:{response2.ErrMsg}");
            }
        });
}
```

## CloudDBCollection.Add
> 6.0.0 开始支持本方法
添加数据，当前仅支持单个添加。

| 前提条件 | 已正确获取抖音云 DBCollection 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
void Add(JsonData dataMap, Action<DouyinCloud.DBResponse> success,
    Action<DouyinCloud.DBResponse> fail)
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| dataMap | JsonData | -- | 是 | dataMap，添加数据内容 |
| success | Action<DouyinCloud.DBResponse> | -- | 是 | 成功回调 |
| fail | Action<DouyinCloud.DBResponse> | -- | 是 | 失败回调 |

### 代码示例

```csharp
public void TestDouyinCloud()
{

    JsonData jsonData = new JsonData();
    JsonData subJson = new JsonData();
    JsonData subSubJson = new JsonData();
    
    bool boolValue = true;
    
    jsonData["num_int"] = 1;
    jsonData["num_float"] = 1.1f;
    
    subJson["sub_num_int"] = 1;
    subJson["sub_num_float"] = 1.1f;
    
    subSubJson["sub_sub_num_int"] = 1;
    subSubJson["string"] = "hello sub sub";

    subJson["sub_sub_json"] = subSubJson;    
    jsonData["sub_json"] = subJson;

    TT.CreateCloud().CloudDb().GenDBCollection("xxx", "xxx").Add(
        jsonData,
        response1 =>{
            Debug.Log($"TestDBAdd  RawCloudDb StatusCode:{response1.StatusCode},Data:{response1.Data.ToJson()}");
        },
        response2 =>{
            Debug.Log($"TestDBAdd RawCloudDb StatusCode:{response2.StatusCode},ErrMsg:{response2.ErrMsg}");
        });
}
```

## CloudDB.GenDbCmd
> 6.0.0 开始支持本方法
获取 CloudDBCommand 对象。

| 前提条件 | 已正确获取抖音云数据库对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
CloudDBCommand GenDbCmd(string name);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | -- | 是 | 字段名字 name |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    CloudDBCommand Cmd = TT.CreateCloud().CloudDb().GenDbCmd("num_int");
}
```

## CloudDBCommand.And
> 6.0.0 开始支持本方法
数据库操作符 And。

| 前提条件 | 已正确获取抖音云 CloudDBCommand 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
CloudDBCommand And(List<CloudDBCommand> listData);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listData | List<CloudDBCommand> | -- | 是 |  |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    List<CloudDBCommand> andCmdList = new List<CloudDBCommand>();
    CloudDBCommand andCmd = TT.CreateCloud().CloudDb().GenDbCmd("");
    andCmd.And(andCmdList);
}
```

## CloudDBCommand.Or
> 6.0.0 开始支持本方法
数据库操作符 Or。

| 前提条件 | 已正确获取抖音云 CloudDBCommand 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
CloudDBCommand Or(List<CloudDBCommand> listData);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listData | List<CloudDBCommand> | -- | 是 |  |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    List<CloudDBCommand> otherCmdList = new List<CloudDBCommand>();
    otherCmdList.Add(TT.CreateCloud().CloudDb().GenDbCmd("num_long").Eq(3000000007L));
    otherCmdList.Add(TT.CreateCloud().CloudDb().GenDbCmd("boolean").Eq(true));
    otherCmdList.Add(TT.CreateCloud().CloudDb().GenDbCmd("num_int").Gt(2));
    CloudDBCommand orCmd = TT.CreateCloud().CloudDb().GenDbCmd("");
    orCmd.Or(otherCmdList);
}
```

## CloudDBCommand.Nor
> 6.0.0 开始支持本方法
数据库操作 Not or。

| 前提条件 | 已正确获取抖音云 CloudDBCommand 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
CloudDBCommand Nor(List<CloudDBCommand> listData);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listData | List<CloudDBCommand> | -- | 是 |  |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    List<CloudDBCommand> otherCmdList = new List<CloudDBCommand>();
    otherCmdList.Add(TT.CreateCloud().CloudDb().GenDbCmd("num_int").Eq(8));
    otherCmdList.Add(TT.CreateCloud().CloudDb().GenDbCmd("boolean").Eq(true));
    CloudDBCommand orCmd = TT.CreateCloud().CloudDb().GenDbCmd("");
    orCmd.Nor(otherCmdList);
}
```

## CloudDBCommand.Eq
> 6.0.0 开始支持本方法
数据库操作 =。

| 前提条件 | 已正确获取抖音云 CloudDBCommand 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
CloudDBCommand Eq(object para);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| para | object | -- | 是 |  |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    List<CloudDBCommand> cmdList = new List<CloudDBCommand>();
    cmdList.Add(TT.CreateCloud().CloudDb().GenDbCmd("num_int").Eq(2));
}
```

## CloudDBCommand.Neq
> 6.0.0 开始支持本方法
数据库操作 `!=` 。

| 前提条件 | 已正确获取抖音云 CloudDBCommand 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
CloudDBCommand Neq(object para);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| para | object | -- | 是 |  |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    List<CloudDBCommand> cmdList = new List<CloudDBCommand>();
    cmdList.Add(TT.CreateCloud().CloudDb().GenDbCmd("string").Neq("hello 1"));
}
```

## CloudDBCommand.Lt
> 6.0.0 开始支持本方法
数据库操作 <。

| 前提条件 | 已正确获取抖音云 CloudDBCommand 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
CloudDBCommand Lt(object para);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| para | object | -- | 是 | 对应类型参数 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    List<CloudDBCommand> cmdList = new List<CloudDBCommand>();
    cmdList.Add(TT.CreateCloud().CloudDb().GenDbCmd("num_int").Lt(3));
}
```

## CloudDBCommand.Lte
> 6.0.0 开始支持本方法
数据库操作 <=。

| 前提条件 | 已正确获取抖音云 CloudDBCommand 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
CloudDBCommand Lte(object para);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| para | object | -- | 是 | 对应类型参数 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    List<CloudDBCommand> cmdList = new List<CloudDBCommand>();
    cmdList.Add(TT.CreateCloud().CloudDb().GenDbCmd("num_int").Lte(3));
}
```

## CloudDBCommand.Gt
> 6.0.0 开始支持本方法
数据库操作 >。

| 前提条件 | 已正确获取抖音云 CloudDBCommand 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
CloudDBCommand Gt(object para);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| para | object | -- | 是 | 对应类型参数 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    List<CloudDBCommand> cmdList = new List<CloudDBCommand>();
    cmdList.Add(TT.CreateCloud().CloudDb().GenDbCmd("num_int").Gt(3));
}
```

## CloudDBCommand.Gte
> 6.0.0 开始支持本方法
数据库操作 >=。

| 前提条件 | 已正确获取抖音云 CloudDBCommand 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
CloudDBCommand Gte(object para);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| para | object | -- | 是 | 对应类型参数 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    List<CloudDBCommand> cmdList = new List<CloudDBCommand>();
    cmdList.Add(TT.CreateCloud().CloudDb().GenDbCmd("num_int").Gte(3));
}
```

## CloudDBCommand.In
> 6.0.0 开始支持本方法
数据库操作 In。

| 前提条件 | 已正确获取抖音云 CloudDBCommand 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
CloudDBCommand In(List<object> listData);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listData | List<object> | -- | 是 | 对应类型参数 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    List<CloudDBCommand> cmdList = new List<CloudDBCommand>();
    List<object> inData = new List<object>();
    inData.Add(2);
    inData.Add(3);
    inData.Add(111);
    cmdList.Add(TT.CreateCloud().CloudDb().GenDbCmd("num_int").In(inData));
}
```

## CloudDBCommand.NIn
> 6.0.0 开始支持本方法
数据库操作 not in。

| 前提条件 | 已正确获取抖音云 CloudDBCommand 对象 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```csharp
CloudDBCommand NIn(List<object> listData);
```

### **参数说明 **

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listData | List<object> | -- | 是 | 对应类型参数 |

### 代码示例

```csharp
public void TestDouyinCloud()
{
    List<CloudDBCommand> cmdList = new List<CloudDBCommand>();
    List<object> ninData = new List<object>();
    ninData.Add(2);
    ninData.Add(3);
    ninData.Add(111);
    cmdList.Add(TT.CreateCloud().CloudDb().GenDbCmd("num_int").NIn(ninData));
}
```
