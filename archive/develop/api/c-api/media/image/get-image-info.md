---
title: "GetImageInfo"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/media/image/get-image-info
update_time: 2025-07-31
---

## TT.GetImageInfo
> 6.4.4 开始支持本方法
获取图片信息。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 无 |
| 相关教程 | 无 |

### **语法 **

```text
public static void GetImageInfo(TTGetImageInfoParam param)
```

### 参数说明
TTGetImageInfoParam包含以下参数

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| src | string | null | 是 | 图片路径，可以是相对路径、临时文件路径或存储文件路径、网络图片 |
| success | Action<TTGetImageInfoSuccessCallbackResult> | null | 否 | 成功回调 |
| fail | Action<string> | null | 否 | 失败回调 |
| complete | Action | null | 否 | 完成回调 |

TTGetImageInfoSuccessCallbackResult包含以下变量

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| path | string | 返回图片的本地路径，若为网络图片则该 API 首先会下载图片再返回下载到本地后的临时路径 |
| type | string | 图片格式 |
| width | double | 图片宽度，单位px |
| height | double | 图片高度，单位px |
| errMsg | string | "getImageInfo:ok" |

### 代码示例

```csharp
public void Test(){
    string image_path = "ttfile://user/example.png";
    TT.GetImageInfo(new TTGetImageInfoParam
    {
        src = image_path,
        success = (result) =>
        {
            string resultOutput = "Success, message: " + result.errMsg + ", width: " + result.width + ", height: " + result.height;
            Debug.Log(resultOutput);
        },
        fail = (msg) =>
        {
            Debug.Log("Fail, message: " + msg);
        },
        complete = () =>
        {
            Debug.Log("Complete");
        }
    });
}
```
