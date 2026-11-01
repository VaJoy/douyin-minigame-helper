---
title: "FileSystemManager.rmdir"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-rmdir
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.rmdir(recursive, dirPath)
```
基础库 1.15.0 开始支持本方法，这是一个**异步**方法。
删除目录, 只能是 ttfile://user 下的目录。

## 示例代码
```js
const fileSystemManager = tt.getFileSystemManager();

// 先创建一个目录
const examplePath = "ttfile://user/example-dir";

try {
  fileSystemManager.mkdirSync(examplePath);
  console.log("创建成功");
} catch (err) {
  console.log("创建失败", err);
}

// 删除文件
fileSystemManager.rmdir({
  dirPath: examplePath,
  success(_res) {
    console.log("创建成功");
  },
  fail(res) {
    console.log("创建失败", res.errMsg);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| recursive | boolean | 否 |  | 1.15.0 | 是否递归删除目录下的文件，false 的情况下只能删除空目录 |
| dirPath | string | 是 |  | 1.15.0 | 要删除的目录路径， 必须以 ttfile://user 开头 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.rmdir:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.rmdir:fail" + 详细错误信息 |

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
开发者只能删除 ttfile://user 下的目录。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-rmdir) / [本地体验路径](file-system-manager-rmdir)
