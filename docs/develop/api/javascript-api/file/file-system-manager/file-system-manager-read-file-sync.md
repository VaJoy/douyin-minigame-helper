---
title: "FileSystemManager.readFileSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-read-file-sync
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.readFileSync(filePath, encoding)
```
基础库 1.15.0 开始支持本方法，这是一个**同步**方法。
读取本地文件内容。

## 示例代码
```js
const fileSystemManager = tt.getFileSystemManager();

tt.chooseImage({
  success(res) {
    try {
      const data = fileSystemManager.readFileSync(res.tempFilePaths[0]);
      console.log("调用成功", data);
    } catch (err) {
      console.log("调用失败", err);
    }
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| filePath | string | 是 |  | 1.15.0 | 要读取的文件的路径 |
| encoding | string | 否 |  | 1.15.0 | 指定读取文件的字符编码，如果不传 encoding，则以 ArrayBuffer 格式读取文件的二进制内容  ### 合法值如下：  \|  \|  \|  \| \| --- \| --- \| --- \| \| 值 \| 说明 \| 最低支持版本 \| \| ascii \| - \| 1.15.0 \| \| base64 \| - \| 1.15.0 \| \| binary \| - \| 1.15.0 \| \| hex \| - \| 1.15.0 \| \| ucs2 \| 以小端序读取 \| 1.15.0 \| \| ucs-2 \| 以小端序读取 \| 1.15.0 \| \| utf16le \| 以小端序读取 \| 1.15.0 \| \| utf-16le \| 以小端序读取 \| 1.15.0 \| \| utf-8 \| - \| 1.15.0 \| \| utf8 \| - \| 1.15.0 \| \| latin1 \| - \| 1.15.0 \| |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | string | 文件内容, 根据 encoding 设置不同返回 string 或 ArrayBuffer 类型 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 21101 | permission denied, $apiName $filePath |  |  |
| 21103 | no such file or directory, $apiName $filePath |  |  |
| 21102 | operation not permitted, $apiName $filePath |  |  |
| 10401 | error stack |  |  |
| 20000 | params $paramName is required |  |  |
| 20000 | params $paramName type is not $paramType type |  |  |
| 20000 | $paramName is invalid |  |  |
| 20000 | internal error |  |  |

## 注意事项
readFileSync 可以用于 用户目录(ttfile://user) 临时目录(ttfile://temp) 以及 包内目录(访问包内目录不需要加额外协议头)

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-read-file-sync) / [本地体验路径](file-system-manager-read-file-sync)
