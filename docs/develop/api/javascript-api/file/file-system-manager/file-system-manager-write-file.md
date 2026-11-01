---
title: "FileSystemManager.writeFile"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-write-file
update_time: 2025-06-05
---

FileSystemManager.writeFile(options)

const fileSystemManager = tt.getFileSystemManager();

const filePath = `ttfile://user/example.txt`;

fileSystemManager.writeFile({
filePath,
encoding: "utf8",
data: "example content",
success(_res) {
console.log("调用成功");
const data = fileSystemManager.readFileSync(filePath);
console.log("写入的内容为:", data);
},
fail(res) {
console.log("调用失败", res.errMsg);
},
});

## 语法

```js
FileSystemManager.writeFile(filePath, data, encoding)
```
基础库 1.15.0 开始支持本方法，这是一个**异步**方法。
写文件，只能写入用户目录(ttfile://user)。

## 示例代码
```js
const fileSystemManager = tt.getFileSystemManager();
const filePath = `ttfile://user/example.txt`;
fileSystemManager.writeFile({
  filePath,
  encoding: "utf8",
  data: "example content",
  success(_res) {
    console.log("调用成功");
    const data = fileSystemManager.readFileSync(filePath);
    console.log("写入的内容为:", data);
  },
  fail(res) {
    console.log("调用失败", res.errMsg);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| filePath | string | 是 |  | 1.15.0 | 要写入的文件路径, 必须以 ttfile://user 开头 |
| data | string | 是 |  | 1.15.0 | string 或 ArrayBuffer 类型。要写入的文本或二进制数据 |
| encoding | number | 否 | utf8 | 1.15.0 | 指定写入文件的字符编码  **可选值：** ascii=-；base64=-；binary=二进制；hex=十六进制；ucs2=以小端序读取；ucs-2=以小端序读取；utf16le=以小端序读取；utf-8/utf8=utf8 格式；latin1=- |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errMsg | string | "writeFile:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| errNo | number | 错误码 |
| errMsg | string | "writeFile:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 10401 | error stack |  |  |
| 21101 | permission denied, $apiName $dirPath |  |  |
| 21102 | no such file or directory, $apiName $dirPath |  |  |
| 21103 | user dir saved file size limit exceeded |  |  |
| 20000 | internal error |  |  |

## 注意事项
filePath 必须以 ttfile://user 开头

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file-system-manager-write-file) / [本地体验路径](file-system-manager-write-file)
