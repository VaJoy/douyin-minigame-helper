---
title: "FileSystemManager.closeSync"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/filesystem-close-sync
update_time: 2025-06-27
---

## 语法

```js
FileSystemManager.closeSync(params)
```
基础库 3.74.0 开始支持本方法，这是一个**同步**方法。
关闭文件

## 示例代码
```js
try {
  const fs = tt.getFileSystemManager();
  fs.closeSync({
    fd,
  });
} catch (err) {
  console.error("文件关闭失败", err);
}
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| params | Object | 是 |  | 3.74.0 | 接口参数  **对象字段** - **fd**（string）：需要被关闭的文件描述符。fd 通过 FileSystemManager.open 或 FileSystemManager.openSync 接口获得 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 21100 | bad file descriptor |  |  |
| 21101 | system error |  |  |
| 21102 | invalid fd |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/file-system-manager-close-sync) / [本地体验路径](file-system-manager-close-sync)
