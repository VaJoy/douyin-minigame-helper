---
title: "FileSystemManager.saveFileSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-save-file-sync
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.saveFileSync(tempFilePath, filePath)
```
基础库 1.15.0 开始支持本方法，这是一个**同步**方法。
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
      const savedFilePath = fileSystemManager.saveFileSync(tempFilePaths[0]);
      console.log(`文件已经从 ${tempFilePaths[0]} 移动到 ${savedFilePath}`);
    }
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| tempFilePath | string | 是 |  | 1.15.0 | 要保存的临时文件地址，临时文件地址必须以 ttfile://temp 开头。 |
| filePath | string | 否 |  | 1.15.0 | 要保存的目标地址，如果没有填写将自动生成一个。 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | string | 保存后的文件地址 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 10401 | error stack |  |  |
| 21101 | permission denied, $apiName $dirPath |  |  |
| 21102 | no such file or directory, $apiName $dirPath |  |  |
| 21105 | operation not permitted, $apiName $filePath |  |  |
| 21103 | user dir saved file size limit exceeded |  |  |
| 20000 | params $paramName is required |  |  |
| 20000 | params $paramName type is not $paramType type |  |  |
| 20000 | $paramName is invalid |  |  |
| 21104 | operation failed |  |  |
| 20000 | internal error |  |  |

## 注意事项
- 该 API 会把临时文件 移动 到用户目录下, 所以在调用成功后原文件路径将访问失败。
- 从 2.21.0 (包含)开始，每个小游戏 ttfile://user 开头的用户目录储存上限从 50M 提升为 200M， 每个小游戏之间储存相互隔离。单个小游戏储存不区分预览版，正式版，统一分配空间额度。
- 卸载宿主(例如头条, 抖音), 或者使用系统的清理功能将清除用户目录内的文件。
- 通过 tt.downloadFile 下载的文件会保存在以 ttfile://temp 开头的临时目录, 临时目录的文件会不定期清理, 如果希望下载的文件永久保留, 则可以通过 saveFile 将文件保存到以 ttfile://user 开头的用户目录下。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android
