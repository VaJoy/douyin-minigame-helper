---
title: "FileSystemManager.readZipEntry"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-read-zip-entry
update_time: 2025-06-05
---

tt.readZipEntry(options);

const fs = tt.getFileSystemManager();
// 读取压缩包内所有文件
fs.readZipEntry({
filePath: "zipPath",
entries: "all",
encoding: "utf8",
success(res) {
console.log("读取压缩包内所有文件成功", res);
},
fail(res) {
console.log("读取压缩包内所有文件失败", res);
},
});

// 读取压缩包内指定文件
fs.readZipEntry({
filePath: "zipPath",
entries: [
{
path: "zipEntryPath1",
},
{
path: "zipEntryPath2",
encoding: "utf8",
},
],
success(res) {
console.log("读取指定压缩文件成功", res);
},
fail(res) {
console.log("读取指定压缩文件失败", res);
},
});

## 语法

```js
FileSystemManager.readZipEntry(encoding, filePath, entries)
```
基础库 2.90.0 开始支持本方法，这是一个**异步**方法。
读取压缩包内的文件。

## 示例代码
```js
const fs = tt.getFileSystemManager();
// 读取压缩包内所有文件
fs.readZipEntry({
  filePath: "zipPath",
  entries: "all",
  encoding: "utf8",
  success(res) {
    console.log("读取压缩包内所有文件成功", res);
  },
  fail(res) {
    console.log("读取压缩包内所有文件失败", res);
  },
});

// 读取压缩包内指定文件
fs.readZipEntry({
  filePath: "zipPath",
  entries: [
    {
      path: "zipEntryPath1",
    },
    {
      path: "zipEntryPath2",
      encoding: "utf8",
    },
  ],
  success(res) {
    console.log("读取指定压缩文件成功", res);
  },
  fail(res) {
    console.log("读取指定压缩文件失败", res);
  },
});
const fs = tt.getFileSystemManager();
// 读取压缩包内所有文件
fs.readZipEntry({
  filePath: "zipPath",
  entries: "all",
  encoding: "utf8",
  success(res) {
    console.log("读取压缩包内所有文件成功", res);
  },
  fail(res) {
    console.log("读取压缩包内所有文件失败", res);
  },
});

// 读取压缩包内指定文件
fs.readZipEntry({
  filePath: "zipPath",
  entries: [
    {
      path: "zipEntryPath1",
    },
    {
      path: "zipEntryPath2",
      encoding: "utf8",
    },
  ],
  success(res) {
    console.log("读取指定压缩文件成功", res);
  },
  fail(res) {
    console.log("读取指定压缩文件失败", res);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| encoding | number | 否 |  | 2.90.0 | 统一指定读取文件的字符编码，只在 entries 值为"all"时有效。如果 entries 值为"all"且不传 encoding，则以 ArrayBuffer 格式读取文件的二进制内容  **可选值：** ascii=-；base64=-；binary=-；hex=-；ucs2=以小端序读取；ucs-2=以小端序读取；utf16le=以小端序读取；utf-16le=以小端序读取；utf-8=-；utf8=-；latin1=- |
| filePath | string | 是 |  | 2.90.0 | 要读取的压缩包的路径 (本地路径) |
| entries | Array<Object> | 是 |  | 2.90.0 | 要读取的压缩包内的文件列表（当传入"all" 时表示读取压缩包内所有文件）  Array<object> \| 'all' 类型，传入 object 时属性如下：  \|  \|  \|  \|  \|  \| \| --- \| --- \| --- \| --- \| --- \| \| 属性名 \| 类型 \| 默认值 \| 必填 \| 说明 \| \| path \| string \|  \| 是 \| 压缩包内文件路径，**entries中对象之间的path不可重复** \| \| encoding \| string \|  \| 否 \| 指定读取文件的字符编码，如果不传 encoding，则以 ArrayBuffer 格式读取文件的二进制内容 \| |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **entries**（Object）：文件读取结果。entries 是一个对象，key是文件路径，value是一个对象 FileItem ，表示该文件的读取结果。每个 FileItem 包含 data （文件内容） 和 errMsg （错误信息） 属性。 - **errMsg**（string）："FileSystemManager.readZipEntry:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.readZipEntry:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 10401 | error stack |  |  |
| 21101 | permission denied, $apiName $dirPath |  |  |
| 21102 | no such file or directory, $apiName $dirPath |  |  |
| 21103 | operation not permitted, $apiName $filePath |  |  |
| 21106 | unzip open file fail |  |  |
| 20001 | option.entries.path should not be repeated |  |  |
| 21103 | no such file or directory, $apiName $filePath |  |  |
| 21102 | operation not permitted, $apiName $filePath |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-read-zip-entry) / [本地体验路径](file-system-manager-read-zip-entry)
