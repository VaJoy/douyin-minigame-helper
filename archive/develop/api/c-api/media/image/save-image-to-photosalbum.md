---
title: "SaveImageToPhotosAlbum"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/media/image/save-image-to-photosalbum
update_time: 2025-07-31
---

## TT.SaveImageToPhotosAlbum
> 6.4.4 开始支持本方法
保存图片到系统相册

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 手动取消也会触发失败回调，回调参数为 saveImageToPhotosAlbum:fail cancel，可以通过判断详细错误信息区分取消和其他错误。 |
| 相关教程 | 无 |

### **语法 **

```text
public static void SaveImageToPhotosAlbum(TTSaveImageToPhotosAlbumParam param)
```

### 参数说明
TTSaveImageToPhotosAlbumParam包含以下参数

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| filePath | string |  | 是 | 图片文件路径，可以用于用户目录 (ttfile://user)、临时目录(ttfile://temp) ，不支持网络路径 |
| success | Action<string> | null | 否 | 成功回调 |
| fail | Action<string> | null | 否 | 失败回调 |
| complete | Action | null | 否 | 完成回调 |

### 代码示例

```csharp
public void Test(){
    string image_path = "ttfile://user/example.png";
    TT.SaveImageToPhotosAlbum(new TTSaveImageToPhotosAlbumParam
    {
        filePath = image_path,
        success = (result) =>
        {
            string resultOutput = "Success, message: " + result;
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
