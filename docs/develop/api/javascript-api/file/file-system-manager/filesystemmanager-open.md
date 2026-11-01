---
title: "FileSystemManager.open"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/filesystemmanager-open
update_time: 2025-06-30
---

## 语法

```js
FileSystemManager.open(filePath, flag)
```
基础库 3.74.0 开始支持本方法，这是一个**异步**方法。
打开文件，返回文件描述符

## 示例代码
```js
const fs = tt.getFileSystemManager();
fs.open({
  filePath,
  success: res => {
    console.log('fd', res.fd);
  },
  fail: err => {
    console.log('fail', err);
  }
})
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| filePath | string | 是 |  | 3.73.0 | 文件路径 |
| flag | number | 否 | r | 3.73.0 | 文件系统标志，默认值: 'r'  **可选值：** a=打开文件用于追加。 如果文件不存在，则创建该文件；wx=类似于 'w'，但如果路径存在，则失败；w=打开文件用于写入。 如果文件不存在则创建文件，如果文件存在则截断文件；ax=类似于 'a'，但如果路径存在，则失败；a+=打开文件用于读取和追加。 如果文件不存在，则创建该文件；ax+=类似于 'a+'，但如果路径存在，则失败；as=打开文件用于追加（在同步模式中）。 如果文件不存在，则创建该文件；as+=打开文件用于读取和追加（在同步模式中）。 如果文件不存在，则创建该文件；r=打开文件用于读取。 如果文件不存在，则会发生异常；r+=打开文件用于读取和写入。 如果文件不存在，则会发生异常；w+=打开文件用于读取和写入。 如果文件不存在则创建文件，如果文件存在则截断文件；wx+=类似于 'w+'，但如果路径存在，则失败 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.open:ok" - **fd**（string）：文件描述符 |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.open:fail" + 详细错误信息 |

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
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/file-system-manager-open) / [本地体验路径](file-system-manager-open)
