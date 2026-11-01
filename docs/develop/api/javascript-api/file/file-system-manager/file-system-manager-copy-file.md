---
title: "FileSystemManager.copyFile"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-copy-file
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.copyFile(srcPath, destPath)
```
基础库 1.15.0 开始支持本方法，这是一个**异步**方法。
复制文件。

## 示例代码
```js
const fileSystemManager = tt.getFileSystemManager();

tt.chooseImage({
  success(res) {
    copyFile(res.tempFilePaths[0], `ttfile://user/my-pic`);
  },
  fail(res) {
    console.log("下载失败", res.errMsg);
  },
});

function copyFile(srcPath, destPath) {
  fileSystemManager.copyFile({
    srcPath,
    destPath,
    success(_res) {
      console.log("拷贝成功");
    },
    fail(res) {
      console.log("拷贝失败", res.errMsg);
    },
  });
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| srcPath | string | 是 |  | 1.15.0 | 源文件路径，只可以是普通文件，不能是目录 |
| destPath | string | 是 |  | 1.15.0 | 目标文件路径, 必须以 ttfile://user 开头 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.copyFile:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.copyFile:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10401 | error stack |  |  |
| 21101 | permission denied, $apiName $srcPath -> $destPath |  |  |
| 21102 | operation not permitted, $apiName $srcPath |  |  |
| 21103 | no such file or directory, $apiName $srcPath -> $destPath |  |  |
| 21104 | user dir saved file size limit exceeded |  |  |
| 20001 | invalid param |  |  |
| 20000 | params $paramName is required |  |  |
| 20000 | params $paramName type is not $paramType type |  |  |
| 20000 | $paramName is invalid |  |  |
| 20000 | no such file or directory, $apiName $filePath |  |  |
| 21105 | operation failed |  |  |
| 20000 | internal error |  |  |

## 注意事项
- srcPath 值和 destPath 必须对等。如果 srcPath 是文件路径，destPath 就要是文件路径。目前不支持目录拷贝。
- 当拷贝源路径为文件时，目标也是要是个文件路径，例如，源：ttfile://user/test1.zip，那么目标可以是 ttfile://user/test2.zip， 这里 test2.zip 为开发者定义的拷贝后目标文件名字。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-copy-file) / [本地体验路径](file-system-manager-copy-file)
