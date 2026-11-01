---
title: "FileSystemManager.readFile"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-read-file
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.readFile(encoding, filePath)
```
基础库 1.15.0 开始支持本方法，这是一个**异步**方法。
读取本地文件内容。

## 示例代码
```js
const fileSystemManager = tt.getFileSystemManager();

tt.chooseImage({
  success(res) {
    readFile(res.tempFilePaths[0]);
  },
});

function readFile(filePath) {
  fileSystemManager.readFile({
    filePath,
    success(res) {
      // 输出读取的文件内容
      console.log(res.data);
    },
    fail(res) {
      console.log("调用失败", res.errMsg);
    },
  });
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| encoding | number | 否 |  | 1.15.0 | 指定读取文件的字符编码，如果不传 encoding，则以 ArrayBuffer 格式读取文件的二进制内容  **可选值：** utf-8=-；ascii=-；base64=-；binary=-；hex=-；ucs2=以小端序读取；ucs-2=以小端序读取；utf16le=以小端序读取；utf-16le=以小端序读取；utf8=-；latin1=- |
| filePath | string | 是 |  | 1.15.0 | 要读取的文件的路径 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **data**（string）：数据。string 或 ArrayBuffer 类型 - **errMsg**（string）："FileSystemManager.readFile:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.readFile:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 10401 | error stack |  |  |
| 21101 | permission denied, $apiName $filePath |  |  |
| 21102 | operation not permitted, $apiName $filePath |  |  |
| 21103 | no such file or directory, $apiName $filePath |  |  |
| 20000 | params $paramName is required |  |  |
| 20000 | params $paramName type is not $paramType type |  |  |
| 20000 | $paramName is invalid |  |  |
| 20000 | internal error |  |  |

## 注意事项
readFile 可以用于 用户目录(ttfile://user) 临时目录(ttfile://temp) 以及 包内目录(访问包内目录不需要加额外协议头)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-read-file) / [本地体验路径](file-system-manager-read-file)
