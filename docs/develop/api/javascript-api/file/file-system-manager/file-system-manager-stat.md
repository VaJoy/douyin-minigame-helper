---
title: "FileSystemManager.stat"
source: https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/javascript-api/file/file-system-manager/file-system-manager-stat
update_time: 2025-06-05
---

const fileSystemManager = tt.getFileSystemManager();
tt.chooseImage({
success(res) {
const tempFile = res.tempFilePaths[0];
fileSystemManager.stat({
path: tempFile,
success(res) {
console.log("是否是目录:", res.stat.isDirectory());
console.log("是否是文件:", res.stat.isFile());
},
fail(res) {
console.log("调用失败", res.errMsg);
},
});
},
});

const fileSystemManager = tt.getFileSystemManager();
fs.stat({
path: `ttfile://user`,
recursive: true,
success: (res) => {
if (Array.isArray(res.stats)) {
res.stats.forEach(({ path, stat }) => {
console.log(path, stat.isDirectory());
});
} else {
console.log(res.stats.isDirectory());
}
},
});

FileSystemManager.stat(options)

## 语法

```js
FileSystemManager.stat(recursive, path)
```
基础库 1.15.0 开始支持本方法，这是一个**异步**方法。
获取文件 Stats 对象。

## 示例代码

【代码示例 1】查询单一文件 stat：

```js
const fileSystemManager = tt.getFileSystemManager();
tt.chooseImage({
  success(res) {
    const tempFile = res.tempFilePaths[0];
    fileSystemManager.stat({
      path: tempFile,
      success(res) {
        console.log("是否是目录:", res.stat.isDirectory());
        console.log("是否是文件:", res.stat.isFile());
      },
      fail(res) {
        console.log("调用失败", res.errMsg);
      },
    });
  },
});
```

【代码示例 2】递归查询用户目录 stat：

```js
const fileSystemManager = tt.getFileSystemManager();
fs.stat({
  path: `ttfile://user`,
  recursive: true,
  success: (res) => {
    if (Array.isArray(res.stats)) {
      res.stats.forEach(({ path, stat }) => {
        console.log(path, stat.isDirectory());
      });
    } else {
      console.log(res.stats.isDirectory());
    }
  },
});
```

## 参数
| 属性名 | 类型 | 必填 | 默认值 | 最低版本 | 说明 |
| --- | --- | --- | --- | --- | --- |
| recursive | boolean | 否 | false | 3.1.0 | 是否递归获取目录下每个文件的 stat 信息 |
| path | string | 是 |  | 1.15.0 | 文件/目录路径 |

## 回调：成功回调
调用成功时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **stats**（Array<Object>）：Array<StatItem> \| [Stats](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/stats/stats)  当查询结果是多个时，为数组类型；当结果唯一时，为 [Stats](https://developer.open-douyin.com/docs/resource/zh-CN/mini-game/develop/api/file/stats/stats) 对象类型 - **errMsg**（string）："FileSystemManager.stat:ok" |

## 回调：失败回调
调用失败时的回调函数
| 属性名 | 类型 | 说明 |
| --- | --- | --- |
| res | Object | object 类型，属性如下：  **对象字段** - **errMsg**（string）："FileSystemManager.stat:fail" + 详细错误信息 |

## 错误码
| 错误码 | 错误信息 | 处理建议 | 版本 |
| --- | --- | --- | --- |
| 20001 | invalid param |  |  |
| 10401 | error stack |  |  |
| 21101 | permission denied, $apiName $dirPath |  |  |
| 21102 | no such file or directory, $apiName $dirPath |  |  |
| 20000 | internal error |  |  |

## 授权要求
无需开发者授权；无需用户授权

## 支持平台
iOS、Android

## 相关链接
[体验链接](https://developer.open-douyin.com/docs/resource/ideCodeLink?path=/zh-CN/mini-game/develop/api/file/file-system-manager/file-system-manager-stat) / [本地体验路径](file-system-manager-stat)