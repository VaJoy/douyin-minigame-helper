---
title: "FileSystemManager.write"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/filesystem-write
update_time: 2025-06-30
---

## 语法

```js
FileSystemManager.write(length, position, data, fd, encoding, offset)
```
基础库 3.74.0 开始支持本方法，这是一个**异步**方法。
写入文件

## 示例代码
```js
const fs = tt.getFileSystemManager();
const fd = fs.openSync({
  filePath,
  flag: "w+",
});
fs.write({
  fd,
  data: '测试写入的数据',
  offset: 0,
  length: 10,
  position: 0,
  success: (res) => {
    console.log('文件写入成功', res);
  },
  fail: (err) => {
    console.error('文件写入失败', err);
  }
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| length | number | 否 |  | 3.74.0 | 只在 data 类型是 ArrayBuffer 时有效，指定要写入的字节数，默认为 ArrayBuffer 从0开始偏移 offset 个字节后剩余的字节数 |
| position | number | 否 |  | 3.74.0 | 指定文件开头的偏移量，即数据要被写入的位置。当 position 不传或者传入非 Number 类型的值时，数据会被写入当前指针所在位置 |
| data | string \| Arraybuffer | 是 |  | 3.74.0 | 写入的内容，类型为 String 或 ArrayBuffer |
| fd | string | 是 |  | 3.74.0 | 文件描述符。fd 通过 FileSystemManager.open 或 FileSystemManager.openSync 接口获得 |
| encoding | number | 否 | utf8 | 3.74.0 | 只在 data 类型是 String 时有效，指定写入文件的字符编码，默认为 utf8  **可选值：** ascii=ascii；base64=base64；binary=binary；hex=hex；ucs2=以小端序读取；ucs-2=以小端序读取；utf16le=以小端序读取；utf-16le=以小端序读取；utf-8=utf-8；utf8=utf8；latin1=latin1 |
| offset | number | 否 | 0 | 3.74.0 | 只在 data 类型是 ArrayBuffer 时有效，决定 ArrayBuffer 中要被写入的部位，即 ArrayBuffer 中的索引，默认0 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.write:ok" - **bytesWritten**（number）：实际被写入到文件中的字节数（被写入的字节数不一定与被写入的字符串字符数相同） |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.write:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 21100 | bad file descriptor |  |  |
| 21101 | system error |  |  |
| 21102 | the maximum size of the file storage limit is exceeded |  |  |
| 21103 | ${encoding} encode error |  |  |
| 21104 | data to write is empty |  |  |
| 21105 | illegal operation on a directory |  |  |
| 21106 | value of length is out of range |  |  |
| 21107 | value of offset is out of range |  |  |
| 21108 | invalid fd |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/file-system-manager-write) / [本地体验路径](file-system-manager-write)
