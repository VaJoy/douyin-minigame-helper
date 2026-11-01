---
title: "PreviewImage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/media/image/preview-image
update_time: 2025-07-31
---

## TT.PreviewImage
> 6.4.4 开始支持本方法
预览一组网络图片。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | 抖音不支持预览图片保存功能。 当 urls 中存在多个相同的图片地址，预览时会选择 current 地址对应的第一张图片进行展示，可通过给图片地址增加 query 或 hash 值避免地址重复。 图片地址必须以https或http开头。 |
| 相关教程 | 无 |

### **语法 **

```text
public static void PreviewImage(TTPreviewImageParam param)
```

### 参数说明
TTPreviewImageParam包含以下参数

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| current | string | null | 否 | 当前显示图片的链接，不填则默认为 urls 中的第一张 |
| urls | string[] | null | 是 | 需要预览的图片链接列表，链接必须以https或http开头 |
| success | Action<string> | null | 否 | 成功回调 |
| fail | Action<string> | null | 否 | 失败回调 |
| complete | Action | null | 否 | 完成回调 |

### 代码示例

```csharp
public void Test(){
    string[] image_path = {"https://a/test/image/example.png"};
    TT.PreviewImage(new TTPreviewImageParam
    {
        urls = image_path,
        current = "",
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
