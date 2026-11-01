---
title: "FileSystemManager.renameSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-rename-sync
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.renameSync(oldPath, newPath)
```
基础库 1.15.0 开始支持本方法，这是一个**同步**方法。
重命名文件，可以把文件从 oldPath 移动到 newPath。

## 示例代码
```js
const fileSystemManager = tt.getFileSystemManager();

fileSystemManager.getSavedFileList({
  success(res) {
    res.fileList.forEach(removeExt);
  },
  fail(res) {
    console.log("获取失败", res.errMsg);
  },
});

/**
 * @param {*} fileItem
 * @param {string} fileItem.filePath
 * @param {number} fileItem.createTime
 * @param {number} fileItem.size
 */
function removeExt(fileItem) {
  console.log(`移除 ${fileItem.filePath} 的 ext`);
  const newPath = fileItem.filePath.replace(/(\..+)?$/, "");

  try {
    fileSystemManager.renameSync(fileItem.filePath, newPath);
    console.log("重命名成功");
  } catch (err) {
    console.log("重命名失败", err);
  }
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| oldPath | string | 是 |  | 1.15.0 | 必须以 ttfile://user 开头 源文件路径，可以是普通文件或目录 |
| newPath | string | 是 |  | 1.15.0 | string 类型, 必须以 ttfile://user 开头 新文件路径 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 10401 | error stack |  |  |
| 21101 | permission denied, $apiName $oldPath -> $newPath |  |  |
| 21102 | no such file or directory, $apiName $oldPath -> $newPath |  |  |
| 21103 | operation not permitted, $apiName $filePath |  |  |
| 21104 | user dir saved file size limit exceeded |  |  |
| 20000 | params $paramName is required |  |  |
| 20000 | params $paramName type is not $paramType type |  |  |
| 20000 | $paramName is invalid |  |  |
| 21105 | operation failed |  |  |
| 20000 | internal error |  |  |

## 注意事项
因为开发者只有在 ttfile://user 目录下才有写的权限, 因此 rename 只能在用户目录下进行。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-rename-sync) / [本地体验路径](file-system-manager-rename-sync)
