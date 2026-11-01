---
title: "FileSystemManager.ftruncateSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/filesystemmanager-ftruncatesync
update_time: 2025-06-27
---

## 语法

```js
FileSystemManager.ftruncateSync(params)
```
基础库 3.74.0 开始支持本方法，这是一个**同步**方法。
对文件内容进行截断操作

## 示例代码
```js
try {
  const fs = tt.getFileSystemManager();
  const fd = fs.openSync({
    filePath,
    flag: "w+",
  });
  fs.ftruncateSync({
    fd,
    length: 1,
  });
  console.log("文件同步截断成功");
} catch (err) {
  console.error("文件同步截断失败", err);
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| params | Object | 是 |  | 3.74.0 | 接口参数  **对象字段** - **length**（number）：截断位置，默认0。如果 length 小于文件长度（单位：字节），则只有前面 length 个字节会保留在文件中，其余内容会被删除；如果 length 大于文件长度，则会对其进行扩展，并且扩展部分将填充空字节（'\0'） - **fd**（string）：文件描述符。fd 通过 FileSystemManager.open 或 FileSystemManager.openSync 接口获得 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 21100 | bad file descriptor |  |  |
| 21101 | Path permission denied |  |  |
| 21102 | system error |  |  |
| 21103 | the maximum size of the file storage limit is exceeded |  |  |
| 21104 | illegal operation on a directory |  |  |
| 21105 | invalid fd |  |  |
| 21106 | value of length is out of range |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/file-system-manager-ftruncate-sync) / [本地体验路径](file-system-manager-ftruncate-sync)
