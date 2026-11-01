---
title: "FileSystemManager.getFileInfo"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-get-file-info
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.getFileInfo(filePath)
```
基础库 1.15.0 开始支持本方法，这是一个**异步**方法。
获取 临时目录 (ttfile://tmep) 或 用户目录 (ttfile://user) 下的文件信息。

## 示例代码
```js
const fileSystemManager = tt.getFileSystemManager();

tt.chooseImage({
  success(res) {
    getFileInfo(res.tempFilePaths[0]);
  },
});

function getFileInfo(filePath) {
  fileSystemManager.getFileInfo({
    filePath,
    success(res) {
      console.log("文件信息:", res);
    },
    fail(res) {
      console.log("调用失败", res.errMsg);
    },
  });
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| filePath | string | 是 |  | 1.15.0 | 要读取的文件路径 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **size**（number）：文件大小，以字节为单位 - **errMsg**（string）："FileSystemManager.getFileInfo:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.getFileInfo:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 21101 | permission denied, $apiName $filePath |  |  |
| 21102 | no such file or directory, $apiName $filePath |  |  |
| 21103 | operation not permitted, $apiName $filePath |  |  |
| 10401 | Internal error:sandbox is nil |  |  |
| 20000 | params $paramName is required |  |  |
| 20000 | params $paramName type is not $paramType type |  |  |
| 20000 | $paramName is invalid |  |  |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-get-file-info) / [本地体验路径](file-system-manager-get-file-info)
