---
title: "FileSystemManager.fstat"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/filesystemmanager-fstat
update_time: 2025-06-27
---

## 语法

```js
FileSystemManager.fstat(fd)
```
基础库 3.74.0 开始支持本方法，这是一个**异步**方法。
获取文件的状态信息

## 示例代码
```js
const fs = tt.getFileSystemManager();
const fd = fs.openSync({
  filePath,
  flag: "r",
});
fs.fstat({
  fd,
  success: (res) => {
    console.log('文件状态获取成功', res);
  },
  fail: (err) => {
    console.error('文件状态获取失败', err);
  }
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| fd | string | 是 |  | 3.74.0 | 文件描述符。fd 通过 FileSystemManager.open 或 FileSystemManager.openSync 接口获得 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.fstat:ok" - **Stats**（Object）：[Stats](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/stats/stats) 对象，包含了文件的状态信息 |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.fstat:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 21100 | bad file descriptor |  |  |
| 21101 | invalid fd |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/foundation/file-system-manager-fstat) / [本地体验路径](file-system-manager-fstat)
