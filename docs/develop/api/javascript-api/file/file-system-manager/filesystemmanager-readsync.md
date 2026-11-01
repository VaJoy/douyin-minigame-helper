---
title: "FileSystemManager.readSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/filesystemmanager-readsync
update_time: 2025-06-30
---

## 语法

```js
FileSystemManager.readSync(params)
```
基础库 3.74.0 开始支持本方法，这是一个**同步**方法。
读文件

## 示例代码
```js
try {
  const fs = tt.getFileSystemManager();
  const arrayBuffer = new ArrayBuffer(1024);
  const res = fs.readSync({
    fd,
    arrayBuffer,
    offset: 0,
    position: 0,
    length: 10,
  });
  console.log("文件同步读取成功", res);
} catch (err) {
  console.error("文件同步读取失败", err);
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| params | Object | 是 |  | 3.74.0 | 接口参数  **对象字段** - **position**（number）：文件读取的起始位置，如不传或传 null，则会从当前文件指针的位置读取。如果 position 是正整数，则文件指针位置会保持不变并从 position 读取文件。 - **length**（number）：要从文件中读取的字节数，默认 0 - **arrayBuffer**（ArrayBuffer）：数据写入的缓冲区，必须是 ArrayBuffer 实例 - **fd**（string）：文件描述符。fd 通过 FileSystemManager.open 或 FileSystemManager.openSync 接口获得 - **offset**（number）：缓冲区中的写入偏移量，默认 0 |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | 返回值  **对象字段** - **arrayBuffer**（ArrayBuffer）：被写入的缓存区的对象，即接口入参的 arrayBuffer - **bytesRead**（number）：实际读取的字节数 |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/file-system-manager-read-sync) / [本地体验路径](file-system-manager-read-sync)
