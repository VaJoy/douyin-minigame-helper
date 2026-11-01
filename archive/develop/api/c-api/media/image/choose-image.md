---
title: "chooseImage"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/c-api/media/image/choose-image
update_time: 2025-07-31
---

## TT.ChooseImage
> 6.4.4 开始支持本方法
从系统相册中选择图片，或使用相机拍摄图片，选取成功后将存入本地临时文件，并在 success 回调中返回相应路径列表。

| 前提条件 | 无 |
| --- | --- |
| 业务背景 | 无 |
| 使用限制 | 无 |
| 注意事项 | Android 上所选图片总大小不能超过 180M。 手动取消也会触发失败回调，回调参数为 chooseImage:fail cancel，可以通过判断详细错误信息区分取消和其他错误。 |
| 相关教程 | 无 |

### **语法 **

```text
public static void ChooseImage(TTChooseImageParam param)
```

### 参数说明
TTChooseImageParam包含以下参数

| 属性名 | 类型 | 默认值 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| count | int | 9 | 否 | 最多可以选择的图片张数 |
| sourceType | string[] | { "album", "camera" } | 否 | 指定图片来源，album 从相册选图，camera 使用相机，默认二者都有 |
| success | Action<TTChooseImageSuccessCallbackResult> | null | 否 | 成功回调 |
| fail | Action<string> | null | 否 | 失败回调 |
| complete | Action | null | 否 | 完成回调 |

TTChooseImageSuccessCallbackResult包含以下变量

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| tempFiles | TTImageFile[] | 选择的图片列表，为本地临时路径 |
| tempFilePaths | string[] | 选择的图片路径 |
| errMsg | string | "chooseImage:ok" |

TTImageFile包含以下变量

| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| path | string | 本地临时路径 |
| size | double | 图片大小，单位为字节 |

### 代码示例

```text
public void Test(){
    TT.ChooseImage(new TTChooseImageParam
    {
        count = 9,
        sourceType = { "album", "camera" },
        success = (result) =>
        {
            string resultOutput = "Success, message: " + result.errMsg;
            Debug.Log(resultOutput);
            foreach (var file in result.tempFiles)
            {
                Debug.Log(file.path);
            }
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
