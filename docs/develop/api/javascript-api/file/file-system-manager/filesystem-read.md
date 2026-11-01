---
title: "FileSystemManager.read"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/filesystem-read
update_time: 2025-06-30
---

## 语法

```js
FileSystemManager.read(position, length, arrayBuffer, fd, offset)
```
基础库 3.74.0 开始支持本方法，这是一个**异步**方法。
读文件

## 示例代码
```js
const fs = tt.getFileSystemManager();
const arrayBuffer = new ArrayBuffer(1024);
fs.read({
  fd,
  arrayBuffer,
  offset: 0,
  position: 0,
  length: 10,
  success: (res) => {
    console.log('文件读取成功', res);
  },
  fail: (err) => {
    console.error('文件读取失败', err);
  }
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| position | number | 否 |  | 3.74.0 | 文件读取的起始位置，如不传或传 null，则会从当前文件指针的位置读取。如果 position 是正整数，则文件指针位置会保持不变并从 position 读取文件。 |
| length | number | 否 | 0 | 3.74.0 | 要从文件中读取的字节数，默认0 |
| arrayBuffer | ArrayBuffer | 是 |  | 3.74.0 | 数据写入的缓冲区，必须是 ArrayBuffer 实例 |
| fd | string | 是 |  | 3.74.0 | 文件描述符。fd 通过 FileSystemManager.open 或 FileSystemManager.openSync 接口获得 |
| offset | number | 否 | 0 | 3.74.0 | 缓冲区中的写入偏移量，默认0 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.readCompressedFile:ok" - **bytesRead**（number）：实际读取的字节数 - **arrayBuffer**（ArrayBuffer）：被写入的缓存区的对象，即接口入参的 arrayBuffer |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.readCompressedFile:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 21100 | bad file descriptor |  |  |
| 21101 | system error |  |  |
| 21102 | illegal operation on a directory |  |  |
| 21103 | value of length is out of range |  |  |
| 21104 | value of offset is out of range |  |  |
| 21105 | value of position is out of range |  |  |
| 21106 | invalid fd |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/file-system-manager-read) / [本地体验路径](file-system-manager-read)
