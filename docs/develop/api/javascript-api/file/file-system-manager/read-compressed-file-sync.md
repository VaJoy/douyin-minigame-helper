---
title: "FileSystemManager.readCompressedFileSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/read-compressed-file-sync
update_time: 2025-06-27
---

## 语法

```js
FileSystemManager.readCompressedFileSync(params)
```
基础库 3.74.0 开始支持本方法，这是一个**同步**方法。
读取指定压缩类型的本地文件内容

## 示例代码
```js
try {
  const fs = tt.getFileSystemManager();
  const res = fs.readCompressedFileSync({
    filePath,
    compressionAlgorithm: "br",
  });
  console.log("压缩文件同步读取成功", res);
} catch (err) {
  console.error("压缩文件同步读取失败", err);
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| params | Object | 是 |  | 3.74.0 | 接口参数  **对象字段** - **filePath**（string）：要读取的文件的路径 (本地用户文件或代码包文件) - **compressionAlgorithm**（number）：文件压缩类型，目前仅支持 'br' |

## 返回值
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| （返回值） | ArrayBuffer | 文件内容 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 21100 | no such file or directory ${path} |  |  |
| 21101 | Path permission denied |  |  |
| 21102 | Is a directory |  |  |
| 21103 | brotli decompress fail |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/file-system-manager-read-compressed-file-sync) / [本地体验路径](file-system-manager-read-compressed-file-sync)
