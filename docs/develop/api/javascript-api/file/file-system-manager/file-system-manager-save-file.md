---
title: "FileSystemManager.saveFile"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-save-file
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.saveFile(filePath, tempFilePath)
```
基础库 1.15.0 开始支持本方法，这是一个**异步**方法。
保存临时文件到用户目录, 用户目录以 ttfile://user 开头。

## 示例代码
```js
const fileSystemManager = tt.getFileSystemManager();

tt.chooseImage({
  success(res) {
    // 获取图片, chooseImage 获取的文件在临时文件目录内
    const tempFilePaths = res.tempFilePaths;
    if (tempFilePaths[0]) {
      // 保存到用户目录
      saveFile(tempFilePaths[0]);
    }
  },
});

function saveFile(tempFilePath) {
  fileSystemManager.saveFile({
    tempFilePath,
    success(res) {
      console.log(`文件已经从 ${tempFilePath} 移动到 ${savedFilePath}`);
    },
    fail(res) {
      console.log("保存失败", res.errMsg);
    },
  });
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| filePath | string | 否 |  | 1.15.0 | 要存储的路径, 必须以 ttfile://user 开头 |
| tempFilePath | string | 是 |  | 1.15.0 | 文件临时路径 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **savedFilePath**（string）：保存后文件路径 - **errMsg**（string）："saveFile:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："saveFile:fail " + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 10401 | error stack |  |  |
| 21101 | permission denied, $apiName $dirPath |  |  |
| 21102 | no such file or directory, $apiName $dirPath |  |  |
| 21103 | user dir saved file size limit exceeded |  |  |
| 21105 | operation not permitted, $apiName $filePath |  |  |
| 20000 | params $paramName is required |  |  |
| 20000 | params $paramName type is not $paramType type |  |  |
| 20000 | $paramName is invalid |  |  |
| 21104 | operation failed |  |  |
| 20000 | internal error |  |  |

## 注意事项
- 该 API 会把临时文件 **移动** 到用户目录, 所以在调用成功后原文件路径将访问失败。
- 从 2.21.0 (包含)开始，每个小游戏 ttfile://user 开头的用户目录储存上限从 50M 提升为 200M， 每个小游戏之间储存相互隔离。单个小游戏储存不区分预览版，正式版，统一分配空间额度。
- 卸载宿主(例如头条, 抖音), 或者使用系统的清理功能将清除用户目录内的文件。
- 通过 tt.downloadFile 下载的文件, tt.chooseImage 选择的文件会保存在以 ttfile://temp 开头的临时目录, 临时目录的文件会不定期清理, 如果希望下载的文件永久保留, 则可以通过 saveFile 将文件保存到以 ttfile://user 开头的用户目录下

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
