---
title: "FileSystemManager.copyFileSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-copy-file-sync
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.copyFileSync(srcPath, destPath)
```
基础库 1.15.0 开始支持本方法，这是一个**同步**方法。
同步复制文件。

## 示例代码
```js
const fileSystemManager = tt.getFileSystemManager();

// 下载网络资源
tt.downloadFile({
  url:
    "https://s3.pstatp.com/toutiao/resource/developer/static/img/main-logo.8e3a839.png",
  success(res) {
    console.log("下载成功", res.tempFilePath);

    try {
      // 拷贝文件, destPath 目录必须以 `ttfile://user` 开头
      fileSystemManager.copyFileSync(
        res.tempFilePath,
        `ttfile://user/logo.png`
      );
      console.log("拷贝成功");
    } catch (err) {
      console.log("拷贝失败", err);
    }
  },
  fail(res) {
    console.log("下载失败", res.errMsg);
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| srcPath | string | 是 |  | 1.15.0 | 源文件地址 |
| destPath | string | 是 |  | 1.15.0 | 目标文件地址，必须以 ttfile://user 开头 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 10401 | error stack |  |  |
| 21101 | permission denied, $apiName $srcPath -> $destPath |  |  |
| 21102 | operation not permitted, $apiName $srcPath |  |  |
| 21103 | no such file or directory, $apiName $srcPath -> $destPath |  |  |
| 21104 | user dir saved file size limit exceeded |  |  |
| 20000 | params $paramName is required |  |  |
| 20000 | params $paramName type is not $paramType type |  |  |
| 20000 | $paramName is invalid |  |  |
| 21105 | operation failed |  |  |
| 20001 | invalid param |  |  |
| 20000 | internal error |  |  |

## 注意事项
destPath 必须以 ttfile://user 开头。

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-copy-file-sync) / [本地体验路径](file-system-manager-copy-file-sync)
