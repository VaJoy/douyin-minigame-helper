---
title: "FileSystemManager.readdir"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-readdir
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.readdir(dirPath)
```
基础库 1.15.0 开始支持本方法，这是一个**异步**方法。
读取目录内文件列表。

## 示例代码
```js
const fileSystemManager = tt.getFileSystemManager();

const files = fileSystemManager.readdir({
  dirPath: "ttfile://user/",
  success(res) {
    console.log("调用成功", res.files);
  },
  fail(res) {
    console.log("调用失败", res.errMsg);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| dirPath | string | 是 |  | 1.15.0 | 要读取的目录路径 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **files**（Array<string>）：指定目录下的文件名数组 - **errMsg**（string）："FileSystemManager.readdir:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.readdir:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10401 | error stack |  |  |
| 21101 | permission denied, $apiName $filePath |  |  |
| 21102 | operation not permitted, $apiName $filePath |  |  |
| 21103 | no such file or directory, $apiName $filePath |  |  |
| 20001 | invalid param |  |  |
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
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-readdir) / [本地体验路径](file-system-manager-readdir)
