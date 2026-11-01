---
title: "抖音云C#接口文档"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/install-connect/starksdkmigrationguide/dycloud-csharp-interface
update_time: 2024-12-31
---

> **警告**
> - 本文档作为 旧版 StarkSdk API  文档将不再维护，**新版本 API 文档请至 “**[**Unity引擎适配 / C# API**](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/c-api/api-overview)** ”目录下查看**。
> - 迁移说明可参考 [旧版 StarkSdk API 迁移 TTSDK API 说明文档](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/guide/game-engine/rd-to-SCgame/unity-game-access/starksdk-migration-guide)。

## GetScUserInfo
API
对比原来的 GetScUserInfo 新增了参数 withCredentials ， 如果传递为true 则 OnGetScUserInfoSuccessCallback 回调里面的ScUserInfo 中会返回 cloudId 字段， 可以用于抖音云的请求中

```json
/// <summary>
/// 获取已登录用户的基本信息或特殊信息
/// 若匿名登录后 userinfo里面字段全部为默认值
/// 登录了宿主后可以获取账号数据，下次不用login GetScUserInfo也可以返回正确数据
/// 新增 withCredentials 字段，如果为true  这样就会返回ScUserInfo 中 cloudId 就会被赋值，可以用于后续的抖音云的接口调用
/// </summary>
/// <param name="withCredentials">是否获取加密信息以及 CloudId</param>
/// <param name="successCallback">验证有效的回调</param>
/// <param name="failedCallback">验证无效或者验证失败的回调</param>
/// 
[StarkVersion(MinSCAndroidVersion = "5.45.0")]
public abstract void GetScUserInfo(Boolean withCredentials, OnGetScUserInfoSuccessCallback successCallback,
    OnGetScUserInfoFailedCallback failedCallback);
```

#### 
## StarkDouyinCloud
抖音云服务 相关方法调用
#### CallContainer
请求抖音云服务
##### API

```json

/// <summary>
///
/// 请求抖音云服务端接口
/// </summary>
/// <param name="eveId">抖音云平台环境id</param>
/// <param name="serviceId">抖音云平台服务id</param>
/// <param name="path">请求path</param>
/// <param name="options">请求参数</param>
/// <param name="success">成功回调</param>
/// <param name="fail">失败回调</param>

[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public abstract void CallContainer(string eveId, string serviceId, string path, Options options,
    Action<Response> success, Action<ErrorResponse> fail);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| options | object | - | 是 | cloud 配置 |
| eveId | string | - | 是 | 云环境ID |
| serviceId | string | - | 是 | 云服务ID |
| success | Action<Response> | - | 是 | 请求成功回调 |
| fail | Action<ErrorResponse> | - | 是 | 请求失败回调 |

##### options 说明

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| Method | object | - | 否是 | 网络请求方法，支持 GET/POST/OPTIONS/PUT/HEAD/DELETE |
| Header | JsonData | - | 否 | 请求header |
| DataserviceId | JsonData | - | 否 | Post 请求的参数 |
| CloudIdMaps | Dictionary<string, string> | - | 否 | CloudId key 开发自己定义, value 是cloudId 数据,  cloudId 可以通过 GetScUserInfo 结果获取 |

##### Response 说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| Header | JsonData | 服务端返回的 header 数据 |
| Data | String | 服务端返回的 json 数据 |

##### ErrorResponse 说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| StatusCode | Int | 请求错误码 0 表示成功 |
| ErrMsg | String | 错误描述 |

#### GetTempFileUrl
获取抖音云文件 临时访问地址
##### Api

```json

/// <summary>
/// 抖音云文件信息
/// </summary>
public class FileInfo
{
    public int Status;
    public string FileName;
    public string URL;
    public int MaxAge;
    public string Message;
    public string RawJsonString;
}

/// <summary>
/// 抖音云操作文件结果
/// </summary>
public class FileResponse
{
    public int StatusCode;
    public string ErrMsg;
    
}

/// <summary>
/// 获取抖音云文件 临时访问地址
/// </summary>
/// <param name="eveId">抖音云平台环境id</param>
/// <param name="cloudPaths">云文件path</param>
/// <param name="maxAge">最大有效期</param>
/// <param name="success">成功回调</param>
/// <param name="fail">失败回调</param>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public abstract void GetTempFileUrl(string eveId, List<String> cloudPaths, int maxAge,
    Action<FileResponse> success, Action<ErrorResponse> fail);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| cloudPaths | List<String> | - | 是 | 云文件path 列表 |
| eveID | string | - | 是 | 云环境ID |
| serviceId | string | - | 是 | 云服务ID |
| success | Action<FileResponse> | - | 是 | 请求成功回调 |
| fail | Action<ErrorResponse> | - | 是 | 请求失败回调 |

##### FileResponse 说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| StatusCode | Int | 请求错误码 0 表示成功 |
| ErrMsg | String | 错误描述 |
| FileInfo | FileInfo | 文件信息 |

##### FileInfo 说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| Status | Int | 请求错误码 0 表示成功 |
| FileName | string | 文件名 |
| URL | string | 文件 url |
| MaxAge | Int | 有效期 |
| Message | string | 错误描述 |
| RawJsonString | string | 服务端返回的原始 json 数据 |

#### DeleteFile
##### API

```json
/// <summary>
/// 抖音云文件删除
/// </summary>
/// <param name="eveId">抖音云平台环境id</param>
/// <param name="cloudPaths">云文件path</param>
/// <param name="success">成功回调</param>
/// <param name="fail">失败回调</param>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public abstract void DeleteFile(string eveId, List<string> cloudPaths, Action<FileResponse> success,
    Action<FileResponse> fail);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| cloudPaths | List<String> | - | 是 | 云文件path 列表 |
| eveID | string | - | 是 | 云环境ID |
| serviceId | string | - | 是 | 云服务ID |
| success | Action<FileResponse> | - | 是 | 请求成功回调 |
| fail | Action<ErrorResponse> | - | 是 | 请求失败回调 |

#### UploadFile
##### API

```json
/// <summary>
/// 上传抖音云文件结果
/// </summary>
public class UploadResponse
{
    public int TaskId;
    public int StatusCode;
    public string ErrMsg;
}

/// <summary>
/// 上传\下载抖音云文件 进度回调
/// </summary>
public class DownloadUploadProgressData
{
    public float Progress;
    public long TotalBytesSent;
    public long TotalBytesExpectedToSend;
}

/// <summary>
/// 抖音云文件上传
/// </summary>
/// <param name="eveId">抖音云平台环境id</param>
/// <param name="cloudPath">云文件path</param>
/// <param name="filePath"> 需要传递绝对路径</param> 
/// <param name="progress"> 上传进度回调</param>
/// <param name="success"> 上传成功毁掉</param>
/// <param name="fail"> 上传失败回调</param>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public abstract void UploadFile(string eveId, string cloudPath, string filePath,
    Action<DownloadUploadProgressData> progress, Action<UploadResponse> success, Action<UploadResponse> fail);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| cloudPaths | List<String> | - | 是 | 云文件path 列表 |
| eveID | string | - | 是 | 云环境ID |
| serviceId | string | - | 是 | 云服务ID |
| filePath | string | - | 是 | 本地文件路径 |
| progress | Action<DownloadUploadProgressData> | - | 是 | 进度回调 |
| success | Action<FileResponse> | - | 是 | 请求成功回调 |
| fail | Action<ErrorResponse> | - | 是 | 请求失败回调 |

##### DownloadUploadProgressData 说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| Progress | float | 进度百分比 |
| TotalBytesSent | long | 以及传输的 字节大学 |
| TotalBytesExpectedToSend | long | 文件总大小 |

#### DownloadFile
##### API

```json

/// <summary>
/// 下载抖音云文件结果
/// </summary>
public class DownloadResponse
{
    public int TaskId;
    public string State;
    public string FilePath;
    public int StatusCode;
    public string ErrMsg;
}

/// <summary>
/// 下载抖音云文件 
/// </summary>
/// <param name="eveId">抖音云平台环境id</param>
/// <param name="cloudPath">云文件path</param>
/// <param name="filePath">需要传递绝对路径</param>
/// <param name="progress">下载进度回调</param>
/// <param name="success">下载成功毁掉</param>
/// <param name="fail">下载成功毁掉</param>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public abstract void DownloadFile(string eveId, string cloudPath, string filePath,
    Action<DownloadUploadProgressData> progress, Action<DownloadResponse> success,
    Action<DownloadResponse> fail);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| cloudPaths | String> | - | 是 | 云文件path |
| eveID | string | - | 是 | 云环境ID |
| serviceId | string | - | 是 | 云服务ID |
| filePath | string | - | 是 | 本地文件路径 |
| progress | Action<DownloadUploadProgressData> | - | 是 | 进度回调 |
| success | Action<DownloadResponse> | - | 是 | 请求成功回调 |
| fail | Action<DownloadResponse> | - | 是 | 请求失败回调 |

##### DownloadResponse 说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| FilePath | String | 文件路径 |
| StatusCode | int | 错误码 |
| ErrMsg | String | 错误描述 |

## CloudDB
所有的抖音云数据库的操作本质都是发起网络请求 /api/cloud_db/exec_cloud_database ，其的数据封装在 C# 层完成的。

#### GenDBCollection
创建一个 DBCollection 对象

```json
/// <summary>
/// 创建 DBCollection 对象
/// </summary>
/// <param name="evnId">抖音云环境 ID</param>
/// <param name="name">集合名称</param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBCollection GenDBCollection(string evnId, string name);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| eveID | string | - | 是 | 云环境ID |
| serviceId | string | - | 是 | 云服务ID |

#### GenServerDateJson
返回一个 ServerDate Json 对象, 用于表示服务端时间, 可以用于插入数据或者 查询的条件判断

```json
/// <summary>
/// 返回一个 ServerDate Json 对象, 用于表示服务端时间, 可以用于插入数据或者 查询的条件判断
/// </summary>
/// <param name="offsetTimeMil"></param>
/// <returns></returns>
public static JsonData GenServerDateJson(int offsetTimeMil)
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| offsetTimeMil | int | - | 是 | 引用的服务端时间偏移量，毫秒为单位，可以是正数或负数 |

##### 调用示例：
以下语句类比为 create_time < 当前服务端时间+1000ms

```json
StarkSDK.API.GetStarkDouyinCloudManager().CloudDb()
.GenDbCmd("create_time").Lt(CloudDB.GenServerDateJson(1000))
```

以下语句表示 create_time < 当前服务端时间-24h

```json
StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDbCmd("create_time").Gt(CloudDB.GenServerDateJson(-60 * 1000 * 60 * 24))
```

## CloudDBCollection
抖音云数据库 多条数据操作
#### Doc
返回Doc 对象， 该方法不会发起请求
##### API

```json
/// <summary>
/// 基于 docid 获取单个文档
/// </summary>
/// <param name="id"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBDocument Doc(string id);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| id | String | - | 是 | document id |

#### Add
添加数据
##### API

```json
/// <summary>
/// 添加数据, 当前进支持单个添加
/// </summary>
/// <param name="dataMap"></param>
/// <param name="success"></param>
/// <param name="fail"></param>
/// 
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public void Add(JsonData dataMap, Action<StarkDouyinCloud.DBResponse> success,
    Action<StarkDouyinCloud.DBResponse> fail);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| dataMap | JsonData | - | 是 | 插入的数据 |
| success | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作成功回调 |
| fail | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作失败回调 |

##### DBResponse 说明：

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| Data | String | 服务端返回的 json 数据 |
| StatusCode | int | 错误码 |
| ErrMsg | String | 错误描述 |

##### 调用示例

```json
JsonData jsonData = new JsonData();
jsonData["string"] = "hello ";
StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDBCollection(DY_CLOUD_EVN_ID, DY_CLOYD_DB_NAME).Add(
    jsonData,
    response =>
    {
        // TODO check add 数量
        PrintText(
            $"TestDBAdd  RawCloudDb response.StatusCode:{response.StatusCode},response.Data:{response.Data.ToJson()}");
    },
    response =>
    {
        PrintText(
            $"TestDBAdd RawCloudDb response.StatusCode:{response.StatusCode},response.ErrMsg:{response.ErrMsg}");
    });
    
    
```

###### 
#### where
设置 Wehe 查询条件
调用该方法还不会发出请求需要配合 Get Count Update Remove 方法一起使用
这里的wehre 查询只能做 Eq 查询， 即 a=1, a.b=1 这种， 无法做复杂的逻辑条件查询
如果需要复制的条件查询参考 **CloudDBCommand**

```json
/// <summary>
///
/// where 条件查询, 录入 a=1,  a.b=1 
/// </summary>
/// <param name="query"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBQuery where(Dictionary<string, object> query);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| query | Dictionary<string, object> | - | 是 | Where 查询条件参数，   a=1, b=1 |

#### AddWhereCmd
添加 查询 CMD 需要配合 CloudDBCommand 使用， 可以形成复杂的逻辑查询语句
调用该方法还不会发出请求需要配合 Get Count Update Remove 方法一起使用

```json
/// <summary>
/// 多种条件同时查询, 具体支持请看 CloudDBCommand
/// </summary>
/// <param name="cmd"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBQuery AddWhereCmd(CloudDBCommand cmd);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| query | CloudDBCommand | - | 是 | 复杂查询的 CloudDBCommand 对象 |

#### Field
设置返回数据的字段列表，入参是一个Dictionary 字节， key 是字段名， value 是bool 值， true 表示返回， false 表示 不返回改字段
调用该方法还不会发出请求需要配合 Get Count Update Remove 方法一起使用

```json
/// <summary>
/// 设置查询结果返回的字段,  a=true  a.b=true
/// </summary>
/// <param name="field"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBQuery Field(Dictionary<string, bool> field);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| field | CloudDBCommand | - | 是 | key 是字段名， value 是bool 值， true 表示返回， false 表示 不返回改字段 |

#### Limit
设置查询数据量限制
调用该方法还不会发出请求需要配合 Get Count Update Remove 方法一起使用

```json
/// <summary>
/// 设置查询数据量限制
/// </summary>
/// <param name="limitNum"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBQuery Limit(int limitNum);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| limitNum | int | - | 是 | 查询数据量限制 |

#### Skip
设置查询跳过的数量， 主要用于查询是否的翻页处理
调用该方法还不会发出请求需要配合 Get Count Update Remove 方法一起使用

```json
/// <summary>
/// 设置查询跳过的数量
/// </summary>
/// <param name="skipCount"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBQuery Skip(int skipCount);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| skipCount | int | - | 是 | 查询跳过的数量 |

#### OrderBy
设置查询结果的 排序方式
调用该方法还不会发出请求需要配合 Get Count Update Remove 方法一起使用

```json
/// <summary>
/// 设置查询的排序方式
/// </summary>
/// <param name="field"></param>
/// <param name="orderDirection"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBQuery OrderBy(string field, OrderDirection orderDirection);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| field | int | - | 是 | 排序字段名 |
| orderDirection | OrderDirection 枚举 |  |  | 排序顺序 DESC, ASC |

#### Get
获取查询结果

```json
/// <summary>
/// 获取查询结果
/// </summary>
/// <param name="success"></param>
/// <param name="fail"></param>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public void Get(Action<StarkDouyinCloud.DBResponse> success, Action<StarkDouyinCloud.DBResponse> fail);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作成功回调 |
| fail | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作失败回调 |

#### Count
执行 count 查询， 仅会返回数量

```json

/// <summary>
/// 获取查询结果 使用 count 语句
/// </summary>
/// <param name="success"></param>
/// <param name="fail"></param>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public void Count(Action<StarkDouyinCloud.DBResponse> success, Action<StarkDouyinCloud.DBResponse> fail);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作成功回调 |
| fail | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作失败回调 |

#### Update
基于设置的条件 批量更新数据

```json
/// <summary>
///
/// 基于设置的条件 更新数据
/// </summary>
/// <param name="dataMap"></param>
/// <param name="success"></param>
/// <param name="fail"></param>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public void Update(JsonData dataMap, Action<StarkDouyinCloud.DBResponse> success,
    Action<StarkDouyinCloud.DBResponse> fail);
    
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| dataMap | JsonData | - | 是 | 更新的数据 |
| success | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作成功回调 |
| fail | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作失败回调 |

#### Remove
基于设置的条件 删除数据

```json
/// <summary>
/// 基于设置的条件 删除数据
/// </summary>
/// <param name="success"></param>
/// <param name="fail"></param>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public void Remove(Action<StarkDouyinCloud.DBResponse> success,
    Action<StarkDouyinCloud.DBResponse> fail);
```

##### 参数说明：

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作成功回调 |
| fail | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作失败回调 |

#### 调用示例
多个条件 一起的 查询方法， Get 也换成 Count Update Remove 执行相应的逻辑

```json
Dictionary<string, object> query = new Dictionary<string, object>();
query[queryKey] = exceptValue;
CloudDBCollection cloudDBCollection = StarkSDK.API.GetStarkDouyinCloudManager().CloudDb()
    .GenDBCollection(DY_CLOUD_EVN_ID, DY_CLOYD_DB_NAME);

if (skip > 0)
{
    cloudDBCollection.Skip(skip);
}

cloudDBCollection.Where(query);

if (limit > 0)
{
    cloudDBCollection.Limit(limit);
}

if (isCheckOrder)
{
    cloudDBCollection.OrderBy(orderKey, orderDirection);
}

if (field != null)
{
    cloudDBCollection.Field(field);
}
// 上述条件设置完成后， 调用具体的查询 、更新方法
cloudDBCollection.Get(
     response =>
    {
        // TODO check add 数量
        PrintText(
            $"TestDBAdd  RawCloudDb response.StatusCode:{response.StatusCode},response.Data:{response.Data.ToJson()}");
    },
    response =>
    {
        PrintText(
            $"TestDBAdd RawCloudDb response.StatusCode:{response.StatusCode},response.ErrMsg:{response.ErrMsg}");
    }）
```

## CloudDBDocument
单个Doc 文件的 删改查
#### Get
获取当前Doc 文档的数据
##### API

```json

/// <summary>
/// 获取抖音云数据单个文档数据
/// </summary>
/// <param name="success"></param>
/// <param name="fail"></param>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public void Get(Action<StarkDouyinCloud.DBResponse> success, Action<StarkDouyinCloud.DBResponse> fail);
```

##### 参数说明

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作成功回调 |
| fail | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作失败回调 |

##### 调用示例：

```json
// 调用示例：
StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDBCollection(DY_CLOUD_EVN_ID, DY_CLOYD_DB_NAME)
    .Doc(DyCloudTestDocId).Get(
        succResponse =>
        {

        },
        failResponse =>
        {

        });
    
```

#### Update
更新 当前Doc 文档的数据
##### API

```json

/// <summary>
///
/// 更新单个云文档数据
/// </summary>
/// <param name="dataMap"></param>
/// <param name="success"></param>
/// <param name="fail"></param>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public void Update(JsonData dataMap, Action<StarkDouyinCloud.DBResponse> success,
    Action<StarkDouyinCloud.DBResponse> fail);
```

##### 参数说明

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| dataMap | JsonData | - | 是 | 更新的数据 |
| success | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作成功回调 |
| fail | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作失败回调 |

##### 调用示例：

```json
JsonData updateData = GetTestDocJson(2);
updateData["update_new_field"] = "hello value by TestDbDocUpdateJson";
StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDBCollection(DY_CLOUD_EVN_ID, DY_CLOYD_DB_NAME)
    .Doc(DyCloudTestDocId).Update(updateData,
        response =>
        {
            PrintText(
                $"TestDbDocUpdate  RawCloudDb response.StatusCode:{response.StatusCode},response.Data:{response.Data.ToJson()}");
        },
        response =>
        {
            PrintText(
                $"TestDbDocUpdate failed response.StatusCode:{response.StatusCode},response.ErrMsg:{response.ErrMsg}");
        });
```

#### Set
设置单个云文档数据, 仅会更新已有字段
##### API

```json
/// <summary>
/// 设置单个云文档数据, 仅会更新已有字段
/// </summary>
/// <param name="dataMap"></param>
/// <param name="success"></param>
/// <param name="fail"></param>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public void Set(JsonData dataMap, Action<StarkDouyinCloud.DBResponse> success,
    Action<StarkDouyinCloud.DBResponse> fail);
```

##### 参数说明

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| dataMap | JsonData | - | 是 | 更新的数据 |
| success | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作成功回调 |
| fail | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作失败回调 |

##### 调用示例：

```json
JsonData setData = GetTestDocJson(1);
setData["set_new_field"] = "hello value by TestDbDocSetJson";
StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDBCollection(DY_CLOUD_EVN_ID, DY_CLOYD_DB_NAME)
    .Doc(DyCloudTestDocId).Set(setData,
        response =>
        {
            PrintText(
                $"TestDbDocSet  RawCloudDb response.StatusCode:{response.StatusCode} response.ErrMsg:{response.ErrMsg} ,response.Data:{response.Data.ToJson()}");
        },
        response =>
        {
            PrintText(
                $"TestDbDocSet failed response.StatusCode:{response.StatusCode} response.ErrMsg:{response.ErrMsg}");
        });
```

#### Remove

```json

/// <summary>
///
/// 删除单个云文档数据
/// </summary>
/// <param name="success"></param>
/// <param name="fail"></param>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public void Remove(Action<StarkDouyinCloud.DBResponse> success, Action<StarkDouyinCloud.DBResponse> fail);
```

##### 参数说明

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| success | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作成功回调 |
| fail | Action<StarkDouyinCloud.DBResponse> | - | 是 | 数据库操作失败回调 |

##### 调用示例：

```json
StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDBCollection(DY_CLOUD_EVN_ID, DY_CLOYD_DB_NAME)
    .Doc(DyCloudTestDocId).Remove(
        response =>
        {
            PrintText(
                $"TestDbDocRemove  RawCloudDb response.StatusCode:{response.StatusCode},response.Data:{response.Data.ToJson()}");
        },
        response =>
        {
            PrintText(
                $"TestDbDocRemove failed response.StatusCode:{response.StatusCode},response.ErrMsg:{response.ErrMsg}");
        });
```

## CloudDBCommand
CloudDBCollection 提供的Where 查询仅可以做 Eq 查询， 无法做复杂的条件查询， 使用 CloudDBCommand 就可以做 > < = != And Or 这些复杂的查询

#### GenDbCmd
基于字段名 创建 DbCmd 对象， 后续的cmd 都是基于此字段的操作
##### API

```json
/// <summary>
///
/// 基于字段名 创建 DbCmd 对象， 后续的cmd 都是基于此字段的操作
/// </summary>
/// <param name="name"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBCommand GenDbCmd(string name);
```

##### 参数说明

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | - | 是 | 数据库 doc 字段名 |

##### 调用示例：
以下语句可以类比为 num_int<3

```json
// 创建查询条件
CloudDBCommand cmd1 = StarkSDK.API.GetStarkDouyinCloudManager().CloudDb()
.GenDbCmd("num_int").Lt(3))

CloudDBCollection cloudDBCollection = StarkSDK.API.GetStarkDouyinCloudManager().CloudDb()
    .GenDBCollection(DY_CLOUD_EVN_ID, DY_CLOYD_DB_NAME);
    
// DBCollection 加入查询调整， 可以同时添加多个查询条
cloudDBCollection.AddWhereCmd(cmd1);
cloudDBCollection.AddWhereCmd(cmd2);
cloudDBCollection.AddWhereCmd(cmd3);
```

#### Eq
查询筛选条件，表示字段等于某个值
##### API

```json
/// <summary>
/// 数据库操作符 = 
/// </summary>
/// <param name="para"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBCommand Eq(object para);
```

##### 参数说明

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| para | object | - | 是 | 表示等于的数据， 可以是 number, boolean, string 这些基本数据类型 |

#### 调用示例：
以下语语句可以类比为 num_int=3

```json
StarkSDK.API.GetStarkDouyinCloudManager().CloudDb()
.GenDbCmd("num_int").Eq(3))
```

#### Neq
查询筛选条件，表示字段不等于某个值。
##### API

```json
/// <summary>
/// 数据库操作符 !=
/// </summary>
/// <param name="para"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBCommand Neq(object para);
```

##### 参数说明

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| para | object | - | 是 | 表示等于的数据， 可以是 number, boolean, string 这些基本数据类型 |

##### 调用示例：
以下语句可以类比为 num_int=3

```json
StarkSDK.API.GetStarkDouyinCloudManager().CloudDb()
.GenDbCmd("num_int").Neq(3))
```

#### Lt
查询筛选操作符，表示需小于指定值。可以传入 Date 对象用于日期比较。
##### API

```json
/// <summary>
/// 数据库操作符 <
/// </summary>
/// <param name="para"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBCommand Lt(object para);
```

##### 参数说明

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| para | object | - | 是 | 表示等于的数据， 可以是 number, boolean, string 这些基本数据类型 |

##### 调用示例：
以下语句可以类比为 num_int<3

```json
StarkSDK.API.GetStarkDouyinCloudManager().CloudDb()
.GenDbCmd("num_int").Lt(3))
```

#### Lte
查询筛选操作符，表示需小于或等于指定值。可以传入 Date 对象用于进行日期比较。
##### API

```json
/// <summary>
/// 数据库操作符 <=
/// </summary>
/// <param name="para"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBCommand Lte(object para);
```

##### 调用示例：
以下语句可以类比为 num_int<=3

```json
StarkSDK.API.GetStarkDouyinCloudManager().CloudDb()
.GenDbCmd("num_int").Lte(3))
```

#### Gt
查询筛选操作符，表示需大于指定值。可以传入 Date 对象用于进行日期比较。
##### API

```json
/// <summary>
/// 数据库操作符 >
/// </summary>
/// <param name="para"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBCommand Gt(object para);
```

##### 调用示例：
以下语句可以类比为 num_int>3

```json
StarkSDK.API.GetStarkDouyinCloudManager().CloudDb()
.GenDbCmd("num_int").Gt(3))
```

#### Gte
查询筛选操作符，表示需大于或等于指定值。
##### API

```json
/// <summary>
/// 数据库操作符 >= 
/// </summary>
/// <param name="para"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBCommand Gte(object para);
```

##### 调用示例：
以下语句可以类比为 num_int>=3

```json
StarkSDK.API.GetStarkDouyinCloudManager().CloudDb()
.GenDbCmd("num_int").Gte(3))
```

#### In
查询筛选操作符，表示要求值在给定的数组内。
##### API

```json
/// <summary>
/// 数据库操作符 in
/// </summary>
/// <param name="para"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBCommand In(List<object> listData);
```

##### 参数说明

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listData | List<object> | - | 是 | object 可以是 number, boolean, string 这些基本数据类型 |

##### 调用示例：
以下语句可以类比为 num_int in (2, 3,4, 5, 111)

```json
List<object> inData = new List<object>();
inData.Add(2);
inData.Add(3);
inData.Add(4);
inData.Add(5);
inData.Add(111);
cmdList.Add(StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDbCmd("num_int").In(inData));
```

#### NIn
查询筛选操作符，表示要求值不在给定的数组内。
##### API

```json
/// <summary>
/// 数据库操作符 not in
/// </summary>
/// <param name="para"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBCommand NIn(List<object> listData);
```

##### 参数说明

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listData | List<object> | - | 是 | object 可以是 number, boolean, string 这些基本数据类型 |

调用示例：
以下语句可以类比为 num_int not in (2, 3,4, 5, 111)

```json
List<object> inData = new List<object>();
inData.Add(2);
inData.Add(3);
inData.Add(4);
inData.Add(5);
inData.Add(111);
cmdList.Add(StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDbCmd("num_int").NIn(inData));
```

#### 逻辑语句查询
逻辑语句， 用于多个 CloudDBCommand 对象之间组合
如 num_int> 10 and num_int< 100 and num_int in (12, 13, 1,5) 这样组合Sql 语句
#### And
查询操作符，用于表示逻辑 "与" 的关系，表示需同时满足多个查询筛选条件。
##### API

```json
/// <summary>
/// 数据库操作符 And
/// </summary>
/// <param name="listData"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBCommand And(List<CloudDBCommand> listData);
```

##### 参数说明

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listData | List<CloudDBCommand> | - | 是 | 表示 一组 CloudDBCommand 用And 条件查询 |

调用示例：

```json
// 创建一个 andCmd 对象， 这个对象的参数为空 
CloudDBCommand andCmd1 = StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDbCmd("");
List<CloudDBCommand> andCmdList1 = new List<CloudDBCommand>();
andCmdList1.Add(StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDbCmd("num_int").Eq(5));
andCmdList1.Add(StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDbCmd("num_double").Eq(5.1));

// andCmdList1 列表中的 条件都做 And 操作
andCmd1.And(andCmdList1);

andCmd1 可以传递给cloudDBCollection去做查询操作
cloudDBCollection.AddWhereCmd(andCmd1);
```

#### Or
查询操作符，用于表示逻辑 "或" 的关系，或指令有两种用法，一是可以进行字段值的 “或” 操作，二是也可以进行跨字段的 “或” 操作。
##### API

```json
/// <summary>
/// 数据库操作符 Or
/// </summary>
/// <param name="listData"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBCommand Or(List<CloudDBCommand> listData);
```

##### 参数说明

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listData | List<CloudDBCommand> | - | 是 | 表示 一组 CloudDBCommand 用OR 条件查询 |

##### 调用示例：

```json
// 创建一个 andCmd 对象， 这个对象的参数为空 
CloudDBCommand cmd1 = StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDbCmd("");
List<CloudDBCommand> andCmdList1 = new List<CloudDBCommand>();
andCmdList1.Add(StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDbCmd("num_int").Eq(5));
andCmdList1.Add(StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDbCmd("num_double").Eq(5.1));

// andCmdList1 列表中的 条件都做 Or 操作
cmd1.Or(andCmdList1);

cmd1 可以传递给cloudDBCollection去做查询操作
cloudDBCollection.AddWhereCmd(cmd1);
```

#### Nor
查询操作符，用于表示逻辑 "都不" 的关系，表示需不满足指定的所有条件。如果记录中没有对应的字段，则默认满足条件。

##### API

```json
/// <summary>
/// 数据库操作 Not or
/// </summary>
/// <param name="listData"></param>
/// <returns></returns>
[StarkVersion(MinSCAndroidVersion = "5.45.0", IsSupportWebGL = true)]
public CloudDBCommand Nor(List<CloudDBCommand> listData);
```

##### 参数说明

| 参数 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| listData | List<CloudDBCommand> | - | 是 | 表示 一组 CloudDBCommand 用NOR 条件查询 |

##### 调用示例：

```json
List<CloudDBCommand> norCmdList2 = new List<CloudDBCommand>();
norCmdList2.Add(StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDbCmd("num_int").Eq(5));
norCmdList2.Add(StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDbCmd("num_int").Eq(7));
CloudDBCommand norCmd2 = StarkSDK.API.GetStarkDouyinCloudManager().CloudDb().GenDbCmd("");

// andCmdList1 列表中的 条件都做 Nor 操作
norCmd2.Nor(norCmdList2);

norCmd2 可以传递给cloudDBCollection去做查询操作
cloudDBCollection.AddWhereCmd(norCmd2);
```
