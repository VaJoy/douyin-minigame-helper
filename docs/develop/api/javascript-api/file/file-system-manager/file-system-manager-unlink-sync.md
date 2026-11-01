---
title: "FileSystemManager.unlinkSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-unlink-sync
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.unlinkSync(filePath)
```
基础库 1.15.0 开始支持本方法，这是一个**同步**方法。
删除文件，只能删除 用户目录(ttfile://user)下的文件。

## 示例代码
```js
const fileSystemManager = tt.getFileSystemManager();

tt.chooseImage({
  success(res) {
    // 保存临时文件到 用户目录
    const savedFilePath = fileSystemManager.saveFileSync(res.tempFilePaths[0]);

    try {
      // 删除文件
      fileSystemManager.unlinkSync(savedFilePath);
      console.log("删除成功");
    } catch (err) {
      console.log("删除失败", err);
    }
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| filePath | string | 是 |  | 1.15.0 | 要删除的文件路径，必须以 ttfile://user 开头。 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 10401 | error stack |  |  |
| 21101 | permission denied, $apiName $dirPath |  |  |
| 21102 | no such file or directory, $apiName $dirPath |  |  |
| 21103 | operation not permitted, $apiName $filePath |  |  |
| 20000 | internal error |  |  |

## 注意事项
filePath 必须以 ttfile://user 开头

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file-system-manager-unlink-sync) / [本地体验路径](file-system-manager-unlink-sync)
