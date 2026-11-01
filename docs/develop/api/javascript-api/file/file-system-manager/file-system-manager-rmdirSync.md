---
title: "FileSystemManager.rmdirSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-rmdirSync
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.rmdirSync(dirPath, recursive)
```
基础库 1.15.0 开始支持本方法，这是一个**同步**方法。
删除目录，开发者只能删除 用户目录(ttfile://user) 下的目录。

## 示例代码
```js
const fileSystemManager = tt.getFileSystemManager();
// 必须以 "ttfile://user" 开头
const exmaplePath = "ttfile://user/example-dir";
try {
  fileSystemManager.mkdirSync(exmaplePath);
  console.log("成功");
} catch (err) {
  console.log("失败", err);
}
try {
  fileSystemManager.rmdirSync(exmaplePath);
  console.log("成功");
} catch (err) {
  console.log("失败", err);
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| dirPath | string | 是 |  | 1.15.0 | 要删除的目录路径， 必须以 ttfile://user 开头的字符串 |
| recursive | boolean | 否 |  | 1.15.0 | 是否递归删除目录下的文件 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 10401 | error stack |  |  |
| 21101 | permission denied, $apiName $dirPath |  |  |
| 21102 | no such file or directory, $apiName $dirPath |  |  |
| 21103 | directory not empty |  |  |
| 21105 | operation not permitted, $apiName $filePath |  |  |
| 20000 | params $paramName is required |  |  |
| 20000 | params $paramName type is not $paramType type |  |  |
| 20000 | $paramName is invalid |  |  |
| 21104 | remove path |  |  |
| 20000 | internal error |  |  |

## 注意事项
开发者只能删除 ttfile://user 下的目录

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-rmdir-sync) / [本地体验路径](file-system-manager-rmdir-sync)
