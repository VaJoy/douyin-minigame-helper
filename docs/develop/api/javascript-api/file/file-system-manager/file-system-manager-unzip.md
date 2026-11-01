---
title: "FileSystemManager.unzip"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-unzip
update_time: 2024-07-24
---

## 语法

```js
FileSystemManager.unzip(zipFilePath, targetPath)
```
基础库 1.15.0 开始支持本方法，这是一个**异步**方法。
解压文件。

## 示例代码
```js
const fileSystemManager = tt.getFileSystemManager();

// 下载一个 zip 文件
tt.downloadFile({
  url: "https://sf1-cdn-tos.douyinstatic.com/obj/microapp/frontend/docs/images/test-4423286930445687.zip",
  success(res) {
    console.log("下载 zip 成功", res.tempFilePath);
    // 解压 zip 文件
    unzip(res.tempFilePath);
  },
  fail(res) {
    console.log("下载 zip 失败", res.errMsg);
  },
});

function unzip(zipFilePath) {
  const targetPath = `ttfile://user/abc`;

  fileSystemManager.unzip({
    zipFilePath,
    targetPath,
    success(_res) {
      console.log("解压成功");
      const concent = fs.readdirSync(targetPath);
      // 输出 zip 内文件内容
      console.log("压缩包内文件:", concent);
    },
    fail(res) {
      console.log("解压失败", res.errMsg);
    },
  });
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| zipFilePath | string | 是 |  | 1.15.0 | 源文件路径，只可以是 zip 压缩文件 |
| targetPath | string | 是 |  | 1.15.0 | 目标目录路径, 必须以 ttfile://user 开头 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.unzip:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.unzip:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 10401 | error stack |  |  |
| 21101 | permission denied, $apiName $dirPath |  |  |
| 21103 | no such file or directory, $apiName $dirPath |  |  |
| 21104 | user dir saved file size limit exceeded |  |  |
| 21102 | operation not permitted, $apiName $filePath |  |  |
| 20000 | internal error |  |  |

## 使用限制
由于开发者只有在 用户目录(ttfile://user) 才有写的权限, 因此 targetPath 必须以 ttfile://user 开头

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file-system-manager-unzip) / [本地体验路径](file-system-manager-unzip)
