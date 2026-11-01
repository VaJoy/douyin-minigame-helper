---
title: "FileSystemManager.removeSavedFile"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-remove-saved-file
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.removeSavedFile(filePath)
```
基础库 1.15.0 开始支持本方法，这是一个**异步**方法。
删除该小游戏下用户目录内的文件，用户目录以 ttfile://user 开头。

## 示例代码
```js
const fileSystemManager = tt.getFileSystemManager();

fileSystemManager.getSavedFileList({
  success(res) {
    console.log("当前用户目录下的文件:", res.fileList);
    removeSavedFile(res.fileList);
  },
});

function removeSavedFile(fileList) {
  fileList.forEach((filePath) => {
    fileSystemManager.removeSavedFile({
      filePath,
      success(res) {
        console.log(`${filePath} 删除成功`);
      },
      fail(res) {
        console.error(`${filePath} 删除失败`, res.errMsg);
      },
    });
  });
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| filePath | string | 是 |  | 1.15.0 | 要删除的文件路径，必须以 ttfile://user 开头 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.removeSavedFile:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.removeSavedFile:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 21101 | permission denied, %s%s |  |  |
| 21102 | no such file or directory, $apiName $filePath |  |  |
| 21104 | operation not permitted, %s%s |  |  |
| 10401 | Internal error:sandbox is nil |  |  |
| 20000 | params $paramName is required |  |  |
| 20000 | params $paramName type is not $paramType type |  |  |
| 20000 | $paramName is invalid |  |  |
| 21104 | no such file or directory, $apiName $filePath |  |  |
| 21103 | permission denied, %s%s |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-remove-saved-file) / [本地体验路径](file-system-manager-remove-saved-file)
