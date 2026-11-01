---
title: "FileSystemManager.truncateSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-truncate-sync
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.truncateSync(filePath, length)
```
基础库 3.1.0 开始支持本方法，这是一个**同步**方法。
对文件内容进行截断操作，只有用户目录ttfile://user下的文件可以截断。

## 示例代码
```js
const fs = tt.getFileSystemManager();

fs.truncate({
  filePath: `ttfile://user/example.txt`,
  length: 10,
  success(res) {
    console.log(res)
  },
  fail(res) {
    console.error(res)
  },
});

// 同步接口
try {
  fs.truncateSync(`ttfile://user/example.txt`, 10);
} catch (e) {
  console.error(e);
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| filePath | string | 是 |  | 3.1.0 | 要截断的文件路径，必须是用户目录，以 ttfile://user 开头 |
| length | number | 否 | 0 | 3.1.0 | 截断长度，要求是自然数。若 length < 文件长度（字节），则前 length 个字节内容会保留在文件中，其余内容删除；若 length > 文件长度，则会对文件进行扩展，扩展部分将填充空字节 '\0' |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10401 | inetrnal error |  |  |
| 21101 | permission denied, %s%s |  |  |
| 21102 | no such file or directory, %s%s |  |  |
| 21103 | user dir saved file size limit exceeded |  |  |
| 21104 | operation not permitted, %s%s |  |  |
| 20000 | internal error |  |  |
| 20001 | invalid param |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file-system-manager-truncate-sync) / [本地体验路径](file-system-manager-truncate-sync)
