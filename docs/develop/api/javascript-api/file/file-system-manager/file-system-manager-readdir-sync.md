---
title: "FileSystemManager.readdirSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-readdir-sync
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.readdirSync(dirPath)
```
基础库 1.15.0 开始支持本方法，这是一个**同步**方法。
读取目录内文件列表。

## 示例代码
```js
const fileSystemManager = tt.getFileSystemManager();

try {
  const files = fileSystemManager.readdirSync("ttfile://user/");
  console.log("调用成功", files);
} catch (err) {
  console.log("调用失败", err);
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| dirPath | string | 是 |  | 1.15.0 | 要读取的目录路径 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | Array<string> | 指定目录下的文件名数组，类型为 Array<string> |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 10401 | error stack |  |  |
| 21101 | permission denied, $apiName $filePath |  |  |
| 21102 | operation not permitted, $apiName $filePath |  |  |
| 21103 | no such file or directory, $apiName $filePath |  |  |
| 20000 | params $paramName is required |  |  |
| 20000 | params $paramName type is not $paramType type |  |  |
| 20000 | $paramName is invalid |  |  |
| 21104 | * |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-readdir-sync) / [本地体验路径](file-system-manager-readdirsync)
