---
title: "FileSystemManager.openSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/filesystem-opensync
update_time: 2025-06-30
---

## 语法

```js
FileSystemManager.openSync(params)
```
基础库 3.74.0 开始支持本方法，这是一个**同步**方法。
打开文件，返回文件描述符

## 示例代码
```js
try {
  const fs = tt.getFileSystemManager();
  const fd = fs.openSync({
    filePath: tempFilePath,
    flag: "r",
  });
  console.log("fd", fd);
} catch (err) {
  console.log("fail", err);
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| params | Object | 是 |  | 3.74.0 | 入参  **对象字段** - **filePath**（string）：文件路径 - **flag**（number）：文件系统标志，默认值: 'r' |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| fd | string | 文件描述符 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 21100 | no such file or directory ${path} |  |  |
| 21101 | Path permission denied |  |  |
| 21102 | system error |  |  |
| 21103 | illegal operation on a directory |  |  |
| 21104 | illegal operation on a package directory |  |  |
| 21105 | file already exists ${dirPath} |  |  |
| 21106 | excced max concurrent fd limit |  |  |
| 21107 | invalid flag |  |  |
| 21108 | permission denied when open using flag |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/file-system-manager-open-sync) / [本地体验路径](file-system-manager-open-sync)
